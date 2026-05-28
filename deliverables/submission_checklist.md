# Submission Checklist

鏈竻鍗曠敤浜庢渶缁堟彁浜わ紱闃舵鎬у涔犲拰宸ョ▼涓婁氦鐗╀互 `workflow/algo_b_teaching_delivery_plan.md` 涓哄噯銆傛瘡鍛ㄦ垨姣忎釜 P 闃舵缁撴潫鏃讹紝鑷冲皯琛ヤ竴浠藉懆浜や粯鍖咃紝璇存槑褰撳墠闃舵銆佸凡瀹屾垚璇佹嵁銆佽繘搴﹀€哄拰鏄惁鍏佽杩涘叆涓嬩竴闃舵銆?
## Weekly / Phase Delivery Pack

- 鍛ㄦ湡鎴栭樁娈碉細
- 瀵瑰簲鍘熻鍒掞細
- 褰撳墠鐪熷疄闃舵锛?- 鏈懆瀹屾垚锛?- 鏈懆涓婁氦鐗╋細
- 璇佹嵁璺緞锛?- 鐢ㄦ埛宸叉帉鎻★細
- 浠嶉渶澶嶄範锛?- 杩涘害鍊猴細
- 涓嬪懆鐩爣锛?- 绂佹鎺ㄨ繘鑼冨洿锛?- 鏄惁鍏佽杩涘叆涓嬩竴闃舵锛?
## Current P1 Catch-up Pack

Use this section before claiming P1 is on-track.

- Pack file: `deliverables/2026-05-12_p1_catchup_pack.md`
- Status: artifacts packaged; learner P0 transfer check still gates `on-track`.

- [x] UART command side-effect table exists in a repo file.
- [x] DMA + IDLE receive flow exists in a repo file.
- [x] Existing COM5 serial evidence is linked from the pack.
- [x] User mastery evidence cites `learning/MASTERY_MAP.md`.
- [x] Open weak points cite `learning/review_queue.md`.
- [x] The pack says explicitly whether P2 MCSDK no-power precheck may start.
- [x] Forbidden scope repeats: no 24V, no power board, no motor, no PWM Gate, no Motor Profiler, no Hall/SMO.

This checklist confirms the P1 catch-up pack exists. It does not by itself prove learner mastery or authorize P2/P3 hardware work.

## Current P2 No-Power Precheck Pack

Use this section before claiming P2 is ready to generate or build an MCSDK project.

- Pack file: `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`
- Packet A 2026-05-15 update: `packet_a_local_probe_2026-05-15.md`,
  `packet_a_capture_checklist_2026-05-15.md`, and
  `source_packet_review_2026-05-15_002_my_first_foc_stwb6.md` now exist. A
  local MCSDK 6 Workbench project candidate,
  `packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`, was found and
  reviewed as `Partial clue`; selected-field Workbench screenshots are still
  required before build-only generated-project trust.
- Non-hardware 2026-05-15 update:
  `stm32_side_signal_contract_2026-05-15.md` and
  `future_build_only_gate_2026-05-15.md` now exist. They preserve STM32 signal
  responsibilities and future build-only rules without upgrading Packet A/B/C
  or any hardware evidence.
- Readiness 2026-05-15 update:
  `p2_readiness_snapshot_2026-05-15.md` now exists. It records that P2 remains
  in progress, Packet A is `Partial clue`, generated-project trust is `Not allowed`,
  and P3 powered or motor work is not allowed.
- Packet A 2026-05-16 update:
  `packet_a_sources/2026-05-16_custom_nucleo_stdrive101/` and
  `source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`
  now exist. The package prepares a new project-specific Workbench capture for
  `NUCLEO-G474RE` plus a Custom / Generic STDRIVE101 power stage, Hall
  fallback, 3-shunt current sensing, supplier-clue motor label
  `57BLF01_VENDOR_CANDIDATE`, no-power motor measurement, and pin assignment
  review. It is `Partial clue / Preparation
  only` until the real `.stwb6` and selected-field screenshots are added.
- Packet A/B 2026-05-17 source intake:
  `source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md` and
  `mcu_pin_compatibility_check_2026-05-17.md` now exist. Supplier motor data
  for `57BLF01` and the hardware teammate `STM32G431RB` pin table are archived
  as `Partial clue`; the hardware teammate says the relevant G431/G474 pins are
  the same, and local MCSDK assets support the compared key rows. This does not
  accept CN8 routing, `J_HALL` numbering, `PB3` SWO release, OPAMP2 feasibility,
  measured motor parameters, or generated-project trust.
