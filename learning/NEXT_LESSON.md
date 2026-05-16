# NEXT_LESSON

Last updated: 2026-05-14

This is the short teaching entry point for the next ChatGPT/Codex learning turn. It does not replace `workflow/algo_b_teaching_delivery_plan.md`; it distills the next executable lesson from the current project stage, weak points, review queue, and delivery debt.

## Progress Checkpoint

- Current real stage: P1 NUCLEO basics and UART command handling is on-track for the current concept layer.
- Corresponding original plan: Week 1/2 transition, now reduced to safe P2 no-power precheck work.
- Current pace: P1 concept layer is on-track; STOP side effects, DMA `Size` count/index, command side-effect reading, and DMA + IDLE callback flow have learner evidence. P2 artifact implementation has started.
- Next lesson target: continue P2 MCSDK no-power precheck without touching power hardware.
- Lesson deliverable: skip basic toolchain navigation and continue from the pin/config safety review; current fallback GUI evidence proves the saved `.ioc` opens in CubeMX, and the Workbench entry probe proves MotorControl package data exists. The user asked on 2026-05-15 to skip the hardware-source package branch for now, so the next safe parallel handoff is `apps/stm32_g474_foc/mcsdk_no_power_precheck/non_hardware_parallel_track_2026-05-15.md`: keep Packet B/C blockers visible, then progress Packet A Workbench/MCSDK MotorControl screenshot or `.stmcx`, STM32-side signal contract, and future build-only gate.
- 2026-05-15 Packet A follow-up: `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_local_probe_2026-05-15.md` and `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_checklist_2026-05-15.md` now record a bounded local search and the next acceptable capture checklist. A later follow-up found `F:\STMCSDK\My_First_FOC.stwb6`, preserved it under `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`, and reviewed it in `source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`. Packet A is now `Partial clue`, not accepted build-only clearance.
- 2026-05-16 Packet A correction: user clarified `My_First_FOC.stwb6` is only a previous toolchain-learning leftover and its `EVALSTDRIVE101` power-board choice is arbitrary. Codex added `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/` and `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`. The new target is `NUCLEO-G474RE` plus a Custom / Generic STDRIVE101 power stage, FOC, Hall fallback, 3-shunt current sensing, placeholder motor data, no-power motor measurement, and pin assignment review. Status is `Partial clue / Preparation only` until the real `.stwb6` and selected-field screenshots exist.
- 2026-05-15 non-hardware follow-up: `apps/stm32_g474_foc/mcsdk_no_power_precheck/stm32_side_signal_contract_2026-05-15.md` and `apps/stm32_g474_foc/mcsdk_no_power_precheck/future_build_only_gate_2026-05-15.md` now split the STM32-side signal responsibilities and future generated-project build-only rules into standalone review artifacts. They do not upgrade Packet A/B/C or hardware evidence.
- 2026-05-15 readiness follow-up: `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md` now consolidates Packet A/B/C, PB3/SWO, signal-contract, and build-only status into one gate decision. Current decision: P2 remains in progress, Packet A is `Partial clue`, generated-project trust is `Not allowed`, and powered or motor work remains forbidden.
- 2026-05-15 phase-gate follow-up: `workflow/phase_gate_checklist.md` now contains a P2 no-power insert. It prevents direct NUCLEO-to-Motor-Profiler jumps, separates P2-S1 no-power precheck from P2-S2 build-only generated-project work, and keeps P2-to-P3 blockers explicit.
- Forbidden scope: no 24V, no power board, no motor, no PWM Gate, no real Motor Profiler run, no Hall closed-loop, no SMO, no claim that `SET_RPM` controls real speed.

## Review Priority Stack

### P0 - Completed Current Layer

1. STOP side effects:
   - Given `ARMED,target_rpm=1200,mode_change_count=5` and command `STOP`, predict final `mode`, `target_rpm`, and `mode_change_count`.
   - Compare with `IDLE,target_rpm=1200,mode_change_count=5` and command `STOP`.
2. DMA receive size/index:
   - Explain why `Size = 10` means process indices `0..9`.
   - State the loop condition: `i < Size`.

Current status: passed on 2026-05-13 and recorded in `learning/session_notes.md`, `learning/MASTERY_MAP.md`, `learning/weak_points.md`, `learning/review_queue.md`, and `workflow/current_learning_sprint.md`.

### P1 - Keep As Review Only

1. Command classification:
   - Classify `PING`, `MODE?`, `ARM`, `SET_RPM`, and `STOP` as read-only, guarded state command, safe command, or guarded target command.
2. Branch reading:
   - For each command, separate match condition, guard condition, state/target side effect, counter side effect, and response output.
3. DMA + IDLE callback structure:
   - Explain: DMA fills `rx_buf`; IDLE means this batch is ready; CPU loops through `rx_buf[0..Size-1]`; every byte goes into `AppFeedRxByte(...)`; reception restarts.

Current status: current concept-layer checks passed. Reopen only when implementing/reviewing real callback code or adding a new command.

### P2 - Next Lesson Candidate

