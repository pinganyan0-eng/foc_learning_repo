---
type: note-system
status: active
area: obsidian
tags:
  - foc/notes
---

# Obsidian notes layer

这个目录是本仓库的个人学习笔记层。打开 Obsidian 时，直接选择仓库根目录 `foc_learning_repo/` 作为 vault。

## 边界

- `notes/`：草稿、学习卡片、日报、问题闭环、答辩素材池。
- `docs/`：已经确认、可追溯、可答辩复用的项目事实和知识库。
- `experiments/`：真实联调记录、波形、串口日志、结论。
- `interfaces/`：STM32 与 ESP32 的协议契约。

笔记可以先粗糙，但任何会影响项目方案、硬件安全、实验结论或答辩卖点的内容，最后必须回写到 `docs/` 或 `experiments/`，并保留来源。

## 推荐入口

- [[notes/00_home/foc_dashboard|FOC 总控台]]
- [[notes/00_home/today|今日工作台]]
- [[notes/10_learning/learning_index|中文学习索引]]
- [[notes/90_system/obsidian_workflow|笔记工作流]]
- [[notes/90_system/plugin_setup|插件安装清单]]

## 中文学习卡片

- 中文优先概念、术语和复习卡统一放在 `notes/10_learning/chinese/`。
- 新卡优先从 `notes/99_templates/chinese_concept_card.md`、
  `notes/99_templates/chinese_term_card.md` 或
  `notes/99_templates/chinese_review_card.md` 创建。
- 基础标签使用 `foc/learning/zh`，再叠加 `foc/concept`、
  `foc/glossary` 或 `foc/review`。
- 这些卡片是个人学习材料；影响项目事实、实验结论、接口契约或答辩卖点时，
  仍要回写到 `docs/`、`experiments/`、`interfaces/` 或 `deliverables/`。
