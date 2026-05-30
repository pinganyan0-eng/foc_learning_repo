# Current Task

This is the current single task. It records the no-power software Hall firmware
entry plan for the future `PA0/PA1/PB4` adapter. It is not STM32 firmware
implementation, not generated-code editing, not CubeMX / Workbench editing,
not flashing, not Run / Debug, not hardware validation, and not powered
testing.

## Current Workflow Guard Addendum

- User-reported issue: Codex kept drifting into concept teaching even though the
  dual-teacher workflow says ChatGPT should teach pure theory.
- Hotfix task:
  `TASK-2026-05-28-workflow-dual-teacher-concept-guard`.
- Evidence:
  `EV-2026-05-28-WORKFLOW-DUAL-TEACHER-CONCEPT-GUARD-001`.
- Decision:
  `Dual-teacher concept-only role guard / ChatGPT teaches theory / Codex reviews records and executes repo work`.
- Boundary: workflow-control only; no firmware, no Workbench regeneration, no
  flash, no 24V, no power-board connection, no motor connection, no Gate PWM,
  no Motor Profiler, no Hall closed-loop, and no powered readiness.

## Task ID

- ID: `TASK-2026-05-28-p2-software-hall-firmware-entry-plan`
- Topic: software Hall firmware-entry plan for future debug-only
  `PA0/PA1/PB4` adapter
- Status: `done`
- Risk Level: `L1 no-power design boundary / no firmware / no hardware`
- Definition of Done: `workflow/definition_of_done.md`
- Evidence ID:
  `EV-2026-05-28-P2-SOFTWARE-HALL-FIRMWARE-ENTRY-PLAN-001`
- Related build-only task:
  `TASK-2026-05-27-p2-qiansai-g474-stdrive101-foc-p2-debug-build-only`
- Related MCSDK interface task:
  `TASK-2026-05-27-p2-software-hall-mcsdk-speed-position-feedback-interface-review`
- Related hardware gate:
  `TASK-2026-05-22-p2-dmm-continuity-short-check-request`
- Review Required: yes

## Background

PCB2 is still unpopulated. DMM continuity / short-check evidence is deferred,
not passed. Deferred does not mean passed.

The external Workbench project must remain stable at:

`C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`

The no-power Debug build-only task already recorded local compile evidence.
That build-only pass does not prove current PCB2 physical routing, GPIO/EXTI
runtime behavior, MCSDK Hall integration, Gate PWM safety, Hall closed-loop
behavior, motor readiness, power-stage readiness, or sensorless validation.

## Feature Sentence

The project now has a Chinese-first no-power firmware-entry plan:

```text
accepted current route PA0/PA1/PB4
-> future GPIO/EXTI debug-only capture
-> ISR stores raw_state + timestamp + event count only
-> low-priority state machine rejects 000/111, repeats, bounce candidates, and abnormal jumps
-> low-frequency debug snapshot exposes direction_candidate and speed_candidate
-> no MCSDK hook, no firmware implementation, no Hall readiness
```

## Evidence Decision

- Decision:
  `Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.
- Evidence level: L1 no-power design-boundary evidence.
- New artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_plan_2026-05-28.md`.
- Current route:
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- Fixed constraint: `PB3=LIN1`; it is not current Hall.
- Generated-route reminder: MCSDK standard TIM2 Hall `PA15/PB3/PB10` is
  generated-source evidence only, not current PCB2 Hall proof.
- This artifact is not usable to claim firmware implementation, MCSDK Hall
  integration, MCSDK hook readiness, DMM continuity, Gate PWM safety, Hall
  closed-loop, motor readiness, power-stage readiness, or sensorless
  validation.

## Input Files

- `workflow/CURRENT_SNAPSHOT.md`
- `CURRENT_STATUS.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_checklist_2026-05-27.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_gpio_exti_boundary_review_2026-05-27.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_timestamp_source_review_2026-05-27.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_debug_output_route_review_2026-05-27.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md`

