# 2026-05-19 Gerber PCB2 Manufacturing Package Intake

New Gerber package:
`hardware/schematic/2026-05-19_gerber_pcb2_stdrive101/Gerber_PCB2_2026-05-19.zip`.

New Packet B/C no-power review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_003_gerber_pcb2.md`.

Decision: `Partial clue / accepted board-side Gerber + flying-probe net clue`.

The ZIP is a same-day Gerber manufacturing package supplied after the
self-developed STDRIVE101 driver-board `.epro` source. It contains top/bottom
copper, two inner copper layers, solder mask, paste mask, silkscreen, board
outline, drill files, and `FlyingProbeTesting.json`. Gerber headers record
`EasyEDA Pro v3.2.91`, generated `2026-05-19 11:16:57`. The archived ZIP hash
is SHA256 `F61C073C5A9E71CD608460976430D3F927E7AD48EC05A42661E77662AF04CE56`.

Accepted exact board-side clues:

- `CN3` flying-probe pad/net table:
  `1 HIN1`, `2 LIN1`, `3 HIN2`, `4 LIN2`, `5 HIN3`, `6 LIN3`,
  `7 ADC_U`, `8 ADC_V`, `9 ADC_W`, `10 IA`, `11 IB`, `12 IC`,
  `13 NFAULT`, `14 3V3`, `15 GND_SIGNAL`.
- `U1=STDRIVE101` pad nets include `$2N118` for the `CP` pin position,
  `GND_POWER` for the `DT/MODE` pin position, plus `SCREF`, `24V_FUSED`,
  `REG12`, `NFAULT`, `INx`, `ENx`, `BOOTx`, `GHSx`, `GLSx`, and `OUTx`.
- PWM input paths are visible at pad-net level:
  `R4 HIN1-IN1`, `R8 LIN1-EN1`, `R5 HIN2-IN2`, `R6 LIN2-EN2`,
  `R7 HIN3-IN3`, `R9 LIN3-EN3`.
- Protection/current-sense pad-net clues are visible:
  `R3 NFAULT-3V3`, `R1 SCREF-3V3`, `R2 GND_SIGNAL-SCREF`,
  `C4/C5 REG12-GND_SIGNAL`, `D1/D2/D3 REG12-to-BOOTx`,
  and `R12/R14/R17 ADC_U/V/W-GND_POWER`.
- Connector clues are visible:
  `U2=J_HALL` has `+5V`, `GND_SIGNAL`, and three signal paths through
  `R22/R23/R24` to `IA/IB/IC`; `CN2=J_MOTOR` has `OUT1/OUT2/OUT3`.

Blocked exact fields:

- No NUCLEO `CN8` endpoint, STM32 pin mapping, or harness/adapter mapping is
  present in this package.
- Exact fabrication/revision match still needs user or hardware teammate
  confirmation before it can be treated as final build evidence.
- `CP` is present only as unnamed net `$2N118`; `STBY` was not observed.
- `J_HALL` physical pin-1 orientation and Hall A/B/C numbering are not
  accepted.
- PB3/SWO release, Packet A/Workbench selected fields, generated-project
  trust, continuity checks, power-stage readiness, Motor Profiler readiness,
  motor readiness, and sensorless readiness remain unchanged.

# 2026-05-19 ProDoc P1 EDA Pro Source Intake

New self-developed STDRIVE101 driver-board source:
`hardware/schematic/2026-05-19_prodoc_p1_stdrive101_epro/ProDoc_P1_2026-05-19.epro`.

New Packet B/C no-power review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_002_prodoc_p1_epro.md`.

Decision: `Partial clue / accepted schematic-source clue`.

The `.epro` is a readable EDA Pro schematic source for the user-confirmed
self-developed STDRIVE101 driver board. Parsed metadata shows
`STDRIVE101_3Phase_Inverter`, board `Schematic1`, sheet `P1`, create/update
date `2026-05-19`, and create/update time `10:26:36`. The archived file hash
is SHA256 `B9D67B9E5D6DD08D5229928636DFA8048C081DED7EE230ADDB79F20D83D718A1`.

Accepted exact schematic clues:

