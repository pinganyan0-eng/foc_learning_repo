# 2026-05-31 Software Hall Adapter Processing Order ChatGPT Follow-Up

## Status

Completed as L2 concept evidence. The user first used ChatGPT for the concept check, then pasted the result back to Codex for local review and evidence recording.

## Project Boundary

- Current Hall route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- This record is learning evidence for the future software Hall adapter processing order only.
- It is not firmware implementation, not GPIO/EXTI runtime evidence, not MCSDK Hall integration, not build evidence, and not Hall closed-loop readiness.
- No 24V, power-board connection, motor connection, Gate PWM output, Motor Profiler, or Motor Pilot action is authorized by this review.

## User Teach-Back

User's first version:

```text
先读 PA0/PA1/PB4 -> 拒绝 000/111 -> 第一次有效状态只存基准，不计边沿 -> 重复不计边沿，也不判断方向 -> 太快算抖动候选 -> 相邻跳变判断正反向 -> 非相邻合法状态不是 000/111，而是合法码之间跳太远
```

ChatGPT's assessment:

- Order is correct.
- `PA0/PA1/PB4` raw read is present.
- `000/111` rejection is present.
- First valid state is not mistakenly counted as an edge.
- Repeated state is not mistakenly counted as an edge or direction decision.
- The missing precision is the final action: record abnormal jump.

Final standard version:

```text
先读 PA0/PA1/PB4 -> 拒绝 000/111 -> 第一次有效状态只存基准，不计边沿 -> 重复不计边沿，也不判断方向 -> 太快算抖动候选 -> 相邻跳变判断正反向 -> 非相邻合法状态不是 000/111，而是合法码之间跳太远，记跳码异常
```

## Evidence Meaning

- Evidence level: L2. The user can restate the processing order and key defensive checks in their own words.
- The repaired point is the final step: non-adjacent legal-state jumps must be recorded as abnormal jump events.
- This does not yet prove L4 transfer, because the user has not independently traced a mixed sample sequence through baseline, repeat, bounce, adjacent direction, and abnormal-jump decisions.

## Next Check

Before software Hall firmware work, ask the user to trace one raw sequence and label it. Assume the bounce threshold is `50` ticks:

```text
(1000, 100)
(1600, 100)
(2200, 110)
(2210, 010)
(3000, 111)
(3800, 011)
```

Expected reasoning shape:

- first valid state becomes baseline;
- repeated state is not an edge;
- `100 -> 110` is an adjacent legal transition and defines a direction candidate;
- `110 -> 010` at `10` ticks is a bounce candidate and should not update the accepted baseline;
- illegal `111` is rejected before direction judgment;
- `110 -> 011` is a non-adjacent legal jump and increments abnormal-jump evidence;
- the result remains debug-only and does not feed MCSDK Hall.
