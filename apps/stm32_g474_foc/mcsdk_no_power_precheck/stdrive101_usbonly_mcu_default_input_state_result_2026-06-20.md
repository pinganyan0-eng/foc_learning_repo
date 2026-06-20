# STDRIVE101 USB-Only MCU Default Input State Result - 2026-06-20

## Boundary

This record captures the user-reported no-24V USB/ST-LINK default-state check
after the STDRIVE101 clean single-input wake retest and all-inputs-low static
recheck.

This is a USB-only / no-24V measurement. It checks only whether the MCU-facing
driver input pins appear low when USB/ST-LINK is connected and HSPY remains
off.

It does not validate PWM output, gate waveforms, firmware motor-control
runtime, Hall closed-loop behavior, sensorless behavior, motor operation,
power-stage readiness, or motor readiness.

Still forbidden after this result:

- Do not connect a motor.
- Do not start PWM or Gate PWM.
- Do not run Motor Pilot.
- Do not run Motor Profiler.
- Do not flash, Run, or Debug firmware for motor-control output.
- Do not apply 24 V for a new step unless a separate bounded checklist is
  opened.

## Setup

The requested setup was:

```text
HSPY: OFF
VS / 24V_FUSED: below 1 V before USB-only check
Motor: disconnected
10 kohm LIN1 wake stimulus: removed
USB/ST-LINK: connected
No Flash / Run / Debug command
DMM: DC voltage mode, black lead on GND
```

## User-Reported Raw Readings

User reported on 2026-06-20:

```text
usbonly_CN3_1_to_CN3_6_driver_inputs = all close to 0 V
P13 = 3.3 V
P14 = 3.3 V
```

Based on the requested measurement table, `P13` and `P14` are interpreted as:

```text
CN3_13 / nFAULT = 3.3 V
CN3_14 / 3V3 = 3.3 V
```

If `P13` / `P14` refer to a different board silkscreen or connector naming,
this record must be corrected before using it as connector-specific evidence.

## Interpretation

The reported USB-only state is the expected safe default for this boundary:

- `CN3_1` through `CN3_6` were all close to `0 V`, so no STDRIVE101 drive
  input was reported high with USB/ST-LINK connected and no 24 V applied.
- `CN3_14 / 3V3 = 3.3 V` confirms the logic rail is present.
- `CN3_13 / nFAULT = 3.3 V` is compatible with the fault line being high in
  this no-24V check.

This supports the next bounded static check with USB/ST-LINK connected and
HSPY current-limited, if explicitly opened. It still does not prove PWM safety
or motor readiness.

## Decision

`STDRIVE101 USB-only MCU default input state result / HSPY OFF no 24 V /
USB-STLINK connected / CN3_1 through CN3_6 all close to 0 V / interpreted
CN3_13 nFAULT 3.3 V / interpreted CN3_14 3V3 3.3 V / no MCU-facing driver
input high observed in USB-only state / no PWM-output validation / no
powered-drive readiness`.

## Next Boundary

The next bounded hardware-adjacent step, if continued, is a static 24 V check
with USB/ST-LINK connected but no Flash / Run / Debug command:

```text
Motor disconnected
10 kohm wake stimulus removed
HSPY 24 V / 0.2 A
Watch HSPY CV/CC and current first
Measure CN3_1 through CN3_6, CN3_13 / nFAULT, CN3_14 / 3V3, and REG12
Stop on CC, abnormal current, any input high, nFAULT low, or REG12 wake
```

No motor connection, PWM, Motor Pilot, Motor Profiler, Hall closed-loop claim,
sensorless claim, power-stage readiness claim, or motor readiness claim is
opened by this result.
