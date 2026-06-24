# Main Agent Priority Matrix And Subagent Tracking

Date: 2026-06-23

## Decision

`Main-agent priority matrix / sensorless FOC first / filtered subagent task queue / no firmware implementation / no generated-code edit / no hardware action`.

## Startup Sources

The main agent startup for this work used:

- `AI_CONTEXT.md`
- `workflow/CURRENT_SNAPSHOT.md`
- `workflow/ACTIVE_TASK.md`
- `CURRENT_STATUS.md`
- `AGENTS.md`
- `workflow/SUBAGENT_PROTOCOL.md`
- `docs/00_project_truth/project_context.md`
- `docs/00_project_truth/ai_architecture.md`

`workflow/SUBAGENT_PROTOCOL.md` is a compatibility stub. The authoritative
protocol remains `docs/00_project_truth/ai_architecture.md` under
`## Subagent Communication Protocol`: subagents are scoped helpers, not
parallel owners; the main agent keeps the task contract, filters context, and
merges decision-relevant summaries before repo writes or user-facing claims.

## Priority Matrix

| Priority | Task lane | Why it matters now | Current status | Next deliverable |
| --- | --- | --- | --- | --- |
| P0 | Sensorless host-side command/replay semantics | This directly advances the no-power algorithm evidence chain without touching firmware or hardware. | Positive-to-reverse target-omega crossing replay added in the current increment. | Add the next missing host-side replay fixture only after this evidence is verified and registered. |
| P0 | Evidence registration and workflow contracts | The project relies on status/evidence files as durable truth for future agents and teacher review. | Current increment is being registered in review/status/evidence docs and workflow tests. | Passing focused tests, workflow contract tests, full unittest discovery, compileall, AI contract check, and diff check. |
| P1 | MCSDK source-backed sensorless boundary review | This is useful for future comparison planning, but only if it stays source-backed and no-power. | Existing generated-source boundary says archived MCSDK remains Hall-based with generic CORDIC/STO support symbols. | A scoped read-only review or fixture that maps exactly one source-backed boundary row, not an integration claim. |
| P1 | Reality-useful hardware fault-tree packet | Physical progress remains blocked by STDRIVE101 power-board-side `nFAULT = 1.3 V`. | Needs no-power source-photo / EDA crop packet and confidently identified DMM rows from the user/teacher path. | A no-power evidence packet template/checklist update if the user supplies images or raw rows. |
| P2 | Firmware-entry planning | Firmware work is not opened while no-power and hardware blockers remain. | Plans exist, but no implementation permission is open. | Keep as future planning only; do not edit generated or firmware files. |
| P2 | Presentation/demo material | Useful later, but weaker than algorithm evidence and hardware blocker removal. | Existing reports are evidence-heavy; no new demo is justified by current state. | Summarize only after verified evidence accumulates. |

## Active Subagent Tracking

Filtered subagent digest: read-only helper Kuhn identified the crossing
fixture gap, and read-only helper Feynman confirmed the priority/order
boundary. The main agent kept all repo writes and final claims.

| Helper | Scope | Output used by main agent | Status |
| --- | --- | --- | --- |
| Kuhn | Read-only frontend/bridge fixture slice around signed reverse and rate-limit replay. | Identified missing locked positive-to-reverse target-omega crossing through zero. | Integrated into current algorithm fixture decision. |
| Feynman | Read-only priority matrix and next subtask queue review. | Confirmed P0 status alignment for the crossing fixture, P1 fixture parity / MCSDK boundary follow-up, and P2 no-power hardware fault-tree input. | Integrated into this matrix and status update. |

## Next Scoped Subagent Packets

These packets are allowed only as filtered helper work unless the main agent
explicitly changes the assignment later.

- `sensorless-next-gap-explorer`: read only
  `src/foc_sensorless_frontend.py`,
  `tests/test_foc_sensorless_frontend.py`,
  `tests/fixtures/foc_sensorless_frontend_vectors.json`, and the latest
  review artifacts; return the smallest next host-side no-power replay gap.
- `mcsdk-boundary-row-explorer`: read only archived generated-source boundary
  review artifacts and `tests/test_mcsdk_sensorless_observer_boundary_static.py`;
  return one source-backed boundary row that could be protected without
  claiming MCSDK observer equivalence.
- `hardware-packet-checker`: read only latest STDRIVE101 `nFAULT = 1.3 V`
  review/status records; return missing no-power photo/DMM rows and wording
  constraints for a future user/teacher packet.

## Safety Boundary

This matrix does not authorize firmware logic edits, generated-code edits,
Workbench/CubeMX edits, flash, Run / Debug, 24 V, power-board connection,
motor connection, Gate PWM output, Motor Pilot, Motor Profiler, Hall
closed-loop claims, sensorless / SMO claims, power-stage readiness, or motor
readiness.

The current physical blocker remains the STDRIVE101 power-board-side
`nFAULT = 1.3 V` fault-isolation result. The current algorithm work is
host-side no-power evidence only.

## Verification

`python -m json.tool tests\fixtures\foc_sensorless_frontend_vectors.json`
passed; `python -m json.tool tests\fixtures\foc_mcsdk_bridge_vectors.json`
passed; `python -m unittest tests.test_foc_sensorless_frontend
tests.test_foc_sensorless_frontend_vectors tests.test_mcsdk_foc_bridge_vectors`
passed: 42 tests OK; `python -m unittest
tests.test_workflow_contracts.FocCoreHostModelWorkflowTests` passed:
37 tests OK; `python -m unittest tests.test_workflow_contracts` passed:
153 tests OK; full `python -m unittest discover -s tests` passed:
308 tests OK; `python -m compileall src tests` passed;
`python tools\check_ai_contracts.py` passed with no AI contract errors and
the known `ACTIVE_TASK.md` review-lifecycle warning; `git diff --check`
passed with only LF/CRLF conversion warnings.
