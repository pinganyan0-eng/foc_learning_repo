# STDRIVE101 Protection Nodes No-Power DMM Result - 2026-06-20

## Boundary

This record captures the user-reported no-power DMM follow-up after the
STDRIVE101 single-input wake result where `REG12 = 12 V` and `nFAULT = 0 V`.

This is no-power continuity / resistance / diode-mode evidence only. It does
not authorize repeat powered wake, alternate input stimulus, firmware
implementation, generated-code edits, CubeMX / Workbench edits, flash,
Run / Debug, motor connection, Gate PWM, Motor Pilot, Motor Profiler,
Hall closed-loop validation, sensorless validation, power-stage readiness, or
motor readiness.

Do not probe U1 pins, MOSFET pins, or unknown pads by guesswork.

## Requested Setup

The requested setup was:

```text
HSPY output OFF
VS / 24V_FUSED < 1 V
10 kohm stimulus resistor removed
Motor disconnected
USB/ST-LINK unplugged
DMM continuity / resistance / diode mode only
```

The user previously reported `10k_removed = yes`. The latest corrected result
did not restate `VS_OFF_V`; `VS / 24V_FUSED < 1 V` must be confirmed before
any later measurement or powered proposal.

## User-Reported Raw Readings

User reported on 2026-06-20:

| Row | Check | User-reported result |
| --- | --- | --- |
| 1 | `SCREF` to `CN3_14 / 3V3` | `12 kohm` |
| 2 | `SCREF` to `CN3_15 / GND` | `12 kohm` |
| 3 | `CP` to `CN3_15 / GND` | initially `1.54 Mohm`, after 5 s about `2 Mohm`, resistance mode no beep |
| 4 | `REG12` to `CN3_15 / GND` | initially `0.2 Mohm`, after 5 s `0.28 Mohm` |
| 5 | `REG12` to `VS / 24V_FUSED` | initially `40 kohm`, after 5 s `40 kohm` |
| 6 | `OUT1 / phase-U` to `CN3_15 / GND` | no beep |
| 7 | `OUT1 / phase-U` to `VS / 24V_FUSED` | diode mode: red `OUT1`, black `VS` = `OL`; red `VS`, black `OUT1` = `OL` |

Earlier continuity-mode reports of beeping on `CP-GND`, `REG12-GND`,
`REG12-VS`, and `OUT1-VS` are superseded for interpretation by the corrected
resistance / diode-mode readings above. They should not be treated as stable
hard-short evidence unless a later measurement reports sustained low ohms.

## Interpretation

### SCREF

`SCREF` reads `12 kohm` to both `3V3` and `GND`. This is not a rail hard short.
It also does not by itself validate the exact VDS threshold network, because
the measurement is in-circuit and can include parallel paths through the board
and IC.

### CP

`CP-GND` at megaohms and rising with no resistance-mode beep is compatible with
a capacitor-connected / high-impedance node. It does not indicate a persistent
hard short in this no-power reading.

### REG12

`REG12-GND` rising from `0.2 Mohm` to `0.28 Mohm` does not indicate a hard
short. `REG12-VS = 40 kohm` is a finite board path, not a low-ohm short, but it
remains a review clue because the earlier powered event involved `REG12`
rising while `nFAULT` stayed low.

### OUT1 / phase-U

`OUT1-GND` no beep reduces concern about a direct phase-U short to ground.

`OUT1-VS` diode mode `OL` both ways reduces concern about a direct phase-U to
VS hard short. It does not prove the high-side MOSFET path or physical point
identification, because an expected MOSFET body-diode clue was not observed in
the reported diode-mode result.

## Updated Cause Review

The reported rows do not show a stable hard short on `CP`, `REG12`, or
`OUT1`. VDS monitoring after the `LIN1` low-side command remains the primary
review target, but the next no-power evidence should move closer to the
phase-U low-side device:

```text
Q2 source / ADC_U / R25 path to GND_POWER
Q2 drain / OUT1 to Q2 source diode behavior
Q2 gate / GLS1 gate-source pull-down path, if safely identifiable
```

If the exact Q2 source, drain, gate, `ADC_U`, `R25`, or `GLS1` pads cannot be
identified with certainty, do not probe them. Provide a board photo or EDA crop
first.

## Decision

`STDRIVE101 protection-node no-power DMM result / SCREF to 3V3 12 kohm /
SCREF to GND 12 kohm / CP to GND 1.54 Mohm rising to about 2 Mohm no beep /
REG12 to GND 0.2 Mohm rising to 0.28 Mohm / REG12 to VS 40 kohm steady /
OUT1 to GND no beep / OUT1 to VS diode OL both directions / stable hard short
not indicated on CP, REG12, or OUT1 in the reported rows / VDS low-side path
remains the primary review target / next no-power Q2 low-side path checks only
/ no repeat powered wake / no PWM-output validation / no powered-drive
readiness`.

## Next User Checkpoint

No power. Confirm:

```text
VS_OFF_V = ___ V
10k_removed = yes
```

Then use only confidently identified component pads for Q2 low-side path
checks. If any point is uncertain, stop and provide a board photo or EDA crop.
