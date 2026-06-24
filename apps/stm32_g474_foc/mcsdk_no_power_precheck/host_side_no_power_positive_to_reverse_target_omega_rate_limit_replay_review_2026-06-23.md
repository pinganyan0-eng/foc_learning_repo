# Host-Side No-Power Positive-To-Reverse Target-Omega Rate-Limit Replay Review

Date: 2026-06-23

## Decision

`Host-side no-power positive-to-reverse target-omega rate-limit replay / command-ramp crossing fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record extends only the host-side no-power sensorless command fixture
chain. It freezes the existing target-omega command ramp behavior when an
already locked positive-speed command is reversed through zero:

```text
locked positive target_omega state
-> negative target_omega command
-> target_omega_rate_limit_e_rad_s2 crossing ramp
-> lock-aware speed PI
-> lock-aware effective iq command
-> q-axis current-loop PI movement
-> MCSDK-shaped q15 speed/current metadata
```

It does not change host-side model behavior. It adds fixture coverage around
the existing `SensorlessSpeedLoopConfig.target_omega_rate_limit_e_rad_s2`,
`_ramp_target_omega(...)`, `sensorless_current_control_replay_sequence(...)`,
and `sensorless_replay_to_mcsdk_speed_command_snapshots(...)` paths.

## Code And Fixture

- `tests/test_foc_sensorless_frontend.py`
  - adds
    `test_replay_sequence_rate_limits_positive_target_across_zero_to_reverse`;
  - starts from an already locked tracking state with
    `speed_loop_state.target_omega_e_rad_s = 20.0`;
  - commands `target_omega_e_rad_s = -20.0` with
    `target_omega_rate_limit_e_rad_s2 = 50.0` and `dt_s = 0.1`;
  - verifies `speed_loop_target_omega`, `speed_loop_target_iq`,
    `speed_loop_pi_integrator`, `effective_target_iq`, and
    `q_axis_integrator`.
- `tests/fixtures/foc_sensorless_frontend_vectors.json`
  - adds
    `positive_to_reverse_target_omega_rate_limit_crosses_zero_while_locked`;
  - records the same positive-to-reverse crossing replay for fixture-driven
    regression tests.
- `tests/fixtures/foc_mcsdk_bridge_vectors.json`
  - adds
    `positive_to_reverse_target_omega_rate_limit_crossing_steps_map_to_q15`;
  - freezes the MCSDK-shaped q15 snapshot sequence for the same replay.
- `tests/test_foc_sensorless_frontend_vectors.py` and
  `tests/test_mcsdk_foc_bridge_vectors.py`
  - now record that the vector files include positive-to-reverse target-omega
    crossing fixture coverage.

## Protected Replay Sequence

The protected frontend case is
`positive_to_reverse_target_omega_rate_limit_crosses_zero_while_locked`.

It starts from:

```text
sensorless_state: tracking, locked, omega_e_rad_s = 10.0
startup_policy_state: tracking_enabled = true
speed_loop_state.target_omega_e_rad_s = 20.0
speed_loop_state.speed_pi.integrator = 0.5
```

With `target_omega_rate_limit_e_rad_s2 = 50.0` and `dt_s = 0.1`, the target
command can move only 5 rad/s per step. The protected rows are:

```text
speed_loop_target_omega: [15.0, 10.0, 5.0, 0.0, -5.0, -10.0, -15.0, -20.0]
speed_loop_target_iq:    [1.25, 0.75, 0.0, -1.0, -1.5, -2.0, -2.0, -2.0]
speed_loop_pi_integrator:[0.75, 0.75, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0]
effective_target_iq:     [1.25, 0.75, 0.0, -1.0, -1.5, -1.5, -1.5, -1.5]
q_axis_integrator:       [1.25, 2.0, 2.0, 1.0, -0.5, -2.0, -3.5, -5.0]
```

This freezes only host-side command-ramp semantics. It is not a firmware
direction reversal strategy and it does not prove that an MCSDK speed loop,
firmware current limiting path, or motor can safely execute this sequence.

## Protected MCSDK-Shaped Snapshot Sequence

The protected bridge case is
`positive_to_reverse_target_omega_rate_limit_crossing_steps_map_to_q15`.

It freezes the comparison metadata returned by
`sensorless_replay_to_mcsdk_speed_command_snapshots(...)`:

```text
target_omega_q15:    [24576, 16384, 8192, 0, -8192, -16384, -24576, -32768]
measured_omega_q15:  [16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384]
requested_iq_q15:    [20480, 12288, 0, -16384, -24576, -32768, -32768, -32768]
effective_iq_q15:    [20480, 12288, 0, -16384, -24576, -24576, -24576, -24576]
locked:              [true, true, true, true, true, true, true, true]
limited:             [false, false, false, false, false, true, true, true]
```

The final three steps show the comparison-only current-command clamp after the
requested q-axis current exceeds the locked host-side `iq` limit.

## Subagent Protocol

Read-only helper Kuhn reviewed the filtered frontend/bridge fixture slice and
identified the missing locked positive-to-reverse command reversal through
zero as the smallest useful no-power gap after the signed reverse
target-omega rate-limit replay. The main agent kept all repo writes in the
owner path and used the helper digest only as decision-relevant evidence for
this no-power increment.

## Boundary

This is host-side no-power algorithm fixture and comparison-shape evidence
only.

It is not firmware.
It is not generated-code edit permission.
It is not MCSDK integration.
It is not MCSDK numerical equivalence.
It is not MCSDK speed-loop hook evidence.
It is not firmware speed-loop behavior.
It is not firmware current limiting.
It is not a firmware direction reversal strategy.
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

`python -m json.tool tests\fixtures\foc_sensorless_frontend_vectors.json`
passed; `python -m json.tool tests\fixtures\foc_mcsdk_bridge_vectors.json`
passed; `python -m unittest tests.test_foc_sensorless_frontend
tests.test_foc_sensorless_frontend_vectors tests.test_mcsdk_foc_bridge_vectors`
passed: 42 tests OK; `python -m unittest
tests.test_workflow_contracts.FocCoreHostModelWorkflowTests` passed:
37 tests OK; `python -m unittest tests.test_workflow_contracts` passed:
153 tests OK; full `python -m unittest discover -s tests` passed:
308 tests OK; `python -m compileall src tests` passed;
`python tools\check_ai_contracts.py` passed with no AI contract errors and
the known `ACTIVE_TASK.md` review-lifecycle warning; `git diff --check`
passed with only LF/CRLF conversion warnings.
