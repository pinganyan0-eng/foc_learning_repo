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
- Current stage: P2 MCSDK no-power precheck / Packet A generated-source review / no-power build-only Debug pass recorded / PCB2 no-power DMM summary recorded / software Hall firmware-entry plan and MCSDK speed-position boundary governance / STDRIVE101 single-input wake clean bounded retest, post-retest all-inputs-low static recovery recheck, USB-only MCU-facing driver input default-state check, USB + 24 V static recheck, PWM/gate-test no-power source review, R3_2 MCSDK PWM output path source closure, manual gate-test firmware plan, manual gate-test lockout source package, manual gate-test lockout object-only target, manual gate-test lockout object-only build pass, manual gate-test USB-only runtime lockout preparation, manual gate-test linked-image build-boundary plan, manual gate-test linked-image build-only record, manual gate-test USB-only runtime lockout phase-gate plan, manual gate-test USB-only runtime lockout execution-entry, manual gate-test USB-only runtime lockout result, manual gate-test 24V static lockout phase-gate plan, manual gate-test 24V static lockout execution-entry, manual gate-test 24V static lockout carry-forward result, gate-waveform / PWM-output no-power phase-gate plan, Gate E0 gate-waveform image design plan, Gate E1 isolated source package review, Gate E2 gate-waveform build-only record, Gate E3 USB-only neutral-state phase-gate plan, gate-waveform neutral-wrapper source review, gate-waveform neutral-wrapper build-only record, neutral-wrapper USB-only neutral-state phase-gate plan, neutral-wrapper BIN artifact record, neutral-wrapper USB-only download execution-entry, neutral-wrapper USB-only download result, neutral-wrapper USB-only DMM partial result, neutral-wrapper USB-only DMM completion result, neutral-wrapper residual-voltage isolation result, neutral-wrapper 24V static no-motor result, neutral-wrapper 24V static scope baseline result, waveform candidate BIN artifact record, waveform candidate USB-only download execution-entry, waveform candidate USB-only download result, waveform candidate USB-only DMM result, waveform candidate residual-voltage isolation result, waveform candidate 24V static scope no-waveform result, open-loop CN3 no-waveform correction, open-loop no-rotation result, PA7 LIN1 wake nFAULT 1.3V fault-isolation result, host-side sensorless speed-loop hold registration, host-side signed reverse speed/current command fixture registration, MCSDK / host-side signed reverse speed command snapshot sequence bridge registration, host-side signed reverse target-omega rate-limit replay registration, host-side positive-to-reverse target-omega rate-limit replay plus main-agent priority matrix registration, host-side positive-to-reverse target-omega loss/relock replay registration, host-side reverse target-omega startup hold registration, and host-side reverse target-omega lock-threshold handoff registration recorded.
- Current host-side FOC algorithm model:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_foc_algorithm_model_review_2026-06-22.md`
  records `src/foc_core_model.py` and `tests/test_foc_core_model.py` as
  host-side no-power FOC math evidence only. Decision:
  `Host-side no-power FOC algorithm model / no firmware implementation / no
  MCSDK integration / no PWM output / no motor readiness`. It covers Clarke,
  inverse Clarke, Park, inverse Park, host-side SVPWM-style duty calculation,
  PI anti-windup, prior-integrator clamping, and one current-loop step. MCSDK
  remains the intended framework generation path; this model is not firmware,
  not a timer driver, not MCSDK hook evidence, not Gate PWM validation, not
  Hall closed-loop, not sensorless / SMO validation, not power-stage
  readiness, and not motor readiness.
- Current host-side FOC golden vectors:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_foc_golden_vectors_review_2026-06-22.md`
  records `tests/fixtures/foc_core_golden_vectors.json` and
  `tests/test_foc_core_vectors.py` as host-side no-power FOC math regression
  fixtures. Decision: `Host-side no-power FOC golden vectors / no firmware
  implementation / no MCSDK integration / no PWM output / no motor readiness`.
  The vectors replay transform, PI, host-side SVPWM-style duty, and
  current-loop behavior against the Python model only. They are not proof that
  MCSDK generated code uses the same sign/scaling convention, not compare
  register evidence, not Gate PWM validation, not MCSDK hook readiness, not
  power-stage readiness, and not motor readiness.
- Current MCSDK / host-side FOC math comparison boundary plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_host_side_foc_math_comparison_boundary_plan_2026-06-22.md`
  records a host-side no-power comparison plan only, plus
  `tests/test_mcsdk_foc_pipeline_static.py` as a static check of the archived
  generated-source FOC pipeline. Decision: `MCSDK host-side FOC math
  comparison boundary plan / no firmware implementation / no MCSDK
  integration / no PWM output / no motor readiness`. MCSDK remains the
  intended motor-control framework generation path. This plan is not MCSDK
  convention proof, not compare-register evidence, not Gate PWM validation,
  not power-stage readiness, and not motor readiness.
- Current MCSDK FOC convention probe translation table:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_foc_convention_probe_translation_table_2026-06-22.md`
  records a host-side no-power generated-source convention mapping only, plus
  `tests/test_mcsdk_foc_convention_probe.py` as static protection for
  source-backed rows around Clarke, qd field order, Park / reverse-Park,
  fixed-point angle representation, PI divisors, circle limitation, and
  timer-count PWM representation. Decision: `MCSDK FOC convention probe /
  translation table / host-side no-power generated-source convention mapping
  only / no firmware implementation / no generated-code edit / no MCSDK
  integration / no PWM output / no motor readiness`. It is not MCSDK
  convention proof beyond explicitly source-backed rows, not host-side / MCSDK
  numerical equivalence evidence, not compare-register evidence, not Gate PWM
  validation, not MCSDK hook readiness, not hardware validation, not
  power-stage readiness, and not motor readiness.
- Current host-side sensorless frontend contract:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_sensorless_frontend_review_2026-06-22.md`
  records `src/foc_sensorless_frontend.py`,
  `tests/fixtures/foc_sensorless_frontend_vectors.json`,
  `tests/test_foc_sensorless_frontend.py`, and
  `tests/test_foc_sensorless_frontend_vectors.py` as host-side no-power
  sensorless frontend contract evidence only. Decision:
  `Host-side no-power sensorless frontend contract / no firmware implementation / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It freezes a host-float `theta_e_rad` producer seam, startup-versus-tracking
  mode behavior, confidence-based lock, and observer angle-step limiting only.
  It is not firmware, not MCSDK observer equivalence proof, not generated-code
  edit permission, not compare-register evidence, not Gate PWM validation, not
  sensorless / SMO validation, not power-stage readiness, and not motor
  readiness.
- Current host-side sensorless observer stub:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_sensorless_observer_stub_review_2026-06-22.md`
  records an extension of `src/foc_sensorless_frontend.py`,
  `tests/fixtures/foc_sensorless_frontend_vectors.json`,
  `tests/test_foc_sensorless_frontend.py`, and
  `tests/test_foc_sensorless_frontend_vectors.py` as host-side no-power
  observer-stub evidence only. Decision:
  `Host-side no-power sensorless observer stub / alpha-beta back-EMF contract only / no firmware implementation / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It adds a deterministic host-float alpha-beta back-EMF stub that consumes
  `v_alpha`, `v_beta`, `i_alpha`, and `i_beta` to produce bounded
  `theta_e_rad`, `omega_e_rad_s`, and confidence values for the existing
  frontend lock contract. It is not firmware, not MCSDK Observer PLL
  equivalence, not MCSDK Observer CORDIC equivalence, not SMO implementation
  or validation, not MCSDK integration, not host-side / MCSDK numerical
  equivalence evidence, not compare-register evidence, not Gate PWM
  validation, not sensorless / SMO validation, not power-stage readiness, and
  not motor readiness.
