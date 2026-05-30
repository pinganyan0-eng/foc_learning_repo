# 2026-05-28 Software Hall Firmware-Entry Plan

New no-power firmware-entry plan:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_plan_2026-05-28.md`.

Decision:
`Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.

Accepted boundary content:

- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it is not current Hall.
- MCSDK standard TIM2 Hall `PA15/PB3/PB10` remains generated-source evidence
  only, not current PCB2 Hall proof.
- Future first adapter, if later authorized, is debug-only: GPIO/EXTI capture,
  ISR `raw_state + timestamp + event counter` only, low-priority state
  machine, and low-frequency debug snapshot.
- The plan defines valid Hall states, rejects `000/111`, treats repeated
  states as no edge, records bounce candidates, counts abnormal jumps, and
  keeps direction / speed as `direction_candidate` and `speed_candidate`.

Evidence limit:

- This is a no-power plan only, not STM32 firmware and not MCSDK integration.
- DMM remains hardware-side deferred, not passed.
- No generated-code edit, no flash, no Run / Debug, no 24V, no power-board
  connection, no motor connection, no Gate PWM output, no Motor Profiler, no
  Motor Pilot, no Hall closed-loop, no motor readiness, no power-stage
  readiness, and no sensorless readiness is upgraded.

# 2026-05-27 No-Power Build-Only Debug Pass

New no-power build-only result record:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/build_only_result_2026-05-27_qiansai_g474_stdrive101_foc_p2_debug.md`.

Decision:
`No-power build-only Debug pass / local toolchain compiles generated project / no firmware runtime or hardware readiness`.

Accepted boundary content:

- External Workbench project:
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`.
- Build command:
  `cmake --build "C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2\build\Debug" --config Debug`.
- Result: exit code `0`; Ninja output `ninja: no work to do`.
- Confirmed artifacts:
  `QIANSAI_G474_STDRIVE101_FOC_P2.elf` and
  `QIANSAI_G474_STDRIVE101_FOC_P2.map`.
- This is an up-to-date no-power build-only pass, not a clean rebuild record.

Evidence limit:

- This proves only that the generated Workbench project compiles in the local
  toolchain under no-power build-only scope.
- It does not prove current PCB2 routing, DMM continuity, STDRIVE101
  protection, current sensing, GPIO / EXTI runtime behavior, MCSDK Hall
  integration, Gate PWM safety, Hall closed-loop behavior, Motor Profiler
  readiness, motor readiness, power-stage readiness, or sensorless readiness.
- No flash, Run / Debug, 24V, power-board connection, motor connection, Gate
  PWM output, Motor Profiler, or Motor Pilot is authorized.

# 2026-05-27 Software Hall MCSDK Speed/Position Feedback Interface Review

New no-power MCSDK speed / position feedback interface review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md`.

Decision: `Software Hall MCSDK speed/position feedback interface review / no firmware implementation / no MCSDK hook / no Hall readiness`.

Accepted boundary content:

- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it is not a current Hall candidate.
- Archived source review traces the generated chain from `SPD_HALL_TIM_M1_IRQHandler()` to `HALL_TIMx_CC_IRQHandler(&HALL_M1)`, `HALL_CalcAvrgMecSpeedUnit(&HALL_M1, ...)`, `STC_GetSpeedSensor(...)`, `SPD_GetAvrgMecSpeedUnit(...)`, and `SPD_GetElAngle(...)`.
- MCSDK needs electrical angle, speed units, timing, and reliability behavior; a raw `direction_candidate` / `speed_candidate` pair is not an accepted MCSDK feedback interface.
- `speed_pos_fdbk.h` is not present in the archived project `Src/Inc` snapshot, so a custom `SpeednPosFdbk` component remains a future review target only.

Evidence limit:

- This is a no-power source-interface review only, not firmware source and not a MCSDK hook.
- DMM remains hardware-side deferred, not passed.
- No software Hall adapter implementation, runtime API, generated-code hook, MCSDK Hall integration, build record, flash, 24V, power-board connection, motor connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, motor readiness, power-stage readiness, or sensorless readiness is upgraded.
# 2026-05-27 Full Workbench Src/Inc Snapshot

New no-power generated-source snapshot review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-27_001_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot.md`.

Snapshot:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`.

Decision:
`Full generated Src/Inc snapshot archived / source interface evidence available for read-only review / no firmware implementation / no MCSDK hook / no Hall readiness`.

Accepted boundary content:

- The external generated project path exists:
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`.
- The repo now archives generated `Src/`, `Inc/`, `cmake/`, and top-level
  project/build metadata with `SOURCE_MANIFEST_2026-05-27.md` and
  `SHA256SUMS.txt`.
- Required MCSDK source evidence is now available for read-only review,
  including `hall_speed_pos_fdbk.c/.h`, `speed_torq_ctrl.c/.h`,
  `mc_tasks.c/.h`, `mc_tasks_foc.c`, `mc_interface.c/.h`, `mc_api.c/.h`,
  `mc_app_hooks.c/.h`, `mc_parameters.c/.h`, `motorcontrol.c/.h`,
  `mc_type.h`, interrupt sources, current-feedback backend files,
  register-interface files, `usart_aspep_driver.c`, and `aspep.c/.h`.
- `Inc/usart_aspep_driver.h` is not present and must not be silently treated
  as an accepted interface header.
- Static review confirms generated MCSDK Hall remains TIM2 `PA15/PB3/PB10`,
  while current PCB2 remains `PA0/PA1/PB4` software Hall with `PB3=LIN1`.

Evidence limit:

- This is exact source availability for no-power read-only interface review
  only.
- This is not firmware implementation, generated-code edit permission, MCSDK
  hook evidence, no-power build evidence, DMM proof, Hall closed-loop proof, or
  hardware readiness.
- No flash, 24V, power-board connection, motor connection, Gate PWM output,
  Motor Profiler, Motor Pilot, motor readiness, power-stage readiness, or
  sensorless readiness is upgraded.

# 2026-05-27 Software Hall MCSDK Hook Evidence Request Checklist

New no-power MCSDK hook evidence request checklist:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md`.

Decision: `Software Hall MCSDK hook evidence request checklist / no firmware implementation / no MCSDK hook / no Hall readiness`.

Accepted boundary content:

- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it is not a current Hall candidate.
- The checklist requests exact generated or MCSDK interface source evidence before any hook proposal.
- Required source evidence includes `hall_speed_pos_fdbk.c/.h`, speed / position feedback interface evidence, `speed_torq_ctrl.c/.h`, `mc_tasks.c/.h`, `mc_tasks_foc.c`, `mc_interface.c/.h`, `mc_api.c/.h`, `mc_app_hooks.c/.h`, `mc_parameters.c/.h`, `motorcontrol.c/.h`, `mc_type.h`, interrupt sources, current-feedback backend files, and ASPEP / register-interface files.
- Log-only names, screenshots, different-project files, different-version files without review, AI summaries, host tests, and build-only success by itself are rejected as hook evidence.

Evidence limit:

- This is a no-power source-evidence request only, not firmware source and not a MCSDK hook.
- DMM remains hardware-side deferred, not passed.
- No software Hall adapter implementation, runtime API, generated-code hook, MCSDK Hall integration, build record, flash, 24V, power-board connection, motor connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, motor readiness, power-stage readiness, or sensorless readiness is upgraded.
# 2026-05-27 Software Hall MCSDK Firmware-Integration Boundary Review

New no-power MCSDK firmware-integration boundary review draft:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md`.

Decision: `Software Hall MCSDK firmware-integration boundary review draft / no firmware implementation / no MCSDK hook / no Hall readiness`.

Accepted boundary content:

- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it is not a current Hall candidate.
- Future software Hall output is limited to `direction_candidate` and
  `speed_candidate` until accepted MCSDK interface evidence exists.
- `HALL_M1`, `SpeednTorqCtrlM1`, `PIDSpeedHandle_M1`, `pSTC`,
  `MCI_Handle_t`, `FOCVars`, `SPD_HALL_TIM_M1_IRQHandler`,
  `M1_SPEED_SENSOR=HALL_SENSOR`, and `M1_HALL_TIMER_SELECTION=HALL_TIM2` are
  generated standard Hall / speed-loop clues, not accepted hooks.
- `hall_speed_pos_fdbk.c/.h`, `speed_torq_ctrl.c/.h`, and `mc_app_hooks.c/.h`
  are log-only file-name clues until archived source and interface contracts
  are reviewed.
- Direct writes to `HALL_M1`, speed loop, speed PID, JEOC / FOC ISR, or TIM1
  PWM remain hard stops.

Evidence limit:

- This is a no-power MCSDK boundary draft only, not firmware source and not a
  MCSDK hook.
- It is not GPIO/EXTI runtime proof.
- DMM remains hardware-side deferred, not passed.
- Compatibility note for legacy contract tests: 下一步证据入口; 仍没有 current-version EDA;
  仍只有官方器件要求和缺证矩阵.
- No software Hall adapter implementation, runtime API, generated-code hook,
  MCSDK Hall integration, build record, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall
  closed-loop, motor readiness, power-stage readiness, or sensorless readiness
  is upgraded.
# 2026-05-27 Software Hall Debug-Output Route Review

New no-power low-frequency debug-output route review draft:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_debug_output_route_review_2026-05-27.md`.

Decision: `Software Hall low-frequency debug-output route review draft / no firmware implementation / no UART implementation / no Hall readiness`.

Accepted boundary content:

- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it is not a current Hall candidate and is not cleared as SWO.
- Future debug snapshot fields are drafted:
  `current_raw_state`, `last_accepted_state`, `last_decision`, `edge_count`,
  `illegal_state_count`, `repeat_count`, `bounce_candidate_count`,
  `abnormal_jump_count`, `lost_event_count`, `last_edge_dt_ticks`,
  `timestamp_source_id`, `direction_candidate`, and `speed_candidate`.
- Output must be a low-frequency snapshot, not every-edge streaming.
- ISR remains forbidden for `printf`, JSON formatting, UART transmit,
  WebSocket / ESP32 communication, blocking delays, dynamic allocation, MCSDK
  speed feedback, and FOC control decisions.
- UART text / CSV / JSON, ESP32 / WebSocket display, MCSDK USART2 / ASPEP /
  MCP reuse, `PA2/PA3` reuse, and SWO / ITM are not authorized by this draft.

Evidence limit:

- This is a no-power debug-output boundary draft only, not firmware source and
  not UART implementation.
- It is not GPIO/EXTI runtime proof.
- DMM remains hardware-side deferred, not passed.
- No software Hall adapter implementation, runtime API, generated-code hook,
  MCSDK Hall integration, build record, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall
  closed-loop, motor readiness, power-stage readiness, or sensorless readiness
  is upgraded.

# 2026-05-27 Software Hall Timestamp Source Review

New no-power timestamp-source review draft:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_timestamp_source_review_2026-05-27.md`.

Decision: `Software Hall timestamp-source review draft / no firmware implementation / no timer configuration / no Hall readiness`.