- `U1=STDRIVE101`.
- `Q1-Q6=NCEP40T11G`.
- `R12/R14/R17=20mOhm` shunt resistors.
- `CN3=2.54mm-15P ZZ` board-side control connector.
- `U2=J_HALL`, `CN2=J_MOTOR`.
- `CN3` board-side pinout:
  `1 HIN1`, `2 LIN1`, `3 HIN2`, `4 LIN2`, `5 HIN3`, `6 LIN3`,
  `7 ADC_U`, `8 ADC_V`, `9 ADC_W`, `10 IA`, `11 IB`, `12 IC`,
  `13 NFAULT`, `14 3V3`, `15 GND_SIGNAL`.
- `J_HALL` schematic clue: `+5V`, `GND_SIGNAL`, and three signal paths
  through `R22/R23/R24=100 ohm` into `IA/IB/IC`.
- STDRIVE101 schematic clues: `NFAULT`, `REG12`, `SCREF`, `BOOTx`, `OUTx`,
  `GHSx`, and `GLSx` are visible. `DT/MODE` appears tied to `GND_POWER` at
  the STDRIVE101 pin, but this remains a clue pending dedicated review.

Blocked exact fields:

- The archive contains no PCB layout data: `project.json` has `pcbs: {}`, the
  board entry has an empty `pcb` field, and `PCB/` is only an empty directory
  entry.
- No NUCLEO `CN8` endpoint or STM32 pin mapping is proven.
- `CP` has no explicit parsed net label, `STBY` was not observed, and the
  protection thresholds/fault-release path still need review.
- PB3/SWO release, `J_HALL` numbering, Hall readiness, power-stage readiness,
  Packet A/Workbench selected fields, generated-project trust, Motor Profiler
  readiness, motor readiness, and sensorless readiness remain unchanged.

# 2026-05-19 Packet A Workbench Capture Attempt

New Packet A no-power capture-attempt review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_001_packet_a_workbench_capture_attempt.md`.

New Workbench screenshots:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_launch_fullscreen.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_after_new_project.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_motor_control_kit_selected.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_board_path_probe.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_power_slot_search_stdrive101_exact.png`

Decision: `Partial clue / stopped`.

Accepted exact clue: Workbench 6.4.2 Desktop launches, and the component path
can show `NUCLEO-G474RE` / `STM32G474RETx` as the control-board context.

Blocked exact fields: no project-specific `.stwb6`, no accepted Custom /
Generic self-made STDRIVE101 power-stage context, and no selected-field
screenshots for PWM, current sensing, Hall/sensorless, driver protection, or
pin usage. User clarified on 2026-05-19 that the project uses a self-developed
motor driver board based on the STDRIVE101 chip, so built-in ST board entries
such as `EVALSTDRIVE101` or `STEVAL-LVLP01` cannot be used as board-match
substitutes.

Packet A remains `Partial clue / Preparation only`. Generated-project trust
remains `Not allowed`. Packet B/C, CN8 routing, STDRIVE101 protection-path
proof, PB3/SWO release, `J_HALL`, Hall readiness, power-stage readiness, Motor
Profiler readiness, motor readiness, and sensorless readiness remain unchanged.

# 2026-05-18 PB3 / SWO CubeMX Probe

New PB3/SWO no-power review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-18_002_pb3_swo_probe.md`.

New evidence files:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-18_cubemx_pb3_current_swo_fullscreen.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/pb3_tim2_ch2_probe_2026-05-18.ioc`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-18_cubemx_pb3_tim2_ch2_probe_fullscreen.png`

Decision: `Partial clue`.

The existing NUCLEO-G474RE no-power draft still records
`PB3.GPIO_Label=T_SWO` and `PB3.Signal=SYS_JTDO-SWO`; the new CubeMX screenshot
preserves that current state. A separate dated probe `.ioc` changes only the
copy to `PB3.GPIO_Label=HALL_B_PROBE` and `PB3.Signal=TIM2_CH2`, and CubeMX can
open that probe. This is a configuration-layer clue only. It does not prove
NUCLEO SWO release / isolation, Workbench Hall B selection, CN8 / `J_HALL`
endpoint mapping, Hall readiness, or any powered behavior.

`PB3` remains blocked for Hall B until separate SWO release / isolation evidence
and board-route endpoint evidence arrive. Packet A/B/C, generated-project
trust, CN8 routing, STDRIVE101 protection-path proof, Hall closed-loop,
power-stage readiness, Motor Profiler readiness, motor readiness, and sensorless
readiness are unchanged.

# 2026-05-17 Vendor Motor And G431 Pin Table Update

New motor source:
`hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.md`.

New hardware teammate pin-table source:
`hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.md`.

New MCU pin compatibility check:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/mcu_pin_compatibility_check_2026-05-17.md`.

