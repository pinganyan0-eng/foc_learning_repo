# 软件 Hall GPIO/EXTI 边界审查草案 - 2026-05-27

Decision:
`Software Hall GPIO/EXTI boundary review draft / no firmware implementation / no GPIO runtime proof / no Hall readiness`.

本文把未来 `PA0/PA1/PB4` 软件 Hall adapter 的 GPIO/EXTI 边界先审清楚。
它不是固件实现，不是 CubeMX / Workbench 修改，不是构建记录，也不是硬件验证。

## 当前边界

当前 PCB2 路线保持不变：

```text
HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4
PB3 = LIN1，不参与 Hall
P14/P15 = 3V3/GND
```

PCB2 仍未焊接完成，DMM 连续性 / 短路表暂缓。暂缓不是通过。

## 功能句

未来 GPIO/EXTI 层只允许做输入采样和事件捕获：

```text
PA0/PA1/PB4 configured as Hall input candidates
-> EXTI captures change events
-> ISR stores raw_state + timestamp + pending/event count
-> lower-priority Hall state machine consumes the event
```

它不能直接接入 MCSDK Hall，不能替换 `HALL_M1`，不能证明 Hall 闭环可运行。
简写为：不替换 `HALL_M1`，不写 MCSDK speed feedback，不碰 FOC 高频路径。

## 已有静态线索

| 项目 | 静态线索 | 当前结论 |
| --- | --- | --- |
| `PA0` | 项目 pin-function 记录为 `GPIO_EXTI0`, `TIM2_CH1` | 可作为软件 Hall 输入候选，不是当前闭环证据 |
| `PA1` | 项目 pin-function 记录为 `GPIO_EXTI1`, `TIM2_CH2` | 可作为软件 Hall 输入候选，不是当前闭环证据 |
| `PB4` | 项目 pin-function 记录为 `GPIO_EXTI4`, `TIM3_CH1` | 可作为软件 Hall 输入候选，但不是 `TIM2_CH3` |
| `PA0/PA1/PB4` 组合 | 分散在 `EXTI0/EXTI1/EXTI4`，不是同一个 TIM2 Hall 三通道组合 | 只能先按软件 GPIO/EXTI Hall 处理 |
| `PB3` | 当前 PCB2 固定为 `LIN1` | 不能作为当前 Hall 输入 |
| MCSDK TIM2 Hall | Workbench / generated clue使用 `PA15/PB3/PB10` | 不匹配当前 PCB2 Hall 路线 |

静态线索来源：

- `current_pcb2_hall_pwm_strategy_2026-05-19.md`;
- `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md`;
- `software_hall_adapter_design_review_2026-05-19.md`;
- 本地 CMSIS `stm32g474xx.h` 中的 `EXTI0_IRQn`、`EXTI1_IRQn`、`EXTI4_IRQn`；
- 本地 HAL `stm32g4xx_hal_gpio.h` 中的 `GPIO_MODE_IT_RISING_FALLING`、
  `GPIO_NOPULL`、`GPIO_PULLUP`、`GPIO_PULLDOWN`。

## GPIO 输入边界

未来代码如果被授权，GPIO 层只允许定义这些东西：

| 项目 | 候选边界 | 当前状态 |
| --- | --- | --- |
| 输入 pin | `PA0`, `PA1`, `PB4` | 静态线索成立，DMM 未通过 |
| 输入模式 | `GPIO_MODE_IT_RISING_FALLING` 是候选 | 只作为草案，不写代码 |
| 上拉/下拉 | `GPIO_NOPULL` / `GPIO_PULLUP` / `GPIO_PULLDOWN` 待硬件电路确认 | 未决 |
| 电平有效性 | 只读取 0/1，不在 GPIO 层解释方向 | 已定 |
| 去抖 | 不在 GPIO 初始化层硬编码阈值 | 已定 |
| 默认状态 | 上电前不声明，第一次合法 Hall 值只作为起点 | 已定 |

上拉/下拉不能靠猜。需要硬件原理图或实测确认 Hall 输出类型、外部上拉、
滤波、电源和输入保护之后再定。

## EXTI 边界

未来代码如果被授权，EXTI 层只允许捕获变化，不允许做状态机闭环：

