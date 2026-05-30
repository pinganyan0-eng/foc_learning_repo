# P2 Source Packet Request Pack - 2026-05-14

This is the concrete request pack for the next P2 evidence handoff. It turns
the intake checklist into files, screenshots, and metadata that the team can
collect without touching powered hardware.

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

## How To Use This Pack

1. Collect only files or screenshots that match one of the packets below.
2. Put the source under a clear repo path before asking Codex to review it.
3. Include source date, board revision, source owner, and whether the file
   matches the current physical board.
4. Do not ask Codex to upgrade any blocker unless the required fields are
   readable in the source packet.

Accepted / rejected source rules are defined in
`source_packet_intake_checklist_2026-05-14.md`.

## Packet A - MCSDK / MotorControl Configuration

Request one of these:

- a real Workbench project file: `.stwb6` for MCSDK 6.x, or legacy `.stmcx`;
- a MotorControl / Workbench configuration screenshot;
- an exact launcher path plus captured version/config screen.

Required capture fields:

| Field | Must be visible or recorded | Current target |
| --- | --- | --- |
| MCU / board | MCU name, package, and board/custom context | `STM32G474RETx` / NUCLEO or the intended custom-board context |
| PWM / timer | TIM1 complementary PWM choices | Planning only, no output |
| Fault input | selected break/fault input | Prefer `PB12/TIM1_BKIN` unless source proves a safer final choice |
| Current sensing | 3-shunt / OPAMP / ADC choice | Planning only |
| Hall / sensorless mode | Hall choice, sensorless choice, or explicit absence | No Hall validation, no SMO validation |
| Debug / UART | whether `PA2/PA3` are excluded or reused | Default exclude from FOC UART |
| `PB3` ownership | SWO or Hall B decision | Blocked until release/isolation evidence exists |

Acceptance decision: this packet can only upgrade MCSDK configuration evidence.
It cannot prove Gate PWM behavior, Motor Profiler results, Hall behavior,
motor behavior, or power-stage readiness.

## Packet B - CN8 / Board Route Evidence

Request one current-version source packet:

- EDA source;
- schematic PDF;
- netlist;
- high-resolution schematic or PCB crop.

Required capture fields:

| Field | Must be visible or recorded |
| --- | --- |
| Board revision | Source date/version and current physical board match statement |
| CN8 mapping | `NFAULT`, PWM inputs, current-sense nets, Hall nets, `3V3`, ground |
| STM32 endpoints | MCU pins or connector pins for each reviewed net |
| STDRIVE101 endpoints | driver pins for fault, input, supply, bootstrap, and protection nets |
| Readability | net names, pin names, reference designators, and values are readable |

Acceptance decision: this packet can only upgrade board-route evidence. It does
not authorize continuity checks, powered testing, Gate PWM, or motor actions.

## Packet C - STDRIVE101 Protection Path Evidence

Request board-level source evidence for these nets and components:

| Protection item | Required board evidence |
| --- | --- |
| `DT/MODE` | endpoint plus resistor/strap value or ground state |
| `nFAULT` | route, pull-up voltage, LED/loading, active-low handling, CN8/STM32 endpoint |
| `REG12` | capacitor values, placement intent, load list, return path |
| `CP` | comparator network, filter components, threshold inputs |
| `SCREF` | divider/bias values, enabled/disabled VDS monitoring decision |
| `VS/VM` | relation among `VS`, `VM`, MOSFET bus, and `24V_FUSED` |
| Bootstrap | `BOOTx` to `OUTx` capacitor and diode/component orientation for U/V/W |
| `STBY` | pull state, MCU route if any, wake path |
| VDS monitoring | threshold path and fault-release path |

Acceptance decision: this packet can upgrade STDRIVE101 protection-path review
only if it proves current-board implementation. ST datasheet facts alone remain
device requirements, not board proof.

## Rejected For This Request

Do not submit these as proof:

- low-resolution screenshots;
- oral descriptions;
- old or unknown-version EDA/PDF/netlist files;
- partial crops without endpoints or board revision;
- generated MCSDK source without matching Workbench project file or
  configuration screen;
- the excluded WeChat-side `netlist_PADS.net` candidate.

## Current Blocking State

| Evidence chain | Current state | Next accepted packet |
| --- | --- | --- |
| MCSDK / MotorControl | Partial clue / Preparation only. `My_First_FOC.stwb6` is preserved as a legacy learning leftover, and the 2026-05-16 custom NUCLEO + STDRIVE101 capture package exists, but no project-specific `.stwb6` or selected-field screenshots are accepted yet. | Packet A GUI screenshots or accepted final Workbench project |
| CN8 / board route | Blocked. No current-version EDA/PDF/netlist/high-resolution route crop exists. | Packet B |
| STDRIVE101 protection path | Blocked. Only official requirements and missing-evidence matrix exist. | Packet C |
| `PB3` Hall/SWO | Blocked. Current `.ioc` still records `PB3.Signal=SYS_JTDO-SWO`. | Packet A plus Packet B or NUCLEO bridge evidence |

## Codex Review Steps After A Packet Arrives

1. Confirm the packet source type and version.
2. Check it against `source_packet_intake_checklist_2026-05-14.md`.
3. Fill `source_packet_review_template_2026-05-14.md` or a dated copy of it
   with Accept / Partial clue / Reject.
4. Update `evidence_packet_2026-05-14.md` only for fields proven by the packet.
5. Update `workflow/evidence_register.md` with limits and forbidden claims.
6. Run `python -m unittest discover -s tests`.
7. Rebuild `vector_store/` if project docs or evidence files changed.

If a packet is incomplete, keep the related item blocked and record it as a
clue only.

## Current Decision

This request pack makes the next handoff executable, but it does not add any
new board evidence. P2 still cannot claim MCSDK MotorControl configuration
completion, CN8 routing proof, STDRIVE101 protection-path proof, power-stage
readiness, Hall readiness, or sensorless readiness.