Review record:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`.

Decision: `Partial clue`.

The supplier motor table supports a better no-power Workbench label,
`57BLF01_VENDOR_CANDIDATE`, but it does not provide project-measured motor
parameters or Motor Profiler data. The hardware teammate pin table is titled
for `STM32G431RB`; the teammate states the relevant G431/G474 pins are the
same, and local MCSDK `STM32G431RBTx` / `STM32G474RETx` asset comparison
supports the compared key rows. This still does not accept CN8 routing,
`J_HALL` connector numbering, `PB3` / SWO release, or OPAMP/VCP policy.

Generated-project trust remains `Not allowed`.

# 2026-05-16 Packet A Custom Capture Package Update

The old `My_First_FOC.stwb6` file is now explicitly treated as a legacy
toolchain-learning leftover, not the intended project-specific Packet A source.
Its arbitrary `EVALSTDRIVE101` power-board choice remains a reason it cannot be
accepted for the custom board.

New package:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`.

New preparation review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`.

Decision: `Partial clue / Preparation only`.

The package defines the next no-power Workbench capture path for
`NUCLEO-G474RE` / `STM32G474RETx`, a Custom / Generic STDRIVE101 power stage,
FOC, Hall fallback, 3-shunt current sensing, `57BLF01_VENDOR_CANDIDATE`
supplier-clue motor label, a
no-power motor measurement log, and a pin assignment table. It still does not
contain a real new `.stwb6` or selected-field Workbench screenshot.

Generated-project trust remains `Not allowed`.

# 2026-05-15 Packet A STWB6 Candidate Update

Codex found the real ST MC Workbench 6.4.2 launcher at
`F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\STMCWB.exe` and preserved
`F:\STMCSDK\My_First_FOC.stwb6` under
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`.