- Current host-side sensorless replay sequence:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_sensorless_replay_sequence_review_2026-06-22.md`
  records a further extension of `src/foc_sensorless_frontend.py`,
  `tests/fixtures/foc_sensorless_frontend_vectors.json`,
  `tests/test_foc_sensorless_frontend.py`, and
  `tests/test_foc_sensorless_frontend_vectors.py` as host-side no-power
  replay-sequence evidence only. Decision:
  `Host-side no-power sensorless multi-step replay / observer-frontend-current-loop state-continuity fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It adds `sensorless_current_control_replay_sequence(...)` to carry
  observer, frontend, and PI state handoff across a short host-side sequence,
  and the fixture now covers low-confidence startup, observer lock, continued
  tracking, and PI integrator carryover. It is not firmware, not MCSDK
  Observer PLL equivalence, not MCSDK Observer CORDIC equivalence, not SMO
  implementation or validation, not MCSDK integration, not host-side / MCSDK
  numerical equivalence evidence, not compare-register evidence, not Gate PWM
  validation, not sensorless / SMO validation, not power-stage readiness, and
  not motor readiness.
- Current host-side sensorless startup policy replay:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_sensorless_startup_policy_replay_review_2026-06-22.md`
  records a host-side no-power lock/loss/relock policy layer on top of the
  sensorless replay path. Decision:
  `Host-side no-power sensorless startup policy replay / lock-loss-relock fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It adds `SensorlessStartupPolicyConfig`, `SensorlessStartupPolicyState`,
  `SensorlessStartupPolicyResult`, and `sensorless_startup_policy_step(...)`
  so replay can require consecutive high-confidence samples before tracking,
  require consecutive low-confidence samples before loss, then return through
  startup ramp and relock while carrying PI state. It is not firmware, not a
  firmware startup state machine, not MCSDK Observer PLL equivalence, not
  MCSDK Observer CORDIC equivalence, not SMO implementation or validation, not
  MCSDK integration, not host-side / MCSDK numerical equivalence evidence, not
  compare-register evidence, not Gate PWM validation, not sensorless / SMO
  validation, not power-stage readiness, and not motor readiness.
- Current host-side reverse target-omega lock-threshold handoff:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_reverse_target_omega_lock_threshold_handoff_review_2026-06-24.md`
  records a host-side no-power startup / unlocked threshold handoff fixture.
  Decision:
  `Host-side no-power reverse target-omega lock-threshold handoff / startup-unlocked threshold fixture only / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It freezes the existing `SensorlessStartupPolicyConfig.lock_count_required`,
  `SensorlessSpeedLoopConfig.hold_when_unlocked`, and
  `SensorlessSpeedLoopConfig.target_omega_rate_limit_e_rad_s2` behavior when a
  startup / unlocked frontend state still carries a prior `+20.0` rad/s
  target, receives a `-20.0` rad/s command, and requires three lock-candidate
  samples before tracking is enabled. The protected frontend fixture
  `reverse_target_omega_lock_threshold_handoff_starts_ramp_only_at_lock`
  records `speed_loop_target_omega` as
  `[20.0, 20.0, 20.0, 15.0, 10.0]`,
  `effective_target_iq` as `[0.0, 0.0, 0.0, 1.5, 1.5]`,
  `locked` as `[false, false, false, true, true]`, and
  `lock_candidate_count` as `[0, 1, 2, 3, 3]`. The companion bridge fixture
  `reverse_target_omega_lock_threshold_handoff_steps_map_to_q15` freezes
  `target_omega_q15` as `[32767, 32767, 32767, 24576, 16384]`,
  `measured_omega_q15` as `[1638, 3277, 4915, -16384, -16384]`,
  `requested_iq_q15` as `[0, 0, 0, 32767, 32767]`, and
  `effective_iq_q15` as `[0, 0, 0, 24576, 24576]`. This is not firmware, not
  generated-code edit permission, not MCSDK integration, not MCSDK numerical
  equivalence, not MCSDK speed-loop hook evidence, not firmware speed-loop
  behavior, not firmware current limiting, not a firmware reverse-startup
  strategy, not reverse open-loop startup validation, not Gate PWM validation,
  not sensorless / SMO validation, not power-stage readiness, and not motor
  readiness.
- Upstream host-side reverse target-omega startup hold:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_reverse_target_omega_startup_hold_review_2026-06-24.md`
  records a host-side no-power startup / unlocked target-freeze fixture.
  Decision:
  `Host-side no-power reverse target-omega startup hold / startup-unlocked target freeze fixture only / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It freezes the existing `SensorlessSpeedLoopConfig.hold_when_unlocked` and
  `SensorlessSpeedLoopConfig.target_omega_rate_limit_e_rad_s2` behavior when a
  startup / unlocked frontend state still carries a prior `+20.0` rad/s
  target and receives a `-20.0` rad/s command. The protected frontend fixture
  `reverse_target_omega_remains_frozen_until_lock_not_startup_strategy`
  records `speed_loop_target_omega` as
  `[20.0, 20.0, 15.0, 10.0, 5.0]`,
  `effective_target_iq` as `[0.0, 0.0, 1.5, 1.5, 1.5]`,
  `locked` as `[false, false, true, true, true]`, and
  `lock_candidate_count` as `[0, 1, 2, 2, 2]`. The companion bridge fixture
  `reverse_target_omega_startup_hold_steps_map_to_q15` freezes
  `target_omega_q15` as `[32767, 32767, 24576, 16384, 8192]`,
  `measured_omega_q15` as `[1638, 3277, -16384, -16384, -16384]`,
  `requested_iq_q15` as `[0, 0, 32767, 32767, 32767]`, and
  `effective_iq_q15` as `[0, 0, 24576, 24576, 24576]`. This is not firmware,
  not generated-code edit permission, not MCSDK integration, not MCSDK
  numerical equivalence, not firmware speed-loop behavior, not firmware
  current limiting, not a firmware reverse-startup strategy, not reverse
  open-loop startup validation, not Gate PWM validation, not sensorless / SMO
  validation, not power-stage readiness, and not motor readiness.
- Current host-side positive-to-reverse target-omega loss/relock replay:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_positive_to_reverse_target_omega_loss_relock_replay_review_2026-06-24.md`
  records a host-side no-power command-ramp hold-loss-relock fixture.
  Decision:
  `Host-side no-power positive-to-reverse target-omega loss/relock replay / command-ramp hold-loss-relock fixture only / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It freezes the existing
  `SensorlessSpeedLoopConfig.target_omega_rate_limit_e_rad_s2` and
  `_ramp_target_omega(...)` behavior when an already tracking `+20.0` rad/s
  target state receives `-20.0` rad/s, loses observer confidence, holds
  target omega at zero during confirmed loss, then resumes negative ramping
  after relock. The protected frontend fixture
  `positive_to_reverse_target_omega_rate_limit_holds_during_loss_and_relock`
  records `speed_loop_target_omega` as
  `[15.0, 10.0, 5.0, 0.0, 0.0, 0.0, -5.0, -10.0]`,
  `effective_target_iq` as
  `[1.25, 0.75, 0.0, -1.0, 0.0, 0.0, -1.5, -1.5]`,
  `locked` as `[true, true, true, true, false, false, true, true]`, and
  final `speed_loop_state.target_omega_e_rad_s = -10.0`. The companion bridge
  fixture
  `positive_to_reverse_target_omega_rate_limit_loss_relock_steps_map_to_observer_snapshots`
  maps the same replay through
  `sensorless_replay_to_mcsdk_observer_snapshots(...)` and freezes
  `theta_q15` as
  `[10430, 11473, 12516, 13559, 25033, -27987, 27119, 17732]`,
  `omega_q15` as
  `[16384, 16384, 16384, 16384, 18022, 19661, 16384, 16384]`, and
  `confidence_q15` as `[31130, 31130, 31130, 3277, 0, 0, 31130, 31130]`.
  The companion speed/current bridge fixture
  `positive_to_reverse_target_omega_rate_limit_loss_relock_steps_map_to_q15`
  maps the same replay through
  `sensorless_replay_to_mcsdk_speed_command_snapshots(...)` and freezes
  `target_omega_q15` as
  `[24576, 16384, 8192, 0, 0, 0, -8192, -16384]`,
  `requested_iq_q15` as
  `[20480, 12288, 0, -16384, 0, 0, -24576, -32768]`, and
  `effective_iq_q15` as
  `[20480, 12288, 0, -16384, 0, 0, -24576, -24576]`. This is not firmware,
  not generated-code edit permission, not MCSDK integration, not firmware
  speed-loop behavior, not firmware current limiting, not a firmware
  direction reversal strategy, not an active MCSDK observer instance, not
  MCSDK numerical equivalence, not Gate PWM validation, not sensorless / SMO
  validation, not power-stage readiness, and not motor readiness.
