# STDRIVE101 Manual Gate-Waveform Build-Only Package - 2026-06-21

This directory is a Gate E2 no-power build-only package for the exact Gate E1
source package:

```text
../manual_gate_waveform_source_package_2026-06-21/
```

It exists only to check object and linked-image boundaries. It does not
authorize flash, Run / Debug, USB runtime execution, 24 V, Gate PWM output,
Motor Pilot, Motor Profiler, motor connection, or readiness claims.

## Build Boundary

This package defines `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK` only inside
the build-only target. The source-review package itself still has no
`CMakeLists.txt` and still raises `#error` if compiled outside a dated Gate E2
build boundary.

## Targets

- `stdrive101_gate_waveform_candidate_objects`: object-only compile boundary.
- `stdrive101_gate_waveform_candidate_image`: linked ELF / MAP build-only
  boundary using the repo-local NUCLEO-G474RE startup, linker script,
  `system_stm32g4xx.c`, and this package's minimal runtime stubs.

No HEX or BIN target is defined here.

The linked image intentionally avoids newlib by using `-nostdlib` and local
empty `__libc_init_array`, `_init`, and `_fini` stubs. This is to keep the
MAP review free of unused malloc/free support paths.
