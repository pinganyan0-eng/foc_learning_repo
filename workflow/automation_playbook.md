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