- Upstream host-side positive-to-reverse target-omega rate-limit replay:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_positive_to_reverse_target_omega_rate_limit_replay_review_2026-06-23.md`
  records a host-side no-power command-ramp crossing fixture. Decision:
  `Host-side no-power positive-to-reverse target-omega rate-limit replay / command-ramp crossing fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It freezes the existing
  `SensorlessSpeedLoopConfig.target_omega_rate_limit_e_rad_s2` and
  `_ramp_target_omega(...)` behavior when an already locked `+20.0` rad/s
  target state receives `-20.0` rad/s and crosses through zero. The protected
  frontend fixture
  `positive_to_reverse_target_omega_rate_limit_crosses_zero_while_locked`
  records `speed_loop_target_omega` as
  `[15.0, 10.0, 5.0, 0.0, -5.0, -10.0, -15.0, -20.0]`,
  `speed_loop_target_iq` as
  `[1.25, 0.75, 0.0, -1.0, -1.5, -2.0, -2.0, -2.0]`, and
  `q_axis_integrator` as
  `[1.25, 2.0, 2.0, 1.0, -0.5, -2.0, -3.5, -5.0]`.
  The companion bridge fixture
  `positive_to_reverse_target_omega_rate_limit_crossing_steps_map_to_q15`
  maps the same replay through
  `sensorless_replay_to_mcsdk_speed_command_snapshots(...)` and freezes
  `target_omega_q15` as
  `[24576, 16384, 8192, 0, -8192, -16384, -24576, -32768]`,
  `requested_iq_q15` as
  `[20480, 12288, 0, -16384, -24576, -32768, -32768, -32768]`, and
  `effective_iq_q15` as
  `[20480, 12288, 0, -16384, -24576, -24576, -24576, -24576]`. This is not
  firmware, not generated-code edit permission, not MCSDK integration, not
  firmware speed-loop behavior, not firmware current limiting, not a firmware
  direction reversal strategy, not MCSDK numerical equivalence, not Gate PWM
  validation, not sensorless / SMO validation, not power-stage readiness, and
  not motor readiness.
- Current main-agent priority matrix:
  `workflow/main_agent_priority_matrix_2026-06-23.md` records P0 sensorless
  host-side command/replay semantics and evidence registration, P1
  source-backed MCSDK sensorless boundary review and STDRIVE101 no-power
  fault-tree input, and P2 firmware-entry planning / presentation only after
  stronger evidence. This is workflow planning only and opens no firmware or
  hardware action.
- Current host-side signed reverse target-omega rate-limit replay:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_signed_reverse_target_omega_rate_limit_replay_review_2026-06-23.md`
  records a host-side no-power command-ramp fixture. Decision:
  `Host-side no-power signed reverse target-omega rate-limit replay / command-ramp fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It freezes the existing
  `SensorlessSpeedLoopConfig.target_omega_rate_limit_e_rad_s2` and
  `_ramp_target_omega(...)` behavior across a signed reverse
  lock/loss/relock replay. The protected frontend fixture
  `signed_reverse_target_omega_rate_limit_holds_until_lock_and_after_loss`
  records `speed_loop_target_omega` as
  `[0.0, 0.0, -5.0, -10.0, -15.0, -15.0, -15.0, -20.0]`,
  `speed_loop_target_iq` as
  `[0.0, 0.0, 0.75, 0.25, -0.5, 0.0, 0.0, -1.5]`, and
  `q_axis_integrator` as
  `[0.0, 0.0, 0.75, 1.0, 0.5, 0.5, 0.5, -1.0]`.
  The companion bridge fixture
  `signed_reverse_target_omega_rate_limit_replay_steps_map_to_q15` maps the
  same replay through
  `sensorless_replay_to_mcsdk_speed_command_snapshots(...)` and freezes
  `target_omega_q15` as
  `[0, 0, -8192, -16384, -24576, -24576, -24576, -32768]`,
  `requested_iq_q15` as
  `[0, 0, 12288, 4096, -8192, 0, 0, -24576]`, and
  `effective_iq_q15` as
  `[0, 0, 12288, 4096, -8192, 0, 0, -24576]`. This is not firmware, not
  generated-code edit permission, not MCSDK integration, not firmware
  speed-loop behavior, not firmware current limiting, not a firmware
  reverse-startup strategy, not MCSDK numerical equivalence, not Gate PWM
  validation, not sensorless / SMO validation, not power-stage readiness, and
  not motor readiness.
- Current host-side signed reverse speed/current command fixture:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_signed_reverse_speed_current_command_fixture_review_2026-06-23.md`
  records a host-side no-power signed reverse speed/current command fixture.
  Decision:
  `Host-side no-power signed reverse speed/current command fixture / signed speed and iq replay only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It freezes the existing host-side signed speed/current path: negative
  `target_omega_e_rad_s` produces negative speed-loop error, negative
  candidate `iq_ref`, symmetric locked current-command clamp, negative
  effective `iq_ref`, negative q-axis current-loop PI movement, and signed
  MCSDK-shaped comparison metadata. The protected fixture
  `signed_reverse_speed_current_command_holds_until_lock_and_after_loss`
  records `speed_loop_target_iq` as
  `[0.0, 0.0, -1.5, -2.0, -2.0, 0.0, 0.0, -2.0]`,
  `speed_loop_pi_integrator` as
  `[0.0, 0.0, -0.5, -1.0, -1.0, -1.0, -1.0, -1.0]`, and
  `q_axis_integrator` as
  `[0.0, 0.0, -1.5, -3.0, -4.5, -4.5, -4.5, -6.0]`. This is not firmware,
  not a firmware reverse-startup strategy, not MCSDK integration, not MCSDK
  numerical equivalence, not Gate PWM validation, not sensorless / SMO
  validation, not power-stage readiness, and not motor readiness.
- Current MCSDK / host-side signed reverse speed command snapshot sequence
  bridge:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_host_side_signed_reverse_speed_command_snapshot_sequence_bridge_review_2026-06-23.md`
  records a host-side no-power replay-step semantic translation fixture.
  Decision:
  `MCSDK host-side signed reverse speed command snapshot sequence bridge / host-side no-power replay-step semantic translation only / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It adds `sensorless_replay_speed_command_snapshot_sequence_cases` to
  `tests/fixtures/foc_mcsdk_bridge_vectors.json` and verifies
  `sensorless_replay_to_mcsdk_speed_command_snapshots(...)` over the full
  signed reverse replay as MCSDK-shaped q15 speed/current metadata. The
  protected fixture `signed_reverse_speed_command_replay_steps_map_to_q15`
  freezes `target_omega_q15` as
  `[0, 0, -32768, -32768, -32768, -32768, -32768, -32768]`,
  `measured_omega_q15` as
  `[1638, 3277, -16384, -16384, -16384, -14746, -13107, -16384]`,
  `requested_iq_q15` as
  `[0, 0, -24576, -32768, -32768, 0, 0, -32768]`, and
  `effective_iq_q15` as
  `[0, 0, -24576, -24576, -24576, 0, 0, -24576]`. This is not firmware, not
  generated-code edit permission, not MCSDK integration, not MCSDK numerical
  equivalence, not firmware speed-loop behavior, not firmware current
  limiting, not sensorless / SMO validation, not Gate PWM validation, not
  power-stage readiness, and not motor readiness.