- Packet A 2026-05-21 generated-source review:
  `source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md`
  now accepts selected Packet A fields for no-power configuration evidence:
  `FOC`, `NUCLEO-G474RE`, `STM32G474RETx`, `MY-STDRIVE101_POWER_BOARD`, TIM1
  complementary PWM, `PB12/TIM1_BKIN`, three-shunt current sensing, TIM2 Hall
  `PA15/PB3/PB10`, and USART2 `PA2/PA3`. The build-only source prerequisite is
  satisfied. The 2026-05-27 no-power Debug build-only result records exit code
  `0` and confirmed `.elf` / `.map` artifacts. Current PCB2 Hall
  `PA0/PA1/PB4`, current PCB2 `PB3=LIN1`, Packet B/C, continuity, and all
  powered claims remain blocked.
- Current PCB2 2026-05-21 software Hall route confirmation:
  `P14/P15=3V3/GND`, `PB3=LIN1`, and
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4` are now the accepted no-power route
  selection facts. Software Hall adapter is the priority no-PCB-change route;
  hardware rework is fallback only. MCSDK standard TIM2 Hall `PA15/PB3/PB10`
  remains generated configuration evidence only and is not current PCB2 Hall
  proof.
- Software Hall 2026-05-28 firmware-entry plan:
  `software_hall_firmware_entry_plan_2026-05-28.md` is now the Chinese-first
  debug-only no-power boundary for the future `PA0/PA1/PB4` adapter. It
  records the state-machine order, ISR limits, debug fields, and MCSDK hard
  stops. It does not claim firmware implementation, MCSDK hook, Hall
  closed-loop readiness, Gate PWM safety, motor readiness, power-stage
  readiness, or sensorless validation.
- DMM 2026-05-22 no-power request:
  `dmm_continuity_short_check_request_2026-05-22.md` now defines the exact
  continuity and short-check table the user should fill before any software
  Hall adapter implementation. CLI toolchain setup is secondary to this
  real-world no-power evidence in the current step.
- Software Hall 2026-05-22 algorithm-side no-power prep:
  `software_hall_no_power_algorithm_prep_2026-05-22.md` now defines the Hall
  state-machine contract, valid/illegal states, transition rules, candidate
  forward/reverse sequences, debug observables, ISR limits, and MCSDK hard
  stops. It is allowed while unpopulated PCB2 defers DMM, but it does not pass
  DMM, implement firmware, or prove Hall readiness.
- Software Hall 2026-05-22 user exercise:
  `software_hall_state_machine_exercise_card_2026-05-22.md` now gives the
  algorithm role a Chinese-first five-question check and four-row transition
  table. It is waiting for user answers and does not implement firmware or
  prove Hall readiness.
- Software Hall 2026-05-27 pseudocode draft:
  `software_hall_adapter_pseudocode_draft_2026-05-27.md` now defines the
  future adapter function responsibilities, state fields, decision order, ISR
  limits, debug observables, MCSDK hard stops, and code-entry conditions. It is
  pseudocode only and does not implement firmware, open MCSDK Hall integration,
  pass DMM, or prove Hall readiness.
- Software Hall 2026-05-27 processing-order card:
  `software_hall_adapter_processing_order_card_2026-05-27.md` now explains the
  future adapter sequence after the user could not restate it. It is a
  no-power repair artifact only and does not implement firmware, open MCSDK
  Hall integration, pass DMM, or prove Hall readiness.
- Software Hall 2026-05-27 host model:
  `src/software_hall_model.py` and `tests/test_software_hall_model.py` now
  provide a host-side executable reference model for the Hall state-machine
  rules. This is not STM32 firmware, not GPIO/EXTI proof, not MCSDK Hall
  integration, not DMM proof, and not Hall readiness.
- Software Hall 2026-05-27 golden vectors:
  `tests/fixtures/software_hall_golden_vectors.json` and
  `tests/test_software_hall_vectors.py` now provide replayable no-power
  input/output examples for the Hall state-machine rules. This is not STM32
  firmware, not GPIO/EXTI proof, not MCSDK Hall integration, not DMM proof,
  and not Hall readiness.
- Software Hall 2026-05-27 MCSDK integration probe:
  `software_hall_mcsdk_integration_probe_2026-05-27.md` now records read-only
  clues for `HALL_M1`, `TIM2`, `SpeednTorqCtrlM1`, and generated
  `hall_speed_pos_fdbk` / `speed_torq_ctrl` file names. This is not firmware
  implementation, not MCSDK Hall integration, not DMM proof, and not Hall
  readiness.

- Software Hall 2026-05-27 firmware-entry checklist:
  `software_hall_firmware_entry_checklist_2026-05-27.md` now freezes the
  missing entry conditions before any future `PA0/PA1/PB4` adapter code:
  populated-board DMM evidence, GPIO/EXTI boundary review, timestamp-source
  decision, debug route, and separate MCSDK firmware-integration review. The
  build-only record now exists but does not open firmware implementation,
  MCSDK Hall integration, DMM proof, or Hall readiness.
- Software Hall 2026-05-27 GPIO/EXTI boundary review:
  `software_hall_gpio_exti_boundary_review_2026-05-27.md` now drafts the
  static boundary for future `PA0/PA1/PB4` input capture: `EXTI0/EXTI1/EXTI4`
  candidates, minimal ISR duties, and unresolved pull-mode, timestamp, debug,
  build-only, DMM, and MCSDK integration blockers. This is not firmware
  implementation, not GPIO runtime proof, not DMM proof, and not Hall
  readiness.

- Software Hall 2026-05-27 timestamp-source review:
  `software_hall_timestamp_source_review_2026-05-27.md` now drafts the
  timestamp-source boundary before any future adapter code. It excludes `TIM1`
  because it is tied to PWM / ADC injected / FOC timing, keeps current `TIM2`
  as the generated MCSDK Hall clue path, limits `HAL_GetTick()` / SysTick to
  coarse logging because of the `1KHz` `uwTickFreq` clue, and leaves an
  isolated free-running timer with `unsigned delta` as a future review target.
  This is not firmware implementation, not timer configuration, not MCSDK Hall
  integration, not DMM proof, and not Hall readiness.
- Software Hall 2026-05-27 debug-output route review:
  `software_hall_debug_output_route_review_2026-05-27.md` now drafts the
  low-frequency debug-output boundary before any future adapter code. It
  defines snapshot fields and blocks ISR printing, JSON formatting, UART
  transmit, ESP32 / WebSocket, SWO, every-edge streaming, and direct MCSDK
  speed feedback. This is not firmware implementation, not UART
  implementation, not MCSDK Hall integration, not DMM proof, and not Hall
  readiness.

- Software Hall 2026-05-27 MCSDK firmware-integration boundary review:
  `software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md`
  now records that future `direction_candidate` and `speed_candidate` must not
  be written into `HALL_M1`, `SpeednTorqCtrlM1`, speed PID, JEOC / FOC ISR, or
  TIM1 PWM without accepted interface evidence. This is not firmware
  implementation, not MCSDK hook evidence, not DMM proof, and not Hall
  readiness.

- Software Hall 2026-05-27 MCSDK hook evidence request checklist:
  `software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md` now
  requests exact generated or interface source files before any future hook:
  `hall_speed_pos_fdbk.c/.h`, speed / position feedback interface evidence,
  `speed_torq_ctrl.c/.h`, `mc_tasks.c/.h`, `mc_tasks_foc.c`,
  `mc_interface.c/.h`, `mc_api.c/.h`, `mc_app_hooks.c/.h`,
  `mc_parameters.c/.h`, `motorcontrol.c/.h`, interrupt sources,
  current-feedback backend files, and ASPEP / register-interface files. This
  is not firmware implementation, not MCSDK hook evidence, not DMM proof, and
  not Hall readiness.
- Full Workbench `Src/Inc` snapshot 2026-05-27:
  `source_packet_review_2026-05-27_001_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot.md`
  records that the existing external Workbench project
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`
  was copied into
  `packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`
  with `SOURCE_MANIFEST_2026-05-27.md` and `SHA256SUMS.txt`. This is exact
  generated-source availability for read-only interface review only, not
  firmware implementation, not MCSDK hook evidence, not DMM proof, and not Hall
  readiness.

