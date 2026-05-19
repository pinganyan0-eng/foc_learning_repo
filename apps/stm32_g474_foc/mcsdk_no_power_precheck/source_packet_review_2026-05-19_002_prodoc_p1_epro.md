# ProDoc P1 EDA Pro Source Review - 2026-05-19

This is a no-power Packet B/C review of the self-developed STDRIVE101 driver
board source file `ProDoc_P1_2026-05-19.epro`.

The file is useful as current schematic-source evidence. It is not PCB layout
evidence, not a NUCLEO `CN8` endpoint proof, not generated firmware, not a
continuity check, and not hardware validation.

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
| Review ID | `P2-SOURCE-REVIEW-2026-05-19-002` |
| Reviewer | Codex |
| Packet type | Packet B / Packet C schematic-source candidate |
| Source path | `hardware/schematic/2026-05-19_prodoc_p1_stdrive101_epro/ProDoc_P1_2026-05-19.epro` |
| Source date/version | EDA sheet metadata records create/update date `2026-05-19` and create/update time `10:26:36` |
| Source hash | SHA256 `B9D67B9E5D6DD08D5229928636DFA8048C081DED7EE230ADDB79F20D83D718A1` |
| Source owner | User-provided current self-developed STDRIVE101 driver-board source file |
| Current board match statement | User confirmed on 2026-05-19 that this `.epro` is the driver-board source file. |
| Intake checklist used | `source_packet_intake_checklist_2026-05-14.md` |
| User action queue used | `user_action_queue_2026-05-14.md` |
| Initial decision | `Partial clue / accepted schematic-source clue` |

## Source Inventory

The `.epro` file is a ZIP-style EDA Pro project archive. It contains:

- `project.json`
- `SHEET/eef83bc8254d7e7e/1.esch`
- symbol, footprint, font, blob, panel, pour, and instance folders
- `PCB/` only as an empty directory entry

Important parsed metadata:

| Field | Observed value |
| --- | --- |
| Project name in title block | `STDRIVE101_3Phase_Inverter` |
| Board name | `Schematic1` |
| Page name | `P1` |
| Sheet path | `SHEET/eef83bc8254d7e7e/1.esch` |
| Schematic sheets | one sheet, `P1` |
| Board mapping | `Schematic1` maps to schematic `eef83bc8254d7e7e` |
| PCB mapping | board entry has `"pcb": ""`; `pcbs` is `{}` |
| Parsed records | 117 components, 119 net labels, 43 unique net names |

Decision from inventory: this source can upgrade current schematic-source
visibility, but it cannot prove PCB routing because no PCB layout data is
present in the archive.

## Packet B - Board Interface Review

| Required field | Evidence observed | Decision |
| --- | --- | --- |
| Current-version EDA, schematic PDF, netlist, or high-resolution crop | Current EDA Pro `.epro` source file archived in the repo. User confirmed it is the driver-board source file. | `Partial clue / accepted schematic-source clue`. |
| Source date/version is readable or recorded | Sheet metadata records `2026-05-19 10:26:36`; source hash recorded. | `Accepted` for source date/hash. |
| Current physical board match is stated | User confirmed source relationship on 2026-05-19. | `Accepted` as user board-match statement; physical PCB inspection is still separate. |
| CN8 `NFAULT` mapping is visible | The source does not use literal `CN8`. Board-side 15-pin connector is `CN3`; `CN3` pin 13 is `NFAULT`. | `Partial clue`; NUCLEO `CN8` endpoint remains `Blocked`. |
| CN8 PWM input nets are visible | `CN3` pinout shows `HIN1`, `LIN1`, `HIN2`, `LIN2`, `HIN3`, `LIN3`. | `Partial clue` for board-side control connector only. |
| CN8 current-sense nets are visible | `CN3` pinout shows `ADC_U`, `ADC_V`, `ADC_W`. Three `20mOhm` shunt resistors are present as `R12`, `R14`, and `R17`. | `Partial clue`; STM32 ADC/OPAMP endpoints remain `Blocked`. |
| CN8 Hall nets are visible | `J_HALL` exists. Its visible signal path uses `R22/R23/R24=100 ohm` into nets `IA`, `IB`, and `IC`; `+5V` and `GND_SIGNAL` are visible. | `Partial clue`; `J_HALL` numbering and STM32 Hall assignment remain `Blocked`. |
| CN8 `3V3` and ground nets are visible | `CN3` pin 14 is `3V3`; pin 15 is `GND_SIGNAL`. | `Partial clue` for board-side connector only. |
| STM32 endpoints or connector endpoints are visible | Board-side `CN3` connector endpoints are visible. NUCLEO `CN8` and STM32 MCU pin endpoints are not in this source. | `Blocked` for NUCLEO/STM32 endpoint proof. |
| STDRIVE101 endpoints are visible | `U1=STDRIVE101` with `NFAULT`, `IN1/IN2/IN3`, `EN1/EN2/EN3`, `BOOTx`, `GHSx`, `GLSx`, and `OUTx` nets visible. | `Partial clue`. |
| Net names, pin names, reference designators, and values are readable | EDA JSON records expose component designators, manufacturer parts, values, and net labels. | `Accepted` for schematic readability. |

