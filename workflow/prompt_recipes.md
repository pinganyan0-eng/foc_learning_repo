# 常用提示词

本文件保存 ChatGPT + Codex 双师制工作流常用提示词。使用时先读 `CURRENT_STATUS.md`、`workflow/ACTIVE_TASK.md`、`workflow/risk_gate_matrix.md` 和 `workflow/definition_of_done.md`。

## ChatGPT：生成今日任务包

```text
请作为本项目主老师，先读取 CURRENT_STATUS.md、workflow/ACTIVE_TASK.md、workflow/risk_gate_matrix.md 和 workflow/definition_of_done.md。

请为今天生成一个可交给 Codex 执行的任务包，必须包含：
- Task ID
- Status（先写 draft，等我确认后改 approved）
- Risk Level
- Definition of Done
- Evidence ID
- Review Required
- 背景
- 当前阶段
- 任务目标
- 允许做
- 禁止做
- 输入文件
- 输出文件
- 验收证据
- 安全边界
- 执行步骤
- Blocked Handling
- 建议 commit message

如果任务涉及 24V、PWM、Gate、nFAULT、电流采样、SCREF/VDS、Hall/SMO 或电机接入，必须回到 workflow/phase_gate_checklist.md，不要让 Codex 执行危险动作。
```

## ChatGPT：复盘 Codex 结果

```text
请作为主老师复盘 Codex 的执行结果。

请检查：
1. ACTIVE_TASK.md 的 Status、Risk Level、Definition of Done、Evidence ID 是否完整。
2. Codex 是否只改了允许范围内的文件。
3. 命令结果和失败原因是否可信。
4. evidence_register.md 是否需要新增证据。
5. CURRENT_STATUS.md 是否需要更新。
6. 是否有越过 phase_gate_checklist.md 的风险。

请输出：
- 是否可以把任务状态从 done 改为 reviewed
- 需要补证据的地方
- 下一步最小任务
```

## Codex：执行 ACTIVE_TASK

```text
你现在在 foc_learning_repo 仓库根目录。

请读取：
- CURRENT_STATUS.md
- AGENTS.md
- workflow/ACTIVE_TASK.md
- workflow/task_state_machine.md
- workflow/risk_gate_matrix.md
- workflow/definition_of_done.md

只执行 workflow/ACTIVE_TASK.md 中 Status 为 approved 或 in_progress 的任务。若 Status 是 draft，停止并报告“Codex 不执行 draft 状态任务”。

严格遵守任务的允许做、禁止做、Risk Level、Definition of Done 和安全边界。不要自动 commit，不要自动 push。
```

## Codex：收工并更新证据

```text
请按 workflow/session_close_checklist.md 收工。

必须输出：
- 修改文件列表
- 每个文件作用
- 运行命令和结果
- 失败命令、报错摘要、可能原因和下一步建议
- 是否需要更新 workflow/evidence_register.md
- git status 摘要
- 建议 commit message

如果有实验证据、构建证据、测试证据或截图日志，请登记到 workflow/evidence_register.md；只登记证据能支持的结论，不要扩大结论。
```

## Codex：遇到 blocked 时如何报告

```text
当前任务无法继续时，请把 ACTIVE_TASK.md 的 Status 更新为 blocked，并报告：
- blocked 原因：缺文件 / 工具失败 / 证据不足 / 风险过高 / 其他
- 已完成内容
- 未完成内容
- 当前证据
- 需要用户提供什么
- 是否需要 ChatGPT 重新拆任务
- 是否需要回到 phase_gate_checklist.md

不要绕过限制继续执行。
```

## Codex：硬件审查只做清单不做危险动作

```text
请只做硬件审查清单和证据整理，不做任何危险动作。

禁止：
- 接 24V
- 接功率板
- 接电机
- 修改 PWM、Gate、FOC 实时控制代码
- 修改保护阈值或硬件参数
- 让用户直接上电测试

必须输出：
- 审查对象
- 依据文件
- 风险级别
- 需要回到 phase_gate_checklist.md 的项目
- 缺失证据
- 不上电可完成的检查
- 上电前必须人工确认的条件
```
