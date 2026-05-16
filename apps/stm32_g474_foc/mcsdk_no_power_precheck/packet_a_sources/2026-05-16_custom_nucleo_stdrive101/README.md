# Packet A Capture Package - Custom NUCLEO + STDRIVE101

Date: 2026-05-16

Status: prepared, Workbench source pending.

This directory is for a new project-specific MCSDK 6 / ST MC Workbench capture.
It replaces the earlier learning leftover `My_First_FOC.stwb6` as the next
Packet A target.

## Target Configuration

| Item | Planned value | Evidence status |
| --- | --- | --- |
| Workbench | ST MC Workbench 6.4.2 | Launcher proven locally. |
| Workbench path | `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\STMCWB.exe` | Proven locally. |
| Algorithm | FOC | To be captured in GUI. |
| Control board | `NUCLEO-G474RE` / `STM32G474RETx` | To be captured in GUI. |
| Power stage | Custom / Generic inverter for the self-made STDRIVE101 board | To be captured in GUI; do not use `EVALSTDRIVE101`. |
| Motor | `PLACEHOLDER_not_profiled_2026-05-16` until no-power records are filled | Placeholder only. |
| Speed feedback | Hall as the first bring-up fallback | Planning only; no Hall validation. |
| Current sensing | 3-shunt low-side, internal OPAMP/PGA preference | Planning only; no current measurement claim. |
| Generated project | None in this package | Not allowed in this step. |

## Expected Future Files

These files should be added only after the GUI work is actually done:

- `custom_nucleo_stdrive101_2026-05-16.stwb6`
- `screenshots/2026-05-16_workbench_project_hw_info.png`
- `screenshots/2026-05-16_workbench_pwm_generation.png`
- `screenshots/2026-05-16_workbench_current_sensing.png`
- `screenshots/2026-05-16_workbench_speed_sensing_hall.png`
- `screenshots/2026-05-16_workbench_driver_protection.png`
- `screenshots/2026-05-16_workbench_pin_usage.png`

## Files In This Package

- `workbench_no_power_configuration_guide_2026-05-16.md`
- `motor_no_power_measurement_log_2026-05-16.md`
- `pin_assignment_table_2026-05-16.md`
- `screenshots/README.md`

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No generated source.
- No build-only work.
- No flashing.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## Current Decision

This package prepares Packet A capture but does not yet accept Packet A. A real
`.stwb6` file and Workbench screenshots are still required before any selected
field can be reviewed as accepted configuration evidence.