Review record:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`.

Decision: `Partial clue`.

Accepted from the file: MCSDK 6 `.stwb6` project format, Workbench version
`6.4.2`, algorithm `FOC`, control board `NUCLEO-G474RE`, and MCU
`STM32G474RETx`.

Still not accepted: final custom-board context, selected TIM1 complementary PWM
topology, final `NFAULT` / `PB12/TIM1_BKIN` selection, custom-board current
sensing, Hall/sensorless final selection, `PA2/PA3` policy, `PB3` ownership,
and generated-project trust.

Current decision: Packet A has a source candidate, but generated-project trust
remains `Not allowed`.

# P2 证据包 - 2026-05-14

这个文件记录当前仓库里“真的有证据”的内容。它的作用不是教你接线，
也不是生成固件，而是帮你判断：哪些东西现在可以相信，哪些还只是草案，
哪些会卡住后续 MCSDK 工程。

## 安全边界

这个证据包不授权任何上电或电机动作：

- 不接 24V；
- 不接功率板；
- 不接电机；
- 不输出 Gate PWM；
- 不运行 Motor Profiler；
- 不声称 Hall 闭环已经验证；
- 不声称 SMO / 无感控制已经验证。

## 当前仓库里有什么

| 检查项 | 当前结果 | 这说明什么 |
| --- | --- | --- |
| `.stmcx` 文件 | `rg --files -g "*.stmcx"` 在 GUI 尝试前后都没有找到任何文件。 | 还没有 Motor Control Workbench 工程文件。 |
| CubeMX `.ioc` 草案 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`。 | 证明 NUCLEO-G474RE 板卡入口、`PB12/TIM1_BKIN`、`PB14/TIM1_CH2N`、`PA2/PA3` VCP、`PB3` SWO 已保存到 CubeMX 配置层；仍不是 `.stmcx` 或 MCSDK MotorControl 工程。 |
| GUI 截图 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png`，`screenshots/2026-05-14_cubemx_ioc_launch_attempt.png`、`screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`，以及 2026-05-18 `screenshots/2026-05-18_cubemx_pb3_current_swo_fullscreen.png` 和 `screenshots/2026-05-18_cubemx_pb3_tim2_ch2_probe_fullscreen.png`。 | 首页截图证明 CubeMX 打开；2026-05-14 截图证明保存的 NUCLEO `.ioc` 可在 CubeMX `Pinout & Configuration` 页面打开；2026-05-18 截图证明当前草案仍显示 `PB3` 为 SWO，另一个 probe 副本可显示 `PB3` 为 `HALL_B_PROBE`。它们仍不证明 MotorControl/Workbench 配置、SWO 物理释放或 Hall endpoint。 |
| PB3/SWO probe | `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/pb3_tim2_ch2_probe_2026-05-18.ioc`。 | 这是从原 `.ioc` 复制出的配置层 probe，只把 `PB3` 改为 `TIM2_CH2` / `HALL_B_PROBE` 并由 CubeMX 打开截图；它不替代原草案，也不证明 NUCLEO SWO 释放、CN8 / `J_HALL` endpoint 或 Hall readiness。 |
| GUI 捕获结果 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_result_2026-05-14.md`。 | 记录本轮 GUI fallback 证据、`.ioc` 读回、截图路径和 `.stmcx` / MotorControl 仍阻塞。 |
| Workbench 入口探测 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`。 | 记录 repo、CubeMX 安装目录、MCSDK package、VS Code STM32 extension、`.stm32cubemx` 和常见 ST 安装目录的目标探测；确认 MotorControl package 数据存在，但仍没有 `.stmcx` 或独立 Workbench launcher 证据。 |
| 板级走线证据 | 仓库里有 `hardware/schematic/2026-05-09_power_board_schematic_screenshot.jpg`、对应说明，以及 2026-05-15 新导入的 `hardware/schematic/2026-05-15_power_board_cn8_stdrive101_schematic_candidate.png` / `.md`。 | 2026-05-15 截图可读性更好，用户已确认它对应当前物理功率板且由硬件同学自绘，能作为 Packet B/C 候选和 `Partial clue`；但缺正式 source revision/date、STM32 端点映射、`DT/MODE` 端点证明和 `STBY` 证明，所以仍不是 accepted CN8 / EDA / netlist 走线证明。 |
| STDRIVE101 资料 | 本地已有 STDRIVE101 PDF、提取文本和 digest。 | 可以用来做保护路径审查，但还不能证明你的功率板实际怎么连。 |
| STDRIVE101 保护路径审查 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`。 | 已把 `DT/MODE`、`nFAULT`、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、standby 和 VDS monitoring 固化成缺证矩阵；这仍只是审查规则，不是板级通过证据。 |

## 证据等级

| 等级 | 需要什么证据 | 当前状态 | 当前决定 |
| --- | --- | --- | --- |
| A | Workbench/CubeMX 的 `.stmcx`、配置截图或可读 `.ioc`，能看到 `STM32G474RETx`、`PB12/TIM1_BKIN`、`PB14/TIM1_CH2N`、`PA2/PA3` 没被偷偷复用、`PB3` Hall/SWO 选择。 | 部分具备：已有 NUCLEO-G474RE `.ioc` 草案和 CubeMX `Pinout & Configuration` 截图，仍没有 `.stmcx` 或 MCSDK/Workbench MotorControl 配置截图。 | 可相信 CubeMX 引脚配置草案已保存并可由 GUI 打开；不能信任“MCSDK MotorControl 配置已经完成”。 |
| B | NUCLEO 连接器和焊桥证据，说明 VCP/SWO 到底占不占对应引脚。 | `.ioc` 已保存 `PA2/PA3` 为 VCP、`PB3` 为 SWO；本地有 UM2505 手册，但还没有当前板子 SWO 释放记录。 | `PB3` 只能当 Hall B 候选，不能说已经可用。 |
| C | CN8 / EDA / netlist 走线证据，证明 `NFAULT`、PWM 输入、电流采样、Hall、`3V3`、`GND_SIGNAL` 实际连到哪里。 | 缺失。现在只有原理图截图，没有 EDA、PDF、PCB、Gerber 或 netlist。 | 不能信任 STM32 引脚真的连到了目标 STDRIVE101 网络。 |
| D | 无功率连续性 / 短路检查记录。 | 缺失。 | P2 书面审查阶段不做这一步；后续硬件阶段前必须补。 |
| E | 限流上电日志、波形和测量记录。 | 缺失，而且 P2 禁止做。 | 不能有功率、电机、PWM Gate、Profiler、Hall、SMO 结论。 |

