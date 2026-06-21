#include "gate_waveform_candidate.h"

#include "stm32g4xx.h"

#define GATE_WAVEFORM_PA_MASK ((uint32_t)((1u << 8) | (1u << 9) | (1u << 10)))
#define GATE_WAVEFORM_PB_MASK ((uint32_t)((1u << 13) | (1u << 14) | (1u << 15)))
#define GATE_WAVEFORM_NFAULT_PIN 12u
#define GATE_WAVEFORM_AF_TIM1 6u

#define TIM1_PSC_FOR_1MHZ \
  ((GATE_WAVEFORM_CANDIDATE_TIMER_HZ / GATE_WAVEFORM_CANDIDATE_TIMER_TICK_HZ) - 1u)
#define TIM1_ARR_FOR_PWM \
  ((GATE_WAVEFORM_CANDIDATE_TIMER_TICK_HZ / GATE_WAVEFORM_CANDIDATE_PWM_HZ) - 1u)
#define TIM1_CCR_FOR_DUTY \
  (((TIM1_ARR_FOR_PWM + 1u) * GATE_WAVEFORM_CANDIDATE_DUTY_PERMILLE) / 1000u)

static bool s_fault_latched;

static void enable_gpio_and_tim1_clocks(void)
{
  RCC->AHB2ENR |= RCC_AHB2ENR_GPIOAEN | RCC_AHB2ENR_GPIOBEN;
  RCC->APB2ENR |= RCC_APB2ENR_TIM1EN;
  (void)RCC->AHB2ENR;
  (void)RCC->APB2ENR;
}

static void configure_pin_as_output_low(GPIO_TypeDef *port, uint32_t pin)
{
  const uint32_t mode_shift = pin * 2u;
  const uint32_t mode_mask = 3u << mode_shift;
  const uint32_t pin_mask = 1u << pin;

  port->BSRR = pin_mask << 16u;
  port->MODER = (port->MODER & ~mode_mask) | (1u << mode_shift);
  port->OTYPER &= ~pin_mask;
  port->OSPEEDR &= ~mode_mask;
  port->PUPDR &= ~mode_mask;
}

static void configure_pin_as_input(GPIO_TypeDef *port, uint32_t pin)
{
  const uint32_t mode_shift = pin * 2u;
  const uint32_t mode_mask = 3u << mode_shift;

  port->MODER &= ~mode_mask;
  port->PUPDR &= ~mode_mask;
}

static void configure_pin_as_tim1_af(GPIO_TypeDef *port, uint32_t pin)
{
  const uint32_t mode_shift = pin * 2u;
  const uint32_t mode_mask = 3u << mode_shift;
  const uint32_t afr_shift = (pin & 7u) * 4u;
  const uint32_t afr_mask = 15u << afr_shift;
  const uint32_t afr_index = pin >> 3u;
  const uint32_t pin_mask = 1u << pin;

  port->BSRR = pin_mask << 16u;
  port->AFR[afr_index] =
      (port->AFR[afr_index] & ~afr_mask) | (GATE_WAVEFORM_AF_TIM1 << afr_shift);
  port->OTYPER &= ~pin_mask;
  port->OSPEEDR = (port->OSPEEDR & ~mode_mask) | (2u << mode_shift);
  port->PUPDR &= ~mode_mask;
  port->MODER = (port->MODER & ~mode_mask) | (2u << mode_shift);
}

static void force_candidate_pins_low(void)
{
  GPIOA->BSRR = GATE_WAVEFORM_PA_MASK << 16u;
  GPIOB->BSRR = GATE_WAVEFORM_PB_MASK << 16u;

  configure_pin_as_output_low(GPIOA, 8u);
  configure_pin_as_output_low(GPIOA, 9u);
  configure_pin_as_output_low(GPIOA, 10u);
  configure_pin_as_output_low(GPIOB, 13u);
  configure_pin_as_output_low(GPIOB, 14u);
  configure_pin_as_output_low(GPIOB, 15u);
}

static void configure_fault_input(void)
{
  configure_pin_as_input(GPIOB, GATE_WAVEFORM_NFAULT_PIN);
}

static void lock_tim1_outputs(void)
{
  TIM1->CR1 = 0u;
  TIM1->DIER = 0u;
  TIM1->CCER = 0u;
  TIM1->BDTR = (TIM1->BDTR & ~(TIM_BDTR_MOE | TIM_BDTR_AOE)) | TIM_BDTR_BKE;
}

static void disable_tim1_outputs_keep_counter(void)
{
  TIM1->CCER = 0u;
  TIM1->BDTR = (TIM1->BDTR & ~(TIM_BDTR_MOE | TIM_BDTR_AOE)) |
               TIM_BDTR_BKE | GATE_WAVEFORM_CANDIDATE_DEADTIME_DTG;
}

