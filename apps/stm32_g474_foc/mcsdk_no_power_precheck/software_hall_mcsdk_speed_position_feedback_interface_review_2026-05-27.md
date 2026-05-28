# 软件 Hall MCSDK Speed/Position Feedback 接口审查 - 2026-05-27

Decision:
`Software Hall MCSDK speed/position feedback interface review / no firmware implementation / no MCSDK hook / no Hall readiness`.

## 中文结论

这次审查回答一个问题：未来 `PA0/PA1/PB4` 软件 Hall adapter 能不能直接接进 MCSDK？

当前结论：不能直接接。已归档源码显示，MCSDK 标准 Hall 路线不是只消费三位 Hall 状态，而是围绕 `HALL_M1` 和 `SpeednPosFdbk_Handle_t` 维护一整套反馈量：电角度、机械速度、电速度、方向、可靠性、速度 FIFO 和故障判断。未来软件 Hall 只能先保持 debug-only，或者另开一轮设计一个经过审查的 `SpeednPosFdbk`-compatible component；不能把 `direction_candidate` / `speed_candidate` 直接写进 `HALL_M1`、`SpeednTorqCtrlM1`、速度 PID 或 FOC ISR。

当前 PCB2 路线仍然是：

```text
HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4
PB3 = LIN1，不参与 Hall
P14/P15 = 3V3/GND
```

PCB2 仍未焊接。DMM 连续性 / 短路表暂缓，不是通过。

## Sources Read

Read-only archived sources from:

`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`

Key files inspected:

- `Src/stm32g4xx_mc_it.c`
- `Src/hall_speed_pos_fdbk.c`
- `Inc/hall_speed_pos_fdbk.h`
- `Src/speed_torq_ctrl.c`
- `Inc/speed_torq_ctrl.h`
- `Src/mc_tasks_foc.c`
- `Src/mc_config.c`
- `Inc/mc_type.h`
- `Inc/main.h`
- `Src/stm32g4xx_hal_msp.c`

Important absence:

- `speed_pos_fdbk.h` is included by `Inc/hall_speed_pos_fdbk.h`, but it is not present in the archived project `Src/Inc` snapshot. Therefore the base `SpeednPosFdbk_Handle_t` interface is only partially visible from generated files; it is not enough to design or claim an accepted custom MCSDK feedback component.

## MCSDK Feedback Data Flow

| Stage | Source clue | Meaning for software Hall |
| --- | --- | --- |
| Generated pin route | `Inc/main.h` and `Src/stm32g4xx_hal_msp.c` map Hall to `PA15/PB3/PB10` on `TIM2`. | This is the Workbench standard TIM2 Hall route, not current PCB2 `PA0/PA1/PB4`. |
| Generated Hall object | `Src/mc_config.c` defines `HALL_M1` with `.TIMx = TIM2`, Hall GPIO ports/pins, reliability limits, measurement frequency, and DPP conversion. | `HALL_M1` is a generated hardware Hall object, not a free software adapter storage object. |
| Hall ISR entry | `Src/stm32g4xx_mc_it.c` routes `SPD_HALL_TIM_M1_IRQHandler()` to `HALL_TIMx_UP_IRQHandler(&HALL_M1)` and `HALL_TIMx_CC_IRQHandler(&HALL_M1)`. | Current software Hall on `PA0/PA1/PB4` cannot reuse this as-is because those pins are not TIM2 Hall channels. |
| Edge processing | `HALL_TIMx_CC_IRQHandler()` reads H1/H2/H3, updates `HallState`, `Direction`, `MeasuredElAngle`, `IncrementElAngle`, speed FIFO, and `AvrElSpeedDpp`. | A future adapter would need equivalent semantics, not only a raw 3-bit state. |
| Medium-frequency speed update | `mc_tasks_foc.c` calls `HALL_CalcAvrgMecSpeedUnit(&HALL_M1, &wAux)`. | MCSDK expects periodic speed/reliability calculation outside the Hall edge ISR. |
| Reliability check | `mc_tasks_foc.c` calls `SPD_Check((SpeednPosFdbk_Handle_t *)&HALL_M1)` in RUN. | A future hook must satisfy MCSDK reliability behavior; bypassing it would be unsafe. |
| Speed loop | `speed_torq_ctrl.c` uses `SPD_GetAvrgMecSpeedUnit(pHandle->SPD)` when calculating speed error. | `speed_candidate` cannot be pushed directly into the PID; MCSDK owns the sensor pointer and units. |
| FOC angle consumption | `FOC_CurrControllerM1()` calls `STC_GetSpeedSensor(pSTC[M1])`, then `SPD_GetElAngle(speedHandle)`, then Park / reverse Park transforms. | FOC consumes electrical angle, not just direction or mechanical speed. Wrong units or timing can corrupt the control frame. |

## Feedback Values MCSDK Appears To Need

A future software Hall integration proposal would need to account for at least these values and behaviors:

