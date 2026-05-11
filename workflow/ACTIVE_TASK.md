# 当前任务

这是当前唯一任务，不是长期计划。每次执行前先读本文件，再按任务边界执行；任务完成后由 Codex 更新结果区，并由 ChatGPT 继续教学、拆解或复盘。

## Task ID

- ID：TASK-2026-05-11-dual-teacher-workflow
- 主题：优化 ChatGPT + Codex 双师制为可检查、可审计、可恢复流程
- Status：done
- Risk Level：L0
- Definition of Done：`workflow/definition_of_done.md#仓库维护任务`
- Evidence ID：EV-2026-05-11-WORKFLOW-HARDENING-001
- Review Required：yes

## 背景

项目已经把 ChatGPT 与 Codex 的分工固定到仓库中；现在继续补齐状态机、完成定义、证据登记、风险矩阵和常用提示词，让流程可检查、可审计、可恢复。

## 当前阶段

阶段 0/流程固化，不进入硬件或电机动作。

## 任务目标

建立任务状态机、完成定义、证据登记表、风险闸门矩阵和提示词模板，并更新项目总控文件，使后续 ChatGPT 与 Codex 通过仓库稳定交接、审计和恢复。

## 允许做

- 新增 `workflow/task_state_machine.md`。
- 新增 `workflow/definition_of_done.md`。
- 新增 `workflow/evidence_register.md`。
- 新增 `workflow/risk_gate_matrix.md`。
- 新增 `workflow/prompt_recipes.md`。
- 更新 `workflow/ACTIVE_TASK.md`。
- 更新 `workflow/task_packet_template.md`。
- 更新 `CURRENT_STATUS.md`。
- 更新 `docs/file_map.md`。
- 运行文档和索引维护相关检查命令。

## 禁止做

- 不接 24V。
- 不接功率板。
- 不接电机。
- 不改 STM32 控制代码。
- 不改硬件参数。
- 不改 MCSDK/CubeMX 工程配置。
- 不自动 commit。
- 不自动 push。

## 输入文件

- `CURRENT_STATUS.md`
- `AGENTS.md`
- `docs/00_project_truth/project_context.md`
- `workflow/ACTIVE_TASK.md`
- `workflow/task_packet_template.md`
- `docs/file_map.md`

## 输出文件

- `workflow/task_state_machine.md`
- `workflow/definition_of_done.md`
- `workflow/evidence_register.md`
- `workflow/risk_gate_matrix.md`
- `workflow/prompt_recipes.md`
- `workflow/ACTIVE_TASK.md`
- `workflow/task_packet_template.md`
- `CURRENT_STATUS.md`
- `docs/file_map.md`

## 验收证据

- 状态机文件存在，并明确 Codex 不执行 `draft` 状态任务。
- Definition of Done 覆盖学习、工程代码、实验记录、硬件审查、文档/答辩和仓库维护任务。
- 证据登记表存在，并包含 NUCLEO baseline 构建证据初始记录。
- 风险闸门矩阵存在，并明确 24V、PWM、Gate、nFAULT、电流采样、SCREF/VDS、Hall/SMO、电机接入至少 L3/L4。
- 提示词模板存在，并覆盖 ChatGPT 与 Codex 的常用交接场景。
- `ACTIVE_TASK.md` 和 `task_packet_template.md` 包含 Status、Risk Level、Definition of Done、Evidence ID、Review Required。
- `CURRENT_STATUS.md` 和 `docs/file_map.md` 能找到新增入口。
- 维护命令已运行并记录结果。

## 安全边界

本任务仅固化流程，不进入硬件、电机或功率动作。涉及 24V、PWM、Gate、nFAULT、电流采样、Hall/SMO 的后续任务，必须回到 `workflow/phase_gate_checklist.md`。

## 执行步骤

1. 新增状态机、完成定义、证据登记、风险矩阵和提示词模板。
2. 更新当前任务入口和任务包模板。
3. 更新项目总控和文件索引。
4. 运行指定维护命令。
5. 输出修改摘要、命令结果、`git status` 摘要和建议 commit message。

## Definition of Done

- 新增 workflow 文档存在且内容覆盖本任务要求。
- `CURRENT_STATUS.md` 和 `docs/file_map.md` 已加入入口。
- 指定命令已运行并记录结果。
- 未修改 STM32 固件控制逻辑、CubeMX/MCSDK/ESP-IDF 配置、硬件参数、PWM、Gate 或 FOC 实时控制代码。

## Blocked Handling

如果缺文件、命令失败、证据不足或风险升级，Codex 应把 Status 改为 `blocked`，记录失败命令、报错摘要、可能原因和下一步建议，不得绕过限制继续执行。

## Codex 结果区

- 执行状态：done
- 修改文件：`workflow/task_state_machine.md`、`workflow/definition_of_done.md`、`workflow/evidence_register.md`、`workflow/risk_gate_matrix.md`、`workflow/prompt_recipes.md`、`workflow/ACTIVE_TASK.md`、`workflow/task_packet_template.md`、`CURRENT_STATUS.md`、`docs/file_map.md`
- 证据：`python tools/normalize_learning_loop.py` 成功；`python tools/build_vector_store.py` 成功并生成 7478 chunks；`python -m unittest discover -s tests` 成功，12 tests OK
- Evidence ID：EV-2026-05-11-WORKFLOW-HARDENING-001
- 失败命令：无已知失败
- 剩余风险：需要 ChatGPT 或用户复盘后才能将 Status 改为 `reviewed`

## 需要更新的文件

- `workflow/task_packet_template.md`
- `workflow/ACTIVE_TASK.md`
- `workflow/task_state_machine.md`
- `workflow/definition_of_done.md`
- `workflow/evidence_register.md`
- `workflow/risk_gate_matrix.md`
- `workflow/prompt_recipes.md`
- `CURRENT_STATUS.md`
- `docs/file_map.md`

## 建议 commit message

```text
docs: 强化双师制任务审计工作流
```
