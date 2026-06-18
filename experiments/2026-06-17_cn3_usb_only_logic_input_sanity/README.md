# 2026-06-17 CN3 USB-only logic-input sanity check

Task ID: `TASK-2026-06-17-L4-cn3-usb-only-logic-input-sanity`

## Purpose

Check the already-remapped CN3 control cable with the power board still
unpowered. This is the first board-joined low-voltage sanity step after the
NUCLEO-only TIM1 complementary PWM validation.

The physical PCB connector is `CN3`. Older schematic/history records may call
the same 15-pin control pin list `CN8`; in this record `CN3 Pn` is the physical
connector pin and `CN8` is only a legacy alias. The separate 6-pin connector is
not used.

## Safety boundary

- NUCLEO is powered only from ST-LINK USB.
- CN3 cable may be installed only with the reviewed eight-wire map.
- Power-board 24 V input remains disconnected.
- Motor and phase wires remain disconnected.
- CN3 P7-P12 and P14/3V3 remain unconnected.
- Do not probe Gate, OUTx, BOOTx, switch nodes, or high-side Vgs.
- Do not claim Gate PWM, power-stage readiness, 24 V readiness, motor
  readiness, Hall closed-loop, or FOC behavior from this check.

## Reviewed CN3 cable map

| CN3 pin | Signal | NUCLEO endpoint |
| --- | --- | --- |
| P1 | HIN1 | PA8 / CN10-23 |
| P2 | LIN1 | PA7 / CN10-15 |
| P3 | HIN2 | PA9 / CN10-21 |
| P4 | LIN2 | PB14 / CN10-28 |
| P5 | HIN3 | PA10 / CN10-33 |
| P6 | LIN3 | PB15 / CN10-26 |
| P13 | nFAULT / BKIN | PB12 / CN10-16 |
| P15 | GND_SIGNAL | NUCLEO GND |

CN3 P7-P12 and P14/3V3 remain open.

## Firmware context

The active intended firmware is:

```text
apps/stm32_g474_foc/tim1_complementary_pwm_probe/
```

Expected behavior from the already validated NUCLEO-only test:

- Reset / before B1: TIM1 MOE is clear and P1-P6 should stay low.
- First B1 press: TIM1 MOE arms and P1-P6 carry 10 kHz complementary PWM.
- Second B1 press: STOP clears MOE and latches off until reset.
- Pulling PB12 / CN3 P13 low to NUCLEO GND: BKIN clears MOE and latches off
  until reset.

## Operation checklist

1. Confirm 24 V, motor, and phase wires are disconnected.
2. Confirm CN3 P7-P12 and P14/3V3 are not connected.
3. Install only the reviewed CN3 cable: P1-P6, P13, and P15.
4. Power only the NUCLEO through USB.
5. Before pressing B1, measure CN3 P1-P6 relative to CN3 P15 / GND.
6. If all P1-P6 are near 0 V before B1, press B1 once and check logic PWM
   presence on P1-P6.
7. Press B1 a second time and confirm outputs return low and remain stopped.
8. After reset and one B1 arm, briefly pull CN3 P13 / PB12 to P15 / GND and
   confirm outputs stop and remain stopped until reset.

## Result table

Fill this table from user-reported raw observations.

| Check | Expected | Observed | Result |
| --- | --- | --- | --- |
| Pre-B1 P1-HIN1 to P15 | Near 0 V / no PWM | User reported 0 V | Pass for DC low sanity |
| Pre-B1 P2-LIN1 to P15 | Near 0 V / no PWM | User reported 0 V | Pass for DC low sanity |
| Pre-B1 P3-HIN2 to P15 | Near 0 V / no PWM | User reported 0 V | Pass for DC low sanity |
| Pre-B1 P4-LIN2 to P15 | Near 0 V / no PWM | User reported 0 V | Pass for DC low sanity |
| Pre-B1 P5-HIN3 to P15 | Near 0 V / no PWM | User reported 0 V | Pass for DC low sanity |
| Pre-B1 P6-LIN3 to P15 | Near 0 V / no PWM | User reported 0 V | Pass for DC low sanity |
| P14/3V3 remains open | No wire / no intentional connection | Kept open throughout this task by setup rule; earlier cable task also verified P14 open | Pass for task boundary |
| P13/P15 no-hard-short check | No beep, only high resistance | User reported no beep in Mohm range | Pass for no-hard-short sanity |
| P13/P14 no-hard-short check | No beep, only high resistance | User reported no beep in Mohm range | Pass for no-hard-short sanity |
| After B1 P1-P6 logic activity | 0-3.3 V logic PWM present | With P13 disconnected and 10X oscilloscope probing, user reported P1-P6 all behaved like P1: reset-before-B1 no waveform, after B1 LD2 stayed on, about 10 kHz and about 3.3 V waveform | Pass for high-impedance USB-only logic-input sanity with P13 disconnected |
| Second B1 STOP | Outputs low, cannot re-arm without reset | User reported: second B1 press turned LD2 off and P1 off | Pass for STOP latch |
| Post-STOP re-arm after RESET | Outputs low until reset, then re-arm on next B1 | User reported: third B1 after STOP did not restore; RESET followed by one B1 restored output | Pass for STOP reset/re-arm chain |
| PB12/P13 BKIN | Outputs stop and latch until reset | User reported: before pulling P13 low, LD2 was on and P1 was about 10 kHz / 3.3 V; when P13 was pulled low, P1 stopped; after releasing P13, output remained stopped; after RESET and one B1 press, output recovered | Pass for USB-only BKIN stop/latch sanity |

## 2026-06-18 ground-contact stop-latch observation

During the after-B1 DMM setup, the user reported that touching the black DMM
probe to the intended ground point caused `LD2` to turn off and stay off after
the probe was removed. The DMM lead jacks were visually checked from the user
photo: red lead was in the `V/ohm` jack and black lead was in the `LO/COM`
jack, so this was not recorded as a current-jack short error.

Recovery check:

```text
After RESET, before B1: LD2 off
After pressing B1 once: LD2 on
```

The same black-probe-to-NUCLEO-GND action did not turn `LD2` off when CN3 was
disconnected from the power board. P13/P15 and P13/P14 were then checked with
the board unpowered and reported as no-beep in the Mohm range. This does not
support a hard short from P13/BKIN to GND or 3V3. The observation is treated as
an unresolved CN3-installed probing interaction, not as evidence of NUCLEO or
power-board damage.

## Current status

`DONE WITH LIMITATIONS`: pre-B1 DMM low-state sanity passed on CN3 P1-P6 relative to P15 / GND. P13/P15 and P13/P14 were checked unpowered and showed no beep in the Mohm range. After-B1 P1-P6 logic activity is accepted only for the high-impedance 10X oscilloscope method with P13 disconnected. USB-only BKIN stop/latch sanity passed with P13 reconnected. STOP latch and reset/re-arm behavior passed. A CN3-installed DMM ground-contact stop-latch observation was recorded; do not use the DMM probing method for after-B1 PWM checks on the unpowered power board.

This closes only the CN3 USB-only logic-input sanity task. It does not validate Gate waveforms, 24 V dynamic behavior, OUTx/BOOTx/high-side Vgs, motor operation, Hall closed-loop, sensorless operation, or FOC runtime behavior.