Accepted boundary content:

- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it is not a current Hall candidate.
- `TIM1` is excluded as a software Hall timestamp source because the generated
  project ties it to PWM, `TIM1_UP_TIM16_IRQn`, ADC injected triggering, and
  FOC timing through `ADC_EXTERNALTRIGINJEC_T1_TRGO`.
- Current `TIM2` clues are standard MCSDK Hall clues:
  `HAL_TIMEx_HallSensor_Init` and `M1_HALL_TIMER_SELECTION=HALL_TIM2`.
  They do not clear the current PCB2 `PA0/PA1/PB4` software Hall route.
- `HAL_GetTick()` / SysTick is coarse-only because local HAL records
  `uwTickFreq = HAL_TICK_FREQ_DEFAULT; /* 1KHz */`.
- A future isolated `dedicated free-running timer` is the preferred class, but
  exact timer instance, prescaler, overflow period, and debug-freeze behavior
  remain undecided.
- Future delta calculation must use `unsigned delta` overflow handling.

Evidence limit:

- This is a no-power timestamp-source boundary draft only, not firmware source
  and not timer configuration.
- It is not GPIO/EXTI runtime proof.
- DMM remains hardware-side deferred, not passed.
- No software Hall adapter implementation, runtime API, generated-code hook,
  MCSDK Hall integration, build record, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall
  closed-loop, motor readiness, power-stage readiness, or sensorless readiness
  is upgraded.

# 2026-05-27 Software Hall GPIO/EXTI Boundary Review

New no-power GPIO/EXTI boundary draft:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_gpio_exti_boundary_review_2026-05-27.md`.

Decision: `Software Hall GPIO/EXTI boundary review draft / no firmware implementation / no GPIO runtime proof / no Hall readiness`.

Accepted boundary content:

- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it is not a current Hall candidate.
- `PA0/PA1/PB4` are documented as software Hall input candidates only.
- `EXTI0/EXTI1/EXTI4` are documented as future event-capture candidates only.
- Future ISR responsibility is limited to raw Hall state, timestamp,
  pending/event flag or lightweight counter, and EXTI pending clear.
- Pull-up / pull-down choice, timestamp source, debug route, no-power build,
  DMM evidence, and MCSDK integration remain unresolved.

Evidence limit:

- This is a no-power boundary draft only, not firmware source.
- It is not GPIO/EXTI runtime proof.
- DMM remains hardware-side deferred, not passed.
- No software Hall adapter implementation, runtime API, generated-code hook,
  MCSDK Hall integration, build record, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall
  closed-loop, motor readiness, power-stage readiness, or sensorless readiness
  is upgraded.

# 2026-05-27 Software Hall Firmware-Entry Checklist

New no-power firmware-entry checklist:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_checklist_2026-05-27.md`.

Decision: `Software Hall firmware-entry checklist / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.

Accepted checklist content:

- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it is not a current Hall candidate.
- The checklist freezes the conditions before any future STM32 adapter code:
  populated PCB2, DMM continuity / short-check table, GPIO/EXTI boundary
  review, timestamp-source decision, low-frequency debug route, no-power
  build-only record, and separate MCSDK firmware-integration review.
- First future code, if later authorized, must remain an independent adapter
  and must not modify TIM1 PWM, JEOC / FOC ISR, `HALL_M1`, MCSDK speed loop,
  Gate PWM, flash, Motor Profiler, Motor Pilot, or powered hardware.
- The next user checkpoint remains the one-sentence software Hall
  processing-order teach-back, not a hardware action while PCB2 is unpopulated.

Evidence limit:

- This is an entry checklist only, not firmware source.
- DMM remains hardware-side deferred, not passed.
- No software Hall adapter implementation, runtime API, generated-code hook,
  MCSDK Hall integration, build record, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall
  closed-loop, motor readiness, power-stage readiness, or sensorless readiness
  is upgraded.

# 2026-05-27 Software Hall MCSDK Integration Probe

New read-only no-power integration clue review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_integration_probe_2026-05-27.md`.

Decision: `MCSDK Hall integration points identified as read-only clues / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.

Read-only sources:

- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/main.c`
- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/mc_config.c`
- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/parameters_conversion.h`
- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/QIANSAI_G474_STDRIVE101_FOC_P2.ioc`
- `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/QIANSAI_G474_STDRIVE101_FOC_P2.log`

Accepted clue content:

- The generated route uses standard TIM2 hardware Hall clues:
  `HAL_TIMEx_HallSensor_Init`, `HALL_M1`, `M1_HALL_TIMER_SELECTION=HALL_TIM2`,
  and `M1_SPEED_SENSOR=HALL_SENSOR`.
- The generated log references `hall_speed_pos_fdbk.c/.h` and
  `speed_torq_ctrl.c/.h`.
- Current PCB2 software Hall remains `PA0/PA1/PB4`, with `PB3=LIN1`.
- Therefore current software Hall is not directly connected to MCSDK standard
  TIM2 Hall and cannot be used as Hall closed-loop evidence.

Evidence limit:

- This is a read-only clue review only.
- It is not firmware implementation, not MCSDK Hall integration, and not Hall
  readiness.
- No DMM, firmware build, flash, 24V, power-board connection, motor
  connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop,
  motor readiness, power-stage readiness, or sensorless readiness is upgraded.

# 2026-05-27 Software Hall Golden Vectors

New host-side no-power algorithm-contract artifact:
`tests/fixtures/software_hall_golden_vectors.json`.

Replay test:
`tests/test_software_hall_vectors.py`.

Review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_golden_vectors_review_2026-05-27.md`.

Decision: `Host-side software Hall golden vectors / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.

Accepted vector content:

- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it is not a current Hall candidate.
- Golden vectors cover the forward candidate cycle
  `001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001`.
- Golden vectors cover illegal-state rejection, repeated-state rejection,
  configurable bounce-candidate rejection, abnormal non-adjacent jump, and
  reverse adjacent step.
- `tests/test_software_hall_vectors.py` replays the JSON against
  `SoftwareHallStateMachine`.

Evidence limit:

- This is a host-side replay contract only.
- It is not STM32 firmware, not GPIO/EXTI runtime behavior, and not MCSDK Hall
  integration.
- No DMM, firmware build, flash, 24V, power-board connection, motor
  connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop,
  motor readiness, power-stage readiness, or sensorless readiness is upgraded.

# 2026-05-27 Software Hall Host Model

New host-side no-power algorithm artifact:
`src/software_hall_model.py`.

Tests:
`tests/test_software_hall_model.py`.

Review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_host_model_review_2026-05-27.md`.

Decision: `Host-side software Hall reference model / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.

Accepted model content:

- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it is not a current Hall candidate.
- The model implements valid-state filtering for `001/010/011/100/101/110`.
- The model rejects `000/111`.
- The model treats first valid state as baseline only.
- The model ignores repeated states as non-edges.
- The model supports configurable bounce/timing rejection without hard-coding a
  project threshold.
- The model counts forward/reverse adjacent steps and abnormal jumps.

Evidence limit:

- This is host-side executable algorithm evidence only.
- It is not STM32 firmware, not GPIO/EXTI runtime behavior, and not MCSDK Hall
  integration.
- No DMM, firmware build, flash, 24V, power-board connection, motor
  connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop,
  motor readiness, power-stage readiness, or sensorless readiness is upgraded.

# 2026-05-27 Software Hall Adapter Processing-Order Card

New no-power repair artifact:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_processing_order_card_2026-05-27.md`.

Decision: `Software Hall adapter processing-order teaching card / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.

Accepted card content:

- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it is not a current Hall candidate.
- The card explains why software Hall processing must follow:
  raw read -> illegal-state check -> first-valid check -> repeated-state check
  -> bounce/timing check -> forward/reverse adjacent check -> abnormal-jump
  count.
- It records the weak point that the user can classify individual rows but
  cannot yet restate the adapter sequence.
- It reduces the next user check to one Chinese sentence before any code review.

Evidence limit:

- This is a teaching card and no-power design-boundary record only.
- This is not firmware implementation, not MCSDK Hall integration, and not
  hardware validation.
- DMM remains hardware-side deferred, not passed.
- No software Hall adapter implementation, runtime API, generated-code hook,
  MCSDK Hall integration, build record, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall
  closed-loop, motor readiness, power-stage readiness, or sensorless readiness
  is upgraded.

# 2026-05-27 Software Hall Adapter Pseudocode Draft

New no-power design artifact:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_pseudocode_draft_2026-05-27.md`.

Decision: `Software Hall adapter pseudocode draft / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.

Accepted draft content:

- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it is not a current Hall candidate.
- The draft uses the 2026-05-27 Hall state-machine L2 learning evidence only
  as concept evidence.
- Future function responsibilities are documented for `Hall_ReadRaw3()`,
  `Hall_IsValidState()`, `Hall_IsForwardAdjacent()`,
  `Hall_IsReverseAdjacent()`, `Hall_CaptureEdge_ISR()`,
  `Hall_ProcessEvent()`, and `Hall_GetDebugSnapshot()`.
- The state-machine decision order is:
  illegal `000/111` -> repeated state -> forward/reverse adjacent transition
  -> abnormal jump.
- ISR work is limited to timestamp, raw Hall state, pending/event flag, and
  small counters.
- MCSDK hard stops are explicit: do not edit JEOC / FOC ISR, TIM1 PWM update,
  speed-loop feedback, or timing-critical generated paths without a separate
  integration review.

Evidence limit:

- This is pseudocode only, not firmware source.
- DMM remains hardware-side deferred, not passed.
- No software Hall adapter implementation, runtime API, generated-code hook,
  MCSDK Hall integration, build record, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall
  closed-loop, motor readiness, power-stage readiness, or sensorless readiness
  is upgraded.

# 2026-05-22 Software Hall State-Machine Exercise Card

New no-power user exercise card:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_state_machine_exercise_card_2026-05-22.md`.

Decision: `User Hall state-machine exercise requested / no firmware implementation / no Hall readiness`.

Accepted exercise content:

- The card is Chinese-first.
- It asks the user to explain why three Hall lines have six normal valid
  states.
- It asks why `000/111` must be illegal.
- It asks why `001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001` can be one
  direction candidate.
- It asks why `PA0/PA1/PB4` is software GPIO/EXTI Hall and not MCSDK standard
  TIM2 Hall.
- It asks why `PB3=LIN1` excludes `PB3` from current Hall use.
- It asks for a small user-filled table:
  `Input sequence | User judgment | Count edge? | Abnormal? | Note`.
- Required rows are `001 -> 101`, `001 -> 001`, `001 -> 010`, and `000`.

Evidence limit:

- This is a learning check and no-power algorithm exercise request only.
- No user answer has been reviewed yet.
- no user answer has been reviewed yet.
- This exercise does not open firmware implementation, MCSDK integration,
  build-only evidence, or any powered path.
