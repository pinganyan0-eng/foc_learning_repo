# 2026-06-18 CN3-connected static power sanity check

Task ID: `TASK-2026-06-18-L4-cn3-connected-static-power-sanity`

## Purpose

Check the power board with the reviewed CN3 cable and NUCLEO connected, but
with PWM deliberately disabled. This is a static supply sanity check before any
empty Gate waveform work.

This task does not validate Gate waveforms, switching nodes, motor behavior,
FOC, Hall closed-loop, or sensorless control.

## Safety boundary

- No motor.
- No phase wires.
- CN3 cable may be installed with P1-P6, P13, and P15 only.
- CN3 P7-P12 and P14/3V3 remain open.
- NUCLEO is connected by USB, but B1 must not be pressed during this task.
- TIM1 outputs remain disabled after RESET / before B1.
- Power board 24V input may be powered only through the bench supply current
  limit described below.
- Do not probe Gate, OUTx, BOOTx, switch nodes, or high-side Vgs.
- Do not run Motor Pilot or Motor Profiler.

## Starting setup

| Item | Required state | Record |
| --- | --- | --- |
| Motor | Disconnected | Pending |
| Phase wires | Disconnected | Pending |
| CN3 P1-P6 | Connected to reviewed NUCLEO endpoints | Pending |
| CN3 P13 | Connected to PB12/BKIN/nFAULT path | Pending |
| CN3 P15 | Connected to NUCLEO GND | Pending |
| CN3 P14/3V3 | Open / no wire | Pending |
| NUCLEO state | USB connected, RESET pressed, B1 not pressed | Pending |
| Bench supply | Output off before wiring | Pending |
| Supply setting | 24V, 0.2A current limit | Pending |

## Power-on steps

1. Keep bench supply output off.
2. Confirm motor and phase wires are disconnected.
3. Confirm CN3 P14/3V3 is open.
4. Connect the CN3 cable.
5. Connect NUCLEO USB.
6. Press NUCLEO RESET and do not press B1.
7. Set bench supply to 24V and 0.2A current limit, output still off.
8. Connect bench supply positive to power-board 24V input and negative to
   power-board power GND.
9. Turn on bench supply output and watch current immediately.
10. If current is stable and supply remains in CV, measure rails.

## Immediate stop conditions

Turn off the bench supply output immediately if any of these happen:

- Supply enters CC or current rises toward 0.2A.
- Smoke, spark, smell, abnormal sound, or fast heating occurs.
- 5V, 3V3, REG12, or nFAULT is missing, unstable, or obviously wrong.
- LD2 turns on unexpectedly before B1, or PWM is seen before B1.
- Any probe, clip, or wire is unstable or touches neighboring pins.

## Measurement table

| Check | Expected | Observed | Result |
| --- | --- | --- | --- |
| Supply mode | CV, not CC | Pending | Pending |
| Input current | Stable, well below 0.2A | Pending | Pending |
| 5V to GND | About 5V | Pending | Pending |
| 3V3 to GND | About 3.3V | Pending | Pending |
| REG12 to GND | About 12V | Pending | Pending |
| P13/nFAULT to GND | High / non-fault, about 3.3V if pull-up is active | Pending | Pending |
| LD2 before B1 | Off | Pending | Pending |
| P1 before B1 | No PWM | Pending | Pending |
| Abnormal smell/sound/heat | None | Pending | Pending |

## Current status

`OPEN`: operation sheet created. No powered CN3-connected static measurement
has been recorded yet.