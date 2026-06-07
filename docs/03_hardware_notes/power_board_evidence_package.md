# power_board_evidence_package

本文件是自研 STDRIVE101 功率板首次限流上电前的证据包清单。它只说明资料和证据是否齐备，不授权上电、不授权输出 PWM、不授权接电机。

## 当前已有证据

这里把“已消化的项目资料”和“硬件签核用原始文件”分开记录。仓库里已经有 V9/技术报告/申报书、部分官方 ST 文档索引和硬件截图/BOM 线索；仍缺的是能直接用于板级签核的原始 EDA、PCB、正式 BOM、Gerber/坐标和若干功率级器件规格页。

| 证据 | 文件 | 当前结论 |
| --- | --- | --- |
| 已消化方案与报告资料 | `materials/extracted/v9_final.txt`、`materials/extracted/tech_report_v1.txt`、`materials/extracted/proposal_v8.txt`、`materials/extracted/proposal_v71.txt` | 已作为系统方案、硬件意图、竞赛表达和历史版本依据；不能替代原始原理图/PCB 签核。 |
| 官方资料索引 | `references/datasheet_index.md` | 已列出已摄入的 STM32G474、NUCLEO、MCSDK 和算法/应用笔记类资料，也列出仍待补的功率级器件规格页。 |
| 原理图截图与截图审查 | `hardware/schematic/2026-05-09_power_board_schematic_screenshot.jpg`、`hardware/schematic/2026-05-09_power_board_schematic_screenshot.md` | 已能看到 STDRIVE101、SCREF、REG12、BOOT、MOS/Gate、接口和 GND_ISO 等关键区域；仍不是原始 EDA 或导出 PDF。 |
| 用户确认版关键器件记录 | `hardware/bom/2026-05-09_user_provided_power_stage_parts.md` | 已记录关键器件、电源轨、保护外围和阈值线索；用户说明不能保证全部正确。 |
| 保护阈值记录 | `docs/03_hardware_notes/protection_thresholds.md` | 已记录 SCREF/VDS、PTC、TVS、SS34、采样电阻等待复核项。 |
| 无电 DMM 检查 | `experiments/2026-06-01_power_board_no_power_dmm/logs/2026-06-01_hall_control_connector_dmm_check.md` | 已排除多项明显短路；不能证明可上电或可接电机。 |
| 24V/0.2A 静态上电操作单 | `experiments/2026-06-01_power_board_first_limited_power_precheck/2026-06-01_24v_0p2a_static_power_on_operation_sheet.md` | 已限定功率板单独上电、无电机、无 NUCLEO/MCU、无 PWM、0.2A 限流和立即断电条件；2026-06-05 已按用户实测完成静态限流上电记录。 |
| 24V/0.2A 静态上电结果 | `experiments/2026-06-01_power_board_first_limited_power_precheck/logs/2026-06-05_24v_0p2a_static_power_on_result.md` | HSPY-30-05 处于 CV，输入电流 0.04A，5V=5V，3V3=3.34V，REG12=12V，nFAULT=3.3V，无异味/异响/快速发热；只证明限流静态供电初步正常。 |

## 仍缺签核资料

| 资料 | 建议路径 | 用途 | 当前状态 |
| --- | --- | --- | --- |
| 原始 EDA 源文件或网表 | `hardware/schematic/` 或 `hardware/pcb/` | 复核 SCREF、DT/MODE、REG12 回流、GND_ISO、Gate/BOOT 网络。 | 未入库 |
| 原理图 PDF | `hardware/schematic/YYYY-MM-DD_power_board_schematic.pdf` | 上电前正式审查和答辩引用。 | 未入库 |
| PCB 顶层/底层/关键区域截图或布局文件 | `hardware/pcb/` | 审查功率回路、Gate、Kelvin、GND 平面和回流路径。 | 未入库 |
| 正式 BOM | `hardware/bom/YYYY-MM-DD_power_board_bom.*` | 复核型号、封装、额定值和替代风险。 | 未入库 |
| Gerber/坐标文件 | `hardware/fabrication/` | 审查生产版本和装配方向。 | 未入库 |
| 功率级器件 Datasheet 或规格页包 | `references/` | 复核 STDRIVE101、MOS、DCDC、TVS、SS34、PTC、采样电阻、母线电容和电机；具体缺口见 `references/datasheet_index.md`。 | 部分官方 ST/MCU 资料已摄入，功率级器件仍待补 |

## 上电前必须复核的设计点

| 项目 | 当前证据 | 上电前口径 |
| --- | --- | --- |
| SCREF 分压 | 截图/BOM 记录 R1 33k 到 3V3、R2 20k 到 GND_SIGNAL；DMM 实测 R1 33.3k、R2 19.8k。 | 不再硬测隐藏中点；后续用原始 EDA/netlist/高清图增强证据。 |
| DT/MODE | 截图中到 GND 的连接不明显。 | 需原始 EDA、网表或局部高清图确认。 |
| REG12 回流 | REG12 去耦回到 GND_SIGNAL，STDRIVE101 EP/VS 涉及 GND_POWER。 | 需结合 R_GND_ISO 和 PCB 回流路径复核。 |
| GND_ISO | DMM 实测 R_GND_ISO 本体 0 ohm。 | 仍需在 PCB 上确认单点连接位置和回流路径。 |
| Gate drive | DMM 实测 GHS/GLS 到 GND 为 OL，到对应 MOS Gate 约 22 ohm。 | 通过无电短路检查；上电后还需示波器验证空载 Gate 波形。 |
| 三相 OUT | DMM 实测 OUTx 对 GND、24V、相间均 OL。 | 通过无电短路检查；不代表可接电机。 |

## 资料导入规则

- 原始资料优先放在 `hardware/` 或 `references/`，不要只贴在聊天里。
- 每份资料必须记录来源、日期、版本、可信度和影响范围。
- 新增资料后更新 `docs/file_map.md`、`CURRENT_STATUS.md`，必要时更新 `workflow/evidence_register.md`。
- 资料进入 `docs/`、`references/`、`workflow/` 或主要索引后，重建 `vector_store/`。

## 当前结论

无电 DMM 检查已完成大部分低风险排查，未发现明显电源轨、BOOT、Gate 或三相输出短路。2026-06-05 用户报告首次 24V/0.2A 级别限流静态上电通过，基础电源轨和 nFAULT 在静态条件下初步正常。仓库已有方案、报告、截图、BOM 线索和部分官方资料作为背景证据；后续硬件签核仍应补原始 EDA/PCB/BOM/Gerber/坐标和功率级器件规格页。任何情况下仍禁止接电机、输出 PWM、放开限流或绕过保护；下一步只能进入单独规划的 MCU 连接前检查、空载 PWM/Gate 波形和采样链路检查。
