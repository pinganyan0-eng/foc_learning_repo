# CURRENT_STATUS

最后更新：2026-06-01

这个文件是项目总控页。每次继续 FOC 项目时，先读这里，再读 `AGENTS.md`、`materials/START_HERE.md` 和 `docs/00_project_truth/project_context.md`。

## 当前阶段

项目处于 NUCLEO 基础工程阶段，同时自研功率板开始进入无电 DMM 后的首次限流上电前准备。2026-05-09 已生成并编译通过 NUCLEO-G474RE baseline CubeMX/CMake 工程；2026-05-11 用户提供 VOFA+ 截图，证明当前固件已下载运行并通过 COM5 / ST-LINK VCP 输出状态机日志，`mode` 与 `mode_name` 能同步显示 `IDLE`、`ARMED`、`RUN_SIM`。2026-05-12 Codex 通过 COM5 验证了 `PING`、`MODE?`、`ARM`、`STOP` 和学习用 `SET_RPM <rpm>` 命令：解析错误、范围错误、状态拒绝、ARM 后目标值更新、STOP 清零均符合规则表。2026-06-01 用户提供 Hall、LIN1、nFAULT、电源轨、BOOTx、三相 OUTx、R1/R2、R_GND_ISO、CN8 Pin15 和 Gate drive 的无电 DMM 读数，多数短路检查符合预期，R1/R2 本体值、CN8 Pin15 到 GND_SIGNAL、Gate 到 GND 和 Gate 串阻路径也符合预期；R1/R2 中点不在顶层裸露，不能安全直接 DMM 探测，但既有原理图截图/BOM 记录已给出 R1/R2 中点连接到 STDRIVE101 Pin3/SCREF 的设计证据。已新增功率板证据包清单、首次限流上电前记录表和 24V/0.2A 静态上电现场操作单；这些仍不代表自研板已上电通过。ESP32 工程、PCB/Gerber、正式 BOM 文件和功率/电机实测日志还没有开始沉淀。

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
- ST 官方资料索引：`references/st_manuals_index.md`。
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
- 自研功率板无电 DMM 局部检查记录：`experiments/2026-06-01_power_board_no_power_dmm/logs/2026-06-01_hall_control_connector_dmm_check.md`；证据编号 `EV-2026-06-01-HW-DMM-001`。
- 自研功率板上电前证据包清单：`docs/03_hardware_notes/power_board_evidence_package.md`；首次限流上电前记录表：`experiments/2026-06-01_power_board_first_limited_power_precheck/2026-06-01_first_limited_power_precheck_record.md`；24V/0.2A 静态上电现场操作单：`experiments/2026-06-01_power_board_first_limited_power_precheck/2026-06-01_24v_0p2a_static_power_on_operation_sheet.md`。
- 学习闭环维护脚本：`tools/normalize_learning_loop.py`、`tools/start_learning_session.*`、`tools/end_learning_session.*`。
- 项目自动化契约：`workflow/automation_playbook.md`；当前 Codex 自动化包括每日学习视频邮件、每日项目进化巡检邮件和每周项目复盘邮件，均绑定项目根目录运行。
- 双师制任务入口：`workflow/ACTIVE_TASK.md`、`workflow/task_packet_template.md`、`workflow/session_close_checklist.md`。
- 双师制审计与恢复文件：`workflow/task_state_machine.md`、`workflow/definition_of_done.md`、`workflow/evidence_register.md`、`workflow/risk_gate_matrix.md`、`workflow/prompt_recipes.md`。
- 双师制教学契约：`workflow/teaching_contract.md`，规定 ChatGPT/Codex 教学时的新名词解释、代码讲解顺序、课后学习记录和 GitHub PR 写入规则。
- B 算法同学教学与交付总计划：`workflow/algo_b_teaching_delivery_plan.md`，把两份 8 周/56 天 HTML 学习计划转成当前真实阶段可执行的教学节奏、补进度机制、每课/每周上交物和安全闸门规则。
- Obsidian 笔记工作区：仓库根目录已配置 `.obsidian/`，个人笔记和看板放在 `notes/`，入口为 `notes/00_home/foc_dashboard.md`。

## 当前未开始

- NUCLEO-G474RE baseline CubeMX/CMake 工程已放入；MCSDK 电机控制工程尚未放入。
- 真实 ESP32-C3 网关工程尚未放入。
- 方案、报告、原理图截图、用户确认版硬件清单和部分官方 ST/MCU 资料已入库并已消化；硬件签核层仍缺 EDA 源文件/网表、导出 PDF、PCB 源文件或关键截图、Gerber/坐标文件、正式 BOM，以及 STDRIVE101/MOS/DCDC/TVS/SS34/PTC/采样电阻/母线电容/电机等功率级器件规格页。
- 已有的用户确认版硬件清单仍是待复核线索，不代表硬件设计已审查通过。2026-06-01 的无电 DMM 表已覆盖 Hall/LIN1/nFAULT、24V/5V/REG12 对地、BOOTx-OUTx、OUTx 对地/24V/相间、R1/R2 本体、R_GND_ISO、CN8 Pin15/GND_SIGNAL、Gate 到 GND 和 Gate 串阻路径检查；SCREF 连接已有截图/BOM 级设计证据，但原始 EDA/netlist/PCB-source、原理图 PDF、PCB 源文件/关键截图、正式 BOM 和功率级器件规格页仍未入库。
- NUCLEO baseline 串口日志和学习用 `SET_RPM` 命令验证已产生；示波器波形、Motor Profiler 结果、Hall 闭环记录尚未产生。

这些不是配置缺失，而是项目尚未进入对应阶段。

## 下一步最小动作

1. 如果要开始学习/实操：进入 NUCLEO-G474RE 基础工程，先做点灯、串口打印、定时器和 UART DMA + IDLE；不接 24V、不接功率板、不接电机。
2. 如果要推进阶段：先对照 `workflow/phase_gate_checklist.md`，确认进入条件、产出证据和禁止动作。
3. 如果要导入新资料：先按 `workflow/intake_checklist.md` 分类命名，再更新对应索引。
4. 如果要继续 STM32 baseline：在已验证 COM5 串口命令路径的基础上，补肉眼 LD2 闪烁证据，或继续做 UART DMA + IDLE 接收一行命令。
5. 如果要继续硬件审查/首次静态上电：按 `experiments/2026-06-01_power_board_first_limited_power_precheck/2026-06-01_24v_0p2a_static_power_on_operation_sheet.md` 执行功率板单独 24V/0.2A 限流静态上电记录；仍不接电机、不接 NUCLEO/MCU、不输出 PWM。并继续按 `docs/03_hardware_notes/power_board_evidence_package.md` 补硬件签核资料。

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
- 教学契约：`workflow/teaching_contract.md`
- 提示词模板：`workflow/prompt_recipes.md`
- 本地检索：`python tools/ask_local.py "你的问题"`
- 开工入口：`powershell -ExecutionPolicy Bypass -File .\tools\start_learning_session.ps1`
- 收工入口：`powershell -ExecutionPolicy Bypass -File .\tools\end_learning_session.ps1 -Topic "主题" -Summary "今天做了什么"`
- 学习队列整理：`python tools/normalize_learning_loop.py`
- 重建检索索引：`python tools/build_vector_store.py`
- 回归测试：`python -m unittest discover -s tests`
