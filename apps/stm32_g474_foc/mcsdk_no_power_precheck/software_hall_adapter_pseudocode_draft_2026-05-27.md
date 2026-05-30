# 软件 Hall Adapter 伪代码草案 - 2026-05-27

本文是算法侧 no-power 设计草案，用来把 2026-05-27 的 Hall 状态机 L2 概念证据推进到后续可实现的接口边界。

它不是固件实现，不是 MCSDK 集成，不是生成代码修改，不是构建记录，也不是硬件验证。
This is not firmware implementation, not MCSDK integration, and not hardware validation.

Decision: `Software Hall adapter pseudocode draft / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.

## 当前边界

当前 PCB2 路线保持不变：

```text
HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4
PB3 = LIN1，不参与 Hall
P14/P15 = 3V3/GND
```

PCB2 仍未焊接完成。DMM 连续性 / 短路表暂缓，不是通过。任何固件实现、GPIO/EXTI 实测、MCSDK 速度/位置反馈接入、编译证据、刷写、Gate PWM、24V、功率板、电机、Hall 闭环或无感结论都仍然关闭。

## 功能句

未来软件 Hall adapter 只做一件事：把 `PA0/PA1/PB4` 读到的三位 Hall 原始状态，整理成低频可诊断的状态机候选输出。

它当前只能输出候选信息：

- 当前原始 Hall 状态；
- 上一次接受的有效 Hall 状态；
- 合法边沿计数；
- 非法状态计数；
- 异常跳变计数；
- 重复状态计数；
- 最近一次合法边沿时间差；
- 方向候选；
- 速度候选。

这些都不是 Hall 闭环已经可运行的证据。

## 规则表

Decision order: illegal `000/111` -> repeated state -> forward/reverse adjacent transition -> abnormal jump.

| 输入情况 | 处理规则 | 是否更新 accepted state | 是否计合法边沿 |
| --- | --- | --- | --- |
| `000` / `111` | 非法 Hall 状态，计 `illegal_state_count` | 否 | 否 |
| 第一次读到有效状态 | 保存为 `last_accepted_state` | 是 | 否 |
| 与上次有效状态相同 | 重复状态，计 `repeat_count` | 否 | 否 |
| 正向相邻跳变 | 计合法边沿，方向候选为 forward | 是 | 是 |
| 反向相邻跳变 | 计合法边沿，方向候选为 reverse | 是 | 是 |
| 有效但非相邻跳变 | 计 `abnormal_jump_count` | 否 | 否 |
| 时间间隔过短 | 未来按实测阈值计 bounce candidate | 暂不定义 | 暂不定义 |

当前候选正向序列：

```text
001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001
```

当前候选反向序列：

```text
001 -> 011 -> 010 -> 110 -> 100 -> 101 -> 001
```

真实正反方向必须等硬件、电机和相序实测后校准。本文只保留 `direction_candidate`，不写死为真实机械正转。

## 函数职责

| 函数 / 模块候选 | 职责 | 禁止事项 |
| --- | --- | --- |
| `Hall_ReadRaw3()` | 未来读取 `PA0/PA1/PB4` 并拼成三位状态 | 不在本文实现 GPIO |
| `Hall_IsValidState(raw)` | 判断是否属于 `001/010/011/100/101/110` | 不接受 `000/111` |
| `Hall_IsForwardAdjacent(prev, cur)` | 判断是否符合候选正向相邻表 | 不声明真实正转 |
| `Hall_IsReverseAdjacent(prev, cur)` | 判断是否符合候选反向相邻表 | 不声明真实反转 |
| `Hall_CaptureEdge_ISR()` | ISR 中只采时间戳和原始状态，置事件标志或写轻量事件槽 | 不打印、不 JSON、不阻塞、不动态分配、不做控制决策 |
| `Hall_ProcessEvent()` | 低优先级上下文里执行合法性、重复、相邻、异常跳变判断 | 不改 MCSDK 高频 FOC ISR |
| `Hall_GetDebugSnapshot()` | 低频读取调试量 | 不在 ISR 格式化输出 |

## 状态数据草案

```c
// Pseudocode only. Not firmware source.
struct SoftHallContext {
    uint8_t current_raw_state;
    uint8_t last_raw_state;
    uint8_t last_accepted_state;
    bool has_accepted_state;

    uint32_t edge_count;
    uint32_t illegal_state_count;
    uint32_t abnormal_jump_count;
    uint32_t repeat_count;
    uint32_t bounce_candidate_count;

    uint32_t last_edge_ticks;
    uint32_t last_edge_dt_ticks;

