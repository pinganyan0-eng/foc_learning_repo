# STDRIVE101 Gate-Waveform Candidate Residual-Voltage Isolation Result - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-RESIDUAL-VOLTAGE-ISOLATION-RESULT-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-residual-voltage-isolation-result`.
- Scope:
  bounded residual-voltage isolation check after the waveform candidate
  USB-only DMM result reported `VS / 24V_FUSED = 2 V` and `REG12 = 0.3 V`.
- Physical boundary:
  USB / ST-LINK disconnected; HSPY / 24 V OFF and physically disconnected;
  motor disconnected; no `10 kohm` wake resistor or LIN1 stimulus installed.
- Decision:
  `STDRIVE101 gate-waveform candidate residual-voltage isolation result /
  USB-STLINK disconnected / HSPY 24 V off and physically disconnected / motor
  disconnected / no 10 kohm wake resistor or LIN1 stimulus installed /
  user-confirmed VS / 24V_FUSED = 0 V / user-confirmed REG12 = 0 V / earlier
  candidate USB-only VS / 24V_FUSED = 2 V cleared after USB disconnect /
  persistent VS backfeed not indicated in this candidate isolation check /
  residual-voltage blocker cleared only / next checkpoint may only be a
  separate candidate 24 V static no-motor phase-gate or execution entry after
  fresh preconditions / no Run Debug / no 24 V command from this record / no
  Gate PWM output / no Motor Pilot / no Motor Profiler / no motor connection /
  no powered-drive readiness`.

## Boundary

This result clears only the immediate residual-voltage isolation blocker raised
by the earlier candidate USB-only `VS / 24V_FUSED = 2 V` reading.

It does not authorize:

- applying 24 V directly from this record;
- power-board powered runtime;
- Run / Debug;
- normal generated MCSDK application execution;
- Gate PWM output or PWM validation;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

Any later candidate 24 V static no-motor check still needs a separate dated
phase-gate or execution-entry record with fresh preconditions, current limit,
measurement points, stop rules, and rollback.

## Prior Result Being Isolated

The preceding waveform candidate USB-only DMM result reported:

```text
CN3_1 through CN3_6 = 0 V
CN3_13 = 3 V
CN3_14 = 3 V
VS / 24V_FUSED = 2 V
REG12 = 0.3 V
board heat / smell / sound / reset loop = not reported in latest row
```

That result did not open upward hardware progression because
`VS / 24V_FUSED = 2 V` was above the prior `< 1 V` USB-only boundary.

## Isolation Measurement

User-confirmed setup:

| Item | State |
| --- | --- |
| USB / ST-LINK | disconnected |
| HSPY / 24 V | OFF and physically disconnected |
| Motor | disconnected |
| `10 kohm` wake resistor / LIN1 stimulus | not installed |
| Measurement instrument | DMM, black probe on GND |

User-confirmed readings after USB / ST-LINK disconnect:

| Item | Reading | Status |
| --- | --- | --- |
| `VS / 24V_FUSED` | `0 V` | cleared after USB / ST-LINK disconnect |
| `REG12` | `0 V` | cleared after USB / ST-LINK disconnect |

## Interpretation

- The earlier candidate USB-only `VS / 24V_FUSED = 2 V` reading is now treated
  as a USB/ST-LINK-associated residual, floating, or backfeed observation for
  this branch.
- Persistent VS backfeed is not indicated by this isolation check because both
  `VS / 24V_FUSED` and `REG12` returned to `0 V` with USB / ST-LINK removed.
- This clears only the residual-voltage blocker raised by the candidate
  USB-only DMM result. It is still not a powered-driver validation.
- No 24 V behavior, gate waveform, PWM safety, Motor Pilot / Profiler
  behavior, motor behavior, or power-stage readiness is proven here.

## Next Checkpoint

Do not repeat the residual-voltage isolation check unless the physical state,
image, wiring, or measured value changes.

The next engineering checkpoint may only be a separate candidate 24 V static
no-motor phase-gate or execution entry. That next record must keep the motor
disconnected, define the current limit and stop rules, and still forbid
Run / Debug, Gate PWM output, Motor Pilot, Motor Profiler, and motor-readiness
claims.
