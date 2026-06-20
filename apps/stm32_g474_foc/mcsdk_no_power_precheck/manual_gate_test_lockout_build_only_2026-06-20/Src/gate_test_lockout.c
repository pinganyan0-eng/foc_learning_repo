#include "gate_test_lockout.h"

#include "stm32g4xx.h"

#define GATE_TEST_PA_LOW_MASK ((uint32_t)((1u << 8) | (1u << 9) | (1u << 10)))
#define GATE_TEST_PB_LOW_MASK ((uint32_t)((1u << 13) | (1u << 14) | (1u << 15)))
#define GATE_TEST_NFAULT_PIN  12u

static bool s_fault_latched;

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

static void enable_gpio_clocks(void)
{
  RCC->AHB2ENR |= RCC_AHB2ENR_GPIOAEN | RCC_AHB2ENR_GPIOBEN;
  (void)RCC->AHB2ENR;
}

static void force_driver_inputs_low(void)
{
  GPIOA->BSRR = GATE_TEST_PA_LOW_MASK << 16u;
  GPIOB->BSRR = GATE_TEST_PB_LOW_MASK << 16u;

  configure_pin_as_output_low(GPIOA, 8u);
  configure_pin_as_output_low(GPIOA, 9u);
  configure_pin_as_output_low(GPIOA, 10u);
  configure_pin_as_output_low(GPIOB, 13u);
  configure_pin_as_output_low(GPIOB, 14u);
  configure_pin_as_output_low(GPIOB, 15u);
}

static void configure_fault_input(void)
{
  configure_pin_as_input(GPIOB, GATE_TEST_NFAULT_PIN);
}

static void lock_tim1_outputs(void)
{
  RCC->APB2ENR |= RCC_APB2ENR_TIM1EN;
  (void)RCC->APB2ENR;

  TIM1->CR1 = 0u;
  TIM1->DIER = 0u;
  TIM1->CCER = 0u;
  TIM1->BDTR = (TIM1->BDTR & ~(TIM_BDTR_MOE | TIM_BDTR_AOE)) | TIM_BDTR_BKE;
}

static bool read_nfault_high(void)
{
  return (GPIOB->IDR & (1u << GATE_TEST_NFAULT_PIN)) != 0u;
}

void gate_test_lockout_force_safe_state(void)
{
  enable_gpio_clocks();
  force_driver_inputs_low();
  configure_fault_input();
  lock_tim1_outputs();
}

void gate_test_lockout_init(void)
{
  s_fault_latched = false;
  gate_test_lockout_force_safe_state();
}

gate_test_lockout_state_t gate_test_lockout_poll(void)
{
  gate_test_lockout_force_safe_state();

  const bool nfault_high = read_nfault_high();
  if (!nfault_high)
  {
    s_fault_latched = true;
  }

  const gate_test_lockout_state_t state = {
    .nfault_high = nfault_high,
    .fault_latched = s_fault_latched,
    .tim1_outputs_disabled = (TIM1->CCER == 0u),
    .tim1_main_output_disabled = ((TIM1->BDTR & TIM_BDTR_MOE) == 0u),
  };

  return state;
}
