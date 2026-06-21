#include "stm32g4xx.h"

int main(void)
{
  RCC->AHB2ENR |= RCC_AHB2ENR_GPIOAEN;
  (void)RCC->AHB2ENR;

  GPIOA->BSRR = 1u << 7u;
  GPIOA->MODER = (GPIOA->MODER & ~(3u << 14u)) | (1u << 14u);
  GPIOA->OTYPER &= ~(1u << 7u);
  GPIOA->OSPEEDR &= ~(3u << 14u);
  GPIOA->PUPDR &= ~(3u << 14u);

  for (;;)
  {
    GPIOA->BSRR = 1u << 7u;
  }
}
