## 2026-05-28 Dual-Teacher Concept-Only Guard Added

- Added an explicit dual-teacher concept-only role guard after the user reported
  repeated drift in the teaching boundary.
- Decision:
  `Dual-teacher concept-only role guard / ChatGPT teaches theory / Codex reviews records and executes repo work`.
- Rule now recorded in `workflow/codex_dual_teacher_execution_gate.md`,
  `workflow/teaching_contract.md`, `AI_CONTEXT.md`,
  `docs/00_project_truth/ai_architecture.md`, and the project Skill source
  `codex_skills/stm32g474-foc-assistant/SKILL.md`.
- New behavior: for theory, concept, "I do not understand", "teach me", or
  "what should I learn" turns that do not require repo files, commands, build
  output, tests, logs, screenshots, learning-record writes, GitHub, or
  hardware-safety state, Codex must hand the user a concrete ChatGPT prompt/task
  packet instead of teaching the full lesson.
- Added GitHub learning-evidence handoff: if ChatGPT has GitHub write access,
  it may open a branch / PR for its own concept-lesson evidence. Codex then
  syncs, reviews, verifies, records, and either accepts or asks for changes.
  The PR is not accepted project truth until Codex review.
- Codex remains responsible for reviewing returned answers, updating learning
  evidence, running checks, recording project status, and executing any
  repo-side engineering work.
- Safety boundary unchanged: this is workflow-control only. It does not
  authorize firmware edits, Workbench regeneration, flash, 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  powered readiness.

## 2026-05-28 Software Hall Firmware-Entry Plan Added

- Added the Chinese-first no-power firmware-entry plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_plan_2026-05-28.md`.
- Decision:
  `Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.
- The plan locks the current route as `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`
  and keeps `PB3=LIN1` out of Hall. MCSDK standard TIM2 Hall
  `PA15/PB3/PB10` remains generated-source evidence only, not current PCB2
  Hall.
- The first future adapter shape is debug-only: GPIO/EXTI capture on
  `PA0/PA1/PB4`, ISR stores only `raw_state + timestamp + event counter`,
  low-priority state machine rejects `000/111`, repeat, bounce candidates, and
  abnormal jumps, and low-frequency debug snapshot exposes counters plus
  `direction_candidate` / `speed_candidate`.
- Hard stops remain: no writes to `HALL_M1`, no `hall_speed_pos_fdbk.c/.h`
  modification, no speed loop / PID injection, no `mc_tasks_foc.c` / JEOC /
  FOC ISR edits, no TIM1 PWM edits, no generated-code edits, no Motor
  Profiler / Motor Pilot, and no Hall closed-loop claim.
- PCB2 is still unpopulated. DMM continuity / short-check evidence is hardware-side deferred, not passed. The 2026-05-27 build-only pass remains
  local compile evidence only and does not replace hardware or runtime proof.
- User checkpoint: no measurement, no power, and no toolchain work is needed
  now. Keep
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`
  stable and report any hardware route change or PCB2 solder-complete signal.

## 2026-05-27 No-Power Build-Only Debug Pass Recorded

- Ran no-power build-only command for the external Workbench project:
  `cmake --build "C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2\build\Debug" --config Debug`.
- Result: exit code `0`; Ninja reported `ninja: no work to do`, meaning the
  Debug target was already up to date.
- Confirmed build artifacts:
  `QIANSAI_G474_STDRIVE101_FOC_P2.elf` (`2161388` bytes,
  SHA256 `8EF20B93DC069F085AEBD670A77C5C4C4266FE59532A91DF784241CCB062BB23`)
  and `QIANSAI_G474_STDRIVE101_FOC_P2.map` (`1484465` bytes,
  SHA256 `B571B7C9CF5F262BF49E35BE63B05C128CC59480E546FA36929BD8704CBD132D`).
- Added build-only result record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/build_only_result_2026-05-27_qiansai_g474_stdrive101_foc_p2_debug.md`.
- Decision:
  `No-power build-only Debug pass / local toolchain compiles generated project / no firmware runtime or hardware readiness`.
- This upgrades only the local no-power compile evidence for the generated
  Workbench project. It does not upgrade firmware runtime behavior, current
  PCB2 routing, DMM continuity, STDRIVE101 protection, current sensing, GPIO /
  EXTI runtime behavior, MCSDK Hall integration, Gate PWM safety, Hall
  closed-loop, Motor Profiler readiness, motor readiness, power-stage
  readiness, or sensorless readiness.
- Safety boundary unchanged: no flash, no Run / Debug, no 24V, no power-board
  connection, no motor connection, no Gate PWM output, no Motor Profiler, no
  Motor Pilot.

## 2026-05-27 Software Hall MCSDK Speed/Position Feedback Interface Review Added

- Added the no-power MCSDK speed / position feedback interface review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md`.
- Decision:
  `Software Hall MCSDK speed/position feedback interface review / no firmware implementation / no MCSDK hook / no Hall readiness`.
- The archived generated `Src/Inc` snapshot shows MCSDK standard Hall is a full feedback chain, not only a three-bit Hall state reader: TIM2 Hall IRQ updates `HALL_M1`, medium-frequency tasks calculate speed/reliability, the speed loop reads `SPD_GetAvrgMecSpeedUnit(...)`, and the FOC current loop consumes electrical angle through `SPD_GetElAngle(...)`.
- Current PCB2 remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`, with `PB3=LIN1`; this still does not match Workbench TIM2 Hall `PA15/PB3/PB10`.
- `speed_pos_fdbk.h` is not present in the archived project `Src/Inc` snapshot, so the base MCSDK feedback interface remains only partially visible and no custom `SpeednPosFdbk` component is accepted.
- Current decision: future software Hall remains debug-only unless a separate reviewed `SpeednPosFdbk`-compatible component proposal is created with full interface evidence, DMM evidence, no-power build record, exact hook list, and rollback plan.
- Verification passed: `python -m unittest discover -s tests` (`126` tests OK), `python -m compileall src tests`, `git diff --check` with CRLF warnings only, `python tools\build_vector_store.py` (`8678` chunks), `python tools\search_local_v2.py --eval`, and `python tools\check_ai_contracts.py` with warning only that `ACTIVE_TASK.md` is done and still requires review.
- No STM32 firmware, generated-code edit, MCSDK hook, no-power build record, DMM proof, flash, 24V, power-board connection, motor connection, Gate PWM output, Hall closed-loop, motor readiness, power-stage readiness, or sensorless readiness is upgraded.
## 2026-05-27 Full Workbench Src/Inc Snapshot Archived

- Confirmed the external generated Workbench project exists at
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`.
- Archived a no-power read-only snapshot at
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`.
- Added source review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-27_001_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot.md`.
- Decision:
  `Full generated Src/Inc snapshot archived / source interface evidence available for read-only review / no firmware implementation / no MCSDK hook / no Hall readiness`.
- The snapshot includes generated `Src/`, `Inc/`, `cmake/`, top-level project/build metadata, `SOURCE_MANIFEST_2026-05-27.md`, and `SHA256SUMS.txt`.
- Key requested files are now present for read-only review: `hall_speed_pos_fdbk.c/.h`, `speed_torq_ctrl.c/.h`, `mc_tasks.c/.h`, `mc_tasks_foc.c`, `mc_interface.c/.h`, `mc_api.c/.h`, `mc_app_hooks.c/.h`, `mc_parameters.c/.h`, `motorcontrol.c/.h`, `mc_type.h`, interrupt sources, current-feedback backend files, register-interface files, `usart_aspep_driver.c`, and `aspep.c/.h`.
- `Inc/usart_aspep_driver.h` is not present in the generated `Inc/` folder and must not be silently treated as an accepted interface header.
- Static review confirms generated MCSDK Hall still uses standard TIM2 Hall `PA15/PB3/PB10`, while current PCB2 remains `PA0/PA1/PB4` software Hall with `PB3=LIN1`; therefore this snapshot does not prove current PCB2 Hall integration.
- No STM32 firmware, generated-code edit, MCSDK hook, no-power build record, DMM proof, flash, 24V, power-board connection, motor connection, Gate PWM output, Hall closed-loop, motor readiness, power-stage readiness, or sensorless readiness is upgraded.

## 2026-05-27 Software Hall MCSDK Hook Evidence Request Checklist Added

- Added the no-power MCSDK hook evidence request checklist:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md`.
- Decision:
  `Software Hall MCSDK hook evidence request checklist / no firmware implementation / no MCSDK hook / no Hall readiness`.
- The checklist turns log-only MCSDK generated file names into a concrete source-evidence request before any future software Hall hook.
- Required evidence now includes exact generated or MCSDK interface sources such as `hall_speed_pos_fdbk.c/.h`, speed / position feedback interface evidence, `speed_torq_ctrl.c/.h`, `mc_tasks.c/.h`, `mc_tasks_foc.c`, `mc_interface.c/.h`, `mc_api.c/.h`, `mc_app_hooks.c/.h`, `mc_parameters.c/.h`, `motorcontrol.c/.h`, `mc_type.h`, interrupt sources, current-feedback backend files, and ASPEP / register-interface files.
- Rejected evidence types include log-only file names, screenshots, files from a different project/version, AI summaries, host tests, build-only success by itself, and memory-based claims.
- No STM32 firmware, MCSDK hook, generated-code edit, build record, DMM proof, flash, 24V, power-board connection, motor connection, Gate PWM output, Hall closed-loop, motor readiness, power-stage readiness, or sensorless readiness is upgraded.
## 2026-05-27 Software Hall MCSDK Firmware-Integration Boundary Review Draft Added

- Added the no-power MCSDK firmware-integration boundary review draft:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md`.
- Decision:
  `Software Hall MCSDK firmware-integration boundary review draft / no firmware implementation / no MCSDK hook / no Hall readiness`.
- The draft records that future software Hall output is only
  `direction_candidate` and `speed_candidate` until accepted MCSDK interface
  evidence exists.
- Generated clues such as `HALL_M1`, `SpeednTorqCtrlM1`, `PIDSpeedHandle_M1`,
  `pSTC`, `MCI_Handle_t`, `FOCVars`, `SPD_HALL_TIM_M1_IRQHandler`,
  `M1_SPEED_SENSOR=HALL_SENSOR`, and `M1_HALL_TIMER_SELECTION=HALL_TIM2` are
  treated as read-only clues, not MCSDK hooks.
- Generated log file names `hall_speed_pos_fdbk.c/.h`, `speed_torq_ctrl.c/.h`,
  and `mc_app_hooks.c/.h` remain file-name clues only until archived source and
  interface contracts are reviewed.
- Hard stops remain: no write to `HALL_M1`, no speed-loop / PID injection, no
  JEOC / FOC ISR edits, no TIM1 PWM edits, no generated-code edits, no Motor
  Profiler / Motor Pilot, and no Hall closed-loop claim.
- No STM32 firmware, MCSDK hook, build record, DMM proof, flash, 24V,
  power-board connection, motor connection, Gate PWM output, Hall closed-loop,
  motor readiness, power-stage readiness, or sensorless readiness is upgraded.
## 2026-05-27 Software Hall Debug-Output Route Review Draft Added

- Added the no-power low-frequency debug-output route review draft:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_debug_output_route_review_2026-05-27.md`.
- Decision:
  `Software Hall low-frequency debug-output route review draft / no firmware implementation / no UART implementation / no Hall readiness`.
- The draft defines future debug snapshot fields:
  `current_raw_state`, `last_accepted_state`, `last_decision`, `edge_count`,
  `illegal_state_count`, `repeat_count`, `bounce_candidate_count`,
  `abnormal_jump_count`, `lost_event_count`, `last_edge_dt_ticks`,
  `timestamp_source_id`, `direction_candidate`, and `speed_candidate`.
- Output boundary:
  first firmware shape, if later authorized, must be a low-frequency snapshot
  path. It is not every-edge streaming, not ISR printing, not JEOC / FOC ISR
  work, and not MCSDK speed feedback.
- Route constraints:
  UART text / CSV / JSON, ESP32 / WebSocket display, MCSDK USART2 / ASPEP /
  MCP reuse, `PA2/PA3` reuse, and SWO / ITM are not authorized by this draft.
- No STM32 firmware, UART implementation, JSON protocol, ESP32 gateway,
  MCSDK hook, build record, DMM proof, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Hall closed-loop, motor
  readiness, power-stage readiness, or sensorless readiness is upgraded.

## 2026-05-27 Software Hall Timestamp Source Review Draft Added

- Added the no-power timestamp-source review draft:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_timestamp_source_review_2026-05-27.md`.
- Decision:
  `Software Hall timestamp-source review draft / no firmware implementation / no timer configuration / no Hall readiness`.
- The draft records why `TIM1` is a hard no for software Hall timestamping:
  generated clues tie it to PWM, ADC injected triggering, and FOC timing through
  `MX_TIM1_Init()`, `TIM1_UP_TIM16_IRQn`, and `ADC_EXTERNALTRIGINJEC_T1_TRGO`.
- The draft records why `TIM2` is not current `PA0/PA1/PB4` software Hall
  timestamp clearance: generated clues use `HAL_TIMEx_HallSensor_Init` and
  `M1_HALL_TIMER_SELECTION=HALL_TIM2` for the standard MCSDK Hall route.
- `HAL_GetTick()` / SysTick is limited to coarse logs or timeouts because the
  local HAL clue is `uwTickFreq = HAL_TICK_FREQ_DEFAULT; /* 1KHz */`.
- Future preferred class is an isolated `dedicated free-running timer`, with
  `1 us tick` only as a review target and `unsigned delta` required for
  overflow handling.
- No exact timer instance, prescaler, CubeMX setting, firmware source,
  MCSDK hook, build record, DMM proof, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Hall closed-loop, motor
  readiness, power-stage readiness, or sensorless readiness is upgraded.

## 2026-05-27 Local Retrieval V2 Added

- Added the second AI architecture foundation batch:
  `tools/search_local_v2.py`,
  `retrieval_eval/queries.json`, and `tests/test_search_local_v2.py`.
- Decision:
  `Local retrieval v2 / source-priority search / retrieval regression checks /
  no RAG hardware claims / no powered readiness`.
- Evidence ID:
  `EV-2026-05-27-AI-RETRIEVAL-V2-001`.
- The new search tool reads the existing `vector_store/` index but adds:
  query expansion, source-priority weighting, phrase bonuses, a minimum
  reliable-score threshold, and a built-in retrieval evaluation mode.
- The first retrieval evaluation cases cover:
  `JEOC 娑擃厽鏌囬柌宀冨厴娑撳秷鍏?printf`,
  `ESP32 閼虫垝绗夐懗鍊熺箻閸?FOC 鐎圭偞妞傞幒褍鍩楅悳鐥? and
  `瑜版挸澧?PCB2 Hall 鐠侯垳鍤?PA0 PA1 PB4 PB3 閺勵垯绮堟稊鍧?
- Verification:
  `python tools/search_local_v2.py "JEOC 娑擃厽鏌囬柌宀冨厴娑撳秷鍏?printf"` now ranks
  `docs/protocol.md` first and also returns the JEOC review template and
  STM32 app rules. `python tools/search_local_v2.py --eval` passed.
  `python -m unittest discover -s tests` passed with 115 tests.
  `python tools/build_vector_store.py` rebuilt the local retrieval index with
  8548 chunks.
- This remains local evidence retrieval only. It does not generate hardware
  conclusions, does not replace phase gates or evidence records, and does not
  upgrade firmware implementation, generated-code trust, build trust,
  GPIO/EXTI runtime proof, MCSDK Hall integration, DMM continuity, flash, 24V,
  power-board connection, motor connection, Gate PWM output, Motor Profiler,
  Hall closed-loop, motor readiness, power-stage readiness, or sensorless
  readiness.

## 2026-05-27 AI Architecture Foundation Added

- Added the first AI architecture foundation batch:
  `docs/00_project_truth/ai_architecture.md`,
  `workflow/CURRENT_SNAPSHOT.md`,
  `tools/build_context_pack.py`, and `tools/check_ai_contracts.py`.
- Decision:
  `AI architecture foundation / low-token handoff / read-only workflow checks /
  no firmware, no hardware, no powered readiness`.
- Evidence ID:
  `EV-2026-05-27-AI-ARCHITECTURE-FOUNDATION-001`.
- The architecture contract keeps the current evidence-first model:
  short context -> grounded retrieval -> task packet -> safe execution ->
  evidence record -> learning update -> verification.
- `CURRENT_SNAPSHOT.md` is now the default low-token current-state page. It
  summarizes P2 no-power state, current PCB2 Hall route, software Hall planning
  status, AI architecture work, and the active safety boundary.
- `build_context_pack.py` can generate mode-specific context packs for
  `codex_task`, `teaching`, `hardware_review`, `mcsdk_packet`,
  `experiment_analysis`, and `report_defense`.
- `check_ai_contracts.py` performs a read-only static check of required AI
  architecture files, `ACTIVE_TASK` status and evidence ID, safety phrases,
  indexes, review-queue size, and dangerous positive readiness claims.
- Verification:
  `python tools/check_ai_contracts.py` passed with no errors,
  `python tools/build_context_pack.py --mode codex_task --max-chars 400`
  emitted a context pack, `python tools/build_context_pack.py --list-modes`
  listed the supported modes, and `python -m unittest discover -s tests`
  passed with 111 tests. `python tools/build_vector_store.py` rebuilt the
  local retrieval index with 8529 chunks.
- This is repository workflow infrastructure only. It does not upgrade
  firmware implementation, generated-code trust, build trust, GPIO/EXTI
  runtime proof, MCSDK Hall integration, DMM continuity, flash, 24V,
  power-board connection, motor connection, Gate PWM output, Motor Profiler,
  Hall closed-loop, motor readiness, power-stage readiness, or sensorless
  readiness.

## 2026-05-27 Software Hall GPIO/EXTI Boundary Review Draft Added

- Added the no-power GPIO/EXTI boundary draft:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_gpio_exti_boundary_review_2026-05-27.md`.
- Decision:
  `Software Hall GPIO/EXTI boundary review draft / no firmware implementation / no GPIO runtime proof / no Hall readiness`.
