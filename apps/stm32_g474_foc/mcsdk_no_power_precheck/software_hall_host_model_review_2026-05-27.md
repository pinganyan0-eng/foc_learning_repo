# Software Hall Host Model Review - 2026-05-27

Decision:
`Host-side software Hall reference model / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.

This review records the first executable no-power algorithm specification for
the future `PA0/PA1/PB4` software Hall adapter. It is Python host-side code
only. It does not read STM32 GPIO, configure EXTI, edit MCSDK generated code,
build firmware, flash hardware, or validate a motor.
It is not STM32 firmware.
It is not GPIO/EXTI runtime behavior.

## 中文速读

- 这一步把 Hall 状态机规则变成主机侧可跑测试。
- 代码位置：`src/software_hall_model.py`.
- 测试位置：`tests/test_software_hall_model.py`.
- 当前路线仍是 `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; PB3 不参与当前 Hall。
- 这个模型只接收 `raw_state` 和 `timestamp_ticks`，不读真实 GPIO。
- 抖动阈值没有写死；`min_edge_ticks` 只能作为测试或未来实测后的配置值。
- 通过测试只能说明主机侧状态机规则可复现，不能说明固件或硬件可用。

## Model Contract

The host model exposes:

- `is_valid_state(state)`;
- `is_forward_adjacent(previous, current)`;
- `is_reverse_adjacent(previous, current)`;
- `SoftwareHallStateMachine.process(raw_state, timestamp_ticks)`.

The state machine records:

- `last_accepted_state`;
- `last_edge_ticks`;
- `direction_candidate`;
- `edge_count`;
- `illegal_state_count`;
- `repeat_count`;
- `bounce_candidate_count`;
- `abnormal_jump_count`;
- `last_edge_dt_ticks`.

## Decision Order Implemented

```text
raw state input
-> illegal-state check
-> first-valid check
-> repeated-state check
-> configurable bounce/timing check
-> forward/reverse adjacent check
-> abnormal-jump count
```

## Test Coverage

`tests/test_software_hall_model.py` covers:

- valid states `001/010/011/100/101/110`;
- illegal states `000/111`;
- candidate forward adjacency `100 -> 110`;
- candidate reverse adjacency `100 -> 101`;
- non-adjacent legal jump `100 -> 011`;
- first valid state as baseline only;
- repeated state not counted as edge;
- forward edge count and direction candidate;
- reverse edge count and direction candidate;
- configurable bounce candidate rejection;
- complete candidate forward cycle:
  `001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001`.

## Evidence Limit

This model is useful as an executable algorithm specification. It is not usable
to claim:

- firmware implementation;
- GPIO/EXTI runtime behavior;
- MCSDK Hall integration;
- no-power build success;
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
- timestamp source and tick resolution are not selected for STM32 firmware.
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
