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
| GUI 截图 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png`，以及本轮新增的 `screenshots/2026-05-14_cubemx_ioc_launch_attempt.png`、`screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`。 | 首页截图证明 CubeMX 打开；新增截图证明保存的 NUCLEO `.ioc` 可在 CubeMX `Pinout & Configuration` 页面打开。它们仍不证明 MotorControl/Workbench 配置。 |
| GUI 捕获结果 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_result_2026-05-14.md`。 | 记录本轮 GUI fallback 证据、`.ioc` 读回、截图路径和 `.stmcx` / MotorControl 仍阻塞。 |
| Workbench 入口探测 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`。 | 记录 repo、CubeMX 安装目录、MCSDK package、VS Code STM32 extension、`.stm32cubemx` 和常见 ST 安装目录的目标探测；确认 MotorControl package 数据存在，但仍没有 `.stmcx` 或独立 Workbench launcher 证据。 |
| 板级走线证据 | 仓库里只有 `hardware/schematic/2026-05-09_power_board_schematic_screenshot.jpg` 和对应说明。 | 这是截图级线索，不是 CN8 / EDA / netlist 走线证明。 |
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
| `PB3` 作为 Hall B | 只有释放或隔离 SWO 后才是候选。 | `.ioc` 已保存 `PB3.Signal=SYS_JTDO-SWO`。 | 需要板子焊桥/设置证据，以及 Workbench/CubeMX Hall 分配证据。 |
| `DT/MODE` 与 PWM 模式 | 仍是硬件审查依赖项。 | STDRIVE101 digest 已解释为什么它重要。 | 需要 EDA/netlist 证明 `DT/MODE` 是电阻设置还是接地，并让 MCSDK/TIM1 输出模式匹配它。 |
| STDRIVE101 保护路径 | 仍是硬件审查依赖项。 | 本地 STDRIVE101 PDF、文本和 digest 都在。 | 还要证明板子上的 `nFAULT`、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、电源唤醒、VDS 监测网络。 |
| STDRIVE101 保护路径审查文件 | 已建立缺证矩阵。 | `stdrive101_protection_path_review_2026-05-14.md` 按同一格式记录官方要求、截图线索、可信等级、缺失证据和 P2 决策。 | 还要用当前版 EDA/PDF/netlist/高清图把每一项从 blocked 升级为 proven。 |

## 生成 MCSDK 前的硬阻塞

1. 没有 `.stmcx`，也没有 Workbench/CubeMX MotorControl 配置页截图；当前只有 NUCLEO-G474RE CubeMX `.ioc` 草案、CubeMX `Pinout & Configuration` GUI fallback 截图，以及 MotorControl package 数据存在的探测记录。
2. 没有 CN8 / EDA / netlist 走线证明。
3. 没有板级 `DT/MODE`、`nFAULT`、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、standby 和 VDS monitoring 源证据；当前只有保护路径审查缺证矩阵。
4. 没有证据证明 `PB3` 用作 Hall B 之前，SWO 已经释放或隔离。
5. 没有连续性 / 短路检查记录；而上电证据在 P2 阶段仍然禁止。

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

## 当前 P2 判断

P2 可以继续做书面审查和 GUI / 配置证据收集。当前仓库还不能信任生成的
MCSDK 电机控制配置，也不能进入功率板、电机、PWM Gate、Motor Profiler、
Hall 闭环或无感控制阶段。