- No-power build-only Debug result 2026-05-27:
  `build_only_result_2026-05-27_qiansai_g474_stdrive101_foc_p2_debug.md`
  records `cmake --build ... --config Debug`, exit code `0`, `ninja: no work
  to do`, and confirmed `.elf` / `.map` artifacts. This is local compile
  evidence only, not flash, not firmware runtime proof, not Hall closed-loop,
  not Gate PWM safety, not motor readiness, and not power-stage readiness.

- Software Hall 2026-05-27 MCSDK speed / position feedback interface review:
  `software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md`
  now records the generated MCSDK feedback chain from TIM2 Hall ISR to
  `HALL_M1`, medium-frequency speed calculation, speed-loop measurement, and
  FOC electrical-angle consumption. It concludes that software Hall remains
  debug-only unless a reviewed `SpeednPosFdbk`-compatible component exists;
  this is not firmware implementation, not MCSDK hook evidence, not DMM proof,
  and not Hall readiness.
- Phase-gate 2026-05-15 update:
  `workflow/phase_gate_checklist.md` now contains a P2 no-power insert. It
  blocks direct NUCLEO-to-Motor-Profiler jumps and requires Packet A before any
  build-only generated-project work.
- Current P2 status correction 2026-05-27: accepted Packet A selected-field
  configuration evidence exists; current PCB2 software Hall route selection is
  confirmed as `PA0/PA1/PB4` with `PB3=LIN1` and `P14/P15=3V3/GND`; a
  no-power Debug build-only pass is recorded. Still missing are software Hall
  firmware implementation, explicit MCSDK integration proof, board-specific
  STDRIVE101 protection-path proof, no-power continuity, and all powered
  validation.
