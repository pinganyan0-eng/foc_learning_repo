# Host-Side No-Power Sensorless Observer Stub Review - 2026-06-22

Decision:
`Host-side no-power sensorless observer stub / alpha-beta back-EMF contract only / no firmware implementation / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

This review records the next host-side algorithm increment after the
sensorless frontend seam. The repo now has a deterministic alpha-beta
back-EMF observer stub that consumes `v_alpha`, `v_beta`, `i_alpha`, and
`i_beta`, estimates a bounded host-float `theta_e_rad`, computes a host-side
`omega_e_rad_s`, and emits a confidence value for the existing frontend lock
contract.

The implementation is intentionally a learning / replay contract. It is not a
claim that ST MCSDK Observer PLL, Observer CORDIC, or an SMO implementation is
numerically equivalent to this model.
It is not MCSDK Observer PLL equivalence.
It is not MCSDK Observer CORDIC equivalence.
It is not SMO implementation or validation.

## Scope

- Frontend / observer module: `src/foc_sensorless_frontend.py`.
- Frontend / observer unit tests: `tests/test_foc_sensorless_frontend.py`.
- Replay fixture and test:
  `tests/fixtures/foc_sensorless_frontend_vectors.json` and
  `tests/test_foc_sensorless_frontend_vectors.py`.
- Existing downstream current-loop seam:
  `src/foc_core_model.py`.
- Existing downstream MCSDK-shaped comparison layer:
  `src/foc_mcsdk_bridge.py`.
- Hardware state: unchanged. The current hardware blocker remains the
  STDRIVE101 PA7 / LIN1 wake `nFAULT = 1.3 V` power-board-side
  fault-isolation result and its 2026-06-22 no-power fault-tree plan.

## Observer Stub Contract

The added host-side observer layer exposes:

- `SensorlessObserverConfig`;
- `SensorlessObserverState`;
- `SensorlessObserverResult`;
- `back_emf_observer_step(inputs, state, config)`.

The observer stub computes:

```text
back_emf_alpha = v_alpha - Rs * i_alpha
back_emf_beta  = v_beta  - Rs * i_beta
candidate theta = atan2(back_emf_beta, back_emf_alpha) + configured offset
```

Then it applies:

- angle wrapping into the host `0..2*pi` electrical-angle domain;
- shortest-path angle delta calculation;
- maximum angle-step limiting;
- confidence from back-EMF magnitude against a configured full-scale voltage;
- separate confidence rise and decay filters;
- optional omega filtering.

The output is routed into the existing `sensorless_frontend_step(...)` lock and
blend contract. Existing explicit `observer_theta_e_rad` inputs still take
priority over the stub, so the new layer does not break the prior frontend API.

## Current-Loop Handoff

`sensorless_current_control_step(...)` can now run this host-side path:

```text
phase currents -> Clarke i_alpha/i_beta
v_alpha/v_beta + i_alpha/i_beta -> back_emf_observer_step(...)
observer theta / omega / confidence -> sensorless_frontend_step(...)
frontend theta_e_rad -> current_control_step(...)
```

This is still a host-side replay chain only. It does not configure ADC,
voltage reconstruction, PWM compare registers, MCSDK speed feedback, or any
firmware runtime path.

## Covered Cases

`tests/test_foc_sensorless_frontend.py` and
`tests/fixtures/foc_sensorless_frontend_vectors.json` now cover:

- valid alpha-beta back-EMF vector producing a lock-capable confidence;
- angle wrapping with shortest-path limited step;
- low-signal confidence decay;
- external observer input priority / compatibility with the prior frontend;
- observer stub feeding the frontend and current-loop model;
- current-loop result remaining bridgeable through the existing MCSDK-shaped
  comparison layer.

## Subagent Protocol

Read-only helper Bernoulli inspected the current frontend and identified the
smallest next no-power increment as an alpha-beta back-EMF observer stub that
uses the already reserved `i_alpha`, `i_beta`, `v_alpha`, and `v_beta` fields.
The main agent kept all repo writes in the owner path and used the helper
result only as filtered evidence.

## Evidence Limit

This observer stub is useful as host-side no-power algorithm fixture evidence
only. It is not usable to claim:

- firmware implementation;
- generated-code edit permission;
- MCSDK integration;
- MCSDK Observer PLL equivalence;
- MCSDK Observer CORDIC equivalence;
- SMO implementation or SMO validation;
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

Use this artifact when future no-power work needs a replayable host-side
observer-output source before current-loop replay or downstream MCSDK-shaped
translation. Do not use it to claim observer correctness on hardware, to bypass
MCSDK generation, to bypass STDRIVE101 fault isolation, or to open any powered
hardware phase gate.