- Earlier host-side sensorless speed-loop hold:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_sensorless_speed_loop_hold_review_2026-06-22.md`
  records a host-side no-power lock-aware PI anti-windup fixture only.
  Decision:
  `Host-side no-power sensorless speed-loop hold / lock-aware PI anti-windup fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It adds `SensorlessSpeedLoopConfig.hold_when_unlocked`, extends
  `sensorless_speed_loop_step(...)` with an `enabled` argument, and calls
  `sensorless_speed_loop_step(..., enabled=frontend.locked)` so the replay
  can freeze the host-side speed PI while startup / unlocked /
  confirmed-loss steps cannot pass current. The protected fixture
  `speed_loop_pi_holds_until_lock_and_after_loss` uses nonzero `ki=0.5`,
  freezes `speed_loop_pi_integrator` as
  `[0.0, 0.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0]`, and keeps q-axis current-loop
  integrator movement tied to effective `iq_ref` pass-through. This is not
  firmware, not MCSDK Observer PLL equivalence, not MCSDK Observer CORDIC
  equivalence, not SMO implementation or validation, not MCSDK integration,
  not compare-register evidence, not Gate PWM validation, not sensorless /
  SMO validation, not power-stage readiness, and not motor readiness.
- Current host-side sensorless locked-theta shortest-path blend:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_sensorless_locked_theta_shortest_path_blend_review_2026-06-22.md`
  records a host-side no-power wrap-boundary fix in
  `sensorless_observer_contract_step(...)`. Decision:
  `Host-side no-power sensorless locked-theta shortest-path blend / wrap-boundary tracking fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It ensures locked tracking blends the observer angle along
  `_shortest_angle_delta_rad(...)` before applying `lock_blend_factor`, so a
  previous angle near `6.1 rad` and observer angle near `0.1 rad` stay near
  the wrap boundary instead of jumping toward `pi`. This is not firmware, not
  MCSDK Observer PLL equivalence, not MCSDK Observer CORDIC equivalence, not
  SMO implementation or validation, not MCSDK integration, not
  compare-register evidence, not Gate PWM validation, not sensorless / SMO
  validation, not power-stage readiness, and not motor readiness.
- Current host-side sensorless speed / current command policy replay:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_sensorless_speed_current_command_policy_replay_review_2026-06-22.md`
  records a host-side no-power speed-loop and lock-aware current-command
  policy layer on top of the sensorless replay path. Decision:
  `Host-side no-power sensorless speed/current command policy replay / lock-aware iq gating fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It adds `SensorlessSpeedLoopConfig`, `SensorlessSpeedLoopState`,
  `SensorlessSpeedLoopResult`, `sensorless_speed_loop_step(...)`,
  `SensorlessCurrentCommandPolicyConfig`,
  `SensorlessCurrentCommandPolicyResult`,
  `sensorless_current_command_policy_step(...)`, and MCSDK-shaped
  `McsdkSpeedCommandSnapshot` translation so replay can generate a candidate
  `iq_ref` from target/measured electrical speed, then clamp or zero the
  effective command while startup / unlocked / confirmed-loss steps are not
  allowed to pass current in the fixture. It is not firmware, not a firmware
  speed loop, not a firmware startup or loss-protection strategy, not MCSDK
  Observer PLL equivalence, not MCSDK Observer CORDIC equivalence, not SMO
  implementation or validation, not MCSDK integration, not host-side / MCSDK
  numerical equivalence evidence, not compare-register evidence, not Gate PWM
  validation, not sensorless / SMO validation, not power-stage readiness, and
  not motor readiness.
- Current MCSDK / host-side FOC comparison bridge:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_host_side_foc_comparison_bridge_review_2026-06-22.md`
  records `src/foc_mcsdk_bridge.py`,
  `tests/fixtures/foc_mcsdk_bridge_vectors.json`, and
  `tests/test_mcsdk_foc_bridge_vectors.py` as host-side no-power comparison
  bridge evidence only. Decision: `MCSDK host-side FOC comparison bridge /
  host-side no-power semantic translation only / no firmware implementation /
  no generated-code edit / no MCSDK integration / no PWM output / no motor
  readiness`. It fixes comparison-ready translation rules for q/d field order,
  q1.15 angle-domain mapping, and duty-to-count representation only. It is not
  MCSDK convention proof, not host-side / MCSDK numerical equivalence
  evidence, not compare-register evidence, not Gate PWM validation, not MCSDK
  hook readiness, not hardware validation, not power-stage readiness, and not
  motor readiness.
- Current MCSDK / host-side sensorless observer snapshot bridge:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_host_side_sensorless_observer_snapshot_bridge_review_2026-06-22.md`
  records a downstream extension of `src/foc_mcsdk_bridge.py`,
  `tests/fixtures/foc_mcsdk_bridge_vectors.json`, and
  `tests/test_mcsdk_foc_bridge_vectors.py` as host-side no-power semantic
  translation only. Decision:
  `MCSDK host-side sensorless observer snapshot bridge / host-side no-power semantic translation only / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It maps host-side sensorless `theta_e_rad`, `omega_e_rad_s`, confidence,
  mode, and lock state into `theta_q15`, `omega_q15`, `confidence_q15`, mode,
  and locked comparison metadata only. It is not firmware, not MCSDK Observer
  PLL equivalence, not MCSDK Observer CORDIC equivalence, not SMO
  implementation or validation, not MCSDK integration, not host-side / MCSDK
  numerical equivalence evidence, not compare-register evidence, not Gate PWM
  validation, not sensorless / SMO validation, not power-stage readiness, and
  not motor readiness.
- Current MCSDK / host-side sensorless observer snapshot sequence bridge:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_host_side_sensorless_observer_snapshot_sequence_bridge_review_2026-06-22.md`
  records `sensorless_replay_to_mcsdk_observer_snapshots(...)` in
  `src/foc_mcsdk_bridge.py`, plus
  `tests/fixtures/foc_mcsdk_bridge_vectors.json` and
  `tests/test_mcsdk_foc_bridge_vectors.py`, as host-side no-power replay-step
  semantic translation only. Decision:
  `MCSDK host-side sensorless observer snapshot sequence bridge / host-side no-power replay-step semantic translation only / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  It maps every `SensorlessReplayResult` step into `McsdkObserverSnapshot`
  metadata so startup ramp, pending lock, tracking, short confidence dip,
  confirmed loss, startup after loss, and relock can be compared as q15-shaped
  host-side snapshots. It is not firmware, not MCSDK Observer PLL equivalence,
  not MCSDK Observer CORDIC equivalence, not SMO implementation or validation,
  not MCSDK integration, not host-side / MCSDK numerical equivalence evidence,
  not compare-register evidence, not Gate PWM validation, not sensorless / SMO
  validation, not power-stage readiness, and not motor readiness.
- Current MCSDK sensorless observer generated-source boundary:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_sensorless_observer_generated_source_boundary_review_2026-06-22.md`
  records `tests/test_mcsdk_sensorless_observer_boundary_static.py` as a
  no-power generated-source boundary check for the archived 2026-05-27 MCSDK
  source snapshot. Decision:
  `MCSDK sensorless observer generated-source boundary / Hall generated-source boundary confirmed / generic CORDIC and STO register symbols noted / no active MCSDK observer instance / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.
  The source-backed boundary is: the generated snapshot uses
  `MotorControl.M1_SPEED_SENSOR=HALL_SENSOR`,
  `MotorControl.SPEED_SENSOR_SELECTION=HALL_SENSORS`, `HALL_M1`,
  `HALL_Init (&HALL_M1);`, and
  `STC_Init(pSTC[M1],&PIDSpeedHandle_M1, &HALL_M1._Super);`. Generic
  `CORDIC_CONFIG_PHASE`, `MCM_PhaseComputation`, `MC_REG_STOPLL_*`, and
  `MC_REG_STOCORDIC_*` symbols are present, but they are not an active MCSDK
  observer instance. This is not firmware implementation, not generated-code
  edit permission, not MCSDK Observer PLL equivalence, not MCSDK Observer
  CORDIC equivalence, not SMO implementation or validation, not MCSDK
  integration, not sensorless validation, not Gate PWM validation, not
  power-stage readiness, and not motor readiness.
- Current STDRIVE101 nFAULT 1.3V fault-tree no-power plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_nfault_1v3_fault_tree_no_power_plan_2026-06-22.md`
  consolidates the PA7 / LIN1 wake fault-isolation result, earlier nFAULT
  cause review, schematic marking, and protection-node no-power DMM result.
  Decision: `STDRIVE101 nFAULT 1.3V fault-tree no-power plan /
  power-board-side fault localized / no-power source and photo evidence only /
  HIN1 comparison remains future teacher-reviewed phase gate / no repeat
  powered wake / no PWM output / no motor readiness`. The primary working
  branch remains `LIN1 / GLS1 / Q2 / OUT1` low-side phase-U VDS or output-path
  behavior, but common protection / `CP` / `SCREF` / `REG12` / soldering /
  chip causes remain unresolved. This opens no repeat 24 V wake, no `HIN1`
  comparison execution, no Gate PWM output, no Motor Pilot / Profiler, no motor
  connection, no power-stage readiness, and no motor readiness.
