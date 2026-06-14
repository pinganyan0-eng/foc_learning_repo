# NUCLEO TIM1 complementary PWM probe - 2026-06-08

Evidence IDs:

- `EV-2026-06-08-FW-TIM1-COMPLEMENTARY-PWM-SOURCE-001`
- `EV-2026-06-08-FW-TIM1-COMPLEMENTARY-PWM-FLASH-001`
- `EV-2026-06-08-FW-TIM1-COMPLEMENTARY-PWM-WAVEFORM-001`
- `EV-2026-06-09-HW-DT-MODE-SCHEMATIC-001`

## Purpose

Prepare and verify a NUCLEO-only firmware that generates three TIM1
main/complementary PWM pairs with explicit arm, latched software STOP,
active-low BKIN shutdown, and hardware deadtime.

This experiment does not approve a power-board connection.

## Safety boundary

- Power board disconnected.
- CN8 cable disconnected.
- 24 V disconnected.
- Motor disconnected.
- NUCLEO powered from ST-LINK USB only.
- Passive probe ground connected only to NUCLEO GND.

## Firmware

- Source:
  `apps/stm32_g474_foc/tim1_complementary_pwm_probe/`
- Output map:
  `hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/2026-06-08_tim1_dynamic_cable_mapping_decision.md`
- Test values: center-aligned 10 kHz, 25% duty, DTG `0xCA`
  (approximately 1.976 us at 170 MHz).

## Source implementation result

- Separate project added; `cn8_pin_probe` was not modified.
- Startup defaults to `MOE=0` and inactive-low outputs.
- First B1 press arms the outputs.
- Second B1 press clears MOE and latches STOP until reset.
- Active-low PB12/TIM1_BKIN clears MOE and latches the fault until reset.
- AOE is not enabled.
- TIM1 is frozen while the core is halted by a debugger.
- CHxN outputs use TIM1's default complementary relationship. A temporary
  `CC1NP/CC2NP/CC3NP` polarity-inversion attempt was rejected after the
  follow-up PA8/PA7 capture still showed same-phase high windows.

## Build and flash status

The ARM Debug build completed after running CMake outside the restricted
sandbox so it could execute the local STM32 GNU Arm toolchain.

Static verification completed before build:

- TIM1 source contract tests: 6/6 passing.
- Repository unittest run: 20/20 passing.
- STM32 project safe-claim dry run: no unsafe added claims detected.

Build commands:

```powershell
$env:PATH='C:\Users\gregrg\AppData\Local\stm32cube\bundles\gnu-tools-for-stm32\14.3.1+st.2\bin;' + $env:PATH
cmake --preset Debug
cmake --build --preset Debug
```

Build output summary:

| Region | Used | Total | Used % |
| --- | --- | --- | --- |
| RAM | 1600 B | 128 KB | 1.22% |
| FLASH | 6672 B | 512 KB | 1.27% |

`arm-none-eabi-size` summary:

| text | data | bss | dec | hex |
| --- | --- | --- | --- | --- |
| 6660 | 12 | 1588 | 8260 | 2044 |

Generated files:

- `build/Debug-mingw/tim1_complementary_pwm_probe.elf`
- `build/Debug-mingw/tim1_complementary_pwm_probe.hex`
- `build/Debug-mingw/tim1_complementary_pwm_probe.bin`

Flash summary:

- User confirmed before flashing that only NUCLEO USB was connected.
- ST-LINK SN: `002F00253235511337333439`
- ST-LINK FW: `V3J17M10`
- Board: `NUCLEO-G474RE`
- Target voltage: 3.28 V
- SWD frequency: 8000 KHz
- Device ID: `0x469`
- Device name: STM32G47x/G48x/G414
- NVM size: 512 KBytes
- File: `tim1_complementary_pwm_probe.hex`
- Programmed size reported by STM32CubeProgrammer: 6.52 KB
- Address: `0x08000000`
- Download verified successfully.
- Software reset performed.

Polarity attempt and rollback:

- Trigger: PA8/PA7 dual-channel scope capture showed high-window overlap, so
  the capture was rejected as complementary PWM evidence.
- Attempt: `TIM_CCER_CC1NP`, `TIM_CCER_CC2NP`, and `TIM_CCER_CC3NP` were added
  for physical CHxN output inversion.
- Result: the follow-up PA8/PA7 capture still showed same-phase high windows,
  so the attempt was rejected and the `CCxNP` bits were removed.
- Static verification after rollback: repository unittest run 20/20 passing;
  STM32 project safe-claim dry run reported no unsafe added claims.
- Build after rollback: completed on 2026-06-09; RAM 1600 B, FLASH 6672 B.
- Flash after rollback: completed on 2026-06-09 using ST-LINK connect under
  reset at reported SWD 3300 KHz. STM32CubeProgrammer v2.22.0 programmed
  6.52 KB at `0x08000000`, verified successfully, and performed software
  reset.

## NUCLEO-only measurement record

The ARM build and NUCLEO flash are complete. Do not fill this table until the
user provides oscilloscope evidence with all prohibited hardware disconnected.

