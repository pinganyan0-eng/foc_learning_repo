# CURRENT_STATUS

最后更新：2026-05-08

这个文件是项目总控页。每次继续 FOC 项目时，先读这里，再读 `AGENTS.md`、`materials/START_HERE.md` 和 `docs/00_project_truth/project_context.md`。

## 当前阶段

项目处于准备期，真实 STM32/ESP32 工程、硬件资料和实测日志还没有开始沉淀。

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
- 阶段推进闸门：`workflow/phase_gate_checklist.md`。
- 首次资料导入规则：`workflow/intake_checklist.md`。
- MacBook Codex 双机配置入口：`workflow/macbook_codex_replica.md`、`tools/create_mac_codex_setup_bundle.ps1`、`tools/bootstrap_mac_codex.sh`。
- GitHub 双机同步远端：`origin` -> `https://github.com/pinganyan0-eng/foc_learning_repo`（私有仓库）。
- STM32/ESP32 工程占位目录：`apps/stm32_g474_foc/`、`apps/esp32_c3_gateway/`。
- STM32 与 ESP32 协议契约：`interfaces/`。
- 实验记录与答辩交付物目录：`experiments/`、`deliverables/`。

## 当前未开始

- 真实 VS Code/STM32CubeIDE 插件、STM32CubeMX 或 MCSDK 工程尚未放入。
- 真实 ESP32-C3 网关工程尚未放入。
- 原理图、PCB、BOM、Gerber 等硬件资料尚未放入。
- 串口日志、示波器波形、Motor Profiler 结果、Hall 闭环记录尚未产生。

这些不是配置缺失，而是项目尚未进入对应阶段。

## 下一步最小动作

1. 如果要开始学习：从 `materials/START_HERE.md` 进入，按 Day 1 做 Windows 工具链（VS Code + STM32CubeIDE 插件 + STM32CubeMX）和 NUCLEO-G474RE 基础工程。
2. 如果要推进阶段：先对照 `workflow/phase_gate_checklist.md`，确认进入条件、产出证据和禁止动作。
3. 如果要导入新资料：先按 `workflow/intake_checklist.md` 分类命名，再更新对应索引。
4. 如果要开始 STM32 工程：把真实 CubeMX/MCSDK 生成工程放进 `apps/stm32_g474_foc/`，用 VS Code + STM32CubeIDE 插件打开/构建/调试，并保持 ST 生成目录原结构。
5. 如果要开始硬件审查：先建立 `hardware/`，放原理图 PDF、PCB 截图、BOM 和关键器件资料。

## 安全红线

- 不直接 24V 大电流上电。
- 首次上电使用限流电源，默认从 0.2A 级别开始。
- 接电机前先做空载 PWM、Gate 波形、nFAULT、VS/REG12/VREG 和采样链路检查。
- JEOC/FOC ISR 内不放 `printf`、`HAL_Delay`、JSON 解析、WebSocket、动态内存或长耗时逻辑。
- V9 与官方 Datasheet 冲突时，先相信官方资料并提示风险；V9 与实测冲突时，先检查测试条件。

## 常用入口

- 项目规则：`AGENTS.md`
- 学习入口：`materials/START_HERE.md`
- 项目事实：`docs/00_project_truth/project_context.md`
- 阶段闸门：`workflow/phase_gate_checklist.md`
- 资料导入：`workflow/intake_checklist.md`
- 本地检索：`python tools/ask_local.py "你的问题"`
- 重建检索索引：`python tools/build_vector_store.py`
- 回归测试：`python -m unittest discover -s tests`
