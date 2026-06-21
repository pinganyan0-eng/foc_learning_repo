# STDRIVE101 Gate-Waveform Neutral-Wrapper Build-Only Record No-Power - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-BUILD-ONLY-RECORD-NO-POWER-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-build-only-record-no-power`.
- Scope:
  object-only and linked-image build-only evidence for the neutral-wrapper
  source review.
- Source packages:
  `manual_gate_waveform_source_package_2026-06-21/` and
  `manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/`.
- Build-only package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_neutral_wrapper_build_only_2026-06-21/`.
- Clean build directory:
  `.tmp/gwnw_build_2026-06-21_clean/`.
- Hardware action:
  none in this record. No 24 V is applied by this build-only check.
- Runtime action:
  none in this record. No flash, Run / Debug, USB runtime execution, or Gate
  PWM output is performed or opened.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper build-only record no-power /
  object-only and linked-image build-only evidence for the neutral-wrapper
  source review / separate build-only package defines
  GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK and
  GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK / source-review packages remain
  source-review only and have no CMakeLists / build inputs include reviewed
  gate_waveform_candidate.c and wrapper main_neutral_wrapper.c / old
  main_waveform_candidate.c excluded from build.ninja and CMake source inputs /
  Generic arm CMake configure and Ninja build passed in short clean build dir /
  object target stdrive101_gate_waveform_neutral_wrapper_objects and linked
  target stdrive101_gate_waveform_neutral_wrapper_image built / ELF and MAP
  artifacts produced and hashed / ELF symbol table retains
  gate_waveform_neutral_wrapper_hold_idle_forever and does not retain
  gate_waveform_candidate_run_once / MAP lists gate_waveform_candidate_run_once
  only as a discarded zero-address input section from gate_waveform_candidate.c
  / no HEX or BIN target / build-only evidence / no flash / no Run Debug / no
  USB runtime execution / no 24 V / no Gate PWM output / no Motor Pilot / no
  Motor Profiler / no motor connection / no powered-drive readiness`.

## Boundary

This record is build-only evidence. It does not authorize:

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

The source-review packages still have no `CMakeLists.txt`. The only place that
defines `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK` and
`GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK` is the separate build-only package.

## Build Boundary

| Item | Value |
| --- | --- |
| Object target | `stdrive101_gate_waveform_neutral_wrapper_objects` |
| Linked target | `stdrive101_gate_waveform_neutral_wrapper_image` |
| Output image | `stdrive101_gate_waveform_neutral_wrapper_image.elf` |
| MAP output | `stdrive101_gate_waveform_neutral_wrapper_image.map` |
| HEX / BIN target | none |
| CMake system | `CMAKE_SYSTEM_NAME=Generic` |
| CMake processor | `CMAKE_SYSTEM_PROCESSOR=arm` |
| Try-compile policy | `CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY` |
| Linker script | `apps/stm32_g474_foc/nucleo_g474re_baseline/STM32G474XX_FLASH.ld` |
| Startup source | `apps/stm32_g474_foc/nucleo_g474re_baseline/startup_stm32g474xx.s` |
| System source | `apps/stm32_g474_foc/nucleo_g474re_baseline/Core/Src/system_stm32g4xx.c` |
| Runtime stubs | `manual_gate_waveform_neutral_wrapper_build_only_2026-06-21/Src/minimal_runtime.c` |
| Newlib policy | `-nostdlib`, local `__libc_init_array`, `_init`, and `_fini` stubs |

No HEX or BIN target is defined here.

The linked image intentionally avoids newlib by using `-nostdlib` and local
empty `__libc_init_array`, `_init`, and `_fini` stubs. This keeps unused
`malloc`, `free`, and `_sbrk` support paths out of the retained ELF symbol
review.

## Source Inputs

The build-only CMake source inputs are:

```text
manual_gate_waveform_source_package_2026-06-21/Src/gate_waveform_candidate.c
manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/Src/main_neutral_wrapper.c
manual_gate_waveform_neutral_wrapper_build_only_2026-06-21/Src/minimal_runtime.c
nucleo_g474re_baseline/startup_stm32g474xx.s
nucleo_g474re_baseline/Core/Src/system_stm32g4xx.c
```

The old
`manual_gate_waveform_source_package_2026-06-21/Src/main_waveform_candidate.c`
is intentionally excluded from both build-only targets. `build.ninja` contains
`gate_waveform_candidate.c` and `main_neutral_wrapper.c`, and has no
`main_waveform_candidate` match.

## Commands

Configure:

```powershell
cmake -S apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_neutral_wrapper_build_only_2026-06-21 -B .tmp\gwnw_build_2026-06-21_clean -G Ninja -DCMAKE_SYSTEM_NAME=Generic -DCMAKE_SYSTEM_PROCESSOR=arm -DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY -DCMAKE_C_COMPILER=$env:USERPROFILE\AppData\Local\stm32cube\bundles\gnu-tools-for-stm32\14.3.1+st.2\bin\arm-none-eabi-gcc.exe -DCMAKE_ASM_COMPILER=$env:USERPROFILE\AppData\Local\stm32cube\bundles\gnu-tools-for-stm32\14.3.1+st.2\bin\arm-none-eabi-gcc.exe -DCMAKE_MAKE_PROGRAM=$env:USERPROFILE\AppData\Local\stm32cube\bundles\ninja\1.13.2+st.1\bin\ninja.exe
```

