# Host-Side No-Power Signed Reverse Target-Omega Rate-Limit Replay Review

Date: 2026-06-23

## Decision

`Host-side no-power signed reverse target-omega rate-limit replay / command-ramp fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record extends only the host-side no-power sensorless command fixture
chain. It freezes the existing target-omega command ramp behavior across a
signed reverse replay:

```text
negative target_omega command
-> target_omega_rate_limit_e_rad_s2 command ramp
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
    `test_replay_sequence_rate_limits_signed_reverse_target_command`;
  - freezes the 8-step signed reverse replay with
    `target_omega_rate_limit_e_rad_s2 = 50.0`,
    `hold_when_unlocked = true`, and `dt_s = 0.1`;
  - verifies `speed_loop_target_omega`, `speed_loop_target_iq`,
    `speed_loop_pi_integrator`, `effective_target_iq`, and
    `q_axis_integrator`.
- `tests/fixtures/foc_sensorless_frontend_vectors.json`
  - adds
    `signed_reverse_target_omega_rate_limit_holds_until_lock_and_after_loss`;
  - records the same command-ramp replay for fixture-driven regression tests.
- `tests/fixtures/foc_mcsdk_bridge_vectors.json`
  - adds
    `signed_reverse_target_omega_rate_limit_replay_steps_map_to_q15`;
  - freezes the MCSDK-shaped q15 snapshot sequence for the same replay.
- `tests/test_foc_sensorless_frontend_vectors.py` and
  `tests/test_mcsdk_foc_bridge_vectors.py`
  - already load `target_omega_rate_limit_e_rad_s2` and replay every fixture
    case; no source change was needed.

## Protected Replay Sequence

The protected frontend case is
`signed_reverse_target_omega_rate_limit_holds_until_lock_and_after_loss`.

It uses the same lock/loss/relock confidence pattern as the earlier signed
reverse fixture. With `target_omega_rate_limit_e_rad_s2 = 50.0` and
`dt_s = 0.1`, the locked target command can move only 5 rad/s per step. The
protected rows are:

```text
speed_loop_target_omega: [0.0, 0.0, -5.0, -10.0, -15.0, -15.0, -15.0, -20.0]
speed_loop_target_iq:    [0.0, 0.0, 0.75, 0.25, -0.5, 0.0, 0.0, -1.5]
speed_loop_pi_integrator:[0.0, 0.0, 0.25, 0.25, 0.0, 0.0, 0.0, -0.5]
effective_target_iq:     [0.0, 0.0, 0.75, 0.25, -0.5, 0.0, 0.0, -1.5]
q_axis_integrator:       [0.0, 0.0, 0.75, 1.0, 0.5, 0.5, 0.5, -1.0]
```

Because the observed speed is already `-10.0` rad/s while the target is still
ramping from `0.0` toward `-20.0`, the first locked step produces a positive
candidate `iq_ref` before later steps cross through small positive and
negative current commands. This is only a host-side replay semantic. It is not
a firmware reverse-startup strategy.

## Protected MCSDK-Shaped Snapshot Sequence

The protected bridge case is
`signed_reverse_target_omega_rate_limit_replay_steps_map_to_q15`.

It freezes the comparison metadata returned by
`sensorless_replay_to_mcsdk_speed_command_snapshots(...)`:

```text
target_omega_q15:    [0, 0, -8192, -16384, -24576, -24576, -24576, -32768]
measured_omega_q15:  [1638, 3277, -16384, -16384, -16384, -14746, -13107, -16384]
requested_iq_q15:    [0, 0, 12288, 4096, -8192, 0, 0, -24576]
effective_iq_q15:    [0, 0, 12288, 4096, -8192, 0, 0, -24576]
locked:              [false, false, true, true, true, false, false, true]
limited:             [false, false, false, false, false, false, false, false]
```

The unlocked steps remain zero effective-current metadata snapshots. The
locked steps preserve the rate-limited signed speed command and the resulting
small positive, small negative, and final negative current-command metadata.

## Subagent Protocol

Read-only helper Dewey reviewed only the filtered frontend/bridge fixture
slice and confirmed that the smallest useful next no-power gap was a
target-omega rate-limit / command-ramp replay fixture. The main agent kept all
repo writes in the owner path and used the helper digest only as
decision-relevant evidence for this no-power increment.

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
It is not a firmware reverse-startup strategy.
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

- `python -m json.tool tests\fixtures\foc_sensorless_frontend_vectors.json`
  passed.
- `python -m json.tool tests\fixtures\foc_mcsdk_bridge_vectors.json` passed.
- `python -m unittest tests.test_foc_sensorless_frontend tests.test_foc_sensorless_frontend_vectors tests.test_mcsdk_foc_bridge_vectors`
  passed: 41 tests OK.
- `python -m unittest tests.test_workflow_contracts.FocCoreHostModelWorkflowTests`
  passed: 35 tests OK.
- `python -m unittest tests.test_workflow_contracts` passed: 151 tests OK.
- `python -m unittest discover -s tests` passed: 305 tests OK.
- `python -m compileall src tests` passed.
- `python tools\check_ai_contracts.py` passed with no AI contract errors and
  the known `ACTIVE_TASK.md` review-lifecycle warning.
- `git diff --check` passed with only LF/CRLF conversion warnings.
