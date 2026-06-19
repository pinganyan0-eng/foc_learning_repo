# Static 24 V Baseline Gate Summary - 2026-06-19

## Boundary

This summary consolidates the reviewed USB-only baseline flash, USB-only CN3
input check, and the current-limited static 24 V checks.

This is not motor validation, PWM validation, Gate PWM validation, Hall
closed-loop validation, sensorless validation, or powered-drive readiness.

Hard stops remain active:

- Motor disconnected.
- No Gate PWM output.
- No Motor Pilot.
- No Motor Profiler.
- No Hall closed-loop claim.
- No sensorless claim.
- No powered-drive readiness claim.

## Evidence Chain

1. Source review:
   `nucleo_g474re_baseline_usb_only_safety_review_2026-06-19.md`
   found no application-level TIM1/TIM8 PWM, MOE, MCSDK motor start, or
   STDRIVE HIN/LIN control path.
2. USB-only flash:
   `nucleo_g474re_baseline_usb_only_flash_result_2026-06-19.md`
   recorded the reviewed `.bin` image flash through the ST-LINK virtual drive.
3. Serial identity:
   `BOOT OK`, `PING -> PONG`, and `MODE? -> OK unchanged mode=0 mode_name=IDLE`.
4. USB-only physical input check:
   `nucleo_g474re_baseline_usb_only_cn3_input_check_2026-06-19.md`
   recorded `CN3_1..CN3_6 = 0 V`.
5. Static 24 V, B1 not pressed:
   `static_24v_baseline_b1_not_pressed_check_2026-06-19.md`.
6. Static 24 V, B1 pressed once:
   `static_24v_baseline_b1_once_check_2026-06-19.md`.
7. STOP returned the baseline app state to IDLE:
   `static_24v_baseline_stop_return_idle_2026-06-19.md`.

The earlier `static_24v_reg12_anomaly_2026-06-19.md` is superseded for the
REG12 value. The current corrected user-reported value is `REG12 = 0.3 V`, not
`24 V`.

## Consolidated Static Measurements

### B1 Not Pressed

```text
Supply state: CV
CN3_14 / 3V3: 3.3 V
CN3_13 / nFAULT: 3.3 V
REG12: 0.3 V
VS / 24V_FUSED: 24 V
CN3_1..CN3_6: 0 V
```

### B1 Pressed Once

```text
Supply current: 0.036 A
Supply state: CV
CN3_13 / nFAULT: 3.3 V
REG12: 0.3 V
CN3_1..CN3_6: 0 V
Serial state: mode=1, mode_name=ARMED, target_rpm=0
```

### STOP After B1

```text
STOP -> OK changed mode=0 mode_name=IDLE
MODE? -> OK unchanged mode=0 mode_name=IDLE
Status line: mode=0, mode_name=IDLE, target_rpm=0
```

## Decision

`Reviewed USB-only baseline / static 24 V current-limited observation /
nFAULT high / CN3 inputs low / current stable in CV / REG12 low / app returned
to IDLE / no PWM-output validation / no powered-drive readiness`.

This supports closing the current static input/nFAULT observation gate. It does
not support connecting a motor, generating PWM, or running Motor Pilot /
Profiler.

## Required Next Step

Before any new powered gate is opened, do a no-power REG12 / VS identity check.

Required setup:

- HSPY output off.
- 24 V disconnected from the board.
- USB/ST-LINK disconnected.
- Motor disconnected.
- DMM in resistance or continuity mode only.

Record raw readings:

```text
REG12 correct point -> VS / 24V_FUSED:
REG12 correct point -> GND:
VS / 24V_FUSED -> GND:
REG12 correct point -> 24V input positive:
REG12 correct point -> CN3_14 / 3V3:
```

Physical point reminder:

- `C2/C3` positive side should be `VS / 24V_FUSED`.
- `C4/C5` positive side should be `REG12`.
- `C4/C5` GND side should beep / read near 0 ohm to GND.