## 关键点逐项结论

| 项目 | 当前草案怎么选 | 现在有什么证据 | 信任前还缺什么 |
| --- | --- | --- | --- |
| `PB12/TIM1_BKIN` 作为 `nFAULT` | 当前首选候选。 | pin/config review 和 config draft 已记录这个选择；`mcsdk_no_power_nucleo_g474re_draft.ioc` 已保存 `PB12.Signal=TIM1_BKIN`。 | CN8/EDA/netlist 必须证明 STDRIVE101 `nFAULT` 真的到这个 STM32 输入；还要确认上拉电压和低有效含义。 |
| `PC5` 作为 `nFAULT` | 当前草案拒绝。 | `config_draft.md` 和 `pin_config_review_2026-05-14.md` 已记录拒绝理由。 | 只有写清楚 OPAMP/VCP/定时器 break/走线冲突怎么解决，才允许重新打开。 |
| `PB14/TIM1_CH2N` 作为 V 相低侧 PWM | 当前优先于 `PA12`。 | 草案已记录这个策略；`mcsdk_no_power_nucleo_g474re_draft.ioc` 已保存 `PB14.Signal=TIM1_CH2N`。 | CN8/EDA/netlist 必须证明它连到目标 STDRIVE101 输入。 |
| `PA2/PA3` 作为 FOC 通信口 | 默认排除。 | `.ioc` 已保存 `PA2.Signal=LPUART1_TX`、`PA3.Signal=LPUART1_RX`，证明这是 NUCLEO VCP 路径。 | 如果以后要复用，必须由 CubeMX/Workbench 证明不会和 OPAMP/PGA 冲突。 |
| `PB3` 作为 Hall B | 只有释放或隔离 SWO 后才是候选。 | 原 `.ioc` 已保存 `PB3.Signal=SYS_JTDO-SWO`，2026-05-18 当前状态截图仍显示 `PB3` 为 `T_SWO`；probe 副本可在 CubeMX 中显示 `PB3` 为 `TIM2_CH2` / `HALL_B_PROBE`。 | 仍需要 NUCLEO SWO 释放/隔离证据、Workbench/CubeMX Hall B 分配证据，以及 CN8 / `J_HALL` board-route endpoint。 |
| `DT/MODE` 与 PWM 模式 | 仍是硬件审查依赖项。 | STDRIVE101 digest 已解释为什么它重要。 | 需要 EDA/netlist 证明 `DT/MODE` 是电阻设置还是接地，并让 MCSDK/TIM1 输出模式匹配它。 |
| STDRIVE101 保护路径 | 仍是硬件审查依赖项。 | 本地 STDRIVE101 PDF、文本和 digest 都在。 | 还要证明板子上的 `nFAULT`、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、电源唤醒、VDS 监测网络。 |
| STDRIVE101 保护路径审查文件 | 已建立缺证矩阵。 | `stdrive101_protection_path_review_2026-05-14.md` 按同一格式记录官方要求、截图线索、可信等级、缺失证据和 P2 决策。 | 还要用当前版 EDA/PDF/netlist/高清图把每一项从 blocked 升级为 proven。 |

## 生成 MCSDK 前的硬阻塞

1. 没有 `.stmcx`，也没有 Workbench/CubeMX MotorControl 配置页截图；当前只有 NUCLEO-G474RE CubeMX `.ioc` 草案、CubeMX `Pinout & Configuration` GUI fallback 截图，以及 MotorControl package 数据存在的探测记录。
2. 没有 CN8 / EDA / netlist 走线证明。
3. 没有板级 `DT/MODE`、`nFAULT`、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、standby 和 VDS monitoring 源证据；当前只有保护路径审查缺证矩阵。
4. 没有证据证明 `PB3` 用作 Hall B 之前，SWO 已经释放或隔离；2026-05-18 probe 只证明配置层可显示 `TIM2_CH2` / `HALL_B_PROBE`，不清除该阻塞。
5. 没有连续性 / 短路检查记录；而上电证据在 P2 阶段仍然禁止。

