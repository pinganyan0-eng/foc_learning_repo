# STDRIVE101 Manual Gate-Waveform Source Package - 2026-06-21

This is a Gate E1 no-power source-review package only.

It is not a build target and intentionally has no `CMakeLists.txt`.

The source files include a compile-time acknowledgement guard:

```c
GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK
```

Do not define that macro unless a later dated Gate E2 build-only record is
opened. This package does not authorize flash, Run / Debug, USB runtime
execution, 24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor
connection, or readiness claims.

## Files

- `Inc/gate_waveform_candidate.h`
- `Src/gate_waveform_candidate.c`
- `Src/main_waveform_candidate.c`

## Source Boundary

The candidate is isolated from the normal generated MCSDK application. It uses
direct STM32G4 register access only, fixes the candidate driver-input pins as
`PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and `PB15`, and returns those pins to
GPIO-low idle before and after the reviewed candidate window.

This source package is review evidence only. It is not object-code evidence,
linked-image evidence, runtime evidence, 24 V evidence, waveform evidence, or
motor evidence.
