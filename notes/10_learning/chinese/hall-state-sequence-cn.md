---
type: learning-note
card_type: glossary
status: active
area: learning
language: zh-CN
term: Hall state sequence
aliases:
  - Hall 状态序列
  - 001/101/100/110/010/011
topic: Hall software state machine
source_status: project-note
project_writeback: none
tags:
  - foc/learning/zh
  - foc/glossary
  - foc/topic/hall
  - foc/status/reviewed
---

# Hall 状态序列

## 术语

- 中文：Hall 状态序列
- 英文 / 缩写：Hall state sequence
- 常见位置：Hall 传感器学习、软件 Hall 状态机、速度 / 方向估计说明

## 中文解释

三路 Hall 信号会组合成 3 bit 状态。理想换相过程中，只应该在六个有效状态之间按相邻顺序移动；`000` 和 `111` 通常作为无效状态处理。

## 在本项目里怎么用

- 出现位置：软件 Hall 学习、未来 `PA0/PA1/PB4` 调试适配思路、MCSDK Hall 概念阅读。
- 相关文件或概念：[[software-hall-review-cn]]、[[notes/10_learning/learning_index]]
- 不能直接推出的结论：会背序列不等于 GPIO/EXTI 运行正确，也不等于 Hall 闭环可用。

## 易混词

| 容易混淆的词 | 区别 |
| --- | --- |
| Hall 状态 | 某一瞬间的 3 bit 值 |
| Hall 状态序列 | 多个状态随时间变化的顺序 |
| 方向候选 | 根据序列前进 / 后退推测方向，还需要边界处理 |
| 速度候选 | 根据状态变化时间间隔估算速度，还不是闭环验证 |

## 相关链接

- 上游来源：[[docs/00_project_truth/project_context]]
- 概念卡：[[tim1-adc-jeoc-window-cn]]
- 复习卡：[[software-hall-review-cn]]

## 检索关键词

- Hall sequence
- software Hall
- invalid state 000 111
- PA0 PA1 PB4

## 边界

这是术语卡，不声明当前硬件连线、DMM 检查、固件适配、MCSDK Hook 或 Hall 闭环已经通过。