1. MCSDK / Motor Control Workbench no-power role map:
   - What CubeMX, MCSDK/Workbench, generated project, and Motor Profiler each do.
   - What is only planning versus what requires power hardware.
2. P2 no-power artifact list:
   - Tool version table. Current status: started in `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`.
   - `.stwb6` / legacy `.stmcx` / Workbench configuration screenshot or placeholder. Current status: `My_First_FOC.stwb6` is preserved only as a legacy `Partial clue`; the 2026-05-16 custom NUCLEO + STDRIVE101 capture package is prepared, and selected-field Workbench screenshots plus the new project-specific `.stwb6` are still needed.
   - NUCLEO pin/config draft. Current status: started, with `PA2/PA3`, `PC5`, `PB3`, and V low-side PWM conflicts called out.
   - Pin/config safety review. Current status: `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md` exists and defines evidence classes, hard stops, and the minimum next evidence packet.
   - 证据包。当前状态：`apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md` 已记录 `.stmcx`、MotorControl 配置页截图、CN8/EDA/netlist 走线证明、板级 STDRIVE101 保护路径证明和 SWO 释放证据仍是缺失阻塞项；新增的 CubeMX `.ioc` 截图只补了 GUI fallback 证据。
   - Source packet request pack. Current status: `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_request_pack_2026-05-14.md` exists and turns missing evidence into Packet A/B/C requests for the next handoff.
   - User action queue. Current status: `apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md` exists and says the most useful next user action is Packet B board-route / STDRIVE101 source evidence, followed by Packet A MCSDK/MotorControl evidence and PB3/SWO release evidence if needed.
   - Source packet review template. Current status: `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_template_2026-05-14.md` exists and makes incoming source review explicit: Accept, Partial clue, or Reject before updating the evidence packet.
   - Non-hardware parallel track. Current status: `apps/stm32_g474_foc/mcsdk_no_power_precheck/non_hardware_parallel_track_2026-05-15.md` exists and records that Packet B/C may be skipped for scheduling only, while Packet A, STM32-side signal contract, and future build-only gate can progress.
   - Motor Profiler plan only, not a real profiler run. Current status: future P3 stop conditions and rollback requirements are now expanded in the P2 card.
   - Risk/no-go checklist.
3. Safety boundary:
   - P2 precheck may discuss/generate/configure only.
   - Do not connect power board, motor, 24V, PWM Gate, or run Motor Profiler.

## Teaching Flow

Use this order. Do not skip to real MCSDK actions until the no-power boundary is stable.

1. Visible behavior:
   - Start from the fact that P1 NUCLEO command behavior is validated and the current MCSDK/Hall/power-board items are not validated.
2. Feature sentence:
   - P2 no-power precheck prepares MCSDK configuration knowledge and artifacts without energizing motor hardware.
3. Rule table:
   - Separate allowed no-power actions from forbidden power/hardware actions.
4. Function responsibilities:
   - MCSDK/Workbench: configuration and generated-project planning.
   - CubeMX / VS Code STM32 extension: project generation/build context.
   - Motor Profiler: future measurement plan only, not a current action.
5. Files/artifacts:
   - Use the P2 artifact list above; do not create hardware evidence that does not exist.
6. Test:
   - Verify only documentation, config files, screenshots, routing evidence, build outputs, or tool-version notes. Hardware validation remains out of scope.

## Acceptance Criteria

The next lesson is complete when the learner can do all of these without hints:

- Explain what P2 MCSDK no-power precheck is allowed to do.
- Explain what P2 is still forbidden to do.
- Identify which artifacts must be collected before a later Motor Profiler / Hall stage.
- State why P2 no-power precheck does not prove motor-control behavior.
- Point to the packaged P1 artifacts and the P2 precheck card or checklist.

## Codex Handoff After The Lesson

If the learner passes the P2 no-power precheck lesson, Codex should:

- update `learning/session_notes.md`, `learning/MASTERY_MAP.md`, and `learning/review_queue.md`;
- update `workflow/current_learning_sprint.md` or create the next sprint card if P2 becomes active;
- update the P2 no-power precheck artifact and linked checklist/evidence files;
- 持续更新 `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`，直到缺失的 `.stmcx` / 截图、CN8/EDA/netlist 和 STDRIVE101 保护路径证据补齐；
- use `apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md` to tell the user exactly which packet to provide next;
- use `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_request_pack_2026-05-14.md` as the next evidence handoff checklist;
- use `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_template_2026-05-14.md` before upgrading any blocker after a source packet arrives;
- use `apps/stm32_g474_foc/mcsdk_no_power_precheck/non_hardware_parallel_track_2026-05-15.md` if the user chooses to defer hardware-source evidence temporarily;
- run `python tools/normalize_learning_loop.py` and `python -m unittest discover -s tests`.

If the learner misses a safety boundary, do not advance. Update only the relevant learning files and keep the next lesson in P2 precheck.

Do not modify FOC, PWM, MCSDK generated motor-control behavior, ESP-IDF, power-board, or motor-control code as part of this teaching turn unless the user explicitly asks Codex to start the no-power implementation/precheck task and the scope remains no-power.
