---
type: index
status: active
area: experiments
tags:
  - foc/experiment
---

# 实验索引

正式实验记录必须落到 `experiments/YYYY-MM-DD_topic/`。本目录只放实验草稿、预案和复盘草稿。

## 官方实验入口

- [[experiments/README]]
- [[templates/experiment_record_template]]
- [[docs/05_test_and_logs/bringup_checklist]]
- [[docs/05_test_and_logs/test_plan]]
- [[docs/05_test_and_logs/final_acceptance]]

## 实验草稿

```dataview
TABLE status, stage, power_state, motor_connected, evidence_level AS evidence
FROM "notes/30_experiments"
WHERE type = "experiment-draft"
SORT file.mtime DESC
```

## 实验待办

```tasks
not done
path includes notes/30_experiments
sort by priority
sort by due
```
