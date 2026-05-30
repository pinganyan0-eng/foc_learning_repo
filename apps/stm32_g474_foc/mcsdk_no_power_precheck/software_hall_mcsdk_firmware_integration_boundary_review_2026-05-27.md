# 软件 Hall MCSDK Firmware-Integration 边界审查草案 - 2026-05-27

Decision:
`Software Hall MCSDK firmware-integration boundary review draft / no firmware implementation / no MCSDK hook / no Hall readiness`.

## 中文结论

你现在不需要知道 MCSDK 内部怎么改。当前要先记住一条红线：
软件 Hall adapter 以后最多先产出 `direction_candidate` 和 `speed_candidate` 这种候选量，不能直接写进 `HALL_M1`、`SpeednTorqCtrlM1`、速度 PID、FOC ISR 或 TIM1 PWM 路径。

当前路线仍然是：

```text
HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4
PB3 = LIN1，不参与 Hall
P14/P15 = 3V3/GND
```

PCB2 仍未完成焊接。DMM 连续性 / 短路表暂缓，不是通过。

## 功能句

```text
software Hall adapter produces direction_candidate + speed_candidate only
-> low-priority integration boundary reviews whether MCSDK can consume it
-> no write to HALL_M1 / SpeednTorqCtrlM1 / FOC ISR without accepted interface evidence
```

中文说法：现在不是把软件 Hall 接进 MCSDK，而是先画红线：哪些对象只是线索，哪些文件不能碰，哪些证据回来前不能 hook。

## Sources Read

Read-only sources:

- `software_hall_mcsdk_integration_probe_2026-05-27.md`
- `software_hall_debug_output_route_review_2026-05-27.md`
- `software_hall_timestamp_source_review_2026-05-27.md`
- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/main.c`
- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/mc_config.c`
- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/parameters_conversion.h`
- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/QIANSAI_G474_STDRIVE101_FOC_P2.ioc`
- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/QIANSAI_G474_STDRIVE101_FOC_P2.log`

## Static MCSDK Clues And Limits

| Clue | What it means | Current limit |
| --- | --- | --- |
| `HALL_M1` | Generated standard MCSDK Hall feedback object. | Clue only. Do not replace or feed it from `PA0/PA1/PB4` software Hall in this stage. |
| `SpeednTorqCtrlM1` | Generated speed / torque controller object. | Clue only. Do not write `speed_candidate` into it. |
| `PIDSpeedHandle_M1` | Generated speed PID object. | Clue only. It is not a software Hall injection point. |
| `pSTC` | Generated controller pointer table. | Clue only. Not a feedback hook. |
| `MCI_Handle_t` | Generated motor-control interface handle. | Clue only. Not a safe software Hall feedback hook. |
| `FOCVars` | Generated FOC variable storage. | Clue only. Do not use it as a custom feedback entry. |
| `SPD_HALL_TIM_M1_IRQHandler TIM2_IRQHandler` | Generated standard Hall ISR naming on TIM2. | This is not the current `PA0/PA1/PB4` GPIO/EXTI route. |
| `M1_SPEED_SENSOR=HALL_SENSOR` | Workbench selected standard Hall sensor mode. | Configuration evidence only, not current PCB2 software Hall integration. |
| `M1_HALL_TIMER_SELECTION=HALL_TIM2` | Workbench selected TIM2 hardware Hall. | It conflicts with the current software Hall route and cannot prove real-board Hall. |
| `hall_speed_pos_fdbk.c/.h` | Generated file names appear in the log. | File-name clues only; source was not archived here as accepted interface evidence. |
| `speed_torq_ctrl.c/.h` | Generated file names appear in the log. | File-name clues only; not accepted as an editable hook. |
| `mc_app_hooks.c/.h` | Generated hook file names appear in the log. | File-name clues only; cannot be used until archived source and hook contract are reviewed. |

## Integration Mode Decision

| Mode | Meaning | Current decision |
| --- | --- | --- |
| Mode A: isolated adapter debug only | Software Hall runs as no-power state-machine / debug artifact and does not feed MCSDK. | Allowed for documents, host tests, and future reviewed no-power firmware draft only. |
| Mode B: custom MCSDK speed / position component | Software Hall exposes a reviewed component that MCSDK can safely consume. | Future maybe; requires accepted MCSDK interface evidence, no-power build record, and separate review. |
| Mode C: replace or edit `HALL_M1` | Reuse generated `HALL_M1` as if `PA0/PA1/PB4` were standard Hall. | Hard stop. |
| Mode D: write `speed_candidate` into speed loop / PID | Push candidate speed directly into `SpeednTorqCtrlM1` or `PIDSpeedHandle_M1`. | Hard stop. |
| Mode E: touch JEOC / FOC ISR / TIM1 PWM | Put software Hall decisions into high-frequency motor-control timing. | Hard stop. |
| Mode F: hardware rework to TIM2 Hall route | Change wiring so MCSDK standard TIM2 Hall can be used. | Separate hardware path only, not this software route. |

## Required Evidence Before Any Hook

Before any MCSDK hook is allowed, all of these must exist:

- populated PCB2 plus reviewed DMM continuity / short-check table;
- accepted GPIO/EXTI boundary for `PA0/PA1/PB4`;
- accepted timestamp-source review with exact timer decision if used;
- accepted low-frequency debug-output route;
- archived `hall_speed_pos_fdbk.*`, `speed_torq_ctrl.*`, and relevant MCSDK interface source or official interface evidence;
- no-power build-only toolchain and build record;
- host model and golden vectors aligned with any firmware behavior;
- exact hook file list and rollback plan;
- proof that the hook does not touch TIM1 PWM, JEOC / FOC ISR, or Gate PWM output.

## Prohibited Until Those Evidence Items Exist

- Do not edit generated MCSDK files.
- Do not write into MCSDK speed feedback.
- Do not replace `HALL_M1`.
- Do not change `.ioc` speed-sensor mode to claim current PCB2 software Hall.
- Do not call MCSDK speed-loop APIs from EXTI or timer ISR.
- Do not use `speed_candidate` as final closed-loop speed.
- Do not run Motor Profiler or Motor Pilot.
- Do not claim Hall closed-loop, motor readiness, power-stage readiness, or sensorless validation.

## What This Artifact Can Claim

- It can claim that MCSDK firmware-integration risks and hard stops are documented.
- It can claim that current `PA0/PA1/PB4` software Hall remains outside the generated TIM2 `HALL_M1` route.
- It can claim that future hook work needs accepted source/interface evidence first.

## What This Artifact Cannot Claim

- No software Hall adapter implementation is claimed.
- No firmware implementation is claimed.
- No MCSDK hook is claimed.
- No MCSDK Hall integration is claimed.
- No GPIO/EXTI runtime proof is claimed.
- No no-power build success is claimed.
- No DMM continuity proof is claimed.
- No Gate PWM safety is claimed.
- No Hall closed-loop claim is made.
- No motor readiness, power-stage readiness, or sensorless validation is claimed.

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

## Next Step

The firmware hook evidence request checklist now exists at
`software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md`.
The exact generated `Src/Inc` source snapshot also now exists at
`packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`.
Use that snapshot for a read-only MCSDK speed / position feedback interface
review before any integration review can move from clue to implementation
proposal.
If the project continues toward implementation, wait for PCB2 population, DMM evidence, and no-power build-only setup first.
