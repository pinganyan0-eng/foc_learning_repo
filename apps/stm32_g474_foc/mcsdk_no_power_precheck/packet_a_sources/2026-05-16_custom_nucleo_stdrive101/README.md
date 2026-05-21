# Packet A Capture Package - Custom NUCLEO + STDRIVE101

Date: 2026-05-16

Status: Workbench GUI FOC source captured on 2026-05-21. Packet A source
evidence is upgraded, but generated-source trust, build-only clearance, and all
hardware readiness remain blocked.

This directory is for a new project-specific MCSDK 6 / ST MC Workbench capture.
It replaces the earlier learning leftover `My_First_FOC.stwb6` as the next
Packet A target.

## Target Configuration

| Item | Planned value | Evidence status |
| --- | --- | --- |
| Workbench | ST MC Workbench 6.4.2 | Launcher proven locally. |
| Workbench path | `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\STMCWB.exe` | Proven locally. |
| Algorithm | FOC | Captured in `QIANSAI_G474_STDRIVE101_FOC_P2_2026-05-21.stwb6`. |
| Control board | `NUCLEO-G474RE` / `STM32G474RETx` | Captured in GUI on 2026-05-20. |
| Power stage | `MY-STDRIVE101_POWER_BOARD` custom board | Captured in the 2026-05-21 Workbench FOC `.stwb6`; `EVALSTDRIVE101` not used. |
| Adapter candidate | `QIANSAI_STDRIVE101_TIM1_ADAPTER_POWER` | No-power GUI follow-up; PWM Generation became green, current sensing still blocked. |
| OPAMP adapter candidate | `QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER` | Source file created and installed in Workbench user board library; GUI reselection still pending. |
| Short-name OPAMP alias | `QS_TIM1_OPAMP_PWR` | Same no-power adapter route as the OPAMP candidate. Installed both as a user board and as a local Workbench app asset because the GUI search did not surface the user-library board even though the API listed it. |
| Motor | `R57BLB50L2` temporary placeholder | User-approved placeholder only; not measured project data. |
| Speed feedback | Hall as the first bring-up fallback | Captured as `HallEffectSensor` / `speedSensorMode: hall`; no Hall hardware validation. |
| Current sensing | 3-shunt Workbench-compatible amplified-current model | Captured as `CURRENT_AMPL_U/V/W -> ML30/MR24/ML34`; no current measurement claim. |
| Driver protection | `DP_TRIGGER -> MR16` / `PB12 TIM1_BKIN` | Captured with active-low driver protection; no electrical validation. |
| Generated project | Side-effect source clues archived separately | Not trusted until a later no-power generated-source review. |

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
- `workbench_foc_capture_blocker_2026-05-20.md`
- `workbench_tim1_adapter_followup_2026-05-20.md`
- `QIANSAI_STDRIVE101_TIM1_ADAPTER_POWER.no_power_candidate_2026-05-20.json`
- `QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER.no_power_candidate_2026-05-20.json`
- `QS_TIM1_OPAMP_PWR.no_power_candidate_2026-05-20.json`
- `logs/2026-05-20_connectAlgo_qiansai_pwm_blocker.log`
- `logs/2026-05-20_connectAlgo_tim1_adapter_pwm_pass_current_sensing_blocked.log`
- `screenshots/README.md`
- `QIANSAI_G474_STDRIVE101_FOC_P2_2026-05-21.stwb6`
- `MY-STDRIVE101_POWER_BOARD.foc_no_power_2026-05-21.json`
- `workbench_foc_capture_success_2026-05-21.md`
- `../2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/`

Related capture attempt from 2026-05-20:

- Workbench GUI selected `NUCLEO-G474RE`, custom
  `QIANSAI_STDRIVE101_PCB2_POWER`, and temporary `R57BLB50L2`.
- Workbench stopped with `DrivingHighAndLowSides No timer matches all signals
  requirement`.
- A no-power `TIM1_ADAPTER` candidate fixed the Workbench PWM-generation
  blocker in the GUI, but current sensing still showed red X.
- A no-power `TIM1_OPAMP_ADAPTER` candidate was created for the next GUI
  attempt. It is an adapter/rework candidate only, not current PCB2 proof.
- Read-only Workbench API confirmed the long-name OPAMP candidate was present
  in the user power-board list, even though the GUI search did not find it.
  A short-name alias `QS_TIM1_OPAMP_PWR` was added and installed for the next
  GUI attempt.
- The alias was also installed as a local Workbench app asset after the user
  still could not see it in the GUI:
  `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\assets\hardware\board\power\QS_TIM1_OPAMP_PWR.json`.
  After restarting Workbench, read-only verification showed it in
  `/api/hardware/app/power`.
- No `.stwb6` was saved from this attempt because `Create` remained disabled
  and no valid pre-generate save path was exposed.

Related new source clues from 2026-05-17:

- `hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.md`
- `hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`

Related new source clues from 2026-05-18:

- `hardware/motor/2026-05-18_57blf01_motor_wiring_definition.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-18_001_motor_wiring_definition.md`

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

This package now contains a reviewable Workbench FOC `.stwb6` with
`NUCLEO-G474RE`, `MY-STDRIVE101_POWER_BOARD`, `FOC`, three-shunt current
sensing, active-low driver protection on `PB12/TIM1_BKIN`, and Hall selected
as the main speed sensor. Packet A source evidence is no longer blocked at the
Workbench-GUI stage.

The next no-power action is a generated-source review of the archived
2026-05-21 Workbench project clues. No build-only clearance, flash, powered
test, Gate PWM output, Hall readiness, motor readiness, or sensorless readiness
is authorized.
