# Software Hall No-Power Algorithm Prep - 2026-05-22

This is an algorithm-side no-power preparation artifact for the current PCB2
software Hall route. It is not firmware implementation, not MCSDK integration,
not generated-code editing, not a build record, and not hardware validation.

Decision: `Algorithm-side no-power preparation / no firmware implementation / no Hall readiness`.

## 中文速读版

这份文档给算法同学看。现在板子还没焊好，所以不用你做 DMM；DMM 是硬件同学后面补的证据。

你现在要做的是把“软件 Hall 怎么判断状态、怎么记异常、以后怎么调试”先想清楚。这里不写固件、不接 MCSDK 闭环、不上电、不接电机。

当前固定路线：

```text
Hall A/B/C 信号 -> IA/IB/IC -> STM32 的 PA0/PA1/PB4
PB3 固定是 LIN1，不是 Hall
P14/P15 是 3V3/GND
```

一句话规则：`PA0/PA1/PB4` 读出三位 Hall 状态，只认 6 个正常状态，`000/111` 当异常，不在中断里做复杂事情。

## 中文规则表

| 项目 | 你要记住的规则 |
| --- | --- |
| 读取对象 | 读 `PA0/PA1/PB4`，拼成三位 Hall 状态。 |
| 正常状态 | 只接受 `001`、`010`、`011`、`100`、`101`、`110`。 |
| 非法状态 | `000` 和 `111` 不正常，只计数，不更新角度和速度。 |
| 第一次读到正常状态 | 先保存，不判断方向。 |
| 重复状态 | 比如 `001 -> 001`，不算新边沿。 |
| 正常跳变 | 相邻状态跳变才算一次有效边沿。 |
| 跨状态跳变 | 比如 `001 -> 010`，先记异常，不当作正常转动。 |
| 抖动 | 很短时间内来回跳，后面用实测阈值过滤；现在不拍死阈值。 |
| 方向 | 只能先叫“方向候选”，真实方向要等电机和相序实测。 |
| 速度 | 只能先叫“速度候选”，靠边沿时间差估算，不能证明闭环可跑。 |

## 中文练习表

| 场景 | 输入序列 | 期望判断 |
| --- | --- | --- |
| 正转候选 | `001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001` | 每一步合法，方向候选为正转。 |
| 反转候选 | `001 -> 011 -> 010 -> 110 -> 100 -> 101 -> 001` | 每一步合法，方向候选为反转。 |
| 非法低 | `000` | 计非法状态，不更新角度/速度。 |
| 非法高 | `111` | 计非法状态，不更新角度/速度。 |
| 重复状态 | `001 -> 001` | 不算新边沿。 |
| 跨状态跳变 | `001 -> 010` | 计异常跳变，不当正常旋转。 |
| 抖动候选 | `001 -> 101 -> 001` 且间隔很短 | 先记可疑抖动，阈值等实测。 |
| 相序未知 | 任何 6 状态循环 | 只输出候选方向，等实测校准。 |

## 中文中断边界

中断里只做很少的事：

- 记时间戳；
- 读三位 Hall 状态；
- 必要时加计数或置标志；
- 复杂判断、串口打印、JSON、日志、控制决策都放到低优先级任务里。

中断里禁止：`printf`、JSON、`HAL_Delay`、阻塞等待、动态内存分配、复杂 MCSDK 调用、长时间控制决策。

## 中文验收点

你后面能讲清楚这 5 件事，就算算法侧当前 no-power 准备到位：

- 为什么三路 Hall 正常只有 6 个状态；
- 为什么 `000/111` 要当非法状态；
- 为什么 `PA0/PA1/PB4` 是软件 GPIO/EXTI Hall，不是 MCSDK 标准 `TIM2 Hall PA15/PB3/PB10`；
- 为什么 `PB3=LIN1` 后不能再拿它当 Hall；
- 为什么中断里不能打印、不能 JSON、不能阻塞。

## 中文练习卡

下一步请填写：
`software_hall_state_machine_exercise_card_2026-05-22.md`。

这张练习卡只检查算法理解，不需要 DMM、不需要板子、不需要上电。

## Current Route

The default current PCB2 route for this preparation is:

```text
HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4
PB3 = LIN1
P14/P15 = 3V3/GND
```

`PB3` is not a current Hall candidate. The MCSDK / Workbench standard Hall
route `PA15/PB3/PB10` remains generated configuration evidence only and is not
the current PCB2 Hall route.

## DMM Gate Relationship

The DMM gate is hardware-side deferred because PCB2 is not populated yet.
Deferred does not mean passed. This is not a pass.

Algorithm-side state-machine design and test-contract preparation may proceed
without DMM results because they do not touch firmware, generated code, power,
or the board. Any firmware implementation, MCSDK hook, build record used as
adapter evidence, flash, Gate PWM output, Hall closed-loop claim, motor action,
or powered stage still needs later hardware evidence.

## State Machine Contract