- The draft records the current static boundary for the future software Hall
  route: `PA0=GPIO_EXTI0`, `PA1=GPIO_EXTI1`, `PB4=GPIO_EXTI4`, with
  `PB3=LIN1` kept out of Hall.
- Local CMSIS/HAL clues identify `EXTI0_IRQn`, `EXTI1_IRQn`, `EXTI4_IRQn`,
  `GPIO_MODE_IT_RISING_FALLING`, and pull-mode options, but this is only a
  no-power review draft.
- Open blockers remain: populated PCB2, DMM continuity / short-check table,
  pull-up / pull-down decision, timestamp-source decision, debug-output route,
  and separate MCSDK firmware-integration review. The build-only record now
  exists but does not open firmware implementation or hardware readiness.
- No STM32 firmware, CubeMX/Workbench setting, generated code, build, flash,
  Gate PWM, Motor Profiler, Motor Pilot, motor, power-stage, Hall closed-loop,
  or sensorless readiness is upgraded.

## 2026-05-27 Software Hall Firmware-Entry Checklist Added

- Added the no-power firmware-entry checklist:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_checklist_2026-05-27.md`.
- Decision:
  `Software Hall firmware-entry checklist / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- The checklist converts the existing software Hall prep, pseudocode, host
  model, golden vectors, and MCSDK probe into explicit entry conditions before
  any future STM32 adapter code.
- Current required but missing entry evidence remains: populated PCB2,
  DMM continuity / short-check table, GPIO/EXTI boundary review, timestamp
  source decision, low-frequency debug-output route, no-power build-only
  record, and a separate MCSDK firmware-integration review before any hook.
- First future code, if later authorized, must stay as an independent adapter.
  It must not modify TIM1 PWM, JEOC / FOC ISR, `HALL_M1`, MCSDK speed loop,
  Gate PWM, flash, Motor Profiler, Motor Pilot, or powered hardware.
- No user hardware action is needed while PCB2 is unpopulated. The next
  learner checkpoint remains the one-sentence processing-order teach-back.

## 2026-05-27 Software Hall MCSDK Integration Probe Added

- Added a read-only MCSDK integration clue review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_integration_probe_2026-05-27.md`.
- Decision:
  `MCSDK Hall integration points identified as read-only clues / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- Read-only checks in the 2026-05-21 generated-project clue folder found the
  standard MCSDK Hall path: `MX_TIM2_Init()`, `HAL_TIMEx_HallSensor_Init`,
  `HALL_Handle_t HALL_M1`, `SpeednTorqCtrlM1`, `PIDSpeedHandle_M1`,
  `M1_SPEED_SENSOR=HALL_SENSOR`, `SPEED_SENSOR_SELECTION=HALL_SENSORS`,
  `M1_HALL_TIMER_SELECTION=HALL_TIM2`, and generated log references to
  `hall_speed_pos_fdbk.c/.h` and `speed_torq_ctrl.c/.h`.
- Conclusion: those are only read-only clues for the standard TIM2 hardware
  Hall route. They do not match current PCB2 `PA0/PA1/PB4` software Hall and
  do not create MCSDK Hall integration.
- Any future MCSDK hook requires a separate firmware-integration review. Hard
  stops remain: do not edit JEOC / FOC ISR, TIM1 PWM timing, generated speed
  loop, or `HALL_M1` path without a new review.

## 2026-05-27 Software Hall Golden Vectors Added

- Added host-side no-power golden vectors for the future software Hall adapter:
  `tests/fixtures/software_hall_golden_vectors.json`.
- Added replay test:
  `tests/test_software_hall_vectors.py`.
- Added no-power review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_golden_vectors_review_2026-05-27.md`.
- Decision:
  `Host-side software Hall golden vectors / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- The vectors turn the state-machine rules into replayable input/output
  examples for later firmware-adapter review: forward candidate cycle,
  illegal-state rejection, repeated-state rejection, configurable
  bounce-candidate rejection, abnormal non-adjacent jump, and reverse adjacent
  step.
- This is host-side no-power algorithm-contract evidence only. It does not read
  GPIO, configure EXTI, edit MCSDK generated code, build firmware, flash
  hardware, pass DMM, output Gate PWM, connect a motor, or prove Hall
  readiness.

## 2026-05-27 Software Hall Host Model Added

- Added a host-side executable reference model for the future software Hall
  adapter:
  `src/software_hall_model.py`.
- Added tests:
  `tests/test_software_hall_model.py`.
- Added no-power review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_host_model_review_2026-05-27.md`.
- Decision:
  `Host-side software Hall reference model / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- The model implements the no-power algorithm sequence:
  illegal-state check -> first-valid baseline -> repeated-state rejection ->
  configurable bounce/timing check -> forward/reverse adjacent step ->
  abnormal-jump count.
- Test coverage includes valid states, `000/111`, `100 -> 110`,
  `100 -> 101`, `100 -> 011`, repeated state, configurable bounce candidate,
  and a full candidate forward cycle.
- This is executable host-side algorithm evidence only. It does not read GPIO,
  configure EXTI, edit MCSDK generated code, build firmware, flash hardware,
  pass DMM, output Gate PWM, connect a motor, or prove Hall readiness.

## 2026-05-27 Software Hall Processing-Order Teaching Card Added

- User could correctly classify individual Hall transition rows, but then
  answered `閹存垳绗夐惌銉╀壕閸熷グ when asked to restate the adapter processing order.
- Added a Chinese-first no-power repair artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_processing_order_card_2026-05-27.md`.
- Decision:
  `Software Hall adapter processing-order teaching card / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- Evidence level:
  L1 repair artifact for the processing-order weak point. This is not a new
  mastery upgrade.
- Evidence limit: not a new mastery upgrade.
- The card explains:
  raw read -> illegal-state check -> first-valid check -> repeated-state check
  -> bounce/timing check -> forward/reverse adjacent check -> abnormal-jump
  count.
- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`;
  `PB3=LIN1` and is not Hall.
- This does not upgrade firmware implementation, GPIO/EXTI runtime behavior,
  MCSDK Hall integration, DMM continuity proof, build record, flash, 24V,
  power-board connection, motor connection, Gate PWM output, Motor Profiler,
  Hall closed-loop, motor readiness, power-stage readiness, or sensorless
  readiness.
- Next user checkpoint:
  say the one-sentence Chinese rule from the card, without filling another
  table.

## 2026-05-27 Hall State-Machine Follow-Up Review Passed

- User completed the follow-up Hall transition table:
  `100 -> 110`, `100 -> 101`, `100 -> 011`, `000`, and `111`.
- Codex review result:
  all five rows are correct.
- Evidence level:
  `L4 for table-level no-power Hall state-machine classification`.
- Recorded learning evidence:
  `learning/session_notes/2026-05-27_hall_state_machine_review_followup.md`
  and
  `learning/review_items/2026-05-27_hall_state_machine_review_completed.md`.
- This upgrades only algorithm-table mastery. It does not upgrade firmware
  implementation, GPIO/EXTI runtime behavior, MCSDK Hall integration, DMM
  continuity proof, build record, flash, 24V, power-board connection, motor
  connection, Gate PWM output, Motor Profiler, Hall closed-loop, motor
  readiness, power-stage readiness, or sensorless readiness.
- Next algorithm-side review before code:
  restate the adapter processing order:
  raw read -> illegal-state check -> first-valid check -> repeated-state check
  -> bounce/timing check -> forward/reverse adjacent check -> abnormal-jump
  count.

## 2026-05-27 Software Hall Adapter Pseudocode Draft Added

- Added the next no-power software Hall design artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_pseudocode_draft_2026-05-27.md`.
- Decision:
  `Software Hall adapter pseudocode draft / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- This uses the 2026-05-27 Hall state-machine L2 learning evidence only as
  algorithm understanding, not as hardware or firmware evidence.
- The draft defines future responsibilities for `Hall_ReadRaw3()`,
  `Hall_IsValidState()`, `Hall_IsForwardAdjacent()`,
  `Hall_IsReverseAdjacent()`, `Hall_CaptureEdge_ISR()`,
  `Hall_ProcessEvent()`, and `Hall_GetDebugSnapshot()` as pseudocode only.
- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`;
  `PB3=LIN1` and is not Hall.
- The draft locks the decision order:
  illegal `000/111` -> repeated state -> forward/reverse adjacent transition
  -> abnormal jump.
- ISR boundary remains minimal: timestamp, raw Hall state, pending/event flag
  or small counter only. No `printf`, JSON, `HAL_Delay`, blocking wait,
  dynamic allocation, complex MCSDK call, speed-loop decision, or FOC-loop
  edit is allowed in ISR.
- PCB2 is still unpopulated, so DMM remains hardware-side deferred, not
  passed. No firmware file, runtime API, generated-code hook, MCSDK Hall
  integration, build record, flash, 24V, power-board connection, motor
  connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop,
  motor readiness, power-stage readiness, or sensorless readiness is
  authorized.

## 2026-05-22 Software Hall State-Machine Exercise Card Added

- Added the next algorithm-side no-power exercise card:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_state_machine_exercise_card_2026-05-22.md`.
- Decision:
  `User Hall state-machine exercise requested / no firmware implementation / no Hall readiness`.
- The card is Chinese-first and asks the algorithm role to answer five checks:
  why three Hall lines have six valid states, why `000/111` are illegal, why
  the candidate sequence `001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001`
  can define one direction candidate, why `PA0/PA1/PB4` must be treated as
  software GPIO/EXTI Hall, and why `PB3=LIN1` cannot be Hall.
- The required user response table is:
  `Input sequence | User judgment | Count edge? | Abnormal? | Note` for
  `001 -> 101`, `001 -> 001`, `001 -> 010`, and `000`.
- PCB2 is still unpopulated, so the DMM gate remains hardware-side deferred,
  not passed. This exercise does not need DMM, board power, Workbench, CubeMX,
  Motor Profiler, oscilloscope, or hardware measurement.
- No firmware logic, runtime API, generated-code hook, MCSDK Hall integration,
  build record, flash, 24V, power-board connection, motor connection, Gate PWM
  output, Motor Profiler, Hall closed-loop, motor readiness, power-stage
  readiness, or sensorless readiness is authorized.

## 2026-05-22 Software Hall No-Power Algorithm Prep Added

- Added the algorithm-side no-power preparation artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_no_power_algorithm_prep_2026-05-22.md`.
- Decision:
  `Algorithm-side no-power preparation / no firmware implementation / no Hall readiness`.
- This lets the algorithm role progress while the unpopulated PCB2 DMM gate is
  hardware-side deferred. Deferred does not mean passed.
- The artifact locks the no-power state-machine contract for
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`, while keeping `PB3=LIN1` outside
  the current Hall path.
- Valid Hall candidates are `001`, `010`, `011`, `100`, `101`, and `110`;
  `000` and `111` are illegal. Repeated states do not count as new edges,
  non-adjacent jumps are abnormal, and bounce filtering remains a future
  measured-threshold topic.
- Future debug observables are only low-frequency candidates:
  raw/accepted Hall state, edge count, illegal-state count, abnormal-jump
  count, repeat count, bounce-candidate count, edge delta, direction candidate,
  and speed candidate.
- ISR boundary remains minimal: capture timestamp/state and defer decoding,
  logging, JSON, UART formatting, WebSocket work, dynamic allocation, blocking
  delays, and control decisions to lower-priority context.
- No firmware logic, runtime API, generated-code hook, MCSDK Hall integration,
  build record, flash, 24V, power-board connection, motor connection, Gate PWM
  output, Motor Profiler, Hall closed-loop, motor readiness, power-stage
  readiness, or sensorless readiness is authorized.

## 2026-05-22 No-Power DMM Evidence Request Opened

- Added the next real-world no-power evidence request:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/dmm_continuity_short_check_request_2026-05-22.md`.
- Current route remains locked as `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`,
  `PB3=LIN1`, and `P14/P15=3V3/GND`.
- Next user action is a filled DMM continuity / short-check table for
  `IA->PA0`, `IB->PA1`, `IC->PB4`, `PB3->LIN1`, `P14->3V3`, `P15->GND`,
  `nFAULT->PB12`, `3V3-GND`, STM32 signal pins to `3V3/GND`, and Hall-line
  pair shorts.
- CLI toolchain setup is not the main real-world progress blocker in this
  step. A later 2026-05-27 no-power build-only record now exists, but it does
  not replace the hardware-side DMM gate.
- No software Hall adapter implementation starts until the DMM table is
  returned and reviewed.
- No firmware logic, runtime API, generated-code hook, flash,
  24V, power-board connection, motor connection, Gate PWM output, Motor
  Profiler, Hall closed-loop, motor readiness, power-stage readiness, or
  sensorless readiness is authorized.

## 2026-05-21 Current PCB2 Software Hall Route Confirmed

- User confirmed the current PCB2 `CN3/CN8 -> STM32` mapping has no known
  error for this route decision.
- Existing archived PCB2 mapping already records `P14=3V3` and `P15=GND`;
  they are no longer a missing-evidence blocker for software Hall route
  selection. They still do not replace no-power continuity or short checks.
- Current PCB2 Hall route is locked for no-PCB-change planning as
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- Current PCB2 `PB3` is locked as `LIN1` / low-side PWM driver input. It is no
  longer a current Hall candidate in Packet A or firmware-design discussion.
- The active route is now `software Hall adapter first`; hardware rework is a
  fallback only if later MCSDK integration proves the software route unsafe or
  unrepresentable.
- The future software Hall adapter boundary is GPIO/EXTI input sampling on
  `PA0/PA1/PB4`, three-bit Hall state readout, illegal-state filtering for
  `000/111`, edge timestamp capture, and minimal ISR work only.
- The Workbench generated TIM2 Hall route `PA15/PB3/PB10` remains accepted only
  as no-power generated configuration evidence. It does not match the current
  PCB2 Hall route and cannot be used directly as current-board Hall proof.
- No firmware logic, runtime API, generated-code hook, build record, flash,
  24V, power-board connection, motor connection, Gate PWM output, Motor
  Profiler, Hall closed-loop, motor readiness, power-stage readiness, or
  sensorless readiness is authorized.

## 2026-05-21 Packet A Generated-Source Review And Build-Only Gate

- Added generated-source side-effect review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md`.
- Decision:
  `Packet A selected fields accepted for no-power configuration evidence /
  build-only source prerequisite satisfied / build execution deferred at the
  time / hardware trust still blocked`.
- Accepted Packet A configuration fields from the 2026-05-21 Workbench
  generated-project clues: `FOC`, `NUCLEO-G474RE`, `STM32G474RETx`,
  `MY-STDRIVE101_POWER_BOARD`, `STDRIVE101`, TIM1 complementary PWM
  `PA8/PA9/PA10 + PB13/PB14/PB15`, `PB12/TIM1_BKIN`, three-shunt current
  sensing, TIM2 Hall `PA15/PB3/PB10`, and USART2 `PA2/PA3` ASPEP/MCP.
