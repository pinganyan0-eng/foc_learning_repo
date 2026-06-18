# Current task

## Task identity

- ID: `TASK-2026-06-18-L4-cn3-connected-static-power-sanity`
- Topic: CN3 connected static supply sanity before any empty Gate waveform work
- Status: `open`
- User approval: 2026-06-18, user accepted continuing after CN3 USB-only logic
  input sanity closed
- Risk level: `L4`
- Planned evidence ID after acceptance:
  `EV-2026-06-18-HW-CN3-CONNECTED-STATIC-POWER-001`
- Review required: yes

## Goal

Check the power board with the reviewed CN3 cable and NUCLEO connected, but
with PWM deliberately disabled. This is a static supply sanity check before any
empty Gate waveform work.

## Allowed

- Connect the reviewed CN3 cable with P1-P6, P13, and P15 only.
- Keep CN3 P7-P12 and P14/3V3 open.
- Connect NUCLEO USB and press RESET.
- Leave B1 unpressed so TIM1 outputs remain disabled.
- Power the power-board 24 V input only through a bench supply current-limited
  to the recorded 0.2 A level.
- Measure supply mode/current and static rails: 5V, 3V3, REG12, and
  P13/nFAULT.
- Update the experiment record only from raw user measurements.

## Prohibited

- No motor.
- No phase wires.
- Do not press B1 during this task.
- Do not intentionally output PWM.
- Do not probe Gate, OUTx, BOOTx, switch nodes, or high-side Vgs.
- Do not run Motor Pilot or Motor Profiler.
- Do not claim Gate waveform, power-stage readiness, motor readiness, Hall
  closed-loop, sensorless, or FOC behavior from this task.

## Acceptance

- Bench supply remains in CV, not CC.
- Input current is stable and comfortably below the 0.2 A current limit.
- 5V, 3V3, REG12, and P13/nFAULT are present and stable.
- LD2 remains off before B1.
- P1 remains inactive before B1.
- No abnormal smell, sound, smoke, or fast heating occurs.

## Operation record

`experiments/2026-06-18_cn3_connected_static_power_sanity/README.md`

## Current result

Open. No CN3-connected static powered measurement is accepted yet.

---

# Previous task

## Task identity

- ID: `TASK-2026-06-17-L4-cn3-usb-only-logic-input-sanity`
- Topic: CN3 installed-cable USB-only logic-input sanity check
- Status: `done-with-limitations`
- Evidence ID: `EV-2026-06-17-HW-CN3-USB-ONLY-LOGIC-INPUT-001`
- Review required: yes

## Previous result

- Pre-B1 DMM low-state sanity passed on CN3 P1-P6 relative to P15/GND.
- P13/P15 and P13/P14 were checked unpowered and showed no beep in the Mohm
  range, so no P13/BKIN hard short to GND or 3V3 was accepted.
- After-B1 P1-P6 logic activity is accepted only for the high-impedance 10X
  oscilloscope method with P13 disconnected: P1-P6 were reported as about
  10 kHz and about 3.3 V.
- P13/BKIN USB-only stop/latch sanity passed with P13 reconnected: pulling P13
  low stopped P1, releasing P13 did not restart output, and RESET plus one B1
  restored output.
- B1 STOP latch and reset/re-arm behavior passed: second B1 stopped P1, third
  B1 did not restart it, and RESET plus one B1 restored output.
- CN3-installed DMM ground-contact probing after B1 turned LD2 off and latched
  the state; this DMM method is recorded as disturbing the unpowered power-board
  input network and must not be reused for PWM checks.

This closed only the USB-only logic-input sanity task. It did not validate Gate
waveforms, 24 V dynamic behavior, OUTx/BOOTx/high-side Vgs, motor operation,
Hall closed-loop, sensorless operation, or FOC runtime behavior.

---

# Earlier task summary

## CN3 15-pin no-power cable remap

- ID: `TASK-2026-06-09-L3-cn8-no-power-cable-remap`
- Status: `done`
- Evidence ID: `EV-2026-06-09-HW-CN8-CABLE-CONTINUITY-001`

Current accepted result:

- The physical power-board control connector is `CN3`; `CN8` is retained only
  as a legacy alias for the same 15-pin control pin list.
- User-reported disconnected-end continuity passed for all eight intended wires
  at 0.1 ohm stable beep: P1-PA8, P2-PA7, P3-PA9, P4-PB14, P5-PA10,
  P6-PB15, P13-PB12, and P15-GND.
- Pairwise isolation passed, P7-P12 and P14/3V3 remain open, and targeted
  post-installation short checks passed.

This task did not authorize 24 V, PWM, Gate probing, OUTx/BOOTx/high-side Vgs
measurement, or motor connection.

## NUCLEO TIM1 complementary PWM

- ID: `TASK-2026-06-08-L3-nucleo-tim1-complementary-pwm`
- Status: `done`
- Evidence IDs:
  - `EV-2026-06-08-FW-TIM1-COMPLEMENTARY-PWM-SOURCE-001`
  - `EV-2026-06-08-FW-TIM1-COMPLEMENTARY-PWM-FLASH-001`
  - `EV-2026-06-08-FW-TIM1-COMPLEMENTARY-PWM-WAVEFORM-001`

Current accepted result:

- Independent TIM1 probe firmware built, flashed, and verified on the isolated
  NUCLEO-G474RE.
- Dynamic TIM1 map is PA8/PA7, PA9/PB14, and PA10/PB15 for CH1/1N, CH2/2N,
  and CH3/3N.
- User oscilloscope evidence accepted all three after-B1 complementary PWM
  pairs at about 10 kHz, no visible high-level overlap, and about 2 us deadtime
  in both transition directions.
- Reset-before-B1 inactive evidence directly covers all six outputs.
- Software STOP and PB12/BKIN latch behavior were observed; source and static
  tests confirm both paths clear global TIM1 MOE.

This task did not approve CN3 power-board behavior, 24 V, Gate probing,
OUTx/BOOTx/high-side Vgs measurement, or motor operation.
