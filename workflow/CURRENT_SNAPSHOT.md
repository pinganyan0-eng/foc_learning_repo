# Current Snapshot

Last updated: 2026-06-19

This is the short current-state page for low-token AI handoff. It summarizes
the current project stage and safety boundary. Historical detail remains in
`CURRENT_STATUS.md`.

## Current Stage

- Main project: STM32G474 edge-gateway FOC drive learning and competition
  project.
- Current stage: P2 MCSDK no-power precheck, PCB2 no-power DMM summary
  recorded, and software Hall no-power firmware-entry planning.
- Current PCB2 no-power DMM result:
  `pcb2_no_power_dmm_continuity_short_check_result_2026-06-19.md` records the
  user-reported table as `通` for `CN3_10-PA0`, `CN3_11-PA1`,
  `CN3_12-PB4`, `CN3_2-PB3`, `CN3_14-3V3`, `CN3_15-GND`, and
  `CN3_13-PB12`, with all requested rail, signal-to-rail, and Hall-pair
  short checks reported as `不通`. Raw ohm values were not provided. This
  closes the immediate no-power DMM-table blocker for planning only; it does
  not authorize firmware implementation, flash, 24 V, motor connection,
  Gate PWM, Motor Pilot, Motor Profiler, Hall closed loop, sensorless
  operation, power-stage readiness, or motor readiness.
- Current post-DMM software Hall boundary:
  `software_hall_code_entry_boundary_after_dmm_2026-06-19.md` defines the
  next allowed no-power document-side work for `PA0 / PA1 / PB4`: exact future
  debug-only file list, GPIO pull / EXTI trigger policy review,
  timestamp-source criteria, low-frequency debug snapshot route, no-power
  build checklist, and rollback checklist. It does not create firmware or open
  MCSDK hooks.
- Current hardware handoff: the 2026-06-19 no-power and static checks have
  reached the execution-gate decision for a bounded STDRIVE101 single-input
  wake diagnostic. If the user says `开始单输入唤醒诊断` or `单输入唤醒`, this means
  `CN3_14 / 3V3 -> 10 kohm series resistor -> CN3_2 / LIN1` with motor
  disconnected and HSPY `24 V / 0.2 A`. It does not mean Codex mobile wakeup,
  service wakeup, or automation wakeup. Before giving steps, read
  `stdrive101_reg12_single_input_wake_plan_2026-06-19.md`,
  `stdrive101_reg12_wake_official_web_review_2026-06-19.md`, and
  `out1_output_node_no_power_short_check_result_2026-06-19.md`.
- Current single-input wake baseline result:
  `stdrive101_reg12_single_input_wake_baseline_result_2026-06-19.md` records
  the user-reported pre-stimulus baseline as `CV`, `0.036 A`,
  `VS / 24V_FUSED = 24 V`, `CN3_14 / 3V3 = 3.3 V`,
  `CN3_13 / nFAULT = 3.3 V`, and `REG12 = 0.33 V`. This closes only the
  baseline condition; no `10 kohm` stimulus was installed and no wake result
  exists yet.
- The single-input wake diagnostic remains a bounded power-stage diagnostic:
  no motor, no firmware PWM, no Motor Pilot, no Motor Profiler, no Hall
  closed-loop claim, no sensorless claim, and no power-stage or motor
  readiness claim.
- Current real-world blocker update: PCB2 is reported populated / in hand, the
  route is unchanged, and the 2026-06-19 no-power DMM summary is now recorded.
  The next allowed hardware-adjacent step is still no-power only: review the
  software Hall adapter interface / code-entry boundary for `PA0 / PA1 / PB4`.
- No-power build-only status: Debug build command completed with exit code `0`
  on 2026-05-27 for
  `QIANSAI_G474_STDRIVE101_FOC_P2`; this is local compile evidence only.
- Strategy: use ST MCSDK for the motor-control framework, keep Hall
  closed-loop as the safe fallback path, and treat SMO/PLL sensorless as a
  later stretch goal.
- Real-time boundary: STM32 owns FOC. ESP32-C3 displays, forwards, and alerts
  only.

