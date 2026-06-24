# MCSDK Sensorless Observer Generated-Source Boundary Review

Date: 2026-06-22

## Decision

`MCSDK sensorless observer generated-source boundary / Hall generated-source boundary confirmed / generic CORDIC and STO register symbols noted / no active MCSDK observer instance / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record is a no-power generated-source boundary review for the archived
2026-05-27 MCSDK source snapshot:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/
2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/
```

It answers one narrow question:

```text
Can the current archived generated-source snapshot be described as an active
MCSDK sensorless observer / STO PLL / STO CORDIC implementation?
```

The answer is no. The snapshot remains a Hall-speed-sensor generated source
boundary, with generic CORDIC math and generic STO register identifiers present
as MCSDK support symbols only.

## Source-Backed Findings

- `QIANSAI_G474_STDRIVE101_FOC_P2.ioc` contains
  `MotorControl.M1_SPEED_SENSOR=HALL_SENSOR`.
- `QIANSAI_G474_STDRIVE101_FOC_P2.ioc` contains
  `MotorControl.SPEED_SENSOR_SELECTION=HALL_SENSORS`.
- `Src/mc_config.c` declares the speed / position sensor block as
  `SpeedNPosition sensor parameters Motor 1 - HALL.` and instantiates
  `HALL_Handle_t HALL_M1 =`.
- `Src/mc_tasks_foc.c` initializes the speed feedback path with
  `HALL_Init (&HALL_M1);` and
  `STC_Init(pSTC[M1],&PIDSpeedHandle_M1, &HALL_M1._Super);`.
- The high-frequency task calls `(void)HALL_CalcElAngle(&HALL_M1);`, then the
  FOC current controller uses `speedHandle = STC_GetSpeedSensor(pSTC[M1]);`
  and `hElAngle = SPD_GetElAngle(speedHandle);`.
- `Inc/mc_math.h` contains generic CORDIC support including
  `CORDIC_CONFIG_PHASE` and `MCM_PhaseComputation(...)` for B-emf alpha / beta
  phase computation.
- `Inc/register_interface.h` contains generic monitor/control register IDs
  such as `MC_REG_STOPLL_EL_ANGLE` and `MC_REG_STOCORDIC_EL_ANGLE`.
- `Inc/mc_stm_types.h` contains generic compile-time guard names such as
  `FULL_MISRA_C_COMPLIANCY_STO_CORDIC` and
  `FULL_MISRA_C_COMPLIANCY_STO_PLL`.
- The archived generated `Src/` and `Inc/` file lists contain
  `hall_speed_pos_fdbk.c` / `hall_speed_pos_fdbk.h`, but not
  `sto_pll_speed_pos_fdbk.*`, `sto_cordic_speed_pos_fdbk.*`,
  `revup_ctrl.*`, or `virtual_speed_sensor.*`.
- The older Workbench file
  `packet_a_sources/2026-05-16_custom_nucleo_stdrive101/QIANSAI_G474_STDRIVE101_FOC_P2_2026-05-21.stwb6`
  contains `revupToFocSwitchOverEnabled`, but that Workbench flag does not
  override the later archived generated-source boundary above.

## Meaning For Host-Side Sensorless Work

The host-side sensorless frontend, observer stub, startup policy replay, and
MCSDK-shaped snapshot bridge remain useful no-power algorithm scaffolding.
They do not prove that the current MCSDK generated source has an active
observer instance.

The current safe interpretation is:

```text
host-side sensorless replay evidence
-> MCSDK-shaped comparison metadata
-> source-backed boundary says current archived generated source is Hall-based
-> future sensorless integration would need a separate generated-source package,
   review artifact, and no-power build evidence
```

## Boundary

This is generated-source review evidence only.

Short form: this is not MCSDK Observer PLL equivalence, not MCSDK Observer CORDIC equivalence, not SMO implementation or validation, not sensorless / SMO validation, not Gate PWM validation, not power-stage readiness, and not motor readiness.

It is not evidence for:

- firmware implementation;
- generated-code edit permission;
- active MCSDK observer instance;
- MCSDK Observer PLL equivalence;
- MCSDK Observer CORDIC equivalence;
- SMO implementation or validation;
- MCSDK integration;
- host-side / MCSDK numerical equivalence evidence;
- compare-register evidence;
- Gate PWM validation;
- sensorless / SMO validation;
- hardware validation;
- power-stage readiness;
- motor readiness;
- safe drive operation.

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

- `python -m unittest tests.test_mcsdk_sensorless_observer_boundary_static`
  must pass for this record to remain valid.
