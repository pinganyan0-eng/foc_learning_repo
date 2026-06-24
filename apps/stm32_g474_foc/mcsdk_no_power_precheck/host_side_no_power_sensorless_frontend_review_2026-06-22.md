# Host-Side No-Power Sensorless Frontend Review - 2026-06-22

Decision:
`Host-side no-power sensorless frontend contract / no firmware implementation / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

This review records a host-side sensorless frontend contract that fills the
existing seam before `current_control_step(...)`: the source of `theta_e_rad`.
It is intentionally a host-float-domain contract, not a claim of ST observer PLL,
CORDIC observer, or generated MCSDK equivalence.

MCSDK remains the intended motor-control framework generation path. This module
exists so the algorithm role can freeze startup-versus-tracking semantics,
angle continuity, lock/confidence behavior, and the handoff into the existing
host-side current-loop model while the hardware branch remains blocked by the
power-board-side `nFAULT = 1.3 V` fault tree.

## Scope

- Frontend module: `src/foc_sensorless_frontend.py`.
- Frontend unit test: `tests/test_foc_sensorless_frontend.py`.
- Frontend replay fixture and test:
  `tests/fixtures/foc_sensorless_frontend_vectors.json` and
  `tests/test_foc_sensorless_frontend_vectors.py`.
- Existing downstream seam:
  `src/foc_core_model.py` with externally supplied `theta_e_rad`.
- Existing comparison layer that remains downstream only:
  `src/foc_mcsdk_bridge.py`.
- Hardware state: unchanged; latest hardware blocker remains the
  STDRIVE101 PA7 / LIN1 wake `nFAULT = 1.3 V` power-board-side
  fault-isolation result and its 2026-06-22 no-power fault-tree plan.

## Frontend Contract

The frontend exposes:

- `normalize_angle_rad(theta_rad)`;
- `sensorless_startup_step(inputs, state, config)`;
- `sensorless_observer_contract_step(inputs, state, config)`;
- `sensorless_frontend_step(inputs, state, config)`;
- `sensorless_current_control_step(...)`.

The module uses host-side float-domain dataclasses only:

- `SensorlessFrontendConfig`;
- `SensorlessFrontendInputs`;
- `SensorlessFrontendState`;
- `SensorlessFrontendResult`;
- `SensorlessCurrentLoopInputs`;
- `SensorlessCurrentLoopResult`.

The intended interface sentence is:

```text
observer-like inputs or startup fallback
-> host-side theta_e_rad producer
-> existing current_control_step(...)
```

## What This Increment Freezes

- startup mode can ramp electrical speed and angle without claiming an
  observer implementation;
- tracking mode requires confidence-based lock before switching the mode to
  `tracking`;
- observer angle updates are limited by an explicit maximum step to avoid
  discontinuous host-side jumps;
- the output stays in host float units and feeds `CurrentLoopInputs.theta_e_rad`
  directly;
- the existing current-loop seam remains the only downstream consumer;
- MCSDK-shaped `theta_q15`, `qd_t`, and duty-count comparison remain a
  downstream bridge concern, not the frontend API itself.

## Covered Cases

`tests/test_foc_sensorless_frontend.py` and
`tests/fixtures/foc_sensorless_frontend_vectors.json` cover:

- negative-angle and multi-turn angle wrapping;
- startup ramp behavior without lock;
- confidence-based tracking lock;
- observer angle-step limiting before lock;
- locked frontend handoff into the existing quarter-turn current-loop path.

This increment also tightens nearby host-side boundaries:

- `tests/test_mcsdk_foc_bridge_vectors.py` now covers out-of-range `dq`
  clamp behavior in the MCSDK-shaped bridge;
- `tests/fixtures/foc_mcsdk_bridge_vectors.json` now covers negative-angle
  wrap and multi-turn angle wrap cases for `radians_to_q15`;
- `tests/test_foc_core_model.py` and
  `tests/fixtures/foc_core_golden_vectors.json` now cover an explicit
  `integrator_limit != output_limit` PI case.

## Evidence Limit

This frontend is useful as host-side no-power contract evidence only. It is
not usable to claim:

- firmware implementation;
- generated-code edit permission;
- MCSDK integration;
- MCSDK observer PLL equivalence;
- MCSDK CORDIC observer equivalence;
- host-side / MCSDK numerical equivalence evidence;
- compare-register evidence;
- Gate PWM output validation;
- Gate PWM safety;
- MCSDK hook readiness;
- Hall closed-loop behavior;
- sensorless / SMO behavior;
- sensorless / SMO validation;
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

Use this artifact when future no-power work needs one explicit host-side
contract for where `theta_e_rad` comes from before current-loop replay or
comparison translation. Do not use it to claim observer correctness, to bypass
MCSDK generation, to bypass STDRIVE101 fault isolation, or to open any powered
hardware phase gate.