- Read-only static checks found no `SIX_STEP`, `sixstep`,
  `mc_tasks_sixstep`, `pwmc_sixstep`, or `speed_duty_ctrl` matches in the
  archived generated-project clue folder.
- At the time of this 2026-05-21 review, the build-only gate source
  prerequisite was satisfied but no no-power build record existed yet. This
  older CLI path blocker is superseded by the 2026-05-27 no-power Debug
  build-only pass recorded at
  `build_only_result_2026-05-27_qiansai_g474_stdrive101_foc_p2_debug.md`.
- The generated Workbench Hall route `PA15/PB3/PB10` still does not match the
  current PCB2 Hall clue `PA0/PA1/PB4`; current PCB2 also records `PB3=LIN1`.
  Hall readiness and current-board route trust remain blocked.
- `R57BLB50L2` remains a temporary Workbench motor placeholder, not measured
  motor evidence.
- No trusted build output, flash, 24V, power-board connection, motor
  connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop,
  sensorless / SMO, powered readiness, motor readiness, or power-stage
  readiness is authorized.

## 2026-05-21 Workbench FOC Source Captured For Packet A

- User completed a no-power ST Motor Control Workbench 6.4.2 GUI route for
  `QIANSAI_G474_STDRIVE101_FOC_P2`.
- Archived primary Workbench source:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/QIANSAI_G474_STDRIVE101_FOC_P2_2026-05-21.stwb6`.
- SHA256:
  `05CD6F0DF86276DE10C96CCCFE5AA32E04C9EDE7D8B27E4242D3532D2A126643`.
- Archived user power-board source:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/MY-STDRIVE101_POWER_BOARD.foc_no_power_2026-05-21.json`.
- SHA256:
  `80B655D52D082F89E6CE73804E9A15511D24A9FF3C965494F6A0D98527311B7A`.
- Added source review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/workbench_foc_capture_success_2026-05-21.md`.
- Read-only verification confirms `algorithm: FOC`, `NUCLEO-G474RE`,
  `STM32G474RETx`, `MY-STDRIVE101_POWER_BOARD`, `HallEffectSensor`,
  `speedSensorMode: hall`, `CURRENT_AMPL_U/V/W`, and `DP_TRIGGER` on
  `PB12/TIM1_BKIN`.
- Key GUI unblock: `CURRENT_AMPL_V` had to move from `MR15` to `MR24`; the
  earlier `MR15` route made hardware checks green but kept FOC disabled.
- Driver protection warning was cleared by adding active-low `DP_TRIGGER ->
  MR16`, which Workbench resolves to `PB12/TIM1_BKIN`.
- Workbench also created a local generated-project directory as a GUI side
  effect. Selected source clues were archived under
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/`.
- Decision: `Workbench FOC source captured / no-power Packet A source evidence
  upgraded / hardware and build trust still blocked`.
- No build-only clearance, trusted generated source, powered readiness, Hall
  readiness, Motor Profiler readiness, motor readiness, power-stage readiness,
  or sensorless readiness is upgraded.
- No build, flash, 24V, power-board connection, motor connection, Gate PWM
  output, Motor Profiler, Motor Pilot, Hall closed-loop, or sensorless / SMO
  claim is authorized.

## 2026-05-20 Workbench Short-Name Power Board Alias Added

- User reported that searching `OPAMP` in the Workbench GUI still did not show
  `QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER`.
- Read-only Workbench API check confirmed the long-name candidate was already
  present in `http://localhost:8009/api/hardware/usr/power`; the problem is
  therefore treated as a Workbench GUI search/filter visibility issue, not a
  missing JSON install.
- Added and installed a short-name no-power alias:
  `QS_TIM1_OPAMP_PWR`.
- Repo source:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/QS_TIM1_OPAMP_PWR.no_power_candidate_2026-05-20.json`.
- Workbench user-board install:
  `C:\Users\gregrg\.st_workbench\hardware\board\power\QS_TIM1_OPAMP_PWR.json`.
- SHA256:
  `79BABB221D6F488FB63B79E73B62B9500CEC19BDE96D9FCCB7308A2882B00141`.
- Workbench log confirms:
  `loading Json User Hardware: QS_TIM1_OPAMP_PWR.json` and
  `successfully parsed User Hardware: QS_TIM1_OPAMP_PWR.json`.
- Because the GUI still did not surface the user-library board, the same
  no-power alias was also installed as a local Workbench app asset:
  `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\assets\hardware\board\power\QS_TIM1_OPAMP_PWR.json`.
- Workbench was restarted. Read-only verification now shows
  `QS_TIM1_OPAMP_PWR` in `http://localhost:8009/api/hardware/app/power`, and
  the log confirms `successfully parsed assets Hardware:
  QS_TIM1_OPAMP_PWR.json`.
- Next GUI action: from a fresh Workbench `New Project` path, search `QS` in
  the Power Board selector, select `QS_TIM1_OPAMP_PWR`, and stop at the
  summary before `Create`.
- Packet A remains blocked. No `.stwb6`, generated-project trust, build-only
  clearance, trusted generated source, powered readiness, Hall readiness, Motor
  Profiler readiness, motor readiness, power-stage readiness, or sensorless
  readiness is upgraded.
- No Generate, build, flash, 24V, power-board connection, motor connection,
  Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
  sensorless / SMO claim is authorized.

## 2026-05-20 Workbench TIM1 Adapter Follow-up Still Blocked

- Added no-power TIM1 adapter follow-up:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/workbench_tim1_adapter_followup_2026-05-20.md`.
- Added no-power candidate board sources:
  `QIANSAI_STDRIVE101_TIM1_ADAPTER_POWER.no_power_candidate_2026-05-20.json`
  and
  `QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER.no_power_candidate_2026-05-20.json`.
- Installed local Workbench user-board candidate:
  `C:\Users\gregrg\.st_workbench\hardware\board\power\QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER.json`.
- GUI evidence shows the `TIM1_ADAPTER` candidate resolves the previous
  `PWM Generation` red X: `PWM Generation`, `Driver Protection`, and UART are
  green in Workbench, while `Current Sensing` remains red and `Create` remains
  disabled.
- Archived follow-up log:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/logs/2026-05-20_connectAlgo_tim1_adapter_pwm_pass_current_sensing_blocked.log`.
- Follow-up log SHA256:
  `3A6109B82EAB2FDF21C97C989640EC8A7F2B99B7B00B312EA6E33A287A583D3C`.
- Current-sense blocker narrowed: current PCB2 clue
  `ADC_U/ADC_V/ADC_W -> PA4/PB0/PA5` is still not accepted by Workbench as the
  G4 internal OPAMP/PGA FOC current-sense route.
- The OPAMP adapter candidate maps current sense to `PA1/PA7/PB0` and PWM to
  `PA8/PA9/PA10 + PB13/PB14/PB15`, but it is only an adapter/rework candidate.
  Its power-board-side current-sense type was corrected to
  `ThreeShunt_RawCurrents_SingleEnded`; Workbench should perform the G474
  OPAMP/PGA mapping during connection. It is not current PCB2 proof and it
  conflicts with the current PCB2 `PA0/PA1/PB4` software-Hall clue.
- GUI reselection of `QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER` remains
  pending. Next no-power GUI action: restart Workbench, select the OPAMP
  adapter candidate, and stop at the summary before `Create`.
- Packet A remains blocked. No `.stwb6`, generated-project trust, build-only
  clearance, trusted generated source, powered readiness, Hall readiness, Motor
  Profiler readiness, motor readiness, power-stage readiness, or sensorless
  readiness is upgraded.
- No Generate, build, flash, 24V, power-board connection, motor connection,
  Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
  sensorless / SMO claim is authorized.

## 2026-05-20 Workbench FOC Custom Board Capture Blocked

- Added no-power Workbench FOC capture blocker:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/workbench_foc_capture_blocker_2026-05-20.md`.
- Archived Workbench connection log:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/logs/2026-05-20_connectAlgo_qiansai_pwm_blocker.log`.
- Captured GUI evidence under:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/`.
- Decision: `Partial clue / Workbench FOC GUI path reached / Packet A still
  blocked`. Workbench accepted the custom
  `QIANSAI_STDRIVE101_PCB2_POWER` board into the summary and did not use
  `EVALSTDRIVE101`, but `PWM Generation` remained blocked.
- Primary Workbench log error:
  `DrivingHighAndLowSides No timer matches all signals requirement`.
- The saved custom board maps STDRIVE101 PWM to
  `PA15/PB10/PA9/PB3/PA8/PA10`, which cannot form one consistent `TIM1`
  complementary `CH1/CH2/CH3 + CH1N/CH2N/CH3N` set. `PB3` also remains tied to
  the existing SWO/Hall blocker context.
- `R57BLB50L2` was selected only as a user-approved temporary Workbench motor
  placeholder. It is not accepted as measured project motor data.
- No `.stwb6` was saved from this attempt because Workbench left `Create`
  disabled and no valid pre-generate save path was exposed.
- Packet A remains blocked. No generated-project trust, build-only clearance,
  trusted generated source, powered readiness, Hall readiness, Motor Profiler
  readiness, motor readiness, power-stage readiness, or sensorless readiness is
  upgraded.
- No Generate, build, flash, 24V, power-board connection, motor connection,
  Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
  sensorless / SMO claim is authorized.

## 2026-05-20 Packet C STDRIVE101 Protection Detail Review

- Added no-power Packet C detail review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_c_stdrive101_protection_detail_review_2026-05-20.md`.
- Updated current task to
  `TASK-2026-05-20-p2-packet-c-stdrive101-protection-detail-review`.
- Evidence ID:
  `EV-2026-05-20-P2-PACKET-C-STDRIVE101-PROTECTION-DETAIL-001`.
- Decision: `Packet C detail narrowed / protection proof still partial clue /
  P3 still blocked`.
- The review narrows `DT/MODE`, `nFAULT`, `REG12`, `CP`, `SCREF`, `VS/VM`,
  bootstrap, `STBY`, and VDS monitoring using the current `.epro`, Gerber,
  current PCB2 mapping note, and repo-local STDRIVE101 extracted text.
- The old `V_DSth = 0.249V` / `I_trip ~= 55A` note is now explicitly not
  accepted as a project threshold. The current local official extraction
  supports `VDSth = VSCREF`; the `33k / 20k` divider gives about `1.245V`, so
  this remains a VDS-monitoring source clue, not a safe current-limit value.
- Packet C remains partial clue. No Packet A acceptance, generated-project
  trust, build-only clearance, continuity proof, powered readiness, Hall
  readiness, Motor Profiler readiness, motor readiness, or sensorless readiness
  is upgraded.
- No Generate, build, flash, 24V, power-board connection, motor connection,
  Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
  sensorless / SMO claim is authorized.

## 2026-05-19 Packet A FOC Route Decision After MY_FOC Rollback

- Added no-power Packet A route decision:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_foc_route_decision_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-packet-a-foc-route-decision-after-my-foc-rollback`.
- Evidence ID:
  `EV-2026-05-19-P2-PACKET-A-FOC-ROUTE-DECISION-001`.
- Decision: `Route narrowed / GUI-created FOC source required / Packet A still
  blocked`. The failed `MY_FOC` manual edit now becomes negative evidence:
  do not retry partial `.stwb6` text edits. A valid next Packet A attempt must
  come from Workbench GUI creation/conversion or another complete reviewable
  FOC source.
- Route comparison recorded: legacy `My_First_FOC.stwb6` proves local FOC
  source structure exists but uses built-in `EVALSTDRIVE101`; restored
  `MY_FOC.original_2026-05-19.stwb6` has custom STDRIVE101 board clues but is
  still `"algorithm": "sixStep"`; failed
  `MY_FOC.codex_foc_candidate_2026-05-19.stwb6` must not be reused.
- Next acceptable Packet A capture must show FOC, `NUCLEO-G474RE`, a
  self-developed/custom STDRIVE101 board path, enabled current sensing,
  enabled fault/break handling, and reviewable Hall/PWM choices before any
  generation or build.
- Packet A still blocked. No generated-project trust, no build-only clearance,
  no trusted generated source, no powered readiness, no Hall readiness, no
  Motor Profiler readiness, no motor readiness, no power-stage readiness, and
  no sensorless readiness is upgraded.
- No Generate, build, flash, 24V, power-board connection, motor connection,
  Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
  sensorless / SMO claim is authorized.
- Verification: `python -m unittest discover -s tests` passed with 64 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8291 chunks.

## 2026-05-19 MY_FOC Manual FOC Edit Rollback

- Backed up the Workbench source project:
  `C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6`.
- Backup:
  `C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6.pre_codex_foc_edit_2026-05-19.bak`.
- Attempted one minimal source-file edit: changed top-level
  `"algorithm": "sixStep"` to `"algorithm": "FOC"`.
- User opened Workbench and reported `娑撯偓閼割剟鏁婄拠?/ 閺冪姵纭堕崝鐘烘祰閺傚洣娆?
  C:/Users/gregrg/.st_workbench/projects/MY_FOC.stwb6`.
- Decision:
  `Manual FOC source edit failed Workbench reload / rolled back / Packet A still not accepted`.
- Rollback completed: external `MY_FOC.stwb6` was restored from the backup and
  now again reads `"algorithm": "sixStep"`.
- Current external `.stwb6` SHA256 matches the backup:
  `062B78AD8E07B5A29A68A007797200FCD4833FE9D3371D2821F3A54D5B9429FD`.
- Archived original/restored and failed FOC-candidate `.stwb6` copies under
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-19_my_foc_generated_project/`.
- Engineering result: do not hand-edit only the top-level `.stwb6` `algorithm`
  field to convert six-step to FOC. Use Workbench GUI flow or create a full
  reviewable FOC `.stwb6` instead.
- Packet A still blocked. No generated-project trust, no build-only clearance,
  no trusted generated source, no powered readiness, no Hall readiness, no
  Motor Profiler readiness, no motor readiness, no power-stage readiness, and
  no sensorless readiness is upgraded.
- No Generate, build, flash, 24V, power-board connection, motor connection,
  Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
  sensorless / SMO claim is authorized.
- Verification: `python -m unittest discover -s tests` passed with 61 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8276 chunks. Read-back confirmed
  external `MY_FOC.stwb6` has `"algorithm": "sixStep"` and matches the backup
  SHA256.

## 2026-05-19 MY_FOC Generated Project Source Review

- Archived selected no-power source files from
  `C:\Users\gregrg\.st_workbench\projects\MY_FOC` under
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-19_my_foc_generated_project/`.
- Added source review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_005_my_foc_generated_project.md`.
- Updated current task to
  `TASK-2026-05-19-p2-my-foc-generated-project-source-review`.
- Evidence ID:
  `EV-2026-05-19-P2-MY-FOC-GENERATED-PROJECT-001`.
- Decision: `Partial clue / generated project quarantined / Packet A not
  accepted`. `MY_FOC` proves Workbench 6.4.2 generated a real project on this
  machine, but it is configured as `SIX_STEP`, not FOC.
- Key blockers remain: `M1_CUR_READING=false`,
  `TIM1.BreakState=TIM_BREAK_DISABLE`, generated Hall on `PA15/PB3/PB10`,
  generated PWM on `PA8/PB13/PA9/PB14/PA10/PB15`, and motor placeholder
  `R57BLB50L2` / `MOONS motor for Zest Demo`.
- User clarification recorded: pins can be changed. The Hall/PWM mismatch is
  now treated as a future editable hardware/adapter or Workbench route, not a
  permanent rejection. It still needs a new reviewable FOC configuration and a
  matching physical route before Packet A can be accepted.
- Packet A still blocked. No generated-project trust, no build-only clearance,
  no FOC configuration completion, no firmware trust, no continuity evidence,
  no powered readiness, no Hall readiness, no Motor Profiler readiness, no
  motor readiness, no power-stage readiness, and no sensorless readiness is
  upgraded.
- No build, flash, 24V, power-board connection, motor connection, Gate PWM
  output, Motor Profiler, Motor Pilot, Hall closed-loop, or sensorless / SMO
  claim is authorized.
- Verification: `python -m unittest discover -s tests` passed with 59 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8265 chunks.

## 2026-05-19 Packet A Board Designer / Manager GUI-Only Checklist

