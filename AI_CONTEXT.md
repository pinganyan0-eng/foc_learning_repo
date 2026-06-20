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
- Current stage: P2 MCSDK no-power precheck / Packet A generated-source review / no-power build-only Debug pass recorded / PCB2 no-power DMM summary recorded / software Hall firmware-entry plan and MCSDK speed-position boundary governance / STDRIVE101 single-input wake clean bounded retest, post-retest all-inputs-low static recovery recheck, USB-only MCU-facing driver input default-state check, USB + 24 V static recheck, PWM/gate-test no-power source review, R3_2 MCSDK PWM output path source closure, manual gate-test firmware plan, manual gate-test lockout source package, manual gate-test lockout object-only target, manual gate-test lockout object-only build pass, and manual gate-test USB-only runtime lockout preparation recorded.
- Current manual gate-test USB-only runtime lockout preparation:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_prep_2026-06-20.md`
  records Gate C preparation only. It carries forward the object-only build
  pass, source hashes, object hashes, future linked-image boundary, USB-only
  no-24V physical boundary, expected future pin readings, stop rules, and a
  user table for a later approved runtime. It does not authorize flash, Run /
  Debug, USB runtime execution, 24 V, Gate PWM output, Motor Pilot, Motor
  Profiler, motor connection, or readiness claims. Next allowed checkpoint is
  a linked-image build-boundary plan or build-only record for the lockout
  image, still without runtime execution.
- Current manual gate-test lockout object-only build pass:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_lockout_object_build_pass_2026-06-20.md`
  records a successful no-power object-only build of
  `stdrive101_gate_lockout_objects` with STM32Cube GNU Arm GCC `14.3.1` and
  Ninja `1.13.2`. It produced `gate_test_lockout.c.obj` and
  `main_lockout.c.obj` only; no lockout ELF / HEX / BIN / MAP linked firmware
  image was produced. This proves object compilation only and does not
  authorize flash, Run / Debug, 24 V, Gate PWM output, Motor Pilot, Motor
  Profiler, motor connection, or readiness claims.
- Current manual gate-test lockout object-only target:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_lockout_object_target_2026-06-20.md`
  records a repo-local CMake object-library target for the isolated lockout
  package. It compiles only `gate_test_lockout.c` and `main_lockout.c` object
  files, with no ELF / HEX / BIN link target. `REPO_ROOT` was corrected and
  the CMSIS device/core headers resolve in static path checks. The sandbox
  blocked external Ninja during CMake configure, and the escalation path
  returned 503, so no object build pass is claimed. This does not authorize
  flash, Run / Debug, 24 V, Gate PWM output, or motor action.
- Current manual gate-test lockout source package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_lockout_source_package_2026-06-20.md`
  records the repo-local isolated lockout source package under
  `manual_gate_test_lockout_build_only_2026-06-20/`. The package forces
  `PA8 / PA9 / PA10 / PB13 / PB14 / PB15` low as GPIO outputs, keeps
  `PB12 / nFAULT` as input, clears TIM1 `CCER`, clears TIM1 `MOE` and
  automatic output, and leaves TIM1 break enabled. Static grep found no
  forbidden normal MCSDK start / command-ingress / output-enable symbols in
  the lockout `Src` and `Inc`. There is no embedded build target yet, no flash,
  no runtime, no 24 V, no Gate PWM output, and no motor action.
