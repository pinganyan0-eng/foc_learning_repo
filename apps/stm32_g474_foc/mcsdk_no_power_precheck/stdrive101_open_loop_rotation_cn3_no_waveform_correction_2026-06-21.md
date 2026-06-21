# STDRIVE101 Open-Loop Rotation CN3 No-Waveform Correction - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-OPEN-LOOP-ROTATION-CN3-NO-WAVEFORM-CORRECTION-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-open-loop-rotation-cn3-no-waveform-correction`.
- Correction:
  the user clarified that `CN3` did not show jumping. The earlier
  waveform-present interpretation must not be used as evidence that the MCU
  side driver inputs toggled.
- Decision:
  `STDRIVE101 open-loop rotation CN3 no-waveform correction / user clarified
  CN3 did not jump / earlier waveform-present interpretation superseded /
  motor no-rotation result is consistent with no observed CN3 driver-input
  waveform / next work is firmware image entry and pin-output diagnosis, not
  repeated motor run`.

## Boundary

This correction removes the premise that the open-loop rotation candidate
produced observed CN3 driver-input toggling. It does not validate firmware
runtime behavior, Gate PWM output, power-stage readiness, motor readiness,
Hall closed loop, or sensorless operation.

## Next Checkpoint

Do not repeat a motor-connected run from this state. First confirm whether the
downloaded image is actually executing and whether the selected GPIO pins are
the expected CN3 driver-input pins.
