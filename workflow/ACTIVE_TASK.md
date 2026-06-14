# Current task

## Task identity

- ID: `TASK-2026-06-09-L3-cn8-no-power-cable-remap`
- Topic: CN3 15-pin loose-wire remap and no-power continuity review
- Status: `done`
- User approval: 2026-06-09, user explicitly requested implementation of the
  reviewed CN8 no-power cable plan
- Risk level: `L3`
- Planned evidence ID after acceptance:
  `EV-2026-06-09-HW-CN8-CABLE-CONTINUITY-001`
- Review required: yes

## Goal

Build and verify an eight-wire loose cable for the physical PCB `CN3` 15-pin
control connector. Earlier schematic/history notes may call the same pin list
`CN8`; `CN8` is now treated as a legacy alias for this task, not the separate
6-pin connector.

- CN3/CN8-alias P1-P6 to PA8/PA7/PA9/PB14/PA10/PB15;
- CN3/CN8-alias P13 to PB12;
- CN3/CN8-alias P15 to reviewed NUCLEO GND.

## Allowed

- Rearrange and label the loose wires while both cable ends are disconnected.
- Measure wire continuity and pairwise isolation with a DMM.
- Photograph the loose cable, CN8 pin-1 orientation, NUCLEO endpoints, and
  open P14 position.
- Update the experiment record only from reported raw measurements and
  reviewed photos.

## Prohibited

- No NUCLEO USB, 24 V, motor, or phase-wire connection.
- Do not install the cable into either board before continuity and photo
  review pass.
- Do not populate CN3/CN8-alias P7-P12 or P14.
- Do not use the separate 6-pin connector for this TIM1 cable.
- No firmware change, flash, PWM output, Gate measurement, or oscilloscope
  work.

## Acceptance

- All eight intended wires show stable low-resistance continuity.
- No intended wire has continuity to another intended wire.
- P7-P12 and P14 are visibly and electrically unconnected.
- Photos make CN8 pin 1 and all NUCLEO endpoints reviewable.

## Operation record

`experiments/2026-06-09_cn8_no_power_cable_remap/2026-06-09_cn8_cable_continuity_record.md`

## Current result

- The physical power-board control connector is `CN3`; `CN8` is retained only
  as a legacy alias for the same 15-pin control pin list.
- The separate 6-pin connector was explicitly rejected for this TIM1 cable.
- User-reported disconnected-end continuity passed for all eight intended
  wires at 0.1 ohm stable beep: P1-PA8, P2-PA7, P3-PA9, P4-PB14, P5-PA10,
  P6-PB15, P13-PB12, and P15-GND.
- User-reported pairwise isolation passed: all listed installed-wire pairs
  showed no beep.
- P7-P12 and P14/3V3 remain open.
- Reviewed photos support installation into the long physical CN3 15-pin
  connector and NUCLEO CN10/Morpho area; endpoint continuity remains the
  primary evidence.
- Post-installation targeted no-power sanity checks passed with no beep on
  P14-P15, P1-P2, P3-P4, P5-P6, and P13-P15.

This closes only the no-power cable mapping and installation review. It does
not authorize NUCLEO USB, 24 V, PWM, Gate probing, OUTx/BOOTx/high-side Vgs
measurement, or motor connection. The next physical step must be opened as a
separate reviewed task.

---

# Previous task

## Task identity

- ID: `TASK-2026-06-08-L3-nucleo-tim1-complementary-pwm`
- Topic: NUCLEO-G474RE TIM1 three-pair complementary PWM logic validation
- Status: `done`
- User approval: 2026-06-08, user explicitly requested implementation of the
  reviewed NUCLEO-only TIM1 plan
- Risk level: `L3`
- Definition of Done: `workflow/definition_of_done.md#工程代码任务`
- Evidence ID: `EV-2026-06-08-FW-TIM1-COMPLEMENTARY-PWM-SOURCE-001`
- Review required: yes

## Previous task closure

`TASK-2026-06-07-L2-nucleo-pa8-square-wave` is closed. It was superseded by
the dedicated `cn8_pin_probe` project, which was built, flashed, and measured
on all six identification outputs. Evidence:

- `EV-2026-06-08-FW-CN8-PIN-PROBE-FLASH-001`
- `EV-2026-06-08-FW-CN8-PIN-PROBE-WAVEFORM-001`

## Goal

Build and measure a separate NUCLEO-only TIM1 firmware with:

- three main/complementary PWM pairs;
- center-aligned 10 kHz operation;
- 25% duty;
- approximately 2 us hardware deadtime;
- reset/startup outputs inactive;
- explicit B1 arm;
- latched software STOP;
- active-low PB12/TIM1_BKIN latched shutdown.

## Allowed

- Modify only the new
  `apps/stm32_g474_foc/tim1_complementary_pwm_probe/` project and supporting
  tests/documents.
- Build and flash only while the NUCLEO is isolated from CN8, the power board,
  24 V, and the motor.
- Measure PA8/PA7, PA9/PB14, and PA10/PB15 relative to NUCLEO GND.
- Pull PB12 to NUCLEO GND for the reviewed NUCLEO-only BKIN test.

## Prohibited

- Do not connect the CN8 cable or power board in this task.
- Do not connect 24 V or the motor.
- Do not probe OUTx, BOOTx, switch nodes, or high-side Vgs.
- Do not treat source tests or a successful build as waveform evidence.
- Do not reuse the old PA15/PB3/PB10 identification mapping as the dynamic
  complementary PWM cable map.

