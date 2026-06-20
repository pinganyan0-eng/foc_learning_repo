# Current Snapshot

Last updated: 2026-06-20

This is the short current-state page for low-token AI handoff. It summarizes
the current project stage and safety boundary. Historical detail remains in
`CURRENT_STATUS.md`.

## Current Stage

- Main project: STM32G474 edge-gateway FOC drive learning and competition
  project.
- Current stage: P2 MCSDK no-power precheck, PCB2 no-power DMM summary
  recorded, software Hall no-power firmware-entry planning, STDRIVE101
  single-input wake clean bounded retest after gate-source pulldown rework,
  post-retest all-inputs-low static recovery recheck, USB-only MCU-facing
  driver input default-state check, USB + 24 V static recheck, PWM/gate
  no-power source review, R3_2 MCSDK PWM output path source closure, manual
  gate-test firmware plan, manual gate-test lockout source package,
  manual gate-test lockout object-only target, manual gate-test lockout
  object-only build pass, and manual gate-test USB-only runtime lockout
  preparation.
- Current manual gate-test USB-only runtime lockout preparation:
  `stdrive101_manual_gate_test_usb_only_runtime_lockout_prep_2026-06-20.md`
  records Gate C preparation only. It carries forward the object-only build
  pass, source hashes, object hashes, future linked-image boundary, USB-only
  no-24V physical boundary, expected future pin readings, stop rules, and a
  user table for a later approved runtime. It does not open flash, Run /
  Debug, USB runtime execution, 24 V, Gate PWM, Motor Pilot, Motor Profiler,
  motor connection, or readiness claims. The next allowed checkpoint is a
  linked-image build-boundary plan or build-only record for the lockout image,
  still without runtime execution.
- Current manual gate-test lockout object-only build pass:
  `stdrive101_manual_gate_test_lockout_object_build_pass_2026-06-20.md`
  records a successful no-power object-only build of
  `stdrive101_gate_lockout_objects` using STM32Cube GNU Arm GCC `14.3.1` and
  Ninja `1.13.2`. The target produced only `gate_test_lockout.c.obj` and
  `main_lockout.c.obj`; no lockout ELF / HEX / BIN / MAP linked firmware image
  was produced. This does not open flash, Run / Debug, 24 V, Gate PWM, Motor
  Pilot, Motor Profiler, motor connection, or readiness claims.
- Current manual gate-test lockout object-only target:
  `stdrive101_manual_gate_test_lockout_object_target_2026-06-20.md` records a
  repo-local CMake object-library target for the isolated lockout package. It
  compiles only `gate_test_lockout.c` and `main_lockout.c` object files and
  has no ELF / HEX / BIN link target. `REPO_ROOT` was corrected and CMSIS
  headers resolve statically. CMake configure could not complete in the
  sandbox because external Ninja was blocked; the escalation path returned
  503, so no object build pass is claimed. No flash, Run / Debug, 24 V,
  Gate PWM, or motor action is authorized.
- Current manual gate-test lockout source package:
  `stdrive101_manual_gate_test_lockout_source_package_2026-06-20.md` records
  the repo-local isolated lockout source under
  `manual_gate_test_lockout_build_only_2026-06-20/`. It forces the six
  STDRIVE101 MCU-facing driver inputs low as GPIO outputs, keeps
  `PB12 / nFAULT` as input, clears TIM1 `CCER`, clears TIM1 `MOE` and
  automatic output, and leaves TIM1 break enabled. Static source grep found no
  forbidden normal MCSDK start / command-ingress / output-enable symbols in
  `Src` and `Inc`. This is source-package evidence only: no embedded build
  target yet, no flash, no Run / Debug, no 24 V, no Gate PWM, and no motor.
- Current manual gate-test firmware plan:
  `stdrive101_manual_gate_test_firmware_plan_no_power_2026-06-20.md` records
  the no-power-only plan for a future isolated lockout firmware path. Normal
  MCSDK start remains blocked. Future gate-test work must avoid
  `MC_StartMotor1`, `MCI_START`, PC13 start/stop, MCP command ingress,
  Motor Pilot, Hall closed-loop paths, speed-loop paths, and motor connection.
  This plan opens no firmware edit, build, flash, Run / Debug, 24 V, Gate PWM,
  Motor Pilot, Motor Profiler, or motor action.
