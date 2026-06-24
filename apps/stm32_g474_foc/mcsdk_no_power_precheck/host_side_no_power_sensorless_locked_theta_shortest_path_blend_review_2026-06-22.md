# Host-Side No-Power Sensorless Locked-Theta Shortest-Path Blend Review

Date: 2026-06-22

## Decision

`Host-side no-power sensorless locked-theta shortest-path blend / wrap-boundary tracking fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record extends only the host-side no-power sensorless frontend contract.
When the frontend is locked and blends the previous host-side electrical angle
with the observer electrical angle, it now blends along the shortest wrapped
angle delta instead of linearly averaging absolute radians.

The increment is useful because the previous locked branch could mis-blend
across the `0 / 2*pi` boundary. For example, a previous angle near `6.1 rad`
and an observer angle near `0.1 rad` should stay near the wrap boundary, not
jump toward `pi`.

## Code And Fixture

- `src/foc_sensorless_frontend.py`
  - updates `sensorless_observer_contract_step(...)` locked tracking behavior
    to call `_shortest_angle_delta_rad(...)` before applying
    `lock_blend_factor`.
- `tests/test_foc_sensorless_frontend.py`
  - adds `test_tracking_mode_blends_theta_across_wrap_by_shortest_path`.
- `tests/fixtures/foc_sensorless_frontend_vectors.json`
  - adds `tracking_lock_blends_across_wrap_by_shortest_path`.
- `tests/test_foc_sensorless_frontend_vectors.py`
  - replays the JSON fixture through the existing frontend vector test.

## Source-Backed Behavior

The host-side tracking rule is now:

```text
delta = shortest_wrapped_delta(observer_theta, previous_theta)
theta = normalize(previous_theta + lock_blend_factor * delta)
```

The new fixture freezes:

```text
previous theta = 6.1 rad
observer theta = 0.1 rad
lock_blend_factor = 0.5
expected theta = 6.241592653589793 rad
```

## Subagent Protocol

Read-only helper Schrodinger found the wrap-boundary gap while reviewing only
the current host-side sensorless frontend / bridge files and fixtures. The
main agent kept all repo writes in the owner path and used the helper output
only as filtered evidence for selecting this no-power increment.

## Boundary

This is host-side no-power algorithm fixture evidence only.

It is not firmware implementation. It is not generated-code edit permission.
It is not MCSDK Observer PLL equivalence. It is not MCSDK Observer CORDIC
equivalence. It is not SMO implementation or validation. It is not MCSDK
integration. It is not host-side / MCSDK numerical equivalence evidence. It is
not compare-register evidence. It is not Gate PWM validation. It is not
sensorless / SMO validation. It is not hardware validation. It is not
power-stage readiness. It is not motor readiness.

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
- `python -m unittest tests.test_foc_sensorless_frontend tests.test_foc_sensorless_frontend_vectors`
  must pass.
