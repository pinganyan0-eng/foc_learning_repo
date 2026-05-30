# MCSDK No-Power Precheck

This directory is the P2 no-power MCSDK practice area.

It is not the firmware working tree for manual edits. It holds no-power
planning, source-review, and build-only evidence that must be checked before
any Motor Profiler step, power-board connection, motor connection, or PWM Gate
output.

## Current Status

- Created: 2026-05-14.
- Scope: configuration planning only.
- Existing evidence in this directory: draft configuration, tool probe notes,
  a CubeMX Home screenshot, a CubeMX `.ioc` pinout screenshot, pin/config safety
  review, GUI capture result, a current P2 璇佹嵁鍖? source packet intake rules,
  a source packet request pack, a source packet review template, and a user
  action queue, STM32-side signal/build gates, a P2 readiness snapshot, a
  2026-05-16 custom Workbench capture package, 2026-05-17 vendor motor /
  hardware teammate pin-table source clues, a 2026-05-18 Packet A capture
  task package, a 2026-05-19 Workbench capture attempt stopped on the
  self-made STDRIVE101 power-stage context blocker, 2026-05-19 `.epro` and
  Gerber PCB2 board-side source clues, a 2026-05-19 hardware supplement
  handoff, a minimal hardware-teammate request, and a local Workbench
  Board Designer / Board Manager asset probe, plus a 2026-05-19 current PCB2
  mapping / pin-1 / protection source review, a current PCB2 Hall/PWM
  no-power strategy review, a current PCB2 Packet A / firmware feasibility
  review, a software Hall adapter design review, and a Packet A Board
  Designer / Board Manager path review, plus a Packet A Board Designer /
  Manager GUI-only checklist, a `MY_FOC` generated-project source review, a
  `MY_FOC` manual FOC edit rollback record, and a 2026-05-20 Packet C
  STDRIVE101 protection detail review, plus a 2026-05-22 DMM continuity /
  short-check request before software Hall adapter implementation, and a
  2026-05-22 software Hall no-power algorithm prep artifact, plus a
  2026-05-22 software Hall state-machine exercise card, plus a 2026-05-27
  software Hall adapter pseudocode draft, plus a 2026-05-27 software Hall
  adapter processing-order teaching card, plus a 2026-05-27 host-side software
  Hall reference model review, plus 2026-05-27 software Hall golden vectors
  and replay test, plus a 2026-05-27 read-only MCSDK integration probe for
  the software Hall route, plus a 2026-05-27 firmware-entry checklist that
  freezes the missing conditions before any future adapter code, plus a
  2026-05-27 GPIO/EXTI boundary review draft for `PA0/PA1/PB4`, plus a
  2026-05-27 timestamp-source review draft that excludes `TIM1`, keeps current
  `TIM2` as a generated MCSDK Hall clue only, limits `HAL_GetTick()` to coarse
  logs, and leaves an isolated free-running timer as a future review target,
  plus a 2026-05-27 no-power Debug build-only result record for
  `QIANSAI_G474_STDRIVE101_FOC_P2`, plus a 2026-05-27 low-frequency
  debug-output route review draft that defines
  snapshot fields and blocks ISR printing / UART transmit / JSON / ESP32 /
  SWO / every-edge streaming, plus a 2026-05-27 MCSDK firmware-integration boundary review draft that blocks direct writes to `HALL_M1`, speed loop, PID, JEOC / FOC ISR, or TIM1 PWM, plus a 2026-05-28 Chinese-first software Hall firmware-entry plan that defines the future debug-only adapter layers, state-machine order, ISR limits, debug fields, and MCSDK hard stops without opening firmware implementation.
- Missing evidence: accepted final Workbench selected-field screenshots,
  Packet A / firmware feasibility proof for the current PCB2
  `HIN/LIN -> PA15/PB3/PB10/PA8/PA9/PA10` route and `PA0/PA1/PB4` software
  Hall route beyond no-power design review, a corrected FOC Workbench
  configuration for `MY_FOC` or a replacement project, filled no-power DMM
  continuity / short-check results, software Hall firmware implementation, and
  all powered hardware evidence.

