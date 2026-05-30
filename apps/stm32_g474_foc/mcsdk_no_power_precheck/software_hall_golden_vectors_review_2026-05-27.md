# Software Hall Golden Vectors Review - 2026-05-27

Decision:
`Host-side software Hall golden vectors / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.

## 中文结论

- 这一步把软件 Hall 状态机规则固化成“黄金测试向量”。
- 向量位置：`tests/fixtures/software_hall_golden_vectors.json`。
- 回放测试位置：`tests/test_software_hall_vectors.py`。
- 当前路线仍是 `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`。
- `PB3=LIN1`，PB3 不参与当前 Hall。
- 这些向量以后可以给 C 固件 adapter 当输入/输出对照表。
- 这不是固件实现，不是 GPIO/EXTI 实测，不是 MCSDK Hall 接入，不是硬件通过。

This is not firmware implementation, not GPIO/EXTI runtime behavior, and not
hardware validation.

## What Was Added

- `tests/fixtures/software_hall_golden_vectors.json`
  - records replayable Hall sample sequences;
  - records expected decisions, accepted states, previous states, edge counts,
    direction candidates, and abnormal counters;
  - records the route and `PB3=LIN1` pin constraint.
- `tests/test_software_hall_vectors.py`
  - loads the JSON vectors;
  - replays them through `SoftwareHallStateMachine`;
  - checks every expected decision and counter.

## Covered Scenarios

- forward candidate cycle:
  `001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001`;
- illegal state rejection for `000`;
- repeated-state rejection;
- configurable bounce-candidate rejection;
- abnormal non-adjacent legal jump;
- reverse adjacent step after previous rejected samples.

## Evidence Limit

This artifact is useful as a no-power algorithm test contract. It is not usable
to claim:

- firmware implementation;
- GPIO/EXTI runtime behavior;
- MCSDK Hall integration;
- no-power firmware build success;
- DMM continuity proof;
- Gate PWM safety;
- Motor Profiler readiness;
- Hall readiness;
- Hall closed-loop readiness;
- motor readiness;
- power-stage readiness;
- sensorless validation.

## Still Blocked Before Firmware

- PCB2 is unpopulated.
- DMM continuity / short-check table is deferred, not passed.
- `PA0/PA1/PB4` GPIO/EXTI electrical boundary is not reviewed.
- STM32 timestamp source and tick resolution are not selected.
- debounce threshold is not measured.
- MCSDK speed / position feedback integration point is not accepted.
- no-power firmware build is not recorded.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler or Motor Pilot.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
