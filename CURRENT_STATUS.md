# CURRENT_STATUS

最后更新：2026-05-11

这个文件是项目总控页。每次继续 FOC 项目时，先读这里，再读 `AGENTS.md`、`materials/START_HERE.md` 和 `docs/00_project_truth/project_context.md`。

## 当前阶段

项目处于 NUCLEO 基础工程阶段。2026-05-09 已生成并编译通过 NUCLEO-G474RE baseline CubeMX/CMake 工程，且已加入 LD2 闪烁与 LPUART1 串口打印测试固件；但 baseline 工程尚未完成下载、调试和板上运行验证。用户确认版功率板关键器件、电源轨、保护外围和阈值线索已记录；ESP32 工程、PCB/Gerber、正式 BOM 文件和实测日志还没有开始沉淀。

当前仓库的主要作用是：固定项目事实源、学习路线、安全红线、资料索引、接口契约和后续交付物目录。

## 当前项目定位

- 项目名称：基于 STM32G474 的边缘网关型无感 FOC 驱动系统。
- 主线架构：STM32G474 + STDRIVE101 + 三相 BLDC + Hall 保底 + SMO 无感冲刺 + ESP32-C3 边缘网关。
- 当前工具链口径：VS Code + STM32CubeIDE 插件 + STM32CubeMX + MCSDK；不使用独立 STM32CubeIDE 作为主 IDE。
- 默认服务对象：B 同学，算法/主控方向。
- 工程原则：先安全转起来，再做无感、优化和答辩亮点。

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
- STM32 baseline 工程：`apps/stm32_g474_foc/nucleo_g474re_baseline/`，CubeMX/CMake 生成成功，Debug 构建通过并生成 `build/Debug/nucleo_g474re_baseline.elf`。当前固件会打印 `BOOT OK` / `LD2 toggle` 并每 500 ms 翻转 LD2；尚未下载和板上运行验证。
- ESP32 工程占位目录：`apps/esp32_c3_gateway/`。
- STM32 与 ESP32 协议契约：`interfaces/`。
- 实验记录与答辩交付物目录：`experiments/`、`deliverables/`。
- NUCLEO 基础工程实验记录：`experiments/2026-05-09_nucleo_baseline/`。
- 学习闭环维护脚本：`tools/normalize_learning_loop.py`、`tools/start_learning_session.*`、`tools/end_learning_session.*`。
- 项目自动化契约：`workflow/automation_playbook.md`；当前 Codex 自动化包括每日学习视频邮件、每日项目进化巡检邮件和每周项目复盘邮件，均绑定项目根目录运行。
- Obsidian 笔记工作区：仓库根目录已配置 `.obsidian/`，个人笔记和看板放在 `notes/`，入口为 `notes/00_home/foc_dashboard.md`。

## 当前未开始

- NUCLEO-G474RE baseline CubeMX/CMake 工程已放入；MCSDK 电机控制工程尚未放入。
- 真实 ESP32-C3 网关工程尚未放入。
- 原理图截图已放入；EDA 源文件、导出 PDF、PCB、Gerber/坐标文件、器件 Datasheet 包和正式 BOM 表尚未放入。
- 已有的用户确认版硬件清单仍是待复核线索，不代表硬件设计已审查通过。
- 串口日志、示波器波形、Motor Profiler 结果、Hall 闭环记录尚未产生。

这些不是配置缺失，而是项目尚未进入对应阶段。

## 下一步最小动作

1. 如果要开始学习/实操：进入 NUCLEO-G474RE 基础工程，先做点灯、串口打印、定时器和 UART DMA + IDLE；不接 24V、不接功率板、不接电机。
2. 如果要推进阶段：先对照 `workflow/phase_gate_checklist.md`，确认进入条件、产出证据和禁止动作。
3. 如果要导入新资料：先按 `workflow/intake_checklist.md` 分类命名，再更新对应索引。
4. 如果要继续 STM32 baseline：用 VS Code/STM32Cube 扩展把 `apps/stm32_g474_foc/nucleo_g474re_baseline/` 的 Debug 构建下载到 NUCLEO-G474RE，确认 ST-LINK 连接，再观察 LD2 闪烁，并在 COM5 串口查看 `BOOT OK` / `LD2 toggle`。
5. 如果要开始硬件审查：以 `hardware/bom/2026-05-09_user_provided_power_stage_parts.md` 为器件线索，继续补原理图 PDF、PCB 截图、正式 BOM、Datasheet 和关键保护阈值计算。

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
- 本地检索：`python tools/ask_local.py "你的问题"`
- 开工入口：`powershell -ExecutionPolicy Bypass -File .\tools\start_learning_session.ps1`
- 收工入口：`powershell -ExecutionPolicy Bypass -File .\tools\end_learning_session.ps1 -Topic "主题" -Summary "今天做了什么"`
- 学习队列整理：`python tools/normalize_learning_loop.py`
- 重建检索索引：`python tools/build_vector_store.py`
- 回归测试：`python -m unittest discover -s tests`
