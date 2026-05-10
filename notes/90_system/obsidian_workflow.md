---
type: note-system
status: active
area: obsidian
tags:
  - foc/notes
---

# Obsidian 工作流

## 一句话原则

Obsidian 负责捕捉和连接想法，仓库正式目录负责留下可复核证据。

## 日常闭环

1. 快速想法先进入 [[notes/01_inbox/README|Inbox]] 或当天日报。
2. 确定有学习价值的内容，转成 `learning-note`。
3. 确定是问题的内容，转成 `debug-case`，直到有结论或明确阻塞。
4. 确定影响项目方案的内容，回写到 `docs/`。
5. 确定是真实实验的内容，按 `experiments/YYYY-MM-DD_topic/` 固化。

## 标签约定

- `#foc/learning`：学习卡片。
- `#foc/experiment`：实验预案或复盘草稿。
- `#foc/debug`：问题闭环。
- `#foc/source-check`：官方资料核查。
- `#foc/defense`：答辩素材。
- `#foc/today`：日报与临时执行。

## 状态约定

- `active`：正在推进。
- `waiting`：等待资料、硬件、他人反馈或实测条件。
- `blocked`：当前无法推进，需要明确阻塞原因。
- `done`：已经闭环。
- `archived`：仅保留历史。

## 证据等级

- `idea`：想法。
- `source`：有来源但未实测。
- `simulated`：软件或仿真验证。
- `measured`：有实测日志、波形或仪器数据。
- `official`：来自官方文档或已纳入项目事实源。
