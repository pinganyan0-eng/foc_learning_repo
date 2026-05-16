# Workbench No-Power Configuration Guide - 2026-05-16

This guide is the hand-run path for creating a new project-specific Workbench
configuration for Packet A.

It is not a generation instruction, not a build instruction, not a wiring
instruction, and not hardware validation.

## Feature Sentence

Create a saved MCSDK 6 Workbench configuration for `NUCLEO-G474RE` plus the
self-made STDRIVE101 power board so Packet A can review planned PWM, current
sensing, Hall, fault, UART, and pin ownership fields under no-power rules.

## Rule Table

| Rule | Required action |
| --- | --- |
| Do not reuse the old learning file | Do not treat `My_First_FOC.stwb6` as the new source. |
| Do not select the wrong power board | Do not select `EVALSTDRIVE101` for this project-specific capture. |
| Keep the control context stable | Use `NUCLEO-G474RE` / `STM32G474RETx`. |
| Keep the first feedback conservative | Select Hall as the first bring-up fallback. |
| Keep motor data honest | Use placeholder motor data until no-power records are filled. |
| Keep current sensing explicit | Select 3-shunt and prefer internal OPAMP/PGA where the GUI allows it. |
| Keep generated code blocked | Save the Workbench project and screenshots only. |

## Function Responsibilities

| Area | Responsibility in this step |
| --- | --- |
| Workbench GUI | Create and save the planned configuration source. |
| Screenshots | Prove visible selected fields for later review. |
| Motor measurement log | Record no-power motor clues without claiming Profiler data. |
| Pin assignment table | Track planned Workbench selections versus STM32 AF, CN8, and blocker status. |
| Source packet review | Decide which fields are accepted, candidate-only, blocked, or rejected. |

## GUI Steps

1. Launch `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\STMCWB.exe`.
2. Select `New Project`.
3. Select `FOC`.
4. Select control board `NUCLEO-G474RE` and MCU `STM32G474RETx`.
5. Select a Custom / Generic inverter or equivalent user power-stage path.
6. Do not select `EVALSTDRIVE101`.
7. Use a placeholder motor named `PLACEHOLDER_not_profiled_2026-05-16`.
8. Select Hall as the main speed feedback path.
9. Do not enable sensorless / SMO as the main path.
10. Select 3-shunt current sensing.
11. Prefer internal OPAMP/PGA amplification if available for the selected board.
12. Select TIM1 high-side and low-side complementary PWM.
13. Keep `PB12/TIM1_BKIN` as the draft break / fault candidate if accepted by
    the GUI.
14. Keep `PA2/PA3` out of default FOC UART usage unless the GUI explicitly
    proves the conflict is resolved.
15. Keep `PB3` as blocked for Hall B until SWO release / isolation evidence is
    available.
16. Save the Workbench project as
    `custom_nucleo_stdrive101_2026-05-16.stwb6` in this directory.
17. Do not click any command that generates source code or launches CubeMX code
    generation.

## Required Screenshots

Save screenshots under `screenshots/`:

| Screenshot | Must show |
| --- | --- |
| `2026-05-16_workbench_project_hw_info.png` | Workbench version, algorithm, board / MCU, custom power-stage context. |
| `2026-05-16_workbench_pwm_generation.png` | TIM1 high / low side or equivalent PWM topology. |
| `2026-05-16_workbench_current_sensing.png` | 3-shunt and OPAMP/PGA or ADC selection. |
| `2026-05-16_workbench_speed_sensing_hall.png` | Hall selected and sensorless not selected as the main first path. |
| `2026-05-16_workbench_driver_protection.png` | Fault / break / OCP choices visible if the GUI provides them. |
| `2026-05-16_workbench_pin_usage.png` | Pin conflicts and pin ownership summary. |

## Stop Conditions

Stop and record the reason if:

- the only available path forces `EVALSTDRIVE101`;
- Workbench cannot create a Custom / Generic power stage;
- Workbench requires code generation before saving `.stwb6`;
- the GUI silently reuses `PA2/PA3` or `PB3` in a way that conflicts with the
  current blocker policy;
- Workbench requires powered hardware, Motor Profiler, or Motor Pilot.

## Validation After Capture

After the real `.stwb6` and screenshots exist:

1. Reopen the `.stwb6` in Workbench.
2. Fill a dated source review from
   `../../source_packet_review_template_2026-05-14.md`.
3. Upgrade only fields visible in the source.
4. Keep Packet B/C and PB3/SWO blockers unless separate accepted evidence
   exists.
5. Run `python -m unittest discover -s tests`.
