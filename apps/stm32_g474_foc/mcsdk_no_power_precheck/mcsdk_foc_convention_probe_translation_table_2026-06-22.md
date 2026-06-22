# MCSDK FOC Convention Probe Translation Table - 2026-06-22

Decision:
`MCSDK FOC convention probe / translation table / host-side no-power generated-source convention mapping only / no firmware implementation / no generated-code edit / no MCSDK integration / no PWM output / no motor readiness`.

This artifact is the next no-power increment after the host-side FOC model,
golden vectors, and pipeline boundary plan. It makes the archived MCSDK
generated-source conventions explicit before any future no-power comparison
against `src/foc_core_model.py`.

MCSDK remains the intended motor-control framework generation path. This table
does not replace MCSDK, does not edit generated code, does not create firmware,
and does not prove host-side / MCSDK numerical equivalence.

## Scope

This is a host-side no-power generated-source convention probe and translation
table only. It may describe source-backed naming, field order, sign direction,
angle representation, PI parameter style, and PWM representation clues from the
archived generated project.

Host `clarke_abc` is one comparison anchor for the translation rows below.
Host `DQ(d, q)` dataclass is another comparison anchor for rotor-frame naming.
MCSDK `MCM_Clarke`: `Output.alpha = Input.a;`.
MCSDK `qd_t` stores fields as `q` then `d`.
MCSDK `MCM_Park` writes `Output.q` before `Output.d`.
MCSDK `PWMC_SetPhaseVoltage` computes sector plus `CntPhA`, `CntPhB`, `CntPhC` timer counts.
This is not MCSDK convention proof beyond explicitly source-backed rows.
This is not host-side / MCSDK numerical equivalence evidence.
This is not compare-register evidence.
This is not Gate PWM validation.
This is not MCSDK hook readiness.
This is not hardware validation.

It is not:

- firmware implementation;
- generated-code edit permission;
- MCSDK integration;
- MCSDK convention proof beyond explicitly source-backed rows;
- host-side / MCSDK numerical equivalence evidence;
- compare-register evidence;
- Gate PWM validation;
- MCSDK hook readiness;
- hardware validation;
- power-stage readiness;
- motor readiness.

## Source Packet

