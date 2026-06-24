# Host-Side No-Power Sensorless Speed / Current Command Policy Replay Review

Date: 2026-06-22

## Decision

`Host-side no-power sensorless speed/current command policy replay / lock-aware iq gating fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record extends the host-side no-power sensorless replay chain only:

```text
observer / supplied theta
-> frontend startup / tracking lock state
-> optional startup lock-loss-relock policy
-> optional host-side speed loop target_omega -> candidate iq_ref
-> lock-aware current-command policy
-> current-loop replay
-> MCSDK-shaped comparison-only speed/current snapshots
```

The increment is useful because the previous replay chain already decided where
`theta_e_rad` came from, but the current loop still accepted raw `target_iq`
even when the frontend was in startup or confirmed loss. This review freezes a
host-side policy fixture where startup / unlocked / confirmed-loss steps clamp
the effective `iq_ref` to the configured unlocked limit, while tracking / relock
steps may pass a bounded command.

## Code And Fixture

- `src/foc_sensorless_frontend.py`
  - adds `SensorlessSpeedLoopConfig`, `SensorlessSpeedLoopState`, and
    `SensorlessSpeedLoopResult`;
  - adds `sensorless_speed_loop_step(...)` as a host-side speed outer-loop
    fixture that maps target/measured electrical speed into candidate `iq_ref`;
  - adds `SensorlessCurrentCommandPolicyConfig`,
    `SensorlessCurrentCommandPolicyResult`, and
    `sensorless_current_command_policy_step(...)`;
  - extends `sensorless_current_control_step(...)` and
    `sensorless_current_control_replay_sequence(...)` with optional speed-loop
    state handoff and lock-aware current-command policy gating.
- `tests/fixtures/foc_sensorless_frontend_vectors.json`
  - adds a replay fixture covering startup before lock, tracking, short
    confidence dip, confirmed loss, startup after loss, and relock;
  - records candidate `iq_ref`, effective `iq_ref`, command reasons, and
    current-loop q-axis integrator continuity.
- `tests/test_foc_sensorless_frontend.py`
  - adds direct rule tests for speed-loop target ramp / PI behavior and
    current-command lock gating;
  - adds the end-to-end replay test for speed-loop command gating.
- `tests/test_foc_sensorless_frontend_vectors.py`
  - replays the JSON fixture against the host-side model.
- `src/foc_mcsdk_bridge.py`
  - adds `McsdkSpeedCommandSnapshot`,
    `speed_command_to_mcsdk_snapshot(...)`,
    `sensorless_result_to_mcsdk_speed_command_snapshot(...)`, and
    `sensorless_replay_to_mcsdk_speed_command_snapshots(...)`.
- `tests/fixtures/foc_mcsdk_bridge_vectors.json` and
  `tests/test_mcsdk_foc_bridge_vectors.py`
  - freeze comparison-only q15-shaped speed/current command metadata.

## Source-Backed Behavior

The new host-side replay fixture uses this rule:

```text
candidate iq_ref = host-side speed PI(target_omega - measured_omega)
if frontend locked:
    effective iq_ref = clamp(candidate iq_ref, +/- locked_iq_limit)
else:
    effective iq_ref = clamp(candidate iq_ref, +/- unlocked_iq_limit)
```

The fixture chooses `unlocked_iq_limit = 0`, so startup before lock and
confirmed loss produce `effective_target_iq = 0`. Tracking and relock pass the
bounded speed-loop `iq_ref`. The q-axis current-loop integrator therefore
accumulates only on tracking / relock steps in this fixture.

## Subagent Protocol

Read-only helper Ampere was asked for a filtered gap review. Its decision-
relevant finding was that the current host-side replay already covered
observer/frontend lock state, but not lock-aware current-command behavior. The
main agent kept all repo writes in the owner path and used the helper output
only to select this no-power increment.

## Boundary

This is host-side no-power algorithm fixture and comparison-shape evidence
only.

It is not firmware speed-loop implementation, and it is not firmware startup
or loss-protection strategy.
It is not MCSDK Observer PLL equivalence.
It is not MCSDK Observer CORDIC equivalence.
It is not SMO implementation or validation.

It is not evidence for:

- firmware implementation;
- generated-code edit permission;
- firmware speed-loop implementation;
- firmware startup or loss-protection strategy;
- MCSDK speed-loop hook;
- MCSDK Observer PLL equivalence;
- MCSDK Observer CORDIC equivalence;
- SMO implementation or validation;
- MCSDK integration;
- host-side / MCSDK numerical equivalence evidence;
- compare-register evidence;
- Gate PWM validation;
- sensorless / SMO validation;
- hardware validation;
- power-stage readiness;
- motor readiness;
- safe drive operation.

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
  must pass.
- `python -m json.tool tests\fixtures\foc_mcsdk_bridge_vectors.json` must pass.
- `python -m unittest tests.test_foc_sensorless_frontend tests.test_foc_sensorless_frontend_vectors tests.test_mcsdk_foc_bridge_vectors`
  must pass.
