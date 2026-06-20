# STDRIVE101 nFAULT No-Power DMM Result - 2026-06-20

## Boundary

This record captures the user-reported no-power DMM follow-up after the
STDRIVE101 single-input wake result where `REG12 = 12 V` and `nFAULT = 0 V`.

This is no-power continuity / resistance evidence only. It does not authorize
repeat powered wake, alternate input stimulus, firmware implementation,
generated-code edits, CubeMX / Workbench edits, flash, Run / Debug, motor
connection, Gate PWM, Motor Pilot, Motor Profiler, Hall closed-loop validation,
sensorless validation, power-stage readiness, or motor readiness.

## Requested Setup

These rows were requested under the following boundary:

```text
HSPY output OFF
VS / 24V_FUSED < 1 V
10 kohm stimulus resistor removed
Motor disconnected
USB/ST-LINK unplugged
DMM continuity / resistance mode only
```

The user reported the row results but did not restate the setup line. Keep the
physical setup as a checkpoint before any later measurement.

## User-Reported Raw Readings

User reported on 2026-06-20:

| Row | Check | User-reported result |
| --- | --- | --- |
| 1 | `CN3_2 / LIN1` to `CN3_14 / 3V3` | no beep / `66 kohm` |
| 2 | `CN3_2 / LIN1` to `CN3_15 / GND` | no beep / `60 kohm` |
| 3 | `CN3_13 / nFAULT` to `CN3_14 / 3V3` | no beep / `5 kohm` |
| 4 | `CN3_13 / nFAULT` to `CN3_15 / GND` | no beep / `10 kohm` |

## Interpretation

### LIN1 rows

Rows 1 and 2 do not show a hard short from `LIN1` to either `3V3` or `GND`.
The tens-of-kohms readings also support that the external `10 kohm` wake
stimulus is no longer acting as a direct low-resistance bridge in these two
checks.

This does not prove the STDRIVE101 input is healthy, and it does not validate
the powered wake behavior. It only reduces concern about a simple persistent
`LIN1` rail short after the stimulus was removed.

### nFAULT rows

Rows 3 and 4 do not show a hard short from `nFAULT` to either `3V3` or `GND`.
The readings are finite because the `nFAULT` net has board-level pull-up /
indicator / IC-connected paths; DMM polarity and parallel board paths can make
the measured value differ from a simple single-resistor expectation.

```text
CN3_13 / nFAULT -> CN3_14 / 3V3 = no beep / 5 kohm
CN3_13 / nFAULT -> CN3_15 / GND = no beep / 10 kohm
```

These values reduce concern that the powered `nFAULT = 0 V` event was caused
by a permanent CN3-side short on the `nFAULT` net.

Do not treat this as proof that the STDRIVE101 internal fault cause is known.
It is only a CN3-side no-power screen.

## Updated Cause Review

The earlier cause ranking remains active:

1. VDS monitoring after the `LIN1` low-side command remains the primary review
   target for the powered `nFAULT = 0 V` event.
2. A permanent external `nFAULT` hard short is not indicated by the four CN3
   readings.
3. REG12 sequence / accidental external REG12 tie, CP comparator assertion,
   and thermal shutdown remain secondary review targets.

## Next No-Power Check

Do not power the board. The next useful evidence is a source packet or
confidently identified no-power probing for the protection / output nodes:

```text
SCREF
CP
REG12
OUT1 / phase-U
GLS1 / low-side-1 gate, if identifiable from source
Q2 low-side MOSFET drain/source/gate, if identifiable from source
```

If these points cannot be identified with certainty, do not probe them by
guesswork. Provide a marked board photo or EDA/netlist crop first.

## Decision

`STDRIVE101 nFAULT no-power DMM result / LIN1 to 3V3 66 kohm no beep /
LIN1 to GND 60 kohm no beep / nFAULT to 3V3 5 kohm no beep / nFAULT to GND
10 kohm no beep / LIN1 persistent rail short not indicated / nFAULT persistent
rail short not indicated / VDS monitoring after LIN1 low-side command remains
the primary review target / source packet or identified no-power protection-node
checks needed before any repeat powered wake / no PWM-output validation / no
powered-drive readiness`.