| Rule | Contract |
| --- | --- |
| Input snapshot | Read three compact Hall bits from `PA0/PA1/PB4` as `HALL_A/HALL_B/HALL_C`. |
| Valid states | Accept only `001`, `010`, `011`, `100`, `101`, and `110` as candidate Hall states. |
| Illegal states | Reject `000` and `111`; increment an illegal-state counter and do not update accepted angle or speed. |
| First valid state | Store it as the first accepted state and timestamp; do not infer direction yet. |
| Repeated state | Do not count a new edge; optionally increment a repeated-state counter. |
| Adjacent transition | Count one accepted edge, update timestamp delta, and update the direction candidate. |
| Cross-state jump | Increment abnormal-jump counter; do not treat it as normal rotor movement. |
| Bounce candidate | If a future measured `min_edge_interval_us` threshold is violated, increment bounce counter and keep it out of normal speed estimation. |
| Raw versus accepted state | Keep `last_raw_state` separate from `last_accepted_state` so diagnostics can show noisy input without corrupting direction/speed candidates. |

No fixed debounce threshold is accepted in this document. The future threshold
must be derived from real no-power/powered observation records.

## Candidate Sequences

These sequences are exercise templates only. Real phase/Hall order must be
calibrated after hardware evidence and safe powered checks.

| Scenario | Input sequence | Expected result |
| --- | --- | --- |
| Forward candidate A | `001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001` | Each step is valid and adjacent; direction candidate is forward. |
| Reverse candidate A | `001 -> 011 -> 010 -> 110 -> 100 -> 101 -> 001` | Each step is valid and adjacent; direction candidate is reverse. |
| Illegal low | `000` | Count illegal state; do not update accepted angle or speed. |
| Illegal high | `111` | Count illegal state; do not update accepted angle or speed. |
| Repeated state | `001 -> 001` | Do not count a new accepted edge. |
| Cross-state jump | `001 -> 010` | Count abnormal jump; do not treat it as normal rotation. |
| Bounce candidate | `001 -> 101 -> 001` within a future documented minimum interval | Count suspicious bounce once timing evidence exists. |
| Unknown phase order | Any valid six-state loop with unknown physical direction | Report candidate direction only; wait for real phase/Hall calibration. |

## Debug Observables

A later low-frequency diagnostic path may expose these values after the
hardware gate and firmware boundary are opened:

| Observable | Meaning |
| --- | --- |
| `current_raw_state` | Latest three-bit snapshot from `PA0/PA1/PB4`. |
| `last_accepted_state` | Last valid Hall state accepted into the state machine. |
| `edge_count` | Accepted adjacent-transition count. |
| `illegal_state_count` | Count of `000` / `111` observations. |
| `abnormal_jump_count` | Count of valid but non-adjacent jumps. |
| `repeat_count` | Count of repeated state observations. |
| `bounce_candidate_count` | Count of edge intervals rejected by a future measured threshold. |
| `last_edge_dt_ticks` | Timestamp delta between accepted adjacent edges. |
| `direction_candidate` | Forward, reverse, unknown, or invalid candidate only. |
| `speed_candidate` | Candidate speed derived from edge timing; not a closed-loop proof. |

These debug values must be low-frequency diagnostics. They must not require
printing, JSON formatting, blocking delay, dynamic allocation, or control
decisions inside an EXTI or timer ISR.

## ISR Boundary

A later implementation must keep ISR work minimal:

- capture timestamp;
- capture raw Hall state;
- update only small counters or a ring-buffer/event flag if needed;
- defer decoding, logging, JSON, UART formatting, WebSocket work, and control
  decisions to a lower-priority context.

Forbidden in ISR: `printf`, JSON formatting/parsing, `HAL_Delay`, blocking
waits, dynamic allocation, complex MCSDK calls, or long control decisions.

## MCSDK Boundary

The next research item is to identify the MCSDK speed/position feedback entry
point without modifying the high-frequency FOC path.

Hard stop if the route requires invasive edits inside the generated current
loop, JEOC path, TIM1 PWM update path, or a timing-critical MCSDK ISR. In that
case, open a separate firmware-integration or hardware-rework review instead
of claiming Hall closed-loop readiness.

## Acceptance Checklist

- Explain why three Hall lines have six normal valid states, while `000` and
  `111` are illegal for this use.
- Draw the data flow:
  `state read -> validity check -> transition check -> timestamp -> direction/speed candidate`.
- Explain why `PA0/PA1/PB4` is software GPIO/EXTI Hall, not MCSDK standard
  `TIM2 Hall PA15/PB3/PB10`.
- Explain why `PB3=LIN1` means `PB3` is not available as current Hall.
- List the ISR forbidden operations and explain why they are not allowed in
  time-critical motor-control paths.

## Forbidden Claims

This document cannot be used to claim firmware implementation, runtime API
readiness, MCSDK Hall integration, build success, DMM continuity proof,
no-short proof, Gate PWM safety, Motor Profiler readiness, Hall closed-loop,
motor readiness, power-stage readiness, or sensorless validation.
