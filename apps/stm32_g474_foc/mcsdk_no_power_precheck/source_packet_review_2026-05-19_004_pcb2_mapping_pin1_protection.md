# PCB2 Mapping, Pin-1, And Protection Review - 2026-05-19

This is a no-power review of the user-provided current PCB2 mapping,
connector-orientation, Hall relationship, PB3/SWO, and STDRIVE101 protection
answer.

It is not a wiring instruction, not generated firmware, not a continuity check,
and not hardware validation.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
- No source generation, build, flash, or generated motor-control project.

## Review Header

| Field | Value |
| --- | --- |
| Review ID | `P2-SOURCE-REVIEW-2026-05-19-004` |
| Reviewer | Codex |
| Packet type | Packet B/C plus PB3/SWO and Hall mapping clue |
| Source path | `hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/` |
| Source date/version | 2026-05-19 user-provided hardware teammate answer plus later clarification image; user states it corresponds to current PCB2 |
| Source owner | User / hardware teammate relay |
| Current board match statement | Accepted as a current PCB2 statement from the user for no-power review, not as continuity or powered validation |
| Intake checklist used | `source_packet_intake_checklist_2026-05-14.md` |
| User action queue used | `user_action_queue_2026-05-14.md` |
| Initial decision | `Partial clue / accepted current PCB2 mapping source; apparent Hall/PWM conflicts clarified as alternate suggestion` |

## Archived Files

| File | SHA256 |
| --- | --- |
| `hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/pcb2_mapping_pin1_protection_note_2026-05-19.md` | text source, not hashed separately |
| `hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/pcb2_cn3_control_connector_pin1_layout_2026-05-19.png` | `DF97CA441B117CAFF97B651C5D58A28FADB8150E193B8CD468A706DA7F642343` |
| `hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/pcb2_blue_connector_pin1_3d_2026-05-19.png` | `93A6186ED213239CB526D0E36E9C7AF0C2505C3BB06302336321643613A3883F` |
| `hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/pcb2_hall_mapping_clarification_2026-05-19.jpg` | `470CF84061E543D72D5D32AD13A4BC7648918931916D89E30FC832C2BA7A0BCE` |

## Evidence Observed

| Required field | Evidence observed | Decision |
| --- | --- | --- |
| Current PCB2 exact-version statement | User states this answer corresponds to current PCB2. | `Accepted as source-owner statement`; not continuity or powered evidence. |
| `CN3/CN8 -> NUCLEO -> STM32` mapping | Table provides P1-P15 mapping for `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3/ADC_U/ADC_V/ADC_W/IA/IB/IC/nFAULT/3V3/GND`. Later clarification states apparent `PC7/PB3/PB10` Hall rows were alternate suggestions, not current PCB2 physical routing. | `Partial clue / clarified`; endpoint picture improved, but final Workbench/CubeMX selected fields remain missing. |
| Connector pin-1 evidence | Red PCB layout image shows numbered 15-pin connector pads; blue PCB 3D image was supplied as pin-1 evidence. | `Partial clue`; useful layout/orientation source, not harness continuity. |
| Hall A/B/C relationship | Source states current PCB2 Hall route is `HALL_A -> IA -> PA0`, `HALL_B -> IB -> PA1`, `HALL_C -> IC -> PB4`; `IA/IB/IC` are Hall signal nets after pull-up/filtering. | `Partial clue / clarified`; physical endpoint clue accepted, but final software Hall strategy remains a Packet A/CubeMX/Workbench question. |
| PB3/SWO handling | Clarification states `PB3` is for `LIN1`, not `HALL_B`; `PB10` is for `HIN2`, not `HALL_C`; `PC7/PB3/PB10` was an alternate suggestion. | `Clarified for PCB2 routing`; SWO release is no longer a Hall B requirement for the current PCB2 physical route, but Packet A selected fields remain missing. |
| STDRIVE101 protection chain | Source states `DT/MODE -> GND`, `CP -> 100 nF -> GND`, `SCREF` divider `33 k / 20 k`, `nFAULT` 10 k pull-up to 3.3 V, and no separate `STBY` pin. | `Partial clue / accepted board-intent statement`; threshold math, endpoint handling, continuity, and powered fault behavior remain blocked. |

## Mapping Table As Reviewed

