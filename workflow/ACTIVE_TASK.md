# Current Task

This is the current single task. It is a no-power documentation and evidence
governance task, not firmware implementation or hardware validation.

## Task ID

- ID: `TASK-2026-05-19-p2-my-foc-manual-foc-edit-rollback`
- Topic: P2 MY_FOC manual FOC edit rollback
- Status: `ready`
- Risk Level: `L0 documentation / no-power governance`
- Definition of Done: `workflow/definition_of_done.md`
- Evidence ID: `EV-2026-05-19-P2-MY-FOC-FOC-CANDIDATE-EDIT-001`
- Review Required: yes

## Background

The user asked Codex to modify the `MY_FOC` project after the source review
showed that the generated project was `SIX_STEP`. Codex tried a minimal
top-level `.stwb6` source edit from `"algorithm": "sixStep"` to
`"algorithm": "FOC"`. The user then reported a Workbench GUI load failure:
`一般错误 / 无法加载文件:
C:/Users/gregrg/.st_workbench/projects/MY_FOC.stwb6`.

The active task is now to record that failed edit, keep the failed candidate as
negative evidence, and restore the external Workbench source file from backup.

## Feature Sentence

Restore `MY_FOC.stwb6` to the original loadable six-step source and record that
the one-field manual FOC edit is not a valid Workbench conversion path.

## Rule Table

| Item | Decision |
| --- | --- |
| Allowed | Restore external `MY_FOC.stwb6` from the backup, archive the failed manual FOC candidate as negative evidence, update status/evidence entry points, tests, and vector index. |
| User clarification | Pins can be changed; treat Hall/PWM mismatch as an editable future route, not a permanent rejection. |
| Not accepted | Manual `.stwb6` algorithm edit as a valid FOC conversion, Packet A, generated-project trust, build-only clearance, generated source, FOC completion, current-sense readiness, fault readiness, Hall readiness, powered readiness. |
| Forbidden | No Generate, no build, no flash, no 24V, no power-board connection, no motor connection, no Gate PWM output, no Motor Profiler run, no Motor Pilot. |

## Input Files

- `C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6`
- `C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6.pre_codex_foc_edit_2026-05-19.bak`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `workflow/evidence_register.md`
- `tests/test_workflow_contracts.py`

## Output Files

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/my_foc_foc_candidate_edit_2026-05-19.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_005_my_foc_generated_project.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-19_my_foc_generated_project/`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md`
- `workflow/ACTIVE_TASK.md`
- `workflow/evidence_register.md`
- `CURRENT_STATUS.md`
- `tests/test_workflow_contracts.py`
- `vector_store/chunks.jsonl`
- `vector_store/index.json`

## Acceptance Evidence

- MY_FOC edit record exists and contains `MY_FOC.stwb6`,
  `Manual FOC source edit failed Workbench reload`, `rolled back`,
  `"algorithm": "sixStep"`, `pre_codex_foc_edit_2026-05-19.bak`,
  `No Generate`, `No build`, `No 24V`, `No Gate PWM output`,
  `No Motor Profiler run`, `Packet A still not accepted`, and
  `no generated-project trust`.
- The generated-project review still records `SIX_STEP` generated outputs,
  `R57BLB50L2`, `Number.NaN`, and the user's statement that pins can be
  changed.
- P2 readiness still keeps generated-project trust and build-only clearance
  blocked.
- `python -m unittest discover -s tests` passes.
- `git diff --check` passes or reports only known line-ending warnings.
- `python tools/build_vector_store.py` completes.

## Safety Boundary

This task does not authorize Generate, build, flash, 24V, power-board
connection, motor connection, Gate PWM output, Motor Profiler, Motor Pilot,
Hall closed-loop, or sensorless / SMO claims.

## Codex Result Area

- Execution status: ready; external `MY_FOC.stwb6` was restored from backup
  after the manual `sixStep` to `FOC` source edit failed Workbench reload.
- Modified files: `my_foc_foc_candidate_edit_2026-05-19.md`,
  `source_packet_review_2026-05-19_005_my_foc_generated_project.md`,
  `packet_a_sources/2026-05-19_my_foc_generated_project/`,
  `p2_readiness_snapshot_2026-05-15.md`, `README.md`,
  `evidence_packet_2026-05-14.md`, `user_action_queue_2026-05-14.md`,
  `CURRENT_STATUS.md`, `workflow/evidence_register.md`,
  `tests/test_workflow_contracts.py`, `workflow/ACTIVE_TASK.md`,
  `vector_store/chunks.jsonl`, and `vector_store/index.json`. External file
  restored: `C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6`; external
  backup used: `C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6.pre_codex_foc_edit_2026-05-19.bak`.
- Evidence ID: `EV-2026-05-19-P2-MY-FOC-FOC-CANDIDATE-EDIT-001`
- Verification: `python -m unittest discover -s tests` passed with 61 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8276 chunks. Read-back confirmed
  external `MY_FOC.stwb6` now has `"algorithm": "sixStep"` and its hash
  matches the backup.
- Remaining risk: Packet A remains blocked until Workbench GUI or a full
  reviewable `.stwb6` creates a valid FOC configuration with complete
  motor/startup/current-sense, fault, and Hall/PWM route settings. All
  generated-project, build-only, and powered evidence remains blocked.

## Historical Tasks

- `TASK-2026-05-19-p2-my-foc-generated-project-source-review`: ready; MY_FOC generated project source review completed.
- `TASK-2026-05-19-p2-packet-a-board-designer-manager-gui-checklist`: ready; Board Designer / Manager GUI-only checklist completed.
- `TASK-2026-05-19-p2-packet-a-board-designer-manager-path-review`: ready; Board Designer / Board Manager path review completed.
- `TASK-2026-05-19-p2-software-hall-adapter-design-review`: ready; software Hall adapter design review completed.
- `TASK-2026-05-19-p2-current-pcb2-packet-a-firmware-feasibility`: ready; current PCB2 Packet A / firmware feasibility review completed.
- `TASK-2026-05-19-p2-current-pcb2-hall-pwm-strategy`: ready; current PCB2 Hall/PWM no-power strategy review completed.
- `TASK-2026-05-19-p2-pcb2-mapping-pin1-protection-intake`: ready; current PCB2 mapping, pin-1 images, Hall clarification, and protection-chain source review completed.
- `TASK-2026-05-19-p2-min-hw-request-workbench-asset-probe`: ready; minimal hardware request and Workbench asset probe completed.
- `TASK-2026-05-19-p2-packet-a-workbench-capture-attempt`: blocked/stopped; Workbench did not capture an accepted self-made STDRIVE101 power-stage context.

## Suggested Commit Message

```text
docs: add packet a board designer gui checklist
```