static void configure_tim1_for_candidate_window(void)
{
  TIM1->CR1 = 0u;
  TIM1->DIER = 0u;
  TIM1->CCER = 0u;
  TIM1->BDTR = TIM_BDTR_BKE | GATE_WAVEFORM_CANDIDATE_DEADTIME_DTG;
  TIM1->PSC = TIM1_PSC_FOR_1MHZ;
  TIM1->ARR = TIM1_ARR_FOR_PWM;
  TIM1->CCR1 = TIM1_CCR_FOR_DUTY;
  TIM1->CCR2 = TIM1_CCR_FOR_DUTY;
  TIM1->CCR3 = TIM1_CCR_FOR_DUTY;
  TIM1->CCMR1 = TIM_CCMR1_OC1PE | TIM_CCMR1_OC1M_1 | TIM_CCMR1_OC1M_2 |
                TIM_CCMR1_OC2PE | TIM_CCMR1_OC2M_1 | TIM_CCMR1_OC2M_2;
  TIM1->CCMR2 = TIM_CCMR2_OC3PE | TIM_CCMR2_OC3M_1 | TIM_CCMR2_OC3M_2;
  TIM1->EGR = TIM_EGR_UG;
  TIM1->SR = 0u;
}

static void configure_candidate_pins_for_timer(void)
{
  configure_pin_as_tim1_af(GPIOA, 8u);
  configure_pin_as_tim1_af(GPIOA, 9u);
  configure_pin_as_tim1_af(GPIOA, 10u);
  configure_pin_as_tim1_af(GPIOB, 13u);
  configure_pin_as_tim1_af(GPIOB, 14u);
  configure_pin_as_tim1_af(GPIOB, 15u);
}

static bool read_nfault_high(void)
{
  return (GPIOB->IDR & (1u << GATE_WAVEFORM_NFAULT_PIN)) != 0u;
}

static bool wait_for_pwm_periods_or_fault(uint32_t periods)
{
  for (uint32_t i = 0u; i < periods; ++i)
  {
    while ((TIM1->SR & TIM_SR_UIF) == 0u)
    {
    }
    TIM1->SR = (uint32_t)~TIM_SR_UIF;

    if (!read_nfault_high())
    {
      s_fault_latched = true;
      disable_tim1_outputs_keep_counter();
      force_candidate_pins_low();
      return false;
    }
  }

  return true;
}

static void arm_candidate_outputs(void)
{
  TIM1->BDTR = TIM_BDTR_BKE | GATE_WAVEFORM_CANDIDATE_DEADTIME_DTG | TIM_BDTR_MOE;
  TIM1->CCER = TIM_CCER_CC1E | TIM_CCER_CC1NE |
               TIM_CCER_CC2E | TIM_CCER_CC2NE |
               TIM_CCER_CC3E | TIM_CCER_CC3NE;
}

gate_waveform_candidate_config_t gate_waveform_candidate_get_config(void)
{
  const gate_waveform_candidate_config_t config = {
    .timer_hz = GATE_WAVEFORM_CANDIDATE_TIMER_HZ,
    .timer_tick_hz = GATE_WAVEFORM_CANDIDATE_TIMER_TICK_HZ,
    .pwm_hz = GATE_WAVEFORM_CANDIDATE_PWM_HZ,
    .duty_permille = GATE_WAVEFORM_CANDIDATE_DUTY_PERMILLE,
    .window_periods = GATE_WAVEFORM_CANDIDATE_WINDOW_PERIODS,
    .pre_idle_periods = GATE_WAVEFORM_CANDIDATE_PRE_IDLE_PERIODS,
    .post_idle_periods = GATE_WAVEFORM_CANDIDATE_POST_IDLE_PERIODS,
    .deadtime_dtg = GATE_WAVEFORM_CANDIDATE_DEADTIME_DTG,
    .command_ingress_present = false,
  };

  return config;
}

void gate_waveform_candidate_force_idle_low(void)
{
  enable_gpio_and_tim1_clocks();
  lock_tim1_outputs();
  force_candidate_pins_low();
  configure_fault_input();
}

gate_waveform_candidate_state_t gate_waveform_candidate_run_once(void)
{
  s_fault_latched = false;
  gate_waveform_candidate_force_idle_low();
  configure_tim1_for_candidate_window();

  TIM1->CR1 = TIM_CR1_CEN;
  (void)wait_for_pwm_periods_or_fault(GATE_WAVEFORM_CANDIDATE_PRE_IDLE_PERIODS);

  if (s_fault_latched || !read_nfault_high())
  {
    s_fault_latched = true;
  }
  else
  {
    configure_candidate_pins_for_timer();
    arm_candidate_outputs();
    (void)wait_for_pwm_periods_or_fault(GATE_WAVEFORM_CANDIDATE_WINDOW_PERIODS);
  }

  disable_tim1_outputs_keep_counter();
  force_candidate_pins_low();
  (void)wait_for_pwm_periods_or_fault(GATE_WAVEFORM_CANDIDATE_POST_IDLE_PERIODS);
  gate_waveform_candidate_force_idle_low();

  const bool nfault_high = read_nfault_high();
  if (!nfault_high)
  {
    s_fault_latched = true;
  }

  const gate_waveform_candidate_state_t state = {
    .nfault_high = nfault_high,
    .fault_latched = s_fault_latched,
    .window_completed = !s_fault_latched,
    .tim1_outputs_disabled = (TIM1->CCER == 0u),
    .tim1_main_output_disabled = ((TIM1->BDTR & TIM_BDTR_MOE) == 0u),
  };

  return state;
}
