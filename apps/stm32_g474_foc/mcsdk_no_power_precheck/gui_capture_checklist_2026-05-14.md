# GUI Capture Checklist - 2026-05-14

This checklist is for the next P2 no-power GUI step. It keeps the work inside
configuration evidence only.

## Current Captured Evidence

- CubeMX launch screenshot:
  `screenshots/2026-05-14_cubemx_home.png`
- CubeMX saved `.ioc` pinout screenshots:
  `screenshots/2026-05-14_cubemx_ioc_launch_attempt.png` and
  `screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`
- GUI follow-up record:
  `gui_capture_result_2026-05-14.md`
- CubeMX local path:
  `F:\STMCubeMX\STM32CubeMX.exe`
- No repo `.stmcx` exists yet.

The screenshot proves the CubeMX GUI is open at Home. It does not prove an
MCSDK configuration, generated firmware, board wiring, or safe hardware
behavior.

The later pinout screenshots prove the saved NUCLEO `.ioc` can be reopened in
CubeMX at `Pinout & Configuration`. They still do not prove a Workbench
`.stmcx`, MCSDK MotorControl configuration, board routing, or hardware behavior.

## Allowed GUI Actions

1. Open MCU selector or board selector.
2. Select `STM32G474RETx` or `NUCLEO-G474RE`.
3. Inspect pinout and middleware configuration pages.
4. Capture screenshots of configuration pages.
5. Save a Workbench/CubeMX configuration file into this directory if the GUI
   offers a no-power save action.

## Required Capture Targets

- MCU selection shows `STM32G474RE` / `STM32G474RETx`.
- TIM1 complementary PWM draft is visible.
- Protection input draft shows `PB12 / TIM1_BKIN`, not `PC5`.
- Hall draft keeps `PA15 / PB3 / PB10` visible, with `PB3` SWO conflict noted.
- FOC communication does not silently choose `PA2 / PA3` as the default UART.
- Any saved `.stmcx` or generated project path is inside
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/`.

## Forbidden GUI Actions

- Do not connect 24V.
- Do not connect the power board.
- Do not connect a motor.
- Do not run Motor Profiler.
- Do not flash firmware to hardware.
- Do not start debug/run on hardware.
- Do not enable or test Gate PWM output.

## If The GUI Blocks The Step

Record the block exactly:

- GUI page name.
- Button or menu attempted.
- Error text or missing control.
- Screenshot path.
- Whether the GUI offered `.stmcx`, `.ioc`, or project generation only.

This turns a GUI block into valid P2 evidence without overstating progress.