Board-side `CN3` pinout observed from the source:

| CN3 pin | Schematic net |
| --- | --- |
| 1 | `HIN1` |
| 2 | `LIN1` |
| 3 | `HIN2` |
| 4 | `LIN2` |
| 5 | `HIN3` |
| 6 | `LIN3` |
| 7 | `ADC_U` |
| 8 | `ADC_V` |
| 9 | `ADC_W` |
| 10 | `IA` |
| 11 | `IB` |
| 12 | `IC` |
| 13 | `NFAULT` |
| 14 | `3V3` |
| 15 | `GND_SIGNAL` |

Packet B conclusion: the `.epro` upgrades the project from screenshot-only
power-board clues to a current schematic-source clue for the self-made driver
board. It still does not prove NUCLEO `CN8`, STM32 pin mapping, connector
cabling, continuity, or PCB routing.

## Packet C - STDRIVE101 Protection Path Review

| Protection item | Evidence observed | Decision |
| --- | --- | --- |
| `DT/MODE` endpoint and resistor/strap value or ground state | STDRIVE101 symbol pin 2 is `DT/MODE`; in this sheet the corresponding wire at the component pin is net-labeled `GND_POWER`. | `Partial clue`; needs human schematic review before treating the PWM mode as accepted. |
| `nFAULT` route, pull-up voltage, loading, active-low handling, CN8/STM32 endpoint | `NFAULT` appears at STDRIVE101, `R3=10k`, `LED1`, and `CN3` pin 13. Pull-up rail is visible as `3V3` in the nearby network. | `Partial clue`; STM32 break input and NUCLEO endpoint remain `Blocked`. |
| `REG12` capacitor values, loads, and return path | `REG12`, `C4=4.7uF`, `C5=100nF`, and bootstrap diode links are visible. | `Partial clue`. |
| `CP` comparator network, filter components, and threshold inputs | STDRIVE101 symbol has pin 1 named `CP`; no explicit `CP` net label was observed in parsed unique net names. | `Blocked` for named route proof. |
| `SCREF` divider/bias values and VDS monitoring decision | `SCREF` is visible with `R1=33kOhm` and `R2=20kOhm` divider clue. | `Partial clue`; threshold review still pending. |
| `VS/VM` relation to MOSFET bus and `24V_FUSED` | `24V` and `24V_FUSED` nets are visible; STDRIVE101 supply-side path is visible at schematic level. | `Partial clue`; no powered or PCB proof. |
| Bootstrap capacitors and diode/component orientation for U/V/W | `BOOT1/2/3`, `OUT1/2/3`, `D1/D2/D3=SS34`, and `C11/C12/C13=1uF` are visible. | `Partial clue`. |
| `STBY` pull state, MCU route if any, and wake path | No `STBY` net or token was observed in parsed nets/source text. | `Blocked`. |
| VDS monitoring threshold path and fault-release path | `SCREF`, `OUTx`, `GHSx`, and `GLSx` clues exist, but VDS threshold and fault-release behavior are not fully proven. | `Blocked`. |