## Output Files

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_plan_2026-05-28.md`
- `CURRENT_STATUS.md`
- `AI_CONTEXT.md`
- `workflow/ACTIVE_TASK.md`
- `workflow/CURRENT_SNAPSHOT.md`
- `workflow/evidence_register.md`
- `workflow/current_learning_sprint.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md`
- `deliverables/submission_checklist.md`
- `tests/test_workflow_contracts.py`

## Carry-Forward Build-Only Contract

The earlier build-only evidence remains active context, but it is not the
current task.

- `TASK-2026-05-27-p2-qiansai-g474-stdrive101-foc-p2-debug-build-only` /
  `EV-2026-05-27-P2-QIANSAI-G474-STDRIVE101-FOC-P2-BUILD-ONLY-001`:
  `No-power build-only Debug pass / local toolchain compiles generated project / no firmware runtime or hardware readiness`.
- Build command:
  `cmake --build "C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2\build\Debug" --config Debug`.
- Result: exit code `0`; Ninja output `ninja: no work to do`.
- Confirmed artifacts:
  `QIANSAI_G474_STDRIVE101_FOC_P2.elf` and
  `QIANSAI_G474_STDRIVE101_FOC_P2.map`.
- The record is `not a clean rebuild record`; it is local no-power compile
  evidence only.

## Carry-Forward Software Hall Contracts

These prior no-power software Hall records remain active context for safety and
review. They are not usable to claim firmware implementation, MCSDK Hall
integration, Hall closed-loop behavior, Gate PWM safety, motor readiness,
power-stage readiness, or sensorless validation.

Stable carry-forward phrases:

- not usable to claim firmware implementation
- Not usable to claim firmware implementation
- not firmware or hardware readiness

- `TASK-2026-05-22-p2-software-hall-no-power-algorithm-prep` /
  `EV-2026-05-22-P2-SOFTWARE-HALL-ALGORITHM-PREP-001`:
  `Algorithm-side no-power preparation only`; `Deferred does not mean passed`.
- `TASK-2026-05-22-p2-software-hall-state-machine-exercise` /
  `EV-2026-05-22-P2-SOFTWARE-HALL-STATE-MACHINE-EXERCISE-001`:
  `Software Hall state-machine exercise`; `Waiting for user answer`; learning
  check only.
- `TASK-2026-05-27-p2-software-hall-adapter-pseudocode-draft` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-PSEUDOCODE-DRAFT-001`:
  `Pseudocode draft added / no firmware implementation / no MCSDK Hall integration / no Hall readiness`;
  DMM remains deferred, not passed.
- `TASK-2026-05-27-p2-software-hall-followup-review` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-FOLLOWUP-REVIEW-001`:
  `L4 table-level no-power Hall state-machine classification / no firmware implementation / no hardware validation`.
- `TASK-2026-05-27-p2-software-hall-processing-order-card` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-PROCESSING-ORDER-CARD-001`:
  `Software Hall Adapter Processing-Order Card`; L1 repair artifact, not a new
  mastery upgrade.
- `TASK-2026-05-27-p2-software-hall-host-model` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-HOST-MODEL-001`:
  `Host-side software Hall reference model / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-golden-vectors` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-GOLDEN-VECTORS-001`:
  `Host-side software Hall golden vectors / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-mcsdk-integration-probe` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-INTEGRATION-PROBE-001`:
  `MCSDK Hall integration points identified as read-only clues / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-firmware-entry-checklist` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-FIRMWARE-ENTRY-CHECKLIST-001`:
  `Software Hall firmware-entry checklist / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-gpio-exti-boundary` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-GPIO-EXTI-BOUNDARY-001`:
  `Software Hall GPIO/EXTI boundary review draft / no firmware implementation / no GPIO runtime proof / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-timestamp-source-review` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-TIMESTAMP-SOURCE-001`:
  `Software Hall timestamp-source review draft / no firmware implementation / no timer configuration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-debug-output-route-review` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-DEBUG-OUTPUT-ROUTE-001`:
  `Software Hall low-frequency debug-output route review draft / no firmware implementation / no UART implementation / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-mcsdk-firmware-integration-boundary` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-FIRMWARE-INTEGRATION-BOUNDARY-001`:
  `Software Hall MCSDK firmware-integration boundary review draft / no firmware implementation / no MCSDK hook / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-mcsdk-hook-evidence-request-checklist` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-HOOK-EVIDENCE-REQUEST-001`:
  `Software Hall MCSDK hook evidence request checklist / no firmware implementation / no MCSDK hook / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-mcsdk-speed-position-feedback-interface-review` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-SPEED-POSITION-INTERFACE-001`:
  `Software Hall MCSDK speed/position feedback interface review / no firmware implementation / no MCSDK hook / no Hall readiness`.

## Next User Checkpoint

No hardware action is needed from the algorithm side while PCB2 is unpopulated.
Keep the external Workbench project path stable. If hardware teammates finish
soldering or change Hall lines, `PB3=LIN1`, `P14/P15=3V3/GND`, or
`nFAULT->PB12`, report it immediately.

After soldering, resume the no-power DMM continuity / short-check table before
any firmware adapter, flash, Run / Debug, or powered work.

## Verification

Pending in this task until repo checks are rerun:

- `python -m unittest discover -s tests`
- `python -m compileall src tests`
- `git diff --check`
- `python tools\check_ai_contracts.py`
- `python tools\build_vector_store.py`

## Safety Boundary

This task does not authorize firmware logic edits, generated-code edits,
CubeMX/Workbench edits, flash, Run / Debug, 24V, power-board connection, motor
connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
sensorless / SMO claims.
