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
| `ai_architecture` | `docs/00_project_truth/ai_architecture.md` | AI 架构契约，定义事实源、上下文包、检索、任务控制、安全闸门、学习记忆、契约检查和后续探针边界 |
| `current_snapshot` | `workflow/CURRENT_SNAPSHOT.md` | 低 token 当前状态快照，避免日常 handoff 默认读取完整 `CURRENT_STATUS.md` 历史 |
| `active_task` | `workflow/ACTIVE_TASK.md` | 当前唯一执行任务包 |
| `task_packet_template` | `workflow/task_packet_template.md` | ChatGPT/Codex 任务包模板 |
| `session_close_checklist` | `workflow/session_close_checklist.md` | 收工、测试、证据与提交前检查清单 |
| `task_state_machine` | `workflow/task_state_machine.md` | ACTIVE_TASK 状态流与 Codex 执行条件 |
| `definition_of_done` | `workflow/definition_of_done.md` | 各类任务的完成标准、伪完成边界和最小验收证据 |
| `evidence_register` | `workflow/evidence_register.md` | 构建、测试、实验、截图、波形和复核证据登记表 |
| `risk_gate_matrix` | `workflow/risk_gate_matrix.md` | L0-L4 风险等级、允许动作、证据要求和禁止动作 |
| `algo_b_teaching_delivery_plan` | `workflow/algo_b_teaching_delivery_plan.md` | B 算法/主控 8 周和 56 天计划的消化版，定义教学节奏、补进度机制、每课/每周上交物和阶段安全边界 |
| `current_learning_sprint` | `workflow/current_learning_sprint.md` | 当前学习 sprint 执行层，记录 P2 MCSDK 无功率预检交付物、复习优先级和退出条件 |
| `teaching_contract` | `workflow/teaching_contract.md` | ChatGPT/Codex 双师制教学规则、代码讲解顺序、新名词解释和课后学习记录要求 |
| `prompt_recipes` | `workflow/prompt_recipes.md` | ChatGPT/Codex 双师制常用提示词 |
| `next_lesson` | `learning/NEXT_LESSON.md` | 下一课执行卡，给出当前阶段、P0/P1/P2 复习优先级、教学流程和 Codex 接力点 |
| `mastery_map` | `learning/MASTERY_MAP.md` | 掌握证据地图，区分已掌握、待迁移验证和禁止声称完成的阶段 |
| `week1_nucleo_baseline` | `docs/05_test_and_logs/week1_nucleo_baseline.md` | P1 NUCLEO baseline 事实、UART 命令分类和副作用表 |
| `uart_dma_idle` | `docs/04_iot_gateway/uart_dma_idle.md` | DMA + IDLE 接收流程、`Size` count/index 规则和 callback 迁移边界 |
| `p1_catchup_pack_2026_05_12` | `deliverables/2026-05-12_p1_catchup_pack.md` | P1 catch-up 周/阶段交付包，链接证据、掌握地图、复习队列和禁止范围 |
| `p2_mcsdk_no_power_precheck_2026_05_13` | `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md` | P2 MCSDK 无功率预检卡，记录工具版本/status、baseline `.ioc` 读回、pin/config 草案和冲突清单 |
| `build_context_pack` | `tools/build_context_pack.py` | 按 `codex_task`、`teaching`、`hardware_review`、`mcsdk_packet`、`experiment_analysis`、`report_defense` 生成最小上下文包 |
| `check_ai_contracts` | `tools/check_ai_contracts.py` | 只读检查 AI 架构入口、当前任务状态、安全短语、索引入口、复习队列和危险正向 claim |
| `search_local_v2` | `tools/search_local_v2.py` | 带事实源优先级、最低可信分、查询扩展和 `retrieval_eval/queries.json` 回归评测的本地证据检索 |

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

## Obsidian 本地笔记层

| 位置 | 用途 |
| --- | --- |
| `.obsidian/` | 打开仓库即用的 Obsidian vault 配置、插件启用清单、模板路径和样式片段 |
| `notes/00_home/foc_dashboard.md` | Obsidian 总控台，聚合当前状态、项目事实、学习、实验、调试和答辩入口 |
| `notes/99_templates/` | 日报、学习卡片、实验草稿、问题闭环、资料核查和答辩素材模板 |
| `notes/90_system/plugin_setup.md` | Obsidian 插件安装与配置说明 |

`notes/` 是个人笔记层，不是项目事实源。可复核结论仍需回写到 `docs/`、`experiments/` 或 `interfaces/`。

## 待你补充

- `apps/stm32_g474_foc/`：VS Code/STM32CubeIDE 插件使用的 STM32CubeMX 或 MCSDK 生成工程。
- `apps/esp32_c3_gateway/`：ESP32-C3 网关真实工程。
- `experiments/`：每次联调记录、波形截图、串口日志。
- `hardware/`：已记录用户确认版关键器件清单和原理图截图；仍待补 EDA 源文件、原理图 PDF、PCB 截图、正式 BOM、Gerber/坐标文件和器件 Datasheet。
- `learning/`：已开始记录 NUCLEO 基础学习过程、薄弱点和复习队列；使用 `tools/normalize_learning_loop.py` 保持编号与表格整洁。
