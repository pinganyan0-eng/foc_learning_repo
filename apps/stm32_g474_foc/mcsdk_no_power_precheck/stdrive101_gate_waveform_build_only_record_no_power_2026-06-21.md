# STDRIVE101 Gate-Waveform Build-Only Record No-Power - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-BUILD-ONLY-RECORD-NO-POWER-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-build-only-record-no-power`.
- Gate:
  Gate E2 from the gate-waveform / PWM-output no-power phase-gate ladder.
- Scope:
  object-only and linked-image build-only evidence for the exact Gate E1
  reviewed source package.
- Source package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_source_package_2026-06-21/`.
- Build-only package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_build_only_2026-06-21/`.
- Clean build directory:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/`.
- Hardware action:
  none in this record. No 24 V is applied by this build-only check.
- Runtime action:
  none in this record. No flash, Run / Debug, USB runtime execution, or Gate
  PWM output is performed or opened.
- Decision:
  `STDRIVE101 gate-waveform build-only record no-power / Gate E2 object-only
  and linked-image build-only evidence for the exact Gate E1 reviewed source
  package / separate build-only package defines
  GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK / Gate E1 source package remains
  source-review only and has no CMakeLists / Generic arm CMake configure and
  Ninja build passed / object target
  stdrive101_gate_waveform_candidate_objects and linked target
  stdrive101_gate_waveform_candidate_image built / ELF and MAP artifacts
  produced and hashed / -nostdlib minimal runtime keeps newlib malloc free
  paths out of the MAP / forbidden source ELF MAP screens clean / build-only
  evidence / no flash / no Run Debug / no USB runtime / no 24 V / no Gate PWM
  output / no Motor Pilot / no Motor Profiler / no motor connection / no
  powered-drive readiness`.

## Boundary

This record is Gate E2 build-only evidence. It does not authorize:

- firmware flash;
- Run / Debug;
- USB runtime execution;
- applying 24 V;
- Gate PWM output on hardware;
- oscilloscope probing on live gate or phase nodes;
- normal generated MCSDK application execution;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

The Gate E1 source package still has no `CMakeLists.txt`. The only place that
defines `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK` is the separate Gate E2
build-only package.

## Build Boundary

| Item | Value |
| --- | --- |
| Object target | `stdrive101_gate_waveform_candidate_objects` |
| Linked target | `stdrive101_gate_waveform_candidate_image` |
| Output image | `stdrive101_gate_waveform_candidate_image.elf` |
| MAP output | `stdrive101_gate_waveform_candidate_image.map` |
| HEX / BIN target | none |
| CMake system | `CMAKE_SYSTEM_NAME=Generic` |
| CMake processor | `CMAKE_SYSTEM_PROCESSOR=arm` |
| Try-compile policy | `CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY` |
| Linker script | `apps/stm32_g474_foc/nucleo_g474re_baseline/STM32G474XX_FLASH.ld` |
| Startup source | `apps/stm32_g474_foc/nucleo_g474re_baseline/startup_stm32g474xx.s` |
| System source | `apps/stm32_g474_foc/nucleo_g474re_baseline/Core/Src/system_stm32g4xx.c` |
| Runtime stubs | `manual_gate_waveform_build_only_2026-06-21/Src/minimal_runtime.c` |
| Newlib policy | `-nostdlib`, local `__libc_init_array`, `_init`, and `_fini` stubs |

No HEX / BIN target is produced or claimed by this build-only package.
No HEX or BIN target is defined here.

The linked image intentionally avoids newlib by using `-nostdlib` and local
empty `__libc_init_array`, `_init`, and `_fini` stubs. This keeps unused
`malloc`, `free`, and `_sbrk` support paths out of the MAP review.

## Commands

Configure:

```powershell
cmake -S apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_build_only_2026-06-21 -B .tmp\manual_gate_waveform_build_only_2026-06-21_clean -G Ninja -DCMAKE_SYSTEM_NAME=Generic -DCMAKE_SYSTEM_PROCESSOR=arm -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY -DCMAKE_C_COMPILER=$env:USERPROFILE\AppData\Local\stm32cube\bundles\gnu-tools-for-stm32\14.3.1+st.2\bin\arm-none-eabi-gcc.exe -DCMAKE_ASM_COMPILER=$env:USERPROFILE\AppData\Local\stm32cube\bundles\gnu-tools-for-stm32\14.3.1+st.2\bin\arm-none-eabi-gcc.exe -DCMAKE_MAKE_PROGRAM=$env:USERPROFILE\AppData\Local\stm32cube\bundles\ninja\1.13.2+st.1\bin\ninja.exe
```

Result:

- exit code `0`;
- `CMAKE_SYSTEM_NAME=Generic`;
- `CMAKE_SYSTEM_PROCESSOR=arm`;
- `CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY`.

Build:

```powershell
cmake --build .tmp\manual_gate_waveform_build_only_2026-06-21_clean --target stdrive101_gate_waveform_candidate_objects stdrive101_gate_waveform_candidate_image
```

Result:

- exit code `0`;
- built `stdrive101_gate_waveform_candidate_objects`;
- built `stdrive101_gate_waveform_candidate_image`.

Tool versions:

```text
cmake version 4.3.2
arm-none-eabi-gcc.exe (GNU Tools for STM32 14.3.rel1.20251027-0700) 14.3.1 20250623
ninja 1.13.2
```

## Files And Hashes

Build-only package files:

| File | SHA256 |
| --- | --- |
| `manual_gate_waveform_build_only_2026-06-21/README.md` | `9048571ED14E59ABE698D933BA2150061B649F22A42D11D7CE68DCDE81C2C5FF` |
| `manual_gate_waveform_build_only_2026-06-21/CMakeLists.txt` | `82D18A906B569AD5E93D57E996122BF42F45CDBF1F9C975E390723EA3D2CDD64` |
| `manual_gate_waveform_build_only_2026-06-21/Src/minimal_runtime.c` | `1DC25ACDEDE11FB57FBED51722664566F707056AE856B379ED3AF9095790EA42` |

Clean build artifacts:

| Artifact | Size | SHA256 |
| --- | ---: | --- |
| `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.elf` | `26132` | `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C` |
| `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.map` | `32352` | `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C` |

Clean object hashes:

| Object | SHA256 |
| --- | --- |
| `CMakeFiles/stdrive101_gate_waveform_candidate_objects.dir/.../Src/gate_waveform_candidate.c.obj` | `27898EEA12B92A2DE121788E056BBEB0E457F54619B425DB6AEDC4E3E1E1FB84` |
| `CMakeFiles/stdrive101_gate_waveform_candidate_objects.dir/.../Src/main_waveform_candidate.c.obj` | `C5C4B8CD074E7D8810A1E7E2F6EED41890AD623FF1EE00812E1AB52A9D09CCDE` |
| `CMakeFiles/stdrive101_gate_waveform_candidate_image.dir/.../Src/gate_waveform_candidate.c.obj` | `27898EEA12B92A2DE121788E056BBEB0E457F54619B425DB6AEDC4E3E1E1FB84` |
| `CMakeFiles/stdrive101_gate_waveform_candidate_image.dir/.../Src/main_waveform_candidate.c.obj` | `C5C4B8CD074E7D8810A1E7E2F6EED41890AD623FF1EE00812E1AB52A9D09CCDE` |
| `CMakeFiles/stdrive101_gate_waveform_candidate_image.dir/Src/minimal_runtime.c.obj` | `E1FD810C65E3D81A01A1545689CDC27592560CDE4E64B90EFB75918B669E9489` |
| `CMakeFiles/stdrive101_gate_waveform_candidate_image.dir/.../startup_stm32g474xx.s.obj` | `72DAD9582B377A73C517B804D31B8C136635862ACAD9FA08A5AEE0BA8E2968E8` |
| `CMakeFiles/stdrive101_gate_waveform_candidate_image.dir/.../Core/Src/system_stm32g4xx.c.obj` | `A02922F4D7DF01C63500F9CE78680ED9602D929F5E710E8A03B7C178A145ADE4` |

## Size And Memory

`arm-none-eabi-size` output:

```text
   text    data     bss     dec     hex filename
   1852       0    1544    3396     d44 .\.tmp\manual_gate_waveform_build_only_2026-06-21_clean\stdrive101_gate_waveform_candidate_image.elf
