# 2026-05-30 Hall 软件状态机 ChatGPT 复习回传

## 状态

已完成。用户先由 ChatGPT 做概念教学，再把 5 道题答案贴回 Codex，由 Codex 负责审查、记录和后续工程边界控制。

## 项目边界

- 当前 Hall 路线仍是 `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`。
- `PB3=LIN1`，PB3 不是当前 Hall 输入。
- 本记录只作为 Hall software adapter 概念证据。
- 不上 24V、不接电机、不输出 Gate PWM、不运行 Motor Profiler / Motor Pilot、不声明 MCSDK Hall 闭环可用。

## 用户答案审查

候选正转序列：

```text
001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001
```

| 题目 | 用户答案 | Codex 审查 |
| --- | --- | --- |
| `110 -> 010` | 正向相邻跳转，计 Hall 边沿，不异常 | 正确 |
| `010 -> 110` | 反向相邻跳转，计 Hall 边沿，不异常 | 正确 |
| `111` | 非法 Hall 状态，不计边沿，异常 | 正确 |
| 7 极对电机中 60 度电角度对应机械角度 | `60 / 7 = 8.57 deg` 机械角度 | 概念级正确 |
| 为什么 `PB3` 不能当 Hall | `PB3=LIN1`，Hall 输入保持 `PA0/PA1/PB4` | 正确 |

## 已修正弱点

```text
反向相邻跳转不是异常。
只有 000/111 或非相邻跨状态跳变才记异常。
```

## 证据含义

- Hall 状态机表格分类：L4 no-power 概念证据。
- `PB3=LIN1` 路线约束解释：L4 no-power 概念证据。
- 电角度到机械角度换算：L2-L3 公式练习证据。
- 这不是固件实现证据，不是 GPIO/EXTI 运行证据，不是 MCSDK Hall 接入证据，不是 Gate PWM / 功率板 / 电机验证证据。

## 下一个复习点

软件 Hall firmware 前仍需一句话复述完整 adapter 处理顺序：

```text
raw read -> illegal-state check -> first-valid baseline -> repeat check
-> bounce/timing check -> forward/reverse adjacent check -> abnormal jump count
```
