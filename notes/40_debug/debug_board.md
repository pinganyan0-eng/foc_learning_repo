---
type: board
status: active
area: debug
tags:
  - foc/debug
---

# 问题闭环看板

## 未关闭问题

```dataview
TABLE status, stage, symptom, next_check, evidence_level AS evidence
FROM "notes/40_debug"
WHERE type = "debug-case" AND status != "done" AND status != "archived"
SORT file.mtime DESC
```

## 调试待办

```tasks
not done
path includes notes/40_debug
sort by priority
sort by due
```

## 最小证据包

给 Codex 定位硬件或固件问题时，至少带上：

- 供电电压、限流值、是否接电机。
- 板卡版本、关键外设配置、分支或提交号。
- 串口原始日志，不只写“报错了”。
- nFAULT、Gate、相电流或母线电流证据。
- 已经排除的原因和下一步允许做的最小验证。
