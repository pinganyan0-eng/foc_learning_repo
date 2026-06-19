# NUCLEO-G474RE USB-Only Baseline Safety Review - 2026-06-19

## Boundary

This review is source and build evidence only.

- No flash was performed.
- No 24 V powered step was performed.
- No power board or motor validation is claimed.
- No Gate PWM, Motor Pilot, Motor Profiler, Hall closed-loop, or sensorless
  readiness is claimed.

The user's latest field measurements are treated as static measurement
evidence only. They do not open firmware flash or powered-drive readiness by
themselves.

## Reviewed Target

- Project:
  `apps/stm32_g474_foc/nucleo_g474re_baseline`
- Purpose:
  candidate USB-only safety baseline before any later explicitly approved
  flash gate.

## Source Review Findings

- `Core/Src/main.c` implements an application state model with
  `APP_MODE_IDLE`, `APP_MODE_ARMED`, and `APP_MODE_RUN_SIM`.
- Serial commands `PING`, `MODE?`, `SET_RPM`, `ARM`, and `STOP` only change or
  report software variables such as `app_mode`, `mode_change_count`, and
  `target_rpm`.
- `target_rpm` is explicitly documented in source as a communication-layer
  simulated target speed and not a motor or PWM drive.
- B1 handling only advances the software state sequence:
  `IDLE -> ARMED -> RUN_SIM -> IDLE`.
- The periodic report prints state, button, LED, UART, and simulated RPM
  fields only.
- `MX_GPIO_Init()` only enables GPIO port clocks in this project snapshot.
- `nucleo_g474re_baseline.ioc` lists only the NUCLEO board support, NVIC, RCC,
  and SYS project blocks. The visible application pins are PA2/PA3 for
  LPUART1 and default debug / clock pins.
- `Core/Inc/stm32g4xx_hal_conf.h` leaves `HAL_TIM_MODULE_ENABLED` and
  `HAL_HRTIM_MODULE_ENABLED` commented out.
- `Core/Src/stm32g4xx_it.c` contains only the B1 EXTI handler, DMA1 channel 1
  handler, and LPUART1 handler beyond core exception handlers.

Targeted searches in `Core/Src`, `Core/Inc`, the `.ioc`, and the CubeMX CMake
source list found no application-level `TIM1`, `TIM8`, `PWM`, `MOE`, `BDTR`,
`HAL_TIM_PWM_Start`, `HAL_TIMEx_PWMN_Start`, `LL_TIM_EnableAllOutputs`,
`__HAL_TIM_MOE_ENABLE`, `MC_StartMotor`, `MCI_StartMotor`, `HIN`, `LIN`,
`CN3`, `NFAULT`, `STDRIVE`, `GATE`, `PHASE`, or motor-control start path.

## Build-Only Check

Command run from
`apps/stm32_g474_foc/nucleo_g474re_baseline`:

```powershell
cmake --build --preset Debug
```

Result:

```text
ninja: no work to do.
```

Exit code: `0`.

The first sandboxed attempt failed because executing the STM32Cube-bundled
Ninja outside the workspace was blocked. The approved rerun completed as a
local build-only check. It did not flash or access hardware.

## Decision

`nucleo_g474re_baseline` is a reasonable candidate for a later USB-only safety
flash gate because the reviewed source does not configure or start motor PWM,
TIM1/TIM8 outputs, MOE, MCSDK motor start, or STDRIVE HIN/LIN control.

This is not proof of the firmware currently running on the NUCLEO. In the
preceding COM5 read-only / query check, the board did not return the expected
periodic status, `PING`, or `MODE?` responses, so the current flashed firmware
identity remains unknown.

## Next Gate

The next project step should be a separate explicit flash gate only if the user
approves it:

1. USB only.
2. HSPY output off.
3. 24 V disconnected from the board.
4. Motor disconnected.
5. Flash only this reviewed baseline image.
6. After flashing, confirm serial boot text and command responses.
7. With USB only, re-check CN3 HIN/LIN remain 0 V before any later powered
   step is considered.