- Current manual gate-test firmware plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_firmware_plan_no_power_2026-06-20.md`
  records a plan only. Normal MCSDK start remains blocked. A future gate-test
  must use an isolated lockout firmware path that avoids `MC_StartMotor1`,
  `MCI_START`, PC13 start/stop, MCP command ingress, Motor Pilot, Hall
  closed-loop paths, speed-loop paths, and motor connection. First future
  lockout image must keep `PA8 / PA9 / PA10 / PB13 / PB14 / PB15` low,
  monitor `PB12 / nFAULT`, keep TIM1 `MOE = 0`, `CCER = 0`, automatic output
  disabled, and break enabled. This does not authorize firmware edits, build,
  flash, Run / Debug, 24 V, Gate PWM output, or motor action.
- Current R3_2 MCSDK PWM output path closure:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_r3_2_mcsdk_pwm_output_path_source_closure_2026-06-20.md`
  records that the exact local Workbench MCSDK
  `r3_2_g4xx_pwm_curr_fdbk.c` was found and hashed as
  `D3787B25374154AB1DC6A2CABD05DE299D5691DA92DDC4DE4BEC93DE81BE2451`.
  The reviewed source confirms that `R3_2_TurnOnLowSides()` treats `0` ticks
  as low-sides ON and calls `LL_TIM_EnableAllOutputs(TIMx)`, while the
  generated state path calls `LL_TIM_DisableBRK(TIM1)` before the boot-cap
  low-side action. Normal generated MCSDK start remains blocked for powered
  PWM. Next allowed checkpoint is a no-power-only manual gate-test firmware
  plan, not hardware output.
- Current STDRIVE101 PWM/gate-test source review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_pwm_gate_test_no_power_source_review_2026-06-20.md`
  records that the static hardware screen has passed for planning only, but
  generated MCSDK direct PWM remains blocked. Main source findings: no direct
  `main.c` autostart was found; PC13 start/stop and MCSDK command paths can
  set `DirectCommand = MCI_START`; the state path reaches
  `R3_2_TurnOnLowSides()` and later `PWMC_SwitchOnPWM()`; the exact
  `r3_2_g4xx_pwm_curr_fdbk.c` implementation is external to the packet; TIM1
  BKIN / `nFAULT` polarity still needs closure; generated Hall pins do not
  match the accepted PCB2 Hall route; and the generation log contains PWM /
  BKIN / MotorControl invalid-parameter messages. This does not authorize
  PWM output, firmware Flash / Run / Debug, Motor Pilot, Motor Profiler,
  motor connection, power-stage readiness, or motor readiness.
- Current PCB2 no-power DMM summary result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/pcb2_no_power_dmm_continuity_short_check_result_2026-06-19.md`
  records the user-reported continuity rows as `通` for
  `CN3_10-PA0`, `CN3_11-PA1`, `CN3_12-PB4`, `CN3_2-PB3`,
  `CN3_14-3V3`, `CN3_15-GND`, and `CN3_13-PB12`, and records the
  rail / signal-to-rail / Hall-pair short-check rows as `不通`.
  Raw ohm values were not provided. This opens only no-power software Hall
  adapter interface / code-entry boundary planning; it is not powered
  readiness and does not authorize firmware implementation, flash, 24 V,
  motor connection, Gate PWM, Motor Pilot, Motor Profiler, Hall closed loop,
  or sensorless operation.
- Current post-DMM software Hall boundary:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_code_entry_boundary_after_dmm_2026-06-19.md`
  records the next allowed no-power work as software Hall adapter code-entry
  planning for `PA0 / PA1 / PB4`. It defines the future debug-only shape,
  state-machine contract, remaining GPIO / timestamp / debug-output decisions,
  and MCSDK hard stops. It does not authorize firmware implementation,
  generated-code edits, flash, 24 V, motor connection, Gate PWM, Motor Pilot,
  Motor Profiler, Hall closed loop, or sensorless operation.
- Current hardware handoff as of 2026-06-19: if the user says
  `开始单输入唤醒诊断`, `单输入唤醒`, `STDRIVE101 唤醒`, or `REG12 唤醒`, treat it as
  the STDRIVE101 single-input wake diagnostic, not Codex/mobile/service
  wakeup. Read
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_plan_2026-06-19.md`,
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_wake_official_web_review_2026-06-19.md`,
  and
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/out1_output_node_no_power_short_check_result_2026-06-19.md`
  before giving steps. Candidate diagnostic is `CN3_14 / 3V3 -> 10 kohm
  series resistor -> CN3_2 / LIN1`, motor disconnected, HSPY `24 V / 0.2 A`,
  no firmware PWM, no Motor Pilot / Profiler, no readiness claim.
