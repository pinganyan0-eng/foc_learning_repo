# Current Task

This is the current single task. It is a no-power documentation and evidence
governance task, not firmware implementation or hardware validation.

## Task ID

- ID: `TASK-2026-05-19-p2-packet-a-foc-route-decision-after-my-foc-rollback`
- Topic: Packet A FOC route decision after MY_FOC rollback
- Status: `ready`
- Risk Level: `L0 documentation / no-power governance`
- Definition of Done: `workflow/definition_of_done.md`
- Evidence ID: `EV-2026-05-19-P2-PACKET-A-FOC-ROUTE-DECISION-001`
- Review Required: yes

## Background

The latest Packet A work found a user-created Workbench project named
`MY_FOC`, but it was generated as `SIX_STEP`, not FOC. Codex then tried a
minimal source edit from `"algorithm": "sixStep"` to `"algorithm": "FOC"`.
Workbench failed to reload that edited `.stwb6`, and Codex restored the
external source from backup.

The project now needs a route decision that prevents another partial source
edit and tells the next Packet A attempt exactly what a valid no-power FOC
capture must contain.

## Feature Sentence

After the `MY_FOC` one-field manual FOC edit failed Workbench reload, the next
valid Packet A path is a Workbench GUI-created or otherwise complete
reviewable FOC source, not another partial `.stwb6` text edit.

## Rule Table

| Item | Decision |
| --- | --- |
| Allowed | Compare archived Workbench sources, create a route-decision artifact, update P2 readiness, user action queue, evidence register, current status, and tests. |
| User clarification | Pins can be changed; treat Hall/PWM mismatch as an editable future route, not a permanent rejection. |
| Not accepted | Manual one-field `.stwb6` algorithm edit, Packet A, generated-project trust, build-only clearance, generated source, FOC completion, current-sense readiness, fault readiness, Hall readiness, powered readiness. |
| Forbidden | No Generate, no build, no flash, no 24V, no power-board connection, no motor connection, no Gate PWM output, no Motor Profiler run, no Motor Pilot. |

## Input Files

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-19_my_foc_generated_project/MY_FOC.original_2026-05-19.stwb6`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-19_my_foc_generated_project/MY_FOC.codex_foc_candidate_2026-05-19.stwb6`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_005_my_foc_generated_project.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/my_foc_foc_candidate_edit_2026-05-19.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `workflow/evidence_register.md`
- `tests/test_workflow_contracts.py`

## Output Files

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_foc_route_decision_2026-05-19.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md`
- `workflow/ACTIVE_TASK.md`
- `workflow/evidence_register.md`
- `CURRENT_STATUS.md`
- `tests/test_workflow_contracts.py`
- `vector_store/chunks.jsonl`
- `vector_store/index.json`

## Acceptance Evidence

- Route-decision artifact exists and contains `Route narrowed / GUI-created
  FOC source required / Packet A still blocked`, `My_First_FOC.stwb6`,
  `MY_FOC.original_2026-05-19.stwb6`,
  `MY_FOC.codex_foc_candidate_2026-05-19.stwb6`,
  `Do not attempt another partial text edit`, `self-developed STDRIVE101
  board`, `current sensing`, `fault / break`, `Hall/PWM`, `No Generate`, and
  `No 24V`.
- P2 readiness snapshot includes the new route decision and keeps
  generated-project trust blocked.
- User action queue tells the user the minimum next Workbench GUI capture
  fields and hard stops.
- Evidence register has
  `EV-2026-05-19-P2-PACKET-A-FOC-ROUTE-DECISION-001`.
- `python -m unittest discover -s tests` passes.
- `git diff --check` passes or reports only known line-ending warnings.
- `python tools/build_vector_store.py` completes.

## Safety Boundary

This task does not authorize Generate, build, flash, 24V, power-board
connection, motor connection, Gate PWM output, Motor Profiler, Motor Pilot,
Hall closed-loop, or sensorless / SMO claims.

## Codex Result Area

- Execution status: ready; Packet A route decision added after `MY_FOC`
  rollback.
- Modified files: `packet_a_foc_route_decision_2026-05-19.md`,
  `p2_readiness_snapshot_2026-05-15.md`,
  `user_action_queue_2026-05-14.md`, `CURRENT_STATUS.md`,
  `workflow/evidence_register.md`, `tests/test_workflow_contracts.py`,
  `workflow/ACTIVE_TASK.md`, `vector_store/chunks.jsonl`, and
  `vector_store/index.json`.
- Evidence ID: `EV-2026-05-19-P2-PACKET-A-FOC-ROUTE-DECISION-001`
- Verification: `python -m unittest discover -s tests` passed with 64 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8291 chunks.
- Remaining risk: Packet A remains blocked until Workbench GUI or a complete
  reviewable `.stwb6` creates a valid FOC configuration with project
  self-developed/custom STDRIVE101 board identity, current sensing,
  fault/break, Hall/PWM, and motor-entry fields visible. All generated-project,
  build-only, and powered evidence remains blocked.

## Historical Tasks

- `TASK-2026-05-19-p2-my-foc-manual-foc-edit-rollback`: ready; manual FOC edit rollback completed.
- `TASK-2026-05-19-p2-my-foc-generated-project-source-review`: ready; MY_FOC generated project source review completed.
- `TASK-2026-05-19-p2-packet-a-board-designer-manager-gui-checklist`: ready; Board Designer / Manager GUI-only checklist completed.
- `TASK-2026-05-19-p2-packet-a-board-designer-manager-path-review`: ready; Board Designer / Board Manager path review completed.
- `TASK-2026-05-19-p2-software-hall-adapter-design-review`: ready; software Hall adapter design review completed.
- `TASK-2026-05-19-p2-current-pcb2-packet-a-firmware-feasibility`: ready; current PCB2 Packet A / firmware feasibility review completed.
- `TASK-2026-05-19-p2-current-pcb2-hall-pwm-strategy`: ready; current PCB2 Hall/PWM no-power strategy completed.
- `TASK-2026-05-19-p2-pcb2-mapping-pin1-protection-intake`: ready; current PCB2 mapping, pin-1 images, Hall clarification, and protection-chain source review completed.
- `TASK-2026-05-19-p2-min-hw-request-workbench-asset-probe`: ready; minimal hardware request and Workbench asset probe completed.
- `TASK-2026-05-19-p2-packet-a-workbench-capture-attempt`: blocked/stopped; Workbench did not capture an accepted self-made STDRIVE101 power-stage context.

## Suggested Commit Message

```text
docs: add packet a foc route decision
```
