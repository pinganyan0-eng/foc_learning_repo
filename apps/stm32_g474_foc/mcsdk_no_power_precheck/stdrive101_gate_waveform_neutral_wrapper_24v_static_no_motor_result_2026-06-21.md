# STDRIVE101 Gate-Waveform Neutral-Wrapper 24V Static No-Motor Result - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-24V-STATIC-NO-MOTOR-RESULT-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-24v-static-no-motor-result`.
- Scope:
  bounded 24 V static check after the neutral-wrapper residual-voltage
  isolation result.
- Physical boundary:
  USB / ST-LINK connected only for the neutral-wrapper image state; HSPY set
  to `24 V / 0.2 A`; motor disconnected; no `10 kohm` wake resistor or LIN1
  stimulus installed; no Run / Debug; no Motor Pilot; no Motor Profiler; no
  Gate PWM output.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper 24V static no-motor result /
  HSPY CV 0.036 A / VS 24V_FUSED = 24 V / CN3_1 through CN3_6 all 0 V /
  CN3_13 nFAULT = 3.3 V / CN3_14 3V3 = 3.3 V / REG12 = 0.2 V / no board
  heat smell sound reset-loop reported / six driver-input stop-rule not hit /
  nFAULT high in static no-motor state / bounded 24 V static no-motor check
  clean for this table only / no Run Debug / no Gate PWM output / no Motor
  Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.

## Measurement Table

User-reported setup and readings:

| Item | Reading | Status |
| --- | --- | --- |
| HSPY state | `CV` | reported |
| HSPY current | `0.036 A` | reported |
| `VS / 24V_FUSED` | `24 V` | reported |
| `CN3_1` driver input | `0 V` | reported |
| `CN3_2 / LIN1` | `0 V` | reported |
| `CN3_3` driver input | `0 V` | reported |
| `CN3_4` driver input | `0 V` | reported |
| `CN3_5` driver input | `0 V` | reported |
| `CN3_6` driver input | `0 V` | reported |
| `CN3_13 / nFAULT` | `3.3 V` | reported |
| `CN3_14 / 3V3` | `3.3 V` | reported |
| `REG12` | `0.2 V` | reported |
| board heat / smell / sound / reset loop | none reported | reported |

## Stop-Rule Evaluation

- HSPY remained in `CV` at `0.036 A`.
- No `CN3_1` through `CN3_6` reading was above `0.3 V`.
- `nFAULT` was high at `3.3 V`.
- The user reported no board heat, smell, sound, or reset-loop symptom.
- The bounded 24 V static no-motor table is clean for this static state only.

## Boundary

This result does not authorize:

- motor connection;
- Gate PWM output;
- Motor Pilot;
- Motor Profiler;
- Run / Debug;
- normal generated MCSDK application execution;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

## Next Checkpoint

Turn HSPY output OFF after this static measurement.

The next engineering checkpoint may only be a separate no-motor, no-Motor
Pilot / Profiler, no-motor-readiness gate for the next higher-risk step, such
as instrumented gate-waveform observation. This result does not open motor
connection or motor power-up.
