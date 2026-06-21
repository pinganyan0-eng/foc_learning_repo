# STDRIVE101 Gate-Waveform Neutral-Wrapper 24V Static Scope Baseline Result - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-24V-STATIC-SCOPE-BASELINE-RESULT-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-24v-static-scope-baseline-result`.
- Scope:
  oscilloscope static baseline on the six STDRIVE101 MCU-facing driver inputs
  after the 24 V static no-motor DMM table.
- Physical boundary:
  HSPY `24 V / 0.2 A`; motor disconnected; no `10 kohm` wake resistor or
  LIN1 stimulus installed; no Run / Debug; no Motor Pilot; no Motor Profiler;
  no Gate PWM output; oscilloscope ground on `CN3_15 / GND`.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper 24V static scope baseline result /
  oscilloscope ground on CN3_15 GND / HSPY CV about 0.036 A / CN3_1 and CN3_2
  0 V straight lines / CN3_3 and CN3_4 same 0 V straight lines / CN3_5 and
  CN3_6 same 0 V straight lines / nFAULT remains 3.3 V / no board heat smell
  sound reset-loop reported / all six MCU-facing driver inputs static-low in
  this no-motor no-PWM baseline / no waveform output executed / no Run Debug /
  no Gate PWM output / no Motor Pilot / no Motor Profiler / no motor
  connection / no powered-drive readiness`.

## Probe Setup

| Item | Setup |
| --- | --- |
| Oscilloscope ground | `CN3_15 / GND` |
| CH1 first pair | `CN3_1` |
| CH2 first pair | `CN3_2 / LIN1` |
| CH1 second pair | `CN3_3` |
| CH2 second pair | `CN3_4` |
| CH1 third pair | `CN3_5` |
| CH2 third pair | `CN3_6` |
| Motor | disconnected |
| Gate PWM output | not executed |

## User-Reported Readings

| Pair | HSPY / Board State | CH1 | CH2 |
| --- | --- | --- | --- |
| `CN3_1`, `CN3_2 / LIN1` | `CV`, `0.036 A`, `nFAULT = 3.3 V`, no board abnormal symptom | `0 V` straight line | `0 V` straight line |
| `CN3_3`, `CN3_4` | reported as same | `0 V` straight line | `0 V` straight line |
| `CN3_5`, `CN3_6` | reported as same | `0 V` straight line | `0 V` straight line |

## Boundary

This is a static oscilloscope baseline only. It proves no gate-waveform output
was observed on the six MCU-facing driver-input pins in this no-motor,
no-PWM baseline.

It does not authorize or prove:

- Gate PWM output;
- waveform correctness;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness.

## Next Checkpoint

Turn HSPY output OFF after this baseline.

The next engineering checkpoint may only be a separate no-motor, short-window,
instrumented waveform execution entry. It must still keep the motor
disconnected, keep Motor Pilot / Profiler closed, and define exact probe
points, stop rules, and rollback before any waveform output is attempted.
