# Host-Side No-Power FOC Algorithm Model Review - 2026-06-22

Decision:
`Host-side no-power FOC algorithm model / no firmware implementation / no MCSDK integration / no PWM output / no motor readiness`.

This review records a Python host-side reference model for the FOC math path.
It exists so the algorithm role can learn and regression-test the control
pipeline while the STDRIVE101 / power-board fault remains blocked. It is not a
replacement for ST MCSDK project generation.
It is not firmware implementation.

MCSDK remains the intended motor-control framework generation path. This model
is a learning and test artifact for transforms, PI behavior, voltage-vector
math, and data-flow naming before any firmware integration review.

## Scope

- Model path: `src/foc_core_model.py`.
- Test path: `tests/test_foc_core_model.py`.
- Evidence level: host-side no-power software evidence only.
- Hardware state: unchanged; latest hardware blocker remains the
  STDRIVE101 PA7 / LIN1 wake `nFAULT = 1.3 V` power-board-side fault-isolation
  result.

## Model Contract

The host model exposes:

- `clarke_abc(i_a, i_b, i_c)`;
- `inverse_clarke(alpha, beta)`;
- `park(alpha, beta, theta_e_rad)`;
- `inverse_park(d_axis, q_axis, theta_e_rad)`;
- `svpwm(alpha, beta, vbus)`;
- `pi_step(error, dt_s, state, config)`;
- `current_control_step(inputs, gains, state)`.

`svpwm` is a host-side zero-sequence injection model. It is not a timer driver,
does not configure TIM1, and does not write compare registers.

## Implemented Flow

```text
phase current samples
-> Clarke transform
-> Park transform
-> d/q PI current control
-> inverse Park transform
-> host-side SVPWM duty calculation
```

## Test Coverage

`tests/test_foc_core_model.py` covers:

- balanced three-phase Clarke mapping;
- inverse Clarke round trip for zero-sum phase currents;
- Park / inverse Park round trip;
- positive quarter-turn Park sign convention;
- zero-vector centered duties;
- zero-sequence duty placement;
- large-vector scaling into duty limits;
- invalid `vbus` rejection;
- PI proportional plus integral behavior;
- PI anti-windup hold behavior;
- externally supplied prior-integrator clamp;
- current-loop zero-error centered duty output;
- q-axis current request phase-duty direction.

## Evidence Limit

This model is useful as a host-side FOC math reference and learning regression
test. It is not usable to claim:

- firmware implementation;
- MCSDK generated-code integration;
- MCSDK hook readiness;
- ADC sampling correctness;
- OPAMP / PGA configuration correctness;
- TIM1 configuration correctness;
- firmware runtime behavior;
- Gate PWM output validation;
- Gate PWM safety;
- Motor Pilot readiness;
- Motor Profiler readiness;
- Hall closed-loop behavior;
- sensorless / SMO behavior;
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
- No power-stage readiness or motor readiness claim.

## Next Engineering Use

Use this artifact to explain the FOC control pipeline and to compare future
MCSDK-generated or firmware-side behavior against a simple host-side reference.
Do not use it to bypass MCSDK generation, STDRIVE101 fault isolation, no-power
gate checks, or teacher-reviewed hardware phase gates.
