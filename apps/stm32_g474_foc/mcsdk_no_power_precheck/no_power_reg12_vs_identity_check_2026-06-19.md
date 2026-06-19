# No-Power REG12 / VS Identity Check - 2026-06-19

## Boundary

This record covers a no-power DMM resistance check after the static 24 V
baseline gate summary.

Required setup for the measurement:

- HSPY output off.
- 24 V disconnected from the board.
- USB/ST-LINK disconnected.
- Motor disconnected.
- DMM in resistance or continuity mode.

This is no-power identity / short-check evidence only. It is not motor
validation, PWM validation, Gate PWM validation, Hall closed-loop validation,
sensorless validation, or powered-drive readiness.

## Prior Context

The static 24 V baseline gate recorded:

- reviewed `nucleo_g474re_baseline` firmware;
- app returned to `IDLE` after `STOP`;
- `VS / 24V_FUSED = 24 V`;
- `CN3_13 / nFAULT = 3.3 V`;
- `CN3_1..CN3_6 = 0 V`;
- supply current stable at `0.036 A` in `CV` after B1 once;
- `REG12 = 0.3 V`.

Related prior record:

- `static_24v_baseline_gate_summary_2026-06-19.md`

## User-Reported Raw Measurement

```text
REG12 correct point -> VS / 24V_FUSED: 0.5 Mohm
REG12 correct point -> GND: 3 Mohm
VS / 24V_FUSED -> GND: 0.2 Mohm
REG12 correct point -> 24V input positive: 25 Mohm
REG12 correct point -> CN3_14 / 3V3: 0.4 Mohm
```

Follow-up physical point confirmation from the user:

```text
REG12 / VS measurement points were not misidentified.
```

## Interpretation

No obvious low-resistance short was reported between:

- `REG12` and `VS / 24V_FUSED`;
- `REG12` and GND;
- `VS / 24V_FUSED` and GND;
- `REG12` and 24 V input positive;
- `REG12` and `CN3_14 / 3V3`.

The readings are high-resistance values in the hundreds of kilohms to megohms
range. This supports the limited conclusion that the measured nodes are not
hard-shorted under the reported no-power DMM condition.

Important non-pass limits:

- The user reports the REG12 / VS measurement points were not misidentified,
  but this no-power record still does not explain the powered-static REG12 low
  value.
- This does not explain why powered static `REG12` measured `0.3 V`.
- This does not validate gate-drive supply behavior.
- This does not authorize motor connection, PWM output, Motor Pilot, or Motor
  Profiler.

## Decision

`No-power REG12 / VS identity check / user reports point identity confirmed /
no obvious hard short observed / REG12 powered-static low value remains
unexplained / no powered-drive readiness`.

## Next Boundary

Before any later powered step:

1. Visually re-identify the physical measurement points:
   - `C2/C3` positive side should be `VS / 24V_FUSED`;
   - `C4/C5` positive side should be `REG12`;
   - `C4/C5` GND side should beep / read near 0 ohm to GND.
2. If powered again, keep motor disconnected and keep current limit at
   `24 V / 0.2 A`.
3. Repeat only static readings:
   - supply current and CV/CC state;
   - `VS / 24V_FUSED`;
   - `CN3_13 / nFAULT`;
   - `REG12` at the re-identified `C4/C5` positive side;
   - `CN3_1..CN3_6`.

No PWM or motor step is opened by this record.
