# Automation Playbook

This file records the intended Codex automation behavior for this project. The actual automation definitions live in the user's Codex app, not in this repository, so this page is the project-side contract.

## Active Automations

| Cadence | Name | Purpose | Output | Write Scope |
| --- | --- | --- | --- | --- |
| Daily 20:00 | STM32G474 FOC 每日学习视频邮件 | Recommend one stage-matched learning video. | Gmail to `pinganyan0@gmail.com` | No repo writes |
| Daily 22:30 | STM32G474 FOC 每日项目进化巡检邮件 | Check project direction, learning loop, safety risks, and next action. | Gmail to `pinganyan0@gmail.com` | No repo writes |
| Weekly Sunday 21:30 | STM32G474 FOC 每周项目复盘邮件 | Summarize weekly evidence, gaps, weak points, and next-week tasks. | Gmail to `pinganyan0@gmail.com` | No repo writes |

All project automations should run with the repository root as the working directory:

```text
C:\Users\gregrg\Documents\Codex\2026-04-30\qiansai\foc_learning_repo
```

## ChatGPT + Codex 双师制工作流

ChatGPT 是主老师，负责解释、任务包、复盘和风险判断。Codex 是工程助教，负责执行任务包、改仓库、记录证据和更新交接文件。GitHub 仓库是共同记忆；Obsidian 是个人学习仪表盘，不是最高事实源。

每次任务以 `workflow/ACTIVE_TASK.md` 为唯一执行入口。ChatGPT 应把目标、边界、输入、输出和验收证据写成任务包；Codex 执行时只按任务包和仓库当前事实推进，并把结果回写到仓库。

自动化仍然不得 commit、push、删除、重排用户工作，不得修改高风险控制逻辑、硬件参数、保护阈值、PWM、Gate 或 FOC 实时控制代码。涉及 24V、PWM、Gate、nFAULT、电流采样、Hall/SMO 时，自动化只能提出阶段闸门、证据需求和回退路径。

## Safety Contract

Automations may read project files, check `git status`, and propose low-risk improvements. They must not:

- Commit, push, delete, or reorder user work.
- Modify CubeMX, MCSDK, ESP-IDF, firmware control logic, or hardware parameters.
- Suggest direct 24V, power-board, motor, PWM gate, overcurrent-threshold, Hall/sensorless, or STDRIVE101 protection actions without evidence gates.

For hardware-adjacent content, the output must stay at checklist, evidence requirement, and rollback-path level.

## Manual Maintenance Commands

Use these from the project root when closing a learning session or preparing a push:

```powershell
python tools/normalize_learning_loop.py
python tools/build_vector_store.py
python -m unittest discover -s tests
```

On macOS/Linux:

```bash
python3 tools/normalize_learning_loop.py
python3 tools/build_vector_store.py
python3 -m unittest discover -s tests
```