| Check | Expected | Observed | Evidence |
| --- | --- | --- | --- |
| Reset/startup | Six outputs inactive low before B1 | Accepted across all three pairs: PA8/PA7, PA9/PB14, and PA10/PB15 were directly observed at 2 V/div and 20 us/div with flat traces and no PWM after reset before B1 | `photos/2026-06-09_tim1_pa8_pa7_reset_low_2v_20us_scope.jpg`; `photos/2026-06-09_tim1_pa9_pb14_reset_before_b1_low_scope.jpg`; `photos/2026-06-09_tim1_after_bkin_reset_before_b1_low_scope.jpg` |
| PA8 / PA7 | 10 kHz complementary, about 25%, about 2 us deadtime | Accepted after rollback flash: D7/PA8 and D11/PA7 show reset-before-B1 no PWM, about 10.0 kHz complementary PWM after B1, no visible high-level overlap, and about 2 us deadtime in both transition directions | `photos/2026-06-08_tim1_pa8_d7_10khz_single_channel_scope.jpg`; `photos/2026-06-08_tim1_pa8_pa7_same_phase_before_polarity_fix_scope.jpg`; `photos/2026-06-08_tim1_pa8_pa7_same_phase_wrong_chxn_polarity_scope.jpg`; `photos/2026-06-09_tim1_pa8_pa7_reset_low_2v_20us_scope.jpg`; `photos/2026-06-09_tim1_pa8_pa7_after_b1_full_period_initial_scope.jpg`; `photos/2026-06-09_tim1_pa8_pa7_after_b1_full_period_pass_scope.jpg`; `photos/2026-06-09_tim1_pa8_pa7_deadtime_ch1_rise_zoom_scope.jpg`; `photos/2026-06-09_tim1_pa8_pa7_deadtime_ch1_fall_zoom_scope.jpg` |
| PA9 / PB14 | 10 kHz complementary, about 25%, about 2 us deadtime | Accepted after rollback flash: PA9/D8 and PB14/CN10-28 show about 10.0 kHz complementary PWM after B1, no visible high-level overlap, and about 2 us deadtime in both transition directions | `photos/2026-06-09_tim1_pa9_pb14_after_b1_full_period_pass_scope.jpg`; `photos/2026-06-09_tim1_pa9_pb14_deadtime_ch2_rise_zoom_scope.jpg`; `photos/2026-06-09_tim1_pa9_pb14_deadtime_ch2_fall_zoom_scope.jpg` |
| PA10 / PB15 | 10 kHz complementary, about 25%, about 2 us deadtime | Accepted after rollback flash: PA10/D2 and PB15/CN10-26 show about 10.0 kHz complementary PWM after B1, no visible high-level overlap, and about 2 us deadtime in both transition directions | `photos/2026-06-08_tim1_pa10_d2_10khz_single_channel_scope.jpg`; `photos/2026-06-09_tim1_pa10_pb15_after_b1_full_period_pass_scope.jpg`; `photos/2026-06-09_tim1_pa10_pb15_deadtime_ch3_rise_zoom_scope.jpg`; `photos/2026-06-09_tim1_pa10_pb15_deadtime_ch3_fall_zoom_scope.jpg` |
| Second B1 press | All six stop and remain stopped until reset | Accepted on measured PA10/PB15 pair: second B1 press stops both outputs low; an additional B1 press does not restart PWM, demonstrating the software STOP latch on the measured pair | `photos/2026-06-09_tim1_second_b1_stop_low_scope.jpg`; `photos/2026-06-09_tim1_stop_latched_repress_b1_low_scope.jpg` |
| PB12 pulled low | All six stop asynchronously and remain stopped | Accepted on measured PA10/PB15 pair: pulling PB12/CN10-16 low stops both outputs; after releasing PB12 and pressing B1 again without reset, both remain inactive, demonstrating the BKIN latch on the measured pair | `photos/2026-06-09_tim1_bkin_pb12_low_stop_scope.jpg`; `photos/2026-06-09_tim1_bkin_latched_repress_b1_low_scope.jpg` |
| Reset after break | Outputs remain disabled until B1 | Accepted on measured PA10/PB15 pair: after BKIN, reset leaves both outputs inactive before B1; pressing B1 once restores about 10.0 kHz complementary PWM | `photos/2026-06-09_tim1_after_bkin_reset_before_b1_low_scope.jpg`; `photos/2026-06-09_tim1_after_bkin_reset_b1_rearm_scope.jpg` |

## Acceptance rule

This task can close only after:

- the ARM build succeeds;
- startup-low behavior is measured;
- all three complementary pairs show no overlap and approximately 2 us
  deadtime in both transition directions;
- software STOP and BKIN both remain latched until reset.

Even after acceptance, Gate, power-board, 24 V, and motor validation remain
separate blocked tasks.

## DT/MODE design confirmation

- The existing user-provided schematic was re-reviewed at higher zoom on
  2026-06-09.
- It directly shows `U1 Pin 2 / DT/MODE -> GND_POWER`.
- The populated `R_GND_ISO` component measured approximately 0.1 ohm
  end-to-end.
- STDRIVE101 is therefore configured for six-input mode at design-evidence
  level, with STM32 owning complementary timing and deadtime.
- Direct continuity probing of the fine QFN pin was intentionally abandoned
  because the available probes were too coarse.

This closes the DT/MODE design prerequisite only. Physical cable continuity,
orientation, and disconnected-supply evidence remain required before CN8
installation.
