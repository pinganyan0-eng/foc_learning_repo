# PCB2 No-Power DMM Continuity / Short-Check Result - 2026-06-19

This file records the user-reported no-power DMM continuity and short-check
summary for the current PCB2 route. It is a measurement summary, not firmware,
not a powered test, and not hardware readiness.

## Safety Boundary

- Board unpowered only.
- No 24 V.
- No motor.
- No Gate PWM.
- No flash, Run, Debug, Motor Pilot, or Motor Profiler.
- No Hall closed-loop, power-stage readiness, motor readiness, or sensorless
  claim.

## Measurement Source

- Reporter: user.
- Date: 2026-06-19.
- Mode reported: pass/fail continuity summary with `通` / `不通`.
- Raw ohm values: not provided.
- Beep-state column: not separately provided; `通` is treated as continuity
  reported and `不通` is treated as no-continuity / no-hard-short reported.

## Connector Mapping Used

| CN3 position | Signal | NUCLEO position | STM32 endpoint |
| --- | --- | --- | --- |
| `CN3_2` | `LIN1` | `CN10-D12` | `PB3` |
| `CN3_10` | `IA / HALL_A` | `CN4-A0` | `PA0` |
| `CN3_11` | `IB / HALL_B` | `CN4-A1` | `PA1` |
| `CN3_12` | `IC / HALL_C` | `CN5-D5` | `PB4` |
| `CN3_13` | `nFAULT` | `CN10-D14` | `PB12` |
| `CN3_14` | `3V3` | `CN4-3V3` | rail |
| `CN3_15` | `GND` | `CN4-GND` | ground |

## User-Reported Continuity Rows

| Row | Probe A | Probe B | User result | Interpretation |
| --- | --- | --- | --- | --- |
| 1 | `CN3_10 / IA` | `CN4-A0 / PA0` | `通` | Expected continuity reported |
| 2 | `CN3_11 / IB` | `CN4-A1 / PA1` | `通` | Expected continuity reported |
| 3 | `CN3_12 / IC` | `CN5-D5 / PB4` | `通` | Expected continuity reported |
| 4 | `CN3_2 / LIN1` | `CN10-D12 / PB3` | `通` | Expected continuity reported |
| 5 | `CN3_14 / 3V3` | `CN4-3V3` | `通` | Expected continuity reported |
| 6 | `CN3_15 / GND` | `CN4-GND` | `通` | Expected continuity reported |
| 7 | `CN3_13 / nFAULT` | `CN10-D14 / PB12` | `通` | Expected continuity reported |

## User-Reported Short-Check Rows

| Row | Probe A | Probe B | User result | Interpretation |
| --- | --- | --- | --- | --- |
| 8 | `CN3_14 / 3V3` | `CN3_15 / GND` | `不通` | No rail hard short reported |
| 9 | `CN3_10 / IA` | `CN3_14 / 3V3` | `不通` | No direct short reported |
| 10 | `CN3_10 / IA` | `CN3_15 / GND` | `不通` | No direct short reported |
| 11 | `CN3_11 / IB` | `CN3_14 / 3V3` | `不通` | No direct short reported |
| 12 | `CN3_11 / IB` | `CN3_15 / GND` | `不通` | No direct short reported |
| 13 | `CN3_12 / IC` | `CN3_14 / 3V3` | `不通` | No direct short reported |
| 14 | `CN3_12 / IC` | `CN3_15 / GND` | `不通` | No direct short reported |
| 15 | `CN3_2 / LIN1` | `CN3_14 / 3V3` | `不通` | No direct short reported |
| 16 | `CN3_2 / LIN1` | `CN3_15 / GND` | `不通` | No direct short reported |
| 17 | `CN3_13 / nFAULT` | `CN3_14 / 3V3` | `不通` | No hard short reported; this does not disprove a high-value pull-up path |
| 18 | `CN3_13 / nFAULT` | `CN3_15 / GND` | `不通` | No direct short reported |
| 19 | `CN3_10 / IA` | `CN3_11 / IB` | `不通` | No Hall-line short reported |
| 20 | `CN3_10 / IA` | `CN3_12 / IC` | `不通` | No Hall-line short reported |
| 21 | `CN3_11 / IB` | `CN3_12 / IC` | `不通` | No Hall-line short reported |

## Decision

`PCB2 no-power DMM continuity / short-check summary / expected continuity
reported for CN3_10-PA0, CN3_11-PA1, CN3_12-PB4, CN3_2-PB3, CN3_14-3V3,
CN3_15-GND, and CN3_13-PB12 / no rail, signal-to-rail, or Hall-line hard short
reported / raw ohm values not provided / no powered readiness`.

## What This Opens

This result is sufficient to stop treating the PCB2 no-power DMM table as the
immediate blocker for no-power software Hall interface planning. The next
allowed project step is still no-power only: review the future software Hall
adapter interface / code-entry boundary for `PA0 / PA1 / PB4`.

## What This Does Not Open

This result does not authorize firmware implementation, generated-code edits,
CubeMX or Workbench edits, flash, Run / Debug, 24 V, power-board connection,
motor connection, Gate PWM output, Motor Pilot, Motor Profiler, Hall closed
loop, sensorless operation, power-stage readiness, or motor readiness.
