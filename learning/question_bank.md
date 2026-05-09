# Question Bank

Use these prompts to check understanding without turning every lesson into a long exam.

## General

- Explain the concept in one minute without using the original wording.
- Name one thing that would break if this assumption is wrong.
- Give a minimal test that proves this is working.
- What evidence would make us stop and roll back?

## STM32G474 FOC

- Why must the STM32 own the real-time FOC loop instead of the ESP32-C3?
- What should never be done inside the JEOC/FOC ISR?
- Before connecting a motor, which no-load checks must pass?
- What is the difference between Hall closed-loop bring-up and SMO/PLL sensorless operation?

## Hardware Safety

- What is the current-limit setting for first cautious power-up, and why?
- Which measurements should be checked before trusting PWM gate drive?
- What evidence would distinguish a firmware bug from a current-sense scaling error?
