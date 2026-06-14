# DT/MODE no-power confirmation sheet

Status: `confirmed by schematic design evidence`

This measurement concerns the power board, but it must be performed with the
power board fully unpowered, disconnected, and discharged. It is not required
to build or measure the NUCLEO-only firmware.

## Preconditions

- Disconnect 24 V.
- Disconnect NUCLEO and USB.
- Disconnect the motor.
- Wait for bus and local rails to discharge.
- Confirm the DMM is in resistance/continuity mode.
- Measure the shorted probe-lead resistance first.

## Measurement

| Item | Reading |
| --- | --- |
| Probe leads shorted | 0.1 ohm (user measurement, 2026-06-09) |
| DT/MODE to GND_SIGNAL | 93 Mohm initial reading (user measurement, 2026-06-09); not accepted, measurement point/reference must be rechecked |
| GND_POWER to presumed GND_SIGNAL point | 53 kohm initial reading (user measurement, 2026-06-09); not accepted because the indicated point was ambiguous |
| R_GND_ISO component end-to-end | Approximately 0.1 ohm (user confirmation, 2026-06-09); 0-ohm ground link confirmed |
| Direct Pin 2 reverse-probe check | Not performed; coarse probes cannot contact the QFN pin safely |

## Design evidence

- The archived schematic directly shows `U1 Pin 2 / DT/MODE` wired to
  `GND_POWER`.
- The user measured `R_GND_ISO` end-to-end at approximately 0.1 ohm,
  confirming the populated 0-ohm link between `GND_POWER` and `GND_SIGNAL`.
- Cropped evidence:
  `photos/2026-06-09_stdrive101_dt_mode_pin2_gnd_power_schematic.png`.

## Decision

- Design decision: `DT/MODE` is tied to ground, selecting STDRIVE101
  six-input mode. STM32 therefore owns complementary timing and deadtime.
- The initial 93 Mohm and 53 kohm readings are invalid contact/reference
  attempts and are retained only as raw history.
- Do not repeat the direct QFN-pin measurement with coarse probes.

This closes the DT/MODE design-evidence prerequisite only. No power-board
dynamic test, CN8 installation, 24 V action, or motor action is approved by
this sheet alone.
