# Gerber PCB2 Source Review - 2026-05-19

This is a no-power Packet B/C review of `Gerber_PCB2_2026-05-19.zip`, a
Gerber manufacturing package supplied after the self-developed STDRIVE101
driver-board `.epro` schematic-source review.

The package is useful as board-side PCB manufacturing output plus flying-probe
pad/net evidence. It is not a NUCLEO `CN8` endpoint proof, not STM32 firmware
configuration evidence, not a continuity check, and not hardware validation.

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
| Review ID | `P2-SOURCE-REVIEW-2026-05-19-003` |
| Reviewer | Codex |
| Packet type | Packet B / Packet C board-side Gerber and flying-probe net clue |
| Source path | `hardware/schematic/2026-05-19_gerber_pcb2_stdrive101/Gerber_PCB2_2026-05-19.zip` |
| Source date/version | Gerber headers record `EasyEDA Pro v3.2.91`, generated `2026-05-19 11:16:57`; ZIP file timestamp is `2026-05-19 13:22:02` |
| Source hash | SHA256 `F61C073C5A9E71CD608460976430D3F927E7AD48EC05A42661E77662AF04CE56` |
| Source owner | Hardware teammate supplied Gerber package for the self-developed STDRIVE101 driver board |
| Current board match statement | Treated as a same-day board-side follow-up to `ProDoc_P1_2026-05-19.epro`; exact fabrication/revision match should still be confirmed before powered work. |
| Related schematic review | `source_packet_review_2026-05-19_002_prodoc_p1_epro.md` |
| Intake checklist used | `source_packet_intake_checklist_2026-05-14.md` |
| Initial decision | `Partial clue / accepted board-side Gerber + flying-probe net clue` |

## Source Inventory

The ZIP contains a four-layer manufacturing package plus drill and test data:

| Entry | Evidence meaning |
| --- | --- |
| `Gerber_TopLayer.GTL`, `Gerber_BottomLayer.GBL` | Top/bottom copper layers. |
| `Gerber_InnerLayer1.G1`, `Gerber_InnerLayer2.G2` | Inner copper layers; package is four-layer. |
| `Gerber_TopSolderMaskLayer.GTS`, `Gerber_BottomSolderMaskLayer.GBS` | Solder mask layers. |
| `Gerber_TopPasteMaskLayer.GTP`, `Gerber_BottomPasteMaskLayer.GBP` | Paste mask layers. |
| `Gerber_TopSilkscreenLayer.GTO`, `Gerber_BottomSilkscreenLayer.GBO` | Silkscreen layers. |
| `Gerber_BoardOutlineLayer.GKO`, `Gerber_DocumentLayer.GDL` | Board outline and document layer. |
| `Drill_PTH_Through.DRL`, `Drill_PTH_Through_Via.DRL`, `Gerber_DrillDrawingLayer.GDD` | Plated through-hole and via drill data. |
| `FlyingProbeTesting.json` | Component coordinate and pad-level `NET_NAME` data. |
| `PCB下单必读.txt` | Order instruction note only. |

Important parsed facts:

- Gerber headers record `EasyEDA Pro v3.2.91`, generated
  `2026-05-19 11:16:57`.
- `FlyingProbeTesting.json` has `components` and `pins` tables.
- The `pins` table contains pad-level fields including `PIN_NAME`, `PIN_X`,
  `PIN_Y`, `LAYER`, `PIN_TYPE`, `NET_NAME`, pad shape, pad size, hole size,
  and pad angle.

## Packet B - Board Interface Review