## Current PCB2 Route

- Current Hall planning route: `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1` and is not current PCB2 Hall.
- `P14/P15=3V3/GND`.
- PCB2 populated status is now reported, and the 2026-06-19 no-power DMM
  summary records continuity for `IA/IB/IC -> PA0/PA1/PB4`, `PB3=LIN1`,
  `P14/P15=3V3/GND`, and `nFAULT->PB12`, plus no reported rail / signal /
  Hall-line hard shorts. The WP-030 no-power Hall mixed-sequence check is
  passed at L4.

## Current Software Hall State

- Host-side and document-side no-power software Hall preparation exists:
  state-machine rules, pseudocode, host model, golden vectors, MCSDK integration
  clues, firmware-entry checklist, GPIO/EXTI boundary review,
  timestamp-source review, debug-output route review, MCSDK firmware-integration boundary review, and MCSDK hook evidence request checklist.
- A Chinese-first no-power firmware-entry plan now exists at
  `software_hall_firmware_entry_plan_2026-05-28.md`. It locks
  `PA0/PA1/PB4` as the future software GPIO/EXTI Hall route, keeps
  `PB3=LIN1` out of Hall, defines the debug-only adapter layers, state-machine
  order, ISR limits, debug fields, MCSDK hard stops, and user checkpoint.
  Decision:
  `Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.
- A post-DMM code-entry boundary now exists at
  `software_hall_code_entry_boundary_after_dmm_2026-06-19.md`. It updates the
  entry path after the DMM summary and keeps the next work as document-side
  no-power planning only.
- The external Workbench project
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`
  exists and its generated `Src/`, `Inc/`, `cmake/`, and top-level build
  metadata are now archived as
  `packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`
  with a manifest, hash list, and source review.
- A read-only MCSDK speed / position feedback interface review now exists at
  `software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md`.
  It traces `HALL_M1`, `HALL_CalcAvrgMecSpeedUnit`, `STC_GetSpeedSensor`,
  `SPD_GetAvrgMecSpeedUnit`, and `SPD_GetElAngle`, and records that future
  software Hall must remain debug-only unless a separate reviewed
  `SpeednPosFdbk`-compatible component proposal is created.
- No-power build-only result now exists at
  `build_only_result_2026-05-27_qiansai_g474_stdrive101_foc_p2_debug.md`.
  It records `cmake --build ... --config Debug`, exit code `0`, `ninja: no
  work to do`, and `.elf` / `.map` artifacts from the external Workbench build
  directory.
- PR #5, `learning notes`, was reviewed and merged into `master` on
  2026-06-01 with merge commit
  `2b614b4aae4eb40a5b2a882c5f2252dadbe06079`. Its two added learning files
  record only L2 MCSDK Hall speed / position feedback concept evidence and do
  not claim MCSDK Hall closed-loop, Motor Profiler, power-board, motor, PWM,
  serial, or build validation.
- WP-030 software Hall processing-order transfer is now L4 at no-power
  mixed-sequence level. The next software-Hall learning risk is firmware-entry
  pseudocode discipline, not more sequence recall.
- These are no-power planning and host-model evidence only.
- They do not prove GPIO runtime behavior, MCSDK Hall integration, MCSDK hook
  readiness, DMM continuity, Hall closed-loop behavior, flash readiness, or
  powered readiness.
- The DMM table summary is now recorded for no-power planning only. It is not
  powered validation, firmware runtime proof, MCSDK hook readiness, Hall
  closed-loop behavior, or motor readiness.

## Current AI Architecture Work

- This repository now treats AI assistance as an evidence-first workflow:
  short context, grounded retrieval, one active task, explicit safety boundary,
  contract checks, and evidence records.
- `docs/00_project_truth/ai_architecture.md` is the architecture contract.
- AI Architecture v2 adds `tools/build_context_pack.py --mode ai_maintenance`
  for AI workflow maintenance handoffs.
- Project workflow maintenance now uses
  `tools/build_context_pack.py --mode workflow_maintenance` for automation,
  learning feedback, closeout checklist, definition-of-done, submission
  checklist, index, and tool-contract maintenance.