- No software Hall pseudocode, firmware implementation, runtime API, MCSDK
  hook, DMM continuity proof, no-short proof, build record, flash, 24V,
  power-board connection, motor connection, Gate PWM output, Motor Profiler,
  Hall closed-loop, motor readiness, power-stage readiness, or sensorless
  readiness is upgraded.

# 2026-05-22 Software Hall No-Power Algorithm Prep

New no-power algorithm artifact:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_no_power_algorithm_prep_2026-05-22.md`.

Decision: `Algorithm-side no-power preparation / no firmware implementation / no Hall readiness`.

Accepted planning contract:

- Current route for the algorithm exercise is
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1`; it is not a current Hall candidate.
- Valid Hall state candidates are `001`, `010`, `011`, `100`, `101`, and
  `110`.
- `000` and `111` are illegal states and must not update accepted angle or
  speed.
- Repeated states do not count as new accepted edges.
- Non-adjacent jumps are abnormal and must not be treated as normal rotor
  movement.
- Candidate exercise sequences are recorded for forward and reverse direction.
- Low-frequency debug observables are defined for raw state, accepted state,
  edge count, illegal count, abnormal-jump count, repeat count,
  bounce-candidate count, edge delta, direction candidate, and speed candidate.
- ISR work remains minimal: capture timestamp/state only; no `printf`, JSON,
  blocking delay, dynamic allocation, WebSocket work, UART formatting, or
  control decisions.

DMM relationship:

- The DMM continuity / short-check gate is hardware-side deferred because PCB2
  is not populated yet.
- Deferred is not passed.
- This algorithm-prep work is allowed only because it is documentation and
  test-contract preparation, not firmware or hardware validation.

Evidence limit:

- No software Hall adapter has been implemented.
- No MCSDK speed/position feedback integration has been accepted.
- No DMM continuity proof, no-short proof, build record, flash, 24V,
  power-board connection, motor connection, Gate PWM output, Motor Profiler,
  Hall closed-loop, motor readiness, power-stage readiness, or sensorless
  readiness is upgraded.

# 2026-05-22 DMM Continuity / Short-Check Request

New no-power request:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/dmm_continuity_short_check_request_2026-05-22.md`.

Decision: `DMM continuity / short-check table requested / no measurement result yet / software Hall implementation still blocked`.

Requested exact rows:

- Continuity: `IA->PA0`, `IB->PA1`, `IC->PB4`, `PB3->LIN1`,
  `P14->3V3`, `P15->GND`, and `nFAULT->PB12`.
- Short checks: `3V3-GND`, `PA0/PA1/PB4/PB3/PB12` to `3V3/GND`, and
  `IA-IB`, `IA-IC`, `IB-IC`.

Evidence limit:

- This is a measurement request/template only.
- No filled DMM result exists yet.
- The 2026-05-27 no-power build-only result now provides local compile
  evidence, but it is not the current real-world hardware-progress blocker and
  does not replace DMM evidence.
- Software Hall adapter implementation, MCSDK integration, Hall closed-loop,
  Gate PWM, Motor Profiler, motor readiness, power-stage readiness, and
  sensorless readiness remain blocked.

# 2026-05-21 Current PCB2 Software Hall Route Confirmation

Decision: `Software Hall route confirmed for no-power adapter planning / no firmware implementation / no Hall readiness`.

Accepted exact clues:

- User confirmed the current PCB2 mapping used for this decision has no known
  error.
- `P14/P15` are confirmed as `3V3/GND`; they are no longer a route-selection
  blocker, while no-power continuity and short checks remain required before
  any powered stage.
- Current PCB2 Hall route is
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- Current PCB2 `PB3` is `LIN1` / low-side PWM driver input. It is not a
  current Hall candidate.
- Software Hall adapter is the preferred no-PCB-change route. Hardware rework
  is fallback only if later MCSDK integration cannot safely consume or isolate
  the software Hall route.
- MCSDK standard TIM2 Hall `PA15/PB3/PB10` is not the current PCB2 Hall route
  and cannot be used directly as current-board Hall proof.

Blocked exact fields:

- No software Hall adapter has been implemented.
- No MCSDK integration point, runtime API, generated-code hook, speed/position
  feedback path, continuity record, build record, flash, 24V, power-board
  connection, motor connection, Gate PWM output, Motor Profiler, Hall
  closed-loop, motor readiness, power-stage readiness, or sensorless readiness
  is upgraded.

# 2026-05-21 Packet A Generated-Source Side-Effect Review

New source review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md`.

Decision: `Packet A selected fields accepted for no-power configuration evidence / build-only source prerequisite satisfied / later no-power Debug build-only pass recorded / hardware trust still blocked`.

Accepted exact clues:

- Workbench-generated source records `FOC`, `NUCLEO-G474RE`,
  `STM32G474RETx`, `MY-STDRIVE101_POWER_BOARD`, and `STDRIVE101`.
- TIM1 complementary PWM is visible as `PA8/PA9/PA10` plus
  `PB13/PB14/PB15`.
- Fault/break configuration records `PB12/TIM1_BKIN`,
  `TIM_BREAK_ENABLE`, and generated `TIM_BREAKINPUTSOURCE_BKIN`.
- Current sensing records three-shunt amplified current sensing and
  `PWMC_R3_2_Handle_t` / ADC injected conversion paths.
- Hall is generated as TIM2 Hall on `PA15/PB3/PB10`.
- USART2 is generated on `PA2/PA3`.
- Static search found no `SIX_STEP`, `sixstep`, `mc_tasks_sixstep`,
  `pwmc_sixstep`, or `speed_duty_ctrl` in the archived generated-project
  clue folder.

Blocked exact fields:

- Current PCB2 Hall remains `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`, which does
  not match the generated TIM2 Hall route.
- Current PCB2 records `PB3=LIN1`, while the generated Workbench route uses
  `PB3` as TIM2 Hall H2.
- `R57BLB50L2` remains a Workbench placeholder motor, not measured project
  motor evidence.
- Packet B route proof, Packet C protection proof, no-power continuity, build
  record, flash, 24V, power-board connection, motor connection, Gate PWM
  output, Motor Profiler, Hall closed-loop, motor readiness, power-stage
  readiness, and sensorless readiness remain blocked.
- CLI build execution was not attempted because `ninja` and
  `arm-none-eabi-gcc` were not found in PATH or targeted local toolchain
  searches. This is a toolchain-path blocker, not an MCSDK generated-project
  failure.

# 2026-05-19 MY_FOC Manual FOC Edit Rollback

Codex backed up and then restored the source Workbench project:
`C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6`.

Backup:
`C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6.pre_codex_foc_edit_2026-05-19.bak`.

Edit record:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/my_foc_foc_candidate_edit_2026-05-19.md`.

Decision: `Manual FOC source edit failed Workbench reload / rolled back / Packet A still not accepted`.

Accepted exact clues:

- A one-field manual edit from `"algorithm": "sixStep"` to `"algorithm": "FOC"`
  made Workbench unable to load the file.
- The user reported `娑撯偓閼割剟鏁婄拠?/ 閺冪姵纭堕崝鐘烘祰閺傚洣娆?
  C:/Users/gregrg/.st_workbench/projects/MY_FOC.stwb6`.
- Codex restored the external source from backup.
- The current external source again reads `"algorithm": "sixStep"` and matches
  the backup SHA256:
  `062B78AD8E07B5A29A68A007797200FCD4833FE9D3371D2821F3A54D5B9429FD`.

Blocked exact fields:

- The failed manual FOC candidate is negative evidence only.
- Generated `MY_FOC.ioc`, `MY_FOC.wbdef`, `Src/`, and `Inc/` still reflect the
  old generated six-step outputs.
- No Generate, build, flash, 24V, power-board connection, motor connection, No
  Gate PWM output readiness, Motor Profiler readiness, Hall readiness, motor
  readiness, power-stage readiness, or sensorless readiness is upgraded.
- Packet A still not accepted and no generated-project trust is added.

# 2026-05-19 MY_FOC Generated Project Source Review

New user-created Workbench project source:
`C:\Users\gregrg\.st_workbench\projects\MY_FOC`.

Archived selected no-power source files:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-19_my_foc_generated_project/`.

New source review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_005_my_foc_generated_project.md`.

Decision: `Partial clue / generated project quarantined / Packet A not accepted`.

Accepted exact clues:

- MC Workbench 6.4.2 generated a real `MY_FOC` project on this machine.
- MCU/control context is `NUCLEO-G474RE`, `STM32G474RETx`, and
  `STM32G474RE`.
- Power-board naming includes `M1_POWERBOARD_NAME=~MY-STDRIVE101_POWER_BOARD`
  and `M1_PWM_DRIVER_PN=STDRIVE101`.
- Hall sensor selection exists in the generated configuration.
- The user clarified that pins can be changed; therefore the current Hall/PWM
  mismatch is a future editable route, not a permanent rejection.

Blocked exact fields:

- The project is `SIX_STEP`, not FOC.
- Generated sources include `mc_tasks_sixstep.c`, `pwmc_sixstep.c`, and
  `speed_duty_ctrl.c`.
- Current sensing is disabled: `M1_CUR_READING=false`.
- Fault/break is disabled: `TIM1.BreakState=TIM_BREAK_DISABLE`.
- Generated Hall `PA15/PB3/PB10` and generated PWM
  `PA8/PB13/PA9/PB14/PA10/PB15` are not accepted as the current PCB2 route.
- Motor entry `R57BLB50L2` / `MOONS motor for Zest Demo` is not the project
  motor evidence.
- Packet A not accepted. No generated-project trust, build-only clearance,
  No Gate PWM output readiness, Motor Profiler readiness, Hall readiness, motor readiness,
  power-stage readiness, or sensorless readiness is upgraded.

# 2026-05-19 Packet A Board Designer / Board Manager Path Review

New no-power Packet A path review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_board_designer_manager_path_review_2026-05-19.md`.

Decision: `Board Designer / Board Manager path exists as local documentation
and tool clue / Packet A still blocked`.

Accepted governance updates:

- Workbench `wb2mx.properties` exposes Board Designer and Board Manager as
  external tools.
- Local `STMCBoardDesigner.exe` and `STMCBoardManager.exe` are present.
- Local `STMCBD-UM.pdf` describes creating Power, Control, and Inverter boards,
  importing external boards, custom board clone/modify/delete operations, and
  Board Aggregation from control-board plus power-board choices.
- The path is now documented enough to define a future no-power custom/user
  board capture task for the self-developed STDRIVE101 board.

Blocked exact fields:

- Packet A not accepted.
- Built-in `EVALSTDRIVE101`, `STEVAL-LVLP01`, and `EVLDRIVE101-HPD` remain
  non-substitutes for the project self-developed STDRIVE101 board.
- No custom board source, project-specific `.stwb6`, selected-field
  screenshot, generated project, build-only clearance, firmware, runtime API,
  continuity, Hall readiness, Motor Profiler readiness, motor readiness,
  power-stage readiness, or sensorless readiness is upgraded.
- Generated-project trust remains `Not allowed`; no generated-project trust is
  added by this review.

# 2026-05-19 Software Hall Adapter Design Review