- Status: in progress; tool/status table, pin/config draft, ST source cross-check, pin-function conflict resolution pass, shell GUI evidence probe, expanded future Motor Profiler stop plan, dedicated no-power planning directory, proven CubeMX launch path, CubeMX Home screenshot, next-ring pin/config safety review, current P2 evidence packet, a saved NUCLEO-G474RE CubeMX `.ioc` draft, CubeMX `Pinout & Configuration` fallback screenshots, a Workbench entry probe, STDRIVE101 protection-path review, source packet intake checklist, source packet request pack, user action queue, source packet review template, a 2026-05-15 schematic screenshot candidate review, a non-hardware parallel track, a 2026-05-15 Packet A `.stwb6` legacy source candidate review, a 2026-05-16 custom Packet A capture package, and a 2026-05-17 vendor motor / G431 pin-table source review now exist. The `.ioc` confirms `PB12/TIM1_BKIN`, `PB14/TIM1_CH2N`, `PA2/PA3` VCP, and `PB3` SWO at configuration level; `My_First_FOC.stwb6` is now treated as a legacy learning leftover and remains only `Partial clue` because it uses arbitrary `EVALSTDRIVE101` context. The 2026-05-16 package prepares the intended `NUCLEO-G474RE` plus Custom / Generic STDRIVE101 Workbench path, and the 2026-05-17 review reduces G431/G474 key-pin uncertainty while keeping the motor data and pin table as `Partial clue` only. The protection-path review defines the missing evidence for `DT/MODE`, `nFAULT`, `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, standby, and VDS monitoring. The 2026-05-15 schematic screenshot is useful `Partial clue`; user confirmed it matches the current physical power board and was drawn by the hardware teammate, but formal source revision/date, STM32 endpoint mapping, accepted `DT/MODE` proof, and `STBY` proof are still missing. The non-hardware parallel track records that skipping Packet B/C is a scheduling choice, not clearance. Accepted software Hall firmware integration proof, no-power continuity, a no-power build record, and accepted board-specific STDRIVE101 protection-path proof are still missing.

- [x] P2 no-power card exists in a repo file.
- [x] Tool version/status table records current local evidence and missing PATH/GUI proof.
- [x] Baseline `.ioc` readback is separated from future MCSDK configuration.
- [x] Pin/config draft is explicitly marked as not applied and not a wiring instruction.
- [x] `PA2/PA3` UART-vs-OPAMP, `PC5` nFAULT-vs-OPAMP, and `PB3` SWO-vs-Hall conflicts are visible.
- [x] Frequently used ST PDFs, including STDRIVE101, are mirrored locally under `materials/raw/st_manuals/` and indexed for future retrieval.
- [x] `PC5` / nFAULT conflict is resolved at official pin-function level: reject `PC5`, prefer `PB12/TIM1_BKIN` as draft candidate.
- [x] `PA2/PA3` UART-vs-OPAMP policy is decided for the P2 draft: do not reuse P1 VCP pins as FOC UART unless CubeMX/MCSDK proves it safe.
- [x] Shell probe recorded that no `.stmcx` or Workbench executable path was proven in this turn.
- [x] Dedicated no-power planning directory exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/`.
- [x] Pin/config safety review exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md`.
- [x] CubeMX launch path is proven as `F:\STMCubeMX\STM32CubeMX.exe`.
- [x] CubeMX Home screenshot captured at `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png`.
- [x] Saved `.ioc` was reopened in CubeMX and captured at `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_launch_attempt.png` and `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`.
- [x] Workbench entry probe captured MotorControl package data at `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`; the later 2026-05-15 follow-up resolved the real launcher under `F:\STMCSDK`.
- [x] CN8 / STDRIVE101 route review exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/cn8_stdrive101_route_review_2026-05-14.md`.
- [x] STDRIVE101 protection-path review exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`.
- [x] Source packet intake checklist exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_intake_checklist_2026-05-14.md` and defines accepted / rejected sources before any missing evidence can be upgraded.
- [x] Source packet request pack exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_request_pack_2026-05-14.md` and defines the next `.stmcx` / MotorControl screenshot, CN8 / EDA / netlist, and STDRIVE101 protection-path handoff.
- [x] User action queue exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md` and tells the user to provide Packet B board-route / STDRIVE101 source evidence first, without upgrading any blocker.
- [x] Source packet review template exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_template_2026-05-14.md` and requires Accept / Partial clue / Reject before any blocker can be upgraded.
- [x] 2026-05-15 CN8 / STDRIVE101 schematic screenshot candidate is preserved and reviewed as `Partial clue`, not accepted proof.
- [x] Non-hardware parallel track exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/non_hardware_parallel_track_2026-05-15.md` and keeps Packet B/C skipped-but-blocked while Packet A / signal-contract / build-gate work can continue.
- [x] Packet A local probe exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_local_probe_2026-05-15.md`; the follow-up found `F:\STMCSDK\My_First_FOC.stwb6` and the ST MC Workbench 6.4.2 launcher.
- [x] Packet A `.stwb6` candidate is preserved at `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6` and reviewed at `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_002_my_first_foc_stwb6.md` as `Partial clue`.
- [x] Packet A capture checklist exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_checklist_2026-05-15.md` and defines the next accepted no-power `.stwb6` / legacy `.stmcx` / screenshot / launcher-path capture.
- [x] Packet A custom capture package exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/` with Workbench guide, no-power motor measurement template, pin assignment table, and screenshot inbox.
- [x] Packet A custom capture package review exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md` and marks the package as `Partial clue / Preparation only`.
- [x] 2026-05-17 supplier motor and hardware teammate pin-table sources are archived under `hardware/motor/` and `hardware/schematic/`, reviewed at `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`, and paired with `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcu_pin_compatibility_check_2026-05-17.md`; they remain `Partial clue` only.
- [x] STM32-side signal contract exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/stm32_side_signal_contract_2026-05-15.md` and keeps CN8-facing responsibilities blocked/candidate until source evidence exists.
- [x] Future build-only gate exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/future_build_only_gate_2026-05-15.md` and records generated-project trust as currently `Not allowed` while Packet A is only `Partial clue`.
- [x] P2 readiness snapshot exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md` and records that generated-project trust, build-only work, and hardware action are still not allowed in the current state.
- [x] Phase gate checklist contains a 2026-05-15 P2 no-power insert that separates P2-S1 no-power precheck, P2-S2 build-only generated-project work, and P2-to-P3 blockers.
- [x] The excluded WeChat-side `netlist_PADS.net` candidate was not imported and is not used as current board evidence.
- [x] 褰撳墠璇佹嵁鍖呭凡璁板綍缂哄け鐨?`.stmcx`銆侀厤缃〉鎴浘銆丆N8/EDA/netlist銆丼TDRIVE101 淇濇姢璺緞鍜?SWO 閲婃斁闃诲椤广€?- [x] NUCLEO-G474RE CubeMX `.ioc` 鑽夋宸蹭繚瀛橈細`apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`銆?- [x] `.ioc` 宸茶鍥?`PB12.Signal=TIM1_BKIN`銆乣PB14.Signal=TIM1_CH2N`銆乣PA2/PA3` VCP 鍜?`PB3` SWO銆?- [x] Motor Profiler future plan expanded with required hardware, current limit, stop conditions, and abort criteria.
- [x] Current PCB2 software Hall route confirmed for no-power planning:
  `P14/P15=3V3/GND`, `PB3=LIN1`, and Hall
  `IA/IB/IC -> PA0/PA1/PB4`. This does not prove firmware integration,
  continuity, Hall closed-loop, or powered readiness.
- [x] DMM continuity / short-check request template exists at
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/dmm_continuity_short_check_request_2026-05-22.md`.
- [x] Software Hall no-power algorithm prep exists at
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_no_power_algorithm_prep_2026-05-22.md`;
  this is state-machine/test-contract preparation only, not firmware
  implementation or Hall readiness.
- [x] Software Hall state-machine exercise card exists at
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_state_machine_exercise_card_2026-05-22.md`.
- [x] Software Hall adapter pseudocode draft exists at
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_pseudocode_draft_2026-05-27.md`;
  this is no-power pseudocode only, not firmware implementation or MCSDK Hall
  integration.
- [x] Software Hall adapter processing-order card exists at
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_processing_order_card_2026-05-27.md`;
  this is a no-power teaching card only, not firmware implementation or MCSDK
  Hall integration.
