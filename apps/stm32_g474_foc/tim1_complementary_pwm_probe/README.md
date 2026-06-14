# TIM1 complementary PWM probe

This is a NUCLEO-G474RE-only logic waveform test. It generates three pairs of
TIM1 complementary PWM outputs so that frequency, duty cycle, deadtime,
startup inhibition, software STOP, and BKIN shutdown can be measured before
any power-board connection.

It is not MCSDK, FOC, Gate, power-board, 24 V, or motor validation firmware.

## Safety boundary

- Keep the power board, CN8 cable, 24 V supply, and motor disconnected.
- Power only the NUCLEO through its ST-LINK USB connector.
- Connect an ordinary oscilloscope probe ground only to NUCLEO GND.
- Do not use this firmware as approval to probe `OUTx`, `BOOTx`, or high-side
  `Vgs`.
- Reset the NUCLEO before changing any measurement wiring.

## Output mapping

| Intended CN8 role | STM32 pin | TIM1 function | NUCLEO Morpho point |
| --- | --- | --- | --- |
| P1 HIN1 | PA8 | CH1, AF6 | CN10-23 |
| P2 LIN1 | PA7 | CH1N, AF6 | CN10-15 |
| P3 HIN2 | PA9 | CH2, AF6 | CN10-21 |
| P4 LIN2 | PB14 | CH2N, AF6 | CN10-28 |
| P5 HIN3 | PA10 | CH3, AF6 | CN10-33 |
| P6 LIN3 | PB15 | CH3N, AF4 | CN10-26 |
| P13 nFAULT | PB12 | TIM1_BKIN, AF6 | CN10-16 |

The previous PA15/PB3/PB10/PA8/PA9/PA10 mapping remains valid only as the
measured GPIO identification mapping. It is not used by this complementary
PWM firmware.

## Test configuration

- TIM1 input clock: 170 MHz
- Center-aligned frequency: 10 kHz
- Duty cycle: 25%
- Deadtime code: `0xCA`
- Actual deadtime at 170 MHz: 336 timer ticks, approximately 1.976 us
- Main and complementary outputs: TIM1 default complementary relationship,
  active high and inactive low
- BKIN: active low with MCU pull-up
- Automatic output enable: disabled
- Debug freeze: enabled for TIM1

These values are deliberately conservative for NUCLEO logic measurement.
They are not production FOC parameters.

## State behavior

1. After reset, TIM1 counts but `MOE=0`; all six outputs remain inactive low.
2. Press NUCLEO `B1` once to set `MOE` and start all six outputs. LD2 turns on.
3. Press `B1` again to clear `MOE`. The firmware enters a latched STOP state
   and cannot re-arm until reset.
4. Pull PB12/CN10-16 safely to NUCLEO GND to assert BKIN. Hardware clears
   `MOE`; the interrupt records a latched break state. Reset is required before
   another arm.

`B1` is a test command, not a safety input. BKIN is the asynchronous shutdown
path.

## Build

Open this directory as the VS Code workspace, then run the default build task,
or use:

```powershell
cmake --preset Debug
cmake --build --preset Debug
```

Expected outputs:

- `build/Debug-mingw/tim1_complementary_pwm_probe.elf`
- `build/Debug-mingw/tim1_complementary_pwm_probe.hex`
- `build/Debug-mingw/tim1_complementary_pwm_probe.bin`

## NUCLEO-only measurement order

1. Flash the HEX while the NUCLEO is the only connected board.
2. Reset and verify PA8/PA7, PA9/PB14, and PA10/PB15 remain low before `B1`.
3. Press `B1` once.
4. Measure each complementary pair with both scope channels:
   - 10 kHz frequency
   - approximately 25% high-side-command duty
   - approximately 0 to 3.3 V amplitude
   - no simultaneous high interval
   - approximately 2 us deadtime at both transitions
5. Pull PB12/CN10-16 to GND and verify all six outputs stop and remain stopped.
6. Reset and verify outputs again remain disabled until `B1`.

Official sources:

- STM32G4 reference manual RM0440:
  `https://www.st.com/resource/en/reference_manual/dm00355726.pdf`
- STM32G474 datasheet:
  `https://www.st.com/resource/en/datasheet/stm32g474pb.pdf`
- NUCLEO-G474RE user manual UM2505:
  `https://www.st.com/resource/en/user_manual/dm00556337.pdf`
