# Packet A Local Probe - 2026-05-15

This record continues Packet A after the hardware-source branch was skipped for
scheduling. It is a local no-power evidence inventory only. It does not create
or validate an MCSDK motor-control project.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## Probe Goal

Find whether the current machine already has one of the accepted Packet A
sources:

- a real Workbench `.stmcx`;
- a MotorControl / Workbench configuration screenshot;
- an exact launcher path plus captured version/config screen.

## Results

| Check | Result | Packet A decision |
| --- | --- | --- |
| Repo `.stmcx` inventory | `rg --files -g "*.stmcx"` in the repo returned no files. | No saved Workbench project exists in the repo. |
| Existing screenshot inventory | Current screenshots are `2026-05-14_cubemx_home.png`, `2026-05-14_cubemx_ioc_launch_attempt.png`, and `2026-05-14_cubemx_ioc_pinout_active_window.png`. | They are CubeMX GUI / `.ioc` fallback evidence only, not MotorControl evidence. |
| `apps/stm32_g474_foc/MotorControl` | Directory contains only tracked `.gitkeep`. | It is a placeholder, not generated MCSDK MotorControl source. |
| `F:\STMCubeMX` | `.stmcx` search returned no files; broad name search only found Eclipse workbench plugin names. | CubeMX exists, but no saved Workbench project or MotorControl launcher was proven. |
| `C:\Users\gregrg\STM32Cube\Repository` | `.stmcx` search returned no files. Earlier probe already found MotorControl package data only. | Package data is not project configuration evidence. |
| `C:\Users\gregrg\.stm32cubemx` | `.stmcx` search returned no files; `STM32CubeMX.log` is 0 bytes. | No Packet A configuration evidence found there. |
| `Documents`, `Downloads`, `Desktop` | `.stmcx` search returned no files. Name search found the repo placeholder/probe files, local ST manuals, and one unrelated RemCodex UI path. | No accepted Packet A source was found in common user locations. |
| `C:\Users\gregrg` root | Direct `rg --files -g "*.stmcx" C:\Users\gregrg` returned access denied. | This is not proof that every private user directory was searched. It is recorded as a search limitation. |

## Current Decision

Packet A remains `Blocked`.

Short status: no real `.stmcx` and no MotorControl / Workbench configuration screenshot were found in the checked locations.

Current repo evidence can say:

- CubeMX can reopen the saved NUCLEO `.ioc`;
- the `.ioc` preserves the current no-power pin draft;
- MotorControl package data exists locally;
- a local search did not find a real `.stmcx` in the checked locations.

Current repo evidence cannot say:

- a Workbench `.stmcx` exists;
- a MotorControl / Workbench configuration screen has been captured;
- a generated MCSDK motor-control project exists;
- Gate PWM, Motor Profiler, Hall, motor, power-stage, or sensorless behavior is
  validated.

## Next Valid Packet A Source

Use `packet_a_capture_checklist_2026-05-15.md` for the next GUI session. The
next accepted upgrade must be one of:

1. a real `.stmcx` saved into the repo;
2. a MotorControl / Workbench configuration screenshot with the required fields
   visible;
3. an exact reproducible launcher path plus captured version/config screen.

If none of those exists, keep Packet A blocked and do not create a generated
project trust claim.
