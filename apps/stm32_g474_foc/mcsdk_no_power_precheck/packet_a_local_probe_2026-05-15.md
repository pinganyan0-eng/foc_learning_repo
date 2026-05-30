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

- a real Workbench project file: `.stwb6` for MCSDK 6.x, or legacy `.stmcx`;
- a MotorControl / Workbench configuration screenshot;
- an exact launcher path plus captured version/config screen.

## Results

| Check | Result | Packet A decision |
| --- | --- | --- |
| Repo `.stmcx` inventory | `rg --files -g "*.stmcx"` in the repo returned no files. | No saved Workbench project exists in the repo. |
| Existing screenshot inventory | Current screenshots are `2026-05-14_cubemx_home.png`, `2026-05-14_cubemx_ioc_launch_attempt.png`, and `2026-05-14_cubemx_ioc_pinout_active_window.png`. | They are CubeMX GUI / `.ioc` fallback evidence only, not MotorControl evidence. |
| `apps/stm32_g474_foc/MotorControl` | Directory contains only tracked `.gitkeep`. | It is a placeholder, not generated MCSDK MotorControl source. |
| `F:\STMCubeMX` | `.stmcx` search returned no files; broad name search only found Eclipse workbench plugin names. | CubeMX exists, but no saved Workbench project was found there. |
| Start Menu / `F:\STMCSDK` follow-up | Start Menu contains `MotorControl Workbench 6.4.2.lnk`, resolving to `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\STMCWB.exe`; `F:\STMCSDK\My_First_FOC.stwb6` was found and copied into the repo. | Legacy learning `.stwb6` found; review result is `Partial clue`, not custom-board Packet A acceptance or build-only clearance. |
| `C:\Users\gregrg\STM32Cube\Repository` | `.stmcx` search returned no files. Earlier probe already found MotorControl package data only. | Package data is not project configuration evidence. |
| `C:\Users\gregrg\.stm32cubemx` | `.stmcx` search returned no files; `STM32CubeMX.log` is 0 bytes. | No Packet A configuration evidence found there. |
| `Documents`, `Downloads`, `Desktop` | `.stmcx` search returned no files. Name search found the repo placeholder/probe files, local ST manuals, and one unrelated RemCodex UI path. | No accepted Packet A source was found in common user locations. |
| `C:\Users\gregrg` root | Direct `rg --files -g "*.stmcx" C:\Users\gregrg` returned access denied. | This is not proof that every private user directory was searched. It is recorded as a search limitation. |

## Current Decision

Packet A is no longer "no local Workbench file exists"; it now has a
`Partial clue` source candidate.

Short status: no `.stmcx` was found, but MCSDK 6 Workbench uses `.stwb6`, and
`My_First_FOC.stwb6` was found under `F:\STMCSDK`. No MotorControl / Workbench configuration screenshot has been captured yet.

Current repo evidence can say:

- CubeMX can reopen the saved NUCLEO `.ioc`;
- the `.ioc` preserves the current no-power pin draft;
- MotorControl package data exists locally;
- a local search did not find a real `.stmcx` in the checked locations.

Current repo evidence cannot say:

- a Workbench `.stmcx` exists;
- a `.stwb6` exists as a final accepted competition-board configuration;
- a MotorControl / Workbench configuration screen has been captured;
- a generated MCSDK motor-control project exists;
- Gate PWM, Motor Profiler, Hall, motor, power-stage, or sensorless behavior is
  validated.

## Next Valid Packet A Source

Use `packet_a_capture_checklist_2026-05-15.md` for the next GUI session. The
next accepted upgrade must be one of:

1. a real `.stwb6` or legacy `.stmcx` saved into the repo;
2. a MotorControl / Workbench configuration screenshot with the required fields
   visible;
3. an exact reproducible launcher path plus captured version/config screen.

After the 2026-05-15 follow-up, `My_First_FOC.stwb6` exists only as a legacy
learning-file `Partial clue`. After the 2026-05-16 follow-up, the next
project-specific path is the custom NUCLEO + STDRIVE101 capture package under
`packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`. Keep
generated-project trust `Not allowed` until a review accepts the required
selected fields from a real project-specific `.stwb6` and Workbench
screenshots.
