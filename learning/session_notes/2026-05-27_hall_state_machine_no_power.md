# 2026-05-27 Hall software state machine no-power lesson

## Context

- Learner role: STM32G474 FOC algorithm / main-control teammate.
- Hardware state: PCB2 not soldered; P2 no-power.
- Safety boundary: no 24 V, no motor, no Gate PWM, no power-stage action.
- Current Hall route stated by user: `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- Explicit pin constraint: `PB3 = LIN1`; PB3 must not be reused as Hall.
- Implementation scope for this lesson: concept and table judgment only; no firmware code was written.

## Progress checkpoint

- Current real stage: P2 no-power / Hall software state-machine concept practice.
- Planned position: preparation for Hall fallback before real MCSDK/Hall closed-loop work.
- Lesson target: understand legal Hall states, illegal states, adjacent transitions, reverse adjacent transitions, repeated states, and cross-state jumps.
- Deliverable: completed Hall transition judgment tables.
- Pace status: on-track for concept practice; not hardware-validated.
- Forbidden scope: no MCSDK Hall configuration, no TIM2 Hall assumption, no PWM/Gate output, no power board or motor.

## Rules taught

Candidate forward sequence used for practice:

```text
001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001
```

Core classification rules:

| Case | Example | Counting rule | Fault rule |
| --- | --- | --- | --- |
| Illegal state | `000` or `111` | Do not count edge | Abnormal |
| Repeated state | `001 -> 001` | Do not count edge | Not abnormal |
| Forward adjacent transition | `001 -> 101` | Count edge | Not abnormal |
| Reverse adjacent transition | `101 -> 001` | Count edge | Not abnormal; may update direction candidate |
| Cross-state jump | `001 -> 010` or `101 -> 110` | Do not count normal edge | Abnormal |

## User evidence

The user independently completed two Hall judgment tables.

### Table 1

| Input sequence | User judgment | Count edge? | Abnormal? | Notes |
| --- | --- | --- | --- | --- |
| `001 -> 101` | Legal | Count edge | No | Forward adjacent transition |
| `001 -> 001` | Not abnormal | Do not count edge | No | Repeated state |
| `001 -> 010` | Abnormal | Do not count normal edge | Yes | Possible missed sampling, noise, wrong wiring, too-high speed, or GPIO/EXTI handling issue |
| `000` | Illegal | Do not count edge | Yes | Illegal Hall state |

### Table 2

| Input sequence | User judgment | Count edge? | Abnormal? | Notes |
| --- | --- | --- | --- | --- |
| `101 -> 100` | Legal adjacent transition | Count edge | No | Forward adjacent transition |
| `101 -> 001` | Reverse adjacent transition | Count edge | No | Direction candidate may update |
| `101 -> 110` | Cross-state jump | Do not count normal edge | Yes | Possible missed sampling, noise, wrong wiring, too-high speed, or GPIO/EXTI handling issue |
| `111` | Illegal state | Do not count edge | Yes | Not part of normal 120-degree Hall six-state table |

## Evidence level

- Evidence level: L2.
- Confidence: medium for concept/table judgment.
- Not validated: no GPIO input test, no EXTI interrupt test, no serial log, no MCSDK project, no motor run, no power-stage measurement.

## Weak points observed

No new weak point recorded. The only correction was table-format wording: use `Yes/No` consistently in the `Abnormal?` column instead of writing `abnormal` in that column.

## Next review

Before any real Hall GPIO/EXTI implementation, ask the user to restate the decision order:

```text
1. Check 000/111 illegal states.
2. Check repeated state.
3. Check forward/reverse adjacent state.
4. Otherwise mark cross-state jump abnormal.
```

Then ask the user why PB3 cannot be used as Hall when PB3 is already assigned to LIN1.

## Handoff to Codex

Codex should keep this as a learning record only. Do not treat it as evidence that Hall closed-loop, MCSDK Hall, motor profiler, power-board PWM, or motor running has been completed.