New no-power software Hall adapter design review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_design_review_2026-05-19.md`.

Decision: `Software Hall adapter remains no-power design review / Packet A not accepted`.

Accepted governance updates:

- Current PCB2 Hall route stays `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`.
- The review defines future GPIO/EXTI sampling candidates, edge timestamping,
  valid-state filtering, bounce/repeated-state rejection, minimal ISR
  responsibility, and MCSDK integration boundaries.
- The review explicitly avoids function names, buffers, public runtime APIs,
  MCSDK hooks, generated source, and firmware implementation.
- Hard stops are now written: same-timer hardware Hall requirements, invasive
  high-frequency FOC / JEOC edits, time-critical blocking logic, missing
  build-only verification boundary, or unexplainable MCSDK consumption of
  software Hall state all lead to a separate `hardware-rework planning` task.

Blocked exact fields:

- Packet A selected fields are not accepted.
- Generated-project trust remains `Not allowed`.
- Build-only generated-project clearance remains closed.
- No software Hall adapter is implemented or accepted by MCSDK.
- No runtime API, generated source, build, flash, no-power continuity, powered
  readiness, Hall readiness, Motor Profiler readiness, motor readiness, or
  sensorless readiness is upgraded.

# 2026-05-19 Current PCB2 Packet A / Firmware Feasibility Review

New no-power feasibility review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/current_pcb2_packet_a_firmware_feasibility_2026-05-19.md`.

Decision: `No-PCB-change route remains feasibility only / Packet A not accepted`.

Accepted governance updates:

- Current PCB2 PWM / driver-input route was reviewed against local
  `STM32G474RETx` pin-function clues.
- The route is not cleared as standard MCSDK `TIM1` complementary PWM
  selected-field evidence.
- Current PCB2 Hall route `PA0/PA1/PB4` is not cleared as same-timer hardware
  Hall.
- The no-PCB-change path remains open only as later firmware feasibility
  review for software Hall sampling, timestamping, valid-state filtering, and
  MCSDK integration boundaries.

Blocked exact fields:

- Packet A selected fields are not accepted.
- Generated-project trust remains `Not allowed`.
- Build-only generated-project clearance remains closed.
- No concrete software Hall adapter is implemented or accepted.
- No hardware rework is executed or authorized.
- No continuity, power-stage readiness, Hall readiness, Motor Profiler
  readiness, motor readiness, or sensorless readiness is upgraded.

# 2026-05-19 Current PCB2 Hall/PWM No-Power Strategy Review

New no-power strategy review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/current_pcb2_hall_pwm_strategy_2026-05-19.md`.

Decision: `No-power strategy review opened / no PCB change first`.

Accepted governance updates:

- Current PCB2 PWM / driver-input route under review is
  `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10`.
- Current PCB2 Hall route remains `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`.
- The old standard `TIM1` complementary PWM draft and old
  `PA15/PB3/PB10` hardware Hall draft are historical or alternate candidates
  only. They are not accepted current PCB2 configuration evidence.
- `PA0/PA1/PB4` is not a same-timer hardware Hall set. Software Hall remains
  a future no-power Packet A / firmware design review topic, not Hall
  readiness.
- `PB3` is current PCB2 `LIN1`, not current PCB2 `HALL_B`; any alternate
  Hall use of `PB3` still needs SWO release/isolation and a new accepted route.

Blocked exact fields:

- No accepted Workbench selected-field screenshot or project-specific `.stwb6`
  proves the current PCB2 PWM/Hall choices.
- No generated-project trust, build-only clearance, no-power continuity,
  power-stage readiness, Hall readiness, Motor Profiler readiness, motor
  readiness, or sensorless readiness is upgraded by this strategy review.
- No hardware rework is executed or authorized in this task.

# 2026-05-19 PCB2 Mapping / Pin-1 / Protection Intake

New current PCB2 mapping source packet:
`hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/`.

New Packet B/C plus PB3/SWO/Hall no-power review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md`.

Decision: `Partial clue / accepted current PCB2 mapping source; Hall/PWM
conflicts clarified`.

Accepted exact clues:

- The user states the answer corresponds to current PCB2.
- The source provides a P1-P15 mapping from board-side functions to NUCLEO
  positions and STM32 pins, including `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3`,
  `ADC_U/ADC_V/ADC_W`, `IA/IB/IC`, `nFAULT`, `3V3`, and `GND`.
- Two pin-1 / connector-orientation images are archived.
- Hall relationship is stated as `HALL_A -> U/IA`, `HALL_B -> V/IB`,
  `HALL_C -> W/IC`.
- A later clarification image states `PC7/PB3/PB10` was an alternate suggestion,
  not current PCB2 physical routing. Current PCB2 physical Hall route is
  `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`.
- `IA/IB/IC` are Hall signal nets after pull-up/filtering; `ADC_U/ADC_V/ADC_W`
  are current-sense nets.
- STDRIVE101 protection-chain intent is stated as `DT/MODE -> GND`,
  `CP -> 100 nF -> GND`, `SCREF` divider `33 k / 20 k`, `nFAULT` 10 k pull-up
  to 3.3 V, and no separate `STBY` pin.

Blocked exact fields:

- `PB3` / `PB10` apparent conflicts are clarified: `PB3` is current PCB2
  `LIN1`, `PB10` is current PCB2 `HIN2`, and the Hall rows using
  `PC7/PB3/PB10` are alternate suggestions.
- Current PCB2 Hall route `PA0/PA1/PB4` still needs a software Hall or firmware
  design decision because it is not a normal same-timer three-channel Hall
  input set.
- SWO release is described but not captured as an accepted final CubeMX /
  Workbench project state. The older 2026-05-17 pin table still does not
  release SWO by itself.
- Packet A selected fields, timer alternate-function compatibility,
  generated-project trust, no-power continuity, powered readiness, Motor
  Profiler readiness, Hall readiness, motor readiness, and sensorless readiness
  remain unchanged and not allowed.

# 2026-05-19 Minimal Hardware Request And Workbench Asset Probe

New minimal hardware-teammate request:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/hardware_teammate_min_request_2026-05-19.md`.

New Packet A local asset probe:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_workbench_asset_probe_2026-05-19.md`.

Decision: `Workflow/evidence governance only`.

Accepted exact governance updates:

- Hardware teammate should first provide three P0 items: exact Gerber PCB2
  revision confirmation, complete `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping,
  and marked `CN3` / `J_HALL` pin-1 orientation evidence.
- The full handoff remains in
  `hardware_supplement_handoff_2026-05-19.md` for Hall A/B/C mapping, PB3/SWO,
  STDRIVE101 protection details, optional PCB source, and later no-power DMM
  continuity / short-check records.
- Workbench local config references installed Board Designer and Board Manager
  tools, and the installed hardware assets contain built-in STDRIVE101 board
  definitions such as `EVALSTDRIVE101`, `STEVAL-LVLP01`, and
  `EVLDRIVE101-HPD`.

Blocked exact fields:

- No custom self-developed STDRIVE101 board definition is accepted.
- No project-specific `.stwb6`, legacy `.stmcx`, selected-field screenshot,
  generated source, build, flash, or hardware action exists.
- Built-in ST board definitions remain non-substitutes for the project driver
  board.
- Packet A/B/C, PB3/SWO, `J_HALL`, generated-project trust, continuity,
  powered readiness, motor readiness, Hall readiness, Motor Profiler readiness,
  and sensorless readiness remain unchanged.

# 2026-05-19 Gerber PCB2 Manufacturing Package Intake

New Gerber package:
`hardware/schematic/2026-05-19_gerber_pcb2_stdrive101/Gerber_PCB2_2026-05-19.zip`.

New Packet B/C no-power review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_003_gerber_pcb2.md`.

Decision: `Partial clue / accepted board-side Gerber + flying-probe net clue`.

The ZIP is a same-day Gerber manufacturing package supplied after the
self-developed STDRIVE101 driver-board `.epro` source. It contains top/bottom
copper, two inner copper layers, solder mask, paste mask, silkscreen, board
outline, drill files, and `FlyingProbeTesting.json`. Gerber headers record
`EasyEDA Pro v3.2.91`, generated `2026-05-19 11:16:57`. The archived ZIP hash
is SHA256 `F61C073C5A9E71CD608460976430D3F927E7AD48EC05A42661E77662AF04CE56`.

Accepted exact board-side clues:

- `CN3` flying-probe pad/net table:
  `1 HIN1`, `2 LIN1`, `3 HIN2`, `4 LIN2`, `5 HIN3`, `6 LIN3`,
  `7 ADC_U`, `8 ADC_V`, `9 ADC_W`, `10 IA`, `11 IB`, `12 IC`,
  `13 NFAULT`, `14 3V3`, `15 GND_SIGNAL`.
- `U1=STDRIVE101` pad nets include `$2N118` for the `CP` pin position,
  `GND_POWER` for the `DT/MODE` pin position, plus `SCREF`, `24V_FUSED`,
  `REG12`, `NFAULT`, `INx`, `ENx`, `BOOTx`, `GHSx`, `GLSx`, and `OUTx`.
- PWM input paths are visible at pad-net level:
  `R4 HIN1-IN1`, `R8 LIN1-EN1`, `R5 HIN2-IN2`, `R6 LIN2-EN2`,
  `R7 HIN3-IN3`, `R9 LIN3-EN3`.
- Protection/current-sense pad-net clues are visible:
  `R3 NFAULT-3V3`, `R1 SCREF-3V3`, `R2 GND_SIGNAL-SCREF`,
  `C4/C5 REG12-GND_SIGNAL`, `D1/D2/D3 REG12-to-BOOTx`,
  and `R12/R14/R17 ADC_U/V/W-GND_POWER`.
- Connector clues are visible:
  `U2=J_HALL` has `+5V`, `GND_SIGNAL`, and three signal paths through
  `R22/R23/R24` to `IA/IB/IC`; `CN2=J_MOTOR` has `OUT1/OUT2/OUT3`.

Blocked exact fields:

- No NUCLEO `CN8` endpoint, STM32 pin mapping, or harness/adapter mapping is
  present in this package.
- Exact fabrication/revision match still needs user or hardware teammate
  confirmation before it can be treated as final build evidence.
- `CP` is present only as unnamed net `$2N118`; `STBY` was not observed.
- `J_HALL` physical pin-1 orientation and Hall A/B/C numbering are not
  accepted.
- PB3/SWO release, Packet A/Workbench selected fields, generated-project
  trust, continuity checks, power-stage readiness, Motor Profiler readiness,
  motor readiness, and sensorless readiness remain unchanged.

# 2026-05-19 ProDoc P1 EDA Pro Source Intake

New self-developed STDRIVE101 driver-board source:
`hardware/schematic/2026-05-19_prodoc_p1_stdrive101_epro/ProDoc_P1_2026-05-19.epro`.

