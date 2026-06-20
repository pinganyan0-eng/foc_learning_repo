# STDRIVE101 USB + 24V Static Recheck Result - 2026-06-20

## Boundary

This record captures the user-reported static check with USB/ST-LINK connected
and HSPY 24 V current-limited input applied.

This is a bounded static diagnostic only. It checks whether STDRIVE101 remains
in the all-inputs-low, low-`REG12` standby-like state when both USB/ST-LINK and
24 V are present, with no firmware Flash / Run / Debug command and no PWM
command.

It does not validate PWM output, gate waveforms, firmware motor-control
runtime, Hall closed-loop behavior, sensorless behavior, motor operation,
power-stage readiness, or motor readiness.

Still forbidden after this result:

- Do not connect a motor.
- Do not start PWM or Gate PWM.
- Do not run Motor Pilot.
- Do not run Motor Profiler.
- Do not flash, Run, or Debug firmware for motor-control output.
- Do not treat this static result as gate-waveform, PWM, or motor readiness.

## Setup

The requested setup was:

```text
USB/ST-LINK: connected
HSPY: 24 V / 0.2 A current limit
Motor: disconnected
10 kohm LIN1 wake stimulus: removed
No Flash / Run / Debug command
DMM: DC voltage mode, black lead on CN3_15 / GND
```

## User-Reported Raw Readings

User reported on 2026-06-20:

```text
usb24_supply_state = CV
usb24_supply_current_A = about 0.045 A
usb24_CN3_1_to_CN3_6_driver_inputs = all close to 0 V
usb24_CN3_14_3V3_V = 3.3 V
usb24_CN3_13_nFAULT_V = 3.3 V
usb24_REG12_V = 0.3 V
```

The six driver input pins were reported as a group rather than as separate
per-pin numeric values. Treat this as a static summary reading, not a
pin-by-pin raw-voltage table.

## Interpretation

The reported USB + 24 V static state matches the expected all-inputs-low
condition:

- HSPY stayed in `CV` and the reported current was about `0.045 A`.
- `CN3_1` through `CN3_6` were all close to `0 V`, so no STDRIVE101 drive
  input was reported high with USB/ST-LINK connected and 24 V applied.
- `CN3_14 / 3V3 = 3.3 V` and `CN3_13 / nFAULT = 3.3 V` stayed normal.
- `REG12 = 0.3 V`, so STDRIVE101 remained in the expected low-REG12
  standby-like state without a wake stimulus.

This closes the static "USB connected plus 24 V present" pre-PWM safety
screen. It still does not prove firmware PWM behavior, timer routing, gate
waveforms, MOSFET switching safety, motor behavior, Hall feedback behavior, or
general powered-drive readiness.

## Decision

`STDRIVE101 USB plus 24V static recheck result / USB-STLINK connected / HSPY
CV about 0.045 A / CN3_1 through CN3_6 all close to 0 V / CN3_14 3.3 V /
nFAULT 3.3 V / REG12 about 0.3 V / no MCU-facing driver input high and no
REG12 wake observed in USB plus 24V static state / no PWM-output validation /
no powered-drive readiness`.

## Next Boundary

Physical closeout before any later wiring change:

```text
HSPY output OFF
Confirm VS / 24V_FUSED < 1 V
Keep motor disconnected
Keep 10 kohm wake stimulus removed
```

The next project step should return to no-power firmware/source planning for a
future explicit PWM/gate-test phase gate. No motor connection, PWM, Motor
Pilot, Motor Profiler, Hall closed-loop claim, sensorless claim, power-stage
readiness claim, or motor readiness claim is opened by this result.
