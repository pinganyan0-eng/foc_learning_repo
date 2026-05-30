# 2026-05-19 Packet A Source Review 005 - MY_FOC Generated Project

## Decision

`Partial clue / generated project quarantined / Packet A not accepted`.

The user-created Workbench project at
`C:\Users\gregrg\.st_workbench\projects\MY_FOC` is useful evidence that
Workbench 6.4.2 can create and generate a `MY_FOC` project on this machine.
It is not accepted as Packet A configuration evidence for the current project.

No generated-project trust is added by this review.
Stable phrase: no generated-project trust.

## User-Facing Note

你说“引脚不一致可以改”，这个我已经按后续可修改项处理，不把引脚差异写成死路。

但当前 `MY_FOC` 还不能直接继续编译、烧录或上电，主要原因是它现在是
`SIX_STEP` 六步控制，不是 FOC；并且 current sensing、fault input、Hall/PWM
和当前 PCB2 或后续改线方案还没有形成可审查的 Packet A 证据。

下一次如果你继续在 Workbench 里改，先做这四件事：

1. 控制方式改成 FOC / field-oriented control，不要 `SIX_STEP`。
2. 功率板路径仍然按 self-developed STDRIVE101 board 处理，不要把内置
   `EVALSTDRIVE101`、`STEVAL-LVLP01`、`EVLDRIVE101-HPD` 当成项目板替代。
3. 如果确定可以改线或飞线，就把 Hall/PWM 改到 Workbench/MCSDK 能表达的
   timer-compatible route；如果不改线，就继续走 `PA0/PA1/PB4` software Hall
   设计审查。
4. 只保存配置和截图给 Codex 审查；不要 Build、Flash、Motor Profiler、24V、
   功率板连接、电机连接或 Gate PWM 输出。

## Archived Source

Selected configuration and generation-log files were copied into:

`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-19_my_foc_generated_project/`

The generated `Src/`, `Inc/`, `Drivers/`, and `MCSDK_v6.4.2-Full/` trees were
not copied into the repo. They remain an external generated artifact and are
not trusted for build-only work.

| File | SHA256 |
| --- | --- |
| `MY_FOC.wbdef` | `2A8D3DFA679689B83D411DA15226B5B1CFC67082A9E3182DFFBB6DAB95AC5FBC` |
| `MY_FOC.ioc` | `CB39C6E2DED8CEBC74946124C5B30F9E497D3B9B21F6B79D415710681B71D1D5` |
| `MY_FOC.ioc.wb` | `10026584D89108B5ABBB16E47A0F685C054C862CC8D91801654BDE7E012E9EF5` |
| `MY_FOC.settings` | `CE6D4684D614531DD1DA55D7AC988A7267138C71E24F8117ED92F0ACFF2B2BFA` |
| `MY_FOC.log` | `14AE75E40B843E8D5C8C9513A620C2B62298DBE4E20389617A530CEA527F1E83` |
| `CMakeLists.txt` | `591179BA21FC8C508A995DEDC28AB96C9089E56D59018F5ACF560CBD55DF0EDF` |
| `CMakePresets.json` | `5CFD04CB98883899A9E70BB39DC70F74EE610B88AE34625DAFAC65F18F322A94` |
| `MY_FOC.original_2026-05-19.stwb6` | `062B78AD8E07B5A29A68A007797200FCD4833FE9D3371D2821F3A54D5B9429FD` |
| `MY_FOC.codex_foc_candidate_2026-05-19.stwb6` | `81C34DA89DF40980A64964ECB55C05707FDECDC6720274DA97E6F292B4A26F63` |

## Accepted Clues

- Workbench generated `MY_FOC.ioc`, `MY_FOC.wbdef`, CMake files, and motor
  control source files on 2026-05-19.
- `MY_FOC.log` records `MC Workbench : 6.4.2`.
- MCU/control-board context is `NUCLEO-G474RE`, `STM32G474RETx`, and
  `STM32G474RE`.
- Power-board naming includes `M1_POWERBOARD_NAME=~MY-STDRIVE101_POWER_BOARD`
  and `M1_PWM_DRIVER_PN=STDRIVE101`.
- Hall sensor selection is enabled in the generated configuration.

These are configuration clues only. They do not accept Packet A.

## Blocking Findings

- The project is configured as `MotorControl.DRIVE_TYPE=SIX_STEP` and
  `MotorControl.M1_DRIVE_TYPE=SIX_STEP`, not FOC.
- Generated source filenames confirm the six-step path:
  `mc_tasks_sixstep.c`, `pwmc_sixstep.c`, and `speed_duty_ctrl.c`.
- Current sensing is disabled: `M1_CUR_READING=false` and
  `M1_CURRENT_MONITOR_READING=false`.
- Bus-voltage reading is disabled: `M1_BUS_VOLTAGE_READING=false`.
- Fault/break is disabled: `TIM1.BreakState=TIM_BREAK_DISABLE`,
  `TIM1.Break2State=TIM_BREAK2_DISABLE`, and both break sources are disabled.
- Generated Hall is on `PA15/PB3/PB10` through TIM2, while current PCB2 Hall is
  recorded as `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`.
- Generated PWM is `PA8/PB13/PA9/PB14/PA10/PB15`, while current PCB2 PWM /
  driver-input route is recorded as
  `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10`.
- The user states the pins can be changed. This makes the mismatch a future
  hardware/adapter or Workbench edit path, not a permanent rejection. It still
  needs a new reviewable Workbench configuration and a matching physical route
  before Packet A can be accepted.
- Motor entry is `R57BLB50L2` with `MOONS motor for Zest Demo`; it is not the
  project `57BLF01_VENDOR_CANDIDATE` evidence.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Motor Pilot.
- No flash.
- No build-only generated project from this source.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## Result

Packet A not accepted.

This packet is useful because it proves a concrete Workbench project now exists
and shows which settings must be corrected next. It is not usable to claim FOC
configuration completion, build-only clearance, generated-project trust, No
Gate PWM output readiness, Motor Profiler readiness, Hall readiness, motor readiness,
power-stage readiness, or sensorless readiness.

## Later Manual Edit And Rollback On 2026-05-19

After the user asked Codex to modify the project, Codex found the source
Workbench project:

`C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6`

Codex created a backup and tried changing only the top-level source setting
from `"algorithm": "sixStep"` to `"algorithm": "FOC"`.

The user then opened Workbench and reported:

`一般错误 / 无法加载文件: C:/Users/gregrg/.st_workbench/projects/MY_FOC.stwb6`

Codex restored the external `MY_FOC.stwb6` from the backup. The current
external source file again reads `"algorithm": "sixStep"` and matches the
backup hash.

Edit / rollback record:

`my_foc_foc_candidate_edit_2026-05-19.md`

This proves the one-field manual `.stwb6` edit is not a valid FOC conversion
path. Packet A remains not accepted and no generated-project trust is added.