| EXTI line | Pin | IRQ clue | 边界 |
| --- | --- | --- | --- |
| `EXTI0` | `PA0` | `EXTI0_IRQn` | 捕获 `HALL_A` 候选变化 |
| `EXTI1` | `PA1` | `EXTI1_IRQn` | 捕获 `HALL_B` 候选变化 |
| `EXTI4` | `PB4` | `EXTI4_IRQn` | 捕获 `HALL_C` 候选变化 |

允许的 ISR 责任：

- 读取当前 `PA0/PA1/PB4` 三位；
- 读取时间戳；
- 写入一个轻量事件槽或 pending flag；
- 增加轻量 IRQ 计数；
- 清对应 EXTI pending。

禁止的 ISR 行为：

- `printf`；
- JSON 解析或格式化；
- `HAL_Delay`；
- 阻塞等待；
- 动态分配；
- WebSocket / ESP32 通信；
- 复杂 MCSDK 调用；
- 修改 TIM1 PWM 更新路径；
- 修改 JEOC / FOC ISR；
- 写入 MCSDK 速度环；
- 做最终方向、速度闭环或电流环控制决策。

## 事件数据边界

GPIO/EXTI 层输出给低优先级状态机的事件最多包含：

```c
// Pseudocode only. Not firmware source.
struct SoftHallExtiEvent {
    uint8_t raw_state;          // PA0/PA1/PB4 packed into 3 bits
    uint32_t timestamp_ticks;   // timestamp source remains TBD
    uint32_t irq_count;         // lightweight diagnostic counter
    bool pending;               // single-slot draft only
};
```

本草案不决定：

- 时间戳使用哪一个 timer；
- tick 频率；
- 溢出处理；
- 多事件缓冲深度；
- 是否需要 DMA 或环形队列；
- 是否和 MCSDK 调度器交互。

timestamp-source review 和 debug-output route review 已新增为独立草案，但仍不是
timer、UART 或固件实现。剩余未决项必须进入后续 firmware-integration review。

## 低优先级状态机边界

GPIO/EXTI 层不做 Hall 状态机。低优先级状态机继续沿用已有 no-power 规则：

- 拒绝 `000/111`；
- 第一次合法状态只当起点；
- 重复状态不计边沿；
- 太快变化先记 bounce candidate；
- 正/反向相邻一步才计合法边沿；
- 合法但非相邻跳变计异常；
- 方向只叫 `direction_candidate`；
- 速度只叫 `speed_candidate`。

## 当前硬停止

以下任意情况出现，不能把本草案升级成固件实现：

- PCB2 未焊接；
- DMM 连续性 / 短路表未返回；
- 上拉/下拉电路未确认；
- 时间戳来源未确认；
- debug 输出路径未确认；
- no-power build-only 工具链和构建记录缺失；
- 需要修改 `HALL_M1`、`hall_speed_pos_fdbk.c/.h`、`SpeednTorqCtrlM1`；
- 需要修改 TIM1 PWM、JEOC、ADC injected 或 FOC 高频路径；
- 需要以编译通过替代 Hall、Gate PWM、电机或功率级安全证据。

## 当前结论

当前可以声明：

- 已有 no-power GPIO/EXTI boundary review draft；
- `PA0/PA1/PB4` 可作为软件 Hall 输入候选；
- `EXTI0/EXTI1/EXTI4` 是未来边沿捕获候选；
- `PB3=LIN1` 不进入当前 Hall；
- MCSDK 标准 TIM2 Hall 不等于当前 PCB2 Hall。

当前不可声明：

- 不可声明 software Hall adapter 已实现；
- 不可声明 GPIO/EXTI runtime proof 已完成；
- 不可声明 DMM 已通过；
- 不可声明 no-power build 已通过；
- 不可声明 MCSDK Hall 已接入；
- 不可声明 Hall 闭环可运行；
- 不可声明 Gate PWM 安全；
- 不可声明电机可接；
- 不可声明功率级可上电；
- 不可声明 Motor Profiler / Motor Pilot 可运行；
- 不可声明 sensorless / SMO 已验证。

## 下一步

算法侧下一步仍然不是写固件。timestamp-source review draft 和 debug-output
route review draft 已新增；下一步可选工作是 separate MCSDK firmware-integration
review：只读研究如果未来要把软件 Hall 候选接到 MCSDK，需要哪些接口证据、
哪些文件禁止碰、哪些条件必须先满足。
