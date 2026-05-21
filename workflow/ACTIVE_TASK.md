# Current Task

This is the current single task. It is a no-power documentation and evidence
governance task, not firmware implementation or hardware validation.

## Task ID

- ID: `TASK-2026-05-21-packet-a-workbench-foc-source-capture`
- Topic: Packet A Workbench FOC source capture
- Status: `ready`
- Risk Level: `L0 documentation / no-power governance`
- Definition of Done: `workflow/definition_of_done.md`
- Evidence ID: `EV-2026-05-21-P2-WORKBENCH-FOC-SOURCE-CAPTURE-001`
- Review Required: yes

## Background

The user completed a no-power ST Motor Control Workbench 6.4.2 GUI route for
`QIANSAI_G474_STDRIVE101_FOC_P2` using `NUCLEO-G474RE`,
`MY-STDRIVE101_POWER_BOARD`, `FOC`, three-shunt current sensing, active-low
driver protection, and Hall main speed sensing.

The next safe Codex-side progress is to archive the `.stwb6`, power-board JSON,
screenshot evidence, and selected generated-source clues, then keep build and
hardware gates closed pending a separate source review.

## Feature Sentence

Packet A now has a reviewable no-power Workbench FOC source package, while
generated-source trust, build-only clearance, and hardware readiness remain
blocked.

## Rule Table

| Item | Decision |
| --- | --- |
| Allowed | Archive Workbench `.stwb6`, power-board JSON, screenshot evidence, selected generated-source clues, and update status/evidence docs. |
| Not accepted | Generated-project trust, build-only clearance, continuity proof, Hall readiness, motor readiness, power-stage readiness, powered readiness. |
| Forbidden | No Generate, no build, no flash, no 24V, no power-board connection, no motor connection, no Gate PWM output, no Motor Profiler run, no Motor Pilot. |

## Input Files

- `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2.stwb6`
- `C:\Users\gregrg\.st_workbench\hardware\board\power\MY-STDRIVE101_POWER_BOARD.json`
- `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2\`

## Output Files

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/QIANSAI_G474_STDRIVE101_FOC_P2_2026-05-21.stwb6`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/MY-STDRIVE101_POWER_BOARD.foc_no_power_2026-05-21.json`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/workbench_foc_capture_success_2026-05-21.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/`
- `CURRENT_STATUS.md`
- `workflow/evidence_register.md`

## Acceptance Evidence

- Archived `.stwb6` reads back as `algorithm: FOC`, `NUCLEO-G474RE`,
  `STM32G474RETx`, `MY-STDRIVE101_POWER_BOARD`, `HallEffectSensor`, and
  `speedSensorMode: hall`.
- Power-board JSON records `CURRENT_AMPL_U/V/W -> ML30/MR24/ML34` and
  `DP_TRIGGER -> MR16`.
- Workbench connection output records `PB12/TIM1_BKIN`, `TIM1` complementary
  PWM, and `TIM2` Hall.
- Evidence register includes the new Packet A capture while keeping generated
  source and hardware readiness blocked.
- `git diff --check` passes or reports only known line-ending warnings.

## Safety Boundary

This task does not authorize Generate, build, flash, 24V, power-board
connection, motor connection, Gate PWM output, Motor Profiler, Motor Pilot,
Hall closed-loop, or sensorless / SMO claims.
