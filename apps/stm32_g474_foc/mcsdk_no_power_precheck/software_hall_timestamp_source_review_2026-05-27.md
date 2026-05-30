# 软件 Hall Timestamp Source 审查草案 - 2026-05-27

Decision:
`Software Hall timestamp-source review draft / no firmware implementation / no timer configuration / no Hall readiness`.

本文只审查未来 `PA0/PA1/PB4` 软件 Hall adapter 的边沿时间戳来源边界。
它不是固件实现，不是 CubeMX / Workbench 修改，不是 timer 配置，不是构建记录，
也不是硬件验证。

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

未来软件 Hall 时间戳层只允许提供“边沿发生在什么时候”的原始事实：

```text
EXTI event on PA0/PA1/PB4
-> read timestamp_ticks from an isolated free-running source
-> store raw_state + timestamp_ticks + lightweight event count
-> low-priority state machine computes dt candidate later
```

它不能直接写 MCSDK speed feedback，不能替换 `HALL_M1`，不能证明 Hall 闭环可运行。

## 一句话解释

Hall 边沿时间戳不是“控制电机”的东西，它只是给状态机一个尺子：
上一条边沿和这一条边沿间隔多久。这个间隔以后可以形成 `speed_candidate`，
但在当前 P2 no-power 阶段不能拿它接管 MCSDK 闭环。

## 只读线索来源

本轮只读检查了以下本地线索：

- `software_hall_gpio_exti_boundary_review_2026-05-27.md`;
- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/main.c`;
- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/QIANSAI_G474_STDRIVE101_FOC_P2.ioc`;
- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/parameters_conversion.h`;
- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/mc_config.c`;
- 本地 HAL `stm32g4xx_hal.c` / `stm32g4xx_hal.h`;
- 本地 CMSIS `stm32g474xx.h`。

## 候选来源规则表

| 来源 | 本地线索 | 当前结论 |
| --- | --- | --- |
| `TIM1` | 生成工程中 `MX_TIM1_Init()`、`TIM1_UP_TIM16_IRQn`、`ADC_EXTERNALTRIGINJEC_T1_TRGO`、PWM / ADC injected / FOC timing 线索同时存在 | 硬禁止。`TIM1` 属于 PWM、电流采样和 FOC 高频路径，不作为软件 Hall 时间戳来源 |
| `TIM2` | 生成工程中 `MX_TIM2_Init()`、`HAL_TIMEx_HallSensor_Init(&htim2, ...)`，`.ioc` 记录 `M1_HALL_TIMER_SELECTION=HALL_TIM2` | 当前硬停止。`TIM2` 是 MCSDK 标准硬件 Hall 路线线索，不匹配当前 PCB2 `PA0/PA1/PB4` 软件 Hall |
| `HAL_GetTick()` / SysTick | 本地 HAL 中 `uwTickFreq = HAL_TICK_FREQ_DEFAULT; /* 1KHz */`，`HAL_GetTick()` 返回 `uwTick` | 只适合粗略日志 / 超时，不适合作为 Hall edge speed candidate 时间戳 |
| DWT / `CYCCNT` | 可作为后续调试候选，但当前没有启用、冻结、低功耗和发布策略 | 只列为调试候选，不作为默认运行依赖 |
| dedicated free-running timer | 当前生成工程未给软件 Hall 分配独立 timer；本地 CMSIS/HAL 可见通用 timer 线索，但未做实例选择 | 首选类别，但 exact timer instance / prescaler / overflow policy 仍待后续 firmware-entry review |

## 推荐边界

如果未来所有入口条件满足，软件 Hall adapter 的时间戳来源应优先使用：

```text
dedicated free-running timer
-> 1 us tick design target
-> read counter in EXTI ISR
-> compute dt later with unsigned delta
-> no update IRQ required for the first draft
```

这里的 `1 us tick` 只是设计审查目标，不是已经配置的 timer。
`unsigned delta` 的意思是用无符号减法处理计数器回绕，例如：

```c
// Pseudocode only. Not firmware source.
uint32_t dt_ticks = (uint32_t)(current_ticks - previous_ticks);
```

## 选择标准

未来选择 exact timer 前必须同时满足：

- 与 `TIM1` PWM / ADC injected / JEOC / FOC 高频路径隔离；
- 不复用 `TIM2` 标准 MCSDK Hall / `HALL_M1` 路线；
- 分辨率足够记录 Hall 边沿间隔，草案目标为 `1 us tick`；
- 溢出策略能用 `unsigned delta` 审查；
- EXTI ISR 只读 counter，不启动阻塞等待；
- 不依赖 `printf`、JSON、`HAL_Delay`、动态分配或复杂 MCSDK 调用；
- 不在 ISR 里做方向最终判定、速度闭环或电流环控制决策。

## 事件数据更新

GPIO/EXTI 事件槽草案增加时间戳来源标识：

```c
// Pseudocode only. Not firmware source.
struct SoftHallExtiEvent {
    uint8_t raw_state;             // PA0/PA1/PB4 packed into 3 bits
    uint32_t timestamp_ticks;      // read from reviewed timestamp source
    uint8_t timestamp_source_id;   // documents which source produced ticks
    uint32_t irq_count;            // lightweight diagnostic counter
    bool pending;                  // single-slot draft only
};
```

这仍然不是 STM32 固件源文件，也不是运行时 API。

## 当前未决定

- exact timer instance；
- timer clock tree；
- prescaler / period；
- overflow period；
- debug freeze 策略；
- 是否允许 DWT 调试候选；
- 是否需要多事件 ring buffer；
- 与 MCSDK scheduler 的关系；
- no-power build-only 结果。

## 当前硬停止

以下任意情况出现，不能把本草案升级成 timer 配置或固件实现：

- PCB2 未焊接；
- DMM 连续性 / 短路表未返回；
- GPIO/EXTI 边界仍只是 no-power 草案；
- exact timer instance 未经过 firmware-entry review；
- 需要占用 `TIM1`；
- 需要直接复用 `TIM2` / `HALL_M1`；
- 需要修改 `hall_speed_pos_fdbk.c/.h`、`SpeednTorqCtrlM1` 或 MCSDK 速度环；
- 需要修改 TIM1 PWM、JEOC、ADC injected 或 FOC 高频路径；
- 需要以编译通过替代 Hall、Gate PWM、电机或功率级安全证据。

## 当前可以声明

- 已有 no-power timestamp-source review draft；
- `TIM1` 不作为软件 Hall timestamp source；
- `TIM2` 当前不能直接作为 `PA0/PA1/PB4` 软件 Hall timestamp source；
- `HAL_GetTick()` / SysTick 只适合粗略日志，不适合作为 Hall edge speed candidate；
- 未来首选类别是隔离的 `dedicated free-running timer`；
- `timestamp_ticks` 后续必须用 `unsigned delta` 处理回绕。

## 当前不可声明

- 不可声明 software Hall adapter 已实现；
- 不可声明 timer configuration 已完成；
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

算法侧下一步仍然不是写固件。low-frequency debug-output route review draft
已新增；下一步可选工作是 separate MCSDK firmware-integration review：只读研究
如果未来要把软件 Hall 候选接到 MCSDK，需要哪些接口证据、哪些文件禁止碰、
哪些条件必须先满足。
