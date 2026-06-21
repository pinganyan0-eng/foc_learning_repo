# Host-Side No-Power FOC Golden Vectors Review - 2026-06-22

Decision:
`Host-side no-power FOC golden vectors / no firmware implementation / no MCSDK integration / no PWM output / no motor readiness`.

This review records replayable host-side FOC math vectors for the current
Python reference model. These vectors are host-side no-power regression fixtures for Clarke / Park / PI / inverse Park / zero-sequence duty math.

They do not configure TIM1.
They do not write compare registers.
They do not drive gates.
They do not validate PWM safety.
They do not integrate with MCSDK or change the current STDRIVE101
fault-isolation / no-motor boundary.

The vectors intentionally freeze the current host-side Python convention only.
They are not proof that MCSDK generated code uses the same sign convention,
scaling convention, duty representation, timing, or saturation behavior.

## What Was Added

- `tests/fixtures/foc_core_golden_vectors.json`
  - records transform, PI, host-side SVPWM-style duty, and current-loop cases;
  - records expected values for the current Python reference model;
  - records negative evidence boundaries in metadata.
- `tests/test_foc_core_vectors.py`
  - loads the JSON fixture;
  - replays each vector through `src/foc_core_model.py`;
  - checks expected transform values, duty math, PI state, and current-loop
    state.

## Covered Scenarios

- Clarke transform for a general zero-sum phase-current sample.
- Park / inverse Park angle-wrap round trip.
- Host-side SVPWM zero vector, positive alpha vector, positive q / beta
  vector, negative q / beta vector, and large-vector saturation with `scale`.
- PI proportional plus integral output, `dt_s = 0`, anti-windup hold,
  integrator unwind, and externally supplied prior-integrator clamp.
- Current-loop zero-error centered duty.
- Current-loop positive and negative q-axis requests.
- Current-loop measured current at nonzero electrical angle.
- Two-step current-loop integrator accumulation.

## Evidence Limit

This artifact is useful as a no-power algorithm regression contract. It is not
usable to claim:

- firmware implementation;
- MCSDK generated-code integration;
- MCSDK hook readiness;
- ADC sampling correctness;
- OPAMP / PGA configuration correctness;
- TIM1 configuration correctness;
- compare-register values;
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

Use these vectors to compare future host-side refactors or a separately
reviewed MCSDK / firmware-side convention probe. Do not use them to bypass
MCSDK generation, STDRIVE101 fault isolation, no-power gates, or
teacher-reviewed hardware phase gates.
