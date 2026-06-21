# STDRIVE101 Manual Gate-Test Linked-Image Build-Only Record - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LINKED-IMAGE-BUILD-ONLY-RECORD-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-manual-gate-test-linked-image-build-only-record-no-power`.
- Scope:
  Gate D no-power linked-image build-only evidence for the isolated lockout
  firmware path.
- Hardware action:
  none.
- Firmware runtime action:
  none; no flash, no Run / Debug, no USB runtime execution.
- Decision:
  `STDRIVE101 manual gate-test linked-image build-only record no-power /
  repo-local CMake linked target stdrive101_gate_lockout_image added /
  Generic bare-metal CMake configure and Ninja build passed / ELF and MAP
  artifacts produced and hashed / forbidden source ELF MAP screens clean /
  build-only evidence / no flash / no Run Debug / no USB runtime / no 24 V /
  no PWM-output validation / no powered-drive readiness`.

## Boundary

This record proves only that the isolated lockout source can be linked into a
bare-metal STM32G474 image with the selected repo-local startup, linker script,
system file, and syscall stubs.

It does not authorize:

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

The practical hardware boundary is no Gate PWM output, no motor action, and
no readiness claim.

No HEX or BIN image was generated in this record.

## Build Target Change

The repo-local build-only package remains:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_test_lockout_build_only_2026-06-20/
```

`CMakeLists.txt` now keeps the existing object-only target and adds linked
target `stdrive101_gate_lockout_image`.

| File | SHA256 |
| --- | --- |
| `CMakeLists.txt` | `31F7C3CBE2BA28773A5563F7FE2F6DD565D0F88659DE9EA5839F9A21A7FC292F` |
| `Inc/gate_test_lockout.h` | `E1E69943BFEBC50C12C8FAAEE12203BD4FE5D9A6474E318C9EC10AA8111A9862` |
| `Src/gate_test_lockout.c` | `C5277630BC99E4BA1966799699F6660CA6ABB361EE17FF0AC89D8369135B264B` |
| `Src/main_lockout.c` | `D6BD1CB9BA4C54774E06C4B9381EA94C86903F7FB08426CAC904AEFB1DFB3EE3` |

Linked target inputs:

| Role | File |
| --- | --- |
| Lockout source | `Src/gate_test_lockout.c` |
| Lockout main loop | `Src/main_lockout.c` |
| Startup / vector table | `apps/stm32_g474_foc/nucleo_g474re_baseline/startup_stm32g474xx.s` |
| Linker script | `apps/stm32_g474_foc/nucleo_g474re_baseline/STM32G474XX_FLASH.ld` |
| `SystemInit` source | `apps/stm32_g474_foc/nucleo_g474re_baseline/Core/Src/system_stm32g4xx.c` |
| Newlib syscall stubs | `apps/stm32_g474_foc/nucleo_g474re_baseline/Core/Src/syscalls.c` |
| Newlib heap stub | `apps/stm32_g474_foc/nucleo_g474re_baseline/Core/Src/sysmem.c` |

## Configure And Build

An initial local build attempt configured without `CMAKE_SYSTEM_NAME=Generic`.
That path stopped before evidence acceptance because the linker command
contained Windows host flags. The build directory was removed after confirming
the resolved path stayed under the repository workspace, then reconfigured with
an explicit bare-metal Generic system.

Accepted configure command:

```powershell
cmake -S apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_test_lockout_build_only_2026-06-20 -B .tmp\manual_gate_test_lockout_linked_image -G "Ninja" -DCMAKE_SYSTEM_NAME=Generic -DCMAKE_SYSTEM_PROCESSOR=arm -DCMAKE_BUILD_TYPE=Debug -DCMAKE_C_COMPILER="C:/Users/gregrg/AppData/Local/stm32cube/bundles/gnu-tools-for-stm32/14.3.1+st.2/bin/arm-none-eabi-gcc.exe" -DCMAKE_ASM_COMPILER="C:/Users/gregrg/AppData/Local/stm32cube/bundles/gnu-tools-for-stm32/14.3.1+st.2/bin/arm-none-eabi-gcc.exe" -DCMAKE_MAKE_PROGRAM="C:/Users/gregrg/AppData/Local/stm32cube/bundles/ninja/1.13.2+st.1/bin/ninja.exe" -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY
```

Accepted build command:

```powershell
cmake --build .tmp\manual_gate_test_lockout_linked_image --target stdrive101_gate_lockout_image --verbose
```

Result:

- configure exit code: `0`;
- build exit code: `0`;
- C compiler: GNU Arm GCC `14.3.1`;
- ASM compiler: GNU Arm GCC `14.3.1`;
- generator: Ninja;
- `CMAKE_SYSTEM_NAME`: `Generic`;
- `CMAKE_SYSTEM_PROCESSOR`: `arm`;
- `CMAKE_BUILD_TYPE`: `Debug`;
- `CMAKE_TRY_COMPILE_TARGET_TYPE`: `STATIC_LIBRARY`.

Link memory output:

```text
Memory region         Used Size  Region Size  %age Used
             RAM:        1568 B       128 KB      1.20%
           FLASH:        1356 B       512 KB      0.26%