- Project Skill v2 is now a concise router at
  `codex_skills/stm32g474-foc-assistant/SKILL.md`, with one-level references
  for project navigation, no-power boundaries, learning feedback, and workflow
  maintenance.
- `tools/check_project_skill_install.py` now checks whether the installed user
  Skill matches the repo-local project Skill source.
- `tools/run_ai_maintenance_audit.py` now provides a consolidated no-power AI
  maintenance audit runner, with full and quick repo-only modes plus optional
  Markdown report output via `--write-report`. It records
  `git status --short` as dirty-worktree handoff evidence before
  `git diff --check`; the `git_status` step preserves full output even when
  other step output is tail-limited by `--max-output-chars`, and exposes a
  parsed `workspace_status` summary with `status_paths`, `path_groups`, and
  ordered `focus_groups`, plus a `handoff_review_queue` that names the review
  focus for each dirty-worktree group. It also exposes `contract_status` to
  distinguish contract errors from known review-lifecycle warnings and strict
  readiness, `readability_status` to separate guarded entry headers from
  broader legacy mojibake debt, plus `closeout_summary` for the top-level
  repo-maintenance closeout decision, dirty-worktree state, review-needed
  flag, and next review focus. This does not clean the worktree or validate
  hardware.
- `tools/check_ai_contracts.py` is the no-power workflow consistency checker.
  It checks entry files, safety phrases, task review lifecycle, UTF-8
  readability, index coverage, retrieval-eval coverage, project workflow
  contracts, and dangerous positive claims across project truth, workflow,
  Skill, no-power precheck, deliverable, interface, and learning text.
- The readable entry headers of `workflow/evidence_register.md` and
  `deliverables/submission_checklist.md` are now contract-checked. Broader
  legacy historical mojibake remains separate review work rather than a
  silent full-repair claim.
- Review lifecycle policy: Codex may leave `done + Review Required` warnings
  during implementation closeout. User review clears strict warnings; Codex
  must not silently mark the task `reviewed` just to make strict mode pass.
- `retrieval_eval/queries.json` covers dual-teacher guard, current PCB2 Hall
  route, DMM pending/no-power boundary, ACTIVE_TASK review lifecycle, and ESP32
  real-time boundary, plus workflow closeout, automation no-write, learning
  feedback, repo-maintenance DoD, project Skill v2 router, and project Skill
  install drift cases, plus the AI maintenance audit runner case.
- `tools/search_local_v2.py --eval` is source-finding regression evidence only,
  not hardware validation.
- Dual-teacher concept-only role guard is now explicit: ChatGPT teaches pure
  theory/concept turns, while Codex provides the ChatGPT prompt, reviews and
  records returned learning evidence, and keeps repo-side engineering work.
- The AI architecture doc now also defines a structured subagent communication
  protocol with hierarchical task decomposition, context filtering, a summary gate,
  and an old-flat-vs-new-filtered comparison. Subagent output is
  summarized before it reaches the main-agent decision loop.
- A three-hour optimization sprint report now exists at
  `workflow/three_hour_optimization_report_2026-06-17.md`. It records
  subagent roles, timestamped progress, mid-project review, Obsidian Chinese
  learning note enhancements, retrieval-maintainability changes, verification
  commands, and efficiency recommendations.

## Current Safety Boundary

Unless a later dated phase-gate decision explicitly opens the action:

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

Current Packet A and software Hall artifacts may be accepted only as no-power
configuration, planning, host-model, or generated-source clues. They do not
prove PCB2 physical routing, continuity, protection behavior, firmware runtime
behavior, or powered behavior.

## Default Read Order

1. `AI_CONTEXT.md`
2. `workflow/CURRENT_SNAPSHOT.md`
3. `workflow/ACTIVE_TASK.md`
4. `docs/00_project_truth/project_context.md`
5. Mode-specific files named by `tools/build_context_pack.py`

Open `CURRENT_STATUS.md`, `workflow/evidence_register.md`, historical Packet
records, manuals, and generated directories only for concrete evidence,
hardware-safety, phase-gate, or implementation tasks.