| Required field | Evidence observed | Decision |
| --- | --- | --- |
| Current-version EDA/Gerber/route evidence | Same-day Gerber manufacturing package archived with source hash and EasyEDA Pro generation timestamp. | `Partial clue / accepted board-side Gerber clue`. |
| Source date/version is readable or recorded | Gerber headers show `EasyEDA Pro v3.2.91`, `2026-05-19 11:16:57`; ZIP hash recorded. | `Accepted` for source date/hash. |
| Current physical board match is stated | User said hardware teammate supplemented this file. Treat as same-day board-side follow-up, but exact fabrication/revision match is still a follow-up item. | `Partial clue`. |
| Board-side control connector nets | `FlyingProbeTesting.json` records `CN3_1..CN3_15` nets. | `Accepted` for board-side pad/net clue. |
| NUCLEO `CN8` / STM32 endpoint mapping | No NUCLEO `CN8`, STM32 package pins, or harness endpoint mapping is present. | `Blocked`. |
| STDRIVE101 pad nets | `U1_1..U1_25` pad nets are present, including `SCREF`, `24V_FUSED`, `REG12`, `NFAULT`, `INx`, `ENx`, `BOOTx`, `GHSx`, `GLSx`, and `OUTx`. | `Accepted` for board-side pad/net clue. |
| Hall connector pad nets | `U2` pad nets and series resistor nets are present. | `Partial clue`; physical Hall A/B/C numbering still needs pin-1 and harness evidence. |
| Motor connector pad nets | `CN2_1=OUT1`, `CN2_2=OUT2`, `CN2_3=OUT3` are present. | `Partial clue`; motor phase alignment remains unverified. |

Deduplicated `CN3` board-side control connector pad/net table:

| CN3 pin | Flying-probe net |
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

Packet B conclusion: this Gerber package upgrades the project from schematic
source only to board-side manufacturing output plus pad-level net evidence for
`CN3`, `U1`, `J_HALL`, `J_MOTOR`, shunts, and protection-related nets. It still
does not prove NUCLEO `CN8`, STM32 pin mapping, physical connector cabling,
continuity, or powered readiness.

## Packet C - STDRIVE101 Protection Path Review

| Protection item | Evidence observed | Decision |
| --- | --- | --- |
| `DT/MODE` endpoint and resistor/strap value or ground state | STDRIVE101 pad `U1_2` is net `GND_POWER`, matching the schematic clue that pin 2 `DT/MODE` is grounded. | `Partial clue / accepted pad-net clue`; final PWM-mode interpretation still needs human review. |
| `CP` comparator network, filter components, and threshold inputs | STDRIVE101 pad `U1_1` is net `$2N118`; the flying-probe data does not expose a named `CP` net. | `Partial clue`; named route and component interpretation still blocked. |
| `nFAULT` route, pull-up voltage, loading, active-low handling, CN8/STM32 endpoint | `U1_6=NFAULT`, `R3_1=NFAULT`, `R3_2=3V3`, and `CN3_13=NFAULT` are present. | `Partial clue / accepted board-side pad-net clue`; STM32 break endpoint remains `Blocked`. |
| `REG12` capacitor values, loads, and return path | `U1_5=REG12`; `C4_2=REG12`, `C5_2=REG12`; `D1/D2/D3` tie `REG12` to `BOOT1/2/3`. | `Partial clue / accepted pad-net clue`. |
| `SCREF` divider/bias values and VDS monitoring decision | `U1_3=SCREF`; `R1_1=SCREF`, `R1_2=3V3`; `R2_1=GND_SIGNAL`, `R2_2=SCREF`. | `Partial clue / accepted pad-net clue`; threshold math still pending. |
| `VS/VM` relation to MOSFET bus and `24V_FUSED` | `U1_4=24V_FUSED`; Gerber package includes `24V` and `24V_FUSED` pad nets. | `Partial clue`; no powered or current-capacity validation. |
| Bootstrap capacitors and diodes | `C11 OUT1/BOOT1`, `C12 OUT2/BOOT2`, `C13 OUT3/BOOT3`, and `D1/D2/D3 REG12-to-BOOTx` pad nets are present. | `Partial clue / accepted pad-net clue`. |
| `STBY` pull state, MCU route if any, and wake path | No `STBY` net was observed. | `Blocked`. |
| VDS monitoring threshold and fault-release path | `SCREF`, `OUTx`, `GHSx`, and `GLSx` pad nets exist, but behavior and thresholds are not fully reviewed. | `Blocked` for final protection proof. |

Relevant pad/net clues:

