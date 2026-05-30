# Software Hall Adapter Processing-Order Card - 2026-05-27

Decision:
`Software Hall adapter processing-order teaching card / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.

This is a Chinese-first learning and design-boundary card for the future
software Hall adapter. It is not firmware source, not generated MCSDK code, not
a build record, and not hardware validation.

## 当前工程前提

- 当前阶段：`P2 no-power`.
- 当前 PCB2 还未焊接，DMM 连续性 / 短路表暂缓，暂缓不是通过。
- 当前 Hall 路线：`HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- 固定约束：`PB3 = LIN1`; PB3 不参与当前 Hall。
- MCSDK 标准 TIM2 Hall `PA15/PB3/PB10` 不等于当前 PCB2 Hall 路线。

## 一句话版本

先读原始 Hall 三位，再把明显错误和无意义情况拦掉，最后才判断它是
正向一步、反向一步，还是异常跳码。

```text
raw read -> illegal-state check -> first-valid check -> repeated-state check
-> bounce/timing check -> forward/reverse adjacent check -> abnormal-jump count
```

## 为什么必须这个顺序

| Step | 中文名字 | 目的 | 如果跳过会怎样 |
| --- | --- | --- | --- |
| `raw read` | 读原始三位 | 从 `PA0/PA1/PB4` 读到 `000..111` 之一 | 没有输入，后面无法判断 |
| `illegal-state check` | 先查非法态 | 拦掉 `000/111` | 错误信号可能被当成角度或速度 |
| `first-valid check` | 第一次合法值只定起点 | 第一次读到 `100` 只能记住 | 没有上一个状态时会误算一次边沿 |
| `repeated-state check` | 重复状态不计边沿 | `100 -> 100` 不是转子走一步 | 边沿数和速度会虚高 |
| `bounce/timing check` | 太快先怀疑抖动 | 极短时间反复跳变可能是噪声 | 抖动会被误判成高速旋转 |
| `forward/reverse adjacent check` | 判断正反向相邻一步 | `100 -> 110` 正向，`100 -> 101` 反向 | 不知道方向，也无法估速度 |
| `abnormal-jump count` | 记录跳码异常 | `100 -> 011` 不是相邻状态 | 跳过中间状态会被误当正常旋转 |

## 规则拆开看

### 1. `raw read`

软件 Hall adapter 未来只应该从 `PA0/PA1/PB4` 读三位输入，例如：

```text
PA0 PA1 PB4 -> raw_state
0   0   1   -> 001
1   0   0   -> 100
```

这个步骤只得到事实，不做方向判断。

### 2. `illegal-state check`

只接受六个有效状态：

```text
001, 010, 011, 100, 101, 110
```

拒绝：

```text
000, 111
```

原因：三路 Hall 在正常电角度六步换相区间里，不应该三路同时全 0 或全
1。出现 `000/111` 时，先记 `illegal_state_count++`，不要更新有效角度，
不要算速度。

### 3. `first-valid check`

第一次读到合法值时，只能建立基准：

```text
last_state = 100
has_last_state = true
edge_count 不增加
```

原因：边沿必须比较“上一次”和“这一次”。第一次没有上一次，所以不能说它
已经转了一步。

### 4. `repeated-state check`

如果读到：

```text
100 -> 100
```

这是重复采样，不是新边沿。可以记录 `repeat_count++`，但不要更新速度，
不要增加正常边沿数。

### 5. `bounce/timing check`

如果状态变化合法，但时间间隔极短，例如：

```text
100 -> 110 -> 100
```

且两次边沿间隔短到不符合实际电机速度，就先记为抖动候选。当前没有实测，
所以本卡不接受固定阈值。阈值必须等后续硬件、定时器 tick、实际转速范围
和日志证据一起决定。

### 6. `forward/reverse adjacent check`

当前候选正向序列：

```text
001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001
```

当前候选反向序列：

```text
001 -> 011 -> 010 -> 110 -> 100 -> 101 -> 001
```

所以：

```text
100 -> 110 = 正向相邻一步
100 -> 101 = 反向相邻一步
```

这只能叫“方向候选”。真实正反向名称要等电机实测和相序校准后确认。

### 7. `abnormal-jump count`

两个状态都合法，但不是相邻状态，例如：

```text
100 -> 011
```

这不是正常一步，而是跳码。处理方式：

```text
abnormal_jump_count++;
不要当正常旋转;
不要直接更新速度候选;
```

## 伪代码边界

```c
raw = Hall_ReadRaw3();       // only read PA0/PA1/PB4
now = ReadTimestampTicks();  // timer source is still a future decision

if (!Hall_IsValidState(raw)) {
    illegal_state_count++;
    return;
}

if (!has_last_valid_state) {
    last_state = raw;
    has_last_valid_state = true;
    last_edge_time = now;
    return;
}

if (raw == last_state) {
    repeat_count++;
    return;
}

dt = now - last_edge_time;
if (Hall_IsBounceCandidate(dt)) {
    bounce_candidate_count++;
    return;
}

if (Hall_IsForwardAdjacent(last_state, raw)) {
    direction_candidate = HALL_DIR_FORWARD;
    edge_count++;
    last_state = raw;
    last_edge_time = now;
    last_edge_dt_ticks = dt;
    return;
}

if (Hall_IsReverseAdjacent(last_state, raw)) {
    direction_candidate = HALL_DIR_REVERSE;
    edge_count++;
    last_state = raw;
    last_edge_time = now;
    last_edge_dt_ticks = dt;
    return;
}

abnormal_jump_count++;
```

## ISR 边界

未来如果用 GPIO/EXTI，ISR 只允许做最小工作：

- 读取或保存三位 Hall 原始状态。
- 保存时间戳。
- 置位 pending flag 或写入很小的事件缓冲。
- 增加必要的轻量计数。

ISR 内禁止：

- `printf`;
- JSON 解析;
- `HAL_Delay`;
- 阻塞等待;
- 动态分配;
- WebSocket / ESP32 通信;
- 复杂 MCSDK 调用;
- 修改高频 FOC ISR 或 TIM1 PWM 更新路径;
- 做最终速度闭环或电流环控制决策。

## 当前不能进入固件的原因

- PCB2 未焊接，DMM 连续性 / 短路表没有结果。
- `PA0/PA1/PB4` 的 GPIO/EXTI 电气边界还没有实现评审。
- 时间戳来源和 tick 精度没有定案。
- 抖动阈值没有实测依据。
- MCSDK 速度 / 位置反馈接入口没有被安全确认。
- 没有 no-power build 记录。

This artifact is not usable to claim firmware implementation, MCSDK Hall
integration, build success, continuity proof, Gate PWM safety, Motor Profiler
readiness, Hall readiness, motor readiness, power-stage readiness, or
sensorless validation.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler or Motor Pilot.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## 给算法同学的下一次检查

不用背术语，只要能按顺序说出这句话：

```text
先读 PA0/PA1/PB4，先拦 000/111，第一次合法值只当起点，重复值不算边沿，
太快先怀疑抖动，然后再判断正向或反向相邻一步，最后把不相邻的合法跳变记为异常跳码。
```

如果能解释这句话，就可以进入下一步 no-power 代码草案评审。仍然不能上电、
不能接电机、不能输出 Gate PWM。
