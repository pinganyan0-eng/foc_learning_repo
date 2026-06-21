# STDRIVE101 Gate-Waveform Neutral Wrapper Source Package - 2026-06-21

This package is source-review evidence only.

It exists because the Gate E2 waveform candidate image calls
`gate_waveform_candidate_run_once()` once before entering its idle-low loop.
That image is not ideal for a DMM-only USB neutral-state check, because a DMM
can observe only the steady post-window state and cannot prove there was no
reset-time or boot-time transient.

This neutral wrapper changes only the future candidate entry point:

```text
main()
-> gate_waveform_neutral_wrapper_hold_idle_forever()
-> gate_waveform_candidate_force_idle_low()
-> forever loop calling gate_waveform_candidate_force_idle_low()
```

## Boundary

- No `CMakeLists.txt` is provided in this package.
- No object file, ELF, MAP, HEX, or BIN is produced by this package.
- No flash, Run / Debug, USB runtime execution, 24 V, Gate PWM output, Motor
  Pilot, Motor Profiler, motor connection, power-stage readiness, or motor
  readiness is opened by this package.
- A future build-only package must be separately recorded before compilation.
- A future build-only package must include the reviewed
  `gate_waveform_candidate.c` implementation, exclude the old
  `main_waveform_candidate.c`, and use this package's `main_neutral_wrapper.c`
  as the only entry point.

The wrapper source must not call:

- `gate_waveform_candidate_run_once`;
- TIM1 output-enable helpers;
- waveform-window helpers;
- normal generated MCSDK start or command-ingress paths.

## Compile Guard

The header requires `GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK`. This keeps the
package source-review only until a later dated build-only boundary explicitly
opens compilation.