- Current STDRIVE101 nFAULT fault-tree retrieval coverage:
  `tools/search_local_v2.py`, `retrieval_eval/queries.json`, and
  `tests/test_search_local_v2.py` now include targeted coverage for
  `STDRIVE101 nFAULT 1.3V fault-tree`, `HIN1`, and `no repeat powered wake`
  queries. Decision: `STDRIVE101 nFAULT fault-tree retrieval coverage /
  latest safety-critical boundary searchable / no hardware validation`. This
  is source-finding workflow evidence only; it does not validate hardware,
  authorize `HIN1` comparison, repeat powered wake, Gate PWM output, Motor
  Pilot / Profiler, power-stage readiness, or motor readiness.
- Current PA7 LIN1 wake nFAULT 1.3V fault-isolation result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_pa7_lin1_wake_nfault_1v3_fault_isolation_result_2026-06-21.md`
  records the user-reported return to the minimal PA7 hold-high diagnostic.
  `PA7 / CN10-15 = 3.3 V`, `CN8 P2 / LIN1 = 3.3 V`,
  `VS / 24V_FUSED = 24 V`, and `REG12 = 12 V`, but `nFAULT` remained
  `1.3 V` on both `CN8 P13` and `NUCLEO CN10-16`; after disconnecting the
  `nFAULT -> PB12` wire, power-board `CN8 P13` still measured `1.3 V`.
  User corrected the R3 checks to `R3 = 10 kohm`, R3 3V3 endpoint continuity
  to `CN8 P14 = 0 ohm`, and R3 nFAULT endpoint continuity to `CN8 P13 =
  0 ohm`, so the R3 pull-up value and NUCLEO PB12 are not the primary
  blockers. Current working hypothesis is a power-board-side STDRIVE101 fault
  state, with `LIN1 / GLS1 / Q2 / OUT1` low-side phase-U VDS or related
  output path as the primary review target. This opens no repeated motor run,
  no Motor Pilot, no Motor Profiler, no power-stage readiness, and no motor
  readiness.
- Current gate-waveform candidate 24V static scope no-waveform result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_24v_static_scope_no_waveform_result_2026-06-21.md`
  records the user-reported oscilloscope check on the six STDRIVE101
  MCU-facing driver inputs with the waveform candidate image on the board,
  HSPY at 24 V, and the motor disconnected. User reported no waveform on
  `CN3_1 / CN3_2`, no waveform on `CN3_3 / CN3_4`, and no waveform on
  `CN3_5 / CN3_6`; HSPY stayed `CV` at `0.036 A`; `nFAULT = 3.3 V`; no
  abnormal board symptom was reported. This is bounded no-motor oscilloscope
  evidence only. It opens no Motor Pilot, no Motor Profiler, no motor
  connection, no Hall closed loop, no sensorless operation, no power-stage
  readiness, and no motor readiness. Do not repeat this same check unless the
  image, wiring, board condition, trigger method, measurement setup, or
  observed value changes.
- Current gate-waveform candidate residual-voltage isolation result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_residual_voltage_isolation_result_2026-06-21.md`
  records the bounded isolation follow-up after the waveform candidate
  USB-only DMM result reported `VS / 24V_FUSED = 2 V` and `REG12 = 0.3 V`.
  User confirmed USB / ST-LINK disconnected, HSPY / 24 V OFF and physically
  disconnected, motor disconnected, no `10 kohm` wake resistor or LIN1
  stimulus installed, and DMM black probe on GND. User confirmed
  `VS / 24V_FUSED = 0 V` and `REG12 = 0 V`. Decision: the earlier candidate
  USB-only `VS / 24V_FUSED = 2 V` cleared after USB disconnect, so persistent
  VS backfeed is not indicated in this candidate isolation check and the
  immediate residual-voltage blocker is cleared only. This opens no 24 V
  command from this record, no Run / Debug, no Gate PWM output, no Motor Pilot
  / Profiler, no motor connection, and no readiness claim. Next checkpoint may
  only be a separate candidate 24 V static no-motor phase-gate or execution
  entry with fresh preconditions, not motor power-up.
- Current gate-waveform candidate USB-only DMM result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_usb_only_dmm_result_2026-06-21.md`
  records the user-reported post-download USB-only DMM readings after the
  waveform candidate image copy. The user reported `CN3_1` through `CN3_6`
  all `0 V`, `CN3_13 = 3 V`, `CN3_14 = 3 V`,
  `VS / 24V_FUSED = 2 V`, and `REG12 = 0.3 V`. Board heat / smell / sound /
  reset-loop status was not reported in this latest row. The six driver-input
  stop-rule was not hit, but the voltage-boundary stop condition is active
  because `VS / 24V_FUSED = 2 V` is above the prior `< 1 V` USB-only
  boundary. This is not a pass for upward hardware progression and opens no
  Run / Debug, no 24 V command, no Gate PWM output, no Motor Pilot / Profiler,
  no motor connection, and no readiness claim. Its live checkpoint is
  superseded by the later waveform candidate residual-voltage isolation
  result, which records `VS / 24V_FUSED = 0 V` and `REG12 = 0 V` after
  USB / ST-LINK disconnect.
- Current gate-waveform candidate USB-only download result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_usb_only_download_result_2026-06-21.md`
  records one authorized USB-only ST-LINK mass-storage copy of the waveform
  candidate BIN. User authorization was `允许复制 candidate BIN 到 D:`. The
  copied BIN SHA256 was
  `362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31`, size
  `1852` bytes. `D:` was `NOD_G474RE`; `D:\FAIL.TXT` was absent before and
  after copy; the target BIN was not retained after copy, consistent with
  ST-LINK mass-storage consumption; `DETAILS.TXT` reported
  `Version: V3J17M10` and `Build: Oct 17 2025 15:12:06`. The board image is
  now treated as the waveform candidate image for the next bounded checks.
  This download record itself contained no post-download CN3 / REG12 DMM
  result and no measured waveform result. Because the candidate image calls
  `gate_waveform_candidate_run_once()` once after reset and then holds idle
  low, this record does not prove absence of a boot-time output transition.
  It opens no Run / Debug, no 24 V command, no Motor Pilot / Profiler, no motor
  connection, and no readiness claim. Its live checkpoint is superseded by the
  later waveform candidate residual-voltage isolation result, which clears the
  immediate residual-voltage blocker only and changes the next checkpoint to a
  separate candidate 24 V static no-motor phase-gate or execution entry.
- Current gate-waveform candidate USB-only download execution entry:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_usb_only_download_execution_entry_2026-06-21.md`
  records the allowed envelope that opened the one USB-only mass-storage copy.
  It carries forward the candidate BIN hash above, the `D:` / `NOD_G474RE`
  target, pre-copy `FAIL.TXT` absence, and the one-copy limit. It is superseded
  for the live checkpoint by the download result.
