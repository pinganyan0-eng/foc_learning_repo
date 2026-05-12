# 2026-05-12 COM5 SET_RPM validation

## Scope

- Board: NUCLEO-G474RE through ST-LINK VCP `COM5`.
- Firmware: `apps/stm32_g474_foc/nucleo_g474re_baseline/build/Debug/nucleo_g474re_baseline.elf`.
- Flash method: generated `nucleo_g474re_baseline.bin` with STM32Cube bundled `arm-none-eabi-objcopy`, then copied the BIN to ST-LINK mass-storage drive `D:` (`NOD_G474RE`).
- Safety boundary: NUCLEO USB only. No 24 V bus, no power board, no motor, no PWM power-stage validation.

## Commands validated

```text
>>> MODE?
OK unchanged mode=0 mode_name=IDLE

>>> SET_RPM abc
ERR parse cmd=SET_RPM

>>> SET_RPM 999999
ERR range cmd=SET_RPM rpm=999999 min=-4000 max=4000

>>> SET_RPM 1200
ERR bad_state cmd=SET_RPM mode=0 mode_name=IDLE

>>> ARM
OK changed mode=1 mode_name=ARMED

>>> SET_RPM 1200
OK target_rpm=1200 mode=1 mode_name=ARMED

tick_ms=44000, led=0, led_toggle=440, report=88, btn=0, btn_press=0, mode=1, mode_name=ARMED, mode_chg=1, target_rpm=1200

>>> MODE?
OK unchanged mode=1 mode_name=ARMED

>>> STOP
OK changed mode=0 mode_name=IDLE

tick_ms=49500, led=1, led_toggle=495, report=99, btn=0, btn_press=0, mode=0, mode_name=IDLE, mode_chg=2, target_rpm=0

>>> MODE?
OK unchanged mode=0 mode_name=IDLE

>>> PING
PONG
```

## Result

- `PING`, `MODE?`, `ARM`, `STOP`, and learning-only `SET_RPM <rpm>` responses match the command table.
- `SET_RPM abc` is rejected as parse error.
- `SET_RPM 999999` is rejected as range error.
- `IDLE + SET_RPM 1200` is rejected as bad state.
- `ARMED + SET_RPM 1200` updates only simulated `target_rpm`.
- `STOP` clears `target_rpm` and returns to `IDLE`.

## Notes

- An initial multi-command run after flashing only captured `PONG`; after re-copying the BIN to force a clean reset, the slower command-by-command validation succeeded.
- This validates the NUCLEO baseline command path and simulated target variable only. It is not motor-control validation and does not prove any power-stage behavior.
