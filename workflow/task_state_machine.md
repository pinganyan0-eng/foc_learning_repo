# ACTIVE_TASK 状态机

本文件定义 `workflow/ACTIVE_TASK.md` 的状态流，让任务从草拟、确认、执行、阻塞、完成到复盘都有可检查状态。

```text
draft -> approved -> in_progress -> blocked -> done -> reviewed
```

## 状态定义

| 状态 | 含义 | 谁负责推进 | Codex 是否可执行 |
| --- | --- | --- | --- |
| `draft` | ChatGPT 草拟任务，还不能执行。此时目标、边界、输入、输出或验收证据可能不完整。 | ChatGPT | 否 |
| `approved` | 用户确认任务，可给 Codex 执行。任务必须有明确边界、风险等级和验收证据。 | 用户 | 是 |
| `in_progress` | Codex 正在执行。此时应按任务包最小范围修改并记录证据。 | Codex | 是 |
| `blocked` | 缺文件、工具失败、证据不足或风险过高，无法继续安全推进。 | Codex 报告，ChatGPT/用户处理 | 否，除非用户重新批准 |
| `done` | Codex 已完成并写入证据、命令结果和剩余风险。 | Codex | 否，等待复盘 |
| `reviewed` | ChatGPT 或用户已复盘确认，任务可以归档或进入下一任务。 | ChatGPT/用户 | 否 |

## 执行规则

- Codex 不执行 `draft` 状态任务。
- Codex 只能执行 `approved` 或 `in_progress` 状态任务。
- 如果任务涉及 24V、PWM、Gate、nFAULT、电流采样、SCREF/VDS、Hall/SMO 或电机接入，必须先回到 `workflow/phase_gate_checklist.md`。
- 任务从 `blocked` 恢复时，必须补充缺失证据、修改风险等级或由用户重新确认。
- 任务到 `done` 后，不能自动进入 `reviewed`；必须由 ChatGPT 或用户复盘确认。
- 每次状态变化都应更新 `workflow/ACTIVE_TASK.md`。

## 推荐状态字段

```text
Status: approved
Risk Level: L0
Definition of Done: workflow/definition_of_done.md#仓库维护任务
Evidence ID: EV-YYYY-MM-DD-001
Review Required: yes
```