- Current single-input wake baseline result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_baseline_result_2026-06-19.md`
  records `CV`, `0.036 A`, `VS / 24V_FUSED = 24 V`,
  `CN3_14 / 3V3 = 3.3 V`, `CN3_13 / nFAULT = 3.3 V`, and
  `REG12 = 0.33 V` before any `10 kohm` stimulus was installed. This is
  baseline evidence only, not a wake result.
- Current single-input wake result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_fault_result_2026-06-19.md`
  records the user-reported bounded diagnostic with
  `CN3_14 / 3V3 -> 10 kohm -> CN3_2 / LIN1`: HSPY stayed `CV`,
  current was `0.046 A`, `LIN1 = 3 V`, `REG12 = 12 V`, and
  `nFAULT = 0 V`. The user later reported post-off
  `VS / 24V_FUSED = 0 V`. Decision: `REG12` rose under the single-input
  stimulus, but `nFAULT = 0 V` is a stop-rule event; no retry, no alternate
  input stimulus, no motor, no PWM, no Motor Pilot / Profiler, and no
  powered-drive readiness claim.
- Current single-input wake retest result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_retest_clean_result_2026-06-20.md`
  records the user-reported bounded retest after gate-source pulldown rework:
  `retest_supply_state = CV`, `retest_supply_current_A = 0.048 A`,
  `retest_CN3_2_LIN1_V = 3.13 V`,
  `retest_CN3_13_nFAULT_V = 3.3 V`, and `retest_REG12_V = 12 V`.
  Recovery after removing the `10 kohm` stimulus and restoring all-inputs-low
  was `CV`, `0.045 A`, `nFAULT = 3.3 V`, and `REG12 = 0.33 V`.
  Decision: the previous `nFAULT = 0 V` wake blocker was not reproduced in
  this bounded retest, but this is still not PWM validation, motor validation,
  power-stage readiness, or motor readiness.
- Current all-inputs-low static recheck result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_all_inputs_low_static_recheck_result_2026-06-20.md`
  records the user-reported static state after the `10 kohm` wake stimulus was
  removed: HSPY `CV`, current about `0.045 A`, `CN3_1` through `CN3_6` all
  close to `0 V`, `CN3_14 / 3V3 = 3.3 V`,
  `CN3_13 / nFAULT = 3.3 V`, and `REG12 = 0.3 V`. Decision:
  standby-like recovery is confirmed after the clean `LIN1` wake retest, but
  MCU reset/default GPIO behavior, PWM safety, gate waveforms, motor behavior,
  power-stage readiness, and motor readiness remain unproven.
- Current USB-only MCU default input state result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_usbonly_mcu_default_input_state_result_2026-06-20.md`
  records the user-reported no-24V USB/ST-LINK check: `CN3_1` through
  `CN3_6` all close to `0 V`, with `P13 = 3.3 V` and `P14 = 3.3 V`
  interpreted from the requested table as `CN3_13 / nFAULT = 3.3 V` and
  `CN3_14 / 3V3 = 3.3 V`. This supports the next bounded static 24 V check
  with USB/ST-LINK connected, but it is not PWM, firmware runtime, motor,
  power-stage, or motor readiness.
- Current USB + 24 V static recheck result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_usb24_static_recheck_result_2026-06-20.md`
  records the user-reported static check with USB/ST-LINK connected and 24 V
  applied: HSPY `CV`, current about `0.045 A`, `CN3_1` through `CN3_6` all
  close to `0 V`, `CN3_14 / 3V3 = 3.3 V`,
  `CN3_13 / nFAULT = 3.3 V`, and `REG12 = 0.3 V`. This closes the immediate
  static pre-PWM screen, but it is not PWM validation, firmware runtime
  validation, gate waveform evidence, motor validation, power-stage readiness,
  or motor readiness.
