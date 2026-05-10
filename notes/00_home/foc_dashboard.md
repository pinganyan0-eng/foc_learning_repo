---
type: dashboard
status: active
area: project-control
tags:
  - foc/dashboard
---

# FOC 项目总控台

> 这里是 Obsidian 入口，不是最高事实源。项目事实先看 [[CURRENT_STATUS]] 和 [[docs/00_project_truth/project_context|project_context]]。

## 快速入口

| 位置 | 用途 |
| --- | --- |
| [[CURRENT_STATUS]] | 当前阶段、下一步、红线 |
| [[materials/START_HERE]] | 学习入口 |
| [[docs/00_project_truth/project_context]] | 最高优先级项目事实 |
| [[workflow/phase_gate_checklist]] | 阶段闸门 |
| [[workflow/intake_checklist]] | 新资料导入 |
| [[experiments/README]] | 实验记录规则 |
| [[interfaces/uart_protocol]] | STM32/ESP32 通信契约 |

## 工作台

- [[notes/00_home/today|今日工作台]]
- [[notes/10_learning/learning_index|学习索引]]
- [[notes/20_engineering/engineering_index|工程索引]]
- [[notes/30_experiments/experiment_index|实验索引]]
- [[notes/40_debug/debug_board|问题闭环看板]]
- [[notes/50_references/source_verification_index|资料核查索引]]
- [[notes/60_defense/defense_material_pool|答辩素材池]]

## 进行中的笔记

```dataview
TABLE status, stage, area, evidence_level AS evidence
FROM "notes"
WHERE status != null AND status != "done" AND status != "archived"
SORT file.mtime DESC
LIMIT 20
```

## 未完成任务

```tasks
not done
path includes notes
sort by priority
sort by due
```

## 最近修改

```dataview
TABLE file.mtime AS modified, type, status, area
FROM "notes"
SORT file.mtime DESC
LIMIT 15
```
