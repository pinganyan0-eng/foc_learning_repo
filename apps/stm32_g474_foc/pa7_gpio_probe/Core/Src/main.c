#include "stm32g474xx.h"

#define PA5_STATUS_LED_BIT      (1UL << 5)
#define PA7_TEST_BIT            (1UL << 7)
#define PA8_CONTROL_BIT         (1UL << 8)
#define GPIOA_PROBE_BITS        (PA5_STATUS_LED_BIT | PA7_TEST_BIT | PA8_CONTROL_BIT)

int main(void)
{
  RCC->AHB2ENR |= RCC_AHB2ENR_GPIOAEN;
  __DSB();

  GPIOA->MODER &= ~((3UL << (5U * 2U)) |
                    (3UL << (7U * 2U)) |
                    (3UL << (8U * 2U)));
  GPIOA->MODER |=  ((1UL << (5U * 2U)) |
                    (1UL << (7U * 2U)) |
                    (1UL << (8U * 2U)));

  GPIOA->OTYPER &= ~GPIOA_PROBE_BITS;
  GPIOA->PUPDR &= ~((3UL << (5U * 2U)) |
                    (3UL << (7U * 2U)) |
                    (3UL << (8U * 2U)));
  GPIOA->OSPEEDR &= ~((3UL << (5U * 2U)) |
                      (3UL << (7U * 2U)) |
                      (3UL << (8U * 2U)));

  GPIOA->BSRR = GPIOA_PROBE_BITS;

  while (1)
  {
    __NOP();
  }
}

void SysTick_Handler(void)
{
}

void Error_Handler(void)
{
  while (1)
  {
    __NOP();
  }
}