- Current gate-waveform candidate BIN artifact record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_bin_artifact_record_no_power_2026-06-21.md`
  records conversion of the existing Gate E2 waveform candidate ELF to a
  downloadable BIN. Candidate ELF SHA256 is
  `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C`, MAP
  SHA256 is
  `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`, and
  generated BIN SHA256 is
  `362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31`, size
  `1852` bytes. The fallback ELF32 `PT_LOAD` converter was checked against
  the already-recorded neutral-wrapper objcopy BIN and matched SHA256
  `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71`.
  The MAP retains `gate_waveform_candidate_run_once` at `0x080005bc` and the
  checked forbidden normal-MCSDK MAP screen had no matches. This is a BIN
  artifact only: no USB copy, no board image change, no Run / Debug, no
  24 V execution, no Gate PWM output, no Motor Pilot / Profiler, no motor
  connection, and no readiness claim. Next checkpoint is only a separate
  waveform-candidate USB-only download execution entry after explicit user
  confirmation and authorization.
- Current gate-waveform neutral-wrapper 24V static scope baseline result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_24v_static_scope_baseline_result_2026-06-21.md`
  records oscilloscope ground on `CN3_15 / GND` and three two-channel probe
  passes: `CN3_1` / `CN3_2`, `CN3_3` / `CN3_4`, and `CN3_5` / `CN3_6`.
  User reported HSPY `CV` at about `0.036 A`, `CN3_1` through `CN3_6` as
  `0 V` straight lines, `nFAULT = 3.3 V`, and no board heat / smell / sound /
  reset-loop symptom. This is a static no-motor, no-PWM oscilloscope baseline
  only: no waveform output was executed. Turn HSPY output OFF after the
  baseline. Next checkpoint may only be a separate no-motor, short-window,
  instrumented waveform execution entry; no Motor Pilot / Profiler, no motor
  connection, and no readiness claim.
- Current gate-waveform neutral-wrapper 24V static no-motor result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_24v_static_no_motor_result_2026-06-21.md`
  records the bounded static check after residual-voltage isolation. User
  reported HSPY `CV`, current `0.036 A`, `VS / 24V_FUSED = 24 V`,
  `CN3_1` through `CN3_6 = 0 V`, `CN3_13 / nFAULT = 3.3 V`,
  `CN3_14 / 3V3 = 3.3 V`, `REG12 = 0.2 V`, and no board heat / smell /
  sound / reset-loop symptom. The six driver-input stop-rule was not hit and
  `nFAULT` stayed high in the static no-motor state. This is clean only for
  the bounded 24 V static no-motor table. Turn HSPY output OFF after the
  measurement. It opens no Run / Debug, no Gate PWM output, no Motor Pilot /
  Profiler, no motor connection, and no readiness claim. Next checkpoint may
  only be a separate no-motor instrumented gate-waveform gate, not direct
  motor power-up.
- Current gate-waveform neutral-wrapper residual-voltage isolation result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_residual_voltage_isolation_result_2026-06-21.md`
  records the bounded follow-up after the USB-only DMM completion result
  reported `VS / 24V_FUSED = 2 V` and `REG12 = 0.5 V`. The user disconnected
  USB / ST-LINK while HSPY / 24 V remained OFF and physically disconnected,
  the motor remained disconnected, and no `10 kohm` wake resistor or LIN1
  stimulus was installed. The user then reported `VS / 24V_FUSED = 0 V` and
  `REG12 = 0 V`. Decision: the earlier USB-only `VS / 24V_FUSED = 2 V`
  cleared after USB disconnect, so persistent VS backfeed is not indicated in
  this isolation check and the immediate residual-voltage blocker is cleared
  only. This opens no 24 V execution, no Run / Debug, no Gate PWM output, no
  Motor Pilot / Profiler, no motor connection, and no readiness claim. Next
  checkpoint is a separate dated next-stage phase-gate decision, not another
  repeat of the residual-voltage table and not direct motor power-up.
- Current gate-waveform neutral-wrapper USB-only DMM completion result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_completion_result_2026-06-21.md`
  completes the post-download USB-only DMM table. It carries forward
  `CN3_1` through `CN3_6 = 0 V`, `P13 = 3.3 V`, and `P14 = 3.3 V`, and
  records the new user-reported rows `VS / 24V_FUSED = 2 V`,
  `REG12 = 0.5 V`, and no board heat / smell / sound / reset-loop symptom.
  The six driver-input stop-rule was not hit, but the voltage-boundary stop
  condition for upward progression is active because `VS / 24V_FUSED = 2 V`
  is above the prior `< 1 V` USB-only boundary. This is a completed USB-only
  DMM table but not a pass for 24 V, PWM, or motor progression. Its live
  residual-voltage checkpoint is superseded by the later residual-voltage
  isolation result, which records `VS / 24V_FUSED = 0 V` and `REG12 = 0 V`
  after USB / ST-LINK disconnect.
- Current gate-waveform neutral-wrapper USB-only DMM partial result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_partial_result_2026-06-21.md`
  records the user-reported post-download DMM readings: `CN3_1` through
  `CN3_6` all `0 V`, `P13 = 3.3 V`, and `P14 = 3.3 V`. `P13` and `P14` are
  recorded against the requested `CN3_13 / nFAULT` and `CN3_14 / 3V3` rows
  using the same header-label mapping as the prior USB-only table. The six
  driver-input stop-rule was not hit because no `CN3_1` through `CN3_6`
  reading was stably above `0.3 V`. This is a partial USB-only DMM result
  only: `VS / 24V_FUSED`, `REG12`, and board heat / smell / sound /
  reset-loop status were still not reported in the partial record. It opened
  no 24 V, no Run / Debug, no Gate PWM output, no Motor Pilot / Profiler, no
  motor connection, and no readiness claim. It is superseded for the live
  checkpoint by the later DMM completion result, which reports
  `VS / 24V_FUSED = 2 V` and changes the next checkpoint to residual-voltage
  isolation.
- Current gate-waveform neutral-wrapper USB-only download result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_download_result_2026-06-21.md`
  records one USB-only ST-LINK mass-storage copy of the neutral-wrapper BIN.
  User confirmed `USB-only`, `24V disconnected`, and `motor disconnected`,
  then explicitly allowed copying the neutral-wrapper BIN to `D:`. The source
  ELF SHA256 is
  `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591`, MAP
  SHA256 is
  `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83`, and
  BIN SHA256 is
  `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71`.
  Pre-copy checks showed `D:` volume label `NOD_G474RE`, source BIN hash
  matched, no `D:\FAIL.TXT`, and no existing target BIN. The BIN was copied
  once to `D:\stdrive101_gate_waveform_neutral_wrapper_image.bin`. After a
  short wait, `D:` was still `NOD_G474RE`, `D:\FAIL.TXT` was absent, and the
  target BIN was no longer visible, consistent with ST-LINK mass-storage
  consumption. This download record itself contained no DMM neutral-state
  result and opened no 24 V, no Run / Debug, no Gate PWM output, no Motor
  Pilot / Profiler, no motor connection, and no readiness claim. The later
  later USB-only DMM partial, DMM completion, and residual-voltage isolation
  results supersede this download record's live checkpoint; the newest live
  checkpoint is a separate dated next-stage phase-gate decision.
- Current gate-waveform neutral-wrapper BIN artifact record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_bin_artifact_record_no_power_2026-06-21.md`
  records that the neutral-wrapper ELF was converted to a downloadable BIN
  with STM32Cube GNU Arm `objcopy`. The generated BIN is
  `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.bin`,
  size `1044` bytes, SHA256
  `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71`.
  The retained ELF symbol screen keeps
  `gate_waveform_neutral_wrapper_hold_idle_forever` and has no retained
  `gate_waveform_candidate_run_once`. This artifact record by itself was
  preparation only; the later USB-only download result records the actual
  mass-storage copy.
