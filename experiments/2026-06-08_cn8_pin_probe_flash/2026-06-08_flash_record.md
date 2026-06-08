# 2026-06-08 CN8 pin probe flash record

Evidence ID: `EV-2026-06-08-FW-CN8-PIN-PROBE-FLASH-001`

## Scope

Flash the NUCLEO-only CN8 pin probe firmware to NUCLEO-G474RE.

This record does not approve any power-board, Gate, 24 V, motor, MCSDK, FOC,
or deadtime validation.

## Safety Boundary

- User confirmed before flashing: CN8/power board disconnected.
- User confirmed before flashing: 24 V disconnected.
- User confirmed before flashing: motor disconnected.
- Only NUCLEO ST-LINK USB connection was used for flashing.

## Firmware

- Source directory: `apps/stm32_g474_foc/cn8_pin_probe/`
- Hex file: `apps/stm32_g474_foc/cn8_pin_probe/build/Debug-mingw/cn8_pin_probe.hex`
- Flash address: `0x08000000`
- Programmed size reported by STM32CubeProgrammer: 5.98 KB

## Build Summary

`cmake --build --preset Debug` completed after adding the STM32 bundle GNU Arm
toolchain directory to PATH for the build process.

Memory usage reported at link:

| Region | Used | Total | Used % |
| --- | --- | --- | --- |
| RAM | 1656 B | 128 KB | 1.26% |
| FLASH | 6128 B | 512 KB | 1.17% |

`arm-none-eabi-size` summary:

| text | data | bss | dec | hex |
| --- | --- | --- | --- | --- |
| 6044 | 84 | 1572 | 7700 | 1e14 |

## Flash Summary

STM32CubeProgrammer v2.22.0 output summary:

- ST-LINK SN: `002F00253235511337333439`
- ST-LINK FW: `V3J17M10`
- Board: `NUCLEO-G474RE`
- Target voltage: 3.28 V
- SWD frequency: 8000 KHz
- Device ID: `0x469`
- Revision ID: Rev X
- Device name: STM32G47x/G48x/G414
- NVM size: 512 KBytes
- File download complete
- Download verified successfully
- Software reset performed

## Expected Pin Outputs After Reset

| CN8 | Signal | STM32 pin | Expected waveform |
| --- | --- | --- | --- |
| P1 | HIN1 | PA15 | about 50 Hz square wave |
| P2 | LIN1 | PB3 | about 100 Hz square wave |
| P3 | HIN2 | PB10 | about 200 Hz square wave |
| P4 | LIN2 | PA8 | about 400 Hz square wave |
| P5 | HIN3 | PA9 | about 1 kHz square wave |
| P6 | LIN3 | PA10 | about 2 kHz square wave |

## NUCLEO-only Waveform Measurements

User-provided RIGOL DS1102E Plus screenshots:

| STM32 pin | NUCLEO Arduino point used | Expected | Observed | Evidence photo |
| --- | --- | --- | --- | --- |
| PA8 | `D7` | about 400 Hz | about 401 Hz, period about 2.495 ms | `experiments/2026-06-08_cn8_pin_probe_flash/photos/2026-06-08_pa8_ard_d7_400hz_scope.jpg` |
| PA9 | `D8` | about 1 kHz | 1.00 kHz, period 1.000 ms | `experiments/2026-06-08_cn8_pin_probe_flash/photos/2026-06-08_pa9_ard_d8_1khz_scope.jpg` |
| PA10 | `D2` | about 2 kHz | 2.00 kHz, period 500.0 us | `experiments/2026-06-08_cn8_pin_probe_flash/photos/2026-06-08_pa10_ard_d2_2khz_scope.jpg` |
| PB3 | `D3` | about 100 Hz | 100 Hz, period 9.980 ms | `experiments/2026-06-08_cn8_pin_probe_flash/photos/2026-06-08_pb3_ard_d3_100hz_scope.jpg` |
| PB10 | `D6` | about 200 Hz | 200 Hz, period 5.000 ms | `experiments/2026-06-08_cn8_pin_probe_flash/photos/2026-06-08_pb10_ard_d6_200hz_scope.jpg` |
| PA15 | ST Morpho `CN7-17` | about 50 Hz | 50.0 Hz, period 20.00 ms | `experiments/2026-06-08_cn8_pin_probe_flash/photos/2026-06-08_pa15_cn7_17_50hz_scope.jpg` |

Correction note: Codex previously conflated STM32 `PA9` with the NUCLEO Arduino
silk label `D9`. The correct NUCLEO Arduino point for checking firmware `PA9`
is `D8`; Arduino `D9` is not the PA9 check point. This correction affects only
the user-facing measurement guidance, not the compiled firmware pin assignment.

These screenshots confirm the expected identification frequencies on all six
NUCLEO pin-probe outputs: PA15, PB3, PB10, PA8, PA9, and PA10. They do not
validate Gate outputs, edge quality, the power board, 24 V operation, motor
operation, MCSDK, FOC, or deadtime.

## Next Measurement Boundary

- Scope ground clip may be connected only to NUCLEO GND for this check.
- All six NUCLEO-only identification outputs are measured at their expected
  frequencies.
- This closes only the NUCLEO MCU-pin mapping check. A separate reviewed task
  is required before connecting CN8 to the power board or measuring Gate
  outputs.
- Do not connect scope ground to OUTx, BOOTx, high-side source/switch-node, or
  any unreviewed power-board point.
- Do not connect CN8 to the power board during this NUCLEO-only pin check.

Official connector source:

- ST UM2505, ST Morpho connector table:
  `https://www.st.com/resource/en/user_manual/dm00556337.pdf`
