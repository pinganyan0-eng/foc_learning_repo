# Packet A Generated-Source Review - QIANSAI_G474_STDRIVE101_FOC_P2

Date: 2026-05-21

Review ID: `P2-SOURCE-REVIEW-2026-05-21-001`

Decision: `Packet A selected fields accepted for no-power configuration evidence / build-only source prerequisite satisfied / CLI build blocked by toolchain path / hardware trust still blocked`.

This review consumes the Workbench-generated project side effect from the 2026-05-21 no-power GUI route. It upgrades Packet A selected-field evidence only. It does not prove the current PCB2 physical route, continuity, STDRIVE101 protection behavior, Gate PWM safety, Hall readiness, motor readiness, power-stage readiness, or sensorless readiness.

## Review Header

| Field | Value |
| --- | --- |
| Reviewer | Codex |
| Packet type | Packet A / generated-source side-effect review |
| Primary source path | `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/` |
| Authorizing source package | `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/workbench_foc_capture_success_2026-05-21.md` |
| External live project | `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2` |
| Source date/version | 2026-05-21, ST Motor Control Workbench 6.4.2 |
| Current board match statement | Matches a Workbench user-board model for the intended custom STDRIVE101 route. It is not physical proof of current PCB2. |
| Intake checklist used | `source_packet_intake_checklist_2026-05-14.md` |
| Initial decision | Accept selected Packet A configuration fields; keep hardware fields blocked |

## Accepted Packet A Fields

| Required field | Evidence observed | Decision |
| --- | --- | --- |
| Real Workbench source or equivalent | Archived `.stwb6`, `.ioc`, `.ioc.wb`, `.wbdef`, `main.c`, `mc_config.c`, and `parameters_conversion.h` exist. | Accepted for no-power Packet A configuration evidence. |
| MCU / board context | `NUCLEO-G474RE`, `STM32G474RETx`, and `STM32G474RE` appear in the source package. | Accepted for configuration evidence. |
| Drive type | `MotorControl.DRIVE_TYPE=FOC`, `M1_DRIVE_TYPE=FOC`, and `.wbdef` `DRIVE_TYPE=FOC`. | Accepted. |
| TIM1 complementary PWM | `PA8/TIM1_CH1`, `PA9/TIM1_CH2`, `PA10/TIM1_CH3`, `PB13/TIM1_CH1N`, `PB14/TIM1_CH2N`, `PB15/TIM1_CH3N`. | Accepted as Workbench standard TIM1 route; not accepted as current PCB2 physical proof. |
| Fault / break input | `PB12.Signal=TIM1_BKIN`, `TIM1.BreakState=TIM_BREAK_ENABLE`, and generated `main.c` uses `TIM_BREAKINPUTSOURCE_BKIN`. | Accepted as configuration evidence; Packet C and continuity still blocked. |
| Current-sense mode | `ThreeShunt_AmplifiedCurrents`, `THREE_SHUNT_INDEPENDENT_RESOURCES`, `M1_CURRENT_SENSING_TOPO=THREE_SHUNT`, `PWMC_R3_2_Handle_t`, and ADC injected conversion triggered by `ADC_EXTERNALTRIGINJEC_T1_TRGO`. | Accepted as configuration evidence; current-sense hardware behavior still blocked. |
| Hall / sensor mode | `M1_SPEED_SENSOR=HALL_SENSOR`, `HALL_TIM2`, `TIM2_IRQHandler`, generated `HALL_Handle_t`, and Hall pins `PA15/PB3/PB10`. | Accepted as Workbench selected field; not accepted as current PCB2 Hall route. |
| `PA2/PA3` policy | Generated project uses `USART2` on `PA2/PA3` with DMA and ASPEP/MCP. | Accepted as visible reuse decision; not accepted as communication or OPAMP/PGA hardware validation. |
| `PB3` ownership | Workbench generated route uses `PB3` as `M1_HALL_H2` / `TIM2_CH2`. | Accepted only as Workbench route. Current PCB2 locks `PB3=LIN1`, so this cannot be used as current-board Hall proof. |

