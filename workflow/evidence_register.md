# 证据登记表

本文件登记项目证据，帮助后续复盘、答辩和风险判断。证据可以来自构建输出、测试、串口日志、截图、波形、实验记录、Datasheet、人工复核或工具输出。

| Evidence ID | 日期 | 阶段 | 结论 | 证据类型 | 文件路径 | 关联任务 | 可信度 | 是否可用于答辩 | 待复核项 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV-2026-05-09-NUCLEO-BUILD-001 | 2026-05-09 | NUCLEO 基础工程 | NUCLEO baseline 已构建通过但尚未板上运行验证 | 构建记录 | `apps/stm32_g474_foc/nucleo_g474re_baseline/` | NUCLEO baseline 工程建立 | 中：构建结论可信，板上运行未由本条证据证明 | 可用于说明“工程可构建”，不可用于说明“板上已跑通” | 需要补充下载运行、串口日志、LD2 观察或调试截图；如已有后续证据，应新增记录而不是覆盖本条 |
| EV-2026-05-11-WORKFLOW-HARDENING-001 | 2026-05-11 | 阶段 0/流程固化 | 双师制流程已补齐状态机、完成定义、证据登记、风险矩阵和提示词模板，维护命令通过 | 文档审计与命令结果 | `workflow/ACTIVE_TASK.md`、`workflow/task_state_machine.md`、`workflow/definition_of_done.md`、`workflow/evidence_register.md`、`workflow/risk_gate_matrix.md`、`workflow/prompt_recipes.md` | TASK-2026-05-11-dual-teacher-workflow | 高：文件和命令结果可复查；不代表硬件验证 | 可用于说明项目流程管理能力，不可用于说明电机或功率级已验证 | 需要 ChatGPT 或用户复盘后把任务状态从 `done` 升级为 `reviewed` |

## 字段说明

- `Evidence ID`：稳定证据编号，建议使用 `EV-YYYY-MM-DD-topic-序号`。
- `日期`：证据产生日期，不是登记日期。
- `阶段`：对应项目阶段或任务阶段。
- `结论`：只写该证据能支持的结论。
- `证据类型`：构建记录、测试输出、串口日志、截图、波形、实验记录、Datasheet、人工复核等。
- `文件路径`：仓库内相对路径；外部来源应先归档或记录到 `references/`。
- `关联任务`：对应 `workflow/ACTIVE_TASK.md` 或历史任务名。
- `可信度`：低/中/高，并说明限制。
- `是否可用于答辩`：区分可直接使用、只能作背景、不可使用。
- `待复核项`：下一步补证据或复核事项。