    DirectionCandidate direction_candidate;  // unknown / forward / reverse / invalid
    SpeedCandidate speed_candidate;          // candidate only, not closed-loop proof
};
```

## ISR 伪代码

ISR 只允许做最小工作。复杂判断放到低优先级任务或主循环。

```c
// Pseudocode only. Not firmware source.
void Hall_CaptureEdge_ISR(void)
{
    uint32_t now_ticks = Read_Timer_Ticks();
    uint8_t raw_state = Hall_ReadRaw3_PA0_PA1_PB4();

    hall_event.raw_state = raw_state;
    hall_event.timestamp_ticks = now_ticks;
    hall_event.pending = true;
    hall_irq_event_count++;

    // Forbidden here:
    // printf, JSON, HAL_Delay, blocking wait, malloc/free,
    // MCSDK control calls, speed-loop decisions, FOC-loop edits.
}
```

## 低优先级处理伪代码

```c
// Pseudocode only. Not firmware source.
HallDecision Hall_ProcessEvent(SoftHallContext *ctx, HallEvent event)
{
    uint8_t raw = event.raw_state;
    uint32_t now = event.timestamp_ticks;

    ctx->last_raw_state = ctx->current_raw_state;
    ctx->current_raw_state = raw;

    if (!Hall_IsValidState(raw)) {
        ctx->illegal_state_count++;
        ctx->direction_candidate = DIRECTION_INVALID;
        return HALL_DECISION_ILLEGAL_STATE;
    }

    if (!ctx->has_accepted_state) {
        ctx->last_accepted_state = raw;
        ctx->last_edge_ticks = now;
        ctx->has_accepted_state = true;
        ctx->direction_candidate = DIRECTION_UNKNOWN;
        return HALL_DECISION_FIRST_VALID_STATE;
    }

    if (raw == ctx->last_accepted_state) {
        ctx->repeat_count++;
        return HALL_DECISION_REPEAT_STATE;
    }

    uint32_t dt = now - ctx->last_edge_ticks;

    if (Hall_MinEdgeInterval_IsDefined() && dt < Hall_GetMinEdgeIntervalTicks()) {
        ctx->bounce_candidate_count++;
        return HALL_DECISION_BOUNCE_CANDIDATE;
    }

    if (Hall_IsForwardAdjacent(ctx->last_accepted_state, raw)) {
        ctx->last_edge_dt_ticks = dt;
        ctx->last_edge_ticks = now;
        ctx->last_accepted_state = raw;
        ctx->edge_count++;
        ctx->direction_candidate = DIRECTION_FORWARD_CANDIDATE;
        ctx->speed_candidate = Hall_MakeSpeedCandidate(dt);
        return HALL_DECISION_FORWARD_ADJACENT;
    }

    if (Hall_IsReverseAdjacent(ctx->last_accepted_state, raw)) {
        ctx->last_edge_dt_ticks = dt;
        ctx->last_edge_ticks = now;
        ctx->last_accepted_state = raw;
        ctx->edge_count++;
        ctx->direction_candidate = DIRECTION_REVERSE_CANDIDATE;
        ctx->speed_candidate = Hall_MakeSpeedCandidate(dt);
        return HALL_DECISION_REVERSE_ADJACENT;
    }

    ctx->abnormal_jump_count++;
    ctx->direction_candidate = DIRECTION_INVALID;
    return HALL_DECISION_ABNORMAL_JUMP;
}
```

## 相邻跳变表

```text
Forward candidate:
001 -> 101
101 -> 100
100 -> 110
110 -> 010
010 -> 011
011 -> 001

Reverse candidate:
001 -> 011
011 -> 010
010 -> 110
110 -> 100
100 -> 101
101 -> 001
```

## 调试量草案

| 字段 | 含义 | 当前证据等级 |
| --- | --- | --- |
| `current_raw_state` | 最新三位 Hall 原始状态 | 设计草案 |
| `last_accepted_state` | 最近一次被状态机接受的有效状态 | 设计草案 |
| `edge_count` | 合法相邻跳变计数 | 设计草案 |
| `illegal_state_count` | `000/111` 次数 | 设计草案 |
| `abnormal_jump_count` | 有效但非相邻跳变次数 | 设计草案 |
| `repeat_count` | 重复状态次数 | 设计草案 |
| `bounce_candidate_count` | 未来按实测阈值过滤的抖动候选次数 | 设计草案 |
| `last_edge_dt_ticks` | 最近两次接受边沿的时间差 | 设计草案 |
| `direction_candidate` | 方向候选，不是真实方向证明 | 设计草案 |
| `speed_candidate` | 速度候选，不是闭环速度证明 | 设计草案 |

## MCSDK 接入硬停止

后续研究 MCSDK 接入点时，必须先找速度/位置反馈接口，不允许直接改高频 FOC 路径。

硬停止条件：

- 需要改 JEOC / FOC ISR；
- 需要改 TIM1 PWM 更新路径；
- 需要在中断里调用复杂 MCSDK 控制函数；
- 需要把候选速度直接写入闭环速度反馈而没有接口审查；
- 需要以 build success 代替 Hall、Gate PWM、电机或功率级安全证据。

遇到以上任一情况，必须开新的 firmware-integration review 或 hardware-rework review，不能声明 Hall 闭环可运行。

## 后续开代码条件

本文不允许立即写固件。未来进入源码阶段之前至少需要：

1. PCB2 元器件焊接完成；
2. DMM 连续性 / 短路表返回并通过审查；
3. 明确 `PA0/PA1/PB4` 的 GPIO/EXTI 初始化边界；
4. 明确时间戳来源；
5. 明确调试输出只走低频路径；
6. 明确 MCSDK 接入点，或先保持完全独立的 adapter 单元测试边界；
7. 通过 no-power build-only 闸门后仍不触发 Gate PWM、不刷写实板、不接电机。

## 用户检查点

下一次学习或代码前，先复核这三件事：

1. 按顺序说出状态机判断流程：非法态 -> 重复态 -> 正/反相邻态 -> 异常跳变。
2. 判断 `100 -> 110`、`100 -> 101`、`100 -> 011`、`000`、`111`。
3. 解释为什么 `PB3=LIN1` 后不能再拿来做 Hall。

## 禁止结论

本文不能用于声明：

- No software Hall adapter implementation is claimed.
- 软件 Hall adapter 已实现；
- MCSDK Hall 已接入；
- Hall 闭环可运行；
- Motor Profiler 可以运行；
- DMM 已通过；
- Gate PWM 安全；
- 电机可接；
- 功率级可上电；
- 24V 可接；
- No sensorless / SMO validation is claimed.
