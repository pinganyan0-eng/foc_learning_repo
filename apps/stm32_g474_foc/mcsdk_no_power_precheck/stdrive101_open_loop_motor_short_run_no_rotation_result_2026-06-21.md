# STDRIVE101 Open-Loop Motor Short-Run No-Rotation Result - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-OPEN-LOOP-MOTOR-SHORT-RUN-NO-ROTATION-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-open-loop-motor-short-run-no-rotation`.
- Prior condition:
  an earlier interpretation said the open-loop rotation candidate showed
  sustained CN3 driver-input jumping in a 24 V static scope check, but this
  premise was later superseded by
  `stdrive101_open_loop_rotation_cn3_no_waveform_correction_2026-06-21.md`.
- User-reported motor result:
  motor did not rotate during the short open-loop attempt.
- Decision:
  `STDRIVE101 open-loop motor short-run no-rotation result / earlier CN3
  driver-input jumping premise later corrected as no observed CN3 waveform /
  motor connected for short attempt /
  user-reported motor did not rotate / not a motor pass / next work is
  firmware image entry, driver-input route, and fault-isolation diagnosis,
  not repeated open-loop run`.

## Boundary

This result does not validate motor readiness, power-stage readiness, Hall
closed loop, sensorless operation, or safe drive operation. The later CN3
no-waveform correction means this record must not be used as proof that CN3
driver-input toggling reached the power board. Do not repeat the same
open-loop motor attempt unless a measured condition changes.

## Next Checkpoint

Return to a no-motor or motor-disconnected diagnostic state and check:

- `nFAULT` during the attempt;
- HSPY current during the attempt;
- whether `REG12` is near `12 V` during the attempt;
- whether the MCU-facing driver-input pins are actually driven before looking
  for phase outputs or gate-node switching;
- whether the motor phase wiring is confirmed.