```

`arm-none-eabi-size` output:

```text
text data bss dec hex
1356 0 1568 2924 b6c
```

## Produced Artifacts

| Artifact | Size | SHA256 |
| --- | ---: | --- |
| `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf` | `24788` bytes | `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6` |
| `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.map` | `123825` bytes | `A020546A3D1D56B1C509939161BD80E5A25EC5843C928B9BC13E8D07684FF6C0` |

These artifacts are build-only evidence in the local `.tmp` directory. They
are not a flash or runtime authorization.

## Symbol And MAP Review

Key linked symbols observed with `arm-none-eabi-nm -n`:

| Symbol | Address |
| --- | --- |
| `g_pfnVectors` | `0x08000000` |
| `configure_pin_as_output_low` | `0x08000218` |
| `configure_pin_as_input` | `0x08000290` |
| `force_driver_inputs_low` | `0x080002f0` |
| `configure_fault_input` | `0x08000344` |
| `lock_tim1_outputs` | `0x08000358` |
| `read_nfault_high` | `0x080003a0` |
| `gate_test_lockout_force_safe_state` | `0x080003c4` |
| `gate_test_lockout_init` | `0x080003dc` |
| `gate_test_lockout_poll` | `0x080003f4` |
| `main` | `0x08000474` |
| `Reset_Handler` | `0x08000484` |
| `SystemInit` | `0x080004d6` |
| `__libc_init_array` | `0x080004e4` |
| `_estack` | `0x20020000` |

MAP review shows the expected object inputs:

- `gate_test_lockout.c.obj`;
- `main_lockout.c.obj`;
- `startup_stm32g474xx.s.obj`;
- `system_stm32g4xx.c.obj`;
- `syscalls.c.obj`;
- `sysmem.c.obj`;
- required `libg_nano.a` runtime support pulled by startup and newlib nano.

The `libg_nano.a` entries are runtime support from the selected bare-metal C
library path. They are not MCSDK start, command ingress, Motor Pilot, Hall
closed-loop, speed-loop, or PWM-output evidence.

Forbidden screen commands were run against:

- lockout `Src` and `Inc`;
- linked ELF symbols;
- linked MAP file.

Forbidden patterns checked:

```text
MC_StartMotor1|MCI_START|PC13|MCP|Motor Pilot|R3_2_TurnOnLowSides|PWMC_SwitchOnPWM|LL_TIM_EnableAllOutputs|HALL_M1|PID_|STC_
```

Result:

- source grep: no forbidden source matches;
- ELF symbol screen: no forbidden ELF symbol matches;
- MAP screen: no forbidden MAP matches.

## Output-Lock Boundary Carried Forward

The linked path still uses the isolated lockout source package. Static source
review remains:

- `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and `PB15` are forced low as GPIO
  outputs by the lockout path;
- `PB12 / nFAULT` is kept as input;
- TIM1 `CCER` is cleared;
- TIM1 `BDTR.MOE` and automatic output are cleared;
- TIM1 break remains enabled.

This is source and linked-image build evidence only. It is not register
readback, waveform evidence, USB runtime evidence, 24 V evidence, or motor
evidence.

## Next Allowed Checkpoint

The next allowed checkpoint is a separate USB-only runtime lockout phase-gate
plan or review. That later checkpoint must still be explicitly dated and must
not run runtime by implication.

Still forbidden:

- flash;
- Run / Debug;
- USB runtime execution without a separate dated runtime gate;
- 24 V;
- Gate PWM output;
- Motor Pilot / Profiler;
- motor connection;
- power-stage readiness or motor readiness claims.