- Current gate-waveform neutral-wrapper USB-only neutral-state phase-gate plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_neutral_state_phase_gate_plan_2026-06-21.md`
  records planning only for a future USB-only neutral-state check of the
  neutral-wrapper image. It carries forward neutral-wrapper ELF SHA256
  `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591` and MAP
  SHA256 `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83`.
  The build-only image uses `main_neutral_wrapper.c`, excludes old
  `main_waveform_candidate.c`, retains
  `gate_waveform_neutral_wrapper_hold_idle_forever`, and has no retained ELF
  `gate_waveform_candidate_run_once`; the MAP lists
  `.text.gate_waveform_candidate_run_once` only as a discarded zero-address
  input section. The plan opens no flash, no Run / Debug, no USB runtime
  execution, no 24 V, no Gate PWM output, no Motor Pilot / Profiler, no motor
  connection, and no readiness claim. Next checkpoint is only a separate
  neutral-wrapper USB-only neutral-state execution-entry after explicit user
  request and freshly confirmed preconditions; Gate E4 remains closed.
- Current gate-waveform neutral-wrapper build-only record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_build_only_record_no_power_2026-06-21.md`
  records no-power object-only and linked-image build-only evidence for the
  neutral-wrapper source review. The separate build-only package is
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_neutral_wrapper_build_only_2026-06-21/`.
  The source-review packages still have no `CMakeLists.txt`; only the
  build-only package defines both
  `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK` and
  `GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK`. Clean configure used
  `CMAKE_SYSTEM_NAME=Generic`, `CMAKE_SYSTEM_PROCESSOR=arm`,
  `CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY`, STM32Cube GNU Arm GCC
  `14.3.1`, and Ninja `1.13.2`; clean build produced
  `stdrive101_gate_waveform_neutral_wrapper_objects` and
  `stdrive101_gate_waveform_neutral_wrapper_image`. Clean ELF SHA256 is
  `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591`;
  clean MAP SHA256 is
  `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83`.
  Size is `text=1044`, `data=0`, `bss=1536`, `dec=2580`, `hex=a14`; RAM use
  is `1536 B / 128 KB / 1.17%` and FLASH use is `1044 B / 512 KB / 0.20%`.
  The build includes `gate_waveform_candidate.c` and
  `main_neutral_wrapper.c`, excludes old `main_waveform_candidate.c`, and
  defines no HEX or BIN target. The retained ELF symbol table has no
  `gate_waveform_candidate_run_once`; the MAP lists it only as a discarded
  zero-address input section from `gate_waveform_candidate.c`, which is
  expected with `-ffunction-sections` and `--gc-sections`. This is build-only
  evidence only: no flash, no Run / Debug, no USB runtime execution, no
  24 V, no Gate PWM output, no Motor Pilot / Profiler, no motor connection,
  and no readiness claim. Next checkpoint is a neutral-wrapper USB-only
  neutral-state phase-gate plan or review only, not runtime execution.
- Current gate-waveform neutral-wrapper source review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_source_review_no_power_2026-06-21.md`
  records source-review evidence only for
  `manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/`. The
  package intentionally has no `CMakeLists.txt` and the header requires
  `GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK` with a `#error` guard before
  compilation. `main_neutral_wrapper.c` defines a replacement future entry
  point that calls `gate_waveform_candidate_force_idle_low()` before the
  forever loop and inside the forever loop. Wrapper `Inc/` and `Src/` contain
  no `gate_waveform_candidate_run_once()` call and no TIM1 waveform-window or
  output-enable helper. This closes the Gate E3 source-side limitation review:
  the current Gate E2 `run_once()` image remains unsuitable for proving no
  boot transient with DMM-only evidence, while this wrapper is still only
  source review. It opens no build, flash, Run / Debug, USB runtime execution,
  24 V, Gate PWM output, Motor Pilot / Profiler, motor connection, or
  readiness claim. Next checkpoint is neutral-wrapper build-only boundary
  planning or build-only record only, not USB runtime.
- Current Gate E3 gate-waveform USB-only neutral-state phase-gate plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_usb_only_neutral_state_phase_gate_plan_2026-06-21.md`
  records phase-gate planning only for a future USB-only neutral-state check
  of the Gate E2 waveform candidate image. It carries forward the Gate E2 ELF
  SHA256
  `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C`
  and MAP SHA256
  `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`.
  The current waveform candidate `main()` calls
  `gate_waveform_candidate_run_once()` once and then loops forcing idle low,
  so a future DMM-only USB check can prove only steady post-window idle state;
  it cannot prove absence of a reset-time or boot-time transient. This plan
  opens no flash, no Run / Debug, no USB runtime execution, no 24 V, no Gate
  PWM output, no Motor Pilot / Profiler, no motor connection, and no readiness
  claim. Next checkpoint is only a separate Gate E3 execution-entry after
  explicit user request and fresh preconditions, or a source-side neutral
  wrapper review; Gate E4 remains closed.
- Current Gate E2 gate-waveform build-only record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_build_only_record_no_power_2026-06-21.md`
  records no-power object-only and linked-image build-only evidence for the
  exact Gate E1 reviewed source package. The separate build-only package is
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_build_only_2026-06-21/`.
  The Gate E1 source package still has no `CMakeLists.txt`; only the Gate E2
  package defines `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK`. Clean configure
  used `CMAKE_SYSTEM_NAME=Generic`, `CMAKE_SYSTEM_PROCESSOR=arm`,
  `CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY`, STM32Cube GNU Arm GCC
  `14.3.1`, and Ninja `1.13.2`; clean build produced
  `stdrive101_gate_waveform_candidate_objects` and
  `stdrive101_gate_waveform_candidate_image`. Clean ELF SHA256 is
  `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C`;
  clean MAP SHA256 is
  `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`.
  Size is `text=1852`, `data=0`, `bss=1544`, `dec=3396`, `hex=d44`; RAM use
  is `1544 B / 128 KB / 1.18%` and FLASH use is `1852 B / 512 KB / 0.35%`.
  Source/build, ELF-symbol, and MAP forbidden screens are clean. This is
  build-only evidence only: no flash, no Run / Debug, no USB runtime, no
  24 V, no Gate PWM output, no Motor Pilot / Profiler, no motor connection,
  and no readiness claim. Next checkpoint is Gate E3 only: a separate
  USB-only neutral-state phase-gate plan or review, not runtime execution.
- Current Gate E1 gate-waveform isolated source package review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_isolated_source_package_review_no_power_2026-06-21.md`
  records a no-power source-package review only. The reviewed source package
  is
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_source_package_2026-06-21/`.
  It intentionally has no `CMakeLists.txt` and the header requires
  `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK` with a `#error` guard before
  any compilation. Candidate driver inputs are fixed as `PA8`, `PA9`, `PA10`,
  `PB13`, `PB14`, and `PB15`; startup and shutdown force all six low. The
  frozen candidate constants are `1 kHz`, `100` permille duty, `16` window
  periods, `8` pre-idle periods, `32` post-idle periods, and `DTG 0x90`. TIM1
  `MOE`, `CCER`, break, AOE clear, dead-time, and complementary-output policy
  are visible in source; `wait_for_pwm_periods_or_fault()` disables TIM1
  outputs and forces all six pins low if `nFAULT` falls. This is source-review
  evidence only: no build, no flash, no Run / Debug, no USB runtime, no 24 V,
  no Gate PWM output, no Motor Pilot / Profiler, no motor connection, and no
  readiness claim. Next checkpoint is Gate E2 only: a separate object-only and
  linked-image build-only boundary plan or build-only record for the exact
  reviewed source package, still no runtime or hardware action.
- Current Gate E0 gate-waveform image design plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_image_design_plan_no_power_2026-06-20.md`
  records design-boundary planning only for a future isolated waveform image.
  It requires a separate isolated waveform candidate, keeps the normal
  generated MCSDK app and command ingress blocked, fixes candidate driver
  inputs to `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and `PB15`, requires all
  six to be forced low before and after any future candidate window, and
  requires future TIM1 `MOE`, `CCER`, break, AOE, dead-time, and
  complementary-overlap policy review before source or build. It creates no
  source package, makes no CMake edit, runs no build, flashes no firmware,
  performs no Run / Debug, executes no USB runtime, applies no 24 V, emits no
  Gate PWM output, opens no Motor Pilot / Profiler path, connects no motor,
  and makes no readiness claim. Gate E1 source-package review has now been
  recorded separately; the next checkpoint is Gate E2 build-only boundary
  planning or build-only record only, still without flash, runtime, 24 V,
  Gate PWM output, Motor Pilot, Motor Profiler, motor connection, or readiness
  claim.
