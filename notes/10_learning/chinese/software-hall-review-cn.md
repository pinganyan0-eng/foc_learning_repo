---
type: learning-note
card_type: review
status: active
area: learning
language: zh-CN
topic: software Hall review
weak_point: processing order and invalid-state boundary
mastery: L2
review_due: 2026-06-24
source_status: local-note
tags:
  - foc/learning/zh
  - foc/review
  - foc/topic/hall
---

# 软件 Hall 复习卡

## 薄弱点

我容易把“读到 Hall 状态”直接跳成“可以给 MCSDK 当速度反馈”。正确顺序应该先做原始状态记录、无效状态过滤、相邻跳变检查、方向候选、速度候选，再讨论是否有单独审查过的 MCSDK 接口方案。

## 最小复习题

1. 为什么 `000` / `111` 不能直接当作正常 Hall 状态？
2. ISR 里只应该做哪些最小动作？
3. 为什么“host model 通过”不等于“板上 Hall 闭环通过”？

## 标准答案要点

- `000` / `111` 是无效或异常候选，需要记录和过滤，不能直接用于方向 / 速度估计。
- ISR 只保存 raw_state、timestamp、event count 等短路径信息；复杂判断放到低优先级逻辑。
- Host model 是学习和算法边界证据，不证明 GPIO、EXTI、连线、MCSDK Hook 或电机行为。

## 反例 / 陷阱

- 看到六步序列记熟了，就说 Hall 闭环已准备好。
- 把调试字段直接接进 MCSDK 速度 / 位置反馈。
- 用复习通过替代 DMM、固件运行或实验记录。

## 关联卡片

- 概念卡：[[tim1-adc-jeoc-window-cn]]
- 术语卡：[[hall-state-sequence-cn]]
- 项目文件：[[workflow/CURRENT_SNAPSHOT]]

## 下次复习

- [ ] 能口头说出“ISR 最小动作 -> 低优先级过滤 -> 候选值 -> 接口审查”的顺序。
- [ ] 能指出这张卡不证明任何硬件或固件 readiness。

## 边界

复习通过只代表概念掌握进度，不代表硬件、固件、MCSDK 配置、DMM 检查、Hall 闭环或上电 readiness。
