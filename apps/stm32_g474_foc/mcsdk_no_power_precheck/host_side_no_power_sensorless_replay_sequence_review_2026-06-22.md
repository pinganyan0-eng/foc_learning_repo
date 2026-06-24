# Host-Side No-Power Sensorless Replay Sequence Review

Date: 2026-06-22

## Decision

`Host-side no-power sensorless multi-step replay / observer-frontend-current-loop state-continuity fixture only / no firmware implementation / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record extends the existing host-side sensorless frontend and observer-stub
contract with a short multi-step replay harness:

```text
phase currents
-> Clarke i_alpha / i_beta
-> deterministic alpha-beta back-EMF observer stub
-> host-float sensorless frontend lock contract
-> host-side current_control_step(...)
-> explicit state handoff into the next replay step
```

The new replay evidence is in:

- `src/foc_sensorless_frontend.py`
- `tests/test_foc_sensorless_frontend.py`
- `tests/test_foc_sensorless_frontend_vectors.py`
- `tests/fixtures/foc_sensorless_frontend_vectors.json`

## What It Freezes

- `sensorless_current_control_replay_sequence(...)` returns all step results
  plus the final `SensorlessFrontendState`, `CurrentLoopState`, and optional
  `SensorlessObserverState`.
- Empty replay preserves the caller-provided frontend, current-loop, and
  observer states.
- Multi-step replay carries the observer stub state into the next step instead
  of restarting `theta_e_rad`, `omega_e_rad_s`, or confidence.
- Multi-step replay carries the current-loop PI state forward instead of
  resetting the d/q integrators.
- The JSON fixture now includes a three-step state-continuity sequence covering
  low-confidence startup, later observer lock, continued tracking, and
  PI integrator carryover.

## Subagent Protocol

Read-only helper Bernoulli compared two next increments:

- multi-step replay / harness proving state continuity; and
- MCSDK-shaped observer-output translation snapshot.

The helper recommended the multi-step replay because the current repo already
has a host-side MCSDK-shaped current-loop bridge, while the sensorless path
still needed sequence-level evidence for observer, frontend, and PI state
handoff. The main agent kept all repo writes in the owner path and used the
helper output only as filtered evidence.

## Boundary

This is host-side no-power algorithm fixture evidence only.

It is not evidence for:

- not firmware implementation;
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
- no Gate PWM output.
- No Motor Pilot / Profiler.
- No Hall closed-loop claim.
- no sensorless / SMO claim.

## Verification

- `python -m json.tool tests\fixtures\foc_sensorless_frontend_vectors.json`
  passed.
- `python -m unittest tests.test_foc_sensorless_frontend` passed.
- `python -m unittest tests.test_foc_sensorless_frontend_vectors` passed.
- `python -m py_compile src\foc_sensorless_frontend.py tests\test_foc_sensorless_frontend.py tests\test_foc_sensorless_frontend_vectors.py`
  passed.
