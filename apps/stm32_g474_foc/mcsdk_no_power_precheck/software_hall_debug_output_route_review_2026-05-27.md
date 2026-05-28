# 软件 Hall Low-Frequency Debug-Output Route 审查草案 - 2026-05-27

Decision:
`Software Hall low-frequency debug-output route review draft / no firmware implementation / no UART implementation / no Hall readiness`.

本文只审查未来 `PA0/PA1/PB4` 软件 Hall adapter 的低频调试输出边界。
它不是固件实现，不是 UART 实现，不是 JSON 协议实现，不是 ESP32 网关实现，
不是构建记录，也不是硬件验证。

## 当前边界

当前 PCB2 路线保持不变：

```text
HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4
PB3 = LIN1，不参与 Hall
P14/P15 = 3V3/GND
```

PCB2 仍未焊接完成，DMM 连续性 / 短路表暂缓。暂缓不是通过。

Safety boundary: No 24V, no power-board connection, no motor connection,
no Gate PWM output, no Motor Profiler run, no Motor Pilot run, no Hall
closed-loop claim, and no sensorless / SMO claim.

## 功能句

未来 debug-output 层只允许低频查看状态机结果，不允许参与实时控制：

```text
EXTI ISR captures raw_state + timestamp only
-> low-priority state machine updates counters and candidates
-> debug snapshot copies stable fields at a low rate
-> optional output route prints or transports the snapshot outside ISR
```

它不能在 ISR 打印，不能把 JSON 放进 FOC 高频路径，不能把 debug 字段直接写入
MCSDK speed feedback，不能证明 Hall 闭环可运行。

## 一句话解释

低频 debug snapshot 就像“仪表盘”，只给人看当前状态和计数。
它不是“油门”，不能用来控制电机，也不能放到中断里边算边打印。

## Debug 字段草案

| 字段 | 含义 | 当前边界 |
| --- | --- | --- |
| `current_raw_state` | 最新读到的三位 Hall 原始值 | 可记录，不能当闭环证明 |
| `last_accepted_state` | 上一次通过合法性和跳变规则的状态 | 可记录，真实相序仍待实测 |
| `last_decision` | 最近一次状态机判定结果 | 只能是 debug 结果 |
| `edge_count` | 合法相邻跳变计数 | 不能证明电机已转 |
| `illegal_state_count` | `000/111` 计数 | 用于发现接线/电平异常候选 |
| `repeat_count` | 重复状态计数 | 不计合法边沿 |
| `bounce_candidate_count` | 时间过短的抖动候选计数 | 阈值未实测前只叫候选 |
| `abnormal_jump_count` | 合法但非相邻跳变计数 | 不直接当正常旋转 |
| `lost_event_count` | 事件槽被覆盖或处理不及时的候选计数 | 仅用于诊断，不是硬件证明 |
| `last_edge_dt_ticks` | 最近一次合法边沿间隔 | 来自已审查时间戳来源，仍是候选 |
| `timestamp_source_id` | 时间戳来源标识 | exact timer 未定前只保留字段草案 |
| `direction_candidate` | 方向候选 | 不是真实机械方向证明 |
| `speed_candidate` | 速度候选 | 不能写入 MCSDK 闭环 |

## 输出路线规则表

| 路线 | 当前结论 | 原因 |
| --- | --- | --- |
| host-side Python tests | 当前已可用 | 只跑在 PC 上，不读 GPIO，不碰硬件 |
| debugger watch / memory snapshot | 未来首选观察方式之一 | 不占 UART，不要求 ISR 打印，但仍需要固件实现后才存在 |
| low-priority main-loop snapshot copy | 未来允许的实现形状 | 由低优先级上下文复制字段，不能在 ISR 格式化 |
| UART text / CSV / JSON | 当前不实现，只能后续单独审查 | `PA2/PA3` 是 P1 VCP 路径且默认不作为 FOC UART，生成工程 USART2 / ASPEP / MCP 也不是软件 Hall debug clearance |
| ESP32 / WebSocket display | 当前不实现，只能作为后续网关显示 | ESP32 不进入 STM32 FOC 实时控制环 |
| SWO / ITM | 当前不采用 | `PB3=LIN1`，不能把 SWO 当成当前 debug 出口 |
| every-edge streaming | 禁止作为第一版 | 每个 Hall 边沿都打印/发包会引入实时风险 |

## 频率边界

