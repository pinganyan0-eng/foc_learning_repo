# Static 24 V Baseline B1-Once Check - 2026-06-19

## Boundary

This record covers a current-limited static 24 V observation after pressing B1
once on the reviewed `nucleo_g474re_baseline` firmware.

This is not motor validation, PWM validation, Gate PWM validation, Hall
closed-loop validation, sensorless validation, or powered-drive readiness.

Hard stops remain active:

- Keep motor disconnected.
- Do not start PWM.
- Do not run Motor Pilot or Motor Profiler.
- Do not claim power-stage readiness from this record.

## Prior State

Before pressing B1 once:

- `VS / 24V_FUSED = 24 V`
- `CN3_14 / 3V3 = 3.3 V`
- `CN3_13 / nFAULT = 3.3 V`
- `REG12 = 0.3 V`
- `CN3_1..CN3_6 = 0 V`
- supply was in `CV`

Related prior record:

- `static_24v_baseline_b1_not_pressed_check_2026-06-19.md`

## User-Reported Raw Measurement After Pressing B1 Once

Condition:

- CN3 connected.
- B1 pressed once.
- Motor disconnected.
- Bench supply still current-limited.

Raw result:

```text
Supply current: 0.036 A
Supply state: CV
CN3_13 / nFAULT: 3.3 V
REG12: 0.3 V
CN3_1..CN3_6: 0 V
```

## Serial Query

Codex sent only a safe `MODE?` query on COM5 at `115200 8N1`.

Observed response:

```text
OK unchanged mode=1 mode_name=ARMED
tick_ms=163500, led=1, led_toggle=1635, report=327, btn=0, btn_press=1, mode=1, mode_name=ARMED, mode_chg=1, target_rpm=0
```

## Interpretation

Good-direction static observations:

- Supply current stayed at `0.036 A` and `CV`.
- `nFAULT` stayed high at `3.3 V`.
- `CN3_1..CN3_6` stayed at `0 V`.
- Serial state changed to `ARMED` with `btn_press=1`, matching the reviewed
  baseline state machine.
- `target_rpm` remained `0`.

Important non-pass observation:

- `REG12 = 0.3 V` remains low. This is not evidence of active gate-drive
  supply readiness.

## Decision

`Static 24 V / B1 pressed once / baseline entered ARMED / nFAULT high /
CN3 inputs low / current stable in CV / REG12 low / no PWM-output validation /
no powered-drive readiness`.

The board should not be advanced to motor connection, PWM output, Motor Pilot,
or Motor Profiler from this record.

## Next Bounded Step

Return the baseline application state to `IDLE` before any further static
measurement:

```text
STOP
MODE?
```

Expected serial response after `STOP`:

```text
OK changed mode=0 mode_name=IDLE
OK unchanged mode=0 mode_name=IDLE
```

No further B1 presses are needed for this static gate.
