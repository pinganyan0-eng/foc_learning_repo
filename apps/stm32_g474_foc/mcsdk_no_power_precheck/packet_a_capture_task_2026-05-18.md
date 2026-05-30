# Packet A Workbench Capture Task Package - 2026-05-18

This task package freezes the next no-power Packet A capture step. It is a
workflow artifact only: it does not add a Workbench source file, does not add
screenshots, and does not upgrade Packet A evidence.

## Gate

| Field | Decision |
| --- | --- |
| Project goal | Advance the STM32G474 FOC P2 no-power precheck by making the next Packet A Workbench capture executable. |
| Learning goal | Make clear why Packet A is still `Partial clue / Preparation only` and what the next capture must prove. |
| Change scope | Documentation and task-state records only. |
| Forbidden scope | No Workbench GUI launch, no source generation, no build, no flash, no 24V, no power-board connection, no motor connection, no Gate PWM, no Motor Profiler. |

## Feature Sentence

Create a ready-to-run no-power checklist for the future Workbench capture that
will produce the project-specific `.stwb6` and selected-field screenshots
needed for Packet A review.

## Current State

| Item | Current status | Decision |
| --- | --- | --- |
| Legacy `.stwb6` | `packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6` | `Partial clue`; not the custom-board source. |
| Custom capture package | `packet_a_sources/2026-05-16_custom_nucleo_stdrive101/` | Prepared only; no accepted `.stwb6` or screenshots yet. |
| Vendor motor source | `57BLF01_VENDOR_CANDIDATE` | Label only; supplier clue, not measured data. |
| G431/G474 pin comparison | Local MCSDK assets support compared key rows | MCU pin-function concern reduced; no CN8 routing proof. |
| Packet A decision | `Partial clue / Preparation only` | Generated-project trust remains `Not allowed`. |
| Packet B/C and PB3/SWO | Blocked or partial clue only | Keep all blockers visible. |

## Future Output Paths

The future GUI capture should save the Workbench project here:

`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/custom_nucleo_stdrive101_2026-05-16.stwb6`

The future screenshots should be saved under:

`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/`

Required screenshot names:

- `2026-05-16_workbench_project_hw_info.png`
- `2026-05-16_workbench_pwm_generation.png`
- `2026-05-16_workbench_current_sensing.png`
- `2026-05-16_workbench_speed_sensing_hall.png`
- `2026-05-16_workbench_driver_protection.png`
- `2026-05-16_workbench_pin_usage.png`

Do not rename the package to 2026-05-18. The 2026-05-18 artifact is this task
package; the capture target remains the already prepared 2026-05-16 Packet A
source directory.

## Field Acceptance Matrix

| Field group | Future capture must show | Accept only if visible in source |
| --- | --- | --- |
| Tool context | ST MC Workbench / MCSDK version or project metadata | Yes. |
| MCU / board | `NUCLEO-G474RE` and `STM32G474RETx` | Yes. |
| Power stage | Custom / Generic STDRIVE101-compatible power stage, not `EVALSTDRIVE101` | Yes. |
| Algorithm | FOC | Yes. |
| Speed feedback | Hall as the first bring-up fallback; sensorless not selected as the first path | Yes. |
| Motor entry | `57BLF01_VENDOR_CANDIDATE` only if a motor entry is required | Treat as supplier clue only. |
| Current sensing | 3-shunt and OPAMP/PGA or ADC selection | Configuration evidence only, not measurement evidence. |
| PWM | TIM1 complementary high-side / low-side topology | Configuration evidence only, not Gate PWM behavior. |
| Fault input | `PB12/TIM1_BKIN` or the GUI-selected break/fault input | Requires Packet B/C later for board-route proof. |
| UART policy | `PA2/PA3` not reused as default FOC UART unless conflict is explicitly resolved | Keep policy visible. |
| `PB3` ownership | SWO or Hall B decision | Remains blocked unless SWO release / isolation evidence exists. |

## Stop Conditions

Stop and record the blocker instead of improvising if:

- Workbench forces `EVALSTDRIVE101` for this custom-board capture.
- Workbench requires generating code before saving the `.stwb6`.
- Workbench requires powered hardware, Motor Profiler, Motor Pilot, or any live
  motor step.
- The GUI silently reuses `PA2/PA3` or `PB3` contrary to current blocker policy.
- The motor setup requires treating supplier values as measured Motor Profiler
  data.
- Any step would change generated source, firmware, CubeMX/MCSDK project
  output, or hardware behavior in this no-GUI documentation pass.

## Review Procedure After Future Capture

1. Reopen the saved `.stwb6` in Workbench.
2. Create a dated Packet A source review from
   `source_packet_review_template_2026-05-14.md`.
3. Upgrade only fields visible in the `.stwb6` or screenshots.
4. Keep Packet B/C, `DT/MODE`, `STBY`, STM32 endpoint mapping, `J_HALL`
   numbering, and PB3/SWO blockers unchanged unless separate accepted evidence
   exists.
5. Update `evidence_packet_2026-05-14.md`,
   `p2_readiness_snapshot_2026-05-15.md`, and `workflow/evidence_register.md`
   with the exact limits.
6. Run `python -m unittest discover -s tests`.

## Acceptance Criteria For This 2026-05-18 Task Package

- This file exists and names the exact future `.stwb6` and screenshot paths.
- `workflow/ACTIVE_TASK.md` points to this no-power Packet A capture
  preparation task.
- P2 status files mention this as workflow-only task governance.
- Packet A remains `Partial clue / Preparation only`.
- Generated-project trust remains `Not allowed`.
- No GUI, generated source, build, flash, power, Gate PWM, Motor Profiler,
  Hall, motor, power-stage, or sensorless claim is added.
