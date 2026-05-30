# 软件 Hall Adapter 固件入口方案 - 2026-05-28

Decision:
`Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.

本文把未来 `PA0/PA1/PB4` 软件 Hall adapter 的第一版固件入口形状写清楚。
它是 no-power 方案文档，不是 STM32 固件实现，不是 CubeMX / Workbench 修改，
不是 MCSDK 生成代码补丁，不是烧录记录，也不是硬件验证。

## 当前结论

当前路线保持不变：

```text
HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4
PB3 = LIN1，不参与 Hall
P14/P15 = 3V3/GND
```

MCSDK 标准 TIM2 Hall `PA15/PB3/PB10` 仍只是生成工程路线，不是当前 PCB2
软件 Hall 路线。

PCB2 仍未焊接完成，DMM 连续性 / 短路表暂缓。暂缓不是通过。

Workbench Debug build-only 已有本机编译证据，但它只证明生成工程能在本机
no-power 编译；它不证明 GPIO/EXTI 运行、Hall 闭环、Gate PWM、电机或功率级安全。

Safety boundary: No flash, no 24V, no power-board connection, no motor
connection, no Gate PWM output, no Motor Profiler run, no Motor Pilot run,
no Hall closed-loop claim, and no sensorless / SMO claim.
No Gate PWM output remains a hard boundary.

## 功能句

未来第一版软件 Hall adapter 只能做 debug-only 的状态采集和候选量计算：

```text
PA0/PA1/PB4 GPIO/EXTI captures raw Hall bits
-> EXTI ISR stores raw_state + timestamp + event counter only
-> low-priority state machine rejects illegal / repeat / bounce / abnormal jumps
-> debug snapshot exposes counters, direction_candidate, and speed_candidate
-> no MCSDK hook and no Hall closed-loop claim
```

一句话：先把三根 Hall 线读稳、判稳、记录清楚；先给人看 debug，不直接控制电机。

## 固件入口分层

| 层 | 未来职责 | 当前边界 |
| --- | --- | --- |
| GPIO/EXTI capture | 配置并读取 `PA0/PA1/PB4`，捕获变化事件 | 只允许未来方案；当前不写固件 |
| ISR event latch | 保存 `raw_state`、`timestamp_ticks`、轻量计数或 pending flag | ISR 内不做复杂判断 |
| state machine | 在低优先级上下文处理合法性、跳变、方向和速度候选 | debug-only，不闭环 |
| debug snapshot | 低频复制稳定字段给调试观察 | 不在 ISR 打印，不定义 UART 实现 |
| MCSDK boundary | 只保留接口研究结论和硬停止 | 不写 `HALL_M1`，不接 speed loop |

第一版候选文件名只能是未来建议，不代表已创建：

```text
software_hall_adapter.h/.c
software_hall_debug.h/.c
```

## 状态机规则

有效 Hall 状态只有六个：

```text
001, 010, 011, 100, 101, 110
```

`000` 和 `111` 是非法状态：三路 Hall 同时全低或全高，不符合三相 Hall
120 度错相的正常六步序列。出现时只计非法状态，不更新有效角度，不计合法边沿。

第一版状态机按这个顺序处理：

| 顺序 | 判断 | 结果 |
| --- | --- | --- |
| 1 | 读取 `PA0/PA1/PB4` 拼成三位 `raw_state` | 只记录原始值 |
| 2 | `000/111` | `illegal_state_count++`，不更新有效状态 |
| 3 | 第一次合法状态 | 只建立起点，不计边沿 |
| 4 | 重复状态 | `repeat_count++`，不计边沿 |
| 5 | 时间间隔过短 | `bounce_candidate_count++`，不声明高速旋转 |
| 6 | 正向相邻一步 | `edge_count++`，更新 `direction_candidate=forward` |
| 7 | 反向相邻一步 | `edge_count++`，更新 `direction_candidate=reverse` |
| 8 | 合法但非相邻跳变 | `abnormal_jump_count++`，不当正常旋转 |

候选正向序列：

```text
001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001
```

候选反向序列：

```text
001 -> 011 -> 010 -> 110 -> 100 -> 101 -> 001
```

真实正反方向名称必须等硬件焊接、电机和相序实测后校准。当前只能叫
`direction_candidate`。

## Debug 字段

第一版 debug snapshot 只允许这些低频观察量：

| 字段 | 含义 | 不能用来声明 |
| --- | --- | --- |
| `current_raw_state` | 最新三位原始 Hall 值 | GPIO 运行已可靠 |
| `last_accepted_state` | 上次通过规则的合法状态 | 机械角度已校准 |
| `last_decision` | 最近一次状态机判定 | 闭环控制可用 |
| `edge_count` | 合法相邻跳变计数 | 电机已经安全转动 |
| `illegal_state_count` | `000/111` 计数 | 接线错误已定位 |
| `repeat_count` | 重复状态计数 | Hall 无抖动 |
| `bounce_candidate_count` | 疑似抖动计数 | 抖动阈值已实测 |
| `abnormal_jump_count` | 跳码异常计数 | 相序已确认 |
| `lost_event_count` | 事件被覆盖或处理不及时计数 | 实时性已验证 |
| `last_edge_dt_ticks` | 最近合法边沿间隔 | 真实转速已校准 |
| `timestamp_source_id` | 时间戳来源标识 | timer 已配置 |
| `direction_candidate` | 方向候选 | 真实机械方向 |
| `speed_candidate` | 速度候选 | MCSDK 速度反馈 |

## ISR 边界

ISR 内允许：

- 读取或缓存 `PA0/PA1/PB4` 三位原始状态；
- 读取时间戳；
- 写一个小事件槽、pending flag 或轻量计数；
- 清 EXTI pending。

ISR 内禁止：

- `printf`；
- JSON / CSV / 文本格式化；
- UART transmit；
- `HAL_Delay`；
- 阻塞等待；
- 动态分配；
- WebSocket / ESP32 通信；
- 复杂 MCSDK 调用；
- 写入 MCSDK speed feedback；
- 修改 TIM1 PWM、JEOC、ADC injected 或 FOC 高频路径；
- 做最终方向、速度闭环或电流环控制决策。

## MCSDK 硬停止

以下动作不属于第一版 debug-only adapter，必须另开审查，不得在本方案内直接做：

- 修改 `hall_speed_pos_fdbk.c/.h`；
- 写入或替换 `HALL_M1`；
- 修改 `SpeednTorqCtrlM1`、速度 PID 或 `pSTC`；
- 把 `speed_candidate` 直接写进 MCSDK 速度环；
- 修改 `mc_tasks_foc.c`、JEOC / FOC ISR、ADC injected 路径；
- 修改 TIM1 PWM、互补 PWM、Break / BKIN、死区或 Gate 输出路径；
- 运行 Motor Profiler / Motor Pilot；
- 以 build-only 成功替代 DMM、Hall、Gate PWM、电机或功率级安全证据。

## 代码入口条件

未来真正写 STM32 adapter 代码前，至少必须满足：

| 条件 | 当前状态 |
| --- | --- |
| PCB2 已焊接完成 | 未满足 |
| DMM 连续性 / 短路表返回并通过 | 未满足，硬件侧暂缓 |
| `IA->PA0`、`IB->PA1`、`IC->PB4` 断电证据成立 | 未满足 |
| `PB3=LIN1`、`P14/P15=3V3/GND`、`nFAULT->PB12` 没有变更 | 当前按已确认约束记录 |
| GPIO 输入模式、上下拉、EXTI 触发策略明确 | 只有 no-power 草案 |
| 时间戳 timer 实例和 tick 分辨率明确 | 只有 no-power 草案 |
| 低频 debug 输出路线明确 | 只有 no-power 草案 |
| MCSDK 接入点如需使用，已有单独 review 和 rollback plan | 未满足 |
| no-power build-only 能复现 | 已有 2026-05-27 本机 Debug build-only 记录 |

## 现在可以做 / 不可以做

现在算法侧可以做：

- 审查本文和既有 host model / golden vectors；
- 维护 no-power 状态机规则、debug 字段、接口禁区；
- 等硬件焊好后用 DMM 表恢复入口检查；
- 在用户明确授权后，下一阶段再准备 debug-only adapter 代码草案。

现在算法侧不可以做：

- 修改 STM32 固件；
- 修改 MCSDK 生成代码；
- 修改 CubeMX / Workbench 配置；
- 烧录或 Run / Debug 实板；
- 接 24V、功率板电源或电机；
- 输出 Gate PWM；
- 运行 Motor Profiler / Motor Pilot；
- 声明 Hall 闭环可运行。

## 你现在需要做

你现在不需要测量，不需要补工具链，不需要接板子。

只需要做三件事：

1. 不要覆盖或重新生成
   `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`。
2. 问硬件同学 PCB2 预计什么时候焊完。
3. 如果 Hall 线、`PB3=LIN1`、`P14/P15=3V3/GND`、`nFAULT->PB12`
   任一项有变化，立刻同步。

硬件焊完后，先恢复 DMM 连续性 / 短路表；没焊好之前不做这一步。

## 禁止结论

本文不能用于声明：

- 不可声明 software Hall adapter 已实现；
- GPIO/EXTI runtime proof 已完成；
- MCSDK Hall 已接入；
- 不可声明 MCSDK hook 已完成；
- Hall 闭环可运行；
- DMM 已通过；
- Gate PWM 安全；
- 电机可接；
- 功率级可上电；
- Motor Profiler / Motor Pilot 可运行；
- No sensorless / SMO 已验证。