- Current R3_2 source closure:
  `stdrive101_r3_2_mcsdk_pwm_output_path_source_closure_2026-06-20.md`
  records the exact local Workbench MCSDK source file and hash for
  `r3_2_g4xx_pwm_curr_fdbk.c`. The review confirms `R3_2_TurnOnLowSides()`
  treats `0` ticks as low-sides ON and calls `LL_TIM_EnableAllOutputs(TIMx)`;
  the generated state machine calls `LL_TIM_DisableBRK(TIM1)` before that
  low-side boot-cap action. Normal generated MCSDK start remains blocked for
  powered PWM. The next allowed checkpoint is a no-power-only manual gate-test
  firmware plan.
- Current PWM/gate-test source review:
  `stdrive101_pwm_gate_test_no_power_source_review_2026-06-20.md` records the
  no-power source/configuration decision that the static hardware screen is
  clean for planning only. Generated MCSDK direct PWM remains blocked because
  runtime start-command ingress exists, the start-command path reaches
  low-side / PWM routines, the exact external `r3_2_g4xx_pwm_curr_fdbk.c`
  implementation is not packet-local, TIM1 BKIN / `nFAULT` polarity is not
  closed, generated Hall pins do not match the accepted PCB2 Hall route, and
  the generation log has PWM / BKIN / MotorControl invalid-parameter messages.
  No motor, PWM output, Motor Pilot, Motor Profiler, firmware Flash / Run /
  Debug, power-stage readiness, or motor readiness is authorized.
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
  baseline condition.
- Current single-input wake result:
  `stdrive101_reg12_single_input_wake_fault_result_2026-06-19.md` records the
  user-reported bounded diagnostic with `CN3_14 / 3V3 -> 10 kohm ->
  CN3_2 / LIN1`: HSPY `CV`, `0.046 A`, `LIN1 = 3 V`, `nFAULT = 0 V`,
  `REG12 = 12 V`, and post-off `VS / 24V_FUSED = 0 V`. The diagnostic
  observed `REG12` rising, but did not pass as a clean wake condition because
  `nFAULT` was low. No retry or alternate input stimulus is allowed before
  fault-cause review.
- Current single-input wake retest result:
  `stdrive101_reg12_single_input_wake_retest_clean_result_2026-06-20.md`
  records the user-reported bounded retest after gate-source pulldown rework:
  HSPY `CV`, `0.048 A`, `LIN1 = 3.13 V`, `nFAULT = 3.3 V`, and
  `REG12 = 12 V`. Recovery after removing the `10 kohm` stimulus and returning
  all inputs low was `CV`, `0.045 A`, `nFAULT = 3.3 V`, and
  `REG12 = 0.33 V`. The previous `nFAULT = 0 V` wake blocker was not
  reproduced in this bounded retest. This is not PWM validation, motor
  validation, power-stage readiness, or motor readiness.
- Current all-inputs-low static recheck result:
  `stdrive101_all_inputs_low_static_recheck_result_2026-06-20.md` records the
  user-reported post-retest static state after the `10 kohm` wake stimulus was
  removed: HSPY `CV`, current about `0.045 A`, `CN3_1` through `CN3_6` all
  close to `0 V`, `CN3_14 / 3V3 = 3.3 V`, `CN3_13 / nFAULT = 3.3 V`, and
  `REG12 = 0.3 V`. This confirms standby-like recovery after the clean wake
  retest, but it does not prove MCU reset/default GPIO behavior, PWM safety,
  gate waveforms, motor behavior, power-stage readiness, or motor readiness.
- Current USB-only MCU default input state result:
  `stdrive101_usbonly_mcu_default_input_state_result_2026-06-20.md` records
  the user-reported no-24V USB/ST-LINK check: `CN3_1` through `CN3_6` all
  close to `0 V`, with `P13 = 3.3 V` and `P14 = 3.3 V` interpreted from the
  requested table as `CN3_13 / nFAULT = 3.3 V` and `CN3_14 / 3V3 = 3.3 V`.
  No MCU-facing STDRIVE101 input was reported high in the USB-only state. This
  is not PWM validation, firmware runtime validation, motor validation,
  power-stage readiness, or motor readiness.
