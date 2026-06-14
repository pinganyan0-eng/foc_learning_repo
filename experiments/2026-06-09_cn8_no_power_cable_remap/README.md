# 2026-06-09 CN3 15-pin control cable no-power remap

Task ID: `TASK-2026-06-09-L3-cn8-no-power-cable-remap`

## Purpose

Rearrange and verify the loose 15-pin control-interface cable before either
end is installed. Earlier notes and schematic exports may call this interface
`CN8`, but the populated PCB silkscreen/photo evidence identifies the long
15-pin control connector as `CN3`. In this record, `CN3 Pn` means the physical
PCB connector pin; old `CN8 Pn` names are preserved only as schematic/history
aliases.

The separate 6-pin connector near the board edge is not this PWM control
interface and must not be used for the TIM1 loose-wire map.

## Safety boundary

- NUCLEO USB disconnected.
- Power-board 24 V disconnected and discharged.
- Motor and phase wires disconnected.
- Cable disconnected from both boards during continuity checks.
- No firmware change, flash, PWM output, Gate measurement, or powered test.
- CN3/CN8-alias P7-P12 and P14 remain unpopulated.

## Required records

- Completed `2026-06-09_cn8_cable_continuity_record.md`.
- One overview photo showing the complete loose cable.
- One CN3 15-pin end close-up showing pin 1 and the P1-P15 orientation.
- One NUCLEO-end close-up showing all eight Morpho/GND endpoints.

## Current status

`DONE FOR NO-POWER CABLE INSTALLATION`: the eight intended wires passed
continuity at approximately the probe-tip baseline, pairwise isolation passed,
P7-P12 and P14/3V3 remain open, CN3 orientation photos were reviewed, and the
post-installation targeted sanity checks passed with no beep on P14-P15,
P1-P2, P3-P4, P5-P6, and P13-P15.

This record closes only the no-power cable mapping/installation task. It does
not authorize NUCLEO USB, 24 V, PWM, Gate probing, OUTx/BOOTx/high-side Vgs
measurement, or motor connection.