Result:

- exit code `0`;
- `CMAKE_SYSTEM_NAME=Generic`;
- `CMAKE_SYSTEM_PROCESSOR=arm`;
- `CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY`;
- short clean build directory used to avoid Windows object-path warnings.

Build:

```powershell
cmake --build .tmp\gwnw_build_2026-06-21_clean --target stdrive101_gate_waveform_neutral_wrapper_objects stdrive101_gate_waveform_neutral_wrapper_image
```

Result:

- exit code `0`;
- built `stdrive101_gate_waveform_neutral_wrapper_objects`;
- built `stdrive101_gate_waveform_neutral_wrapper_image`;
- linker memory report: RAM `1536 B / 128 KB / 1.17%`, FLASH `1044 B / 512 KB / 0.20%`.

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
| `manual_gate_waveform_neutral_wrapper_build_only_2026-06-21/README.md` | `DB0D10C67B14C9322CF04B777BCF922CC96A05462FB950B654B4768DD43763CD` |
| `manual_gate_waveform_neutral_wrapper_build_only_2026-06-21/CMakeLists.txt` | `ADDA45A3E703B32BD521ED5E3F03C6AF7CC8FFD37613D90EBCD483BE8B6E3814` |
| `manual_gate_waveform_neutral_wrapper_build_only_2026-06-21/Src/minimal_runtime.c` | `1DC25ACDEDE11FB57FBED51722664566F707056AE856B379ED3AF9095790EA42` |

Clean build artifacts:

| Artifact | Size | SHA256 |
| --- | ---: | --- |
| `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.elf` | `12044` | `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591` |
| `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.map` | `27079` | `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83` |

Clean object hashes:

| Object | SHA256 |
| --- | --- |
| `CMakeFiles/stdrive101_gate_waveform_neutral_wrapper_objects.dir/.../Src/gate_waveform_candidate.c.obj` | `64C89BB1E39DDBB98AF5F2EF9563800D6A6138AA4530C2B6790E8078048D2799` |
| `CMakeFiles/stdrive101_gate_waveform_neutral_wrapper_objects.dir/.../Src/main_neutral_wrapper.c.obj` | `188950B9ADA0C696E6C6CF6EF29A070391A5464D1A60A03E781939163E5B96B1` |
| `CMakeFiles/stdrive101_gate_waveform_neutral_wrapper_image.dir/.../Src/gate_waveform_candidate.c.obj` | `64C89BB1E39DDBB98AF5F2EF9563800D6A6138AA4530C2B6790E8078048D2799` |
| `CMakeFiles/stdrive101_gate_waveform_neutral_wrapper_image.dir/.../Src/main_neutral_wrapper.c.obj` | `188950B9ADA0C696E6C6CF6EF29A070391A5464D1A60A03E781939163E5B96B1` |
| `CMakeFiles/stdrive101_gate_waveform_neutral_wrapper_image.dir/Src/minimal_runtime.c.obj` | `87E70EAF33E61EF8255DCB13BC5CC4F40ED89F3D55EC90176C5C51AC3766F98B` |
| `CMakeFiles/stdrive101_gate_waveform_neutral_wrapper_image.dir/.../startup_stm32g474xx.s.obj` | `5AB74A722C13AE7238DF5A611FB1F9E03C93EE370F86F1464BFF48EE8C016487` |
| `CMakeFiles/stdrive101_gate_waveform_neutral_wrapper_image.dir/.../Core/Src/system_stm32g4xx.c.obj` | `DA172ED0E4297918778BC3F2F5E55B74F32F05457DD908EB149616A45C066A8C` |

## Size And Memory

`arm-none-eabi-size` output:

```text
   text    data     bss     dec     hex filename
   1044       0    1536    2580     a14 .tmp\gwnw_build_2026-06-21_clean\stdrive101_gate_waveform_neutral_wrapper_image.elf
```

Linker memory summary:

| Region | Used | Total | Percent |
| --- | ---: | ---: | ---: |
| RAM | `1536 B` | `128 KB` | `1.17%` |
| FLASH | `1044 B` | `512 KB` | `0.20%` |

## Key Symbols

`arm-none-eabi-nm -n` selected symbols:

```text
08000000 R g_pfnVectors
0800035c T gate_waveform_candidate_force_idle_low
08000374 T gate_waveform_neutral_wrapper_hold_idle_forever
08000382 T main
08000390 T __libc_init_array
0800039c T _init
080003a8 T _fini
080003b4 W Reset_Handler
08000406 T SystemInit
20020000 R _estack
```

The retained ELF symbol table has no `gate_waveform_candidate_run_once` and no
`main_waveform_candidate` symbol.

## Static Screens

Source and build package screen:

