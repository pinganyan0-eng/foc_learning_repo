# NEXT_LESSON

Last updated: 2026-05-13

This is the short teaching entry point for the next ChatGPT/Codex learning turn. It does not replace `workflow/algo_b_teaching_delivery_plan.md`; it distills the next executable lesson from the current project stage, weak points, review queue, and delivery debt.

## Progress Checkpoint

- Current real stage: P1 NUCLEO basics and UART command handling is on-track for the current concept layer.
- Corresponding original plan: Week 1/2 transition, now reduced to safe P2 no-power precheck work.
- Current pace: P1 concept layer is on-track; STOP side effects, DMA `Size` count/index, command side-effect reading, and DMA + IDLE callback flow have learner evidence. P2 artifact implementation has started.
- Next lesson target: continue P2 MCSDK no-power precheck without touching power hardware.
- Lesson deliverable: finish the MCSDK no-power precheck card by adding Workbench/CubeMX screenshot or `.stmcx` placeholder evidence, resolving pin/config conflicts, expanding the Motor Profiler plan, and keeping explicit no-go actions.
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
   - `.stmcx` / Workbench configuration screenshot or placeholder. Current status: missing; 2026-05-13 shell probe did not find an existing `.stmcx` or Workbench executable path.
   - NUCLEO pin/config draft. Current status: started, with `PA2/PA3`, `PC5`, `PB3`, and V low-side PWM conflicts called out.
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
   - Verify only documentation, config files, screenshots, build outputs, or tool-version notes. Hardware validation remains out of scope.

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
- run `python tools/normalize_learning_loop.py` and `python -m unittest discover -s tests`.

If the learner misses a safety boundary, do not advance. Update only the relevant learning files and keep the next lesson in P2 precheck.

Do not modify FOC, PWM, MCSDK generated motor-control behavior, ESP-IDF, power-board, or motor-control code as part of this teaching turn unless the user explicitly asks Codex to start the no-power implementation/precheck task and the scope remains no-power.
