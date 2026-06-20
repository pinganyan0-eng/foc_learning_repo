# STDRIVE101 All-Inputs-Low Static Recheck Result - 2026-06-20

## Boundary

This record captures the user-reported static recheck after the bounded
single-input wake retest and recovery.

This is one limited 24 V static diagnostic under HSPY current limit. It checks
only that, with the `10 kohm` stimulus removed and all driver inputs low,
STDRIVE101 returns to the expected low-`REG12` standby-like state.

It does not validate PWM output, gate waveforms, Hall closed-loop behavior,
sensorless behavior, motor operation, power-stage readiness, or motor
readiness.

Still forbidden after this result:

- Do not connect a motor.
- Do not start PWM or Gate PWM.
- Do not run Motor Pilot.
- Do not run Motor Profiler.
- Do not flash, Run, or Debug firmware for motor-control output.
- Do not install or remove any resistor or probe while HSPY output is on.

## Setup

The user reported this recheck under the intended static setup:

```text
Motor: disconnected
USB/ST-LINK: unplugged
10 kohm LIN1 wake stimulus: removed
HSPY: 24 V / 0.2 A current limit
DMM: DC voltage mode, black lead on CN3_15 / GND
```

## User-Reported Raw Readings

User reported on 2026-06-20:

```text
static2_supply_state = CV
static2_supply_current_A = about 0.045 A
static2_CN3_1_to_CN3_6_driver_inputs = all close to 0 V
static2_CN3_14_3V3_V = 3.3 V
static2_CN3_13_nFAULT_V = 3.3 V
static2_REG12_V = 0.3 V
```

The six driver input pins were reported as a group rather than as separate
per-pin numeric values. Treat this as a static summary reading, not a
pin-by-pin raw-voltage table.

## Interpretation

The post-retest static state matches the expected all-inputs-low condition:

- HSPY stayed in `CV` and the reported current was about `0.045 A`.
- `CN3_1` to `CN3_6` were all close to `0 V`, so no driver input was reported
  accidentally high in this static setup.
- `CN3_14 / 3V3 = 3.3 V` and `CN3_13 / nFAULT = 3.3 V` stayed normal.
- `REG12 = 0.3 V`, so STDRIVE101 returned to the expected low-REG12
  standby-like state after the `LIN1` wake stimulus was removed.

This closes the immediate recovery-static check after the clean single-input
wake retest. It does not prove MCU reset/default GPIO behavior, PWM safety,
MOSFET gate waveform correctness, motor behavior, Hall feedback behavior, or
general powered-drive readiness.

## Decision

`STDRIVE101 all-inputs-low static recheck result / 10 kohm wake stimulus
removed / HSPY CV about 0.045 A / CN3_1 through CN3_6 all close to 0 V /
CN3_14 3.3 V / nFAULT 3.3 V / REG12 about 0.3 V / standby-like recovery
confirmed after clean LIN1 wake retest / no PWM-output validation / no
powered-drive readiness`.

## Next Boundary

Physical closeout before any later wiring change:

```text
HSPY output OFF
Confirm VS / 24V_FUSED < 1 V
Keep motor disconnected
Keep 10 kohm wake stimulus removed
```

The next bounded hardware-adjacent step may be a no-24V USB/ST-LINK default
state check of the MCU-facing driver inputs before considering any firmware,
PWM, or motor-related phase gate.