| Item | Flying-probe pad/net evidence |
| --- | --- |
| PWM input path | `R4 HIN1-IN1`, `R8 LIN1-EN1`, `R5 HIN2-IN2`, `R6 LIN2-EN2`, `R7 HIN3-IN3`, `R9 LIN3-EN3`. |
| Current sense | `R12 ADC_U-GND_POWER`, `R14 ADC_V-GND_POWER`, `R17 ADC_W-GND_POWER`. |
| Hall connector | `U2_1=+5V`, `U2_5=GND_SIGNAL`, `U2_2/$2N61 -> R22 -> IA`, `U2_3/$2N59 -> R23 -> IB`, `U2_4/$2N58 -> R24 -> IC`. |
| Motor connector | `CN2_1=OUT1`, `CN2_2=OUT2`, `CN2_3=OUT3`. |

## Decision

Decision: `Partial clue / accepted board-side Gerber + flying-probe net clue`.

Accepted exact evidence:

- Four-layer Gerber manufacturing package exists and is archived.
- Gerber headers and ZIP hash are recorded.
- `FlyingProbeTesting.json` provides pad-level `NET_NAME` evidence.
- Board-side `CN3` pad/net mapping matches the schematic-source `CN3` table.
- STDRIVE101 pad nets, PWM input series paths, shunt/current-sense nets,
  Hall connector nets, motor connector nets, `NFAULT`, `REG12`, `SCREF`,
  bootstrap, and output pad nets are visible.

Blocked fields that remain unchanged:

- NUCLEO `CN8` and STM32 endpoint mapping are not proven.
- Physical connector/cable continuity is not proven.
- Exact current fabrication/revision match still needs user or hardware
  teammate confirmation before using this as final build evidence.
- `PB3` / SWO release and Hall B readiness are not proven.
- `J_HALL` physical pin-1 orientation and Hall A/B/C harness numbering are not
  accepted.
- Packet A Workbench / MCSDK selected fields remain `Partial clue / stopped`.
- Generated-project trust remains `Not allowed`.
- Power-stage readiness, Motor Profiler readiness, Hall closed-loop readiness,
  motor readiness, and sensorless readiness remain not allowed.

## Files Updated By This Review

- `hardware/schematic/2026-05-19_gerber_pcb2_stdrive101/Gerber_PCB2_2026-05-19.zip`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_003_gerber_pcb2.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `workflow/evidence_register.md`
- `CURRENT_STATUS.md`

## Required Follow-Up

Before this can become endpoint or readiness proof, the project still needs:

1. Hardware teammate confirmation that this Gerber is the exact PCB revision
   being fabricated, assembled, or tested.
2. `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping evidence.
3. `CN3` and `J_HALL` physical pin-1 orientation image or marked screenshot.
4. If available, the EDA PCB source file for object-level layout review.
5. Later no-power continuity/short checks before any powered phase.

## Review Record Stub

```text
Review ID: P2-SOURCE-REVIEW-2026-05-19-003
Packet type: Packet B / Packet C board-side Gerber and flying-probe net clue
Source path: hardware/schematic/2026-05-19_gerber_pcb2_stdrive101/Gerber_PCB2_2026-05-19.zip
Decision: Partial clue / accepted board-side Gerber + flying-probe net clue
Accepted fields: four-layer Gerber package, source date/hash,
FlyingProbeTesting.json pad-level nets, board-side CN3 pinout, U1 STDRIVE101
pad nets, PWM input paths, shunt/current-sense nets, Hall/motor connector
pad-net clues, NFAULT/REG12/SCREF/bootstrap/output pad nets
Rejected or blocked fields: NUCLEO CN8 endpoint, STM32 pin mapping, exact
fabrication revision confirmation, PB3 release, J_HALL physical numbering,
Packet A selected fields, generated-project trust, powered readiness
Evidence packet updates: Packet B/C now record board-side Gerber and flying
probe pad-net clues without upgrading NUCLEO endpoint proof or powered
readiness
Evidence register updates: EV-2026-05-19-P2-GERBER-PCB2-001
Tests: `python -m unittest discover -s tests` passed, 41 tests OK
Vector store: `python tools\build_vector_store.py` completed, 8093 chunks built
Safety statement: no 24V, no power-board connection, no motor connection,
no Gate PWM output, no Motor Profiler run, no Hall closed-loop claim,
no sensorless / SMO claim.
```