## Safety Boundary

Forbidden in this directory and this P2 stage:

- no 24V;
- no power-board connection;
- no motor connection;
- no PWM Gate output;
- no Motor Profiler run;
- no Hall closed-loop validation;
- no SMO / sensorless claim;
- no claim that `SET_RPM` controls real motor speed.

## Files

- `config_draft.md`: no-power MCSDK configuration draft and conflict policy.
- `pin_config_review_2026-05-14.md`: next-ring pin/config safety review and
  hard-stop checklist before trusting any generated MCSDK configuration.
- `evidence_packet_2026-05-14.md`: 褰撳墠璇佹嵁绛夌骇銆佷粨搴撳簱瀛樺拰淇′换浠讳綍鐢熸垚
  MCSDK 閰嶇疆鍓嶇殑闃诲椤广€?- `source_packet_intake_checklist_2026-05-14.md`: accepted / rejected source
  rules before any missing P2 evidence can be upgraded.
- `software_hall_firmware_entry_plan_2026-05-28.md`: Chinese-first no-power
  firmware-entry plan for the future `PA0/PA1/PB4` debug-only software Hall
  adapter. Decision:
  `Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.
- `source_packet_request_pack_2026-05-14.md`: concrete request pack for the
  next `.stmcx`, MotorControl screenshot, CN8/EDA/netlist, and STDRIVE101
  protection-path handoff.
- `source_packet_review_template_2026-05-14.md`: repeatable review form for
  accepting, downgrading to clue-only, or rejecting Packet A/B/C and PB3/SWO
  evidence before updating the evidence packet.
- `source_packet_review_2026-05-15_001_cn8_stdrive101_schematic_candidate.md`:
  review of the user-provided CN8 / STDRIVE101 schematic screenshot candidate;
  current decision is `Partial clue`.
- `packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`: preserved
  local MCSDK 6 Workbench project candidate.
- `source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`: Packet A review
  of the local `.stwb6`; current decision is `Partial clue`, not build-only
  clearance.
- `packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`: prepared capture
  package for a new project-specific Workbench configuration targeting
  `NUCLEO-G474RE` plus a Custom / Generic STDRIVE101 power stage. It contains a
  GUI guide, no-power motor measurement template, pin assignment table, and
  screenshot inbox. It does not yet contain an accepted `.stwb6`.
- `source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`:
  review of the 2026-05-16 capture package. Current decision is
  `Partial clue / Preparation only`; generated-project trust remains
  `Not allowed`.
- `mcu_pin_compatibility_check_2026-05-17.md`: local MCSDK asset comparison for
  `STM32G431RBTx` versus `STM32G474RETx`. It supports the hardware teammate's
  statement that the compared key rows are pin-function compatible, but it does
  not prove CN8 routing, `J_HALL` numbering, or `PB3` / SWO release.
- `source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`:
  review of the vendor `57BLF01` motor source and hardware teammate
  `STM32G431RB` pin table. Current decision is `Partial clue`; motor values are
  supplier clues, and board-route / Hall connector blockers remain.
- `source_packet_review_2026-05-18_001_motor_wiring_definition.md`: review of
  the user-provided 57BLF01 phase/Hall wire-color definition image. Current
  decision is `Partial clue`; wire colors are candidate clues only and do not
  prove physical harness inspection, Hall powering, phase/Hall alignment, or
  `J_HALL` numbering.
- `packet_a_capture_task_2026-05-18.md`: workflow-only task package for the
  future project-specific Workbench capture. It fixes the `.stwb6` path,
  required screenshots, stop conditions, and field acceptance matrix. It does
  not add a real `.stwb6`, screenshots, generated source, build evidence, or
  hardware validation.
- `source_packet_review_2026-05-19_001_packet_a_workbench_capture_attempt.md`:
  review of the no-power Workbench capture attempt. Current decision is
  `Partial clue / stopped`; Workbench 6.4.2 launches and
  `NUCLEO-G474RE` / `STM32G474RETx` control-board context is visible, but no
  accepted self-made STDRIVE101 power-stage context or selected-field
  screenshots were captured.
- `source_packet_review_2026-05-19_002_prodoc_p1_epro.md`: review of the
  user-confirmed EasyEDA Pro schematic source for the self-developed
  STDRIVE101 driver board. Current decision is `Partial clue / accepted
  schematic-source clue`; it improves board-side source visibility but does
  not prove PCB layout, NUCLEO `CN8`, STM32 endpoints, or readiness.
- `source_packet_review_2026-05-19_003_gerber_pcb2.md`: review of the
  hardware-teammate supplied Gerber PCB2 package. Current decision is
  `Partial clue / accepted board-side Gerber + flying-probe net clue`; it
  supports board-side pad/net clues but not NUCLEO endpoint mapping,
  continuity, or readiness.
- `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md`:
  review of the user-provided current PCB2 mapping, pin-1 images, Hall
  relationship, PB3/SWO guidance, and STDRIVE101 protection-chain statement.
  Current decision is `Partial clue / accepted current PCB2 mapping source;
  Hall/PWM conflicts clarified`; `PC7/PB3/PB10` is an alternate suggestion,
  while current PCB2 Hall routing is `IA/IB/IC -> PA0/PA1/PB4`.
- `current_pcb2_hall_pwm_strategy_2026-05-19.md`: no-power strategy review
  for the current PCB2 PWM/Hall mismatch. Current decision is
  `No-power strategy review opened / no PCB change first`; old standard
  `TIM1` PWM and `PA15/PB3/PB10` Hall drafts are historical or alternate
  candidates only, and software Hall on `PA0/PA1/PB4` remains feasibility
  review only.
- `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md`: no-power Packet
  A / firmware feasibility review for the current no-PCB-change route. Current
  decision is `No-PCB-change route remains feasibility only / Packet A not
  accepted`; current PWM is not cleared as standard MCSDK `TIM1`
  complementary PWM selected-field evidence, and `PA0/PA1/PB4` is not cleared
  as same-timer hardware Hall.
- `software_hall_adapter_design_review_2026-05-19.md`: no-power design review
  for the current PCB2 software Hall path on `PA0/PA1/PB4`. Current decision is
  `Software Hall adapter remains no-power design review / Packet A not
  accepted`; it defines future GPIO/EXTI sampling, edge timestamping,
  valid-state filtering, minimal ISR responsibility, MCSDK integration
  boundaries, and `hardware-rework planning` fallback conditions without
  adding firmware, runtime APIs, generated source, build-only clearance, or
  Hall readiness.
- `dmm_continuity_short_check_request_2026-05-22.md`: no-power table template
  for the next real-world evidence before software Hall adapter implementation.
  It requests continuity for `IA->PA0`, `IB->PA1`, `IC->PB4`, `PB3->LIN1`,
  `P14->3V3`, `P15->GND`, `nFAULT->PB12`, plus rail, signal-to-rail, and
  Hall-line short checks. It is not a measurement result.
- `software_hall_no_power_algorithm_prep_2026-05-22.md`: algorithm-side
  no-power preparation for the current software Hall route. Current decision is
  `Algorithm-side no-power preparation / no firmware implementation / no Hall
  readiness`; it defines valid/illegal Hall states, transition rules, candidate
  sequences, debug observables, ISR limits, and MCSDK hard stops while the
  unpopulated-board DMM gate is deferred, not passed.
- `software_hall_state_machine_exercise_card_2026-05-22.md`: Chinese-first
  no-power exercise card for the algorithm role. Current decision is
  `User Hall state-machine exercise requested / no firmware implementation /
  no Hall readiness`; it asks five concept checks and a four-row Hall
  transition table before any pseudocode or firmware work.
- `software_hall_adapter_pseudocode_draft_2026-05-27.md`: Chinese-first
  no-power pseudocode draft for the future `PA0/PA1/PB4` software Hall
  adapter. Current decision is `Software Hall adapter pseudocode draft / no
  firmware implementation / no MCSDK Hall integration / no Hall readiness`;
  it defines function responsibilities, state fields, decision order, ISR
  limits, debug observables, MCSDK hard stops, and future code-entry
  conditions without adding firmware or hardware evidence.
- `software_hall_adapter_processing_order_card_2026-05-27.md`: Chinese-first
  no-power repair card for the future software Hall adapter processing order.
  Current decision is `Software Hall adapter processing-order teaching card /
  no firmware implementation / no MCSDK Hall integration / no Hall readiness`;
  it explains raw read, illegal-state check, first-valid handling, repeated
  state handling, bounce/timing check, adjacent direction check, and
  abnormal-jump count after the user could not restate the sequence.
- `software_hall_host_model_review_2026-05-27.md`: review of the host-side
  executable software Hall reference model in `src/software_hall_model.py` and
  `tests/test_software_hall_model.py`. Current decision is `Host-side software
  Hall reference model / no firmware implementation / no MCSDK Hall integration
  / no Hall readiness`; it proves only host-side algorithm behavior.
- `software_hall_golden_vectors_review_2026-05-27.md`: review of the
  host-side software Hall golden vectors in
  `tests/fixtures/software_hall_golden_vectors.json` and replay test
  `tests/test_software_hall_vectors.py`. Current decision is `Host-side
  software Hall golden vectors / no firmware implementation / no MCSDK Hall
  integration / no Hall readiness`; it proves only host-side no-power
  algorithm replay behavior.
- `software_hall_mcsdk_integration_probe_2026-05-27.md`: read-only probe of
  the 2026-05-21 generated-project clue files for speed/position feedback
  integration points. Current decision is `MCSDK Hall integration points
  identified as read-only clues / no firmware implementation / no MCSDK Hall
  integration / no Hall readiness`; it identifies standard TIM2 hardware Hall
  clues and keeps the current `PA0/PA1/PB4` software Hall route outside MCSDK
  Hall integration.
- `software_hall_firmware_entry_checklist_2026-05-27.md`: no-power entry
  checklist for any future `PA0/PA1/PB4` software Hall adapter firmware work.
  Current decision is `Software Hall firmware-entry checklist / no firmware
  implementation / no MCSDK Hall integration / no Hall readiness`; it requires
  populated-board DMM evidence, GPIO/EXTI boundary review, timestamp-source
  decision, debug route, and separate MCSDK firmware-integration review before
  any adapter code or powered claim. The build-only record now exists but does
  not open firmware implementation.
- `software_hall_gpio_exti_boundary_review_2026-05-27.md`: no-power
  GPIO/EXTI boundary draft for the future software Hall adapter. Current
  decision is `Software Hall GPIO/EXTI boundary review draft / no firmware
  implementation / no GPIO runtime proof / no Hall readiness`; it records
  `PA0/PA1/PB4` as software input candidates, `EXTI0/EXTI1/EXTI4` as
  event-capture candidates, minimal ISR duties, and the remaining pull-mode,
  timestamp, debug, build-only, DMM, and MCSDK integration blockers.
- `software_hall_timestamp_source_review_2026-05-27.md`: no-power timestamp
  source review for the future `PA0/PA1/PB4` software Hall adapter. Current
  decision is `Software Hall timestamp-source review draft / no firmware
  implementation / no timer configuration / no Hall readiness`; it records
  `TIM1` as unavailable, current `TIM2` as the generated MCSDK Hall clue path,
  `HAL_GetTick()` as coarse-only, and a future isolated free-running timer plus
  `unsigned delta` as review targets only.
- `software_hall_debug_output_route_review_2026-05-27.md`: no-power
  low-frequency debug-output route review for the future software Hall adapter.
  Current decision is `Software Hall low-frequency debug-output route review
  draft / no firmware implementation / no UART implementation / no Hall
  readiness`; it defines future snapshot fields and blocks ISR printing,
  JSON formatting, UART transmit, ESP32 / WebSocket, SWO, every-edge streaming,
  and direct MCSDK speed feedback.
- `software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md`:
  no-power MCSDK firmware-integration boundary review for the future software
  Hall adapter. Current decision is `Software Hall MCSDK firmware-integration
  boundary review draft / no firmware implementation / no MCSDK hook / no Hall
  readiness`; it records generated MCSDK clues such as `HALL_M1`,
  `SpeednTorqCtrlM1`, `PIDSpeedHandle_M1`, `pSTC`, `MCI_Handle_t`, `FOCVars`,
  `SPD_HALL_TIM_M1_IRQHandler`, `M1_SPEED_SENSOR=HALL_SENSOR`, and
  `M1_HALL_TIMER_SELECTION=HALL_TIM2` as clues or hard stops, not hooks.
- `software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md`:
  no-power MCSDK hook evidence request checklist for the future software Hall
  adapter. Current decision is `Software Hall MCSDK hook evidence request
  checklist / no firmware implementation / no MCSDK hook / no Hall readiness`;
  it requests exact generated or interface sources such as
  `hall_speed_pos_fdbk.c/.h`, `speed_torq_ctrl.c/.h`, `mc_tasks.c/.h`,
  `mc_tasks_foc.c`, `mc_interface.c/.h`, `mc_api.c/.h`, `mc_app_hooks.c/.h`,
  `mc_parameters.c/.h`, `motorcontrol.c/.h`, interrupt sources,
  current-feedback backend files, and ASPEP / register-interface files before
  any hook proposal.
- `source_packet_review_2026-05-27_001_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot.md`:
  no-power review of the full generated Workbench `Src/Inc` snapshot copied
  from `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`.
  Current decision is `Full generated Src/Inc snapshot archived / source
  interface evidence available for read-only review / no firmware
  implementation / no MCSDK hook / no Hall readiness`; the snapshot lives at
  `packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`
  and includes manifest/hash evidence for read-only interface review only.
- `software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md`:
  no-power MCSDK speed / position feedback interface review for the future
  software Hall route. Current decision is `Software Hall MCSDK speed/position
  feedback interface review / no firmware implementation / no MCSDK hook / no
  Hall readiness`; it traces `HALL_M1`, `HALL_CalcAvrgMecSpeedUnit`,
  `STC_GetSpeedSensor`, `SPD_GetAvrgMecSpeedUnit`, and `SPD_GetElAngle`, and
  records that a future hook needs a reviewed `SpeednPosFdbk`-compatible
  component rather than direct writes of `direction_candidate` or
  `speed_candidate`.
- `packet_a_board_designer_manager_path_review_2026-05-19.md`: no-power Packet
  A path review for the Workbench Board Designer / Board Manager path. Current
  decision is `Board Designer / Board Manager path exists as local
  documentation and tool clue / Packet A still blocked`; it records the local
  Workbench external-tool entries, local Board Designer / Board Manager
  executables, Board Designer manual custom-board workflow clues, and the
  boundary that built-in `EVALSTDRIVE101`, `STEVAL-LVLP01`, and
  `EVLDRIVE101-HPD` cannot replace evidence for the self-developed STDRIVE101
  board. It adds no generated-project trust, no build-only clearance, no
  custom board source, no `.stwb6`, and no powered readiness.
- `packet_a_board_designer_manager_gui_checklist_2026-05-19.md`: GUI-only
  checklist for the later user screenshot capture around Board Designer /
  Board Manager. Current decision is `GUI-only checklist prepared / Packet A
  still blocked`; it defines the screenshot save directory, required screenshots
  for custom/import/create board paths, Power/Control/Inverter board flows,
  Board Aggregation, Finalize/save prompt, Board Manager import/list path, and
  blocked states. It adds no generated-project trust, no custom board source,
  no `.stwb6`, and no powered readiness.
- `source_packet_review_2026-05-19_005_my_foc_generated_project.md`: review of
  the user-created `MY_FOC` Workbench generated project. Current decision is
  `Partial clue / generated project quarantined / Packet A not accepted`; it
  proves a real generated project exists, but the project is `SIX_STEP`, not
  FOC, and current sensing, fault/break, Hall/PWM route, and motor evidence are
  not accepted. User clarification that pins can be changed is recorded as a
  future editable route, not Packet A acceptance.
- `packet_a_sources/2026-05-19_my_foc_generated_project/`: selected no-power
  source/config/log files copied from the user-created `MY_FOC` Workbench
  project. The generated `Src/`, `Inc/`, `Drivers/`, and
  `MCSDK_v6.4.2-Full/` trees are intentionally not copied or trusted.
- `my_foc_foc_candidate_edit_2026-05-19.md`: records the Codex manual FOC edit
  attempt and rollback for
  `C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6`. Current decision is
  `Manual FOC source edit failed Workbench reload / rolled back / Packet A still not accepted`;
  the one-field edit from `"algorithm": "sixStep"` to `"algorithm": "FOC"`
  made Workbench unable to load the file, so Codex restored the external source
  from backup. The current external source is again six-step; the failed FOC
  candidate is negative evidence only.
- `packet_c_stdrive101_protection_detail_review_2026-05-20.md`: no-power
  Packet C detail review for `DT/MODE`, `nFAULT`, `REG12`, `CP`, `SCREF`,
  `VS/VM`, bootstrap, `STBY`, and VDS monitoring. Current decision is
  `Packet C detail narrowed / protection proof still partial clue / P3 still blocked`;
  it marks the old `V_DSth = 0.249V` / `I_trip ~= 55A` note as not accepted and
  keeps Packet C, generated-project trust, continuity, and powered readiness
  blocked.
- `hardware_supplement_handoff_2026-05-19.md`: current hardware-teammate
  handoff for the next accepted evidence. It asks for exact board revision,
  `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping, `CN3` / `J_HALL` pin-1
  orientation, Hall A/B/C mapping, PB3/SWO evidence, STDRIVE101 protection
  chain details, optional PCB source, and later no-power continuity records.
