# PCB2 Waiting-Hardware Handoff - 2026-05-31

Decision:
`PCB2 waiting for population / DMM gate deferred / no powered action / no firmware implementation`.

This handoff implements the current real FOC progress rule while PCB2 is not
populated yet. It is a user-action and evidence-routing card, not a measurement
result, not firmware, not MCSDK integration, and not hardware readiness.

## Current State

- PCB2 status reported by the user: not populated / waiting for hardware.
- DMM continuity and short checks are deferred until the populated board exists.
- Deferred does not mean passed.
- Current software Hall route remains:

```text
HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4
PB3 = LIN1
P14/P15 = 3V3/GND
```

## User Hardware Teammate Message

Send this exact status request to the hardware teammate and return the answer:

```text
PCB2 目前未焊好；预计焊接/到手时间：____。
当前路线是否仍为 PA0/PA1/PB4 + PB3=LIN1 + P14/P15=3V3/GND：是/否。
如果路线、原理图、网表、Gerber、BOM 或引脚表有变化，请附最新版文件或截图。
```

If new hardware material is available, return the latest source package or
screenshots for:

- PCB2 schematic / EDA / netlist / Gerber / BOM;
- `IA/IB/IC -> PA0/PA1/PB4`;
- `PB3=LIN1`;
- `nFAULT -> PB12`;
- `DT/MODE`, `STBY`, `SCREF/VDS`, `CP`, and `VS/VM`.

## No-Power Hall Sequence Check

The next algorithm-side check can proceed while hardware is waiting. Use this
prompt:

```text
给定 Hall 原始样本：
(1000,100), (1600,100), (2200,110), (2210,010), (3000,111), (3800,011)

抖动阈值：50 ticks

请标出：基准、重复、相邻方向候选、抖动候选、非法状态、跳码异常。
最后说明为什么这仍然只是 debug-only 软件 Hall 证据，不能接入 MCSDK Hall。
```

Acceptance target:

- first valid state is the baseline;
- repeated state is not an edge;
- `100 -> 110` is an adjacent direction candidate;
- `110 -> 010` at `10` ticks is a bounce candidate and must not update the
  accepted baseline;
- `111` is rejected before direction judgment;
- `110 -> 011` is a non-adjacent legal jump and records abnormal-jump evidence;
- no MCSDK Hall integration or firmware readiness is claimed.

## Codex Review Rules

- If the user returns hardware files, review them as Packet B/C source evidence
  before upgrading any blocker.
- If the user returns only "PCB2 still not populated and route unchanged", keep
  the DMM gate deferred and do not upgrade hardware status.
- If the user returns the Hall sequence answer, review it under WP-030 and only
  decide whether the no-power software Hall adapter code-review plan can be
  drafted later.

## Forbidden Actions

- No DMM check until PCB2 is populated.
- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No flash / Run / Debug on the generated motor-control project.
- No Generate / Build action caused by this handoff.
- No Motor Profiler or Motor Pilot.
- No Hall closed-loop, sensorless, motor, or power-stage readiness claim.
