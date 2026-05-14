# STDRIVE101 Protection Path Review - 2026-05-14

This is a P2 no-power evidence artifact. It turns the STDRIVE101 datasheet and
the current low-grade schematic screenshot clues into a board-review matrix.

It is not a wiring instruction, not a continuity result, not generated
firmware, and not hardware validation.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## Source Policy

Official requirements:

- STDRIVE101 product page:
  <https://www.st.com/en/power-management/stdrive101.html>
- STDRIVE101 datasheet:
  <https://www.st.com/resource/en/datasheet/stdrive101.pdf>
  (`DS13472 Rev 2`, June 2022)
- Repo-local PDF:
  `materials/raw/st_manuals/st_stdrive101_datasheet.pdf`
- Repo-local extracted digest:
  `materials/extracted/st_manuals/st_stdrive101_datasheet_digest.md`

Low-grade board clue only:

- `hardware/schematic/2026-05-09_power_board_schematic_screenshot.jpg`
- `hardware/schematic/2026-05-09_power_board_schematic_screenshot.md`

Accepted board evidence must be current-version EDA source, current-version
schematic PDF, current-version netlist, or a high-resolution local schematic
crop that clearly shows the target net and endpoint pins.

The existing screenshot may guide what to ask for next, but it does not prove
CN8 routing, PCB routing, connector pinout, protection-path correctness, or
power-stage readiness.

## Official Requirements Summary

| Area | ST official requirement or behavior | P2 meaning |
| --- | --- | --- |
| `DT/MODE` | Selects the input strategy. ENx/INx mode uses an adjustable deadtime resistor; short-to-ground selects INHx/INLx mode with interlocking. | MCSDK/TIM1 output style is blocked until the physical strap or resistor is proven. |
| `nFAULT` | Open-drain fault output. It is forced low for overcurrent, VDS monitoring protection, thermal shutdown, and REG12 UVLO. | The route, pull-up voltage, active-low semantics, and STM32 fault path must all be proven. |
| `REG12` | 12 V LDO output and gate-driver supply. The datasheet requires bypass capacitance and limits total regulator consumption. | Capacitor value, placement, load budget, and return path must be reviewed before power. |
| `CP` | Overcurrent comparator input. | The board threshold and filtering are unknown until the actual net and surrounding components are proven. |
| `SCREF` | Sets the VDS monitoring threshold; high enough bias disables VDS monitoring. | VDS threshold or disabled state must be explicit, not guessed from the screenshot. |
| `VS/VM` | `VS` supplies the device and VDS-monitor reference; ST requires the power-stage voltage relationship to be valid. | The board must prove how `VS`, `VM`, and `24V_FUSED` relate before any bring-up claim. |
| Bootstrap | Integrated bootstrap diodes use external bootstrap capacitors from `BOOTx` to `OUTx`. | Capacitor values and routes must be proven for all three phases before gate-drive trust. |
| `STBY` | Standby and wake-up behavior affects gate output availability and `nFAULT` timing. | Default state and wake path must be known before interpreting faults or PWM behavior. |
| VDS monitoring | Compares MOSFET VDS to the `SCREF` threshold and latches a fault until standby release. | It can create real or false faults; P2 must preserve this as a hard review item. |

## Board Review Matrix