- Added no-power GUI-only checklist:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_board_designer_manager_gui_checklist_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-packet-a-board-designer-manager-gui-checklist`.
- Evidence ID:
  `EV-2026-05-19-P2-PACKET-A-BOARD-DESIGNER-MANAGER-GUI-CHECKLIST-001`.
- Decision: `GUI-only checklist prepared / Packet A still blocked`. The
  checklist tells the user how to capture Board Designer / Board Manager entry,
  custom/import/create board screens, Power/Control/Inverter board flows,
  Board Aggregation, Finalize/save prompt, Board Manager import/list path, and
  blocked states.
- Later screenshots should go under
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-19_board_designer_manager_path/screenshots/`.
- Built-in `EVALSTDRIVE101`, `STEVAL-LVLP01`, and `EVLDRIVE101-HPD` remain
  non-substitutes for the project self-developed STDRIVE101 board. If the GUI
  only exposes those built-in boards or requires source generation / hardware
  actions, the user should capture the blocked screen and stop.
- Packet A still blocked. No generated-project trust, no build-only clearance,
  no custom board source, no `.stwb6`, no firmware, no runtime API, no
  continuity evidence, no powered readiness, no Hall readiness, no Motor
  Profiler readiness, no motor readiness, no power-stage readiness, or no
  sensorless readiness is upgraded.
- No GUI launch occurred in this task. No Generate click, source generation,
  build, flash, 24V, power-board connection, motor connection, Gate PWM output,
  Motor Profiler, Motor Pilot, Hall closed-loop, or sensorless / SMO claim is
  authorized.
- Verification: `python -m unittest discover -s tests` passed with 56 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8243 chunks.

## 2026-05-19 Packet A Board Designer / Board Manager Path Review

- Added no-power Packet A path review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_board_designer_manager_path_review_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-packet-a-board-designer-manager-path-review`.
- Evidence ID:
  `EV-2026-05-19-P2-PACKET-A-BOARD-DESIGNER-MANAGER-PATH-001`.
- Decision: `Board Designer / Board Manager path exists as local documentation
  and tool clue / Packet A still blocked`. Workbench config references Board
  Designer and Board Manager, the executables exist locally, and the local
  Board Designer manual describes custom board creation/import and board
  aggregation workflows.
- Built-in `EVALSTDRIVE101`, `STEVAL-LVLP01`, and `EVLDRIVE101-HPD` remain
  examples only. They cannot replace evidence for the project self-developed
  STDRIVE101 board.
- Packet A is not accepted. Generated-project trust and build-only
  generated-project clearance remain `Not allowed`. No self-developed board
  definition, `.stwb6`, selected-field screenshot, generated project, build,
  flash, continuity, powered readiness, Hall readiness, Motor Profiler
  readiness, motor readiness, or sensorless readiness is upgraded.
- Next valid Packet A task, if used later, is GUI-only path confirmation and
  screenshot/source capture for a custom/user board; if that cannot be made
  reviewable, the fallback is surrogate build-only planning without
  generated-project trust or separate hardware-rework planning.
- No GUI launch occurred in this review. No source generation, build, flash,
  24V, power-board connection, motor connection, Gate PWM output, Motor
  Profiler, Motor Pilot, Hall closed-loop, or sensorless / SMO claim is
  authorized.
- Verification: `python -m unittest discover -s tests` passed with 53 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8231 chunks.

## 2026-05-19 Software Hall Adapter Design Review

- Added no-power software Hall adapter design review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_design_review_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-software-hall-adapter-design-review`.
- Evidence ID:
  `EV-2026-05-19-P2-SOFTWARE-HALL-ADAPTER-DESIGN-001`.
- Decision: `Software Hall adapter remains no-power design review / Packet A
  not accepted`. Current PCB2 Hall route remains
  `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`; the review defines only future GPIO/EXTI
  sampling, edge timestamping, valid-state filtering, minimal ISR responsibility,
  and MCSDK integration boundaries.
- Hard stops are explicit: if Workbench / MCSDK requires same-timer hardware
  Hall, if the adapter would invade the high-frequency FOC / JEOC path, or if
  no build-only verification boundary can be defined after accepted Packet A,
  the next step becomes a separate hardware-rework planning task.
- Packet A selected fields remain not accepted. Generated-project trust and
  build-only generated-project clearance remain `Not allowed`. No software Hall
  adapter, runtime API, firmware implementation, generated project, build, flash,
  continuity, powered readiness, Hall readiness, Motor Profiler readiness, motor
  readiness, or sensorless readiness is upgraded.
- No GUI launch, source generation, build, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Hall closed-loop, or
  sensorless / SMO claim is authorized.
- Verification: `python -m unittest discover -s tests` passed with 50 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8209 chunks.

## 2026-05-19 Current PCB2 Packet A / Firmware Feasibility Review

- Added no-power feasibility review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/current_pcb2_packet_a_firmware_feasibility_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-current-pcb2-packet-a-firmware-feasibility`.
- Evidence ID:
  `EV-2026-05-19-P2-CURRENT-PCB2-PACKET-A-FIRMWARE-FEASIBILITY-001`.
- Decision: `No-PCB-change route remains feasibility only / Packet A not
  accepted`. Current PCB2 `HIN/LIN` route is not cleared as a standard MCSDK
  `TIM1` complementary PWM selected-field claim, and `PA0/PA1/PB4` is not
  cleared as a same-timer hardware Hall interface.
- The no-PCB-change path remains open only as a later no-power firmware design
  review for software Hall sampling, edge timestamping, valid-state filtering,
  and MCSDK integration boundaries.
- Packet A remains not accepted. Generated-project trust and build-only
  generated-project clearance remain `Not allowed`.
- Hardware rework is not executed or decided in this task; it remains a
  fallback if Workbench/firmware feasibility fails.
- No GUI launch, source generation, build, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Hall closed-loop, or
  sensorless / SMO claim is authorized.
- Verification: `python -m unittest discover -s tests` passed with 47 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed.

## 2026-05-19 Current PCB2 Hall/PWM No-Power Strategy Review

- Added no-power strategy review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/current_pcb2_hall_pwm_strategy_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-current-pcb2-hall-pwm-strategy`.
- Evidence ID:
  `EV-2026-05-19-P2-CURRENT-PCB2-HALL-PWM-STRATEGY-001`.
- Decision: `No-power strategy review opened / no PCB change first`. The
  current PCB2 PWM / driver-input route under review is
  `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10`, and the
  current PCB2 Hall route remains `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`.
- The old standard `TIM1` complementary PWM draft and the old
  `PA15/PB3/PB10` hardware Hall draft are now historical or alternate
  candidates only. They are not accepted current PCB2 configuration evidence.
- `PA0/PA1/PB4` is not accepted as a same-timer hardware Hall set. This task
  records only software Hall feasibility review as a future no-power Packet A /
  firmware design topic; it does not upgrade Hall readiness.
- `PB3` is current PCB2 `LIN1`, not current PCB2 `HALL_B`. Any alternate use
  of `PB3` as Hall still needs SWO release/isolation and a new accepted route.
- Packet A remains `Partial clue / Preparation only / stopped`;
  generated-project trust remains `Not allowed`; build-only generated-project
  work remains closed.
- No GUI launch, source generation, build, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Hall closed-loop, or
  sensorless / SMO claim is authorized.
- Verification: `python -m unittest discover -s tests` passed with 44 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` built 8175 chunks. The project dry-run no-power
  safety scan was not completed because the tool platform rejected the call
  with a usage-limit message; it was not bypassed.

## 2026-05-19 PCB2 Mapping / Pin-1 / Protection Intake

- Archived user-provided current PCB2 mapping and pin-1 source packet under:
  `hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/`.
- Added no-power Packet B/C plus PB3/SWO/Hall source review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md`.
- Updated current task to
  `TASK-2026-05-19-p2-pcb2-mapping-pin1-protection-intake`.
- Evidence ID:
  `EV-2026-05-19-P2-PCB2-MAPPING-PIN1-PROTECTION-001`.
- Decision: `Partial clue / accepted current PCB2 mapping source; Hall/PWM
  conflicts clarified`. The user states the answer corresponds to current
  PCB2. The packet provides P1-P15 mapping, connector-orientation images, Hall
  relationship, PB3/SWO handling, and STDRIVE101 `DT/MODE` / `CP` / `SCREF` /
  `nFAULT` / `STBY` statements.
- Latest clarification: `PC7/PB3/PB10` was an alternate suggestion, not current
  PCB2 physical routing. Current PCB2 Hall routing is
  `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`; `IA/IB/IC` are Hall signal nets after
  pull-up/filtering, and `ADC_U/ADC_V/ADC_W` are current-sense nets.
- `PB3` is `LIN1`, not current PCB2 `HALL_B`; `PB10` is `HIN2`, not current
  PCB2 `HALL_C`. The remaining blocker is now software/Workbench strategy:
  current Hall inputs `PA0/PA1/PB4` are not a normal three-channel hardware
  Hall timer set and need a no-power Packet A / firmware design decision.
- Generated-project trust remains `Not allowed`. Packet A selected fields,
  no-power continuity, powered readiness, motor readiness, Hall readiness,
  Motor Profiler readiness, and sensorless readiness remain unchanged.
- No 24V, power-board connection, motor connection, Gate PWM output, Motor
  Profiler, source generation, build, flash, Hall closed-loop, or sensorless /
  SMO claim is authorized.
- Verification passed: `python -m unittest discover -s tests` ran 41 tests OK
  after restoring the required `does not release SWO` boundary phrase;
  `git diff --check` passed with line-ending warnings only; the project dry-run
  no-power safety scan reported no unsafe added claims; `python
  tools/build_vector_store.py` rebuilt the local index with 8160 chunks.

## 2026-05-19 P2 Minimal Hardware Request And Workbench Asset Probe

- Added the short hardware-teammate request:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/hardware_teammate_min_request_2026-05-19.md`.
- Added the read-only Packet A Workbench asset probe:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_workbench_asset_probe_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-min-hw-request-workbench-asset-probe`.
- Evidence ID:
  `EV-2026-05-19-P2-MIN-HW-REQ-WB-ASSET-PROBE-001`.
- Decision: workflow/evidence-governance only. The minimal request narrows the
  next hardware-teammate packet to three P0 items first: exact Gerber PCB2
  revision confirmation, complete `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping,
  and marked `CN3` / `J_HALL` pin-1 evidence.
- Packet A local asset probe found installed Board Designer and Board Manager
  executables referenced by Workbench config, plus built-in STDRIVE101 board
  JSON definitions. This is only a local path clue; no accepted custom
  self-developed STDRIVE101 board definition, project-specific `.stwb6`, or
  selected-field screenshot exists.
- Generated-project trust remains `Not allowed`. Packet A/B/C, PB3/SWO,
  `J_HALL`, continuity, powered readiness, motor readiness, Hall readiness,
  Motor Profiler readiness, and sensorless readiness remain unchanged.
- No 24V, power-board connection, motor connection, Gate PWM output, Motor
  Profiler, source generation, build, flash, Hall closed-loop, or sensorless /
  SMO claim is authorized.
- Verification passed: `python -m unittest discover -s tests` ran 41 tests OK;
  `git diff --check` passed with line-ending warnings only; the project dry-run
  no-power safety scan reported no unsafe added claims; `python
  tools/build_vector_store.py` rebuilt the local index with 8133 chunks.

## 2026-05-19 P2 Hardware Supplement Handoff

- Added hardware-teammate handoff:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/hardware_supplement_handoff_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-hardware-supplement-handoff`.
- Evidence ID:
  `EV-2026-05-19-P2-HARDWARE-SUPPLEMENT-HANDOFF-001`.
- Decision: workflow/evidence-governance only. The handoff converts the
  latest `.epro` and Gerber follow-up blockers into exact hardware teammate
  requests: Gerber exact revision confirmation,
  `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping, `CN3` / `J_HALL` pin-1
  orientation, Hall A/B/C mapping, PB3/SWO release or alternate Hall B route,
  STDRIVE101 `DT/MODE` / `STBY` / `CP` / `SCREF` / `NFAULT` protection-chain
  details, optional EasyEDA Pro PCB source, and later no-power continuity /
  short-check records.
- Packet A remains `Partial clue / Preparation only / stopped`;
  generated-project trust remains `Not allowed`.
- Packet B/C still has accepted board-side schematic + Gerber/flying-probe
  clues only; NUCLEO `CN8`, STM32 endpoint mapping, connector orientation,
  continuity, powered readiness, motor readiness, Hall readiness, and
  sensorless readiness remain not allowed.
- No 24V, power-board connection, motor connection, Gate PWM output, Motor
  Profiler, source generation, build, flash, Hall closed-loop, or sensorless /
  SMO claim is authorized.
- Verification passed: `python -m unittest discover -s tests` ran 41 tests OK;
  `python tools/build_vector_store.py` rebuilt the local index with 8110
  chunks.

## 2026-05-19 Gerber PCB2 Manufacturing Package Intake

- Archived hardware-teammate supplied Gerber package:
  `hardware/schematic/2026-05-19_gerber_pcb2_stdrive101/Gerber_PCB2_2026-05-19.zip`.
- Added no-power Packet B/C Gerber review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_003_gerber_pcb2.md`.
- Decision: `Partial clue / accepted board-side Gerber + flying-probe net
  clue`. The ZIP contains a four-layer EasyEDA Pro Gerber manufacturing
  package plus drill files and `FlyingProbeTesting.json`; Gerber headers record
  `EasyEDA Pro v3.2.91`, generated `2026-05-19 11:16:57`, and the archived
  ZIP hash is
  `F61C073C5A9E71CD608460976430D3F927E7AD48EC05A42661E77662AF04CE56`.
- Accepted exact board-side clues: `CN3` 15-pin pad/net mapping, `U1`
  STDRIVE101 pad nets, PWM input paths through `R4-R9`, `R12/R14/R17`
  shunt/current-sense pad nets, `U2=J_HALL` pad-net clue, `CN2=J_MOTOR`,
  `NFAULT -> R3 -> 3V3 / CN3_13`, `SCREF` divider, `REG12`, bootstrap, and
  `OUT1/2/3` motor output pad nets.
- Still blocked: exact fabrication/revision match confirmation, NUCLEO `CN8`
  endpoint mapping, STM32 pin mapping, PB3/SWO release, `J_HALL` physical
  pin-1 / Hall A/B/C numbering, Packet A/Workbench selected fields,
  generated-project trust, continuity checks, power-stage readiness, Motor
  Profiler readiness, motor readiness, and sensorless readiness.

## 2026-05-19 ProDoc P1 EDA Pro Source Intake

- Archived user-confirmed self-developed STDRIVE101 driver-board source:
  `hardware/schematic/2026-05-19_prodoc_p1_stdrive101_epro/ProDoc_P1_2026-05-19.epro`.
