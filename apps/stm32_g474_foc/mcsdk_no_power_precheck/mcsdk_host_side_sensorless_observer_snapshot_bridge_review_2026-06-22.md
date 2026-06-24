# MCSDK / Host-Side Sensorless Observer Snapshot Bridge Review

Date: 2026-06-22

## Decision

`MCSDK host-side sensorless observer snapshot bridge / host-side no-power semantic translation only / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record adds a downstream comparison-only snapshot for host-side sensorless
outputs:

```text
host-side sensorless theta_e_rad / omega_e_rad_s / confidence / mode / locked
-> theta_q15
-> omega_q15 using an explicit host-side full-scale value
-> confidence_q15 with clamp to [0, 1]
-> mode / locked copied as comparison metadata
```

The new bridge evidence is in:

- `src/foc_mcsdk_bridge.py`
- `tests/fixtures/foc_mcsdk_bridge_vectors.json`
- `tests/test_mcsdk_foc_bridge_vectors.py`

The bridge intentionally stays downstream of
`sensorless_current_control_replay_sequence(...)`. It does not define,
configure, or validate any MCSDK observer component.

## What It Freezes

- `McsdkObserverSnapshot` is a host-side comparison container for
  `theta_q15`, `omega_q15`, `confidence_q15`, `mode`, and `locked`.
- `sensorless_result_to_mcsdk_observer_snapshot(...)` maps host radians through
  the existing q15 angle-domain helper.
- `omega_e_rad_s` is normalized only by the caller-provided
  `omega_full_scale_rad_s`; zero or negative full-scale values are rejected.
- Confidence is clamped before q15 conversion so out-of-range host confidence
  values cannot escape the comparison snapshot.
- Replay output can feed the snapshot, but the snapshot is still semantic
  translation evidence only.

## Boundary

This is host-side no-power comparison evidence only.

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
- No Gate PWM output.
- No Motor Pilot / Profiler.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## Verification

- `python -m json.tool tests\fixtures\foc_mcsdk_bridge_vectors.json` passed.
- `python -m unittest tests.test_mcsdk_foc_bridge_vectors` passed.
- `python -m py_compile src\foc_mcsdk_bridge.py tests\test_mcsdk_foc_bridge_vectors.py`
  passed.
