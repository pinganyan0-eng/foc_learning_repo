# NUCLEO-G474RE USB-Only Baseline Flash Result - 2026-06-19

## Boundary

This record covers one explicitly user-approved USB-only flash gate.

Confirmed working assumption from the user before flash:

- HSPY output off.
- 24 V disconnected from the board.
- Motor disconnected.
- Only USB/ST-LINK connected.

No 24 V powered step, motor connection, Gate PWM output, Motor Pilot, Motor
Profiler, Hall closed-loop, sensorless control, or powered-drive readiness is
claimed.

## Flashed Image

- Project:
  `apps/stm32_g474_foc/nucleo_g474re_baseline`
- Image:
  `apps/stm32_g474_foc/nucleo_g474re_baseline/build/Debug/nucleo_g474re_baseline.bin`
- SHA256:
  `86E8CCA5238CA96A0B00E0E3E7F2B3F927947387DA7CB6960ABCE64852B008A3`
- Prior source / build-only safety review:
  `nucleo_g474re_baseline_usb_only_safety_review_2026-06-19.md`

## ST-LINK Evidence

Windows device enumeration showed:

- `STMicroelectronics STLink Virtual COM Port (COM5)`
- `ST-Link Debug`
- `USB mass storage device`

The ST-LINK virtual drive was:

- Drive: `D:`
- Label: `NOD_G474RE`
- Reported USB storage model: `MBED microcontroller USB Device`

`D:\DETAILS.TXT` after flash reported:

```text
Version: V3J17M10
Build:   Oct 17 2025 15:12:06
```

No `FAIL.TXT` was observed in the ST-LINK drive root after copying the image.

## Flash Command

PowerShell copied the reviewed `.bin` to the ST-LINK virtual drive:

```powershell
Copy-Item -LiteralPath <nucleo_g474re_baseline.bin> -Destination D:\ -Force
```

This was a USB/ST-LINK drag-and-drop flash path, not a 24 V or motor test.

## Serial Identity Check

COM5 was read at `115200 8N1`.

Observed boot / periodic status:

```text
BOOT OK
tick_ms=500, led=1, led_toggle=5, report=1, btn=0, btn_press=0, mode=0, mode_name=IDLE, mode_chg=0, target_rpm=0
tick_ms=1000, led=0, led_toggle=10, report=2, btn=0, btn_press=0, mode=0, mode_name=IDLE, mode_chg=0, target_rpm=0
```

Safe query commands:

```text
PING -> PONG
MODE? -> OK unchanged mode=0 mode_name=IDLE
```

Decision:

`USB-only baseline flashed / serial identity confirmed / application in IDLE /
no powered validation / no CN3 physical voltage validation yet`.

## Next Required Physical Check

Before any later 24 V step is considered, keep the setup USB-only and measure
the six CN3 input pins against CN3 GND:

- Black probe: `CN3_15 / GND`
- Red probe one by one: `CN3_1`, `CN3_2`, `CN3_3`, `CN3_4`, `CN3_5`, `CN3_6`
- Expected for this baseline before any powered step: each input remains near
  `0 V`.

If any of the six input pins is not near `0 V`, stop and report the raw value.
