# CN3 Driver-Input Adjacent Short-Check Result - 2026-06-19

## Boundary

This record captures the user-reported no-power DMM result for adjacent
`CN3_1..CN3_6` driver-input pairs.

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

The result is interpreted under the same no-power setup used by
`cn3_driver_input_rail_short_check_result_2026-06-19.md`:

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
CN3_1 -> CN3_2: no beep, about 90 kohm
CN3_2 -> CN3_3: no beep, about 90 kohm
CN3_3 -> CN3_4: no beep, about 90 kohm
CN3_4 -> CN3_5: no beep, about 90 kohm
CN3_5 -> CN3_6: no beep, about 90 kohm
```

## Interpretation

Under the assumed no-power setup, the report supports this limited conclusion:

- no hard short was found between adjacent driver-input pins in the measured
  subset;
- about `90 kohm` is not a near-`0 ohm` short;
- the value may come from internal input structures, pull-down paths, board
  leakage, or meter-dependent paths, so it must not be interpreted as endpoint
  proof.

Combined with `cn3_driver_input_rail_short_check_result_2026-06-19.md`, the
six driver-input lines have now passed only this hard-short screen:

- no reported hard short to `GND`;
- no reported hard short to `3V3 / CN3_14`;
- no reported hard short to `VS / 24V_FUSED`;
- no reported hard short to `REG12`;
- no reported hard short between adjacent measured driver-input pairs.

## Non-Pass Limits

This result does not prove:

- non-adjacent CN3 driver-input pairs are isolated;
- CN3-to-STDRIVE101 endpoint mapping is final;
- CN3-to-STM32 endpoint mapping is final;
- REG12 wake-up behavior;
- bootstrap charging;
- low-side or high-side gate output behavior;
- nFAULT behavior under active drive.

## Decision

`CN3 driver-input adjacent short-check / adjacent measured pairs no-beep around
90 kohm / no hard short found in rail or adjacent-input screen / hard-short
screen closed for the requested subset / no wake-up validation / no PWM-output
validation / no powered-drive readiness`.

## Next Boundary

Do not continue directly to powered wake-up from this result.

The next project action should be documentation/planning only: create a
separate bounded STDRIVE101 wake-up diagnostic plan before any later powered
action. That plan must define:

- exact single input to command or stimulate;
- why that input is the lowest-risk choice;
- whether the action would turn on any MOSFET gate;
- expected `REG12`, `nFAULT`, and supply current;
- current limit and CV/CC stop rule;
- rollback to all inputs low;
- explicit confirmation that motor remains disconnected.
