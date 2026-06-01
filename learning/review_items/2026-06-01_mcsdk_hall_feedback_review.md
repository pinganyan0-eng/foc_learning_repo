# 2026-06-01 MCSDK Hall feedback review item

## Due

Next MCSDK/Hall-related learning turn, before any software Hall adapter implementation or MCSDK project modification.

## Prompt

Classify each value by where it is allowed to go:

| Value | Destination: current loop, speed loop, debug log, or nowhere? | Why |
| --- | --- | --- |
| Electrical angle returned by `SPD_GetElAngle(...)` |  |  |
| Average mechanical speed returned by `SPD_GetAvrgMecSpeedUnit(...)` |  |  |
| Raw `PA0/PA1/PB4` Hall state |  |  |
| `direction_candidate` from the software Hall adapter |  |  |
| `speed_candidate` before unit conversion, filtering, and reliability handling |  |  |

Then answer in one sentence:

> Why is `HALL_M1` not the same thing as the three Hall pins?

## Expected boundary

Only official MCSDK speed/position feedback object outputs may feed the FOC current loop and speed loop. Software Hall candidates from `PA0/PA1/PB4` remain debug-only unless a formal MCSDK-compatible feedback adapter is implemented and validated.

## Safety boundary

This review is concept-only. It must not be used as permission to enable PWM, connect 24 V, connect the power board, connect the motor, run Motor Profiler, or claim Hall closed-loop operation.