## Current result

- New source project implemented.
- Dynamic TIM1 cable mapping decision recorded.
- Static contract tests pass: 6/6.
- Repository unittest run passes: 20/20.
- STM32 project safe-claim dry run reports no unsafe added claims.
- ARM Debug build succeeds and generated ELF/HEX/BIN.
- `tim1_complementary_pwm_probe.hex` was flashed to NUCLEO-G474RE through
  ST-LINK SN `002F00253235511337333439`; STM32CubeProgrammer verified the
  download successfully and performed software reset.
- User-provided oscilloscope screenshots accept all three after-B1 pairs:
  PA8/PA7, PA9/PB14, and PA10/PB15 each show about 10.0 kHz complementary
  PWM, no visible high-level overlap, and about 2 us deadtime in both
  transition directions. STOP and BKIN action/latching were subsequently
  accepted on measured PA10/PB15.
- User-provided PA8/PA7 dual-channel screenshots showed same-phase high
  windows, including the temporary `CCxNP` polarity-inversion attempt. These
  are recorded as failed/inconclusive intermediate captures, not accepted
  evidence.
- The temporary `TIM_CCER_CC1NP`, `TIM_CCER_CC2NP`, and `TIM_CCER_CC3NP`
  change was removed. The current source uses TIM1 default CHxN complementary
  polarity and the static tests now reject accidental `CCxNP` reintroduction.
- On 2026-06-09 the rollback build passed 20/20 tests, built successfully, and
  was flashed under reset to NUCLEO-G474RE. STM32CubeProgrammer verified the
  download and performed software reset. The D7/D11 retest is accepted below.
- User-provided PA8/PA7 reset-before-B1 captures show no 0-3.3 V PWM. Because
  the captures used sensitive or non-uniform vertical scales, they are recorded
  as preliminary reset/no-large-PWM evidence; final both-channel 2 V/div and
  20 us/div startup-low evidence remains pending.
- User-provided PA8/PA7 reset-before-B1 capture at 2 V/div on both channels
  and 20 us/div shows flat traces with no PWM. PA8/PA7 startup-low evidence is
  accepted for this checked pair; startup-low for the other pairs remains
  unmeasured.
- User-provided PA8/PA7 after-B1 full-period capture at 2 V/div and 20 us/div
  shows about 10.0 kHz complementary PWM with no visible high-level overlap.
  PA8/PA7 full-period complementary evidence is accepted.
- User-provided PA8/PA7 edge zoom at 2 V/div and 1 us/div shows PA7/CH1N
  falling before PA8/CH1 rising by about 2 us. This accepts the first deadtime
  direction for PA8/PA7; the opposite direction is accepted below.
- User-provided PA8/PA7 opposite-edge zoom shows PA8/CH1 falling before
  PA7/CH1N rising by about 2 us. PA8/PA7 is now accepted for startup-low,
  10 kHz full-period complementary behavior, no visible high-level overlap, and
  both-direction deadtime.
- User-provided PA9/PB14 full-period and edge-zoom captures show about
  10.0 kHz complementary PWM after B1, no visible high-level overlap, and about
  2 us deadtime in both transition directions. PA9/PB14 is accepted for the
  checked after-B1 complementary PWM and deadtime behavior.
- User-provided PA10/PB15 full-period and edge-zoom captures show about
  10.0 kHz complementary PWM after B1, no visible high-level overlap, and about
  2 us deadtime in both transition directions. PA10/PB15 is accepted for the
  checked after-B1 complementary PWM and deadtime behavior.
- User-provided PA10/PB15 captures after the second B1 press show both measured
  outputs inactive. A further B1 press without reset does not restart PWM.
  Software STOP action and latch behavior are accepted on the measured pair;
  BKIN was then tested separately.
- Pulling PB12/CN10-16 low stops the measured PA10/PB15 pair. Releasing PB12
  and pressing B1 without reset does not restart PWM, accepting BKIN latch
  behavior on the measured pair. After reset, PA10/PB15 remain inactive until
  B1 is pressed once, then return to about 10.0 kHz complementary PWM.
- Reset-before-B1 captures now directly cover PA8/PA7, PA9/PB14, and
  PA10/PB15 at 2 V/div and 20 us/div. All six outputs have direct startup-low
  evidence.
- The NUCLEO-only TIM1 complementary PWM task is complete. STOP and BKIN were
  directly observed on PA10/PB15; source and static tests confirm both paths
  clear the global TIM1 MOE controlling all three pairs.
- DT/MODE design evidence is closed: the archived schematic directly shows
  `U1 Pin 2 / DT/MODE -> GND_POWER`, and the populated `R_GND_ISO` link
  measured approximately 0.1 ohm. Physical cable continuity/orientation and
  disconnected-supply evidence remain prerequisites before any later
  power-board cable installation.

## Acceptance

- ARM Debug build succeeds and produces ELF/HEX/BIN.
- On reset, all six outputs remain inactive until B1.
- All three pairs measure approximately 10 kHz, 25% duty, and 2 us deadtime
  with no simultaneous high state.
- Second B1 press stops all outputs and cannot re-arm without reset.
- Pulling PB12 low stops all outputs asynchronously and cannot re-arm without
  reset.

## Rollback

Flash the previously verified
`apps/stm32_g474_foc/cn8_pin_probe/build/Debug-mingw/cn8_pin_probe.hex`, or
reset and leave B1 unpressed. The new firmware never enables MOE automatically.