New Packet B/C no-power review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_002_prodoc_p1_epro.md`.

Decision: `Partial clue / accepted schematic-source clue`.

The `.epro` is a readable EDA Pro schematic source for the user-confirmed
self-developed STDRIVE101 driver board. Parsed metadata shows
`STDRIVE101_3Phase_Inverter`, board `Schematic1`, sheet `P1`, create/update
date `2026-05-19`, and create/update time `10:26:36`. The archived file hash
is SHA256 `B9D67B9E5D6DD08D5229928636DFA8048C081DED7EE230ADDB79F20D83D718A1`.

Accepted exact schematic clues:

- `U1=STDRIVE101`.
- `Q1-Q6=NCEP40T11G`.
- `R12/R14/R17=20mOhm` shunt resistors.
- `CN3=2.54mm-15P ZZ` board-side control connector.
- `U2=J_HALL`, `CN2=J_MOTOR`.
- `CN3` board-side pinout:
  `1 HIN1`, `2 LIN1`, `3 HIN2`, `4 LIN2`, `5 HIN3`, `6 LIN3`,
  `7 ADC_U`, `8 ADC_V`, `9 ADC_W`, `10 IA`, `11 IB`, `12 IC`,
  `13 NFAULT`, `14 3V3`, `15 GND_SIGNAL`.
- `J_HALL` schematic clue: `+5V`, `GND_SIGNAL`, and three signal paths
  through `R22/R23/R24=100 ohm` into `IA/IB/IC`.
- STDRIVE101 schematic clues: `NFAULT`, `REG12`, `SCREF`, `BOOTx`, `OUTx`,
  `GHSx`, and `GLSx` are visible. `DT/MODE` appears tied to `GND_POWER` at
  the STDRIVE101 pin, but this remains a clue pending dedicated review.

Blocked exact fields:

- The archive contains no PCB layout data: `project.json` has `pcbs: {}`, the
  board entry has an empty `pcb` field, and `PCB/` is only an empty directory
  entry.
- No NUCLEO `CN8` endpoint or STM32 pin mapping is proven.
- `CP` has no explicit parsed net label, `STBY` was not observed, and the
  protection thresholds/fault-release path still need review.
- PB3/SWO release, `J_HALL` numbering, Hall readiness, power-stage readiness,
  Packet A/Workbench selected fields, generated-project trust, Motor Profiler
  readiness, motor readiness, and sensorless readiness remain unchanged.

# 2026-05-19 Packet A Workbench Capture Attempt

New Packet A no-power capture-attempt review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_001_packet_a_workbench_capture_attempt.md`.

New Workbench screenshots:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_launch_fullscreen.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_after_new_project.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_motor_control_kit_selected.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_board_path_probe.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_power_slot_search_stdrive101_exact.png`

Decision: `Partial clue / stopped`.

Accepted exact clue: Workbench 6.4.2 Desktop launches, and the component path
can show `NUCLEO-G474RE` / `STM32G474RETx` as the control-board context.

Blocked exact fields: no project-specific `.stwb6`, no accepted Custom /
Generic self-made STDRIVE101 power-stage context, and no selected-field
screenshots for PWM, current sensing, Hall/sensorless, driver protection, or
pin usage. User clarified on 2026-05-19 that the project uses a self-developed
motor driver board based on the STDRIVE101 chip, so built-in ST board entries
such as `EVALSTDRIVE101` or `STEVAL-LVLP01` cannot be used as board-match
substitutes.

Packet A remains `Partial clue / Preparation only`. Generated-project trust
remains `Not allowed`. Packet B/C, CN8 routing, STDRIVE101 protection-path
proof, PB3/SWO release, `J_HALL`, Hall readiness, power-stage readiness, Motor
Profiler readiness, motor readiness, and sensorless readiness remain unchanged.

# 2026-05-18 PB3 / SWO CubeMX Probe

New PB3/SWO no-power review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-18_002_pb3_swo_probe.md`.

New evidence files:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-18_cubemx_pb3_current_swo_fullscreen.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/pb3_tim2_ch2_probe_2026-05-18.ioc`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-18_cubemx_pb3_tim2_ch2_probe_fullscreen.png`

Decision: `Partial clue`.

The existing NUCLEO-G474RE no-power draft still records
`PB3.GPIO_Label=T_SWO` and `PB3.Signal=SYS_JTDO-SWO`; the new CubeMX screenshot
preserves that current state. A separate dated probe `.ioc` changes only the
copy to `PB3.GPIO_Label=HALL_B_PROBE` and `PB3.Signal=TIM2_CH2`, and CubeMX can
open that probe. This is a configuration-layer clue only. It does not prove
NUCLEO SWO release / isolation, Workbench Hall B selection, CN8 / `J_HALL`
endpoint mapping, Hall readiness, or any powered behavior.

`PB3` remains blocked for Hall B until separate SWO release / isolation evidence
and board-route endpoint evidence arrive. Packet A/B/C, generated-project
trust, CN8 routing, STDRIVE101 protection-path proof, Hall closed-loop,
power-stage readiness, Motor Profiler readiness, motor readiness, and sensorless
readiness are unchanged.

# 2026-05-17 Vendor Motor And G431 Pin Table Update

New motor source:
`hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.md`.

New hardware teammate pin-table source:
`hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.md`.

New MCU pin compatibility check:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/mcu_pin_compatibility_check_2026-05-17.md`.

Review record:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`.

Decision: `Partial clue`.

The supplier motor table supports a better no-power Workbench label,
`57BLF01_VENDOR_CANDIDATE`, but it does not provide project-measured motor
parameters or Motor Profiler data. The hardware teammate pin table is titled
for `STM32G431RB`; the teammate states the relevant G431/G474 pins are the
same, and local MCSDK `STM32G431RBTx` / `STM32G474RETx` asset comparison
supports the compared key rows. This still does not accept CN8 routing,
`J_HALL` connector numbering, `PB3` / SWO release, or OPAMP/VCP policy.

Generated-project trust remains `Not allowed`.

# 2026-05-16 Packet A Custom Capture Package Update

The old `My_First_FOC.stwb6` file is now explicitly treated as a legacy
toolchain-learning leftover, not the intended project-specific Packet A source.
Its arbitrary `EVALSTDRIVE101` power-board choice remains a reason it cannot be
accepted for the custom board.

New package:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`.

New preparation review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`.

Decision: `Partial clue / Preparation only`.

The package defines the next no-power Workbench capture path for
`NUCLEO-G474RE` / `STM32G474RETx`, a Custom / Generic STDRIVE101 power stage,
FOC, Hall fallback, 3-shunt current sensing, `57BLF01_VENDOR_CANDIDATE`
supplier-clue motor label, a
no-power motor measurement log, and a pin assignment table. It still does not
contain a real new `.stwb6` or selected-field Workbench screenshot.

Generated-project trust remains `Not allowed`.

# 2026-05-15 Packet A STWB6 Candidate Update

Codex found the real ST MC Workbench 6.4.2 launcher at
`F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\STMCWB.exe` and preserved
`F:\STMCSDK\My_First_FOC.stwb6` under
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`.

Review record:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`.

Decision: `Partial clue`.

Accepted from the file: MCSDK 6 `.stwb6` project format, Workbench version
`6.4.2`, algorithm `FOC`, control board `NUCLEO-G474RE`, and MCU
`STM32G474RETx`.

Still not accepted: final custom-board context, selected TIM1 complementary PWM
topology, final `NFAULT` / `PB12/TIM1_BKIN` selection, custom-board current
sensing, Hall/sensorless final selection, `PA2/PA3` policy, `PB3` ownership,
and generated-project trust.

Current decision: Packet A has a source candidate, but generated-project trust
remains `Not allowed`.

# P2 鐠囦焦宓侀崠?- 2026-05-14

鏉╂瑤閲滈弬鍥︽鐠佹澘缍嶈ぐ鎾冲娴犳挸绨遍柌灞糕偓婊呮埂閻ㄥ嫭婀佺拠浣瑰祦閳ユ繄娈戦崘鍛啇閵嗗倸鐣犻惃鍕稊閻劋绗夐弰顖涙殌娴ｇ姵甯寸痪鍖＄礉
娑旂喍绗夐弰顖滄晸閹存劕娴愭禒璁圭礉閼板本妲哥敮顔荤稑閸掋倖鏌囬敍姘憿娴滄稐绗㈢憲璺ㄥ箛閸︺劌褰叉禒銉ф祲娣団槄绱濋崫顏冪昂鏉╂ê褰ч弰顖濆磸濡楀牞绱?
閸濐亙绨烘导姘幢娴ｅ繐鎮楃紒?MCSDK 瀹搞儳鈻奸妴?

## 鐎瑰鍙忔潏鍦櫕

鏉╂瑤閲滅拠浣瑰祦閸栧懍绗夐幒鍫熸綀娴犺缍嶆稉濠勬暩閹存牜鏁搁張鍝勫З娴ｆ粣绱?

- 娑撳秵甯?24V閿?
- 娑撳秵甯撮崝鐔哄芳閺夊尅绱?
- 娑撳秵甯撮悽鍨簚閿?
- 娑撳秷绶崙?Gate PWM閿?
- 娑撳秷绻嶇悰?Motor Profiler閿?
- 娑撳秴锛愮粔?Hall 闂傤厾骞嗗鑼病妤犲矁鐦夐敍?
- 娑撳秴锛愮粔?SMO / 閺冪姵鍔呴幒褍鍩楀鑼病妤犲矁鐦夐妴?

## 瑜版挸澧犳禒鎾崇氨闁插本婀佹禒鈧稊?

