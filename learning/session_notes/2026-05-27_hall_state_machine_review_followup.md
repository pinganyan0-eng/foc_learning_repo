# 2026-05-27 Hall state-machine follow-up review

## Context

- Project stage: P2 no-power.
- Hardware state: PCB2 not soldered; no DMM continuity / short-check result.
- Current route: `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- Pin constraint: `PB3 = LIN1`; PB3 is not available as Hall.
- Scope: software Hall state-machine table review only.

## User Answer Reviewed

Candidate sequence:

```text
001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001
```

User table:

| Input | User judgment | Count edge? | Abnormal? | Codex review |
| --- | --- | --- | --- | --- |
| `100 -> 110` | Legal forward step | Yes | No | Correct: adjacent in the candidate forward sequence. |
| `100 -> 101` | Legal reverse step | Yes | No | Correct: adjacent in the reverse direction. |
| `100 -> 011` | Illegal jump / skipped code | No | Yes | Correct: non-adjacent jump; do not treat as normal rotation. |
| `000` | Illegal Hall state | No | Yes | Correct: not one of the six valid Hall states. |
| `111` | Illegal Hall state | No | Yes | Correct: not one of the six valid Hall states. |

## Evidence Level

- Evidence level: L4 for table-level no-power Hall state-machine classification.
- Confidence: medium-high for concept transfer.
- Reason: the user correctly solved a new state set after the earlier guided table.
- Not L5: no firmware implementation, no GPIO/EXTI test, no serial log,
  no MCSDK Hall integration, no DMM proof, no build record, no Gate PWM,
  no power board, and no motor evidence exists.

## No-Power Boundary

This record is learning evidence only. It does not authorize:

- firmware implementation;
- MCSDK Hall integration;
- Motor Profiler / Motor Pilot;
- 24V;
- power-board connection;
- motor connection;
- Gate PWM output;
- Hall closed-loop claim;
- sensorless / SMO claim.

## Next Review

Before code, ask the user to restate the adapter processing order without a table:

```text
raw read -> illegal-state check -> first-valid check -> repeated-state check
-> bounce/timing check -> forward/reverse adjacent check -> abnormal-jump count
```

Then ask why this still cannot enter firmware until the DMM table and GPIO/EXTI boundary are reviewed.
