# STDRIVE101 Gate-Waveform Neutral-Wrapper Build-Only Package - 2026-06-21

This directory is a no-power build-only package for the neutral-wrapper source
review:

```text
../manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/
```

It exists only to check object and linked-image boundaries. It does not
authorize flash, Run / Debug, USB runtime execution, 24 V, Gate PWM output,
Motor Pilot, Motor Profiler, motor connection, or readiness claims.

## Build Boundary

This package defines both build acknowledgements only inside the build-only
targets:

- `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK`
- `GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK`

The source-review packages themselves still have no `CMakeLists.txt` and still
raise `#error` if compiled outside a dated build-only boundary.

## Source Inputs

The build inputs are intentionally narrow:

- `manual_gate_waveform_source_package_2026-06-21/Src/gate_waveform_candidate.c`
- `manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/Src/main_neutral_wrapper.c`
- this package's `Src/minimal_runtime.c`
- repo-local NUCLEO-G474RE startup, linker script, and `system_stm32g4xx.c`

The old `manual_gate_waveform_source_package_2026-06-21/Src/main_waveform_candidate.c`
is intentionally excluded from every target in this package.

## Targets

- `stdrive101_gate_waveform_neutral_wrapper_objects`: object-only compile
  boundary.
- `stdrive101_gate_waveform_neutral_wrapper_image`: linked ELF / MAP build-only
  boundary.

No HEX or BIN target is defined here.

The linked image intentionally avoids newlib by using `-nostdlib` and local
empty `__libc_init_array`, `_init`, and `_fini` stubs. This keeps the MAP
review free of unused malloc/free support paths.
