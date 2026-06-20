# STDRIVE101 REG12 Single-Input Wake Fault Result - 2026-06-19

## Boundary

This record captures the user-reported result of the bounded STDRIVE101
single-input wake diagnostic using `CN3_2 / LIN1`.

This is one powered diagnostic result under current limit. It does not validate
PWM output, gate waveforms, Hall closed-loop behavior, sensorless behavior,
motor operation, power-stage readiness, or motor readiness.

Hard stops after this result:

- Do not retry the powered wake diagnostic until the `nFAULT` cause is
  reviewed.
- Do not switch to another driver input as a workaround.
- Do not connect a motor.
- Do not start PWM.
- Do not run Motor Pilot.
- Do not run Motor Profiler.
- Do not use a direct wire from `3V3` to `LIN1`.
- Do not install or remove any resistor or probe while HSPY output is on.

## Setup

The user reported the wake readings under the intended bounded setup:

```text
Stimulus: CN3_14 / 3V3 -> 10 kohm series resistor -> CN3_2 / LIN1
Motor: disconnected
USB/ST-LINK: unplugged
CN3: connected as in the static 24 V baseline check
HSPY: 24 V / 0.2 A current limit
DMM: DC voltage mode, black lead on GND
```

Pre-stimulus baseline was already recorded in
`stdrive101_reg12_single_input_wake_baseline_result_2026-06-19.md`.

## User-Reported Raw Readings

User reported on 2026-06-19:

```text
wake_supply_state = CV
wake_supply_current_A = 0.046 A
wake_CN3_2_LIN1_V = 3 V
wake_CN3_13_nFAULT_V = 0 V
wake_REG12_V = 12 V
```

After the stop instruction, the user reported:

```text
post_off_VS_or_24V_FUSED_V = 0 V
```

The user did not explicitly report that the `10 kohm` stimulus resistor had
been removed, so that removal remains a required physical checkpoint after
confirming HSPY output is OFF and `VS / 24V_FUSED < 1 V`.

## Interpretation

The readings separate into four facts:

- `wake_CN3_2_LIN1_V = 3 V`: the `10 kohm` series stimulus reached `LIN1` and
  drove it above the STDRIVE101 logic-high threshold used in the plan.
- `wake_REG12_V = 12 V`: `REG12` rose into the expected regulator range after
  `LIN1` was driven high, so the all-inputs-low `REG12` low condition was not
  a standalone proof of a failed `REG12` regulator.
- `wake_supply_state = CV` and `wake_supply_current_A = 0.046 A`: the bench
  supply did not enter current limit during the reported steady reading.
- `wake_CN3_13_nFAULT_V = 0 V`: the diagnostic violated the explicit stop
  rule requiring `nFAULT` to remain above `3.0 V` after settling.

Therefore the bounded wake diagnostic observed `REG12` rising under the
single-input stimulus, but it did not pass as a clean wake condition because
`nFAULT` was low.

## Decision

`STDRIVE101 REG12 single-input wake result / CN3_14 3V3 through 10 kohm to
CN3_2 LIN1 / LIN1 3 V / HSPY CV 0.046 A / REG12 rose to 12 V / nFAULT 0 V
stop-rule event / post-off VS reported 0 V / no retry before fault-cause
review / no PWM-output validation / no powered-drive readiness`.

## Next Boundary

Immediate physical closeout:

```text
HSPY output OFF
Confirm VS / 24V_FUSED < 1 V
Remove the 10 kohm stimulus resistor
Leave motor disconnected
Do not retry powered wake
```

Next engineering work should be no-power or source-review only:

- review STDRIVE101 `nFAULT` causes and board conditions after single-input
  standby exit;
- review whether commanding one low-side input high with all other driver
  inputs low can legitimately assert a fault on this custom board;
- review relevant protection pins, bootstrap / VDS / UVLO context, and
  board-level pull states before any repeat diagnostic is proposed.

No motor connection, PWM, Motor Pilot, Motor Profiler, Hall closed-loop claim,
sensorless claim, power-stage readiness claim, or motor readiness claim is
opened by this result.
