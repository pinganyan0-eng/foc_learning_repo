---
type: learning-note
card_type: concept
status: active
area: learning
language: zh-CN
topic: TIM1 ADC JEOC sampling window
mastery: L2
source_status: project-doc
project_writeback: none
tags:
  - foc/learning/zh
  - foc/concept
  - foc/topic/timing
  - foc/status/reviewed
---

# TIM1 / ADC / JEOC 采样窗口

## 一句话

FOC 里不是“随时读 ADC”，而是让 TIM1 的 PWM 时序给 ADC 一个相对安静的采样窗口，ADC injected 转换完成后再触发 JEOC 相关处理。

## 先看现象

- PWM 周期内有开关噪声，电流采样点如果乱飘，算法看到的电流就会不稳定。
- TIM1、TRGO2、ADC injected、JEOC 是一条时序链，而不是四个孤立名词。
- JEOC 回调里不能塞长耗时逻辑；它更像实时控制链路里的窄门。

## 规则表

| 概念 | 中文理解 | 学习时注意 |
| --- | --- | --- |
| TIM1 center-aligned PWM | 让 PWM 计数上下对称，有利于安排采样点 | 不等于已经输出安全 Gate PWM |
| TRGO2 | TIM1 发给 ADC 的触发信号 | 触发源要和实际配置核对 |
| ADC injected | 用于电机控制的定时采样通道 | 不是随手轮询 ADC |
| JEOC | injected 转换完成事件 | 回调里保持短、确定、可预测 |

## 和本项目的关系

- STM32 实时控制：帮助理解“TIM1 center-aligned PWM -> TIM1_TRGO2 -> ADC injected -> JEOC -> FOC”的主时序。
- ESP32-C3 网关：网关只看低频状态，不进入这条实时控制链。
- 硬件安全边界：这张卡只讲概念和阅读方法，不表示硬件采样链路已经验证。
- 答辩表达：可用“定时触发采样，减少噪声和时序不确定性”来解释架构思路。

## 相关链接

- 上游来源：[[docs/00_project_truth/project_context]]
- 主线索引：[[notes/10_learning/learning_index]]
- 邻近概念：[[hall-state-sequence-cn]]

## 自测问题

1. 为什么 FOC 不适合在任意时刻读三相电流？
2. TRGO2 在这条链里扮演什么角色？
3. 为什么 JEOC / FOC ISR 里不应该放 `printf` 或 JSON 解析？

## 边界

这是中文学习卡，不是配置审查、固件运行证据、采样链路实测证据或硬件 readiness。
