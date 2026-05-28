# 2026-05-27 Hall state-machine review completed

## Status

Completed in Codex chat on 2026-05-27.

## Result

The user correctly classified:

| Input | Expected result | User result |
| --- | --- | --- |
| `100 -> 110` | Forward adjacent, count edge, not abnormal | Correct |
| `100 -> 101` | Reverse adjacent, count edge, not abnormal | Correct |
| `100 -> 011` | Abnormal jump, do not count normal edge | Correct |
| `000` | Illegal state, do not count edge | Correct |
| `111` | Illegal state, do not count edge | Correct |

## Evidence Meaning

- This supports L4 table-level Hall state-machine classification.
- It does not support firmware implementation, GPIO/EXTI runtime behavior,
  MCSDK Hall integration, Motor Profiler readiness, Gate PWM safety, power-board
  readiness, motor readiness, Hall closed-loop, or sensorless / SMO validation.

## Next Item

Next review before code:

```text
Explain the software Hall adapter processing order:
raw read -> illegal-state check -> first-valid check -> repeated-state check
-> bounce/timing check -> forward/reverse adjacent check -> abnormal-jump count.
```

Also explain why `PB3=LIN1` remains outside Hall and why DMM continuity /
short-check evidence is still required before firmware work.
