# STDRIVE101 REG12 Single-Input Wake Retest Clean Result - 2026-06-20

## Boundary

This record captures the user-reported bounded retest after the gate-source
pulldown rework result.

This is one limited powered diagnostic under HSPY current limit. It verifies
only the `CN3_2 / LIN1` single-input wake behavior, `REG12`, `nFAULT`, and
recovery-to-standby behavior in this setup.

It does not validate PWM output, gate waveforms, Hall closed-loop behavior,
sensorless behavior, motor operation, power-stage readiness, or motor
readiness.

Still forbidden after this result:

- Do not connect a motor.
- Do not start PWM or Gate PWM.
- Do not run Motor Pilot.
- Do not run Motor Profiler.
- Do not flash, Run, or Debug firmware for motor-control output.
- Do not use a direct wire from `3V3` to `LIN1`.
- Do not install or remove any resistor or probe while HSPY output is on.

## Setup

The retest used the same bounded stimulus:

```text
Stimulus: CN3_14 / 3V3 -> 10 kohm series resistor -> CN3_2 / LIN1
Motor: disconnected
USB/ST-LINK: unplugged
HSPY: 24 V / 0.2 A current limit
DMM: DC voltage mode, black lead on GND
```

The preceding no-power rework evidence recorded:

```text
VS_OFF_V = 0 V
10k_removed = yes
Q1_GS = 10 kohm
Q3_GS = 10 kohm
Q5_GS = 10 kohm
Q2_GS = 10 kohm
Q4_GS = 10 kohm
Q6_GS = 10 kohm
```

## User-Reported Retest Readings

User reported on 2026-06-20:

```text
retest_supply_state = CV
retest_supply_current_A = 0.048 A
retest_CN3_2_LIN1_V = 3.13 V
retest_CN3_13_nFAULT_V = 3.3 V
retest_REG12_V = 12 V
```

## User-Reported Recovery Readings

After turning HSPY off, waiting for the bus to discharge, removing the
`10 kohm` stimulus, and restoring the all-inputs-low condition, the user
reported:

```text
recovery_supply_state = CV
recovery_supply_current_A = 0.045 A
recovery_CN3_13_nFAULT_V = 3.3 V
recovery_REG12_V = 0.33 V
```

The user did not restate the exact post-off `VS / 24V_FUSED` value after the
final recovery check in this message. Before any later wiring change, measure
`VS / 24V_FUSED < 1 V` again with HSPY output off.

## Interpretation

The retest separates into these facts:

- `LIN1 = 3.13 V`: the `10 kohm` series stimulus reached `CN3_2 / LIN1` and
  drove it above the STDRIVE101 logic-high threshold used in the plan.
- `REG12 = 12 V`: STDRIVE101 left standby and the 12 V regulator rose into
  the expected practical range.
- `nFAULT = 3.3 V`: the previous clean-wake blocker, `nFAULT = 0 V`, did not
  recur in this bounded retest.
- `HSPY = CV` and `0.048 A`: no bench-supply current-limit event or abnormal
  steady current was reported.
- Recovery `REG12 = 0.33 V` with `nFAULT = 3.3 V`: after removing the
  stimulus and returning all driver inputs low, the driver returned to the
  expected standby-like low-REG12 state.

This upgrades the single-input wake branch from the earlier fault result to a
clean bounded retest result after rework. It still does not prove PWM safety,
MOSFET gate waveform correctness, motor behavior, Hall feedback behavior, or
general powered-drive readiness.

## Decision

`STDRIVE101 REG12 single-input wake retest clean result / CN3_14 3V3 through
10 kohm to CN3_2 LIN1 / LIN1 3.13 V / HSPY CV 0.048 A / REG12 rose to 12 V /
nFAULT stayed 3.3 V / recovery all-inputs-low REG12 0.33 V and nFAULT 3.3 V /
previous nFAULT-low wake blocker not reproduced after gate-source pulldown
rework / no PWM-output validation / no powered-drive readiness`.

## Next Boundary

Physical closeout before any later work:

```text
HSPY output OFF
Confirm VS / 24V_FUSED < 1 V
Confirm 10 kohm stimulus removed
Leave motor disconnected
```

The next project step should return to no-power planning or source review
unless a separate, explicit, bounded phase gate is opened. No motor
connection, PWM, Motor Pilot, Motor Profiler, Hall closed-loop claim,
sensorless claim, power-stage readiness claim, or motor readiness claim is
opened by this result.
