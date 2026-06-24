# Host-Side No-Power Reverse Target-Omega Lock-Threshold Handoff Review

Date: 2026-06-24

## Decision

`Host-side no-power reverse target-omega lock-threshold handoff / startup-unlocked threshold fixture only / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record extends only the host-side no-power sensorless command/replay
fixture chain. It protects the lock-threshold transition when a negative
`target_omega_e_rad_s` command arrives while the frontend is still in startup /
unlocked state:

```text
startup / unlocked frontend state
-> speed_loop_state.target_omega_e_rad_s still carries a prior +20.0 rad/s
-> target_omega_e_rad_s command requests -20.0 rad/s
-> lock_count_required = 3
-> lock_candidate_count = 0, 1, and 2 remain unlocked
-> hold_when_unlocked freezes target omega at +20.0 until the threshold step
-> the first tracking-enabled step begins the rate-limited ramp
-> MCSDK-shaped speed/current q15 metadata records the same semantic boundary
```

It does not change host-side model behavior. It adds fixture coverage around
the existing `SensorlessStartupPolicyConfig.lock_count_required`,
`SensorlessSpeedLoopConfig.hold_when_unlocked`,
`SensorlessSpeedLoopConfig.target_omega_rate_limit_e_rad_s2`,
`sensorless_startup_policy_step(...)`,
`sensorless_current_control_replay_sequence(...)`, and
`sensorless_replay_to_mcsdk_speed_command_snapshots(...)` paths.

## Code And Fixture

- `tests/test_foc_sensorless_frontend.py`
  - adds
    `test_replay_sequence_starts_reverse_target_ramp_at_lock_threshold`;
  - uses `lock_count_required = 3` to force one extra high-confidence sample
    before tracking is enabled;
  - verifies that `lock_candidate_count < lock_count_required` keeps the
    speed-loop target frozen at `20.0`, keeps effective current at zero, and
    does not update the q-axis PI integrator;
  - verifies that the first `tracking_enabled = true` step starts the
    rate-limited ramp from `20.0` to `15.0`.
- `tests/test_foc_sensorless_frontend_vectors.py`
  - now checks optional `lock_candidate_count` rows in
    `sensorless_speed_command_policy_sequences`, so fixture-level startup
    threshold rows are protected.
- `tests/fixtures/foc_sensorless_frontend_vectors.json`
  - adds
    `reverse_target_omega_lock_threshold_handoff_starts_ramp_only_at_lock`;
  - also protects `lock_candidate_count` in the existing
    `reverse_target_omega_remains_frozen_until_lock_not_startup_strategy`
    vector.
- `tests/fixtures/foc_mcsdk_bridge_vectors.json`
  - adds
    `reverse_target_omega_lock_threshold_handoff_steps_map_to_q15`;
  - freezes MCSDK-shaped q15 speed/current snapshot metadata for the same
    replay.
- `tests/test_mcsdk_foc_bridge_vectors.py`
  - keeps the bridge fixture metadata explicit that this is comparison-shape
    metadata only.

## Protected Replay Sequence

The protected frontend case is
`reverse_target_omega_lock_threshold_handoff_starts_ramp_only_at_lock`.

It starts from:

```text
sensorless_state: startup, unlocked, omega_e_rad_s = 0.0
startup_policy_state: tracking_enabled = false
speed_loop_state.target_omega_e_rad_s = 20.0
speed_loop_state.speed_pi.integrator = 0.5
input target_omega_e_rad_s = -20.0
lock_count_required = 3
```

With `target_omega_rate_limit_e_rad_s2 = 50.0` and `dt_s = 0.1`, the target
command can move only 5 rad/s per locked step. The first low-confidence sample
and the first two high-confidence samples remain startup / unlocked, so those
samples do not move the target toward the negative command. The fourth sample
is the first threshold-crossing step and starts the ramp.

Protected rows:

```text
speed_loop_target_omega: [20.0, 20.0, 20.0, 15.0, 10.0]
speed_loop_target_iq:    [0.0, 0.0, 0.0, 2.0, 2.0]
speed_loop_pi_integrator:[0.5, 0.5, 0.5, 0.5, 0.5]
effective_target_iq:     [0.0, 0.0, 0.0, 1.5, 1.5]
command_reasons:         [unlocked_current_limit, unlocked_current_limit, unlocked_current_limit, tracking_command, tracking_command]
q_axis_integrator:       [0.0, 0.0, 0.0, 1.5, 3.0]
locked:                  [false, false, false, true, true]
lock_candidate_count:    [0, 1, 2, 3, 3]
loss_candidate_count:    [0, 0, 0, 0, 0]
final_target_omega:      10.0
final_speed_pi_integrator: 0.5
```

This explicitly keeps reverse `target_omega_e_rad_s` as a locked command
semantic, not a reverse open-loop startup strategy. The startup ramp contract
remains non-negative through `SensorlessFrontendConfig.startup_target_omega_e_rad_s`.

## Protected MCSDK-Shaped Speed/Current Snapshot Sequence

The protected bridge case is
`reverse_target_omega_lock_threshold_handoff_steps_map_to_q15`.

It freezes comparison metadata returned by
`sensorless_replay_to_mcsdk_speed_command_snapshots(...)`:

```text
target_omega_q15: [32767, 32767, 32767, 24576, 16384]
measured_omega_q15: [1638, 3277, 4915, -16384, -16384]
requested_iq_q15: [0, 0, 0, 32767, 32767]
effective_iq_q15: [0, 0, 0, 24576, 24576]
locked: [false, false, false, true, true]
limited: [false, false, false, true, true]
reason: [unlocked_current_limit, unlocked_current_limit, unlocked_current_limit, tracking_command, tracking_command]
```

This is speed/current command snapshot metadata for comparison only. It is not
proof of firmware speed-loop behavior, firmware current limiting, MCSDK
speed-loop hook evidence, MCSDK numerical equivalence, or a reverse startup
strategy.

## Subagent Protocol

Read-only helper Ohm reviewed only the filtered current snapshot, active task,
frontend fixture, and bridge fixture slices. Ohm identified this
lock-threshold handoff fixture as the smallest remaining P0 ambiguity because
the previous startup-hold evidence used `lock_count_required = 2`, while this
case proves that `lock_candidate_count < lock_count_required` keeps the target
frozen and that ramping begins only on the first threshold-crossing tracking
step. The main agent kept all repo writes in the owner path and used the helper
digest only as decision-relevant evidence.

## Boundary

This is host-side no-power algorithm fixture and comparison-shape
speed/current snapshot evidence only.

It is not firmware.
It is not generated-code edit permission.
It is not MCSDK integration.
It is not MCSDK numerical equivalence.
It is not MCSDK speed-loop hook evidence.
It is not firmware speed-loop behavior.
It is not firmware current limiting.
It is not a firmware reverse-startup strategy.
It is not reverse open-loop startup validation.
It is not an active MCSDK observer instance.
It is not MCSDK Observer PLL equivalence.
It is not MCSDK Observer CORDIC equivalence.
It is not SMO implementation or validation.
It is not sensorless / SMO validation.
It is not compare-register evidence.
It is not Gate PWM validation.
It is not hardware validation.
It is not power-stage readiness.
It is not motor readiness.

Forbidden actions and claims remain:

- No flash.
- No Run / Debug.
- No 24 V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Pilot / Profiler.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## Verification

Final verification is recorded in `workflow/ACTIVE_TASK.md` after the status and
contract updates are complete.