- [x] Software Hall host-side reference model exists at
  `src/software_hall_model.py` with tests in `tests/test_software_hall_model.py`;
  this is host-side algorithm evidence only, not firmware or hardware readiness.
- [x] Software Hall golden vectors exist at
  `tests/fixtures/software_hall_golden_vectors.json` with replay tests in
  `tests/test_software_hall_vectors.py`; this is host-side no-power replay
  evidence only, not firmware or hardware readiness.
- [x] Software Hall MCSDK integration probe exists at
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_integration_probe_2026-05-27.md`;
  this is read-only clue evidence only, not MCSDK Hall integration or Hall
  readiness.

- [x] Software Hall timestamp-source review exists at
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_timestamp_source_review_2026-05-27.md`;
  this is timestamp-source boundary evidence only, not firmware implementation,
  not timer configuration, and not Hall readiness.
- [x] Software Hall debug-output route review exists at
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_debug_output_route_review_2026-05-27.md`;
  this is low-frequency debug-output boundary evidence only, not firmware
  implementation, not UART implementation, and not Hall readiness.
- [x] Software Hall MCSDK firmware-integration boundary review exists at
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md`;
  this is no-power boundary evidence only, not firmware implementation, not
  MCSDK hook evidence, and not Hall readiness.
- [x] Software Hall MCSDK hook evidence request checklist exists at
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md`;
  this is no-power source-evidence request only, not firmware implementation,
  not MCSDK hook evidence, and not Hall readiness.
- [x] Full Workbench `Src/Inc` snapshot exists at
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`;
  this is read-only generated-source evidence with manifest/hash records, not
  firmware implementation, not MCSDK hook evidence, and not Hall readiness.
