# Static 24 V REG12 Anomaly - 2026-06-19

## Superseded Note

This anomaly record is superseded by the corrected user measurement recorded in
`static_24v_baseline_b1_not_pressed_check_2026-06-19.md`.

Do not use the `REG12: 24 V` value below as the current project fact. The
current corrected user-reported value is `REG12: 0.3 V`.

## Boundary

This record covers a current-limited static 24 V observation after the reviewed
USB-only baseline firmware was flashed and the six CN3 input pins were measured
as 0 V under USB-only conditions.

This is not motor validation, PWM validation, Hall closed-loop validation, or
powered-drive readiness.

Hard stops after this record:

- Keep motor disconnected.
- Do not press B1 for further testing.
- Do not start PWM.
- Do not run Motor Pilot or Motor Profiler.
- Do not continue powered checks until the `REG12` reading is explained.

## Prior Evidence

- USB-only firmware identity was confirmed:
  `BOOT OK`, `PING -> PONG`, `MODE? -> OK unchanged mode=0 mode_name=IDLE`.
- USB-only physical input check:
  `CN3_1` through `CN3_6` all measured `0 V` against `CN3_15 / GND`.
- Source review found no application-level TIM1/TIM8 PWM, MOE, MCSDK start, or
  STDRIVE HIN/LIN control path in `nucleo_g474re_baseline`.

## User-Reported Raw Measurement

Condition:

- CN3 connected.
- B1 not pressed.
- Motor disconnected by boundary.
- 24 V current-limited static check requested.

Raw result reported by the user:

```text
Power-supply current / CV or CC: not reported
CN3_14 3V3: 3.3 V
CN3_13 nFAULT: 3.3 V
REG12: 24 V
VS / 24V_FUSED: 24 V
CN3_1..CN3_6 still 0 V: yes
```

## Interpretation

Good-direction observations:

- `CN3_14 / 3V3 = 3.3 V`.
- `CN3_13 / nFAULT = 3.3 V`.
- `CN3_1..CN3_6` still measured `0 V`.
- `VS / 24V_FUSED = 24 V`.

Blocking observation:

- `REG12 = 24 V` is not acceptable as a pass result if the probe was truly on
  the `REG12` node.

Repo hardware notes identify `REG12` as the STDRIVE101 internal 12 V LDO /
gate-driver supply node. It is connected to C4 4.7 uF and C5 100 nF to GND and
must not be externally driven. `VS / 24V_FUSED` is the node expected to be
24 V.

Therefore this result is treated as one of:

1. the probe touched the `VS / 24V_FUSED` node while believed to be on REG12;
2. the board has a short or assembly issue between `REG12` and `VS / 24V_FUSED`;
3. the REG12 measurement point has been misidentified on the board.

## Decision

`Static 24 V check blocked / nFAULT high and inputs low observed / REG12
reported as 24 V / stop powered progression until REG12-vs-VS is resolved`.

## Required Next Checks

All next checks must be done with:

- HSPY output off.
- 24 V disconnected from the board.
- USB/ST-LINK disconnected for resistance / beep checks.
- Motor disconnected.

Record these raw DMM results:

```text
REG12 correct point -> VS / 24V_FUSED:
REG12 correct point -> GND:
VS / 24V_FUSED -> GND:
REG12 correct point -> 24V input positive:
REG12 correct point -> CN3_14 / 3V3:
```

Also re-identify the physical measurement point:

- `C2/C3` positive side should be `VS / 24V_FUSED`.
- `C4/C5` positive side should be `REG12`.
- The GND side of `C4/C5` should read 0 ohm / beep to GND.
