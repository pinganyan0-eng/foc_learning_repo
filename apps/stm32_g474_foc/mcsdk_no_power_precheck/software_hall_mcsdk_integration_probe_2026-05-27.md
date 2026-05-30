# Software Hall MCSDK Integration Probe - 2026-05-27

Decision:
`MCSDK Hall integration points identified as read-only clues / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.

## 涓枃缁撹

- 杩欎竴姝ュ彧璇绘鏌?2026-05-21 Workbench 鐢熸垚鍓骇鐗╅噷鍜岄€熷害/浣嶇疆鍙嶉鐩稿叧鐨勭嚎绱€?- 鐪嬪埌鐨勬爣鍑?MCSDK Hall 璺嚎鏄?`TIM2` 纭欢 Hall锛岃€屼笉鏄綋鍓?PCB2 鐨?`PA0/PA1/PB4` 杞欢 Hall銆?- 褰撳墠 PCB2 浠嶇劧鏄細

```text
HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4
PB3 = LIN1
```

- 鍥犳涓嶈兘鐩存帴鎶婂綋鍓?PCB2 Hall 鎺ュ埌 MCSDK 鏍囧噯 `HALL_M1` 骞跺０鏄庨棴鐜彲杩愯銆?- 鍚庣画濡傛灉瑕佹帴 MCSDK锛屽繀椤诲彟寮€ firmware-integration review锛涗笉鑳界洿鎺ユ敼 JEOC / FOC ISR銆乀IM1 PWM 鏇存柊璺緞鎴栭€熷害鐜弽棣堛€?
## Sources Read

Read-only source folder:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/`

Files inspected:

- `main.c`
- `mc_config.c`
- `parameters_conversion.h`
- `QIANSAI_G474_STDRIVE101_FOC_P2.ioc`
- `QIANSAI_G474_STDRIVE101_FOC_P2.log`

## Read-Only Findings

| Source clue | What it shows | Limit |
| --- | --- | --- |
| `main.c` `MX_TIM2_Init()` | Uses `TIM_HallSensor_InitTypeDef` and `HAL_TIMEx_HallSensor_Init(&htim2, ...)`. | This is standard TIM2 hardware Hall setup, not software GPIO/EXTI Hall. |
| `parameters_conversion.h` | Defines `MAIN_SCFG UI_SCODE_HALL`, `M1_HALL_TIM_PERIOD`, `M1_HALL_IC_FILTER`, and `SPD_HALL_TIM_M1_IRQHandler TIM2_IRQHandler`. | Confirms generated Hall path is tied to TIM2 interrupt naming. |
| `mc_config.c` | Defines `SpeednTorqCtrlM1`, `PIDSpeedHandle_M1`, and `HALL_Handle_t HALL_M1`. | These are generated MCSDK objects; no software Hall adapter is connected here. |
| `mc_config.c` `HALL_M1` | References `TIM2`, `M1_HALL_H1/H2/H3` ports and pins, Hall placement, phase shift, speed buffer, and filter. | It expects MCSDK hardware Hall semantics and current generated pins. |
| `.ioc` | Records `MotorControl.M1_SPEED_SENSOR=HALL_SENSOR`, `SPEED_SENSOR_SELECTION=HALL_SENSORS`, `M1_HALL_TIMER_SELECTION=HALL_TIM2`, and `M1_HALL_TIMER_IRQ=TIM2`. | It accepts only generated configuration evidence; it does not match current PCB2 software Hall route. |
| `.log` | Shows generated `hall_speed_pos_fdbk.c/.h` and `speed_torq_ctrl.c/.h`. | Those generated source files were not archived in this packet, so their interfaces are not accepted implementation evidence here. |

## Integration Boundary

The current no-power software Hall work can continue only as one of these
separate tracks:

| Track | Meaning | Current status |
| --- | --- | --- |
| Isolated adapter | Use `PA0/PA1/PB4` only for debug/state-machine evidence. Do not feed MCSDK speed loop. | Allowed as no-power design and host-side tests. |
| MCSDK custom feedback integration | Create a reviewed software speed/position feedback component or adapter boundary that MCSDK can consume safely. | Boundary draft added in `software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md`, but still no firmware hook or implementation clearance; requires a separate firmware-integration review before any hook. |
| Hardware rework fallback | Move Hall signals to a timer-compatible MCSDK Hall route. | Fallback only; not authorized by this probe. |

## Hard Stops

The separate firmware-integration boundary draft now exists, but it is still a hard stop before doing any of these:

- editing `hall_speed_pos_fdbk.c/.h`;
- editing `speed_torq_ctrl.c/.h`;
- replacing `HALL_M1` with a software Hall object;
- changing `M1_SPEED_SENSOR` or `SPEED_SENSOR_SELECTION`;
- writing software Hall speed directly into the speed loop;
- changing JEOC / FOC ISR;
- changing TIM1 PWM update path;
- calling complex MCSDK APIs from EXTI or timer ISR;
- claiming Hall closed-loop readiness from host tests or a build-only result.

## Required Next Evidence Before Any MCSDK Hook

- PCB2 populated and DMM continuity / short-check table reviewed.
- Exact GPIO/EXTI boundary for `PA0/PA1/PB4`.
- Timestamp source and tick resolution decision.
- Confirmed low-priority processing context for `Hall_ProcessEvent()`.
- Archived generated MCSDK speed/position feedback headers or official source
  interface evidence.
- No-power build-only path available.
- Separate review proving the hook does not touch JEOC / FOC ISR or TIM1 PWM
  timing.

## Evidence Limit

This probe is useful to name likely MCSDK integration objects and hard stops.
It is not usable to claim:

- firmware implementation;
- MCSDK Hall integration;
- software Hall adapter implementation;
- no-power firmware build success;
- DMM continuity proof;
- Gate PWM safety;
- Motor Profiler readiness;
- Hall readiness;
- Hall closed-loop readiness;
- motor readiness;
- power-stage readiness;
- sensorless validation.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler or Motor Pilot.
- No flash.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