- Added no-power Packet B/C source review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_002_prodoc_p1_epro.md`.
- Decision: `Partial clue / accepted schematic-source clue`. The `.epro`
  is a readable EDA Pro schematic source with one sheet, project/title-block
  metadata `STDRIVE101_3Phase_Inverter`, create/update time
  `2026-05-19 10:26:36`, and source hash
  `B9D67B9E5D6DD08D5229928636DFA8048C081DED7EE230ADDB79F20D83D718A1`.
- Accepted exact clues: `U1=STDRIVE101`, `Q1-Q6=NCEP40T11G`, three
  `20mOhm` shunts, `CN3` 15-pin board-side control connector, `U2=J_HALL`,
  `CN2=J_MOTOR`, `CN3` pinout, and visible `NFAULT`, `REG12`, `SCREF`,
  `BOOTx`, `OUTx`, `GHSx`, and `GLSx` schematic nets.
- The archive has no PCB layout evidence: `project.json` has `pcbs: {}`, the
  board entry has an empty `pcb` field, and `PCB/` is only an empty directory
  entry. PCB routing, NUCLEO `CN8` endpoint mapping, STM32 pin mapping,
  PB3/SWO release, `J_HALL` numbering, Hall readiness, power-stage readiness,
  Packet A/Workbench selected fields, generated-project trust, Motor Profiler
  readiness, motor readiness, and sensorless readiness remain unchanged and
  not allowed.

## 2026-05-19 Packet A Workbench Capture Attempt

- Added no-power Packet A Workbench capture-attempt review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_001_packet_a_workbench_capture_attempt.md`.
- Captured Workbench 6.4.2 launch and board-selection screenshots under:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/`.
- Decision: `Partial clue / stopped`. Workbench launches and the component path
  can show `NUCLEO-G474RE` / `STM32G474RETx` as the control-board context, but
  no accepted Custom / Generic self-made STDRIVE101 power-stage context was
  captured.
- User clarified on 2026-05-19 that the project uses a self-developed motor
  driver board based on the STDRIVE101 chip. Therefore built-in ST power-board
  entries such as `EVALSTDRIVE101` or `STEVAL-LVLP01` cannot be treated as
  board-match substitutes for Packet A.
- No project-specific `.stwb6`, no selected-field PWM/current-sense/Hall/driver
  protection/pin-usage screenshots, and no generated motor-control project were
  created. Generated-project trust remains `Not allowed`.
- Packet A remains `Partial clue / Preparation only`; Packet B/C, CN8 routing,
  STDRIVE101 protection-path proof, PB3/SWO release, `J_HALL`, Hall readiness,
  power-stage readiness, Motor Profiler readiness, motor readiness, and
  sensorless readiness remain unchanged. No 24V, power-board connection, motor
  connection, Gate PWM, Motor Profiler, build, flash, or generated
  motor-control project is authorized.

## 2026-05-18 PB3 / SWO CubeMX Probe

- Added no-power PB3/SWO source-packet review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-18_002_pb3_swo_probe.md`.
- Captured current CubeMX state screenshot:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-18_cubemx_pb3_current_swo_fullscreen.png`.
- Added dated configuration-layer probe:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/pb3_tim2_ch2_probe_2026-05-18.ioc`.
- Captured probe screenshot:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-18_cubemx_pb3_tim2_ch2_probe_fullscreen.png`.
- Decision: `Partial clue` only. The accepted NUCLEO draft still records
  `PB3.GPIO_Label=T_SWO` and `PB3.Signal=SYS_JTDO-SWO`; the probe copy can show
  `PB3` as `TIM2_CH2` / `HALL_B_PROBE` in CubeMX, but it does not prove SWO
  release / isolation, Workbench Hall B selection, CN8 / `J_HALL` endpoint
  mapping, or Hall readiness.
- Packet A/B/C, generated-project trust, CN8 routing, STDRIVE101
  protection-path proof, Hall closed-loop, power-stage readiness, Motor
  Profiler readiness, motor readiness, and sensorless readiness remain
  unchanged. No 24V, power-board connection, motor connection, Gate PWM,
  Motor Profiler, build, flash, or generated motor-control project is
  authorized.

## 2026-05-18 Motor Wiring Definition Intake

- Added user-provided motor wiring definition source:
  `hardware/motor/2026-05-18_57blf01_motor_wiring_definition.jpg`.
- Added extracted wiring note:
  `hardware/motor/2026-05-18_57blf01_motor_wiring_definition.md`.
- Added P2 source-packet review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-18_001_motor_wiring_definition.md`.
- Updated no-power motor log:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/motor_no_power_measurement_log_2026-05-16.md`.
- Extracted candidate wire colors: phase `U` = yellow thick wire, `V` = red
  thick wire, `W` = black thick wire; Hall `HU` = yellow thin wire, `HV` =
  white thin wire, `HW` = blue thin wire, `H+` / `+5V` = red thin wire, and
  `H-` / `GND` = black thin wire.
- Decision: `Partial clue` only. This source helps future Workbench notes and
  no-power wiring labels, but it does not prove physical harness inspection,
  continuity, Hall powered behavior, phase/Hall alignment, `J_HALL` numbering,
  Motor Profiler data, or motor readiness.
- No 24V, power-board connection, motor connection, Gate PWM, Motor Profiler,
  Hall closed-loop, or sensorless / SMO claim is authorized.

## 2026-05-18 Packet A Capture Task Package Refresh

- Added workflow-only Packet A capture task package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_task_2026-05-18.md`.
- Updated `workflow/ACTIVE_TASK.md` to point at the P2 Packet A capture
  preparation task with `open/ready` status and a no-GUI, no-generation,
  no-build, no-flash, no-hardware boundary.
- Refreshed P2 entry points:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
  and `apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md`.
- Registered workflow-only evidence:
  `EV-2026-05-18-P2-PACKET-A-TASK-PACKAGE-001`.
- Verification passed: `python -m unittest discover -s tests` ran 41 tests OK;
  `python tools\build_vector_store.py` rebuilt the local index successfully.
- Decision unchanged: Packet A remains `Partial clue / Preparation only`;
  generated-project trust remains `Not allowed`; Packet B/C, `PB3` / SWO,
  `J_HALL`, CN8 routing, and STDRIVE101 protection-path blockers remain open.
- This update does not create a new `.stwb6`, does not add Workbench
  screenshots, does not launch Workbench, does not generate or build source,
  and does not authorize 24V, power-board connection, motor connection, Gate
  PWM, Motor Profiler, Hall closed-loop, or sensorless / SMO claims.

## 2026-05-17 Vendor Motor And Hardware Pin Table Intake

- Added supplier motor-parameter source:
  `hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.jpg`.
- Added extracted motor review note:
  `hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.md`.
- Added hardware teammate pin-assignment PDF:
  `hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.pdf`.
- Added extracted pin-table review note:
  `hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.md`.
- Added source-packet review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`.
- Added MCU pin compatibility cross-check:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcu_pin_compatibility_check_2026-05-17.md`.
- Decision: `Partial clue` only. The motor values are supplier clues, not
  project measurements or Motor Profiler results. The pin table is titled for
  `STM32G431RB`, but the hardware teammate says the relevant G431/G474 pins are
  the same; local MCSDK `STM32G431RBTx` / `STM32G474RETx` asset comparison
  supports the compared key TIM1, TIM2, USART, and OPAMP-capable rows.
- `J_HALL` pin numbering is explicitly uncertain. Hall A/B/C rows remain
  candidate or blocked until board source or continuity evidence confirms the
  connector. CN8 endpoint proof and `PB3` / SWO release remain separate
  blockers.
- If Workbench requires a motor entry, the preferred no-power label is now
  `57BLF01_VENDOR_CANDIDATE`, replacing the generic placeholder name only as a
  label. It does not upgrade motor parameters to accepted measurements.
- Generated-project trust remains `Not allowed`; no 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  sensorless / SMO claim is authorized.

## 2026-05-16 Packet A Custom Workbench Capture Package

- Added the new project-specific Packet A capture package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`.
- Added hand-run Workbench guide:
  `workbench_no_power_configuration_guide_2026-05-16.md`.
- Added no-power motor measurement template:
  `motor_no_power_measurement_log_2026-05-16.md`.
- Added pin assignment table:
  `pin_assignment_table_2026-05-16.md`.
- Added preparation review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`.
- User clarified that `My_First_FOC.stwb6` is a previous toolchain-learning
  leftover and that its `EVALSTDRIVE101` power-board choice is arbitrary. It
  remains preserved as a legacy `Partial clue` only and is not the source for
  the new project-specific Packet A path.
- New intended capture target: `NUCLEO-G474RE` / `STM32G474RETx`, Custom /
  Generic STDRIVE101 power stage, FOC, Hall fallback, 3-shunt current sensing,
  motor label `57BLF01_VENDOR_CANDIDATE` if Workbench requires a motor entry,
  and no generated source. The older `PLACEHOLDER_not_profiled_2026-05-16`
  name is superseded as the preferred label, not upgraded into measured motor
  proof.
- Generated-project trust remains `Not allowed`. The 2026-05-16 package
  prepares GUI capture and review, but no new `.stwb6` or selected-field
  Workbench screenshot has been accepted yet.
- Motor information collection is limited to no-power records: nameplate photo,
  wire colors, and multimeter phase-to-phase resistance clues. These are not
  Motor Profiler data and do not authorize motor connection, Hall powering, or
  closed-loop use.

## 2026-05-15 Packet A STWB6 Candidate Intake

- Found the real ST MC Workbench 6.4.2 launcher:
  `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\STMCWB.exe`.
- Found and preserved a local MCSDK 6 Workbench project candidate:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`.
- Added Packet A review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`.
- Review decision: `Partial clue`. The file records Workbench 6.4.2, FOC,
  `NUCLEO-G474RE`, `STM32G474RETx`, `EVALSTDRIVE101`, and `R57BLB50L2`, but it
  is not accepted final evidence for the custom power board, selected TIM1 PWM,
  final fault input, current-sense mode, Hall/sensorless mode, `PA2/PA3`
  policy, or `PB3` ownership.
- Updated Packet A wording to accept MCSDK 6 `.stwb6` project files as the
  current Workbench format; legacy `.stmcx` remains valid only for older
  Workbench sources.
- Generated-project trust remains `Not allowed`. This update does not prove
  CN8 routing, STDRIVE101 protection paths, power-stage readiness, Hall
  readiness, Gate PWM, Motor Profiler, motor behavior, or sensorless behavior,
  and it does not authorize 24V, power-board connection, motor connection,
  flashing, Gate PWM, Motor Profiler, Hall closed-loop, or sensorless FOC
  claims.

## 2026-05-15 Phase Gate P2 Insert

- Updated phase gate checklist:
  `workflow/phase_gate_checklist.md`.
- The phase gate now explicitly blocks jumping from NUCLEO basics directly to
  Motor Profiler or generated-project trust. It adds `P2-S1 - MCSDK No-Power
  Precheck`, `P2-S2 - Build-Only Generated Project Gate`, and a `P2 To P3
  Blocker List`.
- Current decision is unchanged: Packet A must be accepted before build-only
  generated-project work; Packet B/C, PB3/SWO, no-power continuity checks,
  current-limited bring-up settings, measurement points, stop conditions, and a
  rollback image are required before P3 powered work can open.
- This update is workflow gating only. It does not prove MCSDK MotorControl
  configuration, generated-project trust, CN8 routing, STDRIVE101
  protection-path proof, power-stage readiness, Hall readiness, Gate PWM, Motor
  Profiler, motor behavior, or sensorless behavior, and it does not authorize
  24V, power-board connection, motor connection, Gate PWM, Motor Profiler, Hall
  closed-loop, or sensorless FOC claims.

## 2026-05-15 P2 Readiness Snapshot

- Added P2 readiness snapshot:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`.
- At that snapshot time, P2 no-power planning remained in progress, Packet A
  had no accepted selected-field source, generated-project trust was
  `Not allowed`, Packet B/C and PB3/SWO remained blocked or partial clue only,
  and P3 powered or motor work was not allowed. This has since been refined by
  the 2026-05-15 legacy `.stwb6` partial clue review and the 2026-05-16 custom
  capture package preparation, while generated-project trust remains
  `Not allowed`.
- The snapshot does not prove MCSDK MotorControl configuration,
  generated-project trust, CN8 routing, STDRIVE101 protection-path proof,
  power-stage readiness, Hall readiness, Gate PWM, Motor Profiler, motor
  behavior, or sensorless behavior, and it does not authorize 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  sensorless FOC claims.

## 2026-05-15 STM32 Signal Contract And Build-Only Gate

- Added STM32-side signal contract:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stm32_side_signal_contract_2026-05-15.md`.
- Added future build-only gate:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/future_build_only_gate_2026-05-15.md`.
- The signal contract records future STM32 responsibilities for TIM1 PWM
  commands, `NFAULT`, `STBY`, `DT/MODE`, current sensing, Hall fallback,
  `PA2/PA3`, `PB3`, `3V3`, `GND_SIGNAL`, and ESP32 gateway boundaries. All
  hardware-dependent items remain blocked or candidate-only until Packet A/B/C
  or PB3/SWO evidence proves them.
- The build-only gate records that generated-project trust is currently
  `Not allowed` because Packet A is only `Partial clue`. Even after Packet A selected fields are accepted,
  a generated MCSDK project may only be treated as no-power build evidence
  until later hardware phase gates exist.
- This update does not prove MCSDK MotorControl configuration,
  generated-project trust, CN8 routing, STDRIVE101 protection-path proof,
  power-stage readiness, Hall readiness, Gate PWM, Motor Profiler, motor
  behavior, or sensorless behavior, and it does not authorize 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  sensorless FOC claims.

## 2026-05-15 Packet A Local Probe

- Added Packet A local probe:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_local_probe_2026-05-15.md`.
- Added Packet A capture checklist:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_checklist_2026-05-15.md`.
- Current result: checked repo `.stmcx`, existing screenshots,
  `apps/stm32_g474_foc/MotorControl`, `F:\STMCubeMX`,
  `C:\Users\gregrg\STM32Cube\Repository`, `C:\Users\gregrg\.stm32cubemx`, and
  common user locations (`Documents`, `Downloads`, `Desktop`). No real
  `.stmcx` and no MotorControl / Workbench configuration screenshot were found.
  Direct search of `C:\Users\gregrg` returned access denied, so this is a
  bounded local probe, not an all-disk proof.
- Packet A was not accepted by this local probe alone. It later gained only a
  legacy `.stwb6` `Partial clue` and a 2026-05-16 custom capture package
  preparation. This still does not prove MCSDK MotorControl configuration,
  generated-project trust, CN8 routing, STDRIVE101 protection-path proof,
  power-stage readiness, Hall readiness, Gate PWM, Motor Profiler, motor
  behavior, or sensorless behavior, and it does not authorize 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  sensorless FOC claims.

## 2026-05-15 P2 Non-Hardware Parallel Track

- Added non-hardware parallel track:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/non_hardware_parallel_track_2026-05-15.md`.
- User asked to skip the hardware source package branch for now. The repo now
  records this as "skipped for scheduling, not cleared": Packet B/C, `DT/MODE`,
  `STBY`, STM32 endpoint mapping, and `PB3` / SWO release remain blocked.
- Allowed parallel work is now explicit: Packet A MCSDK / MotorControl evidence,
  STM32-side signal contract, future build-only gate, and submission/evidence
  cleanup.
- This update does not prove `.stmcx`, MotorControl configuration, CN8 routing,
  STDRIVE101 protection paths, power-stage readiness, Hall readiness, Gate PWM,
  Motor Profiler, motor behavior, or sensorless behavior, and it does not
  authorize 24V, power-board connection, motor connection, Gate PWM, Motor
  Profiler, Hall closed-loop, or sensorless FOC claims.

## 2026-05-15 P2 Schematic Candidate Intake

- Imported the user-provided schematic screenshot as a preserved P2 hardware
  source candidate:
  `hardware/schematic/2026-05-15_power_board_cn8_stdrive101_schematic_candidate.png`.
- Added source note:
  `hardware/schematic/2026-05-15_power_board_cn8_stdrive101_schematic_candidate.md`.
- Added review record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_001_cn8_stdrive101_schematic_candidate.md`.
- Current decision: `Partial clue`. The screenshot can guide Packet B/C review
  because it shows CN8 labels, STDRIVE101, input resistors, `nFAULT`, `REG12`,
  `CP`, `SCREF`, bootstrap clues, MOSFETs, shunts, and Hall interface clues.
  User confirmed on 2026-05-15 that it is the current physical power board and
  was drawn by the hardware teammate. It still lacks a formal title-block
  source revision/date, STM32-side CN8-to-MCU pin mapping, accepted `DT/MODE`
  endpoint proof, and `STBY` proof.
- This update does not prove CN8 routing, STDRIVE101 protection paths, MCSDK
  MotorControl configuration, power-stage readiness, Hall readiness, Gate PWM,
  Motor Profiler, motor behavior, or sensorless behavior, and it does not
  authorize 24V, power-board connection, motor connection, Gate PWM, Motor
  Profiler, Hall closed-loop, or sensorless FOC claims.

## 2026-05-14 P2 Source Packet Review Template

- Added repeatable source packet review template:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_template_2026-05-14.md`.
- The template defines the Codex-side review path after Packet A, Packet B,
  Packet C, or `PB3` / SWO evidence arrives: Accept, Partial clue, or Reject;
  then update only the exact proven fields.
- This is a no-power review-control artifact only. It does not add `.stmcx`,
  MotorControl screenshot, CN8 / EDA / netlist evidence, STDRIVE101
  protection-path proof, or any hardware validation, and it does not authorize
  24V, power-board connection, motor connection, Gate PWM, Motor Profiler, Hall
  closed-loop, or sensorless FOC claims.

## 2026-05-14 P2 User Action Queue

