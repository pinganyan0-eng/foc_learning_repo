# AI_CONTEXT

This is the default low-token handoff file for the STM32G474 FOC project. Read this first, then open longer files only when the current task needs them.

## Current Project

- Main project: STM32G474 edge-gateway FOC drive learning and competition project.
- Main repo: `foc_learning_repo/`.
- Highest-priority fact source: `docs/00_project_truth/project_context.md`.
- Low-token current snapshot: `workflow/CURRENT_SNAPSHOT.md`.
- AI architecture contract: `docs/00_project_truth/ai_architecture.md`.
- Current stage: P2 MCSDK no-power precheck / Packet A generated-source review / no-power build-only Debug pass recorded / software Hall firmware-entry plan and MCSDK speed-position boundary governance.
- Current strategy: use ST MCSDK for the motor-control framework, keep Hall closed-loop as the safe fallback path, and treat SMO/PLL sensorless as a later stretch goal.
- Real-time boundary: STM32 owns FOC. ESP32-C3 displays, forwards, and alerts only.

## Dual-Teacher Guard

- Concept-only role guard: if the user asks theory, concepts, "I do not understand", "teach me", "what should I learn", `我不懂`, `教我`, or `还要学什么`, and no repo file, command, build output, test, log, screenshot, or learning-record write is needed, this is a ChatGPT teaching turn.
- Codex must not teach the full lesson in that case. Codex should provide a concrete ChatGPT prompt/task packet, state what the user should bring back, then Codex reviews and records the result and decides the next engineering step.
- If ChatGPT has GitHub write access, it may open a learning-evidence PR for its own concept lesson. Codex later syncs, reviews, verifies, and records that PR; it is not accepted project truth until Codex review.
- Except for a ChatGPT-owned learning-evidence PR, if the turn touches real files, commands, builds, tests, logs, screenshots, evidence, learning records, GitHub, or hardware-safety state, Codex owns the repo-side work and must not redirect that engineering work to ChatGPT.

## Current Safety Boundary

Unless a later dated phase-gate decision explicitly opens the action, do not do or claim any of these:

- No flash.
- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Motor Pilot run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
- No powered readiness, motor readiness, or power-stage readiness claim.

Current Packet A selected fields, software Hall firmware-entry plan, software Hall MCSDK speed/position feedback interface review, and no-power Debug build-only pass may be accepted only as no-power generated-source / interface / planning / compile evidence. They do not prove PCB2 physical routing, continuity, protection behavior, firmware runtime behavior, MCSDK hook readiness, Hall closed-loop behavior, or powered behavior.

## Default Read Order

Use this order for normal handoff:

1. `AI_CONTEXT.md` for this short summary.
2. `workflow/CURRENT_SNAPSHOT.md` for the low-token current state.
3. `workflow/ACTIVE_TASK.md` for the current single task and forbidden actions.
4. `docs/00_project_truth/project_context.md` for stable project facts.
5. The latest top section of `CURRENT_STATUS.md` only when the task needs current history.
6. Specific evidence files only when the task names Packet A/B/C, build-only gate, hardware safety, phase gates, or a dated source packet.

For teaching tasks, also read the relevant `learning/` files called out by the skill or user request.

## Do Not Read By Default

These are long or generated areas. Open them only for a concrete task:

- `materials/extracted/*`
- `materials/raw/*`
- `workflow/evidence_register.md`
- `workflow/current_learning_sprint.md`
- `vector_store/*`
- historical Packet review files
- generated build directories
- Obsidian plugin code under `.obsidian/plugins/`

## Current Minimum Next Context

For P2 work, the usual next context is:

- `workflow/CURRENT_SNAPSHOT.md`
- `workflow/ACTIVE_TASK.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/future_build_only_gate_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- the specific Packet review file named by the task

Do not open broad manuals or full extracted materials unless the task requires source verification.

## Maintenance Rule

Keep this file short. It is a navigation summary, not a replacement for evidence. If project facts conflict, trust `docs/00_project_truth/project_context.md` and the latest dated evidence records over this file.
