# STDRIVE101 REG12 Single-Input Wake Baseline Result - 2026-06-19

## Boundary

This record captures the user-reported static baseline immediately before the
optional STDRIVE101 single-input wake stimulus.

This is baseline measurement evidence only. It does not execute the wake
diagnostic, does not install the `10 kohm` stimulus resistor, does not validate
PWM output, does not validate gate-driver output, does not validate Hall
closed-loop behavior, does not validate sensorless behavior, and does not prove
power-stage or motor readiness.

Hard stops remain active:

- Do not connect a motor.
- Do not start PWM.
- Do not run Motor Pilot.
- Do not run Motor Profiler.
- Do not use a direct wire from `3V3` to `LIN1`.
- Do not install or remove any jumper while HSPY output is on.
- Do not claim power-stage readiness or motor readiness from this record.

## Setup

The user reported the baseline under the intended pre-stimulus setup:

```text
Stimulus resistor: not installed
Motor: disconnected
USB/ST-LINK: unplugged
CN3: connected as in the static 24 V baseline check
HSPY: 24 V / 0.2 A current limit
DMM: DC voltage mode, black lead on GND
```

## User-Reported Raw Readings

User reported on 2026-06-19:

```text
baseline_supply_state = CV
baseline_supply_current_A = 0.036 A
baseline_VS_or_24V_FUSED_V = 24 V
baseline_CN3_14_3V3_V = 3.3 V
baseline_CN3_13_nFAULT_V = 3.3 V
baseline_REG12_V = 0.33 V
```

## Interpretation

The baseline matches the earlier all-inputs-low standby observations:

- HSPY remains in `CV`.
- Supply current remains at the earlier `0.036 A` static baseline.
- `VS / 24V_FUSED` is present at `24 V`.
- `CN3_14 / 3V3` is present at `3.3 V` in the exact setup where
  USB/ST-LINK is unplugged.
- `CN3_13 / nFAULT` remains high at `3.3 V`.
- `REG12` remains low at `0.33 V`, consistent with the already reviewed
  STDRIVE101 all-inputs-low standby explanation.

This closes only the pre-stimulus baseline condition for the bounded
single-input wake diagnostic. It does not show what happens after
`CN3_2 / LIN1` is driven high.

## Decision

`STDRIVE101 REG12 single-input wake baseline / HSPY 24 V 0.2 A CV /
0.036 A static current / VS 24 V / CN3_14 3.3 V present with USB-STLINK
unplugged / nFAULT 3.3 V / REG12 0.33 V / pre-stimulus baseline satisfied
only / no wake stimulus installed / no PWM-output validation / no powered-drive
readiness`.

## Next Boundary

The project may stop at this baseline record if the user does not want to
install the `10 kohm` stimulus resistor.

If the user later chooses to continue the wake diagnostic, the next allowed
step is still exactly:

```text
HSPY output OFF
Wait until VS / 24V_FUSED < 1 V
Install 10 kohm series resistor from CN3_14 / 3V3 to CN3_2 / LIN1
HSPY 24 V / 0.2 A
Measure supply CV/CC, current, CN3_2 / LIN1, CN3_13 / nFAULT, and REG12
```

Do not replace the `10 kohm` stimulus with a direct wire.
