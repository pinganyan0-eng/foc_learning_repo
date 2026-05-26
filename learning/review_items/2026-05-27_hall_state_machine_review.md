# 2026-05-27 Hall state machine review item

## Due

Next Hall-related learning turn, before any GPIO/EXTI implementation.

## Prompt

Given the candidate Hall sequence:

```text
001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001
```

Classify these inputs:

| Input | Judgment | Count edge? | Abnormal? | Why |
| --- | --- | --- | --- | --- |
| `100 -> 110` |  |  |  |  |
| `100 -> 101` |  |  |  |  |
| `100 -> 011` |  |  |  |  |
| `000` |  |  |  |  |
| `111` |  |  |  |  |

Then answer:

1. Why do normal 120-degree Hall signals use six valid states instead of all eight binary combinations?
2. Why are `000` and `111` illegal for this software state machine?
3. Why can PB3 not be used as Hall in this project when PB3 is already assigned to LIN1?

## Safety boundary

This review is concept-only. It must not be used as permission to output PWM, enable Gate signals, connect 24 V, connect the power board, or run the motor.
