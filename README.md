# STM32G474 FOC 学习助手工作仓库

这个仓库不是开发板工程本体，而是 Codex 作为学习助手时使用的本地工作区。
它固化项目背景、资料地图、硬件风险、协议约定、代码审查模板、实验记录模板、最小检索问答和回归测试骨架。

## 先读这里

- `AGENTS.md`：Codex 在本仓库里的行为规则，包含事实源优先级、联网核查和硬件安全边界。
- `docs/00_project_truth/project_context.md`：最高优先级项目事实源。
- `docs/00_project_truth/internet_verification_rules.md`：什么时候必须联网、查什么来源、怎么输出证据。

## 当前边界

- 已放入：共享链接文章规则、本地 HTML/PDF/DOCX 抽取文本、V9 方案、技术报告、申报书版本、B 同学学习计划。
- 未放入：真实 STM32CubeIDE/MCSDK 源码树、真实实验日志、真实串口日志。等你给出后放到 `firmware/`、`experiments/`、`logs/`。
- 开发环境不在本仓库范围内；本仓库只配置“Codex 学习助手环境”。

## 常用命令

```powershell
python tools/build_vector_store.py
python tools/ask_local.py "JEOC 中断里能不能 printf"
python tools/ask_local.py "什么时候必须联网核查官方资料"
python -m unittest discover -s tests
```