| 濡偓閺屻儵銆?| 瑜版挸澧犵紒鎾寸亯 | 鏉╂瑨顕╅弰搴濈矆娑?|
| --- | --- | --- |
| `.stmcx` 閺傚洣娆?| `rg --files -g "*.stmcx"` 閸?GUI 鐏忔繆鐦崜宥呮倵闁姤鐥呴張澶嬪閸掗鎹㈡担鏇熸瀮娴犺翰鈧?| 鏉╂ɑ鐥呴張?Motor Control Workbench 瀹搞儳鈻奸弬鍥︽閵?|
| CubeMX `.ioc` 閼藉顢?| `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`閵?| 鐠囦焦妲?NUCLEO-G474RE 閺夊灝宕遍崗銉ュ經閵嗕梗PB12/TIM1_BKIN`閵嗕梗PB14/TIM1_CH2N`閵嗕梗PA2/PA3` VCP閵嗕梗PB3` SWO 瀹歌弓绻氱€涙ê鍩?CubeMX 闁板秶鐤嗙仦鍌︾幢娴犲秳绗夐弰?`.stmcx` 閹?MCSDK MotorControl 瀹搞儳鈻奸妴?|
| GUI 閹搭亜娴?| `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png`閿涘畭screenshots/2026-05-14_cubemx_ioc_launch_attempt.png`閵嗕梗screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`閿涘奔浜掗崣?2026-05-18 `screenshots/2026-05-18_cubemx_pb3_current_swo_fullscreen.png` 閸?`screenshots/2026-05-18_cubemx_pb3_tim2_ch2_probe_fullscreen.png`閵?| 妫ｆ牠銆夐幋顏勬禈鐠囦焦妲?CubeMX 閹垫挸绱戦敍?026-05-14 閹搭亜娴樼拠浣规娣囨繂鐡ㄩ惃?NUCLEO `.ioc` 閸欘垰婀?CubeMX `Pinout & Configuration` 妞ょ敻娼伴幍鎾崇磻閿?026-05-18 閹搭亜娴樼拠浣规瑜版挸澧犻懡澶嬵攳娴犲秵妯夌粈?`PB3` 娑?SWO閿涘苯褰熸稉鈧稉?probe 閸擃垱婀伴崣顖涙▔缁€?`PB3` 娑?`HALL_B_PROBE`閵嗗倸鐣犳禒顑跨矝娑撳秷鐦夐弰?MotorControl/Workbench 闁板秶鐤嗛妴涓糤O 閻椻晝鎮婇柌濠冩杹閹?Hall endpoint閵?|
| PB3/SWO probe | `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/pb3_tim2_ch2_probe_2026-05-18.ioc`閵?| 鏉╂瑦妲告禒搴″斧 `.ioc` 婢跺秴鍩楅崙铏规畱闁板秶鐤嗙仦?probe閿涘苯褰ч幎?`PB3` 閺€閫涜礋 `TIM2_CH2` / `HALL_B_PROBE` 楠炲墎鏁?CubeMX 閹垫挸绱戦幋顏勬禈閿涙稑鐣犳稉宥嗘禌娴狅絽甯懡澶嬵攳閿涘奔绡冩稉宥堢槈閺?NUCLEO SWO 闁插﹥鏂侀妴涓哊8 / `J_HALL` endpoint 閹?Hall readiness閵?|
| GUI 閹规洝骞忕紒鎾寸亯 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_result_2026-05-14.md`閵?| 鐠佹澘缍嶉張顒冪枂 GUI fallback 鐠囦焦宓侀妴涔?ioc` 鐠囪娲栭妴浣瑰焻閸ユ崘鐭惧鍕嫲 `.stmcx` / MotorControl 娴犲秹妯嗘繅鐐偓?|
| Workbench 閸忋儱褰涢幒銏＄ゴ | `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`閵?| 鐠佹澘缍?repo閵嗕竼ubeMX 鐎瑰顥婇惄顔肩秿閵嗕府CSDK package閵嗕箓S Code STM32 extension閵嗕梗.stm32cubemx` 閸滃苯鐖剁憴?ST 鐎瑰顥婇惄顔肩秿閻ㄥ嫮娲伴弽鍥ㄥ赴濞村绱辩涵顔款吇 MotorControl package 閺佺増宓佺€涙ê婀敍灞肩稻娴犲秵鐥呴張?`.stmcx` 閹存牜瀚粩?Workbench launcher 鐠囦焦宓侀妴?|
| 閺夎法楠囩挧鎵殠鐠囦焦宓?| 娴犳挸绨遍柌灞炬箒 `hardware/schematic/2026-05-09_power_board_schematic_screenshot.jpg`閵嗕礁顕惔鏃囶嚛閺勫函绱濇禒銉ュ挤 2026-05-15 閺傛澘顕遍崗銉ф畱 `hardware/schematic/2026-05-15_power_board_cn8_stdrive101_schematic_candidate.png` / `.md`閵?| 2026-05-15 閹搭亜娴橀崣顖濐嚢閹勬纯婵傛枻绱濋悽銊﹀煕瀹歌尙鈥樼拋銈呯暊鐎电懓绨茶ぐ鎾冲閻椻晝鎮婇崝鐔哄芳閺夊じ绗栭悽杈┾€栨禒璺烘倱鐎涳箒鍤滅紒姗堢礉閼虫垝缍旀稉?Packet B/C 閸婃瑩鈧鎷?`Partial clue`閿涙稐绲剧紓鐑橆劀瀵?source revision/date閵嗕讣TM32 缁旑垳鍋ｉ弰鐘茬殸閵嗕梗DT/MODE` 缁旑垳鍋ｇ拠浣规閸?`STBY` 鐠囦焦妲戦敍灞惧娴犮儰绮涙稉宥嗘Ц accepted CN8 / EDA / netlist 鐠ф壆鍤庣拠浣规閵?|
| STDRIVE101 鐠у嫭鏋?| 閺堫剙婀村鍙夋箒 STDRIVE101 PDF閵嗕焦褰侀崣鏍ㄦ瀮閺堫剙鎷?digest閵?| 閸欘垯浜掗悽銊︽降閸嬫矮绻氶幎銈堢熅瀵板嫬顓搁弻銉礉娴ｅ棜绻曟稉宥堝厴鐠囦焦妲戞担鐘垫畱閸旂喓宸奸弶鍨杽闂勫懏鈧簼绠炴潻鐐偓?|
| STDRIVE101 娣囨繃濮㈢捄顖氱窞鐎光剝鐓?| `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`閵?| 瀹稿弶濡?`DT/MODE`閵嗕梗nFAULT`閵嗕梗REG12`閵嗕梗CP`閵嗕梗SCREF`閵嗕梗VS/VM`閵嗕攻ootstrap閵嗕够tandby 閸?VDS monitoring 閸ュ搫瀵查幋鎰繁鐠囦胶鐓╅梼纰夌幢鏉╂瑤绮涢崣顏呮Ц鐎光剝鐓＄憴鍕灟閿涘奔绗夐弰顖涙緲缁狙団偓姘崇箖鐠囦焦宓侀妴?|

## 鐠囦焦宓佺粵澶岄獓

| 缁涘楠?| 闂団偓鐟曚椒绮堟稊鍫ｇ槈閹?| 瑜版挸澧犻悩鑸碘偓?| 瑜版挸澧犻崘鍐茬暰 |
| --- | --- | --- | --- |
| A | Workbench/CubeMX `.stwb6` / `.stmcx`, configuration screenshots, or readable generated source showing `STM32G474RETx`, selected PWM/Hall route, `PB12/TIM1_BKIN`, `PA2/PA3` policy, and `PB3` ownership. | 2026-05-21 generated-source side-effect review accepts selected Packet A fields: `FOC`, `NUCLEO-G474RE`, `STM32G474RETx`, `MY-STDRIVE101_POWER_BOARD`, TIM1 complementary PWM, `PB12/TIM1_BKIN`, three-shunt current sensing, TIM2 Hall `PA15/PB3/PB10`, and USART2 `PA2/PA3`. | Trust Workbench configuration intent and build-only source prerequisite only. Do not trust current PCB2 physical Hall/PWM routing, CN8 continuity, STDRIVE101 protection behavior, build success, or hardware readiness. |
| B | NUCLEO 鏉╃偞甯撮崳銊ユ嫲閻掑﹥藟鐠囦焦宓侀敍宀冾嚛閺?VCP/SWO 閸掓澘绨抽崡鐘辩瑝閸楃姴顕惔鏂跨穿閼存哎鈧?| `.ioc` 瀹歌弓绻氱€?`PA2/PA3` 娑?VCP閵嗕梗PB3` 娑?SWO閿?026-05-19 瑜版挸澧?PCB2 閺勭姴鐨犵拠瀛樻 `PB3` 閺?`LIN1`閿涘奔绗夐弰顖氱秼閸?PCB2 Hall B閵?| `PB3` 娑撳秷鍏樻担婊€璐熻ぐ鎾冲 PCB2 Hall閿涙稐缍旀稉?`LIN1` 娴犲秹娓剁憰?Packet A timer/pin-function proof閵嗗倷鎹㈡担?alternate Hall use 娴犲秹娓?SWO 闁插﹥鏂?闂呮梻顬囩拠浣瑰祦閵?|
| C | CN8 / EDA / netlist 鐠ф壆鍤庣拠浣瑰祦閿涘矁鐦夐弰?`NFAULT`閵嗕赋WM 鏉堟挸鍙嗛妴浣烘暩濞翠線鍣伴弽鏋偓涓燼ll閵嗕梗3V3`閵嗕梗GND_SIGNAL` 鐎圭偤妾潻鐐插煂閸濐亪鍣烽妴?| 缂傚搫銇戦妴鍌滃箛閸︺劌褰ч張澶婂斧閻炲棗娴橀幋顏勬禈閿涘本鐥呴張?EDA閵嗕赋DF閵嗕赋CB閵嗕笩erber 閹?netlist閵?| 娑撳秷鍏樻穱鈥叉崲 STM32 瀵洝鍓奸惇鐔烘畱鏉╃偛鍩屾禍鍡欐窗閺?STDRIVE101 缂冩垹绮堕妴?|
| D | 閺冪姴濮涢悳鍥箾缂侇厽鈧?/ 閻叀鐭惧Λ鈧弻銉唶瑜版洏鈧?| 缂傚搫銇戦妴?| P2 娑旓箓娼扮€光剝鐓￠梼鑸殿唽娑撳秴浠涙潻娆庣濮濄儻绱遍崥搴ｇ敾绾兛娆㈤梼鑸殿唽閸撳秴绻€妞ゆ槒藟閵?|
| E | 闂勬劖绁︽稉濠勬暩閺冦儱绻旈妴浣瑰皾瑜般垹鎷板ù瀣櫤鐠佹澘缍嶉妴?| 缂傚搫銇戦敍宀冣偓灞肩瑬 P2 缁備焦顒涢崑姘モ偓?| 娑撳秷鍏橀張澶婂閻滃洢鈧胶鏁搁張鎭掆偓涓砏M Gate閵嗕赋rofiler閵嗕笭all閵嗕讣MO 缂佹捁顔戦妴?|

## 閸忔娊鏁悙褰掆偓鎰般€嶇紒鎾诡啈