## 下一步证据入口

新增入口规则：
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_intake_checklist_2026-05-14.md`。

这个清单只规定什么来源可以进入证据审查，不升级任何当前缺证项。

用户动作队列：
`apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md`。

这个队列把下一步交付顺序固定为：先交 Packet B 当前版 CN8 / board-route /
STDRIVE101 源包；再交 Packet A MCSDK / MotorControl 配置源包；如果继续
使用 `PB3` 做 Hall B，再补 SWO 释放或隔离证据。它仍不升级任何当前缺证项。

审查模板：
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_template_2026-05-14.md`。

这个模板规定收到源包后先做 Accept / Partial clue / Reject 判断，再决定
是否更新本证据包。未被模板接受的字段继续保持 `Blocked`。

| 缺证项 | 需要走的入口 | 当前状态 |
| --- | --- | --- |
| `.stwb6` / `.stmcx` / MotorControl 配置截图 | MCSDK / MotorControl Configuration Packet | Partial clue. `My_First_FOC.stwb6` is preserved and reviewed, but final selected fields and custom-board context remain unaccepted. |
| CN8 / EDA / netlist 走线证明 | CN8 / Board Route Packet | Blocked. 仍没有 current-version EDA、schematic PDF、netlist 或高清走线图。 |
| STDRIVE101 `DT/MODE`、`nFAULT`、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、standby 和 VDS monitoring | STDRIVE101 Protection Path Packet | Blocked. 仍只有官方器件要求和缺证矩阵，没有板级通过证据。 |
| `PB3` Hall B 前的 SWO 释放或隔离 | CN8 / Board Route Packet plus NUCLEO bridge/source evidence | `Partial clue / still Blocked`. 原 `.ioc` 仍显示 `PB3.Signal=SYS_JTDO-SWO`；2026-05-18 probe 副本可显示 `PB3.Signal=TIM2_CH2`，但缺 SWO release/isolation 和 Hall endpoint 证明。 |

2026-05-15 新增源包审查：
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_001_cn8_stdrive101_schematic_candidate.md`。

当前判定为 `Partial clue`。用户已确认该截图对应当前物理功率板，来源/版本
口径为硬件同学自绘。该截图可见 CN8、STDRIVE101、输入电阻、
`nFAULT` 上拉/LED、`REG12`、`CP`、`SCREF`、bootstrap、MOSFET、采样电阻和
Hall 接口线索；但仍没有正式 source revision/date、STM32 端点映射、
accepted `DT/MODE` 端点证明或 `STBY` 证明。因此本证据包不升级 CN8
routing proof 或 STDRIVE101 protection-path proof。

Rejected source types stay rejected: low-resolution screenshots, oral
descriptions, old or unknown-version files, incomplete crops, generated source
without matching configuration evidence, and the excluded WeChat-side
`netlist_PADS.net` candidate.

## 2026-05-14 Parallel Evidence Push

| Evidence chain | Follow-up result | Current trust level |
| --- | --- | --- |
| `.stmcx` / MotorControl | Repo search still found no `.stmcx`. Narrow checks of `F:\STMCubeMX`, `MCSDK_v6.4.2-Full`, and VS Code extension folders did not identify a saved Workbench project, standalone Workbench launcher, or MotorControl configuration page. | Blocked. MotorControl package presence is not project configuration evidence. |
| CN8 / STDRIVE101 route | `cn8_stdrive101_route_review_2026-05-14.md` now defines the accepted source packet. Current repo evidence is still only screenshot-level clue plus STDRIVE101 datasheet review requirements. | Blocked. No accepted current EDA, schematic PDF, netlist, or high-resolution route crop is in the repo. |
| Excluded source | The WeChat-side `netlist_PADS.net` candidate is intentionally not imported and not used as current board evidence. | Not evidence. |

## 2026-05-14 STDRIVE101 Protection Path Review

| Evidence chain | Follow-up result | Current trust level |
| --- | --- | --- |
| ST official source | ST official product page and datasheet were rechecked. They confirm two input strategies selected by `DT/MODE`, `REG12` gate-driver supply, overcurrent comparator, VDS monitoring, UVLO, thermal shutdown, and standby behavior. | High for official device requirements. |
| Board screenshot clue | Existing screenshot notes mention possible `R3`/`nFAULT`, `C4`/`C5` for `REG12`, `C1` for `CP`, `R1`/`R2` for `SCREF`, and bootstrap components, but resolution/source type is not accepted board proof. | Low-grade clue only. |
| Protection-path review | `stdrive101_protection_path_review_2026-05-14.md` now records a missing-evidence matrix for `DT/MODE`, `nFAULT`, `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, `STBY`, and VDS monitoring. | High for review structure and blockers; blocked for board-level proof. |

