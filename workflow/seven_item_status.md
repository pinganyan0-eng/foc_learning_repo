# 七项配置状态

更新时间：2026-04-30

| # | 链接文章要求 | 当前状态 | 证据/路径 |
| --- | --- | --- | --- |
| 1 | 从 Google Drive 导出并固化四份基础文件：`project_brief.md`、`file_map.md`、`hardware_risks.md`、`protocol.md` | 完成 | `docs/project_brief.md`、`docs/file_map.md`、`docs/hardware_risks.md`、`docs/protocol.md` |
| 2 | 把当前可用源码树、实验日志和技术报告放入本地仓库，并启用 Codex CLI Suggest 做第一次项目结构讲解 | 部分完成 | 本地仓库已建；技术报告/V9/学习资料已放入 `materials/`；暂无真实源码树和实验日志；`codex exec -s read-only` 被系统权限拦截，已固化只读等价稿 `workflow/project_structure_suggest.md` |
| 3 | 建最小 vector store，导入 Drive 核心文档与 V9/技术报告，跑通基于文件检索的学习问答 | 完成，但不是云端托管 vector store | `vector_store/`；Drive 核心文档固化笔记 `materials/drive_core_notes.md`；本地 V9/技术报告在 `materials/extracted/`；已跑通 `tools/ask_local.py` |
| 4 | 做 JEOC 中断代码审查模板，并固定在团队工作流 | 完成 | `templates/jeoc_interrupt_review_template.md`、`workflow/ai_review_and_tests.md` |
| 5 | 给协议解析、错误码、状态机和转速命令控制补回归测试，把 AI 审查与测试生成接入 | 完成测试骨架 | `src/protocol_model.py`、`tests/test_protocol_model.py`；9 个回归测试通过；真实 C 固件测试需等源码 |
| 6 | 为每次联调建立统一实验记录格式 | 完成 | `templates/experiment_record_template.md`、`logs/experiment_000_template.md` |
| 7 | 完成一次“本地 Suggest -> Auto Edit -> 手动验证 -> 回滚”演练，建立团队信任边界 | 部分完成 | Auto Edit/测试/回滚已完成并记录在 `workflow/suggest_autoedit_rehearsal.md`；真实 Codex CLI Suggest 因权限未跑通，用只读等价稿替代 |

## 关键边界

- 这里配置的是 Codex 学习助手环境，不是 STM32CubeIDE、CubeMX、MCSDK、Arduino IDE 等开发环境。
- 真实固件源码、真实实验日志、真实硬件资料还没有提供；后续给出后应分别放入 `firmware/`、`experiments/`、`hardware/`。
- 对真实硬件的任何结论都不能只凭测试脚本，需要限流上电、空载 PWM、示波器波形、nFAULT 和故障链路证据。

## 新链接补充

2026-04-30 根据 `https://chatgpt.com/s/t_69f24b8e5b188191a50b0c69a5e2ccaa` 增补：

- `AGENTS.md`：固定 Codex 行为规则。
- `docs/00_project_truth/project_context.md`：建立最高优先级项目事实源。
- `docs/00_project_truth/internet_verification_rules.md`：建立必须联网核查的触发条件和输出格式。
- `templates/internet_verification_template.md`：建立联网核查模板。
