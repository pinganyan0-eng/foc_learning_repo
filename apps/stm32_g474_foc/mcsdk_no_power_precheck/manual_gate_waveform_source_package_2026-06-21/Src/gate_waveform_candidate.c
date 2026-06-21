#include "gate_waveform_candidate.h"

#include "stm32g4xx.h"

#define GATE_WAVEFORM_PA_MASK ((uint32_t)((1u << 7) | (1u << 8) | (1u << 9) | (1u << 10)))
#define GATE_WAVEFORM_PB_MASK ((uint32_t)((1u << 14) | (1u << 15)))
#define GATE_WAVEFORM_NFAULT_PIN 12u

typedef struct
{
  GPIO_TypeDef *high_port;
  uint32_t high_pin;
  GPIO_TypeDef *low_port;
  uint32_t low_pin;
} gate_waveform_vector_t;

static const gate_waveform_vector_t k_rotation_vectors[GATE_WAVEFORM_CANDIDATE_DIAG_VECTOR_COUNT] = {
  {GPIOA, 8u, GPIOB, 14u},
  {GPIOA, 8u, GPIOB, 15u},
  {GPIOA, 9u, GPIOB, 15u},
  {GPIOA, 9u, GPIOA, 7u},
  {GPIOA, 10u, GPIOA, 7u},
  {GPIOA, 10u, GPIOB, 14u},
};

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

static void set_pin_level(GPIO_TypeDef *port, uint32_t pin, bool high)
{
  const uint32_t pin_mask = 1u << pin;

  port->BSRR = high ? pin_mask : (pin_mask << 16u);
}

static void force_candidate_pins_low_keep_lin1_high(void)
{
  GPIOA->BSRR = ((1u << 8) | (1u << 9) | (1u << 10)) << 16u;
  GPIOB->BSRR = GATE_WAVEFORM_PB_MASK << 16u;
  set_pin_level(GPIOA, 7u, true);
}

static void force_candidate_pins_low(void)
{
  GPIOA->BSRR = GATE_WAVEFORM_PA_MASK << 16u;
  GPIOB->BSRR = GATE_WAVEFORM_PB_MASK << 16u;

  configure_pin_as_output_low(GPIOA, 8u);
  configure_pin_as_output_low(GPIOA, 7u);
  configure_pin_as_output_low(GPIOA, 9u);
  configure_pin_as_output_low(GPIOA, 10u);
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

static bool read_nfault_high(void)
{
  return (GPIOB->IDR & (1u << GATE_WAVEFORM_NFAULT_PIN)) != 0u;
}

static bool diagnostic_delay_or_fault(uint32_t loops)
{
  for (volatile uint32_t i = 0u; i < loops; ++i)
  {
    if (((uint32_t)i & 0x3ffu) == 0u && !read_nfault_high())
    {
      s_fault_latched = true;
      force_candidate_pins_low();
      return false;
    }

    __asm volatile ("nop");
  }

  return true;
}

static bool apply_rotation_vector(const gate_waveform_vector_t *vector)
{
  force_candidate_pins_low_keep_lin1_high();

  if (!read_nfault_high())
  {
    s_fault_latched = true;
    force_candidate_pins_low();
    return false;
  }

  set_pin_level(vector->high_port, vector->high_pin, true);
  set_pin_level(vector->low_port, vector->low_pin, true);
  set_pin_level(GPIOA, 7u, true);
  return true;
}

static bool run_rotation_sequence_once(void)
{
  if (!read_nfault_high())
  {
    s_fault_latched = true;
    force_candidate_pins_low();
    return false;
  }

  for (uint32_t i = 0u; i < GATE_WAVEFORM_CANDIDATE_DIAG_VECTOR_COUNT; ++i)
  {
    if (!apply_rotation_vector(&k_rotation_vectors[i]))
    {
      return false;
    }

    if (!diagnostic_delay_or_fault(GATE_WAVEFORM_CANDIDATE_DIAG_STEP_LOOPS))
    {
      return false;
    }

    force_candidate_pins_low_keep_lin1_high();
    if (!diagnostic_delay_or_fault(GATE_WAVEFORM_CANDIDATE_DIAG_INTERSTEP_LOOPS))
    {
      return false;
    }
  }

  force_candidate_pins_low_keep_lin1_high();

  if (!read_nfault_high())
  {
    s_fault_latched = true;
    force_candidate_pins_low();
    return false;
  }

  return true;
}

static bool wake_driver_with_lin1(void)
{
  force_candidate_pins_low();

  if (!read_nfault_high())
  {
    s_fault_latched = true;
    force_candidate_pins_low();
    return false;
  }

  set_pin_level(GPIOA, 7u, true);
  const bool wake_ok = diagnostic_delay_or_fault(GATE_WAVEFORM_CANDIDATE_WAKE_LOOPS);
  return wake_ok;
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
    .diagnostic_vector_count = GATE_WAVEFORM_CANDIDATE_DIAG_VECTOR_COUNT,
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

  (void)diagnostic_delay_or_fault(GATE_WAVEFORM_CANDIDATE_DIAG_IDLE_LOOPS);

  if (s_fault_latched || !read_nfault_high())
  {
    s_fault_latched = true;
  }
  else
  {
    if (wake_driver_with_lin1())
    {
      (void)run_rotation_sequence_once();
    }
  }

  force_candidate_pins_low_keep_lin1_high();
  (void)diagnostic_delay_or_fault(GATE_WAVEFORM_CANDIDATE_DIAG_IDLE_LOOPS);

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
