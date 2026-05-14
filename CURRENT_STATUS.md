# CURRENT_STATUS

最后更新：2026-05-13

这个文件是项目总控页。每次继续 FOC 项目时，先读这里，再读 `AGENTS.md`、`materials/START_HERE.md` 和 `docs/00_project_truth/project_context.md`。

## 当前阶段

项目处于 NUCLEO 基础工程阶段，并已完成当前 P1 概念层验收。2026-05-09 已生成并编译通过 NUCLEO-G474RE baseline CubeMX/CMake 工程；2026-05-11 用户提供 VOFA+ 截图，证明当前固件已下载运行并通过 COM5 / ST-LINK VCP 输出状态机日志，`mode` 与 `mode_name` 能同步显示 `IDLE`、`ARMED`、`RUN_SIM`。2026-05-12 Codex 通过 COM5 验证了 `PING`、`MODE?`、`ARM`、`STOP` 和学习用 `SET_RPM <rpm>` 命令：解析错误、范围错误、状态拒绝、ARM 后目标值更新、STOP 清零均符合规则表。同日，P1 catch-up 交付包已补齐：UART 命令副作用表、DMA + IDLE 接收流程和阶段复盘均已入仓。2026-05-13 学习者独立通过 STOP/DMA P0 迁移检查、命令副作用阅读和 DMA + IDLE 回调五步流程，`normalize_learning_loop.py` 与单元测试通过；同日 P2 MCSDK 无功率预检卡已开始填写，当前已有本机工具版本/status 表、baseline `.ioc` 读回、pin/config 草案、常用 ST PDF 本地镜像、ST 官网交叉核验和 pin-function 冲突处理：`PC5` 被排除为 nFAULT 草案脚，`PB12/TIM1_BKIN` 成为当前 nFAULT 候选，`PA2/PA3` 不再作为 FOC UART 默认选择，`PB3` Hall B 需要释放/隔离 SWO。这些仍不代表 MCSDK 工程已生成或任何硬件/电机行为已验证。用户确认版功率板关键器件、电源轨、保护外围和阈值线索已记录；ESP32 工程、PCB/Gerber、正式 BOM 文件和功率/电机实测日志还没有开始沉淀。

当前仓库的主要作用是：固定项目事实源、学习路线、安全红线、资料索引、接口契约和后续交付物目录。

## 当前项目定位

- 项目名称：基于 STM32G474 的边缘网关型无感 FOC 驱动系统。
- 主线架构：STM32G474 + STDRIVE101 + 三相 BLDC + Hall 保底 + SMO 无感冲刺 + ESP32-C3 边缘网关。
- 当前工具链口径：VS Code + STM32CubeIDE 插件 + STM32CubeMX + MCSDK；不使用独立 STM32CubeIDE 作为主 IDE。
- 默认服务对象：B 同学，算法/主控方向。
- 工程原则：先安全转起来，再做无感、优化和答辩亮点。
- ChatGPT + Codex 双师制工作流已固化：ChatGPT 负责教学、任务包和复盘；Codex 负责工程执行、证据记录和仓库更新。

## 已完成配置

