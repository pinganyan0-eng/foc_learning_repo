# PCB2 Mapping, Pin-1, And STDRIVE101 Protection Note - 2026-05-19

Source: user-provided hardware teammate answer in the 2026-05-19 Codex thread.

User statement: the answer corresponds to the current PCB2.

This note archives the text evidence alongside the copied image files:

- `pcb2_cn3_control_connector_pin1_layout_2026-05-19.png`
- `pcb2_blue_connector_pin1_3d_2026-05-19.png`
- `pcb2_hall_mapping_clarification_2026-05-19.jpg`

## CN8 / NUCLEO / STM32 Mapping As Provided

| CN8 | Function | NUCLEO position | STM32 pin |
| --- | --- | --- | --- |
| P1 | `HIN1` | `CN10-D11` | `PA15` |
| P2 | `LIN1` | `CN10-D12` | `PB3` |
| P3 | `HIN2` | `CN10-D13` | `PB10` |
| P4 | `LIN2` | `CN10-D7` | `PA8` |
| P5 | `HIN3` | `CN10-D9` | `PA9` |
| P6 | `LIN3` | `CN10-D10` | `PA10` |
| P7 | `ADC_U` | `CN4-A2` | `PA4` |
| P8 | `ADC_V` | `CN4-A3` | `PB0` |
| P9 | `ADC_W` | `CN4-A4` | `PA5` |
| P10 | `IA` | `CN4-A0` | `PA0` |
| P11 | `IB` | `CN4-A1` | `PA1` |
| P12 | `IC` | `CN5-D5` | `PB4` |
| P13 | `nFAULT` | `CN10-D14` | `PB12` |
| P14 | `3V3` | `CN4-3V3` | not applicable |
| P15 | `GND` | `CN4-GND` | not applicable |
| `J_HALL P2` | `HALL_A` | `CN5-D9` | `PC7` |
| `J_HALL P3` | `HALL_B` | `CN10-D12` | `PB3` |
| `J_HALL P4` | `HALL_C` | `CN10-D13` | `PB10` |

## Pin-1 Evidence As Provided

The user supplied:

- a red PCB layout screenshot for the 15-pin control connector numbering;
- a blue PCB 3D screenshot, described by the user as the `CN8` pin-1 image.

These are layout / 3D source clues for connector orientation. They are not a
powered wiring check and not a continuity record.

## Hall Relationship As Provided

| Hall | Motor phase | Current-sense label | MOSFET half bridge |
| --- | --- | --- | --- |
| `HALL_A` | U phase | `IA` | `Q1 + Q2` |
| `HALL_B` | V phase | `IB` | `Q3 + Q4` |
| `HALL_C` | W phase | `IC` | `Q5 + Q6` |

## PB3 / SWO As Provided

Hardware teammate answer:

- release SWO in STM32CubeMX by selecting `SYS -> Debug -> Serial Wire`
  without SWO;
- then `PB3` can be used for `HALL_B`;
- if SWO is not released, `PC7` was suggested as an alternate, but it conflicts
  with the provided `HALL_A` row.

## Clarification From Later Image

The later clarification image answers the earlier ambiguity:

- `PC7/PB3/PB10` were a suggested alternate Hall input scheme, not the current
  PCB2 physical connection.
- Current PCB2 actual Hall route goes through `IA/IB/IC` and CN8:
  - `IA(HALL_A filtered) -> CN8-P10 -> PA0`;
  - `IB(HALL_B filtered) -> CN8-P11 -> PA1`;
  - `IC(HALL_C filtered) -> CN8-P12 -> PB4`.
- `PB3` is assigned to `LIN1`, not `HALL_B`.
- `PB10` is assigned to `HIN2`, not `HALL_C`.
- `IA/IB/IC` are Hall signal nets after pull-up / filtering from `J_HALL`.
- `ADC_U/ADC_V/ADC_W` are current-sense nets.
- The suggested no-PCB-change software path is software Hall handling using
  `PA0/PA1/PB4`, rather than hardware Hall mode requiring three channels on
  one timer.

## STDRIVE101 Protection Chain As Provided

| Pin or function | Connection | Component |
| --- | --- | --- |
| `DT/MODE` | GND | short / fixed connection |
| `CP` | 100 nF to GND | `C1` |
| `SCREF` | 33 k to 3.3 V plus 20 k to GND, divider midpoint to `SCREF` | `R1`, `R2` |
| `nFAULT` | 10 k pull-up to 3.3 V | `R3` |
| `STBY` | no separate STBY pin; use all `INLx` low or `MOE=0` | not applicable |

## Review Notes To Preserve

- The original provided table improved the current PCB2 endpoint picture but
  appeared to list `PB3` for both `LIN1` and `HALL_B`, and `PB10` for both
  `HIN2` and `HALL_C`.
- The later clarification resolves that apparent conflict: `PC7/PB3/PB10` was
  an alternate suggestion, not current PCB2 physical routing.
- Current PCB2 physical Hall routing is `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`.
- Therefore this source can be reviewed as a current PCB2 mapping clue, but it
  does not by itself authorize Packet A selected fields, Hall readiness, PWM,
  build, flash, power, or motor action.