## Rejected Or Blocked Fields

- Current PCB2 Hall route remains `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`; it is not accepted as the generated TIM2 hardware Hall route.
- Current PCB2 PWM / driver-input route remains `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10`; it is not the same as the generated standard TIM1 complementary route.
- `PB3` is a fixed current PCB2 constraint: current board uses it as `LIN1`,
  while generated Workbench Hall uses `PB3`. Do not treat `PB3` as current
  Hall unless a separate hardware-rework route is opened.
- `P14/P15` are confirmed as `3V3/GND` for route planning, but this is not a
  powered or continuity validation.
- `R57BLB50L2` remains a temporary Workbench motor placeholder, not measured motor data.
- `M1_USE_INTERNAL_OPAMP=false` / `M1_CURRENT_AMPLIFICATION_TOPO=EXTERNAL` is accepted only as the generated model, not proof that board current-sense gains and offsets are correct.
- Packet B route proof, Packet C protection proof, no-power continuity, current-limited bring-up, waveform review, and rollback evidence remain blocked.

## Static Verification

The following read-only checks were used:

| Check | Result |
| --- | --- |
| Search for `SIX_STEP`, `sixstep`, `mc_tasks_sixstep`, `pwmc_sixstep`, `speed_duty_ctrl` | No matches in the archived generated-project clue folder. |
| Search for FOC / board / driver fields | Found `DRIVE_TYPE=FOC`, `M1_POWERBOARD_NAME=~MY-STDRIVE101_POWER_BOARD`, `M1_PWM_DRIVER_PN=STDRIVE101`, and Hall/current-sense fields in `.wbdef`, `.ioc`, and `.ioc.wb`. |
| Search for TIM1 break / complementary PWM | Found `PB12/TIM1_BKIN`, `TIM_BREAK_ENABLE`, and `PA8/PA9/PA10 + PB13/PB14/PB15` TIM1 complementary PWM fields. |
| Search for Hall route | Found generated TIM2 Hall on `PA15/PB3/PB10` and `HALL_Handle_t HALL_M1`. |
| Search for current sensing | Found ADC1/ADC3 injected conversions, `PWMC_R3_2_Handle_t`, and `R3_2_*` current feedback functions. |

## Build-Only Gate Result

Packet A selected-field evidence is now accepted enough to satisfy the source prerequisite in `future_build_only_gate_2026-05-15.md`.

Build execution remains blocked in this shell:

- `cmake --version` is available and reports 4.3.2.
- `ninja --version` is not available in PATH.
- `arm-none-eabi-gcc --version` is not available in PATH.
- Targeted searches under the currently readable STM32Cube, VS Code extension, AppData STM, and ST install roots did not locate usable `ninja.exe` or `arm-none-eabi-gcc.exe` paths in this turn.

No CMake build was run. This is recorded as `CLI build blocked by toolchain path`, not as an MCSDK generated-project failure.

## Evidence Updates

Upgrade only these statements:

- Packet A selected fields are accepted as no-power MCSDK/Workbench configuration evidence.
- The generated project side effect is consistent with FOC, TIM1 complementary PWM, three-shunt current sensing, TIM2 Hall, USART2 ASPEP/MCP, and TIM1 BKIN break configuration.
- The build-only gate source prerequisite is satisfied, but no build record exists yet.

Do not upgrade these statements:

- CN8 / current PCB2 routing is correct.
- STDRIVE101 protection paths are correct.
- Current sensing works.
- Hall feedback works.
- Gate PWM is safe.
- Motor Profiler can run.
- Hall closed-loop works.
- Sensorless / SMO works.
- The motor or power board is ready to connect.

## Safety Statement

No flash, 24V, power-board connection, motor connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or sensorless / SMO action is authorized by this review.
