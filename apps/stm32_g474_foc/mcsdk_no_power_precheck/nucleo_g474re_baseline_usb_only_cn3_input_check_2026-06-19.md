# NUCLEO-G474RE USB-Only CN3 Input Check - 2026-06-19

## Boundary

This is a USB-only physical voltage check after the reviewed baseline firmware
was flashed and serial identity was confirmed.

- USB/ST-LINK only.
- 24 V disconnected.
- Motor disconnected.
- No Gate PWM, Motor Pilot, Motor Profiler, Hall closed-loop, sensorless
  control, or powered-drive readiness is claimed.

Related records:

- `nucleo_g474re_baseline_usb_only_safety_review_2026-06-19.md`
- `nucleo_g474re_baseline_usb_only_flash_result_2026-06-19.md`

## Firmware State Before Measurement

Serial evidence from the flash record showed:

- `BOOT OK`
- `PING -> PONG`
- `MODE? -> OK unchanged mode=0 mode_name=IDLE`
- periodic status reported `mode=0`, `mode_name=IDLE`, `target_rpm=0`

## Raw User Measurement

Measurement setup:

- Black probe: `CN3_15 / GND`
- Red probe: `CN3_1` through `CN3_6`, one at a time

User-reported result:

```text
CN3_1: 0 V
CN3_2: 0 V
CN3_3: 0 V
CN3_4: 0 V
CN3_5: 0 V
CN3_6: 0 V
```

## Decision

`USB-only baseline / serial identity confirmed / CN3_1..CN3_6 measured 0 V /
no PWM-output validation / no powered-drive readiness`.

This supports the next bounded static check with 24 V current-limited supply,
but only as a power/nFAULT/REG12 observation step. It does not authorize motor
connection, Gate PWM output, Motor Pilot, Motor Profiler, Hall closed-loop, or
sensorless control.

## Next Bounded Check

Allowed next check, if the user keeps the motor disconnected:

1. Keep CN3 connected.
2. Keep B1 not pressed.
3. Set bench supply to `24 V`, current limit `0.2 A`.
4. Turn output on only after confirming polarity.
5. Stop immediately if current limit engages, current jumps abnormally, smoke,
   heat, smell, or any unexpected LED/fault behavior appears.
6. Record:
   - supply current and CV/CC state
   - `CN3_13 / nFAULT`
   - `CN3_14 / 3V3`
   - `REG12`
   - `VS / 24V_FUSED`
   - optional: `CN3_1..CN3_6` still near `0 V`
