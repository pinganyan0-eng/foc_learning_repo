# STDRIVE101 Manual Gate-Test Lockout Source Package - 2026-06-20

This directory is a repo-local isolated source package for Gate B
no-power build-only review.

It is not a flashed firmware image, not a generated MCSDK project edit, not a
Workbench project edit, not a runtime result, and not hardware validation.

## Scope

The first lockout source package keeps the STDRIVE101 MCU-facing driver inputs
in a known low state and keeps TIM1 output control disabled.

Allowed use in the current stage:

- source review;
- grep-based lockout checks;
- future compile-only integration into a separate build target.

Forbidden use in the current stage:

- flash;
- Run / Debug;
- 24 V powered runtime;
- gate waveform observation;
- Motor Pilot / Profiler;
- motor connection;
- power-stage or motor readiness claims.

## Source Files

| File | Purpose |
| --- | --- |
| `Inc/gate_test_lockout.h` | Public lockout state and API. |
| `Src/gate_test_lockout.c` | GPIO low-state lock, `PB12 / nFAULT` readback, TIM1 output lock. |
| `Src/main_lockout.c` | Minimal foreground loop that repeatedly enforces the lockout state. |
| `CMakeLists.txt` | Object-only compile target; no linkable firmware image. |

## Lockout Behavior

- `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and `PB15` are driven as GPIO
  outputs low.
- `PB12` is kept as a normal input for `nFAULT` observation.
- TIM1 `CCER` is cleared.
- TIM1 `MOE` and automatic output are cleared.
- TIM1 break is left enabled at register level.
- The foreground loop continuously reapplies GPIO and TIM1 lockout state.

## Build Status

This package now has a standalone object-only CMake target. It is intentionally
kept separate from the archived Packet A source snapshot and the external
Workbench project.

The target compiles only object files from:

```text
Src/gate_test_lockout.c
Src/main_lockout.c
```

It does not link an ELF, HEX, or BIN image and therefore is not a flashable
firmware artifact.

Earlier, before this target existed, an object-only syntax compile was
attempted with the local STM32Cube compiler, but the external compiler could
not be executed in the sandbox and the escalation request was rejected because
the workspace was out of credits.

A later build-only task may copy or integrate this source into a separate
repo-local firmware target, but that still will not authorize flash, runtime,
24 V, gate output, or motor action.