| Connector row | Function | NUCLEO position | STM32 pin | Review note |
| --- | --- | --- | --- | --- |
| P1 | `HIN1` | `CN10-D11` | `PA15` | Needs Packet A timer/pin-function proof. |
| P2 | `LIN1` | `CN10-D12` | `PB3` | Clarification says `PB3` is `LIN1`, not `HALL_B`; still needs Packet A timer/pin-function proof. |
| P3 | `HIN2` | `CN10-D13` | `PB10` | Clarification says `PB10` is `HIN2`, not `HALL_C`; still needs Packet A timer/pin-function proof. |
| P4 | `LIN2` | `CN10-D7` | `PA8` | Needs Packet A timer/pin-function proof. |
| P5 | `HIN3` | `CN10-D9` | `PA9` | Needs Packet A timer/pin-function proof. |
| P6 | `LIN3` | `CN10-D10` | `PA10` | Needs Packet A timer/pin-function proof. |
| P7 | `ADC_U` | `CN4-A2` | `PA4` | Current-sense endpoint clue. |
| P8 | `ADC_V` | `CN4-A3` | `PB0` | Current-sense endpoint clue. |
| P9 | `ADC_W` | `CN4-A4` | `PA5` | Current-sense endpoint clue. |
| P10 | `IA` | `CN4-A0` | `PA0` | Clarified as filtered `HALL_A` signal net. |
| P11 | `IB` | `CN4-A1` | `PA1` | Clarified as filtered `HALL_B` signal net. |
| P12 | `IC` | `CN5-D5` | `PB4` | Clarified as filtered `HALL_C` signal net. |
| P13 | `nFAULT` | `CN10-D14` | `PB12` | Supports `PB12/TIM1_BKIN` candidate, but Workbench/CubeMX proof remains needed. |
| P14 | `3V3` | `CN4-3V3` | not applicable | Power rail mapping clue only; no powered validation. |
| P15 | `GND` | `CN4-GND` | not applicable | Return-path mapping clue only; no continuity record. |
| Alternate suggestion | `HALL_A/HALL_B/HALL_C` | Morpho / alternate route | `PC7/PB3/PB10` | Later clarification says this was suggested alternate routing, not current PCB2 physical connection. |

## Accepted Updates

- Exact PCB2 match is no longer the main Gerber blocker because the user states
  the answer corresponds to current PCB2.
- The repo now has a current PCB2 endpoint mapping source for P1-P15 and a
  clarified Hall route: `IA/IB/IC -> PA0/PA1/PB4`.
- The repo now has archived connector-orientation images.
- The repo now has a current PCB2 protection-chain statement for `DT/MODE`,
  `CP`, `SCREF`, `nFAULT`, and `STBY` absence.

## Clarified Fields

- `PB3` is `LIN1`, not current PCB2 `HALL_B`.
- `PB10` is `HIN2`, not current PCB2 `HALL_C`.
- `IA/IB/IC` are Hall signal nets from `J_HALL` after pull-up/filtering.
- `ADC_U/ADC_V/ADC_W` are current-sense nets.
- `PC7/PB3/PB10` is an alternate suggestion, not current PCB2 physical routing.

## Still Blocked Fields

- The current PCB2 Hall route `PA0/PA1/PB4` does not form a normal three-channel
  hardware Hall timer set. The suggested no-PCB-change path is software Hall
  handling, which still needs Packet A/CubeMX/Workbench and firmware design
  review before use.
- SWO release is no longer required for the current PCB2 Hall path, but `PB3`
  as `LIN1` still needs final Packet A timer/pin-function proof.
- Packet A selected fields are still missing. Timer alternate-function
  compatibility and MCSDK Workbench selected pins are not accepted.
- No no-power DMM continuity / short-check table exists.
- No powered STDRIVE101 protection behavior, `nFAULT` event, Gate waveform,
  Motor Profiler, Hall closed-loop, motor, or sensorless evidence exists.

## Decision

Decision: `Partial clue / accepted current PCB2 mapping source; Hall/PWM conflicts clarified`.

This packet upgrades the project from "no current PCB2 mapping answer" to "a
current PCB2 mapping source exists and has been archived, with the apparent
`PB3` / `PB10` Hall conflicts clarified as alternate suggestions." It does not
unlock generated-project trust, build-only work, flashing, powered work, motor
work, Hall readiness, power-stage readiness, or sensorless readiness.

## Required Follow-Up

1. Capture or create the final no-power CubeMX/Workbench configuration showing
   selected PWM pins, break input, Hall pins, SWO state, ADC/current-sense pins,
   and UART choice.
2. Decide and document whether the current PCB2 Hall route will use software
   Hall handling on `PA0/PA1/PB4`, or whether a future hardware rework will
   move Hall to a timer-compatible set.
3. Later, before any powered phase, create a DMM continuity / short-check table
   for the exact connector/harness route.

## Review Record Stub

```text
Review ID: P2-SOURCE-REVIEW-2026-05-19-004
Packet type: Packet B/C plus PB3/SWO and Hall mapping clue
Source path: hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/
Decision: Partial clue / accepted current PCB2 mapping source; Hall/PWM
conflicts clarified
Accepted fields: current PCB2 statement, P1-P15 mapping source, pin-1 images,
STDRIVE101 protection-chain statement
Rejected or blocked fields: Workbench selected fields, software Hall strategy,
generated-project trust, continuity, power, motor
Evidence packet updates: Packet B/C improves from missing endpoint answer to
current mapping source with clarified Hall routing; readiness remains blocked
Evidence register updates: EV-2026-05-19-P2-PCB2-MAPPING-PIN1-PROTECTION-001
Safety statement: no 24V, no power-board connection, no motor connection,
no Gate PWM output, no Motor Profiler run, no Hall closed-loop claim,
no sensorless / SMO claim.
```