Current decision: P2 can continue written review and GUI/config capture work,
but it still cannot claim saved MCSDK MotorControl configuration, CN8 routing
proof, STDRIVE101 protection-path proof, power-stage readiness, Hall readiness,
or sensorless readiness.

## 2026-05-15 Packet A Local Probe

New Packet A records:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_local_probe_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_checklist_2026-05-15.md`

The local probe checked the repo, existing screenshots, the
`apps/stm32_g474_foc/MotorControl` placeholder, `F:\STMCubeMX`,
`C:\Users\gregrg\STM32Cube\Repository`, `C:\Users\gregrg\.stm32cubemx`, and
common user locations (`Documents`, `Downloads`, `Desktop`). It still found no
real `.stmcx` and no MotorControl / Workbench configuration screenshot. Direct
search of `C:\Users\gregrg` returned access denied, so this is a bounded local
probe, not proof that every private user directory was searched.

Packet A was later upgraded to `Partial clue` by
`source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`. The new checklist
defines the next accepted capture: Workbench screenshots or an accepted final
`.stwb6` / legacy `.stmcx` proving the selected fields.
It does not upgrade MCSDK MotorControl configuration, generated-project trust,
Gate PWM, Motor Profiler, Hall, motor, power-stage, CN8 routing, STDRIVE101
protection-path, or sensorless evidence.

## 2026-05-15 STM32 Signal Contract And Build-Only Gate

New non-hardware track artifacts:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/stm32_side_signal_contract_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/future_build_only_gate_2026-05-15.md`

The STM32-side signal contract records future responsibilities for TIM1 PWM
commands, `NFAULT`, `STBY`, `DT/MODE`, current sensing, Hall fallback,
`PA2/PA3`, `PB3`, `3V3`, `GND_SIGNAL`, and the ESP32 gateway boundary. Every
hardware-dependent field remains `Blocked`, `Candidate`, or `Partial clue`
unless Packet A/B/C or PB3/SWO evidence proves it.

The future build-only gate records that generated-project trust is currently
`Not allowed` because Packet A is only `Partial clue`. If Packet A selected
fields are later accepted, a generated MCSDK project can be treated only as no-power build evidence. Build
success will not upgrade CN8 routing, STDRIVE101 protection-path proof, Gate
PWM behavior, Motor Profiler readiness, Hall readiness, motor readiness, or
sensorless readiness.

## 2026-05-15 P2 Readiness Snapshot

New readiness control artifact:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`

The snapshot consolidates Packet A/B/C, PB3/SWO, STM32-side signal-contract,
and future build-only gate status into one current gate decision. Current
decision remains: P2 is in progress, Packet A is `Partial clue`, generated-project
trust is `Not allowed`, Packet B/C and PB3/SWO remain blocked or partial clue
only, and P3 powered or motor work is not allowed.

This snapshot does not upgrade MCSDK MotorControl configuration, generated
project trust, CN8 routing proof, STDRIVE101 protection-path proof, Gate PWM,
Motor Profiler, Hall, motor, power-stage, or sensorless evidence.

## 当前 P2 判断

P2 可以继续做书面审查、GUI / 配置证据收集和非硬件并行准备。2026-05-15
新增 `non_hardware_parallel_track_2026-05-15.md`，把“暂时跳过硬件源包支线”
记录为 scheduling decision, not clearance。当前仓库还不能信任生成的 MCSDK
电机控制配置，也不能进入功率板、电机、PWM Gate、Motor Profiler、Hall 闭环
或无感控制阶段。
