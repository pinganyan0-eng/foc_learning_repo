# 2026-06-01 MCSDK Hall speed/position feedback data-flow lesson

## Context

- Learner role: STM32G474 FOC algorithm / main-control teammate.
- Current project stage: P1 to P2 preview; MCSDK no-power precheck / concept-only learning.
- Hardware boundary: no 24 V, no power board, no motor, no Gate PWM, no Hall closed-loop claim.
- Project-specific Hall route discussed: PCB2 Hall is software Hall on `PA0/PA1/PB4`, not the MCSDK standard TIM2 Hall pin route `PA15/PB3/PB10`.
- Scope of this lesson: MCSDK Hall speed/position feedback data flow and interface boundary only; no firmware code, build, flash, serial log, Motor Profiler, or power-stage validation was performed.

## Progress checkpoint

- Current real stage: no-power / debug-only Hall concept learning.
- Planned position: P2 MCSDK no-power precheck before any real Hall closed-loop work.
- Lesson target: understand what `HALL_M1`, `SPD_GetElAngle(...)`, and `SPD_GetAvrgMecSpeedUnit(...)` mean in the MCSDK feedback path.
- Deliverable: five-sentence user teach-back confirming the interface boundary.
- Pace status: on-track for concept practice; not hardware-validated.
- Forbidden scope: no 24 V, no power board, no motor, no three-phase PWM, no Motor Profiler, no Hall closed-loop claim.

## Rules taught

MCSDK Hall feedback is not raw GPIO reading. The useful control data is produced through the MCSDK speed/position feedback abstraction:

```text
Hall GPIO/TIM input
    -> Hall feedback object for Motor 1 (`HALL_M1`)
    -> `SPD_GetElAngle(...)` for the FOC current loop
    -> `SPD_GetAvrgMecSpeedUnit(...)` for the speed loop
```

Core mapping:

| Item | Meaning | Consumer | Not equivalent to |
| --- | --- | --- | --- |
| `HALL_M1` | Motor 1 Hall speed/position feedback object | MCSDK control stack | The three physical Hall pins |
| `SPD_GetElAngle(...)` | Electrical angle feedback | FOC current loop / Park and inverse Park alignment | Raw Hall state or mechanical speed |
| `SPD_GetAvrgMecSpeedUnit(...)` | Average mechanical speed feedback in MCSDK speed units | Speed loop / speed PI | Raw period, tick count, or unverified `speed_candidate` |
| Software Hall adapter on `PA0/PA1/PB4` | Debug-only candidate source and state-machine checker | Logs, concept validation, no-power debug | Official MCSDK Hall closed-loop sensor feedback |

## Why direct injection is unsafe/incorrect

The user was taught that `direction_candidate` and `speed_candidate` from a software Hall adapter must not be directly pushed into MCSDK as if they were official feedback. A formal feedback path would need at least:

- MCSDK speed/position object interface compatibility.
- Correct electrical angle generation, not just raw Hall state classification.
- Speed-unit conversion into MCSDK's expected mechanical speed unit.
- Hall sequence, direction, and phase-offset calibration.
- Filtering / averaging and timeout handling.
- Reliability handling for illegal states, repeated states, jumps, jitter, and missing edges.
- Evidence from build, no-power validation, controlled hardware tests, and phase-gate approval before any closed-loop claim.

## User evidence

The user correctly restated all five required checks:

1. `HALL_M1` is not the three Hall pins; it is MCSDK's Motor 1 Hall speed/position feedback object.
2. `SPD_GetElAngle(...)` gives the FOC current loop electrical angle for Park / inverse Park direction alignment.
3. `SPD_GetAvrgMecSpeedUnit(...)` gives the speed loop average mechanical speed for comparison against the target speed and torque-current regulation.
4. `PA0/PA1/PB4` software Hall `direction_candidate` / `speed_candidate` are only candidates and cannot bypass unit conversion, filtering, phase calibration, reliability handling, and the MCSDK object interface.
5. A debug-only software Hall adapter is only for no-power debugging and log validation; it does not prove MCSDK Hall closed-loop completion.

## Evidence level

- Evidence level: L2.
- Confidence: medium.
- Reason: the user can accurately restate the conceptual data flow and safety/interface boundary.
- Not validated: no MCSDK project code was inspected in this lesson, no adapter was implemented, no build/flash/log was produced, no GPIO/EXTI or TIM Hall test was run, no Motor Profiler result exists, and no motor/power-board action was performed.

## Weak points observed

No new weak point recorded. The user gave a correct five-sentence teach-back without needing correction.

## Next review

Ask the user to classify the following values by destination:

| Value | Goes to current loop, speed loop, debug log, or nowhere? | Why |
| --- | --- | --- |
| Electrical angle from `SPD_GetElAngle(...)` |  |  |
| Average mechanical speed from `SPD_GetAvrgMecSpeedUnit(...)` |  |  |
| Raw `PA0/PA1/PB4` Hall state |  |  |
| `direction_candidate` from software Hall |  |  |
| `speed_candidate` before unit/filter/reliability handling |  |  |

Expected boundary: only official MCSDK feedback object outputs may feed the control loops. Software Hall candidates remain debug-only until a formal adapter is implemented and validated.

## Handoff to Codex

This is a learning record only. Do not treat it as evidence that MCSDK Hall, Hall closed-loop, Motor Profiler, power-stage PWM, or motor running has been completed.
