## 2026-05-14 P2 STDRIVE101 保护路径审查

- Added STDRIVE101 protection-path review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`.
- The review fixes the required P2 checklist for `DT/MODE`, `nFAULT`,
  `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, standby, and VDS monitoring.
- ST official product page and datasheet (`DS13472 Rev 2`, June 2022) were
  rechecked on 2026-05-14. The official source still describes STDRIVE101 as a
  triple half-bridge gate driver with two input strategies selected by
  `DT/MODE`, 12 V `REG12` gate supply, overcurrent comparator, VDS monitoring,
  UVLO, thermal shutdown, and standby behavior.
- The existing schematic screenshot remains only a low-grade clue. It does not
  prove CN8 routing, PCB routing, connector pinout, STDRIVE101 protection-path
  correctness, or power-stage readiness.
- This update still does not authorize 24V, power-board connection, motor
  connection, Gate PWM, Motor Profiler, Hall closed-loop, or sensorless FOC
  claims.

## 2026-05-14 P2 Parallel Evidence Push

- Added CN8 / STDRIVE101 route review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/cn8_stdrive101_route_review_2026-05-14.md`.
- Rechecked the `.stmcx` / MotorControl side: repo search still found no
  `.stmcx`; narrow checks of `F:\STMCubeMX`,
  `C:\Users\gregrg\STM32Cube\Repository\MCSDK_v6.4.2-Full`, and VS Code
  extension folders still did not prove a saved Workbench project, standalone
  Workbench launcher, or MotorControl configuration page.
- Route review now explicitly accepts only current-version EDA, schematic PDF,
  netlist, or high-resolution route crop as board-route evidence. The existing
  schematic screenshot remains a low-grade clue only.
- The WeChat-side `netlist_PADS.net` candidate was not imported and is not used
  as current board evidence.
- Current blockers remain: real `.stmcx` or MotorControl configuration
  screenshot; accepted CN8 / route evidence; accepted STDRIVE101 `nFAULT`,
  `DT/MODE`, `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, standby, and VDS
  monitoring source evidence.
- This update still does not authorize 24V, power-board connection, motor
  connection, Gate PWM, Motor Profiler, Hall closed-loop, or sensorless FOC
  claims.

## 2026-05-14 P2 GUI 配置证据推进

- Codex 使用 `F:\STMCubeMX\STM32CubeMX.exe` 打开已保存的 NUCLEO-G474RE
  `.ioc` 草案，并新增 GUI 捕获记录：
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_result_2026-05-14.md`.
- 新增截图：
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_launch_attempt.png`
  和
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`.
- 截图证明 CubeMX 可以把保存的 `.ioc` 打开到 `Pinout & Configuration`
  页面，窗口标题显示 `STM32G474RETx - NUCLEO-G474RE`；`.ioc` 读回仍确认
  `PB12/TIM1_BKIN`、`PB14/TIM1_CH2N`、`PA2/PA3` VCP 和 `PB3` SWO。
- `rg --files -g "*.stmcx"` 在 GUI 尝试后仍没有找到 `.stmcx`；本轮也没有
  捕获 MCSDK MotorControl 配置页。当前新增的是 CubeMX `.ioc` GUI fallback
  证据，不是 Workbench / MotorControl 配置证据。
- 这仍然不授权 24V、功率板、电机、Gate PWM、Motor Profiler、烧录/调试、
  Hall 闭环或无感 FOC 结论。

## 2026-05-14 P2 Workbench 入口探测

- Codex 新增 Workbench 入口探测记录：
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`.
- 目标检查覆盖 repo、`F:\STMCubeMX`、`C:\Users\gregrg\STM32Cube\Repository\MCSDK_v6.4.2-Full`、
  VS Code STM32 extension、`.stm32cubemx` 和常见 ST 程序目录。