- Current nFAULT cause review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_single_input_wake_nfault_cause_review_2026-06-20.md`
  ranks VDS monitoring after the `LIN1` low-side command as the primary
  review target, with REG12 sequence / accidental external REG12 tie, CP
  comparator, thermal shutdown, and external nFAULT pull-down as secondary
  targets. Next checkpoint is no-power DMM on `LIN1` and `nFAULT`, or a
  marked source packet for `SCREF`, `CP`, `REG12`, and `OUT1`; no powered
  retry is authorized.
- Current nFAULT no-power DMM result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_nfault_no_power_dmm_result_2026-06-20.md`
  records `LIN1-3V3 = 66 kohm no beep`, `LIN1-GND = 60 kohm no beep`,
  `nFAULT-3V3 = 5 kohm no beep`, and `nFAULT-GND = 10 kohm no beep`.
  Persistent CN3-side rail hard short is not indicated on `LIN1` or
  `nFAULT`. VDS monitoring after the `LIN1` low-side command remains the
  primary review target. Next checkpoint: marked source packet or confidently
  identified no-power checks for `SCREF`, `CP`, `REG12`, `OUT1`, and related
  low-side-1 gate / MOSFET nodes.
- Current STDRIVE101 marked source packet:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_fault_review_schematic_marking_2026-06-20.md`
  records marked images under `hardware/schematic/annotated/` for the
  source schematic's `CN8` / user's measured `CN3` route, `LIN1`, `nFAULT`,
  `CP`, `SCREF`, `REG12`, `OUT1`, `GHS1`, `GLS1`, Q2 low-side path, and
  ground domains. It supports the VDS-monitoring source review after the
  `LIN1` low-side command, but it is not physical probe permission for unknown
  pads and does not authorize repeat powered wake, PWM, motor, or drive
  readiness.
- Current STDRIVE101 protection-node DMM result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_nodes_no_power_dmm_result_2026-06-20.md`
  records `SCREF-3V3 = 12 kohm`, `SCREF-GND = 12 kohm`,
  `CP-GND = 1.54 Mohm` rising to about `2 Mohm` with no resistance-mode beep,
  `REG12-GND = 0.2 Mohm` rising to `0.28 Mohm`,
  `REG12-VS = 40 kohm`, `OUT1-GND = no beep`, and `OUT1-VS` diode mode `OL`
  in both directions. Stable hard short is not indicated on `CP`, `REG12`, or
  `OUT1` in the reported rows. VDS low-side path remains the primary review
  target, and the next checkpoint is no-power Q2 source / body-diode /
  gate-source path checks only if pads are confidently identified.
- Current STDRIVE101 gate-source pulldown rework result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_source_pulldown_rework_result_2026-06-20.md`
  records the user-reported final six-route readings after rework:
  `VS_OFF_V = 0 V`, `Q1_GS = 10 kohm`, `Q3_GS = 10 kohm`,
  `Q5_GS = 10 kohm`, `Q2_GS = 10 kohm`, `Q4_GS = 10 kohm`, and
  `Q6_GS = 10 kohm`, with `10k_removed = yes`. The previous gate-source
  pulldown anomaly branch is no longer indicated. A later bounded wake retest
  records `nFAULT = 3.3 V`, but no PWM, motor, power-stage, or motor readiness
  claim is opened.
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

Hardware-stage sync guard: before any hardware-adjacent next-step answer,
separate three sources: repo snapshot, user's latest现场确认, and raw
measurement evidence. If the repo snapshot says an older gate is pending but
the user states a newer现场 stage, such as `CN3 已连接 + B1 不按 +
24V/0.2A 限流静态电源/nFAULT 检查`, do not silently downgrade back to the
older gate. First state the conflict, repeat the adopted现场 stage, keep it as
a candidate stage until raw readings are recorded, and forbid any readiness
claim that lacks measurement evidence.

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
- The same audit exposes `readability_status`, which separates guarded entry
  headers from broader legacy mojibake debt so future Codex turns can tell
  "entry readability ok" apart from "full historical cleanup not claimed".
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
