# 2026-06-01 Hall/control connector no-power DMM check

## Context

- Source: user-provided DMM readings in chat on 2026-06-01.
- Board state: no-power DMM continuity and short checks only.
- Scope: Hall input nets, one LIN control net, nFAULT net, and selected connector power pins.
- Safety boundary: this record does not authorize 24 V power-up, PWM output, or motor connection.

## Continuity Check

| Item | DMM reading | Beep | Status | Note |
| --- | --- | --- | --- | --- |
| IA -> PA0 | ~0 ohm | Yes | Pass | IA/HALL_A network directly connected. |
| IB -> PA1 | ~0 ohm | Yes | Pass | IB/HALL_B network directly connected. |
| IC -> PB4 | ~0 ohm | Yes | Pass | IC/HALL_C network directly connected. |
| PB3 -> LIN1 | ~10 ohm | Yes | Pass | Series R8 is expected to read about 10 ohm. |
| P14 -> 3V3 | ~0 ohm | Yes | Pass | Pin 14 directly connected to 3V3 network. |
| P15 -> GND_SIGNAL | 0.2 ohm | Yes | Pass | Follow-up reading against GND_SIGNAL shows a clean low-ohm path. Earlier OL reading was likely wrong reference point or probe contact. |
| nFAULT -> PB12 | ~0 ohm | Yes | Pass | nFAULT network directly connected to CN3 Pin 13. |

## Short Check

| Item | DMM reading | Beep | Status | Note |
| --- | --- | --- | --- | --- |
| 3V3 -> GND | OL | No | Pass | No short found on 3V3 to GND. |
| 24V -> GND | OL | No | Pass | Follow-up reading: no input-bus short found. |
| 5V -> GND | OL | No | Pass | Follow-up reading: no 5V rail short found. |
| REG12 -> GND | OL | No | Pass | Follow-up reading: no REG12 rail short found. |
| BOOT1 -> OUT1 | OL | No | Pass | Follow-up reading: no obvious BOOT1 bootstrap short found. |
| BOOT2 -> OUT2 | OL | No | Pass | Follow-up reading: no obvious BOOT2 bootstrap short found. |
| BOOT3 -> OUT3 | OL | No | Pass | Follow-up reading: no obvious BOOT3 bootstrap short found. |
| SCREF -> 3V3 | OL | No | N/A | Later determined not to be a safe/valid direct probe of the hidden R1/R2 midpoint; do not use this as a SCREF failure. |
| SCREF -> GND | OL | No | N/A | Later determined not to be a safe/valid direct probe of the hidden R1/R2 midpoint; do not use this as a SCREF failure. |
| R1 body | 33.3 kohm | No | Pass | Matches expected SCREF upper resistor value, nominal 33 kohm. |
| R2 body | 19.8 kohm | No | Pass | Matches expected SCREF lower resistor value, nominal 20 kohm. |
| R_GND_ISO body | 0 ohm | No | Pass | Matches expected 0 ohm ground-isolation link; no beep is acceptable if meter threshold/contact behavior differs. |
| GHS1/GH1 -> GND | OL | No | Pass | No obvious high-side gate-drive short to GND. |
| GHS2/GH2 -> GND | OL | No | Pass | No obvious high-side gate-drive short to GND. |
| GHS3/GH3 -> GND | OL | No | Pass | No obvious high-side gate-drive short to GND. |
| GLS1/GL1 -> GND | OL | No | Pass | No obvious low-side gate-drive short to GND. |
| GLS2/GL2 -> GND | OL | No | Pass | No obvious low-side gate-drive short to GND. |
| GLS3/GL3 -> GND | OL | No | Pass | No obvious low-side gate-drive short to GND. |
| GHS1 -> Q1 Gate | ~22 ohm | Yes | Pass | Matches expected gate series resistor path. |
| GHS2 -> Q3 Gate | ~22 ohm | Yes | Pass | Matches expected gate series resistor path. |
| GHS3 -> Q5 Gate | ~22 ohm | Yes | Pass | Matches expected gate series resistor path. |
| GLS1 -> Q2 Gate | ~22 ohm | Yes | Pass | Matches expected gate series resistor path. |
| GLS2 -> Q4 Gate | ~22 ohm | Yes | Pass | Matches expected gate series resistor path. |
| GLS3 -> Q6 Gate | ~22 ohm | Yes | Pass | Matches expected gate series resistor path. |
| OUT1/U -> GND | OL | No | Pass | No obvious phase-to-ground short found. |
| OUT2/V -> GND | OL | No | Pass | No obvious phase-to-ground short found. |
| OUT3/W -> GND | OL | No | Pass | No obvious phase-to-ground short found. |
| OUT1/U -> 24V | OL | No | Pass | No obvious phase-to-bus short found. |
| OUT2/V -> 24V | OL | No | Pass | No obvious phase-to-bus short found. |
| OUT3/W -> 24V | OL | No | Pass | No obvious phase-to-bus short found. |
| OUT1/U -> OUT2/V | OL | No | Pass | No obvious inter-phase short found. |
| OUT1/U -> OUT3/W | OL | No | Pass | No obvious inter-phase short found. |
| OUT2/V -> OUT3/W | OL | No | Pass | No obvious inter-phase short found. |
| PA0/IA -> 3V3 | ~4.7 kohm | No | Pass | R19 pull-up present; not a short. |
| PA0/IA -> GND | OL | No | Pass | No short to GND. |
| PA1/IB -> 3V3 | ~4.7 kohm | No | Pass | R20 pull-up present; not a short. |
| PA1/IB -> GND | OL | No | Pass | No short to GND. |
| PB4/IC -> 3V3 | ~4.7 kohm | No | Pass | R21 pull-up present; not a short. |
| PB4/IC -> GND | OL | No | Pass | No short to GND. |
| PB3/LIN1 -> 3V3 | OL | No | Pass | No external LIN1 pull-up observed. |
| PB3/LIN1 -> GND | OL | No | Pass | No short to GND. |
| PB12/nFAULT -> 3V3 | ~10 kohm | No | Pass | R3 pull-up present; not a short. |
| PB12/nFAULT -> GND | OL | No | Pass | No short to GND. |
| IA -> IB | OL | No | Pass | Hall inputs are isolated from each other. |
| IA -> IC | OL | No | Pass | Hall inputs are isolated from each other. |
| IB -> IC | OL | No | Pass | Hall inputs are isolated from each other. |

