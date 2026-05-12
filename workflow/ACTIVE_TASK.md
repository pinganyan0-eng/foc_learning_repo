# 当前任务

这是当前唯一任务，不是长期计划。每次执行前先读本文件，再按任务边界执行；任务完成后由 Codex 更新结果区，并由 ChatGPT 继续教学、拆解或复盘。

## Task ID

- ID：TASK-2026-05-12-algo-b-teaching-delivery-plan
- 主题：消化 B 算法/主控 8 周与 56 天计划，固化教学节奏、补进度机制和上交物规则
- Status：done
- Risk Level：L0
- Definition of Done：`workflow/definition_of_done.md#仓库维护任务`
- Evidence ID：EV-2026-05-12-WORKFLOW-PLAN-001
- Review Required：yes

## 背景

用户指出两份 B 算法/主控 HTML 计划里有明确的每日/每周上交物、验收、Git tag、周报和里程碑要求，但当前教学只在讲局部知识点，没有让教学节奏追上计划，也没有把每课/每周交付物写进规则。

## 当前阶段

阶段 0/教学与交付计划固化；真实工程仍处于 P1 NUCLEO 基础与 UART 命令阶段。此任务只改工作流、计划、索引和教学规则，不进入硬件或电机动作。

## 任务目标

把 `materials/extracted/algo_b_8week.txt` 和 `materials/extracted/algo_56day.txt` 消化为一份可执行的教学与交付总计划，并把“教学必须做进度检查点、必须绑定上交物、落后先 catch-up、阶段闸门高于日历计划”写入规则文件。

## 允许做

- 新增 `workflow/algo_b_teaching_delivery_plan.md`。
- 更新 `workflow/teaching_contract.md`。
- 更新 `workflow/learning_feedback_loop.md`。
- 更新 `workflow/prompt_recipes.md`。
- 更新 `workflow/session_close_checklist.md`。
- 更新 `codex_skills/stm32g474-foc-assistant/SKILL.md`。
- 更新 `deliverables/submission_checklist.md`。
- 更新 `learning/LEARNING_STATUS.md`。
- 更新 `CURRENT_STATUS.md`、`README.md`、`materials/START_HERE.md`、`docs/file_map.md`。
- 更新 `workflow/evidence_register.md`。
- 运行文档、学习记录和索引维护命令。

## 禁止做

- 不接 24V。
- 不接功率板。
- 不接电机。
- 不改 PWM、Gate、FOC 实时控制路径。
- 不改 MCSDK/CubeMX/ESP-IDF 工程配置。
- 不修改硬件参数或保护阈值。
- 不自动 commit。
- 不自动 push。

## 输入文件

- `materials/extracted/algo_b_8week.txt`
- `materials/extracted/algo_56day.txt`
- `CURRENT_STATUS.md`
- `workflow/phase_gate_checklist.md`
- `workflow/teaching_contract.md`
- `workflow/learning_feedback_loop.md`
- `workflow/prompt_recipes.md`
- `learning/LEARNING_STATUS.md`
- `deliverables/submission_checklist.md`
- `codex_skills/stm32g474-foc-assistant/SKILL.md`

## 输出文件

- `workflow/algo_b_teaching_delivery_plan.md`
- `workflow/teaching_contract.md`
- `workflow/learning_feedback_loop.md`
- `workflow/prompt_recipes.md`
- `workflow/session_close_checklist.md`
- `codex_skills/stm32g474-foc-assistant/SKILL.md`
- `deliverables/submission_checklist.md`
- `learning/LEARNING_STATUS.md`
- `CURRENT_STATUS.md`
- `README.md`
- `materials/START_HERE.md`
- `docs/file_map.md`
- `workflow/evidence_register.md`
- `workflow/ACTIVE_TASK.md`

## 验收证据

- 总计划文件存在，明确来源、官方核验、冲突处理、进度检查点、补进度机制、阶段路线、当前阶段上交物和 ChatGPT/Codex 规则补丁。
- 教学契约和学习反馈流程要求每次教学先做进度检查点，并绑定上交物。
- prompt recipes 和 Skill 源文件包含新计划读取顺序。
- `CURRENT_STATUS.md`、`docs/file_map.md`、`README.md` 和 `materials/START_HERE.md` 能找到新计划入口。
- `deliverables/submission_checklist.md` 包含周交付包模板。
- 证据登记表包含本任务证据行。
- 维护命令已运行并记录结果。

## 安全边界

本任务仅固化教学与交付工作流，不进入硬件、电机或功率动作。涉及 24V、PWM、Gate、nFAULT、电流采样、Hall/SMO、电机接入的后续任务，必须回到 `workflow/phase_gate_checklist.md`。

## 执行步骤

1. 读取两份 B 算法/主控计划和当前阶段文件。
2. 联网核验 MCSDK、STM32CubeIDE for VS Code、STM32G474、STDRIVE101、CORDIC/FMAC、ESP32-C3 UART 等关键假设。
3. 新增教学与交付总计划。
4. 更新教学契约、学习反馈、提示词、Skill、索引、状态页和提交清单。
5. 运行维护命令。
6. 输出修改摘要、命令结果、`git status` 摘要和建议 commit message。

## Definition of Done

- 新计划覆盖教学、交付、进度、补课、阶段闸门和双师分工。
- 入口文件和索引均指向新计划。
- 指定命令已运行并记录结果，或明确说明未运行原因。
- 未修改功率相关代码、CubeMX/MCSDK/ESP-IDF 配置、硬件参数、PWM、Gate 或 FOC 实时控制代码。

## Blocked Handling

如果缺文件、命令失败、证据不足或风险升级，Codex 应把 Status 改为 `blocked`，记录失败命令、报错摘要、可能原因和下一步建议，不得绕过限制继续执行。

## Codex 结果区

- 执行状态：done
- 修改文件：`workflow/algo_b_teaching_delivery_plan.md`、`workflow/teaching_contract.md`、`workflow/learning_feedback_loop.md`、`workflow/prompt_recipes.md`、`workflow/session_close_checklist.md`、`codex_skills/stm32g474-foc-assistant/SKILL.md`、`deliverables/submission_checklist.md`、`learning/LEARNING_STATUS.md`、`CURRENT_STATUS.md`、`README.md`、`materials/START_HERE.md`、`docs/file_map.md`、`workflow/evidence_register.md`、`workflow/ACTIVE_TASK.md`
- 证据：`workflow/evidence_register.md` 中新增 `EV-2026-05-12-WORKFLOW-PLAN-001`；`python tools\normalize_learning_loop.py` 成功；`python tools\build_vector_store.py` 成功并生成 7503 chunks；`python -m unittest discover -s tests` 成功，14 tests OK
- Evidence ID：EV-2026-05-12-WORKFLOW-PLAN-001
- 失败命令：无已知失败
- 剩余风险：需要后续真实执行周交付包；P1 当前 UART 命令副作用表和 DMA + IDLE 流程图仍需补齐为正式上交物

## 建议 commit message

```text
docs: 固化 B 算法教学与交付计划
```