未来如果 firmware-entry review 允许输出 debug，第一版目标只能是低频人类可读：

```text
default review target: 1 Hz to 10 Hz snapshot
not every EXTI edge
not in JEOC / FOC ISR
not in EXTI ISR formatting path
```

这里的 `1 Hz to 10 Hz` 是审查目标，不是已经配置的任务频率。

## ISR 禁止清单

未来无论选哪条输出路线，ISR 内仍然禁止：

- `printf`；
- JSON 解析或格式化；
- CSV / 文本格式化；
- UART transmit；
- WebSocket / ESP32 通信；
- `HAL_Delay`；
- 阻塞等待；
- 动态分配；
- 复杂 MCSDK 调用；
- 写入 MCSDK speed feedback；
- 修改 TIM1 PWM、JEOC、ADC injected 或 FOC 高频路径；
- 做最终方向、速度闭环或电流环控制决策。

## Snapshot 草案

```c
// Pseudocode only. Not firmware source.
struct SoftHallDebugSnapshot {
    uint8_t current_raw_state;
    uint8_t last_accepted_state;
    uint8_t last_decision;
    uint32_t edge_count;
    uint32_t illegal_state_count;
    uint32_t repeat_count;
    uint32_t bounce_candidate_count;
    uint32_t abnormal_jump_count;
    uint32_t lost_event_count;
    uint32_t last_edge_dt_ticks;
    uint8_t timestamp_source_id;
    uint8_t direction_candidate;
    uint32_t speed_candidate;
};
```

这仍然不是 STM32 固件源文件，也不是运行时 API。

## 当前未决定

- 是否输出到 UART；
- 如果输出到 UART，使用哪个外设和引脚；
- 是否复用 MCSDK USART2 / ASPEP / MCP；
- 是否需要 ESP32 显示；
- 输出格式是 text、CSV 还是 JSON；
- 低频输出任务频率；
- snapshot 的并发保护方式；
- no-power build-only 结果。

## 当前硬停止

以下任意情况出现，不能把本草案升级成 UART / debug 固件实现：

- PCB2 未焊接；
- DMM 连续性 / 短路表未返回；
- GPIO/EXTI 边界仍只是 no-power 草案；
- timestamp source 仍只是 no-power 草案；
- 需要在 ISR 里 `printf`、JSON、UART transmit 或 WebSocket；
- 需要复用 `PA2/PA3` 作为 FOC UART 但没有新审查；
- 需要直接复用 MCSDK USART2 / ASPEP / MCP 但没有新审查；
- 需要使用 `PB3` / SWO 作为 debug 出口；
- 需要把 `speed_candidate` 写入 `HALL_M1`、`SpeednTorqCtrlM1` 或 MCSDK 速度环；
- 需要修改 TIM1 PWM、JEOC、ADC injected 或 FOC 高频路径；
- 需要以 debug 输出替代 Hall、Gate PWM、电机或功率级安全证据。

## 当前可以声明

- 已有 no-power low-frequency debug-output route review draft；
- 未来 debug snapshot 字段已有草案；
- 第一版输出必须是低频 snapshot，不是 every-edge streaming；
- ISR 内不允许打印、JSON、UART transmit、WebSocket 或阻塞；
- `PA2/PA3`、MCSDK USART2 / ASPEP / MCP、ESP32、SWO 都没有被本草案直接授权。

## 当前不可声明

- 不可声明 software Hall adapter 已实现；
- 不可声明 debug-output firmware 已实现；
- 不可声明 UART debug 已实现；
- 不可声明 GPIO/EXTI runtime proof 已完成；
- 不可声明 no-power build 已通过；
- 不可声明 MCSDK Hall 已接入；
- 不可声明 Hall 闭环可运行；
- 不可声明 Gate PWM 安全；
- 不可声明电机可接；
- 不可声明功率级可上电；
- 不可声明 Motor Profiler / Motor Pilot 可运行；
- 不可声明 sensorless / SMO 已验证。

## 下一步

算法侧下一步仍然不是写固件。下一步可选工作是 separate MCSDK
firmware-integration review：只读研究如果未来要把软件 Hall 候选接到 MCSDK，
需要哪些接口证据、哪些文件禁止碰、哪些条件必须先满足。

## MCSDK Follow-Up

The next MCSDK firmware-integration boundary draft now exists at software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md. It is still no-power boundary evidence only, not a MCSDK hook and not firmware implementation.
