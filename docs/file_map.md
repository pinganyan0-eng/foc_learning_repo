# file_map

## 本地已导入资料

| ID | 文件 | 用途 |
| --- | --- | --- |
| `algo_b_8week` | `materials/extracted/algo_b_8week.txt` | B 同学 8 周学习主线 |
| `algo_56day` | `materials/extracted/algo_56day.txt` | 56 天算法冲刺细化任务 |
| `tech_report_v1` | `materials/extracted/tech_report_v1.txt` | 线上初赛技术报告 |
| `v9_final` | `materials/extracted/v9_final.txt` | V9 最终方案，硬件/系统高优先级参考 |
| `proposal_v8` | `materials/extracted/proposal_v8.txt` | V8 申报书，工程盲区修正版 |
| `proposal_v71` | `materials/extracted/proposal_v71.txt` | V7.1 申报书，历史版本 |
| `hardware_initial_parts_2026_05_09` | `hardware/bom/2026-05-09_user_provided_power_stage_parts.md` | 用户确认版功率板关键器件、电源轨、保护外围和阈值线索，尚待 Datasheet/原理图/BOM/PCB/实测复核 |
| `power_board_schematic_screenshot_2026_05_09` | `hardware/schematic/2026-05-09_power_board_schematic_screenshot.md` | 用户提供的功率板原理图截图元数据和截图初审观察 |
| `automation_playbook` | `workflow/automation_playbook.md` | Codex 每日/每周项目自动化的项目侧契约、边界和人工维护命令 |

## 共享链接中已读 Google Docs

| 文档 | 作用 |
| --- | --- |
| `STM32无感FOC边缘网关项目` | 项目总纲、分工、技术路线 |
| `STM32FOC 工业驱动系统实战指南` | STDRIVE101、低侧三电阻、四层板、上电流程 |
| `STM32G474 无感 FOC 终极指南` | G474 资源、Hall 保底、SMO 冲刺 |
| `嵌入式大赛项目汇报书` | 报告表达与竞赛价值 |
| `STM32G474 STDRIVE101 电路审查` | 关键硬件问题与红线 |
| `原理图审查与问题修复` | 最新审查意见，优先级高于早期采购方案 |
| `算法工程师八周冲刺学习清单` | B 同学学习路线 |
| `主控同学嵌入式竞赛学习计划` | 主控最短路径与避坑 |
| `STM32 串口非阻塞通信学习笔记` | UART DMA + IDLE、环形缓冲 |
| `IoT工程师40天速成学习计划` | ESP32-C3 网关路线 |
| `硬件工程师速成 35 天学习计划` | A 同学硬件学习路线 |

## 资料优先级

1. 最新硬件审查意见、问题修复文档、V9/V8。
2. 技术报告与正式申报书。
3. B 同学 8 周/56 天学习计划。
4. V7.1、早期采购清单、早期设计方案只作历史参考；冲突时不优先采用。

## 待你补充

- `apps/stm32_g474_foc/`：VS Code/STM32CubeIDE 插件使用的 STM32CubeMX 或 MCSDK 生成工程。
- `apps/esp32_c3_gateway/`：ESP32-C3 网关真实工程。
- `experiments/`：每次联调记录、波形截图、串口日志。
- `hardware/`：已记录用户确认版关键器件清单和原理图截图；仍待补 EDA 源文件、原理图 PDF、PCB 截图、正式 BOM、Gerber/坐标文件和器件 Datasheet。
- `learning/`：已开始记录 NUCLEO 基础学习过程、薄弱点和复习队列；使用 `tools/normalize_learning_loop.py` 保持编号与表格整洁。
