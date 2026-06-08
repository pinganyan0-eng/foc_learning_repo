# CN8 pin probe firmware

This is a NUCLEO-only STM32G474RE pin probe for the PCB2 CN8 mapping.

It is not an MCSDK, FOC, Gate, power-board, 24 V, or motor validation firmware.
Use it only with the NUCLEO powered from USB and the power board fully
disconnected.

## Safety Boundary

- Do not connect CN8 to the power board while flashing or measuring this probe.
- Do not connect 24 V.
- Do not connect a motor.
- Do not connect OUTx, BOOTx, high-side source/switch-node, or Gate nodes to
  an ordinary passive probe ground clip.
- Scope ground may be clipped only to NUCLEO GND for this NUCLEO-only check.

## Output Pattern

TIM6 generates a 20 kHz scheduler tick and toggles six GPIO outputs:

| PCB2 role | CN8 pin | STM32 pin | Approx. square wave |
| --- | --- | --- | --- |
| HIN1 | P1 | PA15 | 50 Hz |
| LIN1 | P2 | PB3 | 100 Hz |
| HIN2 | P3 | PB10 | 200 Hz |
| LIN2 | P4 | PA8 | 400 Hz |
| HIN3 | P5 | PA9 | 1 kHz |
| LIN3 | P6 | PA10 | 2 kHz |

These are identification waveforms, not motor-control PWM waveforms. Their
purpose is to prove that the firmware can drive the six STM32 pins that match
the recovered PCB2 CN8 mapping.

## NUCLEO Arduino Header Measurement Map

Do not infer the NUCLEO Arduino silk label from the STM32 pin name. On the
NUCLEO-G474RE, Arduino `D9` is not `PA9`; use Arduino `D8` to check `PA9`.

| Firmware STM32 pin | Approx. square wave | NUCLEO Arduino silk label / access point | Status |
| --- | --- | --- | --- |
| PA8 | 400 Hz | `D7` | Measured 2026-06-08: about 401 Hz |
| PA9 | 1 kHz | `D8` | Measured 2026-06-08: 1.00 kHz |
| PA10 | 2 kHz | `D2` | Measured 2026-06-08: 2.00 kHz |
| PB3 | 100 Hz | `D3` | Measured 2026-06-08: 100 Hz |
| PB10 | 200 Hz | `D6` | Measured 2026-06-08: 200 Hz |
| PA15 | 50 Hz | ST Morpho `CN7-17` | Measured 2026-06-08: 50.0 Hz |

## Build

```powershell
cmake --preset Debug
cmake --build --preset Debug
```

Expected outputs:

- `build/Debug-mingw/cn8_pin_probe.elf`
- `build/Debug-mingw/cn8_pin_probe.hex`
- `build/Debug-mingw/cn8_pin_probe.bin`

## Measurement Setup

1. Keep the power board disconnected.
2. Keep the motor disconnected.
3. Power the NUCLEO from USB only.
4. Flash `cn8_pin_probe.hex` to the NUCLEO.
5. Clip the oscilloscope ground to NUCLEO GND.
6. Probe the user-facing points in the NUCLEO Arduino header map one at a
   time. For PA15, use ST Morpho `CN7-17`: the odd-numbered column, ninth
   position from the `CN7-1/2` end. Do not touch adjacent `CN7-18` (5 V).

Record one screenshot per pin with time scale, voltage scale, and measured
frequency visible.
