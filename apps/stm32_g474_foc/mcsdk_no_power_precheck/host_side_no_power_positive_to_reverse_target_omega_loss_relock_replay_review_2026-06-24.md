# Host-Side No-Power Positive-To-Reverse Target-Omega Loss/Relock Replay Review

Date: 2026-06-24

## Decision

`Host-side no-power positive-to-reverse target-omega loss/relock replay / command-ramp hold-loss-relock fixture only / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record extends only the host-side no-power sensorless command/replay
fixture chain. It protects the existing target-omega command ramp when a
positive-to-reverse command is interrupted by confirmed observer loss and then
relocks:

```text
locked positive target_omega state
-> negative target_omega command
-> rate-limited ramp toward zero while tracking
-> confirmed loss holds target_omega at zero and blocks effective iq
-> relock resumes the ramp toward the negative target
-> MCSDK-shaped observer snapshot metadata for the same replay
-> MCSDK-shaped speed/current command snapshot metadata for the same replay
```

It does not change host-side model behavior. It adds fixture coverage around
the existing `SensorlessSpeedLoopConfig.target_omega_rate_limit_e_rad_s2`,
`_ramp_target_omega(...)`, `sensorless_current_control_replay_sequence(...)`,
`sensorless_replay_to_mcsdk_observer_snapshots(...)`, and
`sensorless_replay_to_mcsdk_speed_command_snapshots(...)` paths.

## Code And Fixture

- `tests/test_foc_sensorless_frontend.py`
  - adds
    `test_replay_sequence_holds_positive_to_reverse_ramp_during_loss_and_relock`;
  - starts from an already tracking state with
    `speed_loop_state.target_omega_e_rad_s = 20.0`;
  - commands `target_omega_e_rad_s = -20.0` with
    `target_omega_rate_limit_e_rad_s2 = 50.0` and `dt_s = 0.1`;
  - verifies that confirmed loss holds the ramp at zero, clamps effective
    current to zero, and relock resumes the negative ramp.
- `tests/fixtures/foc_sensorless_frontend_vectors.json`
  - adds
    `positive_to_reverse_target_omega_rate_limit_holds_during_loss_and_relock`;
  - records the same loss/relock replay for fixture-driven regression tests.
- `tests/fixtures/foc_mcsdk_bridge_vectors.json`
  - adds
    `positive_to_reverse_target_omega_rate_limit_loss_relock_steps_map_to_observer_snapshots`;
  - adds
    `positive_to_reverse_target_omega_rate_limit_loss_relock_steps_map_to_q15`;
  - freezes MCSDK-shaped observer and speed/current command snapshot metadata
    for the same replay.
- `tests/test_foc_sensorless_frontend_vectors.py` and
  `tests/test_mcsdk_foc_bridge_vectors.py`
  - replay the vector files against the host-side reference model and bridge
    adapter.

## Protected Replay Sequence

The protected frontend case is
`positive_to_reverse_target_omega_rate_limit_holds_during_loss_and_relock`.

It starts from:

```text
sensorless_state: tracking, locked, omega_e_rad_s = 10.0
startup_policy_state: tracking_enabled = true
speed_loop_state.target_omega_e_rad_s = 20.0
speed_loop_state.speed_pi.integrator = 0.5
```

With `target_omega_rate_limit_e_rad_s2 = 50.0` and `dt_s = 0.1`, the target
command can move only 5 rad/s per step while tracking. When confirmed loss is
reached, the host-side replay holds target omega at zero and blocks the
effective q-axis command until relock.

Protected rows:

```text
speed_loop_target_omega: [15.0, 10.0, 5.0, 0.0, 0.0, 0.0, -5.0, -10.0]
speed_loop_target_iq:    [1.25, 0.75, 0.0, -1.0, 0.0, 0.0, -1.5, -2.0]
speed_loop_pi_integrator:[0.75, 0.75, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0]
effective_target_iq:     [1.25, 0.75, 0.0, -1.0, 0.0, 0.0, -1.5, -1.5]
command_reasons:         [tracking_command, tracking_command, tracking_command, tracking_command, unlocked_current_limit, unlocked_current_limit, tracking_command, tracking_command]
q_axis_integrator:       [1.25, 2.0, 2.0, 1.0, 1.0, 1.0, -0.5, -2.0]
locked:                  [true, true, true, true, false, false, true, true]
loss_candidate_count:    [0, 0, 0, 1, 2, 0, 0, 0]
final_target_omega:      -10.0
final_speed_pi_integrator: 0.0
```

This freezes only host-side command-ramp behavior across loss and relock. It is
not a firmware direction reversal strategy and it does not prove that an MCSDK
speed loop, firmware current limiting path, sensorless observer, or motor can
safely execute this sequence.

## Protected MCSDK-Shaped Observer Snapshot Sequence

The protected bridge case is
`positive_to_reverse_target_omega_rate_limit_loss_relock_steps_map_to_observer_snapshots`.

It freezes comparison metadata returned by
`sensorless_replay_to_mcsdk_observer_snapshots(...)`:

```text
theta_q15:      [10430, 11473, 12516, 13559, 25033, -27987, 27119, 17732]
omega_q15:      [16384, 16384, 16384, 16384, 18022, 19661, 16384, 16384]
confidence_q15: [31130, 31130, 31130, 3277, 0, 0, 31130, 31130]
mode:           [tracking, tracking, tracking, tracking, startup, startup, tracking, tracking]
locked:         [true, true, true, true, false, false, true, true]
```

This is observer snapshot metadata for comparison only. It is not proof of an
active MCSDK observer instance, MCSDK Observer PLL equivalence, MCSDK Observer
CORDIC equivalence, SMO validation, or sensorless operation.

## Protected MCSDK-Shaped Speed/Current Snapshot Sequence

The protected bridge case is
`positive_to_reverse_target_omega_rate_limit_loss_relock_steps_map_to_q15`.

It freezes comparison metadata returned by
`sensorless_replay_to_mcsdk_speed_command_snapshots(...)`:

```text
target_omega_q15: [24576, 16384, 8192, 0, 0, 0, -8192, -16384]
measured_omega_q15: [16384, 16384, 16384, 16384, 18022, 19661, 16384, 16384]
requested_iq_q15: [20480, 12288, 0, -16384, 0, 0, -24576, -32768]
effective_iq_q15: [20480, 12288, 0, -16384, 0, 0, -24576, -24576]
limited: [false, false, false, false, false, false, false, true]
reason: [tracking_command, tracking_command, tracking_command, tracking_command, unlocked_current_limit, unlocked_current_limit, tracking_command, tracking_command]
```

This is speed/current command snapshot metadata for comparison only. It is not
proof of firmware speed-loop behavior, firmware current limiting, MCSDK
speed-loop hook evidence, MCSDK numerical equivalence, or a firmware direction
reversal strategy.

## Subagent Protocol

Read-only helper Locke identified the frontend fixture need from a filtered
sensorless frontend slice. Read-only helper Mill identified the companion
MCSDK-shaped observer snapshot parity fixture from a filtered bridge slice.
Read-only helper Gauss later confirmed the registration mismatch to avoid:
the 2026-06-23 locked crossing case is
`positive_to_reverse_target_omega_rate_limit_crosses_zero_while_locked`, while
this 2026-06-24 increment is the loss/relock case
`positive_to_reverse_target_omega_rate_limit_holds_during_loss_and_relock`.
Read-only helper Confucius later identified the remaining bridge gap: the same
loss/relock replay had observer snapshots but not speed/current q15 parity.
The main agent kept all repo writes in the owner path and used helper digests
only as decision-relevant evidence.

## Boundary

This is host-side no-power algorithm fixture and comparison-shape observer plus
speed/current snapshot evidence only.

It is not firmware.
It is not generated-code edit permission.
It is not MCSDK integration.
It is not MCSDK numerical equivalence.
It is not MCSDK speed-loop hook evidence.
It is not firmware speed-loop behavior.
It is not firmware current limiting.
It is not a firmware direction reversal strategy.
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
