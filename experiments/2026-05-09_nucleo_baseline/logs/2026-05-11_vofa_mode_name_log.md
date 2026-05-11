# 2026-05-11 VOFA+ mode-name serial log

## Source

- Source type: user-provided VOFA+ screenshot in Codex chat.
- Tool: VOFA+ 1.3.10.
- Port: COM5, STMicroelectronics STLink Virtual COM Port.
- Serial settings shown: 115200 baud, 8 data bits, no parity, 1 stop bit.
- Firmware behavior under observation: B1 event counter and application mode state machine.

## Observed excerpt

```text
tick_ms=3500, led=1, led_toggle=35, report=7, btn=0, btn_press=1, mode=1, mode_name=ARMED, mode_chg=1
tick_ms=4000, led=0, led_toggle=40, report=8, btn=0, btn_press=1, mode=1, mode_name=ARMED, mode_chg=1
tick_ms=4500, led=1, led_toggle=45, report=9, btn=0, btn_press=2, mode=2, mode_name=RUN_SIM, mode_chg=2
tick_ms=5000, led=0, led_toggle=50, report=10, btn=0, btn_press=2, mode=2, mode_name=RUN_SIM, mode_chg=2
tick_ms=5500, led=1, led_toggle=55, report=11, btn=0, btn_press=3, mode=0, mode_name=IDLE, mode_chg=3
tick_ms=6000, led=0, led_toggle=60, report=12, btn=0, btn_press=3, mode=0, mode_name=IDLE, mode_chg=3
tick_ms=6500, led=1, led_toggle=65, report=13, btn=0, btn_press=4, mode=1, mode_name=ARMED, mode_chg=4
tick_ms=7000, led=0, led_toggle=70, report=14, btn=0, btn_press=4, mode=1, mode_name=ARMED, mode_chg=4
tick_ms=7500, led=1, led_toggle=75, report=15, btn=0, btn_press=5, mode=2, mode_name=RUN_SIM, mode_chg=5
tick_ms=8000, led=0, led_toggle=80, report=16, btn=0, btn_press=5, mode=2, mode_name=RUN_SIM, mode_chg=5
```

## Interpretation

- LPUART1/ST-LINK VCP serial output is working through COM5.
- The app mode state machine follows `IDLE -> ARMED -> RUN_SIM -> IDLE`.
- `mode` and `mode_name` agree:
  - `0 = IDLE`
  - `1 = ARMED`
  - `2 = RUN_SIM`
- `btn_press` and `mode_chg` increase together, so one accepted button event is producing one state transition in this excerpt.
- `led_toggle` increases by 5 between 500 ms reports, consistent with a 100 ms LED task.

## Boundaries

- This is NUCLEO baseline evidence only.
- It does not validate MCSDK, motor control, power board hardware, 24V power-up, PWM gate waveforms, current sensing, Hall closed loop, or sensorless FOC.
