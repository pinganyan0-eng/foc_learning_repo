# MCSDK / Host-Side Sensorless Observer Snapshot Sequence Bridge Review

Date: 2026-06-22

## Decision

`MCSDK host-side sensorless observer snapshot sequence bridge / host-side no-power replay-step semantic translation only / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record extends the downstream comparison-only bridge from a single
host-side sensorless output to every step in a replay result:

```text
SensorlessReplayResult.steps
-> per-step host-side sensorless theta_e_rad / omega_e_rad_s / confidence / mode / locked
-> per-step McsdkObserverSnapshot tuple
-> theta_q15 / omega_q15 / confidence_q15 / mode / locked comparison metadata
```

The new bridge evidence is in:

- `src/foc_mcsdk_bridge.py`
- `tests/fixtures/foc_mcsdk_bridge_vectors.json`
- `tests/test_mcsdk_foc_bridge_vectors.py`

The sequence bridge intentionally stays downstream of
`sensorless_current_control_replay_sequence(...)`. It does not define,
configure, implement, or validate any MCSDK observer component.

## What It Freezes

- `sensorless_replay_to_mcsdk_observer_snapshots(...)` maps each
  `SensorlessReplayResult` step into a `McsdkObserverSnapshot`.
- The function reuses `sensorless_result_to_mcsdk_observer_snapshot(...)`, so
  q15 angle, omega full-scale, confidence clamp, mode, and locked semantics
  stay aligned with the existing single-step bridge.
- The bridge vector fixture now covers a host-side startup-policy replay
  sequence across startup ramp, pending lock, tracking, short confidence dip,
  confirmed loss, startup after loss, and relock.
- The expected snapshots freeze only comparison metadata for each replay step;
  they do not claim MCSDK internal Observer PLL / CORDIC state coverage.

## Subagent Protocol

The main agent requested a filtered, read-only Anscombe helper review for the
specific bridge gap. The helper confirmed that the repo already had replay
steps plus a single-output snapshot bridge, but not a one-call per-step
snapshot bridge. The main agent kept all repo writes and final decisions in
the owner path.

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
- `python -m unittest tests.test_mcsdk_foc_bridge_vectors` passed: 10 tests OK.
