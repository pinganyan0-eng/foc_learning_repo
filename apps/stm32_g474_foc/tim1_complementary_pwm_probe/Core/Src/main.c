#include "main.h"

#define TIM1_INPUT_CLOCK_HZ       170000000UL
#define PWM_TEST_FREQUENCY_HZ         10000UL
#define PWM_TEST_DUTY_PERCENT             25UL
#define PWM_TEST_PERIOD_COUNTS \
  (TIM1_INPUT_CLOCK_HZ / (2UL * PWM_TEST_FREQUENCY_HZ))
#define PWM_TEST_ARR              (PWM_TEST_PERIOD_COUNTS - 1UL)
#define PWM_TEST_CCR \
  ((PWM_TEST_PERIOD_COUNTS * PWM_TEST_DUTY_PERCENT) / 100UL)

/*
 * DTG 0xCA selects (32 + 10) * 8 timer ticks.
 * At 170 MHz this is 336 ticks, approximately 1.976 us.
 */
#define PWM_TEST_DEADTIME_DTG              0xCAUL

#define PWM_OUTPUTS_PORT_A \
  (GPIO_PIN_7 | GPIO_PIN_8 | GPIO_PIN_9 | GPIO_PIN_10)
#define PWM_OUTPUTS_PORT_B \
  (GPIO_PIN_14 | GPIO_PIN_15)
#define PWM_BREAK_PIN                       GPIO_PIN_12
#define USER_BUTTON_PIN                     GPIO_PIN_13
#define STATUS_LED_PIN                       GPIO_PIN_5

typedef enum
{
  PWM_STATE_DISARMED = 0,
  PWM_STATE_ARMED,
  PWM_STATE_STOPPED,
  PWM_STATE_BREAK_LATCHED
} pwm_state_t;

static volatile pwm_state_t g_pwm_state = PWM_STATE_DISARMED;

static void SystemClock_Config(void);
static void MX_SafeGPIO_Init(void);
static void MX_TIM1_ComplementaryPWM_Init(void);
static void PWM_ConfigureAlternatePins(void);
static void PWM_Arm(void);
static void PWM_StopAndLatch(pwm_state_t next_state);
static void Button_Poll(void);

int main(void)
{
  HAL_Init();
  SystemClock_Config();
  MX_SafeGPIO_Init();
  MX_TIM1_ComplementaryPWM_Init();
  PWM_ConfigureAlternatePins();

  while (1)
  {
    Button_Poll();
    __WFI();
  }
}

void HAL_MspInit(void)
{
  __HAL_RCC_SYSCFG_CLK_ENABLE();
  __HAL_RCC_PWR_CLK_ENABLE();
  HAL_PWREx_DisableUCPDDeadBattery();
}

static void MX_SafeGPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();
  __HAL_RCC_GPIOC_CLK_ENABLE();

  HAL_GPIO_WritePin(GPIOA, PWM_OUTPUTS_PORT_A | STATUS_LED_PIN, GPIO_PIN_RESET);
  HAL_GPIO_WritePin(GPIOB, PWM_OUTPUTS_PORT_B, GPIO_PIN_RESET);

  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_PULLDOWN;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  GPIO_InitStruct.Pin = PWM_OUTPUTS_PORT_A | STATUS_LED_PIN;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  GPIO_InitStruct.Pin = PWM_OUTPUTS_PORT_B;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  GPIO_InitStruct.Pin = USER_BUTTON_PIN;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

  GPIO_InitStruct.Pin = PWM_BREAK_PIN;
  GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_HIGH;
  GPIO_InitStruct.Alternate = GPIO_AF6_TIM1;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);
}

static void MX_TIM1_ComplementaryPWM_Init(void)
{
  __HAL_RCC_TIM1_CLK_ENABLE();
  __HAL_DBGMCU_FREEZE_TIM1();

  TIM1->CR1 = 0U;
  TIM1->CR2 = 0U;
  TIM1->SMCR = 0U;
  TIM1->DIER = 0U;
  TIM1->CCER = 0U;
  TIM1->BDTR = 0U;
  TIM1->AF1 = TIM1_AF1_BKINE;
  TIM1->AF2 = 0U;

  TIM1->PSC = 0U;
  TIM1->ARR = PWM_TEST_ARR;
  TIM1->RCR = 0U;
  TIM1->CCR1 = PWM_TEST_CCR;
  TIM1->CCR2 = PWM_TEST_CCR;
  TIM1->CCR3 = PWM_TEST_CCR;

  TIM1->CCMR1 = TIM_CCMR1_OC1PE |
                 TIM_CCMR1_OC1M_1 | TIM_CCMR1_OC1M_2 |
                 TIM_CCMR1_OC2PE |
                 TIM_CCMR1_OC2M_1 | TIM_CCMR1_OC2M_2;
  TIM1->CCMR2 = TIM_CCMR2_OC3PE |
                 TIM_CCMR2_OC3M_1 | TIM_CCMR2_OC3M_2;

  TIM1->CCER = TIM_CCER_CC1E | TIM_CCER_CC1NE |
               TIM_CCER_CC2E | TIM_CCER_CC2NE |
               TIM_CCER_CC3E | TIM_CCER_CC3NE;

  /*
   * OISx/OISxN and all output polarity bits remain clear: inactive state is
   * low. BKP remains clear, so BKIN is active low. AOE remains clear, so a
   * break event cannot automatically restore MOE.
   */
  TIM1->BDTR = PWM_TEST_DEADTIME_DTG |
               TIM_BDTR_OSSI |
               TIM_BDTR_OSSR |
               TIM_BDTR_BKE;

  TIM1->CR1 = TIM_CR1_CMS_0 |
              TIM_CR1_CMS_1 |
              TIM_CR1_ARPE;

  TIM1->EGR = TIM_EGR_UG;
  TIM1->SR = 0U;
  TIM1->DIER = TIM_DIER_BIE;

  HAL_NVIC_SetPriority(TIM1_BRK_TIM15_IRQn, 1U, 0U);
  HAL_NVIC_EnableIRQ(TIM1_BRK_TIM15_IRQn);

  /*
   * The counter may run while disarmed, but MOE stays clear until the user
   * explicitly presses B1. No PWM pin can become active from this statement.
   */
  TIM1->CR1 |= TIM_CR1_CEN;
}

