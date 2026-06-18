# PA7 GPIO probe

This is a NUCLEO-G474RE-only diagnostic firmware for the PA7/D11 physical
output path.

It is not TIM1 complementary PWM, MCSDK, FOC, Gate, power-board, 24 V, or motor
validation firmware.

## Safety boundary

- Keep 24 V, the motor, phase wires, and the power board disconnected.
- Power only the NUCLEO through ST-LINK USB.
- Measure only PA7/D11, PA8/D7, and NUCLEO GND.

## Expected behavior

After reset:

| Point | Expected |
| --- | --- |
| PA7 / D11 | About 3.3 V |
| PA8 / D7 | About 3.3 V |
| LD2 / PA5 | On |

If PA8/D7 measures about 3.3 V and PA7/D11 remains 0 V with this firmware, the
issue is outside TIM1 CH1N configuration and should be treated as a PA7 physical
pin, measurement-point, board-jumper, or damage/strap question before any
power-board work continues.