| Item | Official requirement | Current screenshot clue | Current trust level | Missing accepted evidence | P2 decision |
| --- | --- | --- | --- | --- | --- |
| `DT/MODE` | Must prove whether STDRIVE101 is in ENx/INx mode with resistor-set deadtime or INHx/INLx mode by short-to-ground. | Existing screenshot notes say the connection is unclear. | Blocked. | Current EDA/PDF/netlist/crop showing `DT/MODE` endpoint and value or ground strap. | Do not trust MCSDK PWM style or TIM1 complementary-output meaning yet. |
| `nFAULT` | Open-drain output, forced low on overcurrent, VDS monitoring fault, thermal shutdown, and REG12 UVLO. | Screenshot note sees `R3 10K` pull-up to `3V3` and `LED1` to `GND_SIGNAL`, but route to CN8/STM32 is not accepted proof. | Blocked for board route; useful as review clue. | Current source proving STDRIVE101 `nFAULT` to CN8 `NFAULT`, CN8 to `PB12/TIM1_BKIN`, pull-up voltage, LED loading, and active-low handling. | Keep `PB12/TIM1_BKIN` as a draft candidate only. Do not claim hardware fault handling. |
| `REG12` | 12 V LDO and gate-driver supply needs proper bypass capacitance and load budget. | Screenshot note sees `C4 4.7uF` and `C5 0.1uF` to `GND_SIGNAL`. | Blocked for placement/load/return path. | Current source proving capacitor values, placement intent, all loads on `REG12`, and return path relative to EPAD/GND. | Treat as mandatory P3 precheck item, not as passed evidence. |
| `CP` | Overcurrent comparator input; board network defines the threshold and filtering. | Screenshot note sees `C1 100nF`, but does not prove full comparator network. | Blocked. | Current source showing `CP` network, connected shunt/sense source, filter components, and comparator threshold calculation inputs. | Do not claim overcurrent threshold or protection effectiveness. |
| `SCREF` | Sets VDS monitoring threshold; protection can also be disabled by high enough bias. | Screenshot note sees `R1 33K` to `3V3` and `R2 20K` to `GND_SIGNAL`. | Low-grade clue only. | Current source proving divider endpoints, actual values, resulting threshold or disabled state, and relation to `VS/VM`. | Do not claim the 55 A or any VDS threshold until datasheet math and board source are reviewed. |
| `VS/VM` | `VS` supplies the driver and VDS reference; the power-stage voltage must not violate the datasheet relationship. | Screenshot note suggests `VS/24V_FUSED` nearby and board input `24V_FUSED`, but not a full power-tree proof. | Blocked. | Current source proving `VS`, power-stage `VM`, `24V_FUSED`, MOSFET drain bus, and any split or filtering between them. | Keep VDS monitoring and bring-up readiness blocked. |
| Bootstrap | `BOOTx`, `OUTx`, and `REG12` bootstrap network must support each high-side driver. | Screenshot note sees `C22/C23/C24 1uF`, `D1/D2/D3 SS34`, and `BOOTx/OUTx/REG12` labels. | Low-grade clue only. | Current source proving each `BOOTx` to `OUTx` capacitor and any diode/component orientation for all phases. | Do not trust high-side gate-drive readiness. |
| `STBY` | Standby controls wake-up and affects when outputs and `nFAULT` become meaningful. | Existing screenshot summary does not identify a clear `STBY` route or default state. | Blocked. | Current source showing `STBY` net, pull state, MCU control if any, and wake sequence assumptions. | Do not interpret future `nFAULT` behavior without standby-state evidence. |
| VDS monitoring | VDS fault latches the gate outputs low and forces `nFAULT` low; release requires standby. | Screenshot clue shows `SCREF` divider only; it does not prove enabled/disabled behavior or `VS/VM` relationship. | Blocked. | Current source proving `SCREF`, `VS/VM`, MOSFET drain/source endpoints, and intended fault-release path. | Treat VDS monitoring as a hard blocker before P3 power-stage readiness. |

## Minimum Accepted Protection Packet

Before any protection-path item can be upgraded from blocked to proven, the repo
needs one current-version accepted source packet containing:

- STDRIVE101 endpoint mapping for `DT/MODE`, `nFAULT`, `REG12`, `CP`,
  `SCREF`, `VS`, `BOOTx`, `OUTx`, `STBY`, and all gate outputs.
- CN8 mapping for `NFAULT`, PWM inputs, current-sense nets, Hall nets, `3V3`,
  and `GND_SIGNAL`.
- A statement that the source matches the current physical board version.
- If a screenshot crop is used, enough resolution to read all relevant net
  names, component values, reference designators, and STDRIVE101 pins.
- A written decision on whether VDS monitoring is enabled or intentionally
  disabled.

## Current Decision

This review upgrades P2 from a loose STDRIVE101 note to a concrete missing-
evidence matrix. It does not upgrade any board signal to proven.

Current P2 may continue document review, GUI/config capture, and source-packet
collection. It may not claim STDRIVE101 protection-path proof, CN8 routing
proof, power-stage readiness, Hall readiness, Motor Profiler readiness, or
sensorless readiness.