static void PWM_ConfigureAlternatePins(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
  GPIO_InitStruct.Pull = GPIO_PULLDOWN;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_HIGH;

  GPIO_InitStruct.Pin = PWM_OUTPUTS_PORT_A;
  GPIO_InitStruct.Alternate = GPIO_AF6_TIM1;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  GPIO_InitStruct.Pin = GPIO_PIN_14;
  GPIO_InitStruct.Alternate = GPIO_AF6_TIM1;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  GPIO_InitStruct.Pin = GPIO_PIN_15;
  GPIO_InitStruct.Alternate = GPIO_AF4_TIM1;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);
}

static void PWM_Arm(void)
{
  uint32_t primask;

  if (g_pwm_state != PWM_STATE_DISARMED)
  {
    return;
  }

  primask = __get_PRIMASK();
  __disable_irq();

  if (((GPIOB->IDR & PWM_BREAK_PIN) != 0U) &&
      ((TIM1->SR & TIM_SR_BIF) == 0U) &&
      (g_pwm_state == PWM_STATE_DISARMED))
  {
    TIM1->BDTR |= TIM_BDTR_MOE;
    g_pwm_state = PWM_STATE_ARMED;
    GPIOA->BSRR = STATUS_LED_PIN;
  }
  else
  {
    PWM_StopAndLatch(PWM_STATE_BREAK_LATCHED);
  }

  if (primask == 0U)
  {
    __enable_irq();
  }
}

static void PWM_StopAndLatch(pwm_state_t next_state)
{
  TIM1->BDTR &= ~TIM_BDTR_MOE;
  g_pwm_state = next_state;
  GPIOA->BRR = STATUS_LED_PIN;
}

static void Button_Poll(void)
{
  static uint32_t last_sample_tick = 0U;
  static uint32_t last_event_tick = 0U;
  static GPIO_PinState last_state = GPIO_PIN_RESET;
  static uint8_t initialized = 0U;
  uint32_t now = HAL_GetTick();
  GPIO_PinState state;

  if ((now - last_sample_tick) < 10U)
  {
    return;
  }

  last_sample_tick = now;
  state = HAL_GPIO_ReadPin(GPIOC, USER_BUTTON_PIN);

  if (initialized == 0U)
  {
    last_state = state;
    initialized = 1U;
    return;
  }

  if ((last_state == GPIO_PIN_RESET) &&
      (state == GPIO_PIN_SET) &&
      ((now - last_event_tick) >= 50U))
  {
    last_event_tick = now;

    if (g_pwm_state == PWM_STATE_DISARMED)
    {
      PWM_Arm();
    }
    else if (g_pwm_state == PWM_STATE_ARMED)
    {
      PWM_StopAndLatch(PWM_STATE_STOPPED);
    }
    else
    {
      /* STOPPED and BREAK_LATCHED require a reset before another arm. */
    }
  }

  last_state = state;
}

void TIM1_BRK_TIM15_IRQHandler(void)
{
  if ((TIM1->SR & TIM_SR_BIF) != 0U)
  {
    PWM_StopAndLatch(PWM_STATE_BREAK_LATCHED);
    TIM1->DIER &= ~TIM_DIER_BIE;
    TIM1->SR = ~TIM_SR_BIF;
  }
}

void SysTick_Handler(void)
{
  HAL_IncTick();
}

static void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  HAL_PWREx_ControlVoltageScaling(PWR_REGULATOR_VOLTAGE_SCALE1_BOOST);

  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLM = RCC_PLLM_DIV4;
  RCC_OscInitStruct.PLL.PLLN = 85U;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = RCC_PLLQ_DIV2;
  RCC_OscInitStruct.PLL.PLLR = RCC_PLLR_DIV2;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_SYSCLK |
                                RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_4) != HAL_OK)
  {
    Error_Handler();
  }
}

void Error_Handler(void)
{
  __disable_irq();
  TIM1->BDTR &= ~TIM_BDTR_MOE;
  GPIOA->BRR = STATUS_LED_PIN;

  while (1)
  {
  }
}