- [ ] User-filled Hall state-machine exercise table returned and reviewed.
- [ ] Filled DMM continuity / short-check table returned by the user.
- [x] Workbench/MCSDK selected fields accepted as no-power configuration evidence by the 2026-05-21 generated-source review.
- [ ] 宸叉崟鑾?`NFAULT`銆丳WM 杈撳叆銆佺數娴侀噰鏍枫€丠all銆佺數婧愯建鍜屽湴鐨?CN8 / EDA / netlist 璧扮嚎璇佹槑銆?- [ ] 宸叉崟鑾锋澘绾?STDRIVE101 `DT/MODE`銆乣nFAULT`銆乣REG12`銆乣CP`銆乣SCREF`銆乣VS/VM`銆乥ootstrap銆乻tandby 鍜?VDS monitoring 褰撳墠鐗堟簮璇佹嵁銆傚綋鍓嶅彧鏈夌己璇佺煩闃碉紝涓嶆槸閫氳繃璇佹槑銆?- [x] MCSDK MotorControl generated-project side effect archived and reviewed for selected clues only; no hardware trust or runtime claim is added.
- [ ] No-power generated project build record captured. Current blocker: CLI `ninja` and `arm-none-eabi-gcc` paths are unavailable.
- [ ] `PB12/TIM1_BKIN` nFAULT candidate confirmed against CubeMX/Workbench and power-board CN8/EDA/netlist evidence.

This checklist confirms only P2 planning progress. It does not authorize Motor Profiler, power-board connection, motor connection, PWM Gate output, Hall closed-loop, or SMO work.

## Final Submission Items

- 鎶ュ憡
- PPT
- 婕旂ず瑙嗛
- 婧愮爜褰掓。
- BOM / 鍘熺悊鍥?/ PCB 鍏抽敭鎴浘
- 瀹炴祴璇佹嵁绱㈠紩
- 鐗堟湰璇存槑
