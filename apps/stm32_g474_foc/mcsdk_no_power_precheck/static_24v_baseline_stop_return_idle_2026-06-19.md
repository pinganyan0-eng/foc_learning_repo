# Static 24 V Baseline STOP Return-To-IDLE Check - 2026-06-19

## Boundary

This record covers a serial-only state reset after the static 24 V B1-once
check on the reviewed `nucleo_g474re_baseline` firmware.

This is not motor validation, PWM validation, Gate PWM validation, Hall
closed-loop validation, sensorless validation, or powered-drive readiness.

Hard stops remain active:

- Keep motor disconnected.
- Do not start PWM.
- Do not run Motor Pilot or Motor Profiler.
- Do not claim power-stage readiness from this record.

## Prior State

The prior static check recorded:

- B1 pressed once.
- Supply current `0.036 A`, supply state `CV`.
- `CN3_13 / nFAULT = 3.3 V`.
- `REG12 = 0.3 V`.
- `CN3_1..CN3_6 = 0 V`.
- Serial state `mode=1`, `mode_name=ARMED`, `target_rpm=0`.

Related prior record:

- `static_24v_baseline_b1_once_check_2026-06-19.md`

## Serial Commands

Codex sent only these serial commands on COM5 at `115200 8N1`:

```text
STOP
MODE?
```

Observed response:

```text
OK changed mode=0 mode_name=IDLE
OK unchanged mode=0 mode_name=IDLE
tick_ms=276500, led=1, led_toggle=2765, report=553, btn=0, btn_press=1, mode=0, mode_name=IDLE, mode_chg=2, target_rpm=0
```

## Decision

`Static 24 V baseline / STOP command returned app state to IDLE / target_rpm
0 / no PWM-output validation / no powered-drive readiness`.

The baseline application state is now back to `IDLE`.

## Next Boundary

No further B1 presses are needed for this static gate.

If continuing hardware work, the next step should be defined as a separate
bounded gate with:

- motor disconnected;
- explicit current limit;
- exact measurement points;
- rollback condition;
- no PWM or Motor Pilot / Profiler unless a later reviewed phase gate opens it.
