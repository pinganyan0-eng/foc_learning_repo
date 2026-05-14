# P2 GUI Capture Result - 2026-05-14

This record documents the GUI evidence push after the saved
NUCLEO-G474RE CubeMX `.ioc` draft. It is a no-power configuration evidence
record only.

## Attempt

| Item | Result |
| --- | --- |
| GUI launched | `F:\STMCubeMX\STM32CubeMX.exe` |
| Input file | `mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc` |
| Visible page | CubeMX `Pinout & Configuration` |
| Screenshot, full desktop | `screenshots/2026-05-14_cubemx_ioc_launch_attempt.png` |
| Screenshot, active window | `screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png` |
| Repo `.stmcx` search after attempt | No `.stmcx` found. |

## What The Screenshot Shows

The CubeMX window title shows:

- `mcsdk_no_power_nucleo_g474re_draft.ioc`;
- `STM32G474RETx`;
- `NUCLEO-G474RE`;
- `Pinout & Configuration`.

The visible pinout page is configuration evidence for the saved `.ioc` draft.
It is not Motor Control Workbench evidence.

## `.ioc` Readback Used With The Screenshot

The saved `.ioc` still reads back:

- `Mcu.IP0=NUCLEO-G474RE`;
- `Mcu.UserName=STM32G474RETx`;
- `Mcu.CPN=STM32G474RET6`;
- `Mcu.Package=LQFP64`;
- `PA13.Signal=SYS_JTMS-SWDIO`;
- `PA14.Signal=SYS_JTCK-SWCLK`;
- `PA2.Signal=LPUART1_TX`;
- `PA3.Signal=LPUART1_RX`;
- `PB3.Signal=SYS_JTDO-SWO`;
- `PB12.Signal=TIM1_BKIN`;
- `PB14.Signal=TIM1_CH2N`.

## Blocker

This turn did not produce a real Workbench `.stmcx` file and did not capture a
MotorControl configuration page. The valid evidence gained is a CubeMX GUI
pinout capture for the already saved `.ioc` draft, plus the repeated absence of
`.stmcx` in the repo.

Treat this as fallback P2 GUI evidence:

- OK to claim: the saved NUCLEO-G474RE `.ioc` can be reopened in CubeMX and
  viewed on the `Pinout & Configuration` page.
- Do not claim: MCSDK MotorControl configuration, Workbench `.stmcx`, generated
  motor-control firmware, board routing, PWM Gate readiness, Motor Profiler,
  Hall closed-loop, or sensorless FOC.

## Safety Boundary

No 24V, no power-board connection, no motor connection, no PWM Gate output, no
Motor Profiler run, no flashing/debug run, no Hall closed-loop validation, and
no sensorless validation were performed or authorized by this capture.
