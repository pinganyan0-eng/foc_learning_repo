# TIM1 dynamic cable mapping decision - 2026-06-08

## Decision

The recovered 2026-05-19 mapping remains the accepted evidence for the six
GPIO identification test. It is not suitable as the final dynamic PWM cable
map because the six pins do not form three TIM1 main/complementary channel
pairs.

For the NUCLEO-only TIM1 complementary PWM test and any later separately
approved CN8 cable, use:

| CN8 | Driver input | STM32 pin | TIM1 function | NUCLEO Morpho |
| --- | --- | --- | --- | --- |
| P1 | HIN1 | PA8 | CH1, AF6 | CN10-23 |
| P2 | LIN1 | PA7 | CH1N, AF6 | CN10-15 |
| P3 | HIN2 | PA9 | CH2, AF6 | CN10-21 |
| P4 | LIN2 | PB14 | CH2N, AF6 | CN10-28 |
| P5 | HIN3 | PA10 | CH3, AF6 | CN10-33 |
| P6 | LIN3 | PB15 | CH3N, AF4 | CN10-26 |
| P13 | nFAULT | PB12 | BKIN, AF6 | CN10-16 |
| P15 | GND_SIGNAL | NUCLEO GND | Ground reference | reviewed GND |

Initial cable restrictions:

- P7-P12 remain disconnected.
- P14 3V3 remains disconnected to avoid USB/power-board back-power.
- P15 is the only reviewed signal-ground connection.
- No cable is installed during the NUCLEO-only firmware and waveform test.

## Rationale

- TIM1 supplies the three required main/complementary pairs from one advanced
  motor-control timer.
- The timer can insert deadtime in hardware between each main/complementary
  pair.
- PB12 can feed TIM1 BKIN so an active-low nFAULT can remove MOE
  asynchronously.
- PA7/PB14/PB15 do not replace the preserved Hall/current-signal route
  PA0/PA1/PB4 or the ADC route PA4/PB0/PA5.

## Status boundary

This decision defines firmware and loose-wire endpoints only. It does not prove
the physical cable, DT/MODE mode, power-board behavior, Gate timing, or motor
operation.

Before installing a cable:

1. Confirm DT/MODE-to-GND resistance with the board unpowered and discharged.
2. Record every source, destination, and net name.
3. Verify P14 remains open and P15 is the reviewed ground.
4. Complete NUCLEO-only complementary PWM and BKIN waveform validation.

## Official sources

- STM32G474 datasheet:
  `https://www.st.com/resource/en/datasheet/stm32g474pb.pdf`
- NUCLEO-G474RE user manual UM2505:
  `https://www.st.com/resource/en/user_manual/dm00556337.pdf`
- STM32G4 reference manual RM0440:
  `https://www.st.com/resource/en/reference_manual/dm00355726.pdf`
