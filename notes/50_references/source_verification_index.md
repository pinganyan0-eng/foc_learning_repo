---
type: index
status: active
area: references
tags:
  - foc/source-check
---

# 资料核查索引

涉及外部动态事实时，先按 [[docs/00_project_truth/internet_verification_rules]] 核查官方来源。

## 官方资料入口

- [[references/official_links]]
- [[references/st_manuals_index]]
- [[docs/00_project_truth/source_priority]]
- [[docs/00_project_truth/verified_parameters]]

## 核查笔记

```dataview
TABLE status, topic, official_source, conflict, next_action
FROM "notes/50_references"
WHERE type = "source-verification"
SORT file.mtime DESC
```
