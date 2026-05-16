# P2 Source Packet Review - 2026-05-16 - Custom NUCLEO STDRIVE101 Capture Package

Review ID: `P2-SOURCE-REVIEW-2026-05-16-001`

Packet type: Packet A preparation.

Decision: `Partial clue / Preparation only`.

## Reviewed Source

| Item | Value |
| --- | --- |
| Package directory | `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/` |
| Workbench guide | `workbench_no_power_configuration_guide_2026-05-16.md` |
| Motor no-power log template | `motor_no_power_measurement_log_2026-05-16.md` |
| Pin assignment table | `pin_assignment_table_2026-05-16.md` |
| Real `.stwb6` present | No |
| Required screenshots present | No |

## Accepted From This Package

- The old `My_First_FOC.stwb6` learning leftover is not accepted as the final
  project source.
- The intended new capture target is `NUCLEO-G474RE` / `STM32G474RETx` plus a
  Custom / Generic STDRIVE101 power stage.
- `EVALSTDRIVE101` is explicitly excluded from the new project-specific
  capture.
- The first speed-feedback path is Hall fallback.
- Sensorless / SMO remains out of scope for the first configuration.
- Motor data remains placeholder-only until no-power records or a later
  hardware-stage Profiler result exists.
- The package captures the required pin-assignment table shape.

## Still Not Accepted

- No new Workbench `.stwb6` has been saved yet.
- No Workbench selected-field screenshot exists yet.
- No accepted TIM1 PWM selected topology exists yet.
- No accepted `PB12/TIM1_BKIN` fault selection exists yet.
- No accepted 3-shunt / OPAMP / ADC selected field exists yet.
- No accepted Hall selected-field screenshot exists yet.
- No accepted `PA2/PA3` exclusion screenshot exists yet.
- No accepted `PB3` SWO release or Hall B ownership evidence exists yet.
- No accepted Packet B/C CN8 or STDRIVE101 protection-path source exists yet.

## Generated-Project Trust

Generated-project trust remains `Not allowed`.

This package does not authorize:

- source generation;
- build-only work;
- flashing;
- 24V;
- power-board connection;
- motor connection;
- Gate PWM output;
- Motor Profiler;
- Hall closed-loop;
- sensorless / SMO claims.

## Required Follow-Up

1. Use the guide to create and save
   `custom_nucleo_stdrive101_2026-05-16.stwb6`.
2. Add the required screenshots under the package `screenshots/` directory.
3. Reopen the saved `.stwb6` and verify it shows the same selected fields.
4. Create a new dated Packet A source review for the actual `.stwb6` and
   screenshots.
5. Upgrade only fields visible in that real source.
