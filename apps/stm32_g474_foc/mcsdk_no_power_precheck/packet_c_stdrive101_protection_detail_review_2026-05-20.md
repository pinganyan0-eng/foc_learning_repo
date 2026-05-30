# Packet C STDRIVE101 Protection Detail Review - 2026-05-20

## Decision

`Packet C detail narrowed / protection proof still partial clue / P3 still blocked`.

Stable phrase: no powered readiness.

This is a no-power Packet C review. It uses the current `.epro`, Gerber,
current PCB2 mapping note, and repo-local STDRIVE101 datasheet extraction to
narrow the protection-path blockers without claiming hardware validation.

## Feature Sentence

The repo now has enough board-side clues to separate `DT/MODE`, `CP`, `SCREF`,
`nFAULT`, `REG12`, bootstrap, `STBY`, and VDS monitoring into reviewable
sub-items, but not enough evidence to accept Packet C or move to P3.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Motor Pilot.
- No Hall closed-loop validation.
- No sensorless / SMO claim.
- No source generation, build, flash, or generated motor-control project.

## Input Evidence

| Source | Current value |
| --- | --- |
| Official device source | `materials/raw/st_manuals/st_stdrive101_datasheet.pdf`, `materials/extracted/st_manuals/st_stdrive101_datasheet.txt`, manifest ID `st_stdrive101_datasheet`, DS13472 Rev 2, June 2022 |
| Earlier protection matrix | `stdrive101_protection_path_review_2026-05-14.md` |
| Schematic source clue | `source_packet_review_2026-05-19_002_prodoc_p1_epro.md` |
| Gerber / flying-probe clue | `source_packet_review_2026-05-19_003_gerber_pcb2.md` |
| Current PCB2 mapping clue | `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md` |
| Threshold note under review | `docs/03_hardware_notes/protection_thresholds.md` |

## Official Facts Rechecked Locally

These facts come from the repo-local STDRIVE101 extracted text and must still
be checked against the PDF page/table before powered work:

| Area | Local official extraction says | Project meaning |
| --- | --- | --- |
| `DT/MODE` | Ground through `RDT` selects ENx/INx with internal deadtime; short to ground selects INHx/INLx with no internal deadtime and interlocking. The pin status must not change during operation. | Current board clue `DT/MODE -> GND` points toward INHx/INLx mode, so Workbench/MCSDK output style must match that before any generated-project trust. |
| `nFAULT` | Open-drain output goes low for UVLO, VDS monitoring, overcurrent, and thermal events. | `PB12/TIM1_BKIN` remains only a candidate until Workbench/CubeMX selected fields and physical endpoint handling are accepted. |
| `REG12` | 12 V regulator / gate-driver supply needs bypass capacitance and load-budget review. | `C4=4.7uF`, `C5=100nF`, and bootstrap diode clues are useful, but no load budget or placement validation exists. |
| `SCREF` / VDS | Local extraction states `VDSth = VSCREF`; VDS monitoring is enabled below `VSCREF,en` and disabled above `VSCREF,dis`. Extracted thresholds include `VSCREF,en = 2.54 V` and `VSCREF,dis = 2.9 V`. | The current `33k / 20k` divider clue gives about `1.245 V`, which is below the extracted enable threshold. Treat VDS monitoring as intended-enabled at source-clue level, not as validated protection. |
| `CP` | Overcurrent comparator trips when `CP` is higher than internal `VREF`; local extraction gives `VREF` typical near `505 mV`. | The current `CP -> 100 nF -> GND` clue is not enough to calculate an OCP threshold. A named route and component interpretation are still missing. |
| `STBY` | The device can enter standby when all driving inputs stay low for `tSTBY`; standby disables several functions and affects wake / `nFAULT` interpretation. | "No separate STBY pin" is plausible as a source clue only. Firmware idle states, MOE behavior, Workbench settings, and wake/fault interpretation remain blocked. |
| VDS release | VDS monitoring faults latch the gate outputs low and release only when the device enters standby. | The future fault-recovery plan must include a standby/release path; do not assume `nFAULT` clears by software readback alone. |

## Board-Side Detail Matrix