- 助手身份与项目规则：`AGENTS.md`、`materials/assistant_profile.md`。
- Codex 专属 Skill：`stm32g474-foc-assistant`，已安装到本机 Codex skills 目录，并通过 `quick_validate.py` 官方校验。
- 辅助 Skills：`jupyter-notebook`、`screenshot`，已安装到本机 Codex skills 目录，并通过 `quick_validate.py` 官方校验。
- 最高优先级事实源：`docs/00_project_truth/project_context.md`。
- 联网核查与来源优先级：`docs/00_project_truth/internet_verification_rules.md`。
- 本地资料索引：`materials/source_manifest.json`、`docs/file_map.md`。
- ST 官方资料索引：`references/st_manuals_index.md`；常用 ST PDF 已镜像到 `materials/raw/st_manuals/`，包括 STDRIVE101 datasheet；hash 与官方 URL 记录在 `materials/raw/st_manuals/manifest.json`。
- 本地检索索引：`vector_store/`。
- Windows 工具链：CubeMX 生成工程已完成；STM32CubeIDE for VS Code 扩展本体已安装；扩展托管的 CMake/Ninja/GNU Arm GCC bundle 已可用于构建。当前已验证系统 PATH 中 `cmake` 可用，`ninja`、`arm-none-eabi-gcc` 未加入 PATH；这是 bundle 托管工具链下的正常状态。状态记录见 `workflow/windows_toolchain_status.md`。
- 用户确认版硬件器件与阈值线索：`hardware/bom/2026-05-09_user_provided_power_stage_parts.md`（用户说明不能保证全部正确，尚未做 Datasheet/库存/PCB/实测复核）。
- 原理图截图：`hardware/schematic/2026-05-09_power_board_schematic_screenshot.jpg`，截图元数据：`hardware/schematic/2026-05-09_power_board_schematic_screenshot.md`。
- 阶段推进闸门：`workflow/phase_gate_checklist.md`。
- 首次资料导入规则：`workflow/intake_checklist.md`。
- MacBook Codex 双机配置入口：`workflow/macbook_codex_replica.md`、`tools/create_mac_codex_setup_bundle.ps1`、`tools/bootstrap_mac_codex.sh`。
- GitHub 双机同步远端：`origin` -> `https://github.com/pinganyan0-eng/foc_learning_repo`（私有仓库）。
- STM32 baseline 工程：`apps/stm32_g474_foc/nucleo_g474re_baseline/`，CubeMX/CMake 生成成功，Debug 构建通过并生成 `build/Debug/nucleo_g474re_baseline.elf`。当前固件已在 NUCLEO-G474RE 上通过 COM5 / ST-LINK VCP 输出状态机日志；证据见 `experiments/2026-05-09_nucleo_baseline/logs/2026-05-11_vofa_mode_name_log.md`。2026-05-12 已追加串口命令验证和学习用 `SET_RPM` 验证；证据见 `experiments/2026-05-09_nucleo_baseline/logs/2026-05-12_com5_set_rpm_validation.md`。
- ESP32 工程占位目录：`apps/esp32_c3_gateway/`。
- STM32 与 ESP32 协议契约：`interfaces/`。
- 实验记录与答辩交付物目录：`experiments/`、`deliverables/`。
- NUCLEO 基础工程实验记录：`experiments/2026-05-09_nucleo_baseline/`。
- 学习闭环维护脚本：`tools/normalize_learning_loop.py`、`tools/start_learning_session.*`、`tools/end_learning_session.*`。
- 项目自动化契约：`workflow/automation_playbook.md`；当前 Codex 自动化包括每日学习视频邮件、每日项目进化巡检邮件和每周项目复盘邮件，均绑定项目根目录运行。
- 双师制任务入口：`workflow/ACTIVE_TASK.md`、`workflow/task_packet_template.md`、`workflow/session_close_checklist.md`。
- 双师制审计与恢复文件：`workflow/task_state_machine.md`、`workflow/definition_of_done.md`、`workflow/evidence_register.md`、`workflow/risk_gate_matrix.md`、`workflow/prompt_recipes.md`。
- 双师制教学契约：`workflow/teaching_contract.md`，规定 ChatGPT/Codex 教学时的新名词解释、代码讲解顺序、课后学习记录和 GitHub PR 写入规则。
- B 算法同学教学与交付总计划：`workflow/algo_b_teaching_delivery_plan.md`，把两份 8 周/56 天 HTML 学习计划转成当前真实阶段可执行的教学节奏、补进度机制、每课/每周上交物和安全闸门规则。
- 当前学习执行层：`learning/NEXT_LESSON.md`、`learning/MASTERY_MAP.md`、`workflow/current_learning_sprint.md`，把 P1 下一课、掌握证据、复习优先级和 sprint 交付物从长计划里抽成短入口。
- P1 catch-up 交付包：`deliverables/2026-05-12_p1_catchup_pack.md`，并已把 UART 命令副作用表写入 `docs/05_test_and_logs/week1_nucleo_baseline.md`、DMA + IDLE 接收流程写入 `docs/04_iot_gateway/uart_dma_idle.md`。
- P2 MCSDK 无功率预检卡草案：`deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`，当前记录本机工具版本/status、baseline `.ioc` 读回、MCSDK pin/config 草案、ST 官方来源交叉核验、pin-function 冲突处理、shell GUI 证据探测和未来 Motor Profiler 停止/回退计划；这只是无功率计划证据，不是 MCSDK 工程、Motor Profiler、Hall 或功率级验证。
- Obsidian 笔记工作区：仓库根目录已配置 `.obsidian/`，个人笔记和看板放在 `notes/`，入口为 `notes/00_home/foc_dashboard.md`。

## 当前未开始

