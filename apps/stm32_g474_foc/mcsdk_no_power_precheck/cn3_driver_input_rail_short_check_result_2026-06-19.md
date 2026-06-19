# CN3 Driver-Input Rail Short-Check Result - 2026-06-19

## Boundary

This record captures the user-reported no-power DMM result for the six CN3
driver-input lines against the main rails.

This is no-power DMM evidence only. It is not a wake-up test, not PWM
validation, not Gate PWM validation, not motor validation, not Hall closed-loop
validation, not sensorless validation, and not powered-drive readiness.

Hard stops remain active:

- No motor connection.
- No 24 V powered step from this record.
- No USB-powered firmware action from this record.
- No intentional CN3 input drive-high action from this record.
- No Gate PWM output.
- No Motor Pilot or Motor Profiler.

## Setup Assumption

The result is interpreted under the setup requested in
`cn3_driver_input_no_power_short_check_plan_2026-06-19.md`:

```text
HSPY output: OFF
24 V input: disconnected from the board
USB/ST-LINK: unplugged
Motor: disconnected
DMM: resistance or continuity mode only
```

If any of those assumptions were not true, this record must be downgraded and
the measurement repeated.

## User-Reported Raw Result

The user reported:

```text
All tested pairs: no beep, high resistance.
```

The requested tested pairs were:

```text
CN3_1 -> GND / 3V3 / VS(24V_FUSED) / REG12
CN3_2 -> GND / 3V3 / VS(24V_FUSED) / REG12
CN3_3 -> GND / 3V3 / VS(24V_FUSED) / REG12
CN3_4 -> GND / 3V3 / VS(24V_FUSED) / REG12
CN3_5 -> GND / 3V3 / VS(24V_FUSED) / REG12
CN3_6 -> GND / 3V3 / VS(24V_FUSED) / REG12
```

## Interpretation

Under the assumed no-power setup, the report supports this limited conclusion:

- no hard short was found from `CN3_1..CN3_6` to `GND`;
- no hard short was found from `CN3_1..CN3_6` to `3V3 / CN3_14`;
- no hard short was found from `CN3_1..CN3_6` to `VS / 24V_FUSED`;
- no hard short was found from `CN3_1..CN3_6` to `REG12`.

Because exact resistance values were not recorded, this is a hard-short screen
only. It does not characterize leakage, input pull-down strength, ESD paths,
or connector/cable quality.

## Non-Pass Limits

This result does not prove:

- adjacent CN3 driver-input lines are isolated from each other;
- CN3-to-STDRIVE101 endpoint mapping is final;
- CN3-to-STM32 endpoint mapping is final;
- REG12 wake-up behavior;
- bootstrap charging;
- low-side or high-side gate output behavior;
- nFAULT behavior under active drive.

## Decision

`CN3 driver-input rail short-check / all six drive inputs no-beep high-resistance
to GND, 3V3, VS, and REG12 / hard-short screen to rails clear under reported
no-power setup / adjacent input-to-input check still pending / no PWM-output
validation / no powered-drive readiness`.

## Next Measurement

Remain unpowered and measure adjacent input-to-input pairs:

```text
CN3_1 -> CN3_2
CN3_2 -> CN3_3
CN3_3 -> CN3_4
CN3_4 -> CN3_5
CN3_5 -> CN3_6
```

Report `beep / no beep` and resistance if available. Stop if any pair beeps or
reads near `0 ohm`.
