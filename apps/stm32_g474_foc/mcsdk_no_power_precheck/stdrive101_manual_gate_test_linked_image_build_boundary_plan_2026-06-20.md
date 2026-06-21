# STDRIVE101 Manual Gate-Test Linked-Image Build-Boundary Plan - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LINKED-IMAGE-BUILD-BOUNDARY-PLAN-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-manual-gate-test-linked-image-build-boundary-plan-no-power`.
- Scope:
  Gate D no-power boundary plan for a future linkable lockout firmware image.
- Hardware action:
  none.
- Firmware runtime action:
  none; no flash, no Run / Debug, no USB runtime execution, and no linked
  image build in this record.
- Decision:
  `STDRIVE101 manual gate-test linked-image build-boundary plan no-power /
  object-only lockout build pass and USB-only runtime lockout preparation
  carried forward / future link inputs and minimum image artifacts named /
  boundary plan only / no linked image built / no flash / no runtime / no
  PWM-output validation / no powered-drive readiness`.

## Boundary

This record is a build-boundary plan only. It does not authorize:

- firmware flash;
- Run / Debug;
- USB runtime execution;
- 24 V;
- power-board powered connection;
- Gate PWM output;
- oscilloscope gate probing;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness.

No ELF, MAP, HEX, BIN, or other linked lockout image is produced or claimed by
this record.

## Inputs Carried Forward

The accepted isolated lockout source package remains:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_test_lockout_build_only_2026-06-20/
```

Source and build-file provenance carried forward:

| File | SHA256 |
| --- | --- |
| `Inc/gate_test_lockout.h` | `E1E69943BFEBC50C12C8FAAEE12203BD4FE5D9A6474E318C9EC10AA8111A9862` |
| `Src/gate_test_lockout.c` | `C5277630BC99E4BA1966799699F6660CA6ABB361EE17FF0AC89D8369135B264B` |
| `Src/main_lockout.c` | `D6BD1CB9BA4C54774E06C4B9381EA94C86903F7FB08426CAC904AEFB1DFB3EE3` |
| `CMakeLists.txt` | `B3887E85544EF5BB89309200689276312CF2D6BA0287CCAA89684B1F23190CE1` |

Object-only build evidence carried forward:

| Object file | Size | SHA256 |
| --- | ---: | --- |
| `gate_test_lockout.c.obj` | `2084` bytes | `C395D049FDCFC3213B65DF2813E07A663B5BF09D7C983BD2FBEC7025F0B79FE8` |
| `main_lockout.c.obj` | `924` bytes | `B2C77D50306258F7A7FFAE745119B17F9E18E703DC39A98CDC0810ACC4C66D98` |

The prior object-only build pass still proves object compilation only. It does
not prove startup, vector table, linker script, flashability, runtime GPIO
state, TIM1 runtime state, `nFAULT` readback, gate waveform behavior, or motor
readiness.

## Future Link Candidate Inputs

A future no-power linked-image build-only task must stay repo-local and must
not import the normal MCSDK generated start path.

Candidate link inputs are fixed to:

| Role | Candidate file | SHA256 |
| --- | --- | --- |
| Startup / vector table | `apps/stm32_g474_foc/nucleo_g474re_baseline/startup_stm32g474xx.s` | `2D1952A86701643338FBE284341C9099F96A52608D40CBDA35212BF14375AD2A` |
| Linker script | `apps/stm32_g474_foc/nucleo_g474re_baseline/STM32G474XX_FLASH.ld` | `9B7FAB3E33E6F326A5B578E4967A5FF94291D3B00AE4F652CEEE6BE60673CD8B` |
| `SystemInit` source | `apps/stm32_g474_foc/nucleo_g474re_baseline/Core/Src/system_stm32g4xx.c` | `1DE96C381D922635DABC0836D315D66C99B4E9D4A407FEF6EE6F5C4E32B0791A` |
| Newlib syscall stubs | `apps/stm32_g474_foc/nucleo_g474re_baseline/Core/Src/syscalls.c` | `03C06C72EAFB44B499814CF9234ABA57DD830F345D9B8779B5D7090E78517600` |
| Newlib heap stub | `apps/stm32_g474_foc/nucleo_g474re_baseline/Core/Src/sysmem.c` | `AD20F7B1FA1E7C73330727747222CF2FFA3245EBF035230EE9A157545E79DF95` |

The startup file calls `SystemInit`, initializes data and BSS, calls
`__libc_init_array`, and then calls `main`. A future build-only record must
therefore document how those symbols are satisfied and must record the exact
link command and linked symbol set.

## Future Build-Only Target Boundary

A later implementation task may add a link target only if it keeps this exact
boundary:

| Item | Required future value |
| --- | --- |
| Future target name | `stdrive101_gate_lockout_image` |
| Future build directory | `.tmp/manual_gate_test_lockout_linked_image` |
| Minimum artifacts | ELF and MAP |
| Optional artifacts | HEX or BIN only if a later flash phase explicitly opens them |
| Compiler | STM32Cube GNU Arm GCC `14.3.1` path already recorded in the object-only build pass, or a newly recorded replacement |
| Generator | Ninja `1.13.2` path already recorded in the object-only build pass, or a newly recorded replacement |

The future linked-image task must not use `MC_StartMotor1`, `MCI_START`,
PC13 start/stop, MCP command ingress, Motor Pilot ingress,
`R3_2_TurnOnLowSides`, `PWMC_SwitchOnPWM`, `LL_TIM_EnableAllOutputs`, Hall
closed-loop paths, speed-loop paths, or any normal generated MCSDK start path.

The future linked-image path must still force `PA8`, `PA9`, `PA10`, `PB13`,
`PB14`, and `PB15` low as GPIO outputs, keep `PB12 / nFAULT` as input, keep
TIM1 `CCER = 0`, clear TIM1 `MOE` and `AOE`, and leave break enabled.

## Required Future Build-Only Record

Before any USB-only runtime phase can be discussed, a separate dated
build-only record must include:

| Requirement | Required evidence |
| --- | --- |
| Source identity | The lockout source hashes above either match exactly or a replacement source review exists. |
| Link identity | Startup, linker script, vector table, `SystemInit`, syscall stubs, toolchain, generator, build command, and output paths are recorded. |
| Image artifacts | ELF and MAP paths, sizes, and SHA256 hashes are recorded. |
| Map review | MAP file shows only the lockout source, candidate startup/system/syscall inputs, and required runtime support. |
| Forbidden ingress screen | Static grep and symbol checks show the forbidden MCSDK start/output symbols are absent from the link path. |
| Output-lock screen | Static review confirms the lockout path still holds all six driver inputs low and keeps TIM1 outputs disabled. |
| Runtime boundary | Record states that the build-only result still does not authorize flash, Run / Debug, USB runtime, 24 V, Gate PWM, Motor Pilot / Profiler, motor connection, or readiness claims. |

If any required item is missing, the later task must stop at source or build
review and must not open USB-only runtime execution.

## Next Allowed Checkpoint

The next allowed checkpoint is a separate linked-image build-only record for
the lockout image.

Still forbidden until another dated phase gate opens it:

- flash;
- Run / Debug;
- USB runtime execution;
- 24 V;
- Gate PWM output;
- Motor Pilot / Profiler;
- motor connection.
