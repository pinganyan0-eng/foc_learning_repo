#include "stm32g4xx.h"

#define GPIOA_TOGGLE_MASK ((uint32_t)((1u << 7) | (1u << 8) | (1u << 9) | (1u << 10)))
#define GPIOB_TOGGLE_MASK ((uint32_t)((1u << 14) | (1u << 15)))

static void delay_visible(void)
{
  for (volatile uint32_t i = 0u; i < 3000000u; ++i)
  {
    __asm volatile ("nop");
  }
}

static void configure_output_low(GPIO_TypeDef *port, uint32_t pin)
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

static void set_all_low(void)
{
  GPIOA->BSRR = GPIOA_TOGGLE_MASK << 16u;
  GPIOB->BSRR = GPIOB_TOGGLE_MASK << 16u;
}

static void set_one(GPIO_TypeDef *port, uint32_t pin)
{
  set_all_low();
  port->BSRR = 1u << pin;
}

int main(void)
{
  RCC->AHB2ENR |= RCC_AHB2ENR_GPIOAEN | RCC_AHB2ENR_GPIOBEN;
  (void)RCC->AHB2ENR;

  configure_output_low(GPIOA, 8u);
  configure_output_low(GPIOA, 7u);
  configure_output_low(GPIOA, 9u);
  configure_output_low(GPIOB, 14u);
  configure_output_low(GPIOA, 10u);
  configure_output_low(GPIOB, 15u);

  for (;;)
  {
    set_one(GPIOA, 8u);
    delay_visible();
    set_one(GPIOA, 7u);
    delay_visible();
    set_one(GPIOA, 9u);
    delay_visible();
    set_one(GPIOB, 14u);
    delay_visible();
    set_one(GPIOA, 10u);
    delay_visible();
    set_one(GPIOB, 15u);
    delay_visible();
  }
}
