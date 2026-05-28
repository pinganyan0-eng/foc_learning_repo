# Source Packet Review - 2026-05-27 - QIANSAI G474 STDRIVE101 FOC P2 Full Src/Inc Snapshot

Decision:
`Full generated Src/Inc snapshot archived / source interface evidence available for read-only review / no firmware implementation / no MCSDK hook / no Hall readiness`.

## 中文结论

你说得对：Workbench 工程之前确实已经生成在
`C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`。

需要修正的是证据状态：之前仓库里只有部分归档和日志线索，没有把完整
`Src/`、`Inc/`、`cmake/` 和顶层工程文件作为一个可复核 snapshot 登记。本轮已补齐。

这一步让“软件 Hall -> MCSDK hook 前需要的源文件”从“缺完整源文件”推进到
“完整生成源文件已归档，可做只读接口审查”。它仍然不是 hook，不是固件实现，不是 build 结果，不是 Hall 闭环。

## Snapshot

- External source path:
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`
- Repository snapshot:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`
- Manifest:
  `packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/SOURCE_MANIFEST_2026-05-27.md`
- Hash list:
  `packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/SHA256SUMS.txt`

Copied scope:

- `Src/`: 30 files.
- `Inc/`: 28 files.
- `cmake/`: 3 files.
- Top-level project/build metadata: 11 files.

No external Workbench project file was modified.

## Required Hook-Evidence File Check

| Evidence item | Snapshot status | Review note |
| --- | --- | --- |
| `hall_speed_pos_fdbk.c/.h` | Present | Exact generated Hall feedback source is now available for read-only review. |
| Speed / position feedback interface | Partially present through `SpeednPosFdbk_Handle_t` use in generated headers/source | Still needs interface-level review before any adapter proposal. |
| `speed_torq_ctrl.c/.h` | Present | Shows speed-loop ownership and sensor pointer use. |
| `mc_tasks.c`, `mc_tasks.h`, `mc_tasks_foc.c` | Present | Shows generated task timing and FOC feedback consumption. |
| `mc_interface.c/.h`, `mc_api.c/.h` | Present | Shows public/control API boundary. |
| `mc_config.c/.h`, `mc_config_common.c/.h` | Present | Shows generated object wiring and ownership. |
| `mc_parameters.c/.h`, `parameters_conversion.h` | Present | Shows generated scaling/constants and selected Hall/PWM route. |
| `motorcontrol.c/.h`, `mc_type.h` | Present | Shows public motor-control types and entry points. |
| `mc_app_hooks.c/.h` | Present | Hook file exists, but it is not accepted as a software Hall hook without call-timing and ownership review. |
| Interrupt sources such as `stm32g4xx_it.c/.h` | Present | `stm32g4xx_mc_it.c` is also present and records MCSDK motor-control interrupt handling. |
| `pwm_curr_fdbk.c/.h` | Present | Read-only only; software Hall must not alter current feedback or PWM timing. |
| Register / ASPEP files | Present except no generated `Inc/usart_aspep_driver.h` | `register_interface.h`, `mc_configuration_registers.c/.h`, `usart_aspep_driver.c`, `aspep.c/.h` are present. |
| Build metadata | Present | `CMakeLists.txt`, `CMakePresets.json`, `cmake/`, `.ioc`, `.log`, `.wbdef`, `.mxproject`, `.settings`, linker script, and startup file are archived. |

## Static Findings

The snapshot confirms the generated MCSDK standard Hall path.
In short: generated MCSDK Hall remains TIM2.

- `QIANSAI_G474_STDRIVE101_FOC_P2.ioc` contains
  `MotorControl.M1_SPEED_SENSOR=HALL_SENSOR`.
- `QIANSAI_G474_STDRIVE101_FOC_P2.ioc` contains
  `MotorControl.M1_HALL_TIMER_SELECTION=HALL_TIM2`.
- `Inc/main.h` maps generated Hall pins as `PA15`, `PB3`, and `PB10`.
- `Src/stm32g4xx_hal_msp.c` maps `PA15 -> TIM2_CH1`,
  `PB3 -> TIM2_CH2`, and `PB10 -> TIM2_CH3`.
- `Src/mc_config.c` defines `HALL_M1` with `.TIMx = TIM2`.
- `Src/stm32g4xx_mc_it.c` routes `SPD_HALL_TIM_M1_IRQHandler` to
  `HALL_TIMx_UP_IRQHandler(&HALL_M1)` and
  `HALL_TIMx_CC_IRQHandler(&HALL_M1)`.

The snapshot also confirms why current PCB2 software Hall still cannot be
claimed as MCSDK Hall:

- Current PCB2 route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- Current PCB2 constraint remains `PB3=LIN1`, not Hall.
- Generated Workbench route still uses standard TIM2 Hall on
  `PA15/PB3/PB10`.
- `PA0/PA1/PB4` software Hall is not represented as a generated MCSDK Hall
  route in this snapshot.

## Interface Clues For Future Review

- `Src/mc_tasks_foc.c` calls `HALL_Init(&HALL_M1)`.
- `Src/mc_tasks_foc.c` initializes speed control with
  `STC_Init(..., &HALL_M1._Super)`.
- `Src/mc_tasks_foc.c` calls `HALL_CalcAvrgMecSpeedUnit(&HALL_M1, ...)`,
  `SPD_Check((SpeednPosFdbk_Handle_t *)&HALL_M1)`, and
  `HALL_CalcElAngle(&HALL_M1)`.
- `Src/mc_tasks_foc.c` later consumes angle through `SPD_GetElAngle(...)`
  before Park / reverse Park operations.
- `Src/speed_torq_ctrl.c` exposes `STC_SetSpeedSensor(...)`, but this is only
  an interface clue, not an approved hook.
- `Src/aspep.c`, `Src/usart_aspep_driver.c`, and `Inc/register_interface.h`
  show ASPEP / MCP / UART ownership; they are not free debug channels for the
  future software Hall adapter.

## Decision Impact

This review upgrades only one thing:

- Exact generated `Src/` / `Inc` source evidence is now available in the repo
  for no-power read-only interface review.

This review does not upgrade:

- software Hall adapter implementation;
- MCSDK hook implementation;
- generated-code edit permission;
- no-power build success;
- GPIO/EXTI runtime proof;
- DMM continuity / short-check proof;
- Hall closed-loop readiness;
- Gate PWM safety;
- motor readiness;
- power-stage readiness;
- sensorless / SMO readiness.

## Next Allowed No-Power Step

Allowed next Codex-side step:

- create a read-only MCSDK speed / position feedback interface review from the
  archived exact source files.

Still not allowed:

- editing generated MCSDK files;
- writing software Hall code into the generated project;
- building or flashing as proof of hardware safety;
- connecting 24V, power board, or motor;
- outputting Gate PWM;
- running Motor Profiler or Motor Pilot.

## Safety Boundary

- No flash.
- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Motor Pilot run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