| Protection item | Current board clue | Current decision | Still required before Packet C accept |
| --- | --- | --- | --- |
| `DT/MODE` mode | `.epro` and Gerber clues show STDRIVE101 pin 2 / `DT/MODE` on `GND_POWER`; mapping note says `DT/MODE -> GND`. | `Partial clue / likely INHx-INLx mode candidate`. | Human PDF/table check, schematic-source cross-check, Workbench/MCSDK output mode review, and later no-power continuity from `DT/MODE` to ground. |
| `nFAULT` route | `U1_6=NFAULT`, `R3_1=NFAULT`, `R3_2=3V3`, `CN3_13=NFAULT`; mapping note maps P13 to `PB12`. | `Partial clue / board-side pull-up and connector route visible`. | Workbench/CubeMX break input selected fields, active-low handling, interrupt/break policy, CN3-to-NUCLEO continuity, and later powered fault behavior. |
| `REG12` | `U1_5=REG12`; `C4=4.7uF`, `C5=100nF`; `D1/D2/D3` link `REG12` to `BOOTx`. | `Partial clue / bypass and bootstrap charge path visible`. | PDF capacitor guidance check, placement/layout review, load budget, return path, and first-power measurement plan. |
| `CP` | Gerber exposes `U1_1` as `$2N118`; mapping note says `CP -> 100 nF -> GND` using `C1`. | `Partial clue / comparator threshold still blocked`. | Named `CP` net proof, whether there is an `RCP` path, how the comparator sees shunt/current information, and explicit threshold calculation. |
| `SCREF` | `R1=33k` to `3V3`, `R2=20k` to ground, midpoint to `SCREF`. | `Partial clue / VDS monitoring appears intended enabled, threshold claim unresolved`. | PDF table check, divider tolerance calculation, `VS/VM` relationship proof, and a decision on whether VDS monitoring is acceptable for bring-up. |
| Old `55A` VDS claim | `protection_thresholds.md` records `V_SCREF=1.245V`, `V_DSth=0.249V`, and `I_trip ~= 55A` as a user calculation. | `Not accepted`. The current local official extraction supports `VDSth = VSCREF`, so the `0.249V` premise must not be used. | Human PDF recheck and a corrected threshold note. Do not use any Rds(on)-derived value as a current limit. |
| `VS/VM` | `24V` and `24V_FUSED` board clues exist; datasheet extraction says VDS monitoring assumes `VM` and `VS` at the same voltage. | `Partial clue / still blocked for protection correctness`. | Exact `VS`, `VM`, `24V_FUSED`, MOSFET bus, fuse/diode path, and VDS-monitoring false-trip analysis. |
| Bootstrap | `BOOT1/2/3`, `OUT1/2/3`, `C11/C12/C13=1uF`, and `D1/D2/D3` clues exist. | `Partial clue`. | PDF value check, orientation/layout review, and later gate-waveform validation before trust. |
| `STBY` / release | Mapping note says no separate `STBY`; use all `INLx` low or `MOE=0`. | `Partial clue / release path not accepted`. | Firmware idle-state design, Workbench output idle states, break/MOE behavior, and a written fault-release procedure. |

## Current Rule Table

| Rule | Decision |
| --- | --- |
| VDS threshold claim | Do not repeat the old `55A` claim as a project fact. It is now a blocked calculation note. |
| `CP` OCP threshold | Do not calculate until a named `CP` route and comparator input network are proven. A capacitor-to-ground clue is not a threshold. |
| `nFAULT` to `PB12/TIM1_BKIN` | Keep as candidate / partial clue until Packet A selected fields and physical endpoint checks exist. |
| `DT/MODE -> GND` | Treat as source clue for INHx/INLx mode. Do not trust MCSDK/TIM1 output style until Packet A proves the chosen drive strategy. |
| Fault recovery | Any later VDS fault interpretation must include standby release behavior; no automatic software-only clear is assumed. |
| Powered readiness | Packet C detail review does not authorize any powered action. |

## Function Responsibilities

| Function | Responsibility |
| --- | --- |
| Packet C source review | Track board-side protection evidence and keep each item `Partial clue`, `Blocked`, or `Accepted`. |
| Packet A Workbench review | Prove selected PWM, break/fault, current sensing, and speed-sensor fields before generated-project trust. |
| Firmware design review | Later define idle states, `MOE`, break handling, standby/release, and no-blocking ISR behavior. |
| Hardware teammate | Provide final schematic/PCB source, connector continuity, and no-power DMM checks before any P3 action. |
| P3 phase gate | Own current-limited power-up settings, measurement points, stop conditions, and rollback evidence. |

## Next Smallest Actions

1. Update `docs/03_hardware_notes/protection_thresholds.md` so the old `55A`
   VDS claim is explicitly marked not accepted.
2. Keep Packet C in `Partial clue` until a corrected PDF/table-backed
   threshold note and no-power continuity table exist.
3. Continue Packet A through Workbench GUI-created FOC evidence; do not use
   Packet C progress to justify generated-project trust.
4. Before P3, create a no-power continuity / short-check table for `CN3`,
   `DT/MODE`, `NFAULT`, `SCREF`, `CP`, `REG12`, `VS/VM`, bootstrap, `3V3`,
   and `GND_SIGNAL`.

## Result

Packet C is more precise but still not accepted. P2 can keep reviewing source
packets and configuration artifacts. P2 still cannot generate for use, build,
flash, connect 24V, connect the power board, connect the motor, output Gate
PWM, run Motor Profiler, claim Hall closed-loop validation, or claim sensorless
/ SMO validation.
