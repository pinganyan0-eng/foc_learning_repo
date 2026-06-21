# STDRIVE101 Gate-Waveform Open-Loop Rotation 24V Static Scope Waveform-Present Result - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-OPEN-LOOP-ROTATION-24V-STATIC-SCOPE-WAVEFORM-PRESENT-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-open-loop-rotation-24v-static-scope-waveform-present`.
- Scope:
  user-reported oscilloscope check after downloading the open-loop rotation
  candidate BIN.
- Candidate BIN:
  `.tmp/manual_gate_waveform_open_loop_rotation_2026-06-21_clean/stdrive101_gate_waveform_open_loop_rotation_image.bin`.
- Candidate BIN SHA256:
  `717D0B88EA871A70AE46C9C7CA8F2D20FAF532404CA9A5C0863D563D70A0089F`.
- User-reported result:
  sustained CN3 driver-input jumping is present after the open-loop rotation
  candidate download.
- Supersession note:
  this waveform-present interpretation was later corrected by the user in
  `stdrive101_open_loop_rotation_cn3_no_waveform_correction_2026-06-21.md`.
  Do not use this record as evidence that the MCU-facing CN3 driver inputs
  actually toggled.
- Physical boundary:
  HSPY `24 V / 0.2 A` static observation, motor disconnected, no Motor Pilot,
  no Motor Profiler, no Hall closed-loop validation, and no motor-readiness
  claim.

## Decision

`STDRIVE101 gate-waveform open-loop rotation 24V static scope waveform-present
result / open-loop rotation candidate BIN downloaded / user-reported sustained
CN3 driver-input jumping present / motor disconnected / no Motor Pilot / no
Motor Profiler / no Hall closed-loop validation / no sensorless claim / no
motor-readiness claim`.

## Next Checkpoint

Before any wiring change, turn HSPY output OFF and confirm the motor remains
disconnected while residual voltage falls back near `0 V`.

This result may support a separate, explicitly bounded, low-current open-loop
motor short-run checkpoint only after power-off wiring and stop rules are
restated. It is not itself a powered motor pass.

Later correction:
`stdrive101_open_loop_rotation_cn3_no_waveform_correction_2026-06-21.md`
supersedes the waveform-present premise. Future work should rely on the
correction and the later PA7/LIN1 wake fault-isolation record, not on this
record as waveform proof.