- NUCLEO-G474RE baseline CubeMX/CMake 工程已放入；MCSDK 电机控制工程尚未放入。P2 预检卡中的 pin/config 仍是草案，`PB12/TIM1_BKIN` 等候选尚未经过 Workbench/CubeMX 和 CN8/EDA/netlist 共同确认，尚未生成 `.stmcx` 或 Workbench 截图证据。
- 真实 ESP32-C3 网关工程尚未放入。
- 原理图截图已放入；EDA 源文件、导出 PDF、PCB、Gerber/坐标文件、器件 Datasheet 包和正式 BOM 表尚未放入。
- 已有的用户确认版硬件清单仍是待复核线索，不代表硬件设计已审查通过。
- NUCLEO baseline 串口日志和学习用 `SET_RPM` 命令验证已产生；示波器波形、Motor Profiler 结果、Hall 闭环记录尚未产生。

这些不是配置缺失，而是项目尚未进入对应阶段。

## 下一步最小动作

1. 如果要开始学习/实操：进入 NUCLEO-G474RE 基础工程，先做点灯、串口打印、定时器和 UART DMA + IDLE；不接 24V、不接功率板、不接电机。
2. 如果要推进阶段：先对照 `workflow/phase_gate_checklist.md`，确认进入条件、产出证据和禁止动作。
3. 如果要导入新资料：先按 `workflow/intake_checklist.md` 分类命名，再更新对应索引。
4. 如果要继续 P2 MCSDK 无功率预检：先读 `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`，补 Workbench/CubeMX 截图或真实 `.stmcx` 证据，重点确认 `PB12/TIM1_BKIN` nFAULT、`PB14/TIM1_CH2N`、`PA2/PA3` 排除策略和 `PB3` Hall/SWO 选择；当前 shell 未证明 Workbench 可执行路径或已有 `.stmcx`，仍不接 24V、不接功率板、不接电机、不运行 Motor Profiler。
5. 如果要继续 STM32 baseline：在已验证 COM5 串口命令路径的基础上，补肉眼 LD2 闪烁证据，或由 Codex 进行真实 UART DMA + IDLE callback 的无功率实现/构建验证。
6. 如果要开始硬件审查：以 `hardware/bom/2026-05-09_user_provided_power_stage_parts.md` 为器件线索，继续补原理图 PDF、PCB 截图、正式 BOM、Datasheet 和关键保护阈值计算。

## 安全红线

- 不直接 24V 大电流上电。
- 首次上电使用限流电源，默认从 0.2A 级别开始。
- 接电机前先做空载 PWM、Gate 波形、nFAULT、VS/REG12/VREG 和采样链路检查。
- JEOC/FOC ISR 内不放 `printf`、`HAL_Delay`、JSON 解析、WebSocket、动态内存或长耗时逻辑。
- V9 与官方 Datasheet 冲突时，先相信官方资料并提示风险；V9 与实测冲突时，先检查测试条件。

## 常用入口

- 项目规则：`AGENTS.md`
- Obsidian 总控台：`notes/00_home/foc_dashboard.md`
- 学习入口：`materials/START_HERE.md`
- 项目事实：`docs/00_project_truth/project_context.md`
- 阶段闸门：`workflow/phase_gate_checklist.md`
- 资料导入：`workflow/intake_checklist.md`
- 当前任务包：`workflow/ACTIVE_TASK.md`
- 任务包模板：`workflow/task_packet_template.md`
- 收工检查：`workflow/session_close_checklist.md`
- 任务状态机：`workflow/task_state_machine.md`
- 完成定义：`workflow/definition_of_done.md`
- 证据登记：`workflow/evidence_register.md`
- 风险矩阵：`workflow/risk_gate_matrix.md`
- 教学与交付总计划：`workflow/algo_b_teaching_delivery_plan.md`
- 下一课执行卡：`learning/NEXT_LESSON.md`
- 掌握证据地图：`learning/MASTERY_MAP.md`
- 当前学习 sprint：`workflow/current_learning_sprint.md`
- 教学契约：`workflow/teaching_contract.md`
- 提示词模板：`workflow/prompt_recipes.md`
- 本地检索：`python tools/ask_local.py "你的问题"`
- 开工入口：`powershell -ExecutionPolicy Bypass -File .\tools\start_learning_session.ps1`
- 收工入口：`powershell -ExecutionPolicy Bypass -File .\tools\end_learning_session.ps1 -Topic "主题" -Summary "今天做了什么"`
- 学习队列整理：`python tools/normalize_learning_loop.py`
- 重建检索索引：`python tools/build_vector_store.py`
- 回归测试：`python -m unittest discover -s tests`
