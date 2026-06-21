# STDRIVE101 Gate-Waveform Candidate 24V Static Scope No-Waveform Result - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-24V-STATIC-SCOPE-NO-WAVEFORM-RESULT-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-24v-static-scope-no-waveform-result`.
- Scope:
  user-reported oscilloscope check on the six STDRIVE101 MCU-facing driver
  inputs with the waveform candidate image on the board, HSPY at 24 V, and the
  motor disconnected.
- Physical boundary:
  waveform candidate image; HSPY `24 V / 0.2 A`; motor disconnected; no
  `10 kohm` wake resistor or LIN1 stimulus installed; no Run / Debug; no
  Motor Pilot; no Motor Profiler; no motor connection.
- Decision:
  `STDRIVE101 gate-waveform candidate 24V static scope no-waveform result /
  waveform candidate image / HSPY CV 0.036 A / CN3_1 and CN3_2 no waveform /
  CN3_3 and CN3_4 no waveform / CN3_5 and CN3_6 no waveform / nFAULT remains
  3.3 V / no board heat smell sound reset-loop symptom / no observed
  MCU-facing driver-input waveform in this no-motor bounded check / no Run
  Debug / no Motor Pilot / no Motor Profiler / no motor connection / no
  powered-drive readiness`.

## User-Reported Readings

| Pair | Result |
| --- | --- |
| `CN3_1`, `CN3_2 / LIN1` | no waveform observed |
| `CN3_3`, `CN3_4` | no waveform observed |
| `CN3_5`, `CN3_6` | no waveform observed |
| HSPY state | `CV` |
| HSPY current | `0.036 A` |
| `CN3_13 / nFAULT` | `3.3 V` |
| board heat / smell / sound / reset-loop symptom | none reported |

## Boundary

This is bounded measurement evidence for the waveform candidate image in a
24 V, no-motor, oscilloscope-observed state. It records that the user did not
observe a waveform on any of the six MCU-facing STDRIVE101 driver-input pins
in the reported check, while HSPY stayed in `CV` at `0.036 A`, `nFAULT`
remained high, and no abnormal board symptom was reported.

It does not authorize or prove:

- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness.

Do not use this result as a general powered-drive readiness claim. The motor
remains disconnected and normal MCSDK runtime / Motor Pilot / Motor Profiler
remain closed.

## Next Checkpoint

Do not repeat the same candidate 24 V static scope check unless the image,
wiring, board condition, trigger method, measurement setup, or observed value
changes.

The next engineering step should be a separate decision about whether to keep
debugging the missing candidate waveform at the source/build/runtime-entry
level, or to return to a lower-risk neutral-wrapper / lockout path. It is not
direct motor power-up and does not open Motor Pilot, Motor Profiler, motor
connection, power-stage readiness, or motor readiness.
