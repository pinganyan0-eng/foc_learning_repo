#include "main.h"

typedef struct
{
  GPIO_TypeDef *port;
  uint16_t pin;
  uint16_t half_period_ticks;
  uint16_t ticks;
} probe_channel_t;

static void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_TIM6_20kHz_Init(void);
static void Probe_AllLow(void);

static volatile probe_channel_t g_probe_channels[] =
{
  {GPIOA, GPIO_PIN_15, 200U, 0U}, /* CN8 P1 HIN1, about 50 Hz */
  {GPIOB, GPIO_PIN_3,  100U, 0U}, /* CN8 P2 LIN1, about 100 Hz */
  {GPIOB, GPIO_PIN_10,  50U, 0U}, /* CN8 P3 HIN2, about 200 Hz */
  {GPIOA, GPIO_PIN_8,   25U, 0U}, /* CN8 P4 LIN2, about 400 Hz */
  {GPIOA, GPIO_PIN_9,   10U, 0U}, /* CN8 P5 HIN3, about 1 kHz */
  {GPIOA, GPIO_PIN_10,   5U, 0U}, /* CN8 P6 LIN3, about 2 kHz */
};

int main(void)
{
  HAL_Init();
  SystemClock_Config();
  MX_GPIO_Init();
  Probe_AllLow();
  MX_TIM6_20kHz_Init();

  while (1)
  {
    __WFI();
  }
}

void HAL_MspInit(void)
{
  __HAL_RCC_SYSCFG_CLK_ENABLE();
  __HAL_RCC_PWR_CLK_ENABLE();
  HAL_PWREx_DisableUCPDDeadBattery();
}

static void Probe_AllLow(void)
{
  HAL_GPIO_WritePin(GPIOA, GPIO_PIN_8 | GPIO_PIN_9 | GPIO_PIN_10 | GPIO_PIN_15, GPIO_PIN_RESET);
  HAL_GPIO_WritePin(GPIOB, GPIO_PIN_3 | GPIO_PIN_10, GPIO_PIN_RESET);
}

static void MX_TIM6_20kHz_Init(void)
{
  __HAL_RCC_TIM6_CLK_ENABLE();

  TIM6->CR1 = 0U;
  TIM6->PSC = 169U;
  TIM6->ARR = 49U;
  TIM6->EGR = TIM_EGR_UG;
  TIM6->SR = 0U;
  TIM6->DIER = TIM_DIER_UIE;

  HAL_NVIC_SetPriority(TIM6_DAC_IRQn, 3U, 0U);
  HAL_NVIC_EnableIRQ(TIM6_DAC_IRQn);

  TIM6->CR1 = TIM_CR1_CEN;
}

static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  Probe_AllLow();

  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;

  GPIO_InitStruct.Pin = GPIO_PIN_8 | GPIO_PIN_9 | GPIO_PIN_10 | GPIO_PIN_15;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  GPIO_InitStruct.Pin = GPIO_PIN_3 | GPIO_PIN_10;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);
}

void TIM6_DAC_IRQHandler(void)
{
  if ((TIM6->SR & TIM_SR_UIF) != 0U)
  {
    TIM6->SR &= ~TIM_SR_UIF;

    for (uint32_t i = 0U; i < (sizeof(g_probe_channels) / sizeof(g_probe_channels[0])); i++)
    {
      probe_channel_t *channel = (probe_channel_t *)&g_probe_channels[i];
      channel->ticks++;

      if (channel->ticks >= channel->half_period_ticks)
      {
        channel->ticks = 0U;
        HAL_GPIO_TogglePin(channel->port, channel->pin);
      }
    }
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
  Probe_AllLow();

  while (1)
  {
  }
}