| MCSDK value / behavior | Evidence clue | Current software Hall status |
| --- | --- | --- |
| `hElAngle` | `Inc/mc_type.h` records this as the electrical angle used for reference-frame transformation. | Not produced by the current no-power adapter plan. |
| `_Super.hElSpeedDpp` | `HALL_CalcAvrgMecSpeedUnit()` updates it from averaged Hall electrical speed. | Not produced in MCSDK units by the current no-power adapter plan. |
| `_Super.hAvrMecSpeedUnit` | `HALL_CalcAvrgMecSpeedUnit()` stores mechanical speed in MCSDK `SPEED_UNIT`. | Current `speed_candidate` is only a candidate, not accepted MCSDK speed. |
| `Direction` | `HALL_TIMx_CC_IRQHandler()` sets positive / negative based on adjacent state transitions. | Host model can infer direction candidate only. |
| `MeasuredElAngle` / `IncrementElAngle` | Hall edges reset or advance electrical angle. | Not defined for real motor phase shift or pole-pair calibration yet. |
| `SensorIsReliable` and `bSpeedErrorNumber` | Hall code and `SPD_Check()` gate reliability / speed feedback faults. | Current no-power design counts illegal/jump/bounce events but does not satisfy MCSDK reliability contract. |
| Speed FIFO / capture periods | Hall code averages captured periods and handles overflow / prescaler behavior. | Current plan only records edge timestamp deltas; conversion to MCSDK averaging is unresolved. |

## Hook Decision

| Candidate hook | Decision | Reason |
| --- | --- | --- |
| Write `direction_candidate` / `speed_candidate` into `SpeednTorqCtrlM1` or PID | Hard stop | Speed loop uses `SPD_GetAvrgMecSpeedUnit(pHandle->SPD)` and owns units / filtering. |
| Replace or mutate `HALL_M1` from software Hall | Hard stop | `HALL_M1` is configured as TIM2 hardware Hall on `PA15/PB3/PB10`, conflicting with `PA0/PA1/PB4`. |
| Use `STC_SetSpeedSensor()` now | Clue only, not approved | It can change the sensor pointer, but `speed_pos_fdbk.h` / base interface implementation is not archived and no custom component exists. |
| Feed angle directly in FOC ISR | Hard stop | `FOC_CurrControllerM1()` consumes `SPD_GetElAngle()` inside the high-frequency current loop; wrong timing/units are high risk. |
| Stay debug-only | Allowed no-power direction | Software Hall may keep logging state, edge count, illegal count, direction candidate, and speed candidate without feeding MCSDK. |
| Future `SpeednPosFdbk`-compatible component | Future review target only | Requires full interface source, exact units, timing, reliability contract, no-power build record, DMM evidence, and rollback plan. |

## What This Artifact Can Claim

- It can claim that the generated MCSDK Hall / speed / position feedback chain has been read from the archived `Src/Inc` snapshot.
- It can claim that current PCB2 `PA0/PA1/PB4` software Hall is not equivalent to Workbench TIM2 Hall `PA15/PB3/PB10`.
- It can claim that future software Hall MCSDK integration would need electrical angle, speed units, timing, and reliability behavior, not only a 3-bit state machine.
- It can claim that the next safe algorithm-side route is still debug-only or a separately reviewed `SpeednPosFdbk`-compatible design proposal.

## What This Artifact Cannot Claim

- No firmware implementation is claimed.
- No MCSDK hook is claimed.
- No MCSDK Hall integration is claimed.
- No `SpeednPosFdbk` custom component is accepted.
- No GPIO/EXTI runtime proof is claimed.
- No no-power build success is claimed.
- No DMM continuity proof is claimed.
- No Hall closed-loop behavior is claimed.
- No Gate PWM safety, motor readiness, power-stage readiness, or sensorless validation is claimed.

## Verification

- Passed: `rg` static checks for `PA0/PA1/PB4`, `PB3=LIN1`, `PA15/PB3/PB10`, `HALL_M1`, `SPD_GetElAngle`, `speed_pos_fdbk.h`, `debug-only`, and no-power boundary wording.
- Passed: `python -m unittest discover -s tests` (`126` tests OK).
- Passed: `python -m compileall src tests`.
- Passed: `git diff --check` with CRLF warnings only.
- Passed: `python tools\build_vector_store.py` (`8678` chunks).
- Passed: `python tools\search_local_v2.py --eval`.
- Passed with warning only: `python tools\check_ai_contracts.py` (`ACTIVE_TASK.md is done and still requires review`).

## Next Allowed No-Power Step

Allowed next Codex-side step:

- keep software Hall firmware implementation blocked, and if continuing on software architecture, draft a debug-only adapter-to-snapshot contract or request the missing `speed_pos_fdbk.h` / official MCSDK feedback interface source before a custom component proposal.

Still not allowed:

- editing generated MCSDK files;
- writing into `HALL_M1`, `SpeednTorqCtrlM1`, PID, `FOCVars`, JEOC / FOC ISR, or TIM1 PWM;
- building or flashing as hardware proof;
- connecting 24V, power board, or motor;
- outputting Gate PWM;
- running Motor Profiler or Motor Pilot.

## Safety Boundary

- No flash.
- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Motor Pilot run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
