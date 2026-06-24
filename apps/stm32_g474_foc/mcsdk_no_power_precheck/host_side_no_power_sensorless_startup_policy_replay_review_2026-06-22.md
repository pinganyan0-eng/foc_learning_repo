# Host-Side No-Power Sensorless Startup Policy Replay Review

Date: 2026-06-22

## Decision

`Host-side no-power sensorless startup policy replay / lock-loss-relock fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record extends the host-side sensorless replay path with an optional
startup-to-tracking policy layer:

```text
observer confidence
-> host-side lock / loss hysteresis policy
-> frontend lock override metadata
-> existing startup or tracking theta path
-> host-side current_control_step(...)
-> explicit policy, frontend, and PI state handoff into the next replay step
```

The new evidence is in:

- `src/foc_sensorless_frontend.py`
- `tests/test_foc_sensorless_frontend.py`
- `tests/test_foc_sensorless_frontend_vectors.py`
- `tests/fixtures/foc_sensorless_frontend_vectors.json`

## What It Freezes

- `SensorlessStartupPolicyConfig` holds separate lock and unlock confidence
  thresholds plus required consecutive high-confidence / low-confidence counts.
- `SensorlessStartupPolicyState` carries `tracking_enabled`,
  `lock_candidate_count`, and `loss_candidate_count` across replay steps.
- `SensorlessStartupPolicyResult` exposes the policy counters and the
  comparison-only frontend lock override for each host-side replay step.
- `sensorless_startup_policy_step(...)` requires consecutive lock candidates
  before tracking is enabled and consecutive loss candidates before tracking is
  disabled.
- `sensorless_current_control_step(...)` and
  `sensorless_current_control_replay_sequence(...)` can optionally carry the
  startup policy state without changing the earlier replay API behavior when
  no policy is supplied.
- The JSON fixture now covers startup ramp, pending lock, confirmed tracking,
  a short confidence dip that does not immediately unlock, confirmed loss,
  return to startup ramp, relock, and PI integrator continuity.

## Subagent Protocol

The main agent requested a read-only Bernoulli helper review for the next
sensorless host-side increment and kept all writes in the owner path. The
implemented increment is the host-side startup-to-tracking policy fixture
because it fills the gap between single-step lock behavior and downstream
MCSDK-shaped snapshot metadata.

## Boundary

This is host-side no-power algorithm fixture evidence only.

It is not evidence for:

- not firmware implementation;
- not firmware startup state machine;
- not generated-code edit permission;
- not MCSDK Observer PLL equivalence;
- not MCSDK Observer CORDIC equivalence;
- not SMO implementation or validation;
- not MCSDK integration;
- not host-side / MCSDK numerical equivalence evidence;
- not compare-register evidence;
- not Gate PWM validation;
- not sensorless / SMO validation;
- not hardware validation;
- not power-stage readiness;
- not motor readiness;
- not safe drive operation.

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
  passed: 18 tests OK.
