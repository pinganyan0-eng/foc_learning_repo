# 链接 t_69f24b8e 固化摘要

来源：`https://chatgpt.com/s/t_69f24b8e5b188191a50b0c69a5e2ccaa`

主题：项目文件整理与辅导。

## 核心要求

这段对话强调：应该让 Codex 自己联网搜索，但不能自由乱搜、搜到什么就信什么。项目内部文件和外部动态事实必须分层处理。

## 固化规则

- 项目内部事实冲突时，优先采用 `project_context.md` 和 V9。
- 涉及 Datasheet、官方工具链、器件库存、SDK 版本、比赛规则、插件安装方式等外部事实时，必须联网查官方来源再判断。
- 联网来源优先级：ST 官方、OpenAI 官方、器件厂商官网、LCSC/立创、比赛官网、ST Community/GitHub issue/论坛实测帖。
- 不优先相信 CSDN 搬运文、B 站评论区、淘宝详情页、不明来源 PDF、AI 生成博客、无日期/无版本/无出处教程。
- 联网后必须说明来源、官方性、关键结论、是否与 V9 冲突、保守建议、是否需要人工复核 Datasheet。
- 硬件安全相关内容不能直接上电，必须先给风险说明、仪器检查、限流设置、回退方案和不上电验证。

## 已落实文件

- `AGENTS.md`
- `docs/00_project_truth/project_context.md`
- `docs/00_project_truth/internet_verification_rules.md`
- `docs/00_project_truth/openai_codex_network_notes.md`
- `templates/internet_verification_template.md`