- Current USB + 24 V static recheck result:
  `stdrive101_usb24_static_recheck_result_2026-06-20.md` records the
  user-reported static check with USB/ST-LINK connected and 24 V applied:
  HSPY `CV`, current about `0.045 A`, `CN3_1` through `CN3_6` all close to
  `0 V`, `CN3_14 / 3V3 = 3.3 V`, `CN3_13 / nFAULT = 3.3 V`, and
  `REG12 = 0.3 V`. This closes the immediate static pre-PWM screen, but it is
  not PWM validation, firmware runtime validation, gate waveform evidence,
  motor validation, power-stage readiness, or motor readiness.
- Current nFAULT cause review:
  `stdrive101_single_input_wake_nfault_cause_review_2026-06-20.md` records
  the no-power/source review. It ranks VDS monitoring after the `LIN1`
  low-side command as the primary review target, with REG12 sequence /
  accidental external REG12 tie, CP comparator, thermal shutdown, and
  external nFAULT pull-down as secondary targets. Next checkpoint is no-power
  DMM on `LIN1` and `nFAULT`, or a marked source packet for `SCREF`, `CP`,
  `REG12`, and `OUT1`.
- Current nFAULT no-power DMM result:
  `stdrive101_nfault_no_power_dmm_result_2026-06-20.md` records
  `LIN1-3V3 = 66 kohm no beep`, `LIN1-GND = 60 kohm no beep`,
  `nFAULT-3V3 = 5 kohm no beep`, and `nFAULT-GND = 10 kohm no beep`.
  This does not show a persistent CN3-side rail hard short on `LIN1` or
  `nFAULT`. VDS monitoring after the `LIN1` low-side command remains the
  primary review target; the next useful evidence is a marked source packet or
  confidently identified no-power protection-node checks.
- Current STDRIVE101 schematic marking:
  `stdrive101_fault_review_schematic_marking_2026-06-20.md` and the generated
  images under `hardware/schematic/annotated/` mark the source schematic's
  `CN8` / user's measured `CN3` route, `LIN1`, `nFAULT`, `CP`, `SCREF`,
  `REG12`, `OUT1`, `GHS1`, `GLS1`, Q2 low-side path, and ground domains.
  This is source-map evidence for the VDS-monitoring review only; it is not
  physical probe permission for unknown pads and does not open repeat powered
  wake, PWM, motor, or readiness.
- Current STDRIVE101 protection-node DMM result:
  `stdrive101_protection_nodes_no_power_dmm_result_2026-06-20.md` records
  `SCREF-3V3 = 12 kohm`, `SCREF-GND = 12 kohm`,
  `CP-GND = 1.54 Mohm` rising to about `2 Mohm` with no resistance-mode beep,
  `REG12-GND = 0.2 Mohm` rising to `0.28 Mohm`,
  `REG12-VS = 40 kohm`, `OUT1-GND = no beep`, and `OUT1-VS` diode mode `OL`
  both directions. Stable hard short is not indicated on `CP`, `REG12`, or
  `OUT1` in the reported rows, but the result does not prove the `nFAULT`
  cause. VDS low-side path remains the primary review target.
- Current STDRIVE101 gate-source pulldown rework result:
  `stdrive101_gate_source_pulldown_rework_result_2026-06-20.md` records
  final user-reported six-route readings after rework:
  `VS_OFF_V = 0 V`, `Q1_GS = 10 kohm`, `Q3_GS = 10 kohm`,
  `Q5_GS = 10 kohm`, `Q2_GS = 10 kohm`, `Q4_GS = 10 kohm`, and
  `Q6_GS = 10 kohm`, with `10k_removed = yes`. The previous gate-source
  pulldown anomaly branch is no longer indicated. The later bounded wake
  retest now records `nFAULT = 3.3 V`, but this still does not prove PWM,
  waveform, motor, Hall closed-loop, sensorless, power-stage, or motor
  readiness.
- The single-input wake branch now has a clean bounded retest result, but the
  project remains behind the no-motor / no-PWM boundary: no firmware PWM, no
  Motor Pilot, no Motor Profiler, no Hall closed-loop claim, no sensorless
  claim, and no power-stage or motor readiness claim.
- Current real-world blocker update: PCB2 is reported populated / in hand, the
  route is unchanged, and the 2026-06-19 no-power DMM summary is now recorded.
  After the STDRIVE101 clean wake, static recovery, USB-only default-state,
  and USB + 24 V static checks, the next work should be no-power firmware /
  source planning for a future explicit PWM/gate-test phase gate, not motor,
  PWM output, or Motor Pilot / Profiler.
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