## Assessment

This is useful partial no-power evidence:

- Hall input nets IA/IB/IC map to PA0/PA1/PB4 and show expected 4.7 kohm pull-ups to 3V3.
- nFAULT maps to PB12 and shows the expected 10 kohm pull-up to 3V3.
- PB3/LIN1 includes the expected ~10 ohm series path.
- No short was reported among Hall input lines or from these logic nets to GND.
- Follow-up readings show no beep and OL on 24V-GND, 5V-GND, REG12-GND, and BOOTx-OUTx.
- Follow-up readings show no beep and OL on OUTx-to-GND, OUTx-to-24V, and inter-phase OUTx checks.
- R1/R2 body measurements match the expected SCREF divider resistor values: 33.3 kohm and 19.8 kohm.
- R_GND_ISO and CN8 Pin 15 to GND_SIGNAL continuity are confirmed.
- Gate-drive outputs are not shorted to GND, and all six gate series resistor paths read approximately 22 ohm.

The check is not yet a complete self-board first-power gate because one formal signoff evidence gap remains:

- SCREF physical-net evidence is schematic-level, not direct DMM continuity: earlier SCREF-to-3V3 and SCREF-to-GND readings were OL because the R1/R2 midpoint is not safely probeable, but R1/R2 body values are correct and the existing schematic/BOM records state R1 -> SCREF Pin 3 -> R2.

## Required Recheck

Do not force a probe onto STDRIVE101 Pin 3 or hidden/internal copper. Current project records already provide schematic-level SCREF evidence:

- `hardware/schematic/2026-05-09_power_board_schematic_screenshot.md` records `SCREF` divider as R1 33K to 3V3 and R2 20K to GND_SIGNAL.
- `hardware/bom/2026-05-09_user_provided_power_stage_parts.md` records R1 as `3.3V -> SCREF Pin3` and R2 as `SCREF Pin3 -> GND_SIGNAL`.
- Original EDA/netlist/PCB-source evidence would be stronger and is still useful for formal hardware signoff, but it is not a DMM action item.

## Current Gate Decision

- Hall/control connector, basic rail/bootstrap, and phase-output short checks: partial pass.
- Remaining limitation: SCREF has schematic/BOM-level evidence and correct R1/R2 body values, but no original EDA/netlist/PCB-source file is imported yet.
- Self-board first 24 V power-up gate: not passed.
- Motor connection gate: not passed.