- 结论：本机已安装 MCSDK `MotorControl` package 数据，能看到
  `MotorControl_Configs.xml`、`MotorControl_Modes.xml`、`MCSDK/`、`templates/`、
  `libMP/` 和 `libHSO/`；但仍没有 repo `.stmcx`、独立 Workbench launcher 或
  MotorControl 配置页截图。
- 因此 P2 当前能证明“MCSDK MotorControl package 数据存在”，不能证明
  “Workbench 项目配置已保存”。

## 2026-05-14 P2 证据包更新

- 已新增当前 P2 证据包：
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`.
- 证据包记录当前仓库真实库存：没有 `.stmcx`，已有 CubeMX 首页截图和
  NUCLEO-G474RE CubeMX `.ioc` 草案；仍没有 Workbench/CubeMX MotorControl
  配置页截图、CN8/EDA/netlist 走线证明，也没有板级 STDRIVE101 保护路径证明。
- 证据包把 `PB12/TIM1_BKIN`、`PB14/TIM1_CH2N`、`PA2/PA3`、`PB3`、
  `DT/MODE` 和 STDRIVE101 保护项放进阻塞表，避免把草案引脚当成
  可信接线。
- 这仍然只是 P2 无功率证据治理，不授权信任生成的 MCSDK 工程，也不授权
  24V、功率板、电机、Gate PWM、Motor Profiler、Hall 闭环或无感 FOC 结论。

## 2026-05-14 P2 NUCLEO CubeMX 实操草案

- 用户按 NUCLEO-G474RE Board Selector 路径完成手把手无功率实操，并保存
  CubeMX `.ioc` 草案：
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`.
- `.ioc` 读回确认：`PA13/PA14` 为 SWD，`PA2/PA3` 为 NUCLEO VCP，
  `PB3` 为 SWO，`PB12` 为 `TIM1_BKIN`，`PB14` 为 `TIM1_CH2N`。
- 这证明 CubeMX 配置层接受当前 NUCLEO 草案和两个关键候选脚；仍不证明
  `.stmcx`、MCSDK MotorControl 工程、CN8/EDA/netlist 走线、STDRIVE101
  保护路径、Gate PWM、Motor Profiler、Hall 闭环或无感 FOC。

## 2026-05-14 Codex Dual-Teacher Gate Update

- Codex continuation is now hardened in
  `workflow/codex_dual_teacher_execution_gate.md`.
- `AGENTS.md`, `workflow/teaching_contract.md`, `workflow/prompt_recipes.md`,
  `workflow/session_close_checklist.md`, and the project Skill source now point
  to the same four-line gate:
  `项目目标` / `学习目标` / `修改范围` / `禁止范围`.
- New regression tests in `tests/test_workflow_contracts.py` check that the gate
  stays linked from the main entry points and keeps the no-power boundary.
- This is a workflow-control update only. It does not authorize 24V, power
  board connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop,
  or sensorless FOC claims.

## 2026-05-14 P2 No-Power GUI Evidence Update

- CubeMX Home screenshot captured:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png`.
- Next GUI-only checklist added:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_checklist_2026-05-14.md`.
- This proves CubeMX GUI launch visibility. The later NUCLEO `.ioc` draft proves
  a CubeMX board/pin configuration was saved, but still does not prove a saved
  MCSDK MotorControl configuration, generated firmware, hardware wiring, Gate
  PWM output, Motor Profiler result, Hall closed-loop behavior, or motor behavior.
- Current blockers remain: real `.stmcx` or Workbench/CubeMX MotorControl
  configuration screenshot; `PB12/TIM1_BKIN` confirmation against
  CubeMX/Workbench plus CN8/EDA/netlist evidence.

## 2026-05-14 NUCLEO Firmware Update

- The NUCLEO baseline now uses LPUART1 RX DMA + IDLE for command reception.
- The interrupt callback only copies received bytes into a ring buffer and
  restarts DMA; command parsing and `printf()` stay in the main loop.
- Debug build passed:
  `apps/stm32_g474_foc/nucleo_g474re_baseline/build/Debug/nucleo_g474re_baseline.elf`.
