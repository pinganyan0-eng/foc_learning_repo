# Host-Side No-Power Signed Reverse Speed / Current Command Fixture Review

Date: 2026-06-23

## Decision

`Host-side no-power signed reverse speed/current command fixture / signed speed and iq replay only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record extends only the host-side no-power sensorless speed/current
command fixture chain. It proves that the existing host-side speed-loop and
current-command policy can preserve signed reverse command semantics in tests:

```text
negative target_omega
-> negative speed-loop error
-> negative candidate iq_ref
-> symmetric locked iq clamp
-> negative effective iq_ref
-> negative q-axis current-loop PI movement
-> signed MCSDK-shaped comparison snapshot
```

The increment deliberately does not change startup-ramp semantics. As of this
record, `SensorlessFrontendConfig.startup_target_omega_e_rad_s` is still
non-negative in the host-side startup contract. Reverse startup behavior
therefore remains a separate, broader semantic decision.

## Code And Fixture

- `tests/test_foc_sensorless_frontend.py`
  - adds `test_speed_loop_supports_signed_reverse_target_and_integrator`;
  - extends current-command policy coverage with a negative locked command
    clamped to `-1.5`;
  - adds
    `test_replay_sequence_preserves_signed_reverse_speed_current_command`.
- `tests/fixtures/foc_sensorless_frontend_vectors.json`
  - adds
    `signed_reverse_speed_current_command_holds_until_lock_and_after_loss`;
  - records negative `target_omega_e_rad_s = -20.0`;
  - records `speed_loop_target_iq` as
    `[0.0, 0.0, -1.5, -2.0, -2.0, 0.0, 0.0, -2.0]`;
  - records `effective_target_iq` as
    `[0.0, 0.0, -1.5, -1.5, -1.5, 0.0, 0.0, -1.5]`;
  - records q-axis current-loop integrator movement as
    `[0.0, 0.0, -1.5, -3.0, -4.5, -4.5, -4.5, -6.0]`.
- `tests/fixtures/foc_mcsdk_bridge_vectors.json`
  - adds
    `reverse_tracking_speed_command_snapshot_preserves_signed_q15`;
  - freezes comparison-only signed q15 metadata:
    `target_omega_q15 = -32768`,
    `measured_omega_q15 = -16384`,
    `requested_iq_q15 = -24576`, and
    `effective_iq_q15 = -24576`.
- `tests/test_foc_sensorless_frontend_vectors.py` and
  `tests/test_mcsdk_foc_bridge_vectors.py`
  - keep the fixture metadata explicit that this is host-side no-power
    evidence only.

## Source-Backed Behavior

The host-side signed command rule already existed in the source:

```text
ramped_target = _ramp_target_omega(...)
error = ramped_target - measured_omega
candidate iq_ref = speed PI(error)
effective iq_ref = clamp(candidate iq_ref, +/- locked_iq_limit)
```

The new fixture freezes the reverse branch of that rule. Startup and confirmed
loss still hold the speed-loop PI when `hold_when_unlocked = true`; locked
steps carry the negative speed-loop result through the symmetric current
command clamp.

## Subagent Protocol

Read-only helper Hypatia reviewed the filtered signed-speed / reverse-command
slice and found that the smallest high-value gap was test and fixture evidence,
not a startup-contract change. The main agent kept all repo writes in the owner
path and used the helper digest only to choose this no-power increment.

## Boundary

This is host-side no-power algorithm fixture and comparison-shape evidence
only.

It is not firmware.
It is not a firmware reverse-startup strategy.
It is not MCSDK integration.
It is not MCSDK numerical equivalence.
It is not generated-code edit permission.
It is not MCSDK speed-loop hook evidence.
It is not MCSDK Observer PLL equivalence.
It is not MCSDK Observer CORDIC equivalence.
It is not SMO implementation or validation.
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
- `python -m json.tool tests\fixtures\foc_mcsdk_bridge_vectors.json` passed.
- `python -m unittest tests.test_foc_sensorless_frontend tests.test_foc_sensorless_frontend_vectors tests.test_mcsdk_foc_bridge_vectors`
  passed: 40 tests OK.