- Added direct user action queue:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md`.
- The queue tells the user exactly what to provide next: first Packet B
  current-version CN8 / board-route / STDRIVE101 source evidence, then Packet A
  MCSDK / MotorControl `.stmcx` or screenshot evidence, plus `PB3` / SWO release
  evidence if Hall B remains planned.
- This is a handoff and intake artifact only. It does not prove MCSDK
  MotorControl configuration, does not prove CN8 routing, does not prove
  STDRIVE101 protection paths, and does not authorize 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  sensorless FOC claims.

## 2026-05-14 P2 Source Packet Request Pack

- Added concrete source packet request pack:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_request_pack_2026-05-14.md`.
- The request pack turns the intake checklist into three handoff packets:
  MCSDK / MotorControl configuration evidence, CN8 / board-route evidence, and
  board-level STDRIVE101 protection-path evidence.
- It records required fields, rejected sources, Codex review steps, and the
  current blocked state for `.stmcx`, MotorControl screenshots, CN8 / EDA /
  netlist evidence, STDRIVE101 protection paths, and `PB3` Hall/SWO ownership.
- This is a handoff artifact only. It does not add board evidence, does not
  prove MCSDK MotorControl configuration, does not prove CN8 routing or
  STDRIVE101 protection paths, and does not authorize 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  sensorless FOC claims.

## 2026-05-14 P2 Source Packet Intake 闂傤厾骞?
- Added P2 source packet intake checklist:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_intake_checklist_2026-05-14.md`.
- The checklist defines accepted evidence packets for MCSDK `.stmcx` /
  MotorControl screenshots, CN8 / EDA / netlist / high-resolution route
  evidence, and board-level STDRIVE101 protection-path source evidence.
- It also rejects low-resolution screenshots, oral descriptions, old or
  unknown-version files, incomplete crops, generated source without matching
  configuration evidence, and the excluded WeChat-side `netlist_PADS.net`
  candidate.
- This is an evidence-entry rule only. It does not prove MCSDK MotorControl
  configuration completion, CN8 routing, STDRIVE101 protection paths,
  power-stage readiness, Hall readiness, or sensorless readiness, and it still
  does not authorize 24V, power-board connection, motor connection, Gate PWM,
  Motor Profiler, Hall closed-loop, or sensorless FOC claims.

## 2026-05-14 P2 STDRIVE101 娣囨繃濮㈢捄顖氱窞鐎光剝鐓?
- Added STDRIVE101 protection-path review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`.
- The review fixes the required P2 checklist for `DT/MODE`, `nFAULT`,
  `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, standby, and VDS monitoring.
- ST official product page and datasheet (`DS13472 Rev 2`, June 2022) were
  rechecked on 2026-05-14. The official source still describes STDRIVE101 as a
  triple half-bridge gate driver with two input strategies selected by
  `DT/MODE`, 12 V `REG12` gate supply, overcurrent comparator, VDS monitoring,
  UVLO, thermal shutdown, and standby behavior.
- The existing schematic screenshot remains only a low-grade clue. It does not
  prove CN8 routing, PCB routing, connector pinout, STDRIVE101 protection-path
  correctness, or power-stage readiness.
- This update still does not authorize 24V, power-board connection, motor
  connection, Gate PWM, Motor Profiler, Hall closed-loop, or sensorless FOC
  claims.

## 2026-05-14 P2 Parallel Evidence Push

- Added CN8 / STDRIVE101 route review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/cn8_stdrive101_route_review_2026-05-14.md`.
- Rechecked the `.stmcx` / MotorControl side: repo search still found no
  `.stmcx`; narrow checks of `F:\STMCubeMX`,
  `C:\Users\gregrg\STM32Cube\Repository\MCSDK_v6.4.2-Full`, and VS Code
  extension folders still did not prove a saved Workbench project, standalone
  Workbench launcher, or MotorControl configuration page.
- Route review now explicitly accepts only current-version EDA, schematic PDF,
  netlist, or high-resolution route crop as board-route evidence. The existing
  schematic screenshot remains a low-grade clue only.
- The WeChat-side `netlist_PADS.net` candidate was not imported and is not used
  as current board evidence.
- Current blockers remain: real `.stmcx` or MotorControl configuration
  screenshot; accepted CN8 / route evidence; accepted STDRIVE101 `nFAULT`,
  `DT/MODE`, `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, standby, and VDS
  monitoring source evidence.
- This update still does not authorize 24V, power-board connection, motor
  connection, Gate PWM, Motor Profiler, Hall closed-loop, or sensorless FOC
  claims.

## 2026-05-14 P2 GUI 闁板秶鐤嗙拠浣瑰祦閹恒劏绻?
- Codex 娴ｈ法鏁?`F:\STMCubeMX\STM32CubeMX.exe` 閹垫挸绱戝韫箽鐎涙娈?NUCLEO-G474RE
  `.ioc` 閼藉顢嶉敍灞借嫙閺傛澘顤?GUI 閹规洝骞忕拋鏉跨秿閿?  `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_result_2026-05-14.md`.
- 閺傛澘顤冮幋顏勬禈閿?  `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_launch_attempt.png`
  閸?  `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`.
- 閹搭亜娴樼拠浣规 CubeMX 閸欘垯浜掗幎濠佺箽鐎涙娈?`.ioc` 閹垫挸绱戦崚?`Pinout & Configuration`
  妞ょ敻娼伴敍宀€鐛ラ崣锝嗙垼妫版ɑ妯夌粈?`STM32G474RETx - NUCLEO-G474RE`閿涙矖.ioc` 鐠囪娲栨禒宥団€樼拋?  `PB12/TIM1_BKIN`閵嗕梗PB14/TIM1_CH2N`閵嗕梗PA2/PA3` VCP 閸?`PB3` SWO閵?- `rg --files -g "*.stmcx"` 閸?GUI 鐏忔繆鐦崥搴濈矝濞屸剝婀侀幍鎯у煂 `.stmcx`閿涙稒婀版潪顔荤瘍濞屸剝婀?  閹规洝骞?MCSDK MotorControl 闁板秶鐤嗘い鐐光偓鍌氱秼閸撳秵鏌婃晶鐐垫畱閺?CubeMX `.ioc` GUI fallback
  鐠囦焦宓侀敍灞肩瑝閺?Workbench / MotorControl 闁板秶鐤嗙拠浣瑰祦閵?- 鏉╂瑤绮涢悞鏈电瑝閹哄牊娼?24V閵嗕礁濮涢悳鍥ㄦ緲閵嗕胶鏁搁張鎭掆偓涓焌te PWM閵嗕府otor Profiler閵嗕胶鍎宠ぐ?鐠嬪啳鐦妴?  Hall 闂傤厾骞嗛幋鏍ㄦ￥閹?FOC 缂佹捁顔戦妴?
## 2026-05-14 P2 Workbench 閸忋儱褰涢幒銏＄ゴ

- Codex 閺傛澘顤?Workbench 閸忋儱褰涢幒銏＄ゴ鐠佹澘缍嶉敍?  `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`.
- 閻╊喗鐖ｅΛ鈧弻銉洬閻?repo閵嗕梗F:\STMCubeMX`閵嗕梗C:\Users\gregrg\STM32Cube\Repository\MCSDK_v6.4.2-Full`閵?  VS Code STM32 extension閵嗕梗.stm32cubemx` 閸滃苯鐖剁憴?ST 缁嬪绨惄顔肩秿閵?- 缂佹捁顔戦敍姘拱閺堝搫鍑＄€瑰顥?MCSDK `MotorControl` package 閺佺増宓侀敍宀冨厴閻鍩?  `MotorControl_Configs.xml`閵嗕梗MotorControl_Modes.xml`閵嗕梗MCSDK/`閵嗕梗templates/`閵?  `libMP/` 閸?`libHSO/`閿涙稐绲炬禒宥嗙梾閺?repo `.stmcx`閵嗕胶瀚粩?Workbench launcher 閹?  MotorControl 闁板秶鐤嗘い鍨焻閸ヤ勘鈧?- 閸ョ姵顒?P2 瑜版挸澧犻懗鍊熺槈閺勫簶鈧发CSDK MotorControl package 閺佺増宓佺€涙ê婀垾婵撶礉娑撳秷鍏樼拠浣规
  閳ユ凡orkbench 妞ゅ湱娲伴柊宥囩枂瀹歌弓绻氱€涙ǚ鈧縿鈧?
## 2026-05-14 P2 鐠囦焦宓侀崠鍛纯閺?
- 瀹稿弶鏌婃晶鐐茬秼閸?P2 鐠囦焦宓侀崠鍜冪窗
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`.
- 鐠囦焦宓侀崠鍛邦唶瑜版洖缍嬮崜宥勭波鎼存挾婀＄€圭偛绨辩€涙﹫绱板▽鈩冩箒 `.stmcx`閿涘苯鍑￠張?CubeMX 妫ｆ牠銆夐幋顏勬禈閸?  NUCLEO-G474RE CubeMX `.ioc` 閼藉顢嶉敍娑楃矝濞屸剝婀?Workbench/CubeMX MotorControl
  闁板秶鐤嗘い鍨焻閸ヤ勘鈧竼N8/EDA/netlist 鐠ф壆鍤庣拠浣规閿涘奔绡冨▽鈩冩箒閺夎法楠?STDRIVE101 娣囨繃濮㈢捄顖氱窞鐠囦焦妲戦妴?- 鐠囦焦宓侀崠鍛Ω `PB12/TIM1_BKIN`閵嗕梗PB14/TIM1_CH2N`閵嗕梗PA2/PA3`閵嗕梗PB3`閵?  `DT/MODE` 閸?STDRIVE101 娣囨繃濮㈡い瑙勬杹鏉╂盯妯嗘繅鐐躲€冮敍宀勪缉閸忓秵濡搁懡澶嬵攳瀵洝鍓艰ぐ鎾村灇
  閸欘垯淇婇幒銉у殠閵?- 鏉╂瑤绮涢悞璺哄涧閺?P2 閺冪姴濮涢悳鍥槈閹诡喗涓嶉悶鍡礉娑撳秵宸块弶鍐т繆娴犺崵鏁撻幋鎰畱 MCSDK 瀹搞儳鈻奸敍灞肩瘍娑撳秵宸块弶?  24V閵嗕礁濮涢悳鍥ㄦ緲閵嗕胶鏁搁張鎭掆偓涓焌te PWM閵嗕府otor Profiler閵嗕笭all 闂傤厾骞嗛幋鏍ㄦ￥閹?FOC 缂佹捁顔戦妴?
## 2026-05-14 P2 NUCLEO CubeMX 鐎圭偞鎼烽懡澶嬵攳

- 閻劍鍩涢幐?NUCLEO-G474RE Board Selector 鐠侯垰绶炵€瑰本鍨氶幍瀣Ω閹靛妫ら崝鐔哄芳鐎圭偞鎼烽敍灞借嫙娣囨繂鐡?  CubeMX `.ioc` 閼藉顢嶉敍?  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`.
- `.ioc` 鐠囪娲栫涵顔款吇閿涙瓪PA13/PA14` 娑?SWD閿涘畭PA2/PA3` 娑?NUCLEO VCP閿?  `PB3` 娑?SWO閿涘畭PB12` 娑?`TIM1_BKIN`閿涘畭PB14` 娑?`TIM1_CH2N`閵?- 鏉╂瑨鐦夐弰?CubeMX 闁板秶鐤嗙仦鍌涘复閸欐缍嬮崜?NUCLEO 閼藉顢嶉崪灞艰⒈娑擃亜鍙ч柨顔尖偓娆撯偓澶庡壖閿涙稐绮涙稉宥堢槈閺?  `.stmcx`閵嗕府CSDK MotorControl 瀹搞儳鈻奸妴涓哊8/EDA/netlist 鐠ф壆鍤庨妴涓糡DRIVE101
  娣囨繃濮㈢捄顖氱窞閵嗕笩ate PWM閵嗕府otor Profiler閵嗕笭all 闂傤厾骞嗛幋鏍ㄦ￥閹?FOC閵?
## 2026-05-14 Codex Dual-Teacher Gate Update

- Codex continuation is now hardened in
  `workflow/codex_dual_teacher_execution_gate.md`.
- `AGENTS.md`, `workflow/teaching_contract.md`, `workflow/prompt_recipes.md`,
  `workflow/session_close_checklist.md`, and the project Skill source now point
  to the same four-line gate:
  `妞ゅ湱娲伴惄顔界垼` / `鐎涳缚绡勯惄顔界垼` / `娣囶喗鏁奸懠鍐ㄦ纯` / `缁備焦顒涢懠鍐ㄦ纯`.
- New regression tests in `tests/test_workflow_contracts.py` check that the gate
  stays linked from the main entry points and keeps the no-power boundary.
- This is a workflow-control update only. It does not authorize 24V, power
  board connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop,
  or sensorless FOC claims.

## 2026-05-14 P2 No-Power GUI Evidence Update

- CubeMX Home screenshot captured:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png`.
- Next GUI-only checklist added:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_checklist_2026-05-14.md`.
- This proves CubeMX GUI launch visibility. The later NUCLEO `.ioc` draft proves
  a CubeMX board/pin configuration was saved, but still does not prove a saved
  MCSDK MotorControl configuration, generated firmware, hardware wiring, Gate
  PWM output, Motor Profiler result, Hall closed-loop behavior, or motor behavior.
- Current blockers remain: real `.stmcx` or Workbench/CubeMX MotorControl
  configuration screenshot; `PB12/TIM1_BKIN` confirmation against
  CubeMX/Workbench plus CN8/EDA/netlist evidence.

## 2026-05-14 NUCLEO Firmware Update

- The NUCLEO baseline now uses LPUART1 RX DMA + IDLE for command reception.
- The interrupt callback only copies received bytes into a ring buffer and
  restarts DMA; command parsing and `printf()` stay in the main loop.
- Debug build passed:
  `apps/stm32_g474_foc/nucleo_g474re_baseline/build/Debug/nucleo_g474re_baseline.elf`.
- Build size after the change: RAM 2552 B, FLASH 23652 B.
- Detailed log:
  `experiments/2026-05-09_nucleo_baseline/logs/2026-05-14_uart_dma_idle_build.md`.
- This is firmware/build progress only. It does not authorize 24V, power board,
  motor, Gate PWM, Motor Profiler, Hall closed-loop, or SMO work.

## 2026-05-14 UART Protocol Model Update

- `src/protocol_model.py` now includes `LineFramer` for DMA/IDLE-like byte
  chunks and newline-delimited JSON frames.
- `tests/test_protocol_model.py` now covers chunk-split frames, multiple frames
  in one chunk, empty lines, oversize drop, discard-until-line-end behavior,
  and recovery.
- `python -m unittest discover -s tests` passes with 24 tests.
- This advances the ESP32/STM32 command path without touching power hardware.

## 2026-05-14 P2 Pin / Config Safety Review

- User clarified they are already familiar with the toolchain; future teaching
  should skip basic CubeMX/CubeIDE navigation unless explicitly requested.
- Next-ring review artifact added:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md`.
- This review defines evidence classes, hard stops, and the minimum packet
  required before trusting any generated MCSDK configuration:
  Workbench/CubeMX `.stmcx` or screenshot, CN8/EDA/netlist routing evidence,
  and STDRIVE101 `nFAULT` / `DT/MODE` / protection-path evidence.
- This is still P2 no-power evidence only. It does not authorize generated
  PWM behavior, Motor Profiler, power-board connection, motor connection, Hall
  closed-loop, or sensorless FOC claims.

# CURRENT_STATUS

閺堚偓閸氬孩娲块弬甯窗2026-05-14

