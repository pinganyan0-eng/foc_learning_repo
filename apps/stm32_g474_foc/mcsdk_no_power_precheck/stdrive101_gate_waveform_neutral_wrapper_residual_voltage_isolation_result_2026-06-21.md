# STDRIVE101 Gate-Waveform Neutral-Wrapper Residual-Voltage Isolation Result - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-RESIDUAL-VOLTAGE-ISOLATION-RESULT-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-residual-voltage-isolation-result`.
- Scope:
  bounded residual-voltage isolation check after the neutral-wrapper
  USB-only DMM completion result reported `VS / 24V_FUSED = 2 V` and
  `REG12 = 0.5 V`.
- Physical boundary:
  USB / ST-LINK disconnected; HSPY / 24 V OFF and physically disconnected;
  motor disconnected; no `10 kohm` wake resistor or LIN1 stimulus installed.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper residual-voltage isolation result /
  USB-STLINK disconnected / HSPY 24 V off and physically disconnected / motor
  disconnected / no 10 kohm wake resistor or LIN1 stimulus installed /
  user-reported VS / 24V_FUSED = 0 V / user-reported REG12 = 0 V / earlier
  USB-only VS / 24V_FUSED = 2 V cleared after USB disconnect / persistent VS
  backfeed not indicated in this isolation check / residual-voltage isolation
  blocker cleared only / no Run Debug / no 24 V execution / no Gate PWM output /
  no Motor Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.

## Boundary

This result clears only the immediate residual-voltage isolation blocker raised
by the earlier USB-only `VS / 24V_FUSED = 2 V` reading.

It does not authorize:

- applying 24 V;
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

## Prior Result Being Isolated

The preceding USB-only DMM completion result reported:

```text
CN3_1 through CN3_6 = 0 V
P13 = 3.3 V
P14 = 3.3 V
VS / 24V_FUSED = 2 V
REG12 = 0.5 V
board heat / smell / sound / reset loop = none
```

That result completed the USB-only DMM table but did not open upward hardware
progression because `VS / 24V_FUSED = 2 V` was above the prior `< 1 V`
USB-only boundary.

## Isolation Measurement

User-reported setup:

| Item | State |
| --- | --- |
| USB / ST-LINK | disconnected |
| HSPY / 24 V | OFF and physically disconnected |
| Motor | disconnected |
| `10 kohm` wake resistor / LIN1 stimulus | not installed |
| Measurement instrument | DMM, black probe on GND |

User-reported readings after USB / ST-LINK disconnect:

| Item | Reading | Status |
| --- | --- | --- |
| `VS / 24V_FUSED` | `0 V` | cleared after USB / ST-LINK disconnect |
| `REG12` | `0 V` | cleared after USB / ST-LINK disconnect |

## Interpretation

- The earlier USB-only `VS / 24V_FUSED = 2 V` reading is now treated as a
  USB/ST-LINK-associated residual, floating, or backfeed observation for this
  branch.
- Persistent VS backfeed is not indicated by this isolation check because both
  `VS / 24V_FUSED` and `REG12` returned to `0 V` with USB / ST-LINK removed.
- This is still not a powered-driver validation. No 24 V behavior, gate
  waveform, PWM safety, Motor Pilot / Profiler behavior, motor behavior, or
  power-stage readiness is proven here.

## Next Checkpoint

Do not repeat the residual-voltage isolation check unless the physical state,
image, wiring, or measured value changes.

The next engineering checkpoint may only be a separate dated next-stage
phase-gate decision, still with motor disconnected and with no Gate PWM output,
Motor Pilot, Motor Profiler, Run / Debug, or motor-readiness claim. This result
does not by itself open 24 V execution.