Packet C conclusion: the `.epro` improves board-level STDRIVE101 schematic
visibility, especially for `NFAULT`, `REG12`, `SCREF`, bootstrap, and output
networks. It does not fully prove the protection path, because `CP`, `STBY`,
threshold math, STM32 endpoint handling, PCB layout, and physical validation
remain unresolved.

## Key Components Observed

| Designator | Observed part/value | Evidence meaning |
| --- | --- | --- |
| `U1` | `STDRIVE101` | Confirms self-made driver board is STDRIVE101-based at schematic level. |
| `Q1`-`Q6` | `NCEP40T11G` | Three-phase MOSFET bridge clue. |
| `R12`, `R14`, `R17` | `20mOhm` shunt resistors | Three-shunt sensing clue. |
| `CN3` | `2.54mm-15P ZZ` | Board-side control connector; not literal NUCLEO `CN8`. |
| `U2` | `J_HALL`, `MX2.54-LS-5P` | Hall connector clue only. |
| `CN2` | `J_MOTOR`, `MX128-5.08-3P` | Motor phase connector clue only. |

## Decision

Decision: `Partial clue / accepted schematic-source clue`.

Accepted exact evidence:

- The repo now contains a current user-confirmed EDA Pro schematic source file
  for the self-developed STDRIVE101 driver board.
- The source has readable date/time metadata, source hash, component records,
  and net labels.
- Board-side `CN3` control connector pinout is visible.
- STDRIVE101 device, MOSFET bridge, 3-shunt sensing clue, Hall connector, motor
  connector, `NFAULT`, `REG12`, `SCREF`, bootstrap, and output networks are
  visible at schematic level.

Blocked fields that remain unchanged:

- No PCB layout or Gerber data is present in the `.epro`.
- NUCLEO `CN8` and STM32 endpoint mapping are not proven.
- Physical connector/cable continuity is not proven.
- `PB3` / SWO release and Hall B readiness are not proven.
- `J_HALL` numbering is not accepted as project wiring proof.
- Packet A Workbench / MCSDK selected fields remain `Partial clue / stopped`.
- Generated-project trust remains `Not allowed`.
- Power-stage readiness, Motor Profiler readiness, Hall closed-loop readiness,
  motor readiness, and sensorless readiness remain not allowed.

## Files Updated By This Review

- `hardware/schematic/2026-05-19_prodoc_p1_stdrive101_epro/ProDoc_P1_2026-05-19.epro`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_002_prodoc_p1_epro.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `workflow/evidence_register.md`
- `CURRENT_STATUS.md`

## Required Follow-Up

Before this can become accepted route/protection proof, the project still needs:

1. PCB layout, Gerber, or routed-board export for this same board revision.
2. NUCLEO `CN8` or harness mapping from `CN3` to STM32 pins.
3. Dedicated review of `DT/MODE`, `CP`, `STBY`, `SCREF` threshold, and
   `NFAULT` break-input handling.
4. Later no-power continuity/short checks before any powered phase.

## Review Record Stub

```text
Review ID: P2-SOURCE-REVIEW-2026-05-19-002
Packet type: Packet B / Packet C schematic-source clue
Source path: hardware/schematic/2026-05-19_prodoc_p1_stdrive101_epro/ProDoc_P1_2026-05-19.epro
Decision: Partial clue / accepted schematic-source clue
Accepted fields: current EDA Pro schematic source, source date/hash,
board-side CN3 pinout, visible STDRIVE101/MOSFET/shunt/Hall/motor connector
schematic clues, visible NFAULT/REG12/SCREF/bootstrap/output networks
Rejected or blocked fields: PCB routing, NUCLEO CN8 endpoint, STM32 pin
mapping, PB3 release, J_HALL numbering, Packet A selected fields,
generated-project trust, powered readiness
Evidence packet updates: Packet B/C now record current schematic-source clues
without upgrading CN8 routing proof or STDRIVE101 protection-path proof
Evidence register updates: EV-2026-05-19-P2-PRODOC-EPRO-SCHEMATIC-001
Tests: `python -m unittest discover -s tests` passed, 41 tests OK
Vector store: `python tools\build_vector_store.py` completed, 8072 chunks built
Safety statement: no 24V, no power-board connection, no motor connection,
no Gate PWM output, no Motor Profiler run, no Hall closed-loop claim,
no sensorless / SMO claim.
```