鏉╂瑤閲滈弬鍥︽閺勵垶銆嶉惄顔解偓缁樺付妞ょ偣鈧倹鐦″▎锛勬埛缂?FOC 妞ゅ湱娲伴弮璁圭礉閸忓牐顕版潻娆撳櫡閿涘苯鍟€鐠?`AGENTS.md`閵嗕梗materials/START_HERE.md` 閸?`docs/00_project_truth/project_context.md`閵?

## 瑜版挸澧犻梼鑸殿唽

妞ゅ湱娲版径鍕艾 NUCLEO 閸╄櫣顢呭銉р柤闂冭埖顔岄敍灞借嫙瀹告彃鐣幋鎰秼閸?P1 濮掑倸搴风仦鍌炵崣閺€韬测偓?026-05-09 瀹歌尙鏁撻幋鎰嫙缂傛牞鐦ч柅姘崇箖 NUCLEO-G474RE baseline CubeMX/CMake 瀹搞儳鈻奸敍?026-05-11 閻劍鍩涢幓鎰返 VOFA+ 閹搭亜娴橀敍宀冪槈閺勫骸缍嬮崜宥呮祼娴犺泛鍑℃稉瀣祰鏉╂劘顢戦獮鍫曗偓姘崇箖 COM5 / ST-LINK VCP 鏉堟挸鍤悩鑸碘偓浣规簚閺冦儱绻旈敍瀹峬ode` 娑?`mode_name` 閼宠棄鎮撳銉︽▔缁€?`IDLE`閵嗕梗ARMED`閵嗕梗RUN_SIM`閵?026-05-12 Codex 闁俺绻?COM5 妤犲矁鐦夋禍?`PING`閵嗕梗MODE?`閵嗕梗ARM`閵嗕梗STOP` 閸滃苯顒熸稊鐘垫暏 `SET_RPM <rpm>` 閸涙垝鎶ら敍姘承掗弸鎰版晩鐠囶垬鈧浇瀵栭崶鎾晩鐠囶垬鈧胶濮搁幀浣瑰珕缂佹縿鈧竸RM 閸氬海娲伴弽鍥р偓鍏兼纯閺傝埇鈧讣TOP 濞撳懘娴傞崸鍥╊儊閸氬牐顫夐崚娆掋€冮妴鍌氭倱閺冦儻绱漃1 catch-up 娴溿倓绮崠鍛嚒鐞涖儵缍堥敍姝嶢RT 閸涙垝鎶ら崜顖欑稊閻劏銆冮妴涓廙A + IDLE 閹恒儲鏁瑰ù浣衡柤閸滃矂妯佸▓闈涱槻閻╂ê娼庡鎻掑弳娴犳挶鈧?026-05-13 鐎涳缚绡勯懓鍛缁斿鈧俺绻?STOP/DMA P0 鏉╀胶些濡偓閺屻儯鈧礁鎳℃禒銈呭娴ｆ粎鏁ら梼鍛邦嚢閸?DMA + IDLE 閸ョ偠鐨熸禍鏃€顒炲ù浣衡柤閿涘畭normalize_learning_loop.py` 娑撳骸宕熼崗鍐╃ゴ鐠囨洟鈧俺绻冮敍娑樻倱閺?P2 MCSDK 閺冪姴濮涢悳鍥暕濡偓閸椻€冲嚒瀵偓婵锝為崘娆欑礉瑜版挸澧犲鍙夋箒閺堫剚婧€瀹搞儱鍙块悧鍫熸拱/status 鐞涖劊鈧攻aseline `.ioc` 鐠囪娲栭妴涔竔n/config 閼藉顢嶉妴浣哥埗閻?ST PDF 閺堫剙婀撮梹婊冨剼閵嗕讣T 鐎规缍夋禍銈呭级閺嶆悂鐛欓崪?pin-function 閸愯尙鐛婃径鍕倞閿涙瓪PC5` 鐞氼偅甯撻梽銈勮礋 nFAULT 閼藉顢嶉懘姘剧礉`PB12/TIM1_BKIN` 閹存劒璐熻ぐ鎾冲 nFAULT 閸婃瑩鈧绱漙PA2/PA3` 娑撳秴鍟€娴ｆ粈璐?FOC UART 姒涙顓婚柅澶嬪閿涘畭PB3` Hall B 闂団偓鐟曚線鍣撮弨?闂呮梻顬?SWO閵?026-05-14 Codex 閸掓稑缂撴禍鍡欏缁斿娈?P2 閺冪姴濮涢悳鍥帳缂冾喛宕忓鍫㈡窗瑜?`apps/stm32_g474_foc/mcsdk_no_power_precheck/`閿涘矁顔囪ぐ鏇氱啊 MCSDK draft閵嗕礁鍟跨粣浣稿枀缁涙牕鎷板銉ュ徔閹恒垺绁撮敍娑欐拱閺?CubeMX 閸欘垱澧界悰宀冪熅瀵板嫮鈥樼拋銈勮礋 `F:\STMCubeMX\STM32CubeMX.exe` 楠炶泛鍑￠崥顖氬З閸?`javaw.exe` 鏉╂稓鈻奸妴鍌炴閸氬海鏁ら幋宄扮暚閹?NUCLEO-G474RE Board Selector 閹靛濡搁幍瀣杽閹垮秴鑻熸穱婵嗙摠 CubeMX `.ioc` 閼藉顢?`apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`閿涘矁顕伴崶鐐碘€樼拋?`PA13/PA14` 娑?SWD閵嗕梗PA2/PA3` 娑?VCP閵嗕梗PB3` 娑?SWO閵嗕梗PB12` 娑?`TIM1_BKIN`閵嗕梗PB14` 娑?`TIM1_CH2N`閵嗗倷绮ㄦ惔鎾冲敶娴犲秵鐥呴張澶屾埂鐎?`.stmcx`閿涘奔绡冨▽鈩冩箒閻欘剛鐝?Motor Control Workbench 閸欘垱澧界悰宀冪熅瀵板嫨鈧倽绻栨禍娑楃矝娑撳秳鍞悰?MCSDK MotorControl 瀹搞儳鈻煎鑼晸閹存劖鍨ㄦ禒璁崇秿绾兛娆?閻㈠灚婧€鐞涘奔璐熷鏌ョ崣鐠囦降鈧倻鏁ら幋椋庘€樼拋銈囧閸旂喓宸奸弶鍨彠闁款喖娅掓禒韬测偓浣烘暩濠ф劘寤洪妴浣风箽閹躲倕顦婚崶鏉戞嫲闂冨牆鈧偐鍤庣槐銏犲嚒鐠佹澘缍嶉敍姹P32 瀹搞儳鈻奸妴涓矯B/Gerber閵嗕焦顒滃?BOM 閺傚洣娆㈤崪灞藉閻?閻㈠灚婧€鐎圭偞绁撮弮銉ョ箶鏉╂ɑ鐥呴張澶婄磻婵鐭囧ǎ鈧妴?
瑜版挸澧犳禒鎾崇氨閻ㄥ嫪瀵岀憰浣风稊閻劍妲搁敍姘祼鐎规岸銆嶉惄顔荤皑鐎圭偞绨妴浣割劅娑旂姾鐭剧痪瑁も偓浣哥暔閸忋劎瀛╃痪瑁も偓浣界カ閺傛瑧鍌ㄥ鏇樷偓浣瑰复閸欙絽顨栫痪锕€鎷伴崥搴ｇ敾娴溿倓绮悧鈺冩窗瑜版洏鈧?

## 瑜版挸澧犳い鍦窗鐎规矮缍?

- 妞ゅ湱娲伴崥宥囆為敍姘唨娴?STM32G474 閻ㄥ嫯绔熺紓妯肩秹閸忓啿鐎烽弮鐘冲妳 FOC 妞瑰崬濮╃化鑽ょ埠閵?
- 娑撹崵鍤庨弸鑸电€敍姝婽M32G474 + STDRIVE101 + 娑撳娴?BLDC + Hall 娣囨繂绨?+ SMO 閺冪姵鍔呴崘鎻掑煛 + ESP32-C3 鏉堝湱绱純鎴濆彠閵?
- 瑜版挸澧犲銉ュ徔闁炬儳褰涘鍕剁窗VS Code + STM32CubeIDE 閹绘帊娆?+ STM32CubeMX + MCSDK閿涙稐绗夋担璺ㄦ暏閻欘剛鐝?STM32CubeIDE 娴ｆ粈璐熸稉?IDE閵?
- 姒涙顓婚張宥呭鐎电钖勯敍娆?閸氬苯顒熼敍宀€鐣诲▔?娑撶粯甯堕弬鐟版倻閵?
- 瀹搞儳鈻奸崢鐔峰灟閿涙艾鍘涚€瑰鍙忔潪顒冩崳閺夈儻绱濋崘宥呬粵閺冪姵鍔呴妴浣风喘閸栨牕鎷扮粵鏃囦含娴滎喚鍋ｉ妴?
- ChatGPT + Codex 閸欏苯绗€閸掕泛浼愭担婊勭ウ瀹告彃娴愰崠鏍电窗ChatGPT 鐠愮喕鐭楅弫娆忣劅閵嗕椒鎹㈤崝鈥冲瘶閸滃苯顦查惄姗堢幢Codex 鐠愮喕鐭楀銉р柤閹笛嗩攽閵嗕浇鐦夐幑顔款唶瑜版洖鎷版禒鎾崇氨閺囧瓨鏌婇妴?

## 瀹告彃鐣幋鎰板帳缂?

- 閸斺晜澧滈煬顐″敜娑撳酣銆嶉惄顔款潐閸掓瑱绱癭AGENTS.md`閵嗕梗materials/assistant_profile.md`閵?
- Codex 娑撴挸鐫?Skill閿涙瓪stm32g474-foc-assistant`閿涘苯鍑＄€瑰顥婇崚鐗堟拱閺?Codex skills 閻╊喖缍嶉敍灞借嫙闁俺绻?`quick_validate.py` 鐎规ɑ鏌熼弽锟犵崣閵?
- 鏉堝懎濮?Skills閿涙瓪jupyter-notebook`閵嗕梗screenshot`閿涘苯鍑＄€瑰顥婇崚鐗堟拱閺?Codex skills 閻╊喖缍嶉敍灞借嫙闁俺绻?`quick_validate.py` 鐎规ɑ鏌熼弽锟犵崣閵?
- 閺堚偓妤傛ü绱崗鍫㈤獓娴滃鐤勫┃鎰剁窗`docs/00_project_truth/project_context.md`閵?
- 閼辨梻缍夐弽鍛婄叀娑撳孩娼靛┃鎰喘閸忓牏楠囬敍姝歞ocs/00_project_truth/internet_verification_rules.md`閵?
- 閺堫剙婀寸挧鍕灐缁便垹绱╅敍姝歮aterials/source_manifest.json`閵嗕梗docs/file_map.md`閵?
- ST 鐎规ɑ鏌熺挧鍕灐缁便垹绱╅敍姝歳eferences/st_manuals_index.md`閿涙稑鐖堕悽?ST PDF 瀹告煡鏆呴崓蹇撳煂 `materials/raw/st_manuals/`閿涘苯瀵橀幏?STDRIVE101 datasheet閿涙波ash 娑撳骸鐣奸弬?URL 鐠佹澘缍嶉崷?`materials/raw/st_manuals/manifest.json`閵?
- 閺堫剙婀村Λ鈧槐銏㈠偍瀵洩绱癭vector_store/`閵?
- Windows 瀹搞儱鍙块柧鎾呯窗CubeMX 閻㈢喐鍨氬銉р柤瀹告彃鐣幋鎰剁幢STM32CubeIDE for VS Code 閹碘晛鐫嶉張顑跨秼瀹告彃鐣ㄧ憗鍜冪幢閹碘晛鐫嶉幍妯碱吀閻?CMake/Ninja/GNU Arm GCC bundle 瀹告彃褰查悽銊ょ艾閺嬪嫬缂撻妴鍌氱秼閸撳秴鍑℃宀冪槈缁崵绮?PATH 娑?`cmake` 閸欘垳鏁ら敍瀹峮inja`閵嗕梗arm-none-eabi-gcc` 閺堫亜濮為崗?PATH閿涙稖绻栭弰?bundle 閹垫顓稿銉ュ徔闁惧彞绗呴惃鍕劀鐢摜濮搁幀浣碘偓鍌滃Ц閹浇顔囪ぐ鏇☆潌 `workflow/windows_toolchain_status.md`閵?
- 閻劍鍩涚涵顔款吇閻楀牏鈥栨禒璺烘珤娴犳湹绗岄梼鍫濃偓鑲╁殠缁鳖澁绱癭hardware/bom/2026-05-09_user_provided_power_stage_parts.md`閿涘牏鏁ら幋鐤嚛閺勫簼绗夐懗鎴掔箽鐠囦礁鍙忛柈銊︻劀绾噯绱濈亸姘弓閸?Datasheet/鎼存挸鐡?PCB/鐎圭偞绁存径宥嗙壋閿涘鈧?
- 閸樼喓鎮婇崶鐐焻閸ユ拝绱癭hardware/schematic/2026-05-09_power_board_schematic_screenshot.jpg`閿涘本鍩呴崶鎯у帗閺佺増宓侀敍姝歨ardware/schematic/2026-05-09_power_board_schematic_screenshot.md`閵?
- 闂冭埖顔岄幒銊ㄧ箻闂傛悂妫敍姝歸orkflow/phase_gate_checklist.md`閵?
- 妫ｆ牗顐肩挧鍕灐鐎电厧鍙嗙憴鍕灟閿涙瓪workflow/intake_checklist.md`閵?
- MacBook Codex 閸欏本婧€闁板秶鐤嗛崗銉ュ經閿涙瓪workflow/macbook_codex_replica.md`閵嗕梗tools/create_mac_codex_setup_bundle.ps1`閵嗕梗tools/bootstrap_mac_codex.sh`閵?
- GitHub 閸欏本婧€閸氬本顒炴潻婊咁伂閿涙瓪origin` -> `https://github.com/pinganyan0-eng/foc_learning_repo`閿涘牏顫嗛張澶夌波鎼存搫绱氶妴?
- STM32 baseline 瀹搞儳鈻奸敍姝歛pps/stm32_g474_foc/nucleo_g474re_baseline/`閿涘瓔ubeMX/CMake 閻㈢喐鍨氶幋鎰閿涘瓕ebug 閺嬪嫬缂撻柅姘崇箖楠炲墎鏁撻幋?`build/Debug/nucleo_g474re_baseline.elf`閵嗗倸缍嬮崜宥呮祼娴犺泛鍑￠崷?NUCLEO-G474RE 娑撳﹪鈧俺绻?COM5 / ST-LINK VCP 鏉堟挸鍤悩鑸碘偓浣规簚閺冦儱绻旈敍娑滅槈閹诡喛顫?`experiments/2026-05-09_nucleo_baseline/logs/2026-05-11_vofa_mode_name_log.md`閵?026-05-12 瀹歌尪鎷烽崝鐘辫閸欙絽鎳℃禒銈夌崣鐠囦礁鎷扮€涳缚绡勯悽?`SET_RPM` 妤犲矁鐦夐敍娑滅槈閹诡喛顫?`experiments/2026-05-09_nucleo_baseline/logs/2026-05-12_com5_set_rpm_validation.md`閵?
- ESP32 瀹搞儳鈻奸崡鐘辩秴閻╊喖缍嶉敍姝歛pps/esp32_c3_gateway/`閵?
- STM32 娑?ESP32 閸楀繗顔呮總鎴犲閿涙瓪interfaces/`閵?
- 鐎圭偤鐛欑拋鏉跨秿娑撳海鐡熸潏鈺€姘︽禒妯煎⒖閻╊喖缍嶉敍姝歟xperiments/`閵嗕梗deliverables/`閵?
- NUCLEO 閸╄櫣顢呭銉р柤鐎圭偤鐛欑拋鏉跨秿閿涙瓪experiments/2026-05-09_nucleo_baseline/`閵?
- 鐎涳缚绡勯梻顓犲箚缂佸瓨濮㈤懘姘拱閿涙瓪tools/normalize_learning_loop.py`閵嗕梗tools/start_learning_session.*`閵嗕梗tools/end_learning_session.*`閵?
- 妞ゅ湱娲伴懛顏勫З閸栨牕顨栫痪锔肩窗`workflow/automation_playbook.md`閿涙稑缍嬮崜?Codex 閼奉亜濮╅崠鏍у瘶閹奉剚鐦￠弮銉ヮ劅娑旂姾顫嬫０鎴﹀仏娴犺翰鈧焦鐦￠弮銉┿€嶉惄顔跨箻閸栨牕璐板Λ鈧柇顔绘閸滃本鐦￠崨銊┿€嶉惄顔碱槻閻╂﹢鍋栨禒璁圭礉閸у洨绮︾€规岸銆嶉惄顔界壌閻╊喖缍嶆潻鎰攽閵?
- 閸欏苯绗€閸掓湹鎹㈤崝鈥冲弳閸欙綇绱癭workflow/ACTIVE_TASK.md`閵嗕梗workflow/task_packet_template.md`閵嗕梗workflow/session_close_checklist.md`閵?
- 閸欏苯绗€閸掕泛顓哥拋鈥茬瑢閹垹顦查弬鍥︽閿涙瓪workflow/task_state_machine.md`閵嗕梗workflow/definition_of_done.md`閵嗕梗workflow/evidence_register.md`閵嗕梗workflow/risk_gate_matrix.md`閵嗕梗workflow/prompt_recipes.md`閵?
- 閸欏苯绗€閸掕埖鏆€鐎涳箑顨栫痪锔肩窗`workflow/teaching_contract.md`閿涘矁顫夌€?ChatGPT/Codex 閺佹瑥顒熼弮鍓佹畱閺傛澘鎮曠拠宥埿掗柌濞库偓浣峰敩閻浇顔夌憴锝夈€庢惔蹇嬧偓浣筋嚦閸氬骸顒熸稊鐘侯唶瑜版洖鎷?GitHub PR 閸愭瑥鍙嗙憴鍕灟閵?
- B 缁犳纭堕崥灞筋劅閺佹瑥顒熸稉搴濇唉娴犳ɑ鈧槒顓搁崚鎺炵窗`workflow/algo_b_teaching_delivery_plan.md`閿涘本濡告稉銈勫敜 8 閸?56 婢?HTML 鐎涳缚绡勭拋鈥冲灊鏉烆剚鍨氳ぐ鎾冲閻喎鐤勯梼鑸殿唽閸欘垱澧界悰宀€娈戦弫娆忣劅閼哄倸顨旈妴浣剿夋潻娑樺閺堝搫鍩楅妴浣圭槨鐠?濮ｅ繐鎳嗘稉濠佹唉閻椻晛鎷扮€瑰鍙忛梻鎼佹，鐟欏嫬鍨妴?
- 瑜版挸澧犵€涳缚绡勯幍褑顢戠仦鍌︾窗`learning/NEXT_LESSON.md`閵嗕梗learning/MASTERY_MAP.md`閵嗕梗workflow/current_learning_sprint.md`閿涘本濡?P1 娑撳绔寸拠淇扁偓浣瑰笁閹宦ょ槈閹诡喓鈧礁顦叉稊鐘辩喘閸忓牏楠囬崪?sprint 娴溿倓绮悧鈺€绮犻梹鑳吀閸掓帡鍣烽幎鑺ュ灇閻厼鍙嗛崣锝冣偓?
- P1 catch-up 娴溿倓绮崠鍜冪窗`deliverables/2026-05-12_p1_catchup_pack.md`閿涘苯鑻熷鍙夊Ω UART 閸涙垝鎶ら崜顖欑稊閻劏銆冮崘娆忓弳 `docs/05_test_and_logs/week1_nucleo_baseline.md`閵嗕笍MA + IDLE 閹恒儲鏁瑰ù浣衡柤閸愭瑥鍙?`docs/04_iot_gateway/uart_dma_idle.md`閵?
- P2 MCSDK 閺冪姴濮涢悳鍥暕濡偓閸椔ゅ磸濡楀牞绱癭deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`閿涘苯缍嬮崜宥堫唶瑜版洘婀伴張鍝勪紣閸忛澧楅張?status閵嗕攻aseline `.ioc` 鐠囪娲栭妴涓瓹SDK pin/config 閼藉顢嶉妴涓糡 鐎规ɑ鏌熼弶銉︾爱娴溿倕寮堕弽鎼佺崣閵嗕垢in-function 閸愯尙鐛婃径鍕倞閵嗕够hell GUI 鐠囦焦宓侀幒銏＄ゴ閸滃本婀弶?Motor Profiler 閸嬫粍顒?閸ョ偤鈧偓鐠佲€冲灊閿?026-05-14 瀹歌尪鎷烽崝鐘靛缁斿妫ら崝鐔哄芳閼藉顢嶉惄顔肩秿 `apps/stm32_g474_foc/mcsdk_no_power_precheck/`閵嗕竼ubeMX 閸氼垰濮╃捄顖氱窞閵嗕笩UI 闂冭顢ｇ拋鏉跨秿閵嗕腐UCLEO-G474RE CubeMX `.ioc` 閼藉顢?`apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`閿涘奔浜掗崣?STDRIVE101 娣囨繃濮㈢捄顖氱窞鐎光剝鐓?`apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`閿?026-05-18 瀹稿弶鏌婃晶?Packet A 閹规洝骞忔禒璇插閸?`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_task_2026-05-18.md`閿涘苯褰ч崶鍝勭暰閺堫亝娼?`.stwb6`閵嗕焦鍩呴崶淇扁偓浣哥摟濞堢敻鐛欓弨璺烘嫲閸嬫粍顒涢弶鈥叉閵嗗倽绻栨禍娑樺涧閺勵垱妫ら崝鐔哄芳闁板秶鐤嗛妴浣割吀閺屻儱鎷版禒璇插濞岃崵鎮婄拠浣瑰祦閿涘奔绗夐弰?`.stmcx`閵嗕府CSDK MotorControl 瀹搞儳鈻奸妴涓畂tor Profiler閵嗕笭all 閹存牕濮涢悳鍥╅獓妤犲矁鐦夐妴?- Obsidian 缁楁棁顔囧銉ょ稊閸栫尨绱版禒鎾崇氨閺嶅湱娲拌ぐ鏇炲嚒闁板秶鐤?`.obsidian/`閿涘奔閲滄禍铏圭應鐠佹澘鎷伴惇瀣緲閺€鎯ф躬 `notes/`閿涘苯鍙嗛崣锝勮礋 `notes/00_home/foc_dashboard.md`閵?

