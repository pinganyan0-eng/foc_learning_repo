# Static 24 V Baseline B1-Not-Pressed Check - 2026-06-19

## Boundary

This record covers a current-limited static 24 V observation after:

- the reviewed USB-only `nucleo_g474re_baseline` firmware was flashed;
- serial identity was confirmed with `BOOT OK`, `PING -> PONG`, and
  `MODE? -> OK unchanged mode=0 mode_name=IDLE`;
- USB-only `CN3_1..CN3_6` were measured as `0 V`.

This is static measurement evidence only. It is not motor validation, PWM
validation, Hall closed-loop validation, sensorless validation, or powered-drive
readiness.

Hard stops remain active:

- Keep motor disconnected.
- Do not start PWM.
- Do not run Motor Pilot or Motor Profiler.
- Do not claim power-stage readiness from this record.

## Test Condition

- CN3 connected.
- B1 not pressed.
- Motor disconnected by boundary.
- Bench supply set to `24 V / 0.2 A` current limit.
- Supply state reported as `CV`.

The numeric supply current was not reported in this message and should be
captured before the next powered-static step.

## User-Reported Raw Measurement

```text
Power supply: CV, current value not reported
CN3_14 / 3V3: 3.3 V
CN3_13 / nFAULT: 3.3 V
REG12: 0.3 V
VS / 24V_FUSED: 24 V
CN3_1..CN3_6 still 0 V: yes
```

## Interpretation

Good-direction static observations:

- `VS / 24V_FUSED = 24 V`, so the 24 V rail is present at the checked node.
- `CN3_14 / 3V3 = 3.3 V`, so the MCU-side 3.3 V rail is present.
- `CN3_13 / nFAULT = 3.3 V`, so nFAULT is not being pulled low in this static
  condition.
- `CN3_1..CN3_6` remain `0 V`, matching the reviewed baseline source and the
  USB-only physical input check.

Important non-pass observation:

- `REG12 = 0.3 V` remains low in the all-inputs-low static condition. This must
  not be interpreted as active gate-driver readiness or a valid gate-drive
  supply state. In this specific baseline, the firmware does not drive HIN/LIN
  or start PWM, so this record only supports a no-command static observation.

## Decision

`Static 24 V / B1 not pressed / nFAULT high / CN3 inputs low / VS present /
REG12 low / no PWM-output validation / no powered-drive readiness`.

## Next Bounded Check

The next allowed check is still static and motor-disconnected:

1. Keep HSPY at `24 V / 0.2 A`.
2. Keep motor disconnected.
3. Record the numeric supply current while still in CV.
4. Press B1 once only.
5. Confirm the serial mode changes at most to `ARMED`, or report the mode line.
6. Re-measure:
   - supply current and CV/CC state
   - `CN3_13 / nFAULT`
   - `CN3_1..CN3_6`
   - `REG12`

Stop immediately if current limit engages, current jumps, nFAULT drops, any
CN3 input rises, heat, smell, smoke, or abnormal behavior appears.
