# No-Power Build-Only Result - QIANSAI_G474_STDRIVE101_FOC_P2 - 2026-05-27

## 中文结论

本次只完成 `Debug` 本机无功率编译检查：

- 结论：`No-power build-only Debug pass / local toolchain compiles generated project / no firmware runtime or hardware readiness`.
- 这只说明当前 Workbench 生成工程能在本机 STM32Cube bundled CMake / Ninja / GNU Arm GCC 工具链下完成构建检查。
- 这不说明已经烧录、不说明 Hall 闭环可运行、不说明 Gate PWM 安全、不说明功率板或电机可上电。

## Safety Boundary

- No flash.
- No Run / Debug.
- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler.
- No Motor Pilot.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## Input Project

- External Workbench project:
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`
- Build directory:
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2\build\Debug`
- Source evidence already archived in repo:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`

## Command

Working directory:

```powershell
C:\Users\gregrg\Documents\Codex\2026-04-30\qiansai
```

Command:

```powershell
cmake --build "C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2\build\Debug" --config Debug
```

Result:

```text
Exit code: 0
ninja: no work to do.
```

Interpretation:

- CMake build target completed successfully.
- Ninja reported the Debug target was already up to date.
- This is an up-to-date build-only pass, not a clean rebuild record.

## Toolchain Evidence

- `cmake --version`: `4.3.2`
- `CMAKE_MAKE_PROGRAM`:
  `C:/Users/gregrg/AppData/Local/stm32cube/bundles/ninja/1.13.2+st.1/bin/ninja.exe`
- `CMAKE_C_COMPILER`:
  `C:/Users/gregrg/AppData/Local/stm32cube/bundles/gnu-tools-for-stm32/14.3.1+st.2/bin/arm-none-eabi-gcc.exe`
- `CMAKE_C_COMPILER_VERSION`: `14.3.1`

## Artifact Evidence

| Artifact | Size | LastWriteTime | SHA256 |
| --- | ---: | --- | --- |
| `QIANSAI_G474_STDRIVE101_FOC_P2.elf` | `2161388` bytes | `2026-05-27 23:41:05` | `8EF20B93DC069F085AEBD670A77C5C4C4266FE59532A91DF784241CCB062BB23` |
| `QIANSAI_G474_STDRIVE101_FOC_P2.map` | `1484465` bytes | `2026-05-27 23:41:05` | `B571B7C9CF5F262BF49E35BE63B05C128CC59480E546FA36929BD8704CBD132D` |

No `.hex` or `.bin` artifact was recorded in this build result.

## What This Upgrades

Allowed current claim:

```text
The generated Workbench project compiles in the local toolchain under no-power build-only scope.
```

This can be used as build-only configuration evidence for the generated project.

## What This Does Not Upgrade

This result does not prove:

- current PCB2 physical routing;
- `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4` continuity;
- `PB3=LIN1` physical continuity;
- `P14/P15=3V3/GND` physical continuity;
- `nFAULT->PB12` physical continuity;
- STDRIVE101 protection behavior;
- current sensing correctness;
- Gate PWM waveform safety;
- GPIO / EXTI runtime behavior;
- MCSDK Hall integration;
- software Hall closed-loop behavior;
- Motor Profiler readiness;
- motor readiness;
- power-stage readiness;
- sensorless / SMO readiness.

## Carry-Forward Blockers

- PCB2 is still unpopulated, so DMM continuity / short-check evidence remains hardware-side deferred, not passed.
- Current PCB2 Hall route remains software Hall planning only:
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it must not be reused as current Hall.
- Workbench generated TIM2 Hall route remains `PA15/PB3/PB10`, which does not match current PCB2 Hall.
- Future software Hall adapter firmware still needs a separate entry decision, DMM evidence, GPIO/EXTI review, timestamp-source decision, debug-output route, MCSDK integration review, exact hook list, and rollback plan.
