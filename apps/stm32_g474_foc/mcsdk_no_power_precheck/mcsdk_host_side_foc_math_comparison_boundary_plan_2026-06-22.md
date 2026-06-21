# MCSDK / Host-Side FOC Math Comparison Boundary Plan - 2026-06-22

Decision:
`MCSDK host-side FOC math comparison boundary plan / no firmware implementation / no MCSDK integration / no PWM output / no motor readiness`.

This plan answers the current project question: MCSDK remains the intended motor-control framework generation path. The host-side Python FOC model and golden vectors are learning and no-power regression evidence only; they do not replace MCSDK generation.

This is a read-only generated-source pipeline bridge and comparison boundary
plan. It records how a future no-power comparison may inspect MCSDK generated
source against `src/foc_core_model.py`,
`tests/fixtures/foc_core_golden_vectors.json`, and
`tests/test_foc_core_vectors.py`.

It does not modify generated MCSDK source, does not create firmware code, does
not run the generated project, and does not prove that MCSDK generated code
matches the Python model.

## Source Evidence

- Archived generated source snapshot:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`.
- Generated current-loop entry:
  `Src/mc_tasks_foc.c`, function `FOC_CurrControllerM1`.
- Generated math entry points:
  `Src/mc_math.c` and `Inc/mc_math.h` expose `MCM_Clarke`, `MCM_Park`, and
  `MCM_Rev_Park`.
- Generated current-loop state clues:
  `Src/mc_config.c` wires `PIDIqHandle_M1`, `PIDIdHandle_M1`,
  `CircleLimitationM1`, and `FOCVars`.
- Generated data-type clues:
  `Inc/mc_type.h` defines `qd_t`, `alphabeta_t`, and `FOCVars_t`.
- Generated PWM voltage-setting clue:
  `Src/pwm_curr_fdbk.c` implements `PWMC_SetPhaseVoltage`.
- Generated scaling clues:
  `Inc/drive_parameters.h` and `Inc/parameters_conversion.h` define
  `PID_TORQUE_*`, `PID_FLUX_*`, `TF_KPDIV`, `TF_KIDIV`,
  `PWM_PERIOD_CYCLES`, and `MAX_MODULE`.

## Pipeline Shape Confirmed

The archived generated source shows the MCSDK current-loop pipeline in this
order:

```text
PWMC_GetPhaseCurrents -> MCM_Clarke -> MCM_Park -> PI_Controller -> Circle_Limitation -> MCM_Rev_Park -> PWMC_SetPhaseVoltage
```

This confirms the generated source has the expected FOC pipeline shape:
phase-current readback, Clarke transform, Park transform, d/q current
regulation, voltage-vector limitation, reverse Park, and a PWM voltage-setting
entry point.

This is source-shape evidence only. It is not host-side / MCSDK numerical
equivalence evidence.

## Comparison Rules

A future comparison may compare only sign, scaling, saturation, duty representation, and naming assumptions.

Required caution points:

- MCSDK `qd_t` stores fields as `q` then `d`; the Python model exposes
  `DQ(d, q)`, so mapping by field name is mandatory.
- MCSDK `MCM_Park` and `MCM_Rev_Park` use fixed-point electrical angle input
  and CORDIC-derived sine/cosine; the Python model uses radians.
- MCSDK PI gains are generated fixed-point parameters such as
  `PID_TORQUE_*`, `PID_FLUX_*`, `TF_KPDIV`, and `TF_KIDIV`; they are not
  direct Python floating-point `kp` / `ki` values.
- MCSDK `Circle_Limitation` uses `MAX_MODULE` / `MaxVd` fixed-point voltage
  limits; it is not automatically identical to the Python `svpwm(...).scale`
  behavior.
- MCSDK `PWMC_SetPhaseVoltage` computes sector and `CntPhA/B/C` timer-count
  values; those are not the same representation as the Python 0-to-1 duty
  fixture values.

## Host-Side Boundary

The host-side Python model currently provides:

- `clarke_abc`;
- `park`;
- `pi_step`;
- `inverse_park`;
- host-side zero-sequence duty math through `svpwm`;
- golden vectors in `tests/fixtures/foc_core_golden_vectors.json`.

Those artifacts are useful as no-power learning and regression fixtures. They
are not proof that MCSDK generated code matches the Python model.

Future comparison work must keep these as two separate layers:

- MCSDK generated source owns the firmware framework, scheduler, fixed-point
  types, generated PI handles, circle limitation, current-feedback path, and
  PWM voltage-setting entry point.
- Host-side Python owns only an educational floating-point math model and
  repeatable regression vectors.

## What This Allows

- A future no-power convention comparison checklist can inspect `mc_math.c`,
  `mc_tasks_foc.c`, `mc_config.c`, `mc_type.h`, `drive_parameters.h`,
  `parameters_conversion.h`, and `pwm_curr_fdbk.c` against the host-side
  vectors.
- A future host-side helper may translate MCSDK fixed-point source-level clues
  into comparable no-power cases only after a separate review.
- The project can explain to a teacher that MCSDK is still the one-click
  framework generation path, while the Python model exists to make the
  algorithm role understand and regression-check the math.

## What This Does Not Allow

This review is not usable to claim:

- not firmware implementation;
- generated-code edit permission;
- not MCSDK integration;
- MCSDK hook readiness;
- MCSDK convention proof;
- host-side / MCSDK sign or scaling equivalence;
- ADC sampling correctness;
- OPAMP / PGA configuration correctness;
- TIM1 configuration correctness;
- not compare-register evidence;
- not Gate PWM validation;
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

Use this plan to create a future no-power MCSDK convention probe. Do not use it
to bypass Workbench/MCSDK generation, edit generated firmware, bypass the
STDRIVE101 `nFAULT = 1.3 V` fault-isolation blocker, or open any hardware
phase gate.
