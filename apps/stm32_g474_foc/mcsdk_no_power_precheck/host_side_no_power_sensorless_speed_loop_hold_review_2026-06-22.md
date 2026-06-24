# Host-Side No-Power Sensorless Speed-Loop Hold Review

Date: 2026-06-22

## Decision

`Host-side no-power sensorless speed-loop hold / lock-aware PI anti-windup fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record extends only the host-side no-power sensorless replay chain. It
adds an optional speed-loop hold policy so startup, unlocked, and confirmed-loss
steps can freeze the host-side speed PI state instead of quietly accumulating
hidden error while the current-command policy clamps effective `iq_ref`.

The increment is useful because the earlier speed/current command policy replay
could zero the effective current command while still letting the outer speed PI
integrator advance. That made the replay less useful for reviewing startup /
loss / relock behavior, because a later relock could inherit speed PI state
that was accumulated while the frontend was not locked.

## Code And Fixture

- `src/foc_sensorless_frontend.py`
  - adds `SensorlessSpeedLoopConfig.hold_when_unlocked`;
  - extends `sensorless_speed_loop_step(...)` with an `enabled` argument;
  - returns `target_iq = 0.0`, `speed_error_e_rad_s = 0.0`, and the unchanged
    `SensorlessSpeedLoopState` when `enabled` is false and
    `hold_when_unlocked` is true;
  - calls `sensorless_speed_loop_step(..., enabled=frontend.locked)` from
    `sensorless_current_control_step(...)`.
- `tests/test_foc_sensorless_frontend.py`
  - adds `test_speed_loop_can_hold_pi_state_while_unlocked`;
  - adds `test_replay_sequence_can_hold_speed_loop_pi_until_lock_and_after_loss`.
- `tests/fixtures/foc_sensorless_frontend_vectors.json`
  - updates the replay case to
    `speed_loop_pi_holds_until_lock_and_after_loss`;
  - sets `hold_when_unlocked = true`;
  - uses nonzero `ki = 0.5` so integrator movement or hold behavior is visible.
- `tests/test_foc_sensorless_frontend_vectors.py`
  - replays `hold_when_unlocked`;
  - checks `speed_loop_target_omega` and `speed_loop_pi_integrator` when the
    fixture provides those expected rows.

## Source-Backed Behavior

The host-side speed-loop hold rule is:

```text
if not enabled and hold_when_unlocked:
    keep previous speed-loop PI state
    keep previous target_omega_e_rad_s
    emit target_iq = 0
else:
    update target_omega ramp and speed PI normally
```

In the replay path, `enabled` is driven by `frontend.locked`:

```text
sensorless_speed_loop_step(..., enabled=frontend.locked)
```

The protected fixture is `speed_loop_pi_holds_until_lock_and_after_loss`.
With `ki = 0.5`, the expected speed-loop PI integrator row is:

```text
[0.0, 0.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0]
```

That means the PI holds at `[0.0, 0.0]` before lock, advances only after lock,
stays at `1.0` during confirmed loss and startup after loss, and resumes from
that held state after relock.

The current-loop q-axis integrator still advances only when the effective
current command passes through the lock-aware current-command policy:

```text
[0.0, 0.0, 1.5, 3.0, 4.5, 4.5, 4.5, 6.0]
```

## Subagent Protocol

Read-only helper Aquinas reviewed only the filtered host-side sensorless
frontend / replay / fixture slice. Its decision-relevant finding was that the
highest-value next gap was lock-aware speed-loop anti-windup: startup,
unlocked, and confirmed-loss steps could clamp effective `iq_ref` while the
speed PI integrator quietly accumulated error. The main agent kept all repo
writes in the owner path and used the helper output only to select this
no-power increment.

## Boundary

This is host-side no-power algorithm fixture evidence only.

It is not firmware implementation. It is not generated-code edit permission.
It is not firmware speed-loop implementation.
It is not firmware startup or loss-protection strategy.
It is not MCSDK speed-loop hook evidence.
It is not MCSDK Observer PLL equivalence.
It is not MCSDK Observer CORDIC equivalence.
It is not SMO implementation or validation.
It is not MCSDK integration.
It is not host-side / MCSDK numerical equivalence evidence.
It is not compare-register evidence.
It is not Gate PWM validation.
It is not sensorless / SMO validation.
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
- `python -m unittest tests.test_foc_sensorless_frontend tests.test_foc_sensorless_frontend_vectors`
  passed: 25 tests OK.
- `python -m unittest
  tests.test_workflow_contracts.FocCoreHostModelWorkflowTests` passed:
  29 tests OK.
- `python -m unittest tests.test_workflow_contracts` passed: 145 tests OK.
- Full `python -m unittest discover -s tests` passed: 296 tests OK.
- `python -m compileall src tests` passed.
- `python tools\check_ai_contracts.py` passed with no AI contract errors and
  the known review-lifecycle warning.
- `git diff --check` passed with only CRLF conversion warnings.