```

Linker memory summary:

| Region | Used | Total | Percent |
| --- | ---: | ---: | ---: |
| RAM | `1544 B` | `128 KB` | `1.18%` |
| FLASH | `1852 B` | `512 KB` | `0.35%` |

## Key Symbols

`arm-none-eabi-nm -n` selected symbols:

```text
08000000 R g_pfnVectors
08000420 t disable_tim1_outputs_keep_counter
0800051c t wait_for_pwm_periods_or_fault
080005a4 T gate_waveform_candidate_force_idle_low
080005bc T gate_waveform_candidate_run_once
080006a4 T main
080006b8 T __libc_init_array
080006c4 T _init
080006d0 T _fini
080006dc W Reset_Handler
0800072e T SystemInit
20020000 R _estack
```

These symbols prove link visibility only. They do not prove reset-time pin
state on hardware, firmware runtime behavior, or waveform behavior.

## Static Screens

Source and build package forbidden screen:

```powershell
rg -n "MC_StartMotor1|MCI_START|PC13|MCP|ASPEP|Motor Pilot|Motor Profiler|R3_2_TurnOnLowSides|PWMC_SwitchOnPWM|LL_TIM_EnableAllOutputs|HALL_M1|PID_|STC_|HAL_Delay|printf|malloc|free" apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_build_only_2026-06-21 apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_source_package_2026-06-21
```

Result:

- no forbidden source or CMake path matches;
- the only text hits are README boundary language for `Motor Pilot`,
  `Motor Profiler`, and the `malloc/free` MAP-review explanation;
- no `MC_StartMotor1`, `MCI_START`, PC13, MCP, ASPEP,
  `R3_2_TurnOnLowSides`, `PWMC_SwitchOnPWM`,
  `LL_TIM_EnableAllOutputs`, Hall, PID, speed-loop, blocking delay, printf,
  or dynamic-allocation source path was found.

ELF symbol forbidden screen:

```powershell
arm-none-eabi-nm .tmp\manual_gate_waveform_build_only_2026-06-21_clean\stdrive101_gate_waveform_candidate_image.elf | Select-String -Pattern "MC_StartMotor1|MCI_START|PC13|MCP|ASPEP|Motor|Profiler|R3_2_TurnOnLowSides|PWMC_SwitchOnPWM|LL_TIM_EnableAllOutputs|HALL_M1|PID_|STC_|HAL_Delay|printf|malloc|free|_sbrk"
```

Result:

- no forbidden ELF symbol matches.

MAP forbidden screen:

```powershell
Select-String -Path .tmp\manual_gate_waveform_build_only_2026-06-21_clean\stdrive101_gate_waveform_candidate_image.map -Pattern "MC_StartMotor1|MCI_START|PC13|MCP|ASPEP|Motor|Profiler|R3_2_TurnOnLowSides|PWMC_SwitchOnPWM|LL_TIM_EnableAllOutputs|HALL_M1|PID_|STC_|HAL_Delay|printf|malloc|free|_sbrk"
```

Result:

- no forbidden MAP matches.

## Remaining Review Risks

This build-only record still does not prove:

- that this ELF should be flashed;
- reset-time or runtime pin behavior on real hardware;
- that the six candidate driver-input pins are low on a powered board;
- that any physical waveform is present;
- that dead-time, polarity, break input, gate-driver behavior, or phase-node
  behavior is safe under 24 V;
- that Motor Pilot or Motor Profiler can be opened;
- that a motor can be connected.

Those require later separate gates and direct measurement evidence.

## Next Allowed Checkpoint

The next allowed repository-side checkpoint is Gate E3 only:

```text
USB-only neutral-state phase-gate plan or review for the Gate E2 image
```

Gate E3 must be a plan or review unless a later separate dated execution-entry explicitly opens USB-only runtime.
Gate E3 still must not open flash, Run / Debug, USB runtime execution, 24 V,
Gate PWM output, Motor Pilot, Motor Profiler, motor connection, power-stage
readiness, or motor readiness by default.

Still forbidden after this Gate E2 record:

- flash;
- Run / Debug;
- USB runtime execution;
- 24 V;
- Gate PWM output;
- oscilloscope probing on live gate or phase nodes;
- Motor Pilot / Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.
