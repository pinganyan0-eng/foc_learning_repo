# CN3 Driver-Input No-Power Short-Check Plan - 2026-06-19

## Boundary

This plan is the next step after the STDRIVE101 `REG12` standby explanation.
It checks the six CN3 driver-input lines only with all power removed.

This is no-power DMM planning and measurement collection only. It is not a
wake-up test, not PWM validation, not Gate PWM validation, not motor
validation, not Hall closed-loop validation, not sensorless validation, and not
powered-drive readiness.

Hard stops remain active:

- Do not connect a motor.
- Do not start PWM.
- Do not run Motor Pilot.
- Do not run Motor Profiler.
- Do not intentionally drive any CN3 input high in this step.

## Why This Step Comes Next

The static `REG12 = 0.3 V` behavior is now explained by STDRIVE101 standby:
all measured drive inputs were low, so the internal 12 V LDO stayed switched
off.

Before any later wake-up diagnostic can be considered, the project must prove
that the six driver-input lines do not have hard shorts to rails or to each
other. Without that evidence, choosing any input to raise high would be an
unbounded hardware action.

## Mapping Under Check

Use this as the current board-side mapping clue for measurement labels:

| CN3 pin | Board-side signal |
| --- | --- |
| `CN3_1` | `HIN1` |
| `CN3_2` | `LIN1` |
| `CN3_3` | `HIN2` |
| `CN3_4` | `LIN2` |
| `CN3_5` | `HIN3` |
| `CN3_6` | `LIN3` |

This plan does not upgrade the mapping into final firmware readiness. It only
collects no-power evidence for the currently used labels.

## Required Setup

Use this exact setup:

```text
HSPY output: OFF
24 V input: disconnected from the board
USB/ST-LINK: unplugged
Motor: disconnected
CN3: connected in the same physical state as the static 24 V check, unless
     physical access requires disconnecting it; if disconnected, record that
DMM: resistance or continuity mode only
```

Do not use continuity or resistance mode while any external supply or USB is
connected.

## Stop Rules

Stop and report immediately if any of these happen:

- any `CN3_1..CN3_6` line beeps to `VS / 24V_FUSED`;
- any `CN3_1..CN3_6` line beeps to `REG12`;
- any `CN3_1..CN3_6` line reads near `0 ohm` to `3V3` or `GND`;
- any two different `CN3_1..CN3_6` lines beep together;
- the DMM reading is unstable enough that the same probe pair cannot be
  repeated.

STDRIVE101 logic inputs have internal pull-down behavior, so a finite
resistance from an input to GND is not automatically a failure. A hard short or
beep is the stop condition; exact resistance should still be recorded.

## Measurement Table

Record raw values. Use `beep / no beep` plus resistance if available.

### Driver Inputs To Rails

| Check | Beep? | Resistance / reading | Note |
| --- | --- | --- | --- |
| `CN3_1 / HIN1` -> `GND` | TBD | TBD | TBD |
| `CN3_1 / HIN1` -> `3V3 / CN3_14` | TBD | TBD | TBD |
| `CN3_1 / HIN1` -> `VS / 24V_FUSED` | TBD | TBD | TBD |
| `CN3_1 / HIN1` -> `REG12` | TBD | TBD | TBD |
| `CN3_2 / LIN1` -> `GND` | TBD | TBD | TBD |
| `CN3_2 / LIN1` -> `3V3 / CN3_14` | TBD | TBD | TBD |
| `CN3_2 / LIN1` -> `VS / 24V_FUSED` | TBD | TBD | TBD |
| `CN3_2 / LIN1` -> `REG12` | TBD | TBD | TBD |
| `CN3_3 / HIN2` -> `GND` | TBD | TBD | TBD |
| `CN3_3 / HIN2` -> `3V3 / CN3_14` | TBD | TBD | TBD |
| `CN3_3 / HIN2` -> `VS / 24V_FUSED` | TBD | TBD | TBD |
| `CN3_3 / HIN2` -> `REG12` | TBD | TBD | TBD |
| `CN3_4 / LIN2` -> `GND` | TBD | TBD | TBD |
| `CN3_4 / LIN2` -> `3V3 / CN3_14` | TBD | TBD | TBD |
| `CN3_4 / LIN2` -> `VS / 24V_FUSED` | TBD | TBD | TBD |
| `CN3_4 / LIN2` -> `REG12` | TBD | TBD | TBD |
| `CN3_5 / HIN3` -> `GND` | TBD | TBD | TBD |
| `CN3_5 / HIN3` -> `3V3 / CN3_14` | TBD | TBD | TBD |
| `CN3_5 / HIN3` -> `VS / 24V_FUSED` | TBD | TBD | TBD |
| `CN3_5 / HIN3` -> `REG12` | TBD | TBD | TBD |
| `CN3_6 / LIN3` -> `GND` | TBD | TBD | TBD |
| `CN3_6 / LIN3` -> `3V3 / CN3_14` | TBD | TBD | TBD |
| `CN3_6 / LIN3` -> `VS / 24V_FUSED` | TBD | TBD | TBD |
| `CN3_6 / LIN3` -> `REG12` | TBD | TBD | TBD |

### Driver Input To Driver Input

| Check | Beep? | Resistance / reading | Note |
| --- | --- | --- | --- |
| `CN3_1 / HIN1` -> `CN3_2 / LIN1` | TBD | TBD | TBD |
| `CN3_2 / LIN1` -> `CN3_3 / HIN2` | TBD | TBD | TBD |
| `CN3_3 / HIN2` -> `CN3_4 / LIN2` | TBD | TBD | TBD |
| `CN3_4 / LIN2` -> `CN3_5 / HIN3` | TBD | TBD | TBD |
| `CN3_5 / HIN3` -> `CN3_6 / LIN3` | TBD | TBD | TBD |

## Acceptance For This Step

This step can close only if:

- no driver-input line has a hard short to `VS / 24V_FUSED`;
- no driver-input line has a hard short to `REG12`;
- no driver-input line has a hard short to `3V3` or `GND`;
- no adjacent driver-input pair has a hard short;
- the measurement setup is confirmed as unpowered.

Closing this step still does not authorize wake-up, PWM, motor connection,
Motor Pilot, or Motor Profiler. It only allows planning a separate bounded
single-input wake-up diagnostic.

## Next Decision After Results

If the table is clean, create a separate wake-up diagnostic plan before any
powered action. That later plan must define:

- exact single input to command or stimulate;
- why that input is the lowest-risk choice;
- expected `REG12`, `nFAULT`, and supply current;
- current limit and CV/CC stop rule;
- rollback to all inputs low.

If any row shows a hard short or ambiguous repeatability, stop hardware
progression and open a hardware correction / recheck record.
