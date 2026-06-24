# MCSDK / Host-Side FOC Comparison Bridge Review - 2026-06-22

Decision:
`MCSDK host-side FOC comparison bridge / host-side no-power semantic translation only / no firmware implementation / no generated-code edit / no MCSDK integration / no PWM output / no motor readiness`.

This artifact is the next no-power increment after the host-side FOC model,
golden vectors, comparison boundary plan, and convention probe. It adds a
host-side comparison adapter so future no-power work can reuse one explicit
translation layer for MCSDK-shaped comparison semantics instead of re-deciding
field order, angle domain, and PWM representation per test.

MCSDK remains the intended motor-control framework generation path. This bridge
does not edit generated code, does not create firmware, and does not prove
host-side / MCSDK numerical equivalence.

## Scope

- Bridge module: `src/foc_mcsdk_bridge.py`.
- Bridge fixture: `tests/fixtures/foc_mcsdk_bridge_vectors.json`.
- Bridge replay test: `tests/test_mcsdk_foc_bridge_vectors.py`.
- Source anchors remain:
  `src/foc_core_model.py`,
  `tests/fixtures/foc_core_golden_vectors.json`,
  `tests/test_foc_core_vectors.py`,
  `tests/test_mcsdk_foc_pipeline_static.py`,
  and
  `tests/test_mcsdk_foc_convention_probe.py`.

This is a host-side no-power semantic translation layer only.

## Bridge Contract

The bridge exposes:

- `radians_to_q15(theta_e_rad)` for comparison-only angle-domain translation;
- `dq_to_mcsdk_qd(DQ(d, q))` for explicit `qd_t(q, d)` semantic mapping;
- `duty_to_counts(svpwm_result, pwm_period_cycles)` for conceptual duty-to-count
  translation;
- `current_loop_result_to_mcsdk_state(...)` for a comparison-ready MCSDK-shaped
  snapshot.

The bridge is intentionally semantic, not equivalence-claiming:

- it maps host radians into MCSDK q1.15 angle-domain digits;
- it maps host `DQ(d, q)` into MCSDK `qd_t(q, d)` by field meaning;
- it maps host duty floats into a conceptual timer-count layer using an
  explicit `pwm_period_cycles` argument;
- it keeps host `svpwm.saturated` and `svpwm.scale` as host-side comparison
  metadata instead of claiming MCSDK limiter identity.

## Source-Backed Translation Anchors

- MCSDK `qd_t` stores fields as `q` then `d`.
- MCSDK `MCM_Park(..., int16_t Theta)` and `MCM_Rev_Park(..., int16_t Theta)`
  use q1.15 angle input.
- MCSDK Hall and math comments elsewhere in the archived source use `65536`
  full-turn scaling and `q1.15` / `s16degree` wording for electrical angles.
- MCSDK `PWMC_SetPhaseVoltage` computes timer counts `CntPhA`, `CntPhB`, and
  `CntPhC`; the bridge treats host duty as the conceptual layer before that
  timer-count representation.

## Covered Cases

`tests/fixtures/foc_mcsdk_bridge_vectors.json` and
`tests/test_mcsdk_foc_bridge_vectors.py` cover:

- `theta_e_rad -> q1.15` translation for `0`, `pi/2`, and `pi`;
- semantic `DQ(d, q) -> qd_t(q, d)` ordering;
- host duty-to-count mapping for centered duty and positive q-axis duty;
- current-loop bridge snapshots for:
  - zero-angle positive q-axis request;
  - quarter-turn measured-current feedback that rotates into q-axis state.

## Evidence Limit

This bridge is useful as comparison-ready no-power translation evidence only.
It is not usable to claim:

- firmware implementation;
- generated-code edit permission;
- MCSDK integration;
- MCSDK convention proof;
- host-side / MCSDK numerical equivalence evidence;
- compare-register evidence;
- Gate PWM output validation;
- MCSDK hook readiness;
- hardware validation;
- power-stage readiness;
- motor readiness;
- safe drive operation.

## Safety Boundary

- No flash.
- No Run / Debug.
- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler or Motor Pilot.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
- No power-stage readiness claim.
- No motor readiness claim.

## Next Engineering Use

Use this bridge to prepare future host-side comparison cases that explicitly
separate:

- angle-domain translation;
- q/d field-order translation;
- host-side float values versus MCSDK fixed-point digits;
- duty-layer versus timer-count-layer interpretation.

Do not use it to claim that MCSDK generated code numerically matches the
host-side Python model, to bypass MCSDK generation, to bypass the STDRIVE101
fault-isolation blocker, or to open any hardware phase gate.
