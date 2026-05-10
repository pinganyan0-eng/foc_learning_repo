---
type: board
status: active
area: defense
tags:
  - foc/defense
---

# 答辩素材池

这里先收集素材，不直接当最终话术。进入 `docs/06_defense_pack/` 前必须能对应到数据、来源或演示锚点。

## 正式答辩入口

- [[docs/06_defense_pack/demo_script]]
- [[docs/06_defense_pack/b_algorithm_script_4min]]
- [[docs/06_defense_pack/defense_30qa]]
- [[docs/06_defense_pack/evidence_index]]
- [[docs/06_defense_pack/judge_hard_questions]]

## 素材候选

```dataview
TABLE status, claim, evidence, demo_anchor
FROM "notes/60_defense"
WHERE type = "defense-claim"
SORT file.mtime DESC
```

## 素材待办

```tasks
not done
path includes notes/60_defense
sort by due
```
