# AI_CONTEXT

This is the default low-token handoff file for the STM32G474 FOC project. Read this first, then open longer files only when the current task needs them.

## Current Project

- Main project: STM32G474 edge-gateway FOC drive learning and competition project.
- Main repo: `foc_learning_repo/`.
- Highest-priority fact source: `docs/00_project_truth/project_context.md`.
- Low-token current snapshot: `workflow/CURRENT_SNAPSHOT.md`.
- AI architecture contract: `docs/00_project_truth/ai_architecture.md`.
- Project Skill v2 source:
  `codex_skills/stm32g474-foc-assistant/SKILL.md`, with task-specific
  references under `codex_skills/stm32g474-foc-assistant/references/`.
- AI Architecture v2 maintenance context:
  `python tools/build_context_pack.py --mode ai_maintenance`.
- Project workflow maintenance context:
  `python tools/build_context_pack.py --mode workflow_maintenance`.
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

## AI Architecture v2 Handoff

- Use `ai_maintenance` context when the task changes AI workflow docs, local
  retrieval, context packs, contract checks, workflow handoff, or AI tests.
- Use `workflow_maintenance` context when the task changes the project
  automation playbook, learning feedback loop, closeout checklist, definition
  of done, submission checklist, workflow index entries, or project Skill
  maintenance references.
- Project Skill v2 keeps `SKILL.md` as a concise router and moves detailed
  no-power, learning-feedback, navigation, and workflow-maintenance rules into
  one-level `references/*.md` files.
- `python tools/check_project_skill_install.py` checks whether the installed
  user Skill matches the repo-local project Skill source. Use `--repo-only
  --json` for environment-independent tests.
- `python tools/run_ai_maintenance_audit.py` runs the consolidated no-power AI
  maintenance audit. Use `--quick --repo-only-skill --json` for lightweight
  environment-independent handoff checks, or `--write-report <path>` for a
  human-readable Markdown audit report. The audit records `git status --short`
  as dirty-worktree handoff evidence before `git diff --check`; this does not
  clean the worktree or validate hardware. The `git_status` step preserves full
  output even when other step output is tail-limited by `--max-output-chars`,
  and exposes a parsed `workspace_status` summary with `status_paths`,
  `path_groups`, ordered `focus_groups`, and `handoff_review_queue` review
  focus items for handoff. It also exposes `contract_status`, which separates
  AI contract errors, review-lifecycle warnings, unexpected warnings,
  `strict_ready`, and `implementation_closeout_ok`, plus `closeout_summary`
  for the top-level repo-maintenance closeout decision, dirty-worktree state,
  review-needed flag, and next review focus.
- `tools/check_ai_contracts.py` should have no errors after implementation.
  It scans project truth, workflow, Skill, no-power precheck, deliverable,
  interface, and learning text for dangerous positive hardware claims.
  It also guards the readable entry headers of `workflow/evidence_register.md`
  and `deliverables/submission_checklist.md`; this is not a claim that every
  legacy historical row has been repaired.
  Before user review, it may still warn that `ACTIVE_TASK.md` is `done` and
  awaiting review or still lists pending verification.
- `python tools/check_ai_contracts.py --strict` is the post-review target:
  user review clears strict warnings; Codex must not silently mark the task
  `reviewed` just to make strict mode pass.
- Local retrieval hits and retrieval evals are source-finding evidence only.
  They do not validate continuity, soldering, firmware runtime behavior, Gate
  PWM safety, Hall closed-loop behavior, or powered readiness.

## Default Read Order

Use this order for normal handoff:

1. `AI_CONTEXT.md` for this short summary.
2. `workflow/CURRENT_SNAPSHOT.md` for the low-token current state.
3. `workflow/ACTIVE_TASK.md` for the current single task and forbidden actions.
4. `docs/00_project_truth/project_context.md` for stable project facts.
5. The latest top section of `CURRENT_STATUS.md` only when the task needs current history.
6. Mode-specific context from `tools/build_context_pack.py` when the task maps
   to `codex_task`, `ai_maintenance`, `workflow_maintenance`, `teaching`,
   `hardware_review`, `mcsdk_packet`, `experiment_analysis`, or
   `report_defense`.
7. Specific evidence files only when the task names Packet A/B/C, build-only gate, hardware safety, phase gates, or a dated source packet.

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
