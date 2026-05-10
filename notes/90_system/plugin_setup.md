---
type: note-system
status: active
area: obsidian
tags:
  - foc/notes
---

# 插件安装清单

打开 Obsidian 后，选择 `foc_learning_repo/` 作为 vault，然后安装下面插件。`.obsidian/community-plugins.json` 已经写好启用清单，但 Obsidian 仍需要你在社区插件市场安装插件本体。

## 必装

| 插件 | 用途 | 建议设置 |
| --- | --- | --- |
| Dataview | 让看板自动列出学习卡片、实验草稿、问题闭环 | 关闭 DataviewJS，先只用查询 |
| Templater | 用模板创建学习、实验、调试笔记 | Template folder: `notes/99_templates` |
| Tasks | 管理待办、截止日期、优先级 | 开启 created date 即可 |
| Omnisearch | 强化全文搜索 | 默认配置即可 |
| Git / Obsidian Git | 在 Obsidian 内手动备份笔记和仓库变更 | 关闭自动备份、定时 pull、定时 push |

## 强烈推荐

| 插件 | 用途 | 建议设置 |
| --- | --- | --- |
| Calendar | 快速打开日报 | 默认配置即可 |
| Periodic Notes | 周报、月报 | Daily folder: `notes/02_daily` |
| Excalidraw | 画 FOC 控制框图、上电检查流程、系统结构 | 默认保存到 `assets/obsidian/excalidraw` |

## 不建议一开始装太多

先别上复杂主题、AI 自动整理、自动发布和大型数据库插件。这个项目最需要的是：能沉淀证据、能快速搜索、能把问题闭环。

## Git 使用口径

可以使用 Obsidian 社区插件里的 `Git`，它通常就是 Obsidian Git。本仓库已经按保守口径配置：不自动备份、不定时 pull、不定时 push，只在你手动触发时提交。

这个仓库还有代码、工程文件和实验资料。使用插件备份前，先看变更范围，确认不要把临时工程输出、错误实验日志或不想提交的文件混进去。

命令行常用节奏仍然保留：

```bash
git status
git add notes .obsidian assets/obsidian AGENTS.md CURRENT_STATUS.md docs/file_map.md
git commit -m "notes: update obsidian notes"
git push
```
