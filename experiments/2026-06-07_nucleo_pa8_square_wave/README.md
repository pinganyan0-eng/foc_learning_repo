# NUCLEO PA8/D7 square-wave check

## Scope

This is a low-voltage NUCLEO-only GPIO and oscilloscope check.

- Board: NUCLEO-G474RE.
- Firmware: `apps/stm32_g474_foc/nucleo_g474re_baseline/`.
- Output: `PA8`, Arduino `D7`, ST morpho `CN10 pin 23`.
- Expected waveform: approximately 500 Hz, 50% duty, 0 V to 3.3 V.
- Probe: RIGOL PVP2350 in 10X mode.
- Oscilloscope: RIGOL DS1102E Plus, channel probe ratio set to 10X.

## Safety Boundary

- Power board disconnected.
- No 24V supply.
- No motor.
- No CN3 control cable.
- Probe ground clip connects only to a NUCLEO GND pin.
- This is not a TIM1 PWM, complementary-output, Gate, deadtime or power-stage test.

## Firmware Behavior

`APP_PA8_WAVEFORM_TEST` is defined in `Core/Inc/main.h`.

- `1`: initialize PA8 as a push-pull output and toggle it every 1 ms.
- `0`: keep PA8 low and run the original baseline application loop.

The test mode intentionally skips the original UART/status loop so serial output cannot stretch the waveform period.

## Measurement Record

| Field | Result |
| --- | --- |
| Date | 2026-06-07 |
| Firmware source | This task's committed `master` source |
| Compiler | ST GNU Tools for STM32 14.3.1 |
| Build result | Debug build passed, 2026-06-07 |
| ELF size | text 14448 B, data 124 B, bss 2084 B |
| Local HEX file | `apps/stm32_g474_foc/nucleo_g474re_baseline/build/Debug/nucleo_g474re_pa8_square_wave.hex` (ignored build artifact) |
| HEX SHA-256 | `b50c582cd29308fe95e29f024d48b14748473d98992eaa2f20f273e1b2482fb0` |
| Probe attenuation | 10X |
| Scope channel ratio | 10X |
| Measured frequency | Pending |
| Measured Vpp | Pending |
| Duty cycle | Pending |
| Screenshot | Pending |
| Abnormal heating/smell | Not applicable to power board; NUCLEO-only |

## Acceptance

- Frequency is close to 500 Hz.
- Voltage is close to 0~3.3 V.
- Duty cycle is close to 50%.
- No power-board or motor connection was present.

Passing this check proves only that the NUCLEO pin and basic oscilloscope path can show a GPIO square wave.

## Rebuild

The local toolchain was unpacked under the workspace `.tools` directory. It is not added to the system `PATH`.

```sh
export PATH="/Users/ahs/Downloads/foc_learning_repo_mac_codex_setup_bundle/.tools/gnu-tools-for-stm32-14.3.1+st.2/bin:/Users/ahs/Library/Application Support/stm32cube/bundles/ninja/1.13.2+st.1/bin:/Users/ahs/Library/Application Support/stm32cube/bundles/cmake/4.3.1+st.1/CMake.app/Contents/bin:$PATH"
cmake --preset Debug
cmake --build --preset Debug
```
