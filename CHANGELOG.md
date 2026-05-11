# CHANGELOG

## 2026-05-11

- 修正项目自动化契约：每日学习视频、每日项目进化巡检和每周项目复盘均应绑定 `foc_learning_repo` 项目根目录，并通过 Gmail 输出。
- 新增 `workflow/automation_playbook.md`，记录自动化职责、输出渠道、禁止动作和安全边界。
- 新增 `tools/normalize_learning_loop.py`，把学习薄弱点整理为稳定 `WP-001` 编号，并同步修正复习队列引用。
- 更新 `tools/record_learning_session.py`，默认记录新薄弱点时自动分配稳定编号，避免继续产生 `WP-new`。
- 新增开工/收工脚本 `tools/start_learning_session.*` 与 `tools/end_learning_session.*`，用于读状态、整理学习队列、记录学习摘要、重建检索索引和跑测试。
- 更新 `tools/sync_project.*`，在 `push` 前自动整理学习队列、重建 `vector_store/` 并运行测试，降低 Windows/Mac 双机同步时的状态漂移。
- 新增 `.gitattributes`，强制 `.sh` 使用 LF，避免 Mac 端执行脚本时遇到 Windows 换行问题。
- 整理 `learning/weak_points.md` 与 `learning/review_queue.md`，把已有 NUCLEO 基础学习记录从临时 `WP-new` 归档为稳定 `WP-001` 至 `WP-007`。

## 2026-05-09

- 新增 `hardware/bom/2026-05-09_user_provided_power_stage_parts.md`，记录用户提供的功率板关键器件清单。
- 更新 `CURRENT_STATUS.md`、`docs/00_project_truth/project_context.md`、`docs/file_map.md` 和 `references/datasheet_index.md`，把该清单标记为待复核硬件线索。
- 将 `hardware/` 纳入本地检索索引构建范围。
- 将初始器件记录细分为关键器件、电压/电源轨、栅极/自举/采样、保护器件和保护阈值待计算项。
- 根据用户按原理图确认的信息，更新 5V/3.3V 模块、电流采样、STDRIVE101 外围、PTC、端子、TVS、母线电容、MOSFET 和保护阈值记录，并标注未复核风险。
- 归档用户提供的功率板原理图截图，新增截图元数据，并补充截图可见的 VS 去耦、HIN/LIN 串阻、Gate-Source 10k、Hall 滤波、CN8、R_GND_ISO 和待复核点。
- 记录用户确认 Windows 工具链已完成，新增 `workflow/windows_toolchain_status.md`，并将下一步最小动作调整为 NUCLEO-G474RE 基础工程。
- 根据官方 UM2505 修正 NUCLEO-G474RE 基础工程口径：LD2 为 PA5，默认 ST-LINK Virtual COM 为 LPUART1 PA2/PA3，不再写成 USART2。
- 生成 NUCLEO-G474RE baseline CubeMX/CMake 工程，确认 VS Code STM32Cube bundle 托管的 CMake/Ninja/GNU Arm GCC 可用，并完成 Debug 空工程编译。
- 为 NUCLEO-G474RE baseline 加入 LD2 500 ms 翻转和 LPUART1 串口 `BOOT OK` / `LD2 toggle` 测试输出，并重新编译通过。

## 2026-04-30

- 初始化学习助手仓库。
- 固化 V9、技术报告、学习计划和 Drive 核心笔记。
- 新增 `AGENTS.md`、项目事实源、联网核查规则。
- 新增竞赛工程仓库骨架。
