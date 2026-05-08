# STM32G474 FOC 学习助手工作仓库

这个仓库现在按第三个链接的要求升级为“工程可构建 + 学习可追踪 + 答辩可复用”的结构：`apps/` 放 STM32 与 ESP32 工程壳，`interfaces/` 固化两端协议，`docs/` 沉淀事实源和知识库，`experiments/` 记录联调过程，`deliverables/` 服务报告与答辩，`references/` 维护官方资料入口。

这个仓库不是开发板工程本体，而是 Codex 作为学习助手时使用的本地工作区。
它固化项目背景、资料地图、硬件风险、协议约定、代码审查模板、实验记录模板、最小检索问答和回归测试骨架。

## 先读这里

- `CURRENT_STATUS.md`：项目总控页，记录当前阶段、缺口和下一步最小动作。
- `AGENTS.md`：Codex 在本仓库里的行为规则，包含事实源优先级、联网核查和硬件安全边界。
- `workflow/phase_gate_checklist.md`：阶段闸门表，规定每个阶段的进入条件、证据和禁止动作。
- `workflow/intake_checklist.md`：首次资料导入清单，规定新工程、硬件资料和实验日志放哪里。
- `workflow/macbook_codex_replica.md`：在 MacBook Codex 上再配置一份同源项目环境，并用 Git 做后续双机同步。
- `docs/00_project_truth/project_context.md`：最高优先级项目事实源。
- `docs/00_project_truth/internet_verification_rules.md`：什么时候必须联网、查什么来源、怎么输出证据。

## 当前边界

- 已放入：共享链接文章规则、本地 HTML/PDF/DOCX 抽取文本、V9 方案、技术报告、申报书版本、B 同学学习计划。
- 未放入：真实 VS Code/STM32CubeIDE 插件 + STM32CubeMX/MCSDK 源码树、真实 ESP32-C3 工程、真实实验日志、真实串口日志。等你给出后分别放到 `apps/stm32_g474_foc/`、`apps/esp32_c3_gateway/`、`experiments/`、`logs/`。
- 开发环境不在本仓库范围内；本仓库只配置“Codex 学习助手环境”。

## 常用命令

```powershell
python tools/build_vector_store.py
python tools/ask_local.py "JEOC 中断里能不能 printf"
python tools/ask_local.py "什么时候必须联网核查官方资料"
python -m unittest discover -s tests
powershell -ExecutionPolicy Bypass -File .\tools\create_mac_codex_setup_bundle.ps1
```