- Archived generated snapshot:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`
- Main reviewed files:
  `Src/mc_math.c`
  `Src/mc_tasks_foc.c`
  `Src/mc_config.c`
  `Src/pwm_curr_fdbk.c`
  `Inc/mc_type.h`
  `Inc/drive_parameters.h`
  `Inc/parameters_conversion.h`
- Host-side comparison references:
  `src/foc_core_model.py`
  `tests/fixtures/foc_core_golden_vectors.json`
  `tests/test_foc_core_vectors.py`
  `tests/test_mcsdk_foc_pipeline_static.py`

## Translation Table

| Topic | Host-side reference | MCSDK generated-source clue | Translation rule | Boundary |
| --- | --- | --- | --- | --- |
| Clarke input shape | `clarke_abc(i_a, i_b, i_c)` uses three-shunt phase samples | `PWMC_GetPhaseCurrents` feeds `MCM_Clarke` through `ab_t Input` | Treat both as current-loop current-transform stage clues only | Not ADC/current-sampling correctness evidence |
| Clarke alpha | `alpha = (2*a-b-c)/3` | `MCM_Clarke`: `Output.alpha = Input.a;` | Do not assume identical alpha scaling; map as different representation candidates | Not host-side / MCSDK numerical equivalence evidence |
| Clarke beta sign/form | `beta = (b-c)/sqrt(3)` | `MCM_Clarke` derives beta from `-(a_divSQRT3_tmp) - (b_divSQRT3_tmp) - (b_divSQRT3_tmp)` with saturation handling | Treat beta sign and scaling as a source-backed comparison checkpoint | Not MCSDK convention proof beyond this row |
| Rotor-frame data shape | `DQ(d, q)` dataclass exposes `d` then `q` | `qd_t` fields are `int16_t q;` then `int16_t d;` | Mapping must be by field name, not positional order | Not firmware hook evidence |
| Park output order | `park(...) -> DQ(d, q)` | `MCM_Park` writes `Output.q` before `Output.d` | Translate MCSDK result into host-side semantic names before comparing values | Not host-side / MCSDK numerical equivalence evidence |
| Park formula family | `d = alpha*cos + beta*sin`, `q = -alpha*sin + beta*cos` | `MCM_Park` computes `Output.q` from `alpha*cos - beta*sin` and `Output.d` from `alpha*sin + beta*cos` | Compare sign/layout after reconciling q-first field order and fixed-point scaling | Not MCSDK convention proof beyond explicitly source-backed rows |
| Reverse Park family | `inverse_park(d, q)` returns `alpha = d*cos - q*sin`, `beta = d*sin + q*cos` | `MCM_Rev_Park` uses `alpha = q*cos + d*sin`, `beta = d*cos - q*sin` after MCSDK `qd_t` conventions | Translate through MCSDK q-first field semantics before comparing formulas | Not host-side / MCSDK numerical equivalence evidence |
| Angle representation | Host uses `theta_e_rad` in radians | `MCM_Park(..., int16_t Theta)` and `MCM_Trig_Functions(int16_t hAngle)` use fixed-point angle input | Future comparison must explicitly convert angle representation; no direct radian equality assumption | Not MCSDK hook readiness |
| Current-loop PI callsite | Host uses float `pi_step(error, dt_s, state, config)` | `FOC_CurrControllerM1` uses `Vqd.q = PI_Controller(... Iqdref.q - Iqd.q)` and `Vqd.d = PI_Controller(... Iqdref.d - Iqd.d)` | Translate as q-axis and d-axis error channels, not as direct float gain equivalence | Not firmware implementation |
| PI parameter style | Host config uses float `kp`, `ki`, `output_limit`, `integrator_limit` | MCSDK uses `PID_TORQUE_*`, `PID_FLUX_*`, `TF_KPDIV`, `TF_KIDIV`, and `INT16_MAX * TF_KIDIV` limits | Treat MCSDK PI gains as generated fixed-point parameterization, not direct host-side gains | Not host-side / MCSDK numerical equivalence evidence |
| Circle limitation | Host `svpwm(...).scale` reports host-side saturation scale only | `CircleLimitationM1` uses `.MaxModule = MAX_MODULE` and `.MaxVd = (MAX_MODULE * 950) / 1000` | Translate as different voltage-limiting representation layers | Not compare-register evidence |
| PWM representation | Host `svpwm` returns duty floats in `[0,1]` | `PWMC_SetPhaseVoltage` computes sector plus `CntPhA`, `CntPhB`, `CntPhC` timer counts | Compare host duty only as a conceptual output layer, not as compare-register identity | Not Gate PWM validation |
| PWM alpha/beta entry | Host passes float `alpha`, `beta` into `svpwm` | `PWMC_SetPhaseVoltage(PWMC_Handle_t*, alphabeta_t Valfa_beta)` uses `wUAlpha` and `wUBeta` | Translate as alpha-beta voltage-vector entry to timer-count synthesis | Not hardware validation |
| FOC state struct | Host current-loop result is Python dataclasses | `FOCVars_t` includes `Ialphabeta`, `Iqd`, `Iqdref`, `Vqd`, `Valphabeta` | Use these names as source-backed state correspondence clues only | Not firmware runtime evidence |

## Source-Backed Rows

The following rows are directly backed by the archived source text:

- `MCM_Clarke`: `Output.alpha = Input.a;`
- `qd_t`: `int16_t q;` then `int16_t d;`
- `FOC_CurrControllerM1` order:
  `PWMC_GetPhaseCurrents -> MCM_Clarke -> MCM_Park -> PI_Controller -> Circle_Limitation -> MCM_Rev_Park -> PWMC_SetPhaseVoltage`
- PI callsites:
  `Vqd.q = PI_Controller(... Iqdref.q - Iqd.q)`
  `Vqd.d = PI_Controller(... Iqdref.d - Iqd.d)`
- PI divisors:
  `TF_KPDIV = 128`
  `TF_KIDIV = 4096`
- Example generated gains:
  `PID_TORQUE_KP_DEFAULT = 2071`
  `PID_FLUX_KP_DEFAULT = 2071`
- Circle limitation:
  `.MaxModule = MAX_MODULE`
  `.MaxVd = (MAX_MODULE * 950) / 1000`
- PWM representation:
  `wUAlpha = Valfa_beta.alpha * hT_Sqrt3`
  `wUBeta = -(Valfa_beta.beta * PWMperiod) * 2`
  `CntPhA`, `CntPhB`, `CntPhC`

## Allowed Next Use

- Explain to a teacher how the archived MCSDK source names and arranges the
  FOC math path.
- Prepare future no-power host-side comparison cases that explicitly separate:
  field order, sign direction, fixed-point scaling, angle representation, PI
  divisors, circle-limitation representation, and timer-count PWM output.
- Extend static tests that protect these source-backed conventions.

## Not Allowed

Do not use this artifact to claim:

- no firmware implementation;
- no generated-code edit permission;
- no MCSDK integration;
- no PWM output;
- no motor readiness;
- no compare-register evidence;
- no Gate PWM validation;
- no MCSDK hook readiness;
- no hardware validation;
- no power-stage readiness;
- no Hall closed-loop behavior;
- no sensorless / SMO behavior;
- no safe drive operation.

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