```powershell
rg -n "MC_StartMotor1|MCI_START|PC13|MCP|ASPEP|Motor Pilot|Motor Profiler|R3_2_TurnOnLowSides|PWMC_SwitchOnPWM|LL_TIM_EnableAllOutputs|HALL_M1|PID_|STC_|HAL_Delay|printf|malloc|free|main_waveform_candidate|\.bin|\.hex|objcopy|add_custom_command|FLASH_RUN" apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_neutral_wrapper_build_only_2026-06-21 apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_neutral_wrapper_source_package_2026-06-21\Inc apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_neutral_wrapper_source_package_2026-06-21\Src
```

Result:

- no forbidden source or CMake path matches;
- the only text hits are README boundary language for `Motor Pilot`,
  `Motor Profiler`, old `main_waveform_candidate.c` exclusion, and the
  `malloc/free` MAP-review explanation;
- no `MC_StartMotor1`, `MCI_START`, PC13, MCP, ASPEP,
  `R3_2_TurnOnLowSides`, `PWMC_SwitchOnPWM`,
  `LL_TIM_EnableAllOutputs`, Hall, PID, speed-loop, blocking delay, printf,
  or dynamic-allocation source path was found in build source inputs or
  wrapper `Inc/` / `Src/`.

Build-input exclusion screen:

```powershell
rg -n "main_waveform_candidate" .tmp\gwnw_build_2026-06-21_clean\build.ninja apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_neutral_wrapper_build_only_2026-06-21\CMakeLists.txt
```

Result:

- no `main_waveform_candidate` match in `build.ninja`;
- no `main_waveform_candidate` match in the build-only `CMakeLists.txt`.

HEX / BIN target screen:

```powershell
rg -n "add_custom_command|\.hex|\.bin|objcopy|FLASH_RUN|ST-LINK|NOD_G474RE" apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_neutral_wrapper_build_only_2026-06-21\CMakeLists.txt .tmp\gwnw_build_2026-06-21_clean\build.ninja
Get-ChildItem .tmp\gwnw_build_2026-06-21_clean -Recurse -Include *.bin,*.hex
```

Result:

- no CMake or Ninja path defines HEX / BIN / objcopy / flash-run actions;
- no `.bin` or `.hex` artifact exists in the clean build directory.

ELF symbol forbidden screen:

```powershell
arm-none-eabi-nm .tmp\gwnw_build_2026-06-21_clean\stdrive101_gate_waveform_neutral_wrapper_image.elf | Select-String -Pattern "MC_StartMotor1|MCI_START|PC13|MCP|ASPEP|Motor|Profiler|R3_2_TurnOnLowSides|PWMC_SwitchOnPWM|LL_TIM_EnableAllOutputs|HALL_M1|PID_|STC_|HAL_Delay|printf|malloc|free|_sbrk|gate_waveform_candidate_run_once|main_waveform_candidate"
```

Result:

- no forbidden retained ELF symbol matches.

MAP screen:

```powershell
Select-String -Path .tmp\gwnw_build_2026-06-21_clean\stdrive101_gate_waveform_neutral_wrapper_image.map -Pattern "MC_StartMotor1|MCI_START|PC13|MCP|ASPEP|Motor|Profiler|R3_2_TurnOnLowSides|PWMC_SwitchOnPWM|LL_TIM_EnableAllOutputs|HALL_M1|PID_|STC_|HAL_Delay|printf|malloc|free|_sbrk|main_waveform_candidate"
```

Result:

- no forbidden MAP matches for normal generated MCSDK start, command ingress,
  PWM-output enable, Motor Pilot / Profiler, Hall, PID, speed-loop, delay,
  printf, dynamic allocation, `_sbrk`, or old `main_waveform_candidate`.

Additional MAP observation:

```text
.text.gate_waveform_candidate_run_once
                0x00000000       0xe8 .../gate_waveform_candidate.c.obj
```

This appears only in the MAP discarded-input-section area at address
`0x00000000`. It is not retained as an ELF symbol and is not called by
`main_neutral_wrapper.c`. This is expected because
`gate_waveform_candidate.c` is compiled as one source input while
`-ffunction-sections` and `--gc-sections` discard the unreferenced
`gate_waveform_candidate_run_once()` section.

## Remaining Review Risks

This build-only record still does not prove:

- that this ELF should be flashed;
- reset-time or runtime pin behavior on real hardware;
- that the six candidate driver-input pins are low on a powered board;
- that there is no boot-time transient on real hardware;
- that USB-only DMM readings would be idle-low;
- that any physical waveform is present or absent;
- that dead-time, polarity, break input, gate-driver behavior, or phase-node
  behavior is safe under 24 V;
- that Motor Pilot or Motor Profiler can be opened;
- that a motor can be connected.

Those require later separate gates and direct measurement evidence.

## Next Allowed Checkpoint

The next allowed repository-side checkpoint is only:

```text
neutral-wrapper USB-only neutral-state phase-gate plan or review
```

That next checkpoint must still be planning or review unless a later separate
dated execution-entry explicitly opens USB-only runtime. It must carry forward
this exact ELF SHA256, MAP SHA256, old-main exclusion evidence, and the
discarded-section limitation above.

Still forbidden after this neutral-wrapper build-only record:

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