| 妞ゅ湱娲?| 瑜版挸澧犻懡澶嬵攳閹簼绠為柅?| 閻滄澘婀張澶夌矆娑斿牐鐦夐幑?| 娣団€叉崲閸撳秷绻曠紓杞扮矆娑?|
| --- | --- | --- | --- |
| `PB12/TIM1_BKIN` 娴ｆ粈璐?`nFAULT` | 瑜版挸澧犳＃鏍偓澶娾偓娆撯偓澶堚偓?| pin/config review 閸?config draft 瀹歌尪顔囪ぐ鏇＄箹娑擃亪鈧瀚ㄩ敍娌梞csdk_no_power_nucleo_g474re_draft.ioc` 瀹歌弓绻氱€?`PB12.Signal=TIM1_BKIN`閵?| CN8/EDA/netlist 韫囧懘銆忕拠浣规 STDRIVE101 `nFAULT` 閻喓娈戦崚鎷岀箹娑?STM32 鏉堟挸鍙嗛敍娑滅箷鐟曚胶鈥樼拋銈勭瑐閹峰鏁搁崢瀣嫲娴ｅ孩婀侀弫鍫濇儓娑斿鈧?|
| `PC5` 娴ｆ粈璐?`nFAULT` | 瑜版挸澧犻懡澶嬵攳閹锋帞绮烽妴?| `config_draft.md` 閸?`pin_config_review_2026-05-14.md` 瀹歌尪顔囪ぐ鏇熷珕缂佹繄鎮婇悽渚库偓?| 閸欘亝婀侀崘娆愮濡?OPAMP/VCP/鐎规碍妞傞崳?break/鐠ф壆鍤庨崘鑼崐閹簼绠炵憴锝呭枀閿涘本澧犻崗浣筋啅闁插秵鏌婇幍鎾崇磻閵?|
| Workbench generated FOC route | `PA8/PB13`, `PA9/PB14`, `PA10/PB15` TIM1 complementary PWM; Hall `PA15/PB3/PB10`; USART2 `PA2/PA3`; break `PB12/TIM1_BKIN`. | `source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md` accepts these as no-power selected-field configuration evidence. | This is not the current PCB2 route proof. Current PCB2 Hall `PA0/PA1/PB4` and `PB3=LIN1` still require reconciliation before any hardware claim. |
| Current PCB2 PWM / driver-input route | `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10` is now the route under review. | `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md`, `current_pcb2_hall_pwm_strategy_2026-05-19.md`, and `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md` record it as a source clue and feasibility topic. | Accepted Packet A / Workbench selected fields must still prove how this route can be represented; no Gate PWM output in P2. |
| Historical standard TIM1 complementary PWM draft | `PA8/PB13`, `PA9/PB14`, `PA10/PB15`. | `config_draft.md` now marks this as historical candidate only. | It cannot be treated as current PCB2 route unless a future hardware-rework packet changes the board. |
| `PA2/PA3` 娴ｆ粈璐?FOC 闁矮淇婇崣?| 姒涙顓婚幒鎺楁珟閵?| `.ioc` 瀹歌弓绻氱€?`PA2.Signal=LPUART1_TX`閵嗕梗PA3.Signal=LPUART1_RX`閿涘矁鐦夐弰搴ょ箹閺?NUCLEO VCP 鐠侯垰绶為妴?| 婵″倹鐏夋禒銉ユ倵鐟曚礁顦查悽顭掔礉韫囧懘銆忛悽?CubeMX/Workbench 鐠囦焦妲戞稉宥勭窗閸?OPAMP/PGA 閸愯尙鐛婇妴?|
| Current PCB2 Hall route | `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`. | 2026-05-19 mapping packet, strategy review, Packet A / firmware feasibility review, and software Hall adapter design review record this as current board source clue. | It is not accepted as a same-timer hardware Hall set; software Hall remains no-power design review only and cannot upgrade Hall readiness. |
| Alternate `PB3` Hall B route | Only a future alternate route after SWO release/isolation. | Original `.ioc` and 2026-05-18 screenshot still show `PB3` as SWO; probe copy can show `PB3` as `TIM2_CH2` / `HALL_B_PROBE`; 2026-05-19 clarification says current PCB2 uses `PB3` as `LIN1`. | Any alternate Hall use still needs NUCLEO SWO release/isolation evidence, Packet A assignment, and accepted board-route endpoint. |
| `DT/MODE` 娑?PWM 濡€崇础 | 娴犲秵妲哥涵顑挎鐎光剝鐓℃笟婵婄妞ゅ箍鈧?| STDRIVE101 digest 瀹歌尪袙闁插﹣璐熸禒鈧稊鍫濈暊闁插秷顩﹂妴?| 闂団偓鐟?EDA/netlist 鐠囦焦妲?`DT/MODE` 閺勵垳鏁搁梼鏄忣啎缂冾喛绻曢弰顖涘复閸﹀府绱濋獮鎯邦唨 MCSDK/TIM1 鏉堟挸鍤Ο鈥崇础閸栧綊鍘ょ€瑰啨鈧?|
| STDRIVE101 娣囨繃濮㈢捄顖氱窞 | 娴犲秵妲哥涵顑挎鐎光剝鐓℃笟婵婄妞ゅ箍鈧?| 閺堫剙婀?STDRIVE101 PDF閵嗕焦鏋冮張顒€鎷?digest 闁棄婀妴?| 鏉╂顩︾拠浣规閺夊灝鐡欐稉濠勬畱 `nFAULT`閵嗕梗REG12`閵嗕梗CP`閵嗕梗SCREF`閵嗕梗VS/VM`閵嗕攻ootstrap閵嗕胶鏁稿┃鎰暅闁辨帇鈧箓DS 閻╂垶绁寸純鎴犵捕閵?|
| STDRIVE101 娣囨繃濮㈢捄顖氱窞鐎光剝鐓￠弬鍥︽ | 瀹告彃缂撶粩瀣繁鐠囦胶鐓╅梼鐐光偓?| `stdrive101_protection_path_review_2026-05-14.md` 閹稿鎮撴稉鈧弽鐓庣础鐠佹澘缍嶇€规ɑ鏌熺憰浣圭湴閵嗕焦鍩呴崶鍓у殠缁鳖潿鈧礁褰叉穱锛勭搼缁狙佲偓浣哄繁婢惰精鐦夐幑顔兼嫲 P2 閸愬磭鐡ラ妴?| 鏉╂顩﹂悽銊ョ秼閸撳秶澧?EDA/PDF/netlist/妤傛ɑ绔婚崶鐐Ω濮ｅ繋绔存い閫涚矤 blocked 閸楀洨楠囨稉?proven閵?|

## 閻㈢喐鍨?MCSDK 閸撳秶娈戠涵顒勬▎婵?

2026-05-21 update superseding older blocker wording in this section:

1. Packet A selected fields are now accepted for no-power configuration evidence, and a no-power Debug build-only pass is recorded, but there is still no current PCB2 physical proof.
2. The generated Workbench route still conflicts with current PCB2 evidence: generated Hall uses `PA15/PB3/PB10`, current PCB2 Hall clues use `PA0/PA1/PB4`, and current PCB2 also records `PB3=LIN1`.
3. Packet B/C source proof, `PB3` ownership reconciliation, no-power continuity, and all powered evidence remain blocked.
4. CLI build execution is blocked by missing `ninja` and `arm-none-eabi-gcc` paths, not by an observed MCSDK project compile failure.


1. 濞屸剝婀?`.stmcx`閿涘奔绡冨▽鈩冩箒 Workbench/CubeMX MotorControl 闁板秶鐤嗘い鍨焻閸ユ拝绱辫ぐ鎾冲閸欘亝婀?NUCLEO-G474RE CubeMX `.ioc` 閼藉顢嶉妴涓唘beMX `Pinout & Configuration` GUI fallback 閹搭亜娴橀敍灞间簰閸?MotorControl package 閺佺増宓佺€涙ê婀惃鍕赴濞村顔囪ぐ鏇樷偓?
2. 瑜版挸澧?PCB2 `HIN/LIN` route 閸?`PA0/PA1/PB4` software Hall strategy 鏉╂ɑ鐥呴張?Packet A / firmware feasibility review閿涙稐绗夐懗鑺ュΩ source clue 瑜版挷缍?accepted Workbench selected fields閵?
3. 濞屸剝婀?CN8 / EDA / netlist 鐠ф壆鍤庣拠浣规閵?
4. 濞屸剝婀侀弶璺ㄩ獓 `DT/MODE`閵嗕梗nFAULT`閵嗕梗REG12`閵嗕梗CP`閵嗕梗SCREF`閵嗕梗VS/VM`閵嗕攻ootstrap閵嗕够tandby 閸?VDS monitoring 濠ф劘鐦夐幑顕嗙幢瑜版挸澧犻崣顏呮箒娣囨繃濮㈢捄顖氱窞鐎光剝鐓＄紓楦跨槈閻晠妯€閵?
5. 濞屸剝婀佺拠浣瑰祦鐠囦焦妲?alternate `PB3` Hall B use 娑斿澧犻敍瀛瞁O 瀹歌尙绮￠柌濠冩杹閹存牠娈х粋浼欑幢2026-05-18 probe 閸欘亣鐦夐弰搴ㄥ帳缂冾喖鐪伴崣顖涙▔缁€?`TIM2_CH2` / `HALL_B_PROBE`閿涘奔绗夊〒鍛存珟鐠囥儵妯嗘繅鐐偓?
6. 濞屸剝婀佹潻鐐电敾閹?/ 閻叀鐭惧Λ鈧弻銉唶瑜版洩绱遍懓灞肩瑐閻絻鐦夐幑顔兼躬 P2 闂冭埖顔屾禒宥囧姧缁備焦顒涢妴?

## 娑撳绔村銉ㄧ槈閹诡喖鍙嗛崣?

閺傛澘顤冮崗銉ュ經鐟欏嫬鍨敍?
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_intake_checklist_2026-05-14.md`閵?

鏉╂瑤閲滃〒鍛礋閸欘亣顫夌€规矮绮堟稊鍫熸降濠ф劕褰叉禒銉ㄧ箻閸忋儴鐦夐幑顔碱吀閺屻儻绱濇稉宥呭磳缁狙傛崲娴ｆ洖缍嬮崜宥囧繁鐠囦線銆嶉妴?

閻劍鍩涢崝銊ょ稊闂冪喎鍨敍?
`apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md`閵?

鏉╂瑤閲滈梼鐔峰灙閻滄澘婀幎濠佺瑓娑撯偓濮濄儰姘︽禒姗€銆庢惔蹇撴祼鐎规矮璐熼敍姘帥閸?Packet A / firmware strategy
review閿涘矁鐦庢导?current PCB2 `HIN/LIN` route 閸?`PA0/PA1/PB4` software Hall
feasibility閿涙稑鍟€缂佈呯敾鐞?Packet B/C source proof閿涙稑顩ч弸婊勬弓閺夈儴铔?alternate
`PB3` Hall B閿涘苯鍟€鐞?SWO 闁插﹥鏂侀幋鏍缁傛槒鐦夐幑顔衡偓鍌氱暊娴犲秳绗夐崡鍥╅獓娴犺缍嶈ぐ鎾冲缂傞缚鐦夋い骞库偓?

