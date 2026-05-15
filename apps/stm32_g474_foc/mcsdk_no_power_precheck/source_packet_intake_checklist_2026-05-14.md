# P2 Source Packet Intake Checklist - 2026-05-14

This is a P2 no-power intake checklist. It defines what the repo can accept as
new evidence for the MCSDK / STDRIVE101 review, and what must remain blocked.

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

## Accepted Source Packets

### 1. MCSDK / MotorControl Configuration Packet

Accepted source evidence:

- a real Workbench `.stmcx` saved into the P2 no-power directory or another
  clearly named repo path;
- a MotorControl / Workbench configuration screenshot showing the MCU,
  key timer/PWM choices, current-sense mode, protection input, and any Hall or
  sensorless mode selection;
- an exact reproducible GUI path plus a captured version/config screen when a
  saved file cannot be exported yet.

Minimum fields to record:

| Required field | Why it is needed | Current status |
| --- | --- | --- |
| MCU and board context | Confirms the project targets `STM32G474RETx` / NUCLEO or the intended custom board context. | Blocked until `.stmcx` or MotorControl screen exists. |
| TIM1 PWM assignment | Prevents trusting a complementary-output plan that is not actually selected. | Blocked. |
| `PB12/TIM1_BKIN` or final fault input | Prevents confusing a CubeMX draft pin with a trusted MCSDK protection path. | Blocked. |
| `PA2/PA3` exclusion or documented reuse decision | Keeps the P1 VCP path from silently colliding with OPAMP/PGA planning. | Blocked. |
| `PB3` Hall/SWO decision | Prevents claiming Hall B while SWO still owns the pin. | Blocked. |

P2 decision: this packet may prove configuration intent only. It does not prove Gate PWM behavior, Motor Profiler results, Hall behavior, motor behavior, or power-stage safety.

### 2. CN8 / Board Route Packet

Accepted source evidence:

- current-version EDA source;
- current-version schematic PDF;
- current-version netlist;
- current-version high-resolution local schematic or PCB crop that clearly
  shows net names, endpoint pins, component references, and board revision.

Minimum fields to record:

| Required field | Why it is needed | Current status |
| --- | --- | --- |
| Source date/version and board revision | Prevents old or unrelated board files from being treated as current board truth. | Blocked. |
| CN8 mapping | Must prove `NFAULT`, PWM inputs, current-sense nets, Hall nets, `3V3`, and ground. | Blocked. |
| STM32 endpoint mapping | Must connect the planned MCU pins to actual connector or board nets. | Blocked. |
| STDRIVE101 endpoint mapping | Must connect STDRIVE101 inputs, fault, supply, bootstrap, and protection pins to named nets. | Blocked. |
| Screenshot readability if crop-based | Every relevant net name, reference designator, value, and pin must be readable. | Blocked. |

P2 decision: this packet may upgrade board-route evidence only when the source
is current-version and readable. It still does not authorize powered testing.

### 3. STDRIVE101 Protection Path Packet

Accepted source evidence:

- current-version EDA, schematic PDF, netlist, or high-resolution crop proving
  the board-level implementation of the STDRIVE101 protection paths;
- ST official datasheet or product-page references only for device behavior,
  not as proof of this board's wiring.

Minimum fields to record:

| Required field | Why it is needed | Current status |
| --- | --- | --- |
| `DT/MODE` endpoint and value/strap | Determines whether the TIM1 / MCSDK input strategy can match the driver. | Blocked. |
| `nFAULT` route, pull-up, loading, and active-low semantics | Determines whether the STM32 break/fault path can be trusted. | Blocked. |
| `REG12` capacitor values, loads, and return path | Checks the gate-driver supply support network. | Blocked. |
| `CP` network | Defines overcurrent comparator threshold/filtering assumptions. | Blocked. |
| `SCREF` network and VDS-monitoring decision | Defines whether VDS monitoring is enabled, disabled, or threshold-limited. | Blocked. |
| `VS/VM`, bootstrap, `STBY`, and VDS release path | Determines whether later fault behavior can be interpreted. | Blocked. |

P2 decision: the existing STDRIVE101 digest and missing-evidence matrix define
review requirements. They do not prove the current board implementation.

## Rejected Source Types

Do not upgrade evidence from these sources:

- low-resolution screenshots where net names, pin names, component values, or
  board revision cannot be read;
- oral descriptions without a repo-stored source file or screenshot;
- old, draft, or unknown-version EDA/PDF/netlist files;
- partial crops that omit endpoints or board revision;
- generated MCSDK source without the matching `.stmcx` or configuration screen;
- the excluded WeChat-side `netlist_PADS.net` candidate.

Rejected sources may be recorded as clues, but they must remain `Blocked` or
`Low-grade clue only` in the evidence packet.

## Intake Procedure

When a new source packet arrives:

1. Place the source in the correct repo area without renaming away its date,
   version, or origin.
2. Record source type, source date/version, board revision, and who provided it.
3. Check it against the required fields above.
4. Update `evidence_packet_2026-05-14.md` only for the exact items the source
   proves.
5. Update `workflow/evidence_register.md` with the evidence limit and forbidden
   claims.
6. Keep unrelated P2 blockers unchanged.

If any required field is missing, the related item remains blocked.

## Current Decision

As of this checklist, the repo still has no accepted `.stmcx` / MotorControl
configuration packet, no accepted CN8 / board route packet, and no accepted
board-level STDRIVE101 protection path packet.

P2 may continue evidence intake and document review only. It may not claim
MCSDK MotorControl configuration completion, CN8 routing proof, STDRIVE101
protection-path proof, power-stage readiness, Hall readiness, or sensorless
readiness.
