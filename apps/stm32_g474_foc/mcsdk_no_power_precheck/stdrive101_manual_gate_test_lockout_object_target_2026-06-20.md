# STDRIVE101 Manual Gate-Test Lockout Object-Only Target - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LOCKOUT-OBJECT-TARGET-NO-POWER-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-manual-gate-test-lockout-object-target-no-power`.
- Scope:
  Gate B no-power object-only build-target setup for the isolated lockout
  source package.
- Hardware action:
  none.
- Firmware runtime action:
  none; no flash, no Run / Debug, no 24 V runtime.
- Decision:
  `STDRIVE101 manual gate-test lockout object-only target no-power /
  repo-local CMake object library target added for the isolated lockout source
  package / target compiles only gate_test_lockout.c and main_lockout.c object
  files / no ELF HEX BIN link target / REPO_ROOT path corrected and CMSIS
  headers resolved / sandbox blocked external Ninja during configure and
  auto-review escalation returned 503 / no object build pass claimed / no
  flash / no runtime / no PWM-output validation / no powered-drive readiness`.

## Boundary

This record is no-power build-target setup evidence only. It does not
authorize:

- firmware flash;
- Run / Debug;
- 24 V powered runtime;
- Gate PWM output;
- oscilloscope gate probing;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness.

## Added Build Target

File added:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_test_lockout_build_only_2026-06-20/CMakeLists.txt
```

Target:

```text
stdrive101_gate_lockout_objects
```

Target type:

```text
OBJECT library
```

Source files:

```text
Src/gate_test_lockout.c
Src/main_lockout.c
```

Include sources:

```text
Inc
apps/stm32_g474_foc/nucleo_g474re_baseline/Drivers/CMSIS/Device/ST/STM32G4xx/Include
apps/stm32_g474_foc/nucleo_g474re_baseline/Drivers/CMSIS/Include
```

Path correction:

```text
REPO_ROOT = ${CMAKE_CURRENT_LIST_DIR}/../../../..
```

Static path check from repo root resolved:

```text
RepoRoot = C:\Users\gregrg\Documents\Codex\2026-04-30\qiansai\foc_learning_repo
DeviceHeaderExists = True
CoreHeaderExists = True
```

Compile definitions:

```text
STM32G474xx
```

Compile options:

```text
-mcpu=cortex-m4
-mthumb
-Wall
-Wextra
-Werror
```

## Why Object-Only

The target intentionally avoids creating a flashable firmware artifact.

Object-only compile evidence can prove only:

```text
the lockout source parses and compiles for the STM32G474 CMSIS target
```

It cannot prove:

- startup correctness;
- linker script correctness;
- firmware boot behavior;
- GPIO runtime state;
- TIM1 register runtime state;
- `nFAULT` runtime readback;
- `REG12` behavior;
- gate waveform behavior;
- motor-control behavior;
- power-stage or motor readiness.

## Configure Attempt

Command attempted from repo root:

```powershell
cmake -S apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_test_lockout_build_only_2026-06-20 -B .tmp\manual_gate_test_lockout_build_only -G "Ninja" -DCMAKE_C_COMPILER="C:/Users/gregrg/AppData/Local/stm32cube/bundles/gnu-tools-for-stm32/14.3.1+st.2/bin/arm-none-eabi-gcc.exe" -DCMAKE_MAKE_PROGRAM="C:/Users/gregrg/AppData/Local/stm32cube/bundles/ninja/1.13.2+st.1/bin/ninja.exe"
```

Sandboxed result:

```text
Configuring incomplete.
CMake failed while running external Ninja with: operation not permitted.
```

Escalation result:

```text
Escalation was not executed because the automatic approval service returned
503 Service Unavailable.
```

Second configure attempt after correcting `REPO_ROOT`:

```text
External-tool escalation again returned 503 Service Unavailable from the
automatic approval service, so CMake / Ninja / GCC were not executed.
```

No object files, compiler output, or build-pass evidence are claimed.

## Static Carry-Forward

The previous source-package record still carries the current source-level
lockout evidence:

- six driver input pins are forced GPIO low;
- `PB12 / nFAULT` is kept as input;
- TIM1 `CCER` is cleared;
- TIM1 `MOE` and automatic output are cleared;
- TIM1 break is left enabled;
- forbidden normal MCSDK start / command-ingress / output-enable symbols are
  absent from lockout `Src` and `Inc`.

## Next Allowed Checkpoint

Follow-up completed in:

```text
stdrive101_manual_gate_test_lockout_object_build_pass_2026-06-20.md
```

That follow-up records a successful object-only build of
`stdrive101_gate_lockout_objects`. The target produced
`gate_test_lockout.c.obj` and `main_lockout.c.obj` only. No lockout ELF, HEX,
BIN, or MAP linked firmware image is claimed.

The next checkpoint after the object-only pass is USB-only runtime lockout
preparation, not runtime execution yet.

Still forbidden:

- linkable firmware image unless a separate review opens it;
- flash;
- Run / Debug;
- 24 V;
- Gate PWM output;
- Motor Pilot / Profiler;
- motor connection.