- Build size after the change: RAM 2552 B, FLASH 23652 B.
- Detailed log:
  `experiments/2026-05-09_nucleo_baseline/logs/2026-05-14_uart_dma_idle_build.md`.
- This is firmware/build progress only. It does not authorize 24V, power board,
  motor, Gate PWM, Motor Profiler, Hall closed-loop, or SMO work.

## 2026-05-14 UART Protocol Model Update

- `src/protocol_model.py` now includes `LineFramer` for DMA/IDLE-like byte
  chunks and newline-delimited JSON frames.
- `tests/test_protocol_model.py` now covers chunk-split frames, multiple frames
  in one chunk, empty lines, oversize drop, discard-until-line-end behavior,
  and recovery.
- `python -m unittest discover -s tests` passes with 24 tests.
- This advances the ESP32/STM32 command path without touching power hardware.

## 2026-05-14 P2 Pin / Config Safety Review

- User clarified they are already familiar with the toolchain; future teaching
  should skip basic CubeMX/CubeIDE navigation unless explicitly requested.
- Next-ring review artifact added:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md`.
- This review defines evidence classes, hard stops, and the minimum packet
  required before trusting any generated MCSDK configuration:
  Workbench/CubeMX `.stmcx` or screenshot, CN8/EDA/netlist routing evidence,
  and STDRIVE101 `nFAULT` / `DT/MODE` / protection-path evidence.
- This is still P2 no-power evidence only. It does not authorize generated
  PWM behavior, Motor Profiler, power-board connection, motor connection, Hall
  closed-loop, or sensorless FOC claims.

# CURRENT_STATUS

最后更新：2026-05-14

这个文件是项目总控页。每次继续 FOC 项目时，先读这里，再读 `AGENTS.md`、`materials/START_HERE.md` 和 `docs/00_project_truth/project_context.md`。

## 当前阶段

项目处于 NUCLEO 基础工程阶段，并已完成当前 P1 概念层验收。2026-05-09 已生成并编译通过 NUCLEO-G474RE baseline CubeMX/CMake 工程；2026-05-11 用户提供 VOFA+ 截图，证明当前固件已下载运行并通过 COM5 / ST-LINK VCP 输出状态机日志，`mode` 与 `mode_name` 能同步显示 `IDLE`、`ARMED`、`RUN_SIM`。2026-05-12 Codex 通过 COM5 验证了 `PING`、`MODE?`、`ARM`、`STOP` 和学习用 `SET_RPM <rpm>` 命令：解析错误、范围错误、状态拒绝、ARM 后目标值更新、STOP 清零均符合规则表。同日，P1 catch-up 交付包已补齐：UART 命令副作用表、DMA + IDLE 接收流程和阶段复盘均已入仓。2026-05-13 学习者独立通过 STOP/DMA P0 迁移检查、命令副作用阅读和 DMA + IDLE 回调五步流程，`normalize_learning_loop.py` 与单元测试通过；同日 P2 MCSDK 无功率预检卡已开始填写，当前已有本机工具版本/status 表、baseline `.ioc` 读回、pin/config 草案、常用 ST PDF 本地镜像、ST 官网交叉核验和 pin-function 冲突处理：`PC5` 被排除为 nFAULT 草案脚，`PB12/TIM1_BKIN` 成为当前 nFAULT 候选，`PA2/PA3` 不再作为 FOC UART 默认选择，`PB3` Hall B 需要释放/隔离 SWO。2026-05-14 Codex 创建了独立的 P2 无功率配置草案目录 `apps/stm32_g474_foc/mcsdk_no_power_precheck/`，记录了 MCSDK draft、冲突决策和工具探测；本机 CubeMX 可执行路径确认为 `F:\STMCubeMX\STM32CubeMX.exe` 并已启动到 `javaw.exe` 进程。随后用户完成 NUCLEO-G474RE Board Selector 手把手实操并保存 CubeMX `.ioc` 草案 `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`，读回确认 `PA13/PA14` 为 SWD、`PA2/PA3` 为 VCP、`PB3` 为 SWO、`PB12` 为 `TIM1_BKIN`、`PB14` 为 `TIM1_CH2N`。仓库内仍没有真实 `.stmcx`，也没有独立 Motor Control Workbench 可执行路径。这些仍不代表 MCSDK MotorControl 工程已生成或任何硬件/电机行为已验证。用户确认版功率板关键器件、电源轨、保护外围和阈值线索已记录；ESP32 工程、PCB/Gerber、正式 BOM 文件和功率/电机实测日志还没有开始沉淀。

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
- P2 MCSDK 无功率预检卡草案：`deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`，当前记录本机工具版本/status、baseline `.ioc` 读回、MCSDK pin/config 草案、ST 官方来源交叉核验、pin-function 冲突处理、shell GUI 证据探测和未来 Motor Profiler 停止/回退计划；2026-05-14 已追加独立无功率草案目录 `apps/stm32_g474_foc/mcsdk_no_power_precheck/`、CubeMX 启动路径、GUI 阻塞记录、NUCLEO-G474RE CubeMX `.ioc` 草案 `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`，以及 STDRIVE101 保护路径审查 `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`；这些只是无功率配置和审查证据，不是 `.stmcx`、MCSDK MotorControl 工程、Motor Profiler、Hall 或功率级验证。
- Obsidian 笔记工作区：仓库根目录已配置 `.obsidian/`，个人笔记和看板放在 `notes/`，入口为 `notes/00_home/foc_dashboard.md`。

## 当前未开始

- NUCLEO-G474RE baseline CubeMX/CMake 工程已放入；P2 已新增 NUCLEO-G474RE CubeMX `.ioc` 草案并保存 `PB12/TIM1_BKIN`、`PB14/TIM1_CH2N`、`PA2/PA3` VCP 和 `PB3` SWO。MCSDK 电机控制工程尚未放入；这些候选尚未经过 MCSDK/Workbench `.stmcx` 和 CN8/EDA/netlist 共同确认，尚未生成真实 `.stmcx` 或 MotorControl 配置截图证据。
- 真实 ESP32-C3 网关工程尚未放入。
- 原理图截图已放入；EDA 源文件、导出 PDF、PCB、Gerber/坐标文件、器件 Datasheet 包和正式 BOM 表尚未放入。
- 已有的用户确认版硬件清单仍是待复核线索，不代表硬件设计已审查通过。
- NUCLEO baseline 串口日志和学习用 `SET_RPM` 命令验证已产生；示波器波形、Motor Profiler 结果、Hall 闭环记录尚未产生。

这些不是配置缺失，而是项目尚未进入对应阶段。

## 下一步最小动作

1. 如果要开始学习/实操：进入 NUCLEO-G474RE 基础工程，先做点灯、串口打印、定时器和 UART DMA + IDLE；不接 24V、不接功率板、不接电机。
2. 如果要推进阶段：先对照 `workflow/phase_gate_checklist.md`，确认进入条件、产出证据和禁止动作。
3. 如果要导入新资料：先按 `workflow/intake_checklist.md` 分类命名，再更新对应索引。
4. 如果要继续 P2 MCSDK 无功率预检：先读 `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`、`apps/stm32_g474_foc/mcsdk_no_power_precheck/config_draft.md`、`apps/stm32_g474_foc/mcsdk_no_power_precheck/hands_on_evidence_2026-05-14.md` 和 `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`；当前已有 NUCLEO-G474RE CubeMX `.ioc` 草案和 STDRIVE101 保护路径缺证矩阵，但仍要补 MCSDK/Workbench `.stmcx` 或 MotorControl 配置截图、CN8/EDA/netlist 走线证据和当前版 STDRIVE101 保护路径源证据；仍不接 24V、不接功率板、不接电机、不运行 Motor Profiler。
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
