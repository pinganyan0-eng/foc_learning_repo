# 任务包模板

ChatGPT 用它生成任务包，Codex 用它执行任务。ChatGPT 是主老师，负责解释、拆任务、复盘和风险判断；Codex 是工程助教，负责执行、改文件、留证据和更新仓库。GitHub 仓库是共同记忆，`CURRENT_STATUS.md` 是交接棒，`experiments/` 是实验事实，`learning/weak_points.md` 是学习弱点记录。

涉及 24V、PWM、Gate、nFAULT、电流采样、Hall/SMO 时，必须先回到 `workflow/phase_gate_checklist.md` 做阶段闸门确认。

## Task ID

- ID：
- 日期：
- 发起人：
- Status：draft
- Risk Level：
- Definition of Done：
- Evidence ID：
- Review Required：yes

Codex 不执行 `draft` 状态任务。任务必须由用户确认到 `approved`，或由 Codex 执行时标记为 `in_progress` 后，才可进入文件修改和命令执行。

## 背景

- 项目背景：
- 上一次交接：
- 已知证据：

## 当前阶段

- 阶段：
- 阶段依据：
- 是否触及硬件/电机/功率动作：

## 任务目标

- 目标 1：
- 目标 2：
- 非目标：

## 允许做

- 读取并更新任务相关文档、索引、实验记录和学习记录。
- 在明确授权范围内修改仓库文件。
- 记录命令、输出摘要、证据路径和剩余风险。
- 必要时更新 `CURRENT_STATUS.md`，让下一次交接从当前事实开始。

## 禁止做

- 不越过 `workflow/phase_gate_checklist.md`。
- 不直接接 24V、功率板或电机。
- 不修改未经授权的 STM32 固件控制逻辑。
- 不修改 CubeMX、MCSDK、ESP-IDF 工程配置。
- 不修改硬件参数、保护阈值、PWM、Gate、FOC 实时控制代码。
- 不自动 commit、push、删除或重排用户工作。

## 输入文件

- `CURRENT_STATUS.md`：
- `AGENTS.md`：
- 其他输入：

## 输出文件

- 计划更新：
- 计划新增：
- 不应触碰：

## 验收证据

- 文件证据：
- 命令证据：
- 实验证据：
- 截图/日志证据：
- Evidence ID：

## 安全边界

- 当前任务是否涉及 24V：
- 当前任务是否涉及 PWM/Gate/nFAULT：
- 当前任务是否涉及电流采样：
- 当前任务是否涉及 Hall/SMO：
- 如涉及以上任一项，必须先检查 `workflow/phase_gate_checklist.md`，并记录结论。

## 执行步骤

1. 读取 `CURRENT_STATUS.md`、`AGENTS.md`、`workflow/task_state_machine.md` 和本任务包。
2. 确认 Status 不是 `draft`；如果是 `draft`，停止并报告。
3. 对照允许做/禁止做、Risk Level 和 Definition of Done 确认执行边界。
4. 按最小修改范围执行。
5. 记录证据、命令结果和失败原因。
6. 更新 `CURRENT_STATUS.md`、`workflow/evidence_register.md` 或相关索引。
7. 运行任务要求的检查命令。
8. 查看 `git status`，准备交接摘要。

## Definition of Done

- 必须产出：
- 可选产出：
- 不允许伪完成：
- 最小验收证据：

## Blocked Handling

- blocked 原因：
- 已完成内容：
- 未完成内容：
- 当前证据：
- 需要用户提供：
- 是否需要 ChatGPT 重新拆任务：
- 是否需要回到 `workflow/phase_gate_checklist.md`：

## Codex 结果区

- 执行状态：
- Status 更新：
- Risk Level 复核：
- 修改文件：
- 证据：
- Evidence ID：
- 失败命令：
- 剩余风险：
- Review Required：

## 需要更新的文件

- `CURRENT_STATUS.md`：
- `experiments/`：
- `learning/weak_points.md`：
- `learning/review_queue.md`：
- 其他：

## 建议 commit message

```text
docs: 固化 ChatGPT 与 Codex 双师制任务流
```
