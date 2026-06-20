# STDRIVE101 Manual Gate-Test Lockout Object-Only Build Pass - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LOCKOUT-OBJECT-BUILD-PASS-NO-POWER-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-manual-gate-test-lockout-object-build-pass-no-power`.
- Scope:
  Gate B no-power object-only build pass for the isolated lockout source
  package.
- Hardware action:
  none.
- Firmware runtime action:
  none; no flash, no Run / Debug, no 24 V runtime.
- Decision:
  `STDRIVE101 manual gate-test lockout object-only build pass no-power /
  repo-local CMake object library configured with STM32Cube GNU Arm GCC
  14.3.1 and Ninja 1.13.2 / stdrive101_gate_lockout_objects built successfully
  / gate_test_lockout.c.obj and main_lockout.c.obj produced / no lockout ELF
  HEX BIN MAP linked image produced / no flash / no runtime / no PWM-output
  validation / no powered-drive readiness`.

## Boundary

This record is no-power object-build evidence only. It does not authorize:

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

## Configure Command

Working directory:

```text
C:\Users\gregrg\Documents\Codex\2026-04-30\qiansai\foc_learning_repo
```

Command:

```powershell
cmake -S apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_test_lockout_build_only_2026-06-20 -B .tmp\manual_gate_test_lockout_build_only -G "Ninja" -DCMAKE_C_COMPILER="C:/Users/gregrg/AppData/Local/stm32cube/bundles/gnu-tools-for-stm32/14.3.1+st.2/bin/arm-none-eabi-gcc.exe" -DCMAKE_MAKE_PROGRAM="C:/Users/gregrg/AppData/Local/stm32cube/bundles/ninja/1.13.2+st.1/bin/ninja.exe" -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY
```

Result:

```text
Exit code: 0
C compiler identification: GNU 14.3.1
Build files written to .tmp/manual_gate_test_lockout_build_only
```

`CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY` was used so CMake compiler
checks do not require producing a linkable firmware image.

## Build Command

Command:

```powershell
cmake --build .tmp\manual_gate_test_lockout_build_only --target stdrive101_gate_lockout_objects --verbose
```

Result:

```text
Exit code: 0
Ninja built 2/2 source files.
```

Compiler options shown in verbose output include:

```text
-DSTM32G474xx
-std=gnu11
-mcpu=cortex-m4
-mthumb
-Wall
-Wextra
-Werror
```

## Object Artifacts

The lockout target produced:

| Object file | Size | SHA256 |
| --- | ---: | --- |
| `.tmp/manual_gate_test_lockout_build_only/CMakeFiles/stdrive101_gate_lockout_objects.dir/Src/gate_test_lockout.c.obj` | `2084` bytes | `C395D049FDCFC3213B65DF2813E07A663B5BF09D7C983BD2FBEC7025F0B79FE8` |
| `.tmp/manual_gate_test_lockout_build_only/CMakeFiles/stdrive101_gate_lockout_objects.dir/Src/main_lockout.c.obj` | `924` bytes | `B2C77D50306258F7A7FFAE745119B17F9E18E703DC39A98CDC0810ACC4C66D98` |

No lockout ELF, HEX, BIN, or MAP linked image was produced by this target.

CMake also generated its own internal compiler-check file:

```text
.tmp/manual_gate_test_lockout_build_only/CMakeFiles/4.3.2/CMakeDetermineCompilerABI_C.bin
```

That file is CMake internal compiler-detection output, not a lockout firmware
image and not a flashable project artifact.

## Toolchain Evidence

From `.tmp/manual_gate_test_lockout_build_only/CMakeCache.txt`:

```text
CMAKE_GENERATOR = Ninja
CMAKE_C_COMPILER = C:/Users/gregrg/AppData/Local/stm32cube/bundles/gnu-tools-for-stm32/14.3.1+st.2/bin/arm-none-eabi-gcc.exe
CMAKE_MAKE_PROGRAM = C:/Users/gregrg/AppData/Local/stm32cube/bundles/ninja/1.13.2+st.1/bin/ninja.exe
CMAKE_TRY_COMPILE_TARGET_TYPE = STATIC_LIBRARY
```

## What This Upgrades

Allowed upgraded claim:

```text
The isolated STDRIVE101 lockout source package compiles to object files for
the STM32G474 CMSIS target under no-power compile-only scope.
```

## What This Does Not Upgrade

This result does not prove:

- a linked firmware image exists;
- startup or vector-table correctness;
- linker script correctness;
- flashability;
- board runtime behavior;
- GPIO runtime state;
- TIM1 runtime register state;
- `nFAULT` runtime readback;
- `REG12` behavior;
- gate waveform behavior;
- current-sense correctness;
- Hall closed-loop behavior;
- sensorless operation;
- power-stage readiness or motor readiness.

## Next Allowed Checkpoint

The next no-power checkpoint is a USB-only runtime lockout preparation record,
not runtime yet. That preparation must define:

- exact flash image boundary, if a later phase opens it;
- pre-flash source hashes;
- no-24V / motor-disconnected requirements;
- expected USB-only pin readings;
- rollback path;
- stop rules.

Still forbidden until a separate dated phase gate opens it:

- flash;
- Run / Debug;
- 24 V;
- Gate PWM output;
- Motor Pilot / Profiler;
- motor connection.