## 瑜版挸澧犻張顏勭磻婵?

- NUCLEO-G474RE baseline CubeMX/CMake 瀹搞儳鈻煎鍙夋杹閸忋儻绱盤2 瀹稿弶鏌婃晶?NUCLEO-G474RE CubeMX `.ioc` 閼藉顢嶉獮鏈电箽鐎?`PB12/TIM1_BKIN`閵嗕梗PB14/TIM1_CH2N`閵嗕梗PA2/PA3` VCP 閸?`PB3` SWO閵嗕净CSDK 閻㈠灚婧€閹貉冨煑瀹搞儳鈻肩亸姘弓閺€鎯у弳閿涙稖绻栨禍娑樷偓娆撯偓澶婄毣閺堫亞绮℃潻?MCSDK/Workbench `.stmcx` 閸?CN8/EDA/netlist 閸忓崬鎮撶涵顔款吇閿涘苯鐨婚張顏嗘晸閹存劗婀＄€?`.stmcx` 閹?MotorControl 闁板秶鐤嗛幋顏勬禈鐠囦焦宓侀妴?- 閻喎鐤?ESP32-C3 缂冩垵鍙у銉р柤鐏忔碍婀弨鎯у弳閵?
- 閸樼喓鎮婇崶鐐焻閸ユ儳鍑￠弨鎯у弳閿涙宝DA 濠ф劖鏋冩禒韬测偓浣割嚤閸?PDF閵嗕赋CB閵嗕笩erber/閸ф劖鐖ｉ弬鍥︽閵嗕礁娅掓禒?Datasheet 閸栧懎鎷板锝呯础 BOM 鐞涖劌鐨婚張顏呮杹閸忋儯鈧?
- 瀹稿弶婀侀惃鍕暏閹撮鈥樼拋銈囧绾兛娆㈠〒鍛礋娴犲秵妲稿鍛槻閺嶅摜鍤庣槐顫礉娑撳秳鍞悰銊р€栨禒鎯邦啎鐠佲€冲嚒鐎光剝鐓￠柅姘崇箖閵?
- NUCLEO baseline 娑撴彃褰涢弮銉ョ箶閸滃苯顒熸稊鐘垫暏 `SET_RPM` 閸涙垝鎶ゆ宀冪槈瀹歌弓楠囬悽鐕傜幢缁€鐑樺皾閸ｃ劍灏濊ぐ顫偓涓畂tor Profiler 缂佹挻鐏夐妴涓燼ll 闂傤厾骞嗙拋鏉跨秿鐏忔碍婀禍褏鏁撻妴?

鏉╂瑤绨烘稉宥嗘Ц闁板秶鐤嗙紓鍝勩亼閿涘矁鈧本妲告い鍦窗鐏忔碍婀潻娑樺弳鐎电懓绨查梼鑸殿唽閵?

## 娑撳绔村銉︽付鐏忓繐濮╂担?

1. 婵″倹鐏夌憰浣哥磻婵顒熸稊?鐎圭偞鎼烽敍姘崇箻閸?NUCLEO-G474RE 閸╄櫣顢呭銉р柤閿涘苯鍘涢崑姘卞仯閻忣垬鈧椒瑕嗛崣锝嗗ⅵ閸楄埇鈧礁鐣鹃弮璺烘珤閸?UART DMA + IDLE閿涙稐绗夐幒?24V閵嗕椒绗夐幒銉ュ閻滃洦婢橀妴浣风瑝閹恒儳鏁搁張鎭掆偓?
2. 婵″倹鐏夌憰浣瑰腹鏉╂盯妯佸▓纰夌窗閸忓牆顕悡?`workflow/phase_gate_checklist.md`閿涘瞼鈥樼拋銈堢箻閸忋儲娼禒韬测偓浣烽獓閸戦缚鐦夐幑顔兼嫲缁備焦顒涢崝銊ょ稊閵?
3. 婵″倹鐏夌憰浣割嚤閸忋儲鏌婄挧鍕灐閿涙艾鍘涢幐?`workflow/intake_checklist.md` 閸掑棛琚崨钘夋倳閿涘苯鍟€閺囧瓨鏌婄€电懓绨茬槐銏犵穿閵?
4. 婵″倹鐏夌憰浣烘埛缂?P2 MCSDK 閺冪姴濮涢悳鍥暕濡偓閿涙艾鍘涚拠?`deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`閵嗕梗apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_task_2026-05-18.md`閵嗕梗apps/stm32_g474_foc/mcsdk_no_power_precheck/config_draft.md`閵嗕梗apps/stm32_g474_foc/mcsdk_no_power_precheck/hands_on_evidence_2026-05-14.md` 閸?`apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`閿涙稑缍嬮崜宥呭嚒閺?NUCLEO-G474RE CubeMX `.ioc` 閼藉顢嶉妴涓砤cket A 閹规洝骞忔禒璇插閸栧懎鎷?STDRIVE101 娣囨繃濮㈢捄顖氱窞缂傞缚鐦夐惌鈺呮█閿涘奔绲炬禒宥堫洣鐞涖儳婀＄€?MCSDK/Workbench `.stwb6` 閹?MotorControl 闁板秶鐤嗛幋顏勬禈閵嗕竼N8/EDA/netlist 鐠ф壆鍤庣拠浣瑰祦閸滃苯缍嬮崜宥囧 STDRIVE101 娣囨繃濮㈢捄顖氱窞濠ф劘鐦夐幑顕嗙幢娴犲秳绗夐幒?24V閵嗕椒绗夐幒銉ュ閻滃洦婢橀妴浣风瑝閹恒儳鏁搁張鎭掆偓浣风瑝鏉╂劘顢?Motor Profiler閵?5. 婵″倹鐏夌憰浣烘埛缂?STM32 baseline閿涙艾婀鏌ョ崣鐠?COM5 娑撴彃褰涢崨鎴掓姢鐠侯垰绶為惃鍕唨绾偓娑撳绱濈悰銉ㄥ€濋惇?LD2 闂傤亞鍎婄拠浣瑰祦閿涘本鍨ㄩ悽?Codex 鏉╂稖顢戦惇鐔风杽 UART DMA + IDLE callback 閻ㄥ嫭妫ら崝鐔哄芳鐎圭偟骞?閺嬪嫬缂撴宀冪槈閵?
6. 婵″倹鐏夌憰浣哥磻婵鈥栨禒璺侯吀閺屻儻绱版禒?`hardware/bom/2026-05-09_user_provided_power_stage_parts.md` 娑撳搫娅掓禒鍓佸殠缁鳖澁绱濈紒褏鐢荤悰銉ュ斧閻炲棗娴?PDF閵嗕赋CB 閹搭亜娴橀妴浣诡劀瀵?BOM閵嗕笍atasheet 閸滃苯鍙ч柨顔荤箽閹躲倝妲囬崐鑹邦吀缁犳ぜ鈧?

## 鐎瑰鍙忕痪銏㈠殠

- 娑撳秶娲块幒?24V 婢堆呮暩濞翠椒绗傞悽鐐光偓?
- 妫ｆ牗顐兼稉濠勬暩娴ｈ法鏁ら梽鎰ウ閻㈠灚绨敍宀勭帛鐠併倓绮?0.2A 缁狙冨焼瀵偓婵鈧?
- 閹恒儳鏁搁張鍝勫閸忓牆浠涚粚楦挎祰 PWM閵嗕笩ate 濞夈垹鑸伴妴涔禙AULT閵嗕箓S/REG12/VREG 閸滃矂鍣伴弽鐑芥懠鐠侯垱顥呴弻銉ｂ偓?
- JEOC/FOC ISR 閸愬懍绗夐弨?`printf`閵嗕梗HAL_Delay`閵嗕福SON 鐟欙絾鐎介妴涔別bSocket閵嗕礁濮╅幀浣稿敶鐎涙ɑ鍨ㄩ梹鑳偓妤佹闁槒绶妴?
- V9 娑撳骸鐣奸弬?Datasheet 閸愯尙鐛婇弮璁圭礉閸忓牏娴夋穱鈥崇暭閺傜绁弬娆忚嫙閹绘劗銇氭搴ㄦ珦閿涙矂9 娑撳骸鐤勫ù瀣暱缁愪焦妞傞敍灞藉帥濡偓閺屻儲绁寸拠鏇熸蒋娴犺翰鈧?

## 鐢摜鏁ら崗銉ュ經

- 妞ゅ湱娲扮憴鍕灟閿涙瓪AGENTS.md`
- Obsidian 閹粯甯堕崣甯窗`notes/00_home/foc_dashboard.md`
- 鐎涳缚绡勯崗銉ュ經閿涙瓪materials/START_HERE.md`
- 妞ゅ湱娲版禍瀣杽閿涙瓪docs/00_project_truth/project_context.md`
- 闂冭埖顔岄梻鎼佹，閿涙瓪workflow/phase_gate_checklist.md`
- 鐠у嫭鏋＄€电厧鍙嗛敍姝歸orkflow/intake_checklist.md`
- 瑜版挸澧犳禒璇插閸栧拑绱癭workflow/ACTIVE_TASK.md`
- 娴犺濮熼崠鍛侀弶鍖＄窗`workflow/task_packet_template.md`
- 閺€璺轰紣濡偓閺屻儻绱癭workflow/session_close_checklist.md`
- 娴犺濮熼悩鑸碘偓浣规簚閿涙瓪workflow/task_state_machine.md`
- 鐎瑰本鍨氱€规矮绠熼敍姝歸orkflow/definition_of_done.md`
- 鐠囦焦宓侀惂鏄忣唶閿涙瓪workflow/evidence_register.md`
- 妞嬪酣娅撻惌鈺呮█閿涙瓪workflow/risk_gate_matrix.md`
- 閺佹瑥顒熸稉搴濇唉娴犳ɑ鈧槒顓搁崚鎺炵窗`workflow/algo_b_teaching_delivery_plan.md`
- 娑撳绔寸拠鐐⒔鐞涘苯宕遍敍姝歭earning/NEXT_LESSON.md`
- 閹哄本褰欑拠浣瑰祦閸︽澘娴橀敍姝歭earning/MASTERY_MAP.md`
- 瑜版挸澧犵€涳缚绡?sprint閿涙瓪workflow/current_learning_sprint.md`
- 閺佹瑥顒熸總鎴犲閿涙瓪workflow/teaching_contract.md`
- 閹绘劗銇氱拠宥喣侀弶鍖＄窗`workflow/prompt_recipes.md`
- 閺堫剙婀村Λ鈧槐顫窗`python tools/ask_local.py "娴ｇ姷娈戦梻顕€顣?`
- 瀵偓瀹搞儱鍙嗛崣锝忕窗`powershell -ExecutionPolicy Bypass -File .\tools\start_learning_session.ps1`
- 閺€璺轰紣閸忋儱褰涢敍姝歱owershell -ExecutionPolicy Bypass -File .\tools\end_learning_session.ps1 -Topic "娑撳顣? -Summary "娴犲﹤銇夐崑姘啊娴犫偓娑?`
- 鐎涳缚绡勯梼鐔峰灙閺佸鎮婇敍姝歱ython tools/normalize_learning_loop.py`
- 闁插秴缂撳Λ鈧槐銏㈠偍瀵洩绱癭python tools/build_vector_store.py`
- 閸ョ偛缍婂ù瀣槸閿涙瓪python -m unittest discover -s tests`
