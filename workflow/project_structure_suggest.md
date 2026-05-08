# 项目结构讲解（只读 Suggest 等价稿）

## 这仓库解决什么问题

这个仓库是 Codex 学习助手的本地工作区，不是 STM32 固件工程本体。它把共享链接文章、本地 V9/技术报告/申报书/学习计划抽取文本、项目规则、硬件红线、通信协议、JEOC 审查模板、实验记录模板、检索问答和回归测试骨架固化下来。

它的目标是让后续提问有统一上下文：你问“今天学什么”“这段 JEOC 能不能放 printf”“UART 为什么断帧”“上电前要看什么”，我都先从这些固定资料和工作流里找答案，再结合你给的日志/源码/波形定位。

## 每个目录放什么

- `docs/`：四份基础文件，分别是项目简报、资料地图、硬件风险、协议约定。
- `materials/`：从共享链接和本地文件抽取/固化的资料，包含 V9、技术报告、申报书和学习计划。
- `src/`：当前只有协议/状态机的 Python 规格模型，用来先把行为说清楚。
- `tests/`：协议解析、错误码、状态机、速度命令控制的回归测试。
- `templates/`：JEOC 中断代码审查模板和联调实验记录模板。
- `tools/`：本地检索索引构建、基于资料的问答、Auto Edit 回滚演练脚本。
- `vector_store/`：最小本地向量/词频检索索引。
- `workflow/`：AI 审查接入方式、只读结构讲解提示词、Suggest/Auto Edit/验证/回滚演练记录。
- `logs/`：后续真实联调记录。

## B 同学今天最该从哪里开始

先从 `docs/protocol.md` 和 `tests/test_protocol_model.py` 开始。原因很简单：B 同学既要懂主控实时边界，也要和 C 同学的 ESP32 网关对接。把 UART JSON 帧、错误码、状态机和速度命令控制跑通，后面接 MCSDK/Hall/SMO 才不会把问题搅成一团。

今天建议做三步：

1. 运行 `python -m unittest discover -s tests`，确认协议模型回归测试全绿。
2. 运行 `python tools/ask_local.py "UART IDLE 如何避免断帧"`，确认本地资料检索可用。
3. 阅读 `templates/jeoc_interrupt_review_template.md`，记住 JEOC/FOC ISR 里禁止 `printf`、`HAL_Delay`、JSON 解析和长耗时逻辑。

## 还缺什么

- 真实 VS Code/STM32CubeIDE 插件 + STM32CubeMX/MCSDK 源码树：放到 `apps/stm32_g474_foc/` 后才能审查真实 JEOC、ADC、TIM1、UART、状态机代码。
- 真实实验日志：放到 `experiments/` 或 `logs/`，以后定位问题必须附带供电限流、nFAULT、串口日志、波形截图和操作步骤。
- 真实硬件资料：原理图、PCB、BOM、Gerber、关键波形，放到 `hardware/`。
- Codex CLI 只读执行状态：本次 `codex exec -s read-only` 在当前桌面环境被系统权限拦截，错误为 `Access is denied`；因此这里先固化等价只读讲解稿，真实 CLI Suggest 需要在能正常运行 `codex exec` 的终端里复跑。