- Current gate-waveform / PWM-output no-power phase-gate plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_pwm_output_no_power_phase_gate_plan_2026-06-20.md`
  records planning only after the 24V static lockout carry-forward result.
  It accepts the carry-forward static boundary, linked lockout image, and
  USB-only runtime lockout result as planning evidence, keeps the normal
  generated MCSDK PWM path blocked, and names future-only gate-waveform
  execution gates, instrumentation requirements, rollback path, and stop
  rules. It does not open flash, Run / Debug, USB runtime execution, 24 V,
  Gate PWM output, oscilloscope probing on live gate or phase nodes,
  Motor Pilot, Motor Profiler, motor connection, power-stage readiness, or
  motor readiness. Gate E0 and Gate E1 have now been recorded separately; the
  next checkpoint is Gate E2 build-only boundary planning or build-only record
  only, with all execution actions still closed.
- Current manual gate-test 24V static lockout carry-forward result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_24v_static_lockout_carry_forward_result_2026-06-20.md`
  records a no-repeat decision after the user clarified that the equivalent
  USB + 24 V static all-inputs-low check had already been measured. It carries
  forward the earlier USB + 24 V static recheck (`HSPY CV`, about `0.045 A`,
  `CN3_1` through `CN3_6` all close to `0 V`, `nFAULT = 3.3 V`,
  `CN3_14 / 3V3 = 3.3 V`, `REG12 = 0.3 V`) and the USB-only lockout runtime
  result as reviewed lockout-image driver-input-low evidence. It does not
  claim a new 24 V lockout measurement under the lockout image and does not
  open Gate PWM output, Motor Pilot, Motor Profiler, motor connection,
  power-stage readiness, or motor readiness. It has now led to the separate
  gate-waveform / PWM-output no-power phase-gate plan; it still does not open
  execution by itself.
- Current manual gate-test 24V static lockout execution entry:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_24v_static_lockout_execution_entry_2026-06-20.md`
  records that the user asked to continue after the 24V static lockout
  phase-gate plan and confirmed all entry gates: HSPY output `OFF`, HSPY set
  to `24 V / 0.2 A`, `VS / 24V_FUSED` close to `0 V` and below `1 V`, motor
  disconnected, `10 kohm` wake resistor / `LIN1` stimulus removed, Motor
  Pilot / Profiler closed, and no abnormal heat / smell / sound. It opens
  exactly one bounded 24 V static lockout measurement pass only. It does not
  contain the measured result itself; the later carry-forward result closes the
  duplicate-measurement branch using the already recorded USB + 24 V static
  recheck. It still does not open Gate PWM output, Motor Pilot, Motor
  Profiler, motor connection, Hall closed loop, sensorless operation,
  power-stage readiness, or motor readiness.
- Current manual gate-test 24V static lockout phase-gate plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_24v_static_lockout_phase_gate_plan_2026-06-20.md`
  records a phase-gate plan only after the USB-only lockout result. It accepts
  the USB-only runtime lockout result as driver-input-low evidence and carries
  forward the earlier USB plus 24V static baseline. It names candidate later
  24V static lockout execution preconditions, measurement table, rollback path,
  and stop rules. This is not execution: no 24V execution in this record, no
  flash, no Run / Debug, no normal MCSDK app run, no Gate PWM output, no Motor
  Pilot / Profiler, no motor connection, and no powered-drive readiness. Next
  possible checkpoint is only a later separate 24 V static lockout
  execution-entry record if the user explicitly asks to execute it and the
  preconditions are freshly true.
- Current manual gate-test USB-only runtime lockout result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_result_2026-06-20.md`
  records one USB / ST-LINK-only lockout flash-run measurement pass. The
  reviewed ELF SHA256 was
  `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`;
  the generated BIN SHA256 was
  `CBF833C8E9289D8B4A952C32C641CAA94928F1F8119C5DC528EBD779915EA6BE`;
  the BIN was copied through ST-LINK mass storage `D:` / `NOD_G474RE`, and
  no `FAIL.TXT` was present after copy. User-reported USB-only readings:
  `CN3_1` through `CN3_6` all `0 V`, `CN3_13 / nFAULT = 3.3 V`,
  `CN3_14 / 3V3 = 3.3 V`, and `REG12 = 0 V`; driver-input stop rule not
  hit. This is USB-only runtime evidence only: no 24 V, no PWM-output
  validation, no Motor Pilot / Profiler, no motor connection, no
  power-stage readiness, and no motor readiness.
- Current manual gate-test USB-only runtime lockout execution entry:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_execution_entry_2026-06-20.md`
  records that the user requested `USB-only lockout runtime 检查` and confirmed
  HSPY / 24 V OFF and physically disconnected, `VS / 24V_FUSED < 1 V`,
  motor disconnected, `10 kohm` wake resistor / `LIN1` stimulus removed,
  Motor Pilot / Profiler closed, and no abnormal heat / smell / sound. The
  candidate ELF hash matches
  `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`.
  It opens exactly one USB-only lockout flash-run measurement pass using that
  ELF. Still forbidden: 24 V, Gate PWM output, Motor Pilot, Motor Profiler,
  motor connection, Hall closed loop, sensorless operation, power-stage
  readiness, and motor readiness. Next checkpoint is a separate runtime result
  record after the user reports direct measurements.
- Current manual gate-test USB-only runtime lockout phase-gate plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_phase_gate_plan_2026-06-20.md`
  records a phase-gate plan only. It accepts the linked-image build-only
  record as image-boundary evidence, carries forward ELF SHA256
  `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`
  and MAP SHA256
  `A020546A3D1D56B1C509939161BD80E5A25EC5843C928B9BC13E8D07684FF6C0`,
  and names the later USB-only runtime preconditions, measurement table, and
  stop rules. This is still not execution: no flash, no Run / Debug, no USB
  runtime execution, no 24 V, no Gate PWM output, no Motor Pilot / Profiler,
  no motor connection, and no readiness claim. Next possible checkpoint is a
  later separate USB-only runtime execution record only if the user explicitly
  asks to execute it and the preconditions are still true.
- Current manual gate-test linked-image build-only record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_linked_image_build_only_record_2026-06-20.md`
  records Gate D build-only evidence for the isolated lockout image. The
  repo-local `CMakeLists.txt` now keeps `stdrive101_gate_lockout_objects` and
  adds linked target `stdrive101_gate_lockout_image`. CMake configured as
  `Generic` / `arm` with STM32Cube GNU Arm GCC `14.3.1` and Ninja, and the
  linked build exited `0`. Produced artifacts are
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf`
  SHA256 `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`
  and
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.map`
  SHA256 `A020546A3D1D56B1C509939161BD80E5A25EC5843C928B9BC13E8D07684FF6C0`.
  Forbidden source, ELF-symbol, and MAP screens were clean for
  `MC_StartMotor1`, `MCI_START`, PC13 / MCP ingress, Motor Pilot, R3_2 /
  PWM-output enable symbols, Hall, PID, and speed-control symbols. This is
  build-only evidence only: no flash, no Run / Debug, no USB runtime
  execution, no 24 V, no Gate PWM output, no Motor Pilot / Profiler, no motor
  connection, and no readiness claim. Next allowed checkpoint is a separate
  USB-only runtime lockout phase-gate plan or review, not runtime execution.
- Current manual gate-test linked-image build-boundary plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_linked_image_build_boundary_plan_2026-06-20.md`
  records Gate D boundary planning only. It carries forward the lockout source
  hashes and object-only build pass, fixes future link candidate inputs to the
  repo-local `nucleo_g474re_baseline` startup, linker script,
  `system_stm32g4xx.c`, `syscalls.c`, and `sysmem.c`, names the future target
  `stdrive101_gate_lockout_image`, and requires ELF plus MAP as minimum future
  build-only artifacts. It does not create a linked image, edit CMake, run a
  build, authorize flash, Run / Debug, USB runtime execution, 24 V, Gate PWM
  output, Motor Pilot, Motor Profiler, motor connection, or readiness claims.
  Next allowed checkpoint is a separate linked-image build-only record for the
  lockout image, still without runtime execution.
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
- Current algorithm-side next seam: keep sensorless work in host-side no-power
  replay, lock-aware command-policy fixtures, speed-loop hold /
  anti-windup fixtures, wrap-boundary frontend checks, comparison snapshots,
  and source-backed MCSDK boundary checks first. The latest repo-side seam is
  now the host-side reverse target-omega lock-threshold handoff, while
  the current archived generated MCSDK source remains Hall-based with generic
  CORDIC / STO support symbols and not an active MCSDK observer instance.
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