- `hardware_teammate_min_request_2026-05-19.md`: short first packet to send to
  the hardware teammate. It asks first for Gerber PCB2 revision confirmation,
  complete `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping, and marked `CN3` /
  `J_HALL` pin-1 evidence.
- `packet_a_workbench_asset_probe_2026-05-19.md`: read-only local Workbench
  asset probe. It records built-in STDRIVE101 board JSONs and the installed
  Board Designer / Board Manager executables as path clues only; Packet A
  remains blocked until a project-specific custom board definition, `.stwb6`,
  and selected-field screenshots are accepted.
- `non_hardware_parallel_track_2026-05-15.md`: no-power plan for temporarily
  skipping Packet B/C scheduling while keeping blockers visible and progressing
  Packet A, STM32-side signal contract, future build-only gate, and delivery
  cleanup.
- `packet_a_local_probe_2026-05-15.md`: local Packet A recheck covering repo
  `.stmcx`, `.stwb6`, screenshots, common user locations, `.stm32cubemx`,
  CubeMX, STM32Cube Repository, Start Menu, and `F:\STMCSDK`. Current result:
  Packet A has a `Partial clue` source candidate.
- `packet_a_capture_checklist_2026-05-15.md`: next acceptable no-power capture
  checklist for `.stmcx`, MotorControl screenshots, or exact GUI path plus
  captured version/config screen.
- `stm32_side_signal_contract_2026-05-15.md`: no-power planning contract for
  future STM32 responsibilities on CN8-facing signals. It separates candidate
  firmware intent from connector routing and hardware proof.
- `future_build_only_gate_2026-05-15.md`: future gate that allows only
  no-power build evidence after Packet A selected fields are accepted; current
  state is still `Not allowed` because Packet A is only `Partial clue`.
- `p2_readiness_snapshot_2026-05-15.md`: current P2 gate decision. It
  consolidates Packet A/B/C, PB3/SWO, signal-contract, and build-only status
  and records that generated-project trust is still `Not allowed`.
- `user_action_queue_2026-05-14.md`: direct user-facing queue for the next
  Packet B board-route source, Packet A MCSDK/MotorControl source, and PB3/SWO
  release evidence.
- `tool_probe_2026-05-14.md`: local tool and GUI evidence gathered for this
  practice turn.
- `workbench_entry_probe_2026-05-14.md`: targeted probe for Workbench launcher,
  `.stmcx`, and installed MCSDK MotorControl package data.
- `gui_capture_result_2026-05-14.md`: records the GUI follow-up attempt,
  screenshots, `.ioc` readback, and the remaining `.stmcx` / MotorControl
  blocker.
- `gui_capture_checklist_2026-05-14.md`: next GUI-only capture checklist.
- `screenshots/2026-05-14_cubemx_home.png`: CubeMX Home launch evidence. This
  is not a saved MCSDK configuration.
- `screenshots/2026-05-14_cubemx_ioc_launch_attempt.png` and
  `screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`: CubeMX opened
  the saved NUCLEO `.ioc` to `Pinout & Configuration`. These are fallback GUI
  evidence, not Workbench `.stmcx` evidence.

## Next Valid Evidence

Use `user_action_queue_2026-05-14.md` and
`source_packet_request_pack_2026-05-14.md` to collect the next valid P2
evidence. For the current hardware-teammate follow-up after the 2026-05-19
`.epro` and Gerber intakes, start with
`hardware_teammate_min_request_2026-05-19.md`, then use
`hardware_supplement_handoff_2026-05-19.md` for the full matrix. Use
`source_packet_review_template_2026-05-14.md` to review any new material before
upgrading any blocker. After the 2026-05-19 clarification image, current PCB2
Hall/PWM strategy review, and Packet A / firmware feasibility review, the next
question is no longer generic hardware mapping and is no longer whether the
current route is immediately clearable. The current no-PCB-change route remains
feasibility only. After the software Hall adapter design review, Packet A Board
Designer / Board Manager path review, and GUI-only checklist, the next valid
Packet A packet is a GUI-only custom/user board capture for the self-developed
STDRIVE101 board if Workbench can create a reviewable artifact; otherwise
Packet A remains blocked and the fallback is surrogate build-only planning
without generated-project trust or separate hardware-rework planning. The next
valid packet must be one of:

- a real `.stwb6` saved by MCSDK 6 Workbench, or legacy `.stmcx`;
- a screenshot showing the Workbench/CubeMX draft configuration;
- an exact reproducible GUI path plus a captured version/config screen;
- the 2026-05-16 custom capture package after a Workbench-supported
  custom/user board entry path is found and its real `.stwb6` plus screenshots
  are added and reviewed;
- current-version CN8 / EDA / netlist / high-resolution route evidence;
- board-level STDRIVE101 protection-path source evidence.
- exact board-revision confirmation, connector orientation proof, PB3/SWO
  release evidence, or later no-power continuity records as defined in
  `hardware_supplement_handoff_2026-05-19.md`.

Even after that evidence exists, P2 still does not authorize powered hardware
actions.

If the hardware-source branch is skipped for scheduling, use
`non_hardware_parallel_track_2026-05-15.md`. Skipping is not clearance: Packet
B/C blockers stay blocked.

Before claiming readiness for generated-project trust or build-only work, read
`p2_readiness_snapshot_2026-05-15.md`. Before running the next Packet A GUI
capture, read `packet_a_capture_task_2026-05-18.md`. Before asking the hardware
teammate for the next board-side packet, read
`hardware_teammate_min_request_2026-05-19.md` and
`hardware_supplement_handoff_2026-05-19.md`. Before treating any Workbench
Board Designer / Board Manager result as Packet A evidence, read
`packet_a_workbench_asset_probe_2026-05-19.md` and
`packet_a_board_designer_manager_path_review_2026-05-19.md`. Before capturing
later Board Designer / Board Manager screenshots, read
`packet_a_board_designer_manager_gui_checklist_2026-05-19.md`.
Before using any STDRIVE101 protection threshold or `nFAULT` behavior in a
phase decision, read
`packet_c_stdrive101_protection_detail_review_2026-05-20.md` and treat the old
`55A` VDS claim as not accepted.