鐎光剝鐓″Ο鈩冩緲閿?
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_template_2026-05-14.md`閵?

鏉╂瑤閲滃Ο鈩冩緲鐟欏嫬鐣鹃弨璺哄煂濠ф劕瀵橀崥搴″帥閸?Accept / Partial clue / Reject 閸掋倖鏌囬敍灞藉晙閸愬啿鐣?
閺勵垰鎯侀弴瀛樻煀閺堫剝鐦夐幑顔煎瘶閵嗗倹婀悮顐Ｄ侀弶鎸庡复閸欐娈戠€涙顔岀紒褏鐢绘穱婵囧瘮 `Blocked`閵?

| 缂傞缚鐦夋い?| 闂団偓鐟曚浇铔嬮惃鍕弳閸?| 瑜版挸澧犻悩鑸碘偓?|
| --- | --- | --- |
| `.stwb6` / `.stmcx` / MotorControl configuration screenshots | MCSDK / MotorControl Configuration Packet | 2026-05-21 selected fields accepted for no-power configuration evidence via generated-source review; still no current PCB2 physical proof or successful build record. |
| Current PCB2 `HIN/LIN` route plus `PA0/PA1/PB4` software Hall feasibility | Packet A / firmware strategy review and software Hall adapter design review | No-power design review only. `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md` and `software_hall_adapter_design_review_2026-05-19.md` define the boundary, but do not accept selected fields, generated-project trust, build-only clearance, or Hall readiness. |
| CN8 / EDA / netlist 鐠ф壆鍤庣拠浣规 | CN8 / Board Route Packet | Blocked. 娴犲秵鐥呴張?current-version EDA閵嗕够chematic PDF閵嗕苟etlist 閹存牠鐝〒鍛拌泲缁惧灝娴橀妴?|
| STDRIVE101 `DT/MODE`閵嗕梗nFAULT`閵嗕梗REG12`閵嗕梗CP`閵嗕梗SCREF`閵嗕梗VS/VM`閵嗕攻ootstrap閵嗕够tandby 閸?VDS monitoring | STDRIVE101 Protection Path Packet | Blocked. 娴犲秴褰ч張澶婄暭閺傜懓娅掓禒鎯邦洣濮瑰倸鎷扮紓楦跨槈閻晠妯€閿涘本鐥呴張澶嬫緲缁狙団偓姘崇箖鐠囦焦宓侀妴?|
| `PB3` Hall B 閸撳秶娈?SWO 闁插﹥鏂侀幋鏍缁?| CN8 / Board Route Packet plus NUCLEO bridge/source evidence | `Partial clue / still Blocked`. 閸?`.ioc` 娴犲秵妯夌粈?`PB3.Signal=SYS_JTDO-SWO`閿?026-05-18 probe 閸擃垱婀伴崣顖涙▔缁€?`PB3.Signal=TIM2_CH2`閿涘奔绲剧紓?SWO release/isolation 閸?Hall endpoint 鐠囦焦妲戦妴?|

2026-05-15 閺傛澘顤冨┃鎰瘶鐎光剝鐓￠敍?
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_001_cn8_stdrive101_schematic_candidate.md`閵?

瑜版挸澧犻崚銈呯暰娑?`Partial clue`閵嗗倻鏁ら幋宄板嚒绾喛顓荤拠銉﹀焻閸ユ儳顕惔鏂跨秼閸撳秶澧块悶鍡楀閻滃洦婢橀敍灞炬降濠?閻楀牊婀?
閸欙絽绶炴稉铏光€栨禒璺烘倱鐎涳箒鍤滅紒妯糕偓鍌濐嚉閹搭亜娴橀崣顖濐潌 CN8閵嗕讣TDRIVE101閵嗕浇绶崗銉ф暩闂冩眹鈧?
`nFAULT` 娑撳﹥濯?LED閵嗕梗REG12`閵嗕梗CP`閵嗕梗SCREF`閵嗕攻ootstrap閵嗕府OSFET閵嗕線鍣伴弽椋庢暩闂冭鎷?
Hall 閹恒儱褰涚痪璺ㄥ偍閿涙稐绲炬禒宥嗙梾閺堝顒滃?source revision/date閵嗕讣TM32 缁旑垳鍋ｉ弰鐘茬殸閵?
accepted `DT/MODE` 缁旑垳鍋ｇ拠浣规閹?`STBY` 鐠囦焦妲戦妴鍌氭礈濮濄倖婀扮拠浣瑰祦閸栧懍绗夐崡鍥╅獓 CN8
routing proof 閹?STDRIVE101 protection-path proof閵?

Rejected source types stay rejected: low-resolution screenshots, oral
descriptions, old or unknown-version files, incomplete crops, generated source
without matching configuration evidence, and the excluded WeChat-side
`netlist_PADS.net` candidate.

## 2026-05-14 Parallel Evidence Push

| Evidence chain | Follow-up result | Current trust level |
| --- | --- | --- |
| `.stmcx` / MotorControl | Repo search still found no `.stmcx`. Narrow checks of `F:\STMCubeMX`, `MCSDK_v6.4.2-Full`, and VS Code extension folders did not identify a saved Workbench project, standalone Workbench launcher, or MotorControl configuration page. | Blocked. MotorControl package presence is not project configuration evidence. |
| CN8 / STDRIVE101 route | `cn8_stdrive101_route_review_2026-05-14.md` now defines the accepted source packet. Current repo evidence is still only screenshot-level clue plus STDRIVE101 datasheet review requirements. | Blocked. No accepted current EDA, schematic PDF, netlist, or high-resolution route crop is in the repo. |
| Excluded source | The WeChat-side `netlist_PADS.net` candidate is intentionally not imported and not used as current board evidence. | Not evidence. |

## 2026-05-14 STDRIVE101 Protection Path Review

| Evidence chain | Follow-up result | Current trust level |
| --- | --- | --- |
| ST official source | ST official product page and datasheet were rechecked. They confirm two input strategies selected by `DT/MODE`, `REG12` gate-driver supply, overcurrent comparator, VDS monitoring, UVLO, thermal shutdown, and standby behavior. | High for official device requirements. |
| Board screenshot clue | Existing screenshot notes mention possible `R3`/`nFAULT`, `C4`/`C5` for `REG12`, `C1` for `CP`, `R1`/`R2` for `SCREF`, and bootstrap components, but resolution/source type is not accepted board proof. | Low-grade clue only. |
| Protection-path review | `stdrive101_protection_path_review_2026-05-14.md` now records a missing-evidence matrix for `DT/MODE`, `nFAULT`, `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, `STBY`, and VDS monitoring. | High for review structure and blockers; blocked for board-level proof. |

Current decision: P2 can continue written review and GUI/config capture work,
but it still cannot claim saved MCSDK MotorControl configuration, CN8 routing
proof, STDRIVE101 protection-path proof, power-stage readiness, Hall readiness,
or sensorless readiness.

## 2026-05-15 Packet A Local Probe

New Packet A records:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_local_probe_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_checklist_2026-05-15.md`

The local probe checked the repo, existing screenshots, the
`apps/stm32_g474_foc/MotorControl` placeholder, `F:\STMCubeMX`,
`C:\Users\gregrg\STM32Cube\Repository`, `C:\Users\gregrg\.stm32cubemx`, and
common user locations (`Documents`, `Downloads`, `Desktop`). It still found no
real `.stmcx` and no MotorControl / Workbench configuration screenshot. Direct
search of `C:\Users\gregrg` returned access denied, so this is a bounded local
probe, not proof that every private user directory was searched.

Packet A was later upgraded to `Partial clue` by
`source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`. The new checklist
defines the next accepted capture: Workbench screenshots or an accepted final
`.stwb6` / legacy `.stmcx` proving the selected fields.
It does not upgrade MCSDK MotorControl configuration, generated-project trust,
Gate PWM, Motor Profiler, Hall, motor, power-stage, CN8 routing, STDRIVE101
protection-path, or sensorless evidence.

## 2026-05-15 STM32 Signal Contract And Build-Only Gate

New non-hardware track artifacts:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/stm32_side_signal_contract_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/future_build_only_gate_2026-05-15.md`

The STM32-side signal contract records future responsibilities for TIM1 PWM
commands, `NFAULT`, `STBY`, `DT/MODE`, current sensing, Hall fallback,
`PA2/PA3`, `PB3`, `3V3`, `GND_SIGNAL`, and the ESP32 gateway boundary. Every
hardware-dependent field remains `Blocked`, `Candidate`, or `Partial clue`
unless Packet A/B/C or PB3/SWO evidence proves it.

The future build-only gate records that generated-project trust is currently
`Not allowed` because Packet A is only `Partial clue`. If Packet A selected
fields are later accepted, a generated MCSDK project can be treated only as no-power build evidence. Build
success will not upgrade CN8 routing, STDRIVE101 protection-path proof, Gate
PWM behavior, Motor Profiler readiness, Hall readiness, motor readiness, or
sensorless readiness.

## 2026-05-21 Packet A Source Review And Build-Only Gate

New current review artifact:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md`

Current decision: Packet A selected fields are accepted for no-power configuration evidence, the build-only source prerequisite is satisfied, and a local no-power Debug build-only pass is now recorded.

Toolchain status in this turn:

- `cmake --version` is available and reports 4.3.2.
- `ninja --version` is not available in PATH.
- `arm-none-eabi-gcc --version` is not available in PATH.
- The no-power Debug build-only command returned exit code `0`; Ninja reported `ninja: no work to do`, and `.elf` / `.map` artifacts were confirmed. This is compile evidence only, not firmware runtime or hardware validation.

This update does not upgrade CN8 routing proof, STDRIVE101 protection-path proof, continuity, Gate PWM, Motor Profiler, Hall, motor, power-stage, or sensorless evidence.

## 2026-05-15 P2 Readiness Snapshot

New readiness control artifact:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`

The snapshot consolidates Packet A/B/C, PB3/SWO, STM32-side signal-contract,
and future build-only gate status into one current gate decision. Current
decision remains: P2 is in progress, Packet A is `Partial clue`, generated-project
trust is `Not allowed`, Packet B/C and PB3/SWO remain blocked or partial clue
only, and P3 powered or motor work is not allowed.

This snapshot does not upgrade MCSDK MotorControl configuration, generated
project trust, CN8 routing proof, STDRIVE101 protection-path proof, Gate PWM,
Motor Profiler, Hall, motor, power-stage, or sensorless evidence.

## 瑜版挸澧?P2 閸掋倖鏌?

2026-05-27 current correction: Packet A selected fields are accepted as no-power Workbench/generated-source configuration evidence, the build-only source prerequisite is satisfied, and a no-power Debug build-only pass is recorded. Current PCB2 route trust, Packet B/C, continuity, Gate PWM, Motor Profiler, Hall, motor, power-stage, and sensorless evidence remain blocked.


P2 閸欘垯浜掔紒褏鐢婚崑姘姛闂堛垹顓搁弻銉ｂ偓涓烾I / 闁板秶鐤嗙拠浣瑰祦閺€鍫曟肠閸滃矂娼涵顑挎楠炴儼顢戦崙鍡楊槵閵?026-05-15
閺傛澘顤?`non_hardware_parallel_track_2026-05-15.md`閿涘本濡搁垾婊勬畯閺冩儼鐑︽潻鍥┾€栨禒鑸电爱閸栧懏鏁痪搴撯偓?
鐠佹澘缍嶆稉?scheduling decision, not clearance閵嗗倸缍嬮崜宥勭波鎼存捁绻曟稉宥堝厴娣団€叉崲閻㈢喐鍨氶惃?MCSDK
閻㈠灚婧€閹貉冨煑闁板秶鐤嗛敍灞肩瘍娑撳秷鍏樻潻娑樺弳閸旂喓宸奸弶瑁も偓浣烘暩閺堟亽鈧赋WM Gate閵嗕府otor Profiler閵嗕笭all 闂傤厾骞?
閹存牗妫ら幇鐔稿付閸掑爼妯佸▓鐐光偓?
