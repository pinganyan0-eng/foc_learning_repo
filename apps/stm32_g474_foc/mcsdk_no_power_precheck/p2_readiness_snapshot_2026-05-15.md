# P2 Readiness Snapshot - 2026-05-15

This snapshot answers one control question:

`Can the project move from P2 no-power planning to generated-project trust,
build-only work, or hardware action?`

Current answer: no. P2 remains in progress. Generated-project trust is
`Not allowed` because Packet A is only `Partial clue / Preparation only`.
The 2026-05-18 Packet A capture task package is workflow-only preparation, not
accepted Packet A evidence. The 2026-05-19 Workbench capture attempt adds only
launch/control-board visibility and then stops because no acceptable self-made
STDRIVE101 power-stage context was captured. The 2026-05-19 ProDoc `.epro`
intake adds a current schematic-source clue for the self-developed STDRIVE101
driver board, but it has no PCB layout data and does not prove NUCLEO `CN8` or
STM32 endpoint mapping. The 2026-05-19 Gerber PCB2 intake adds board-side
manufacturing-output and flying-probe pad-net clues, but still does not prove
NUCLEO `CN8`, STM32 endpoint mapping, continuity, or powered readiness.
The 2026-05-19 hardware supplement handoff is now the current exact request
pack for board-revision confirmation, endpoint mapping, connector orientation,
PB3/SWO, STDRIVE101 protection details, PCB source, and later no-power
continuity records. The 2026-05-19 minimal hardware request narrows the first
hardware-teammate packet to exact Gerber PCB2 revision confirmation,
`CN3 -> NUCLEO/CN8 -> STM32 pin` mapping, and marked `CN3` / `J_HALL` pin-1
evidence. The 2026-05-19 Workbench asset probe found installed Board Designer
and Board Manager executables referenced by Workbench config, but it did not
produce an accepted custom board definition or `.stwb6`. The 2026-05-19 PCB2
mapping / pin-1 / protection packet adds a current PCB2 source statement,
P1-P15 endpoint table, connector-orientation images, Hall relationship, PB3/SWO
handling, and STDRIVE101 protection-chain intent. A later clarification image
states `PC7/PB3/PB10` was an alternate suggestion, not current PCB2 physical
routing; current PCB2 Hall routing is `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`.
The 2026-05-19 current PCB2 Hall/PWM strategy review opens the no-PCB-change
path first: current PWM / driver-input routing
`HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10` and software
Hall feasibility on `PA0/PA1/PB4` need Packet A / firmware design review.
The 2026-05-19 Packet A / firmware feasibility review concludes that this
no-PCB-change route remains feasibility only: current PWM is not cleared as
standard MCSDK `TIM1` complementary PWM selected-field evidence, and
`PA0/PA1/PB4` is not cleared as same-timer hardware Hall. Packet A is not
accepted.
The 2026-05-19 software Hall adapter design review keeps the same boundary:
`PA0/PA1/PB4` may be discussed only as future GPIO/EXTI sampling, edge
timestamping, valid-state filtering, minimal ISR responsibility, and MCSDK
integration design. It does not implement an adapter, does not define a runtime
API, does not accept Packet A, and provides no generated-project trust.
The 2026-05-19 Packet A Board Designer / Board Manager path review concludes
that the local Board Designer / Board Manager path exists as documentation and
tool clue for a self-developed STDRIVE101 board, but Packet A still blocked:
no custom/user board artifact, project-specific `.stwb6`, or selected-field
screenshot is accepted, and there is no generated-project trust.
The 2026-05-19 Packet A Board Designer / Manager GUI-only checklist now defines
the next user-side screenshot capture path and hard stops. It does not launch
GUI tools, does not create a board, does not create a `.stwb6`, and does not
accept Packet A.
The 2026-05-19 MY_FOC generated project source review records the user's new
Workbench project as `Partial clue / generated project quarantined / Packet A
not accepted`. It proves a real Workbench 6.4.2 generated project exists, but
the project is `SIX_STEP`, not FOC; current sensing and fault/break are
disabled, the motor entry is a demo clue, and Hall/PWM pins still need either
an accepted physical change or a new matching Workbench route. The user says
pins can be changed, so the mismatch is editable future work, not a permanent
rejection. No generated-project trust is added.
The 2026-05-19 MY_FOC manual FOC edit attempt changed the source Workbench
`MY_FOC.stwb6` from `"algorithm": "sixStep"` to `"algorithm": "FOC"`, but
Workbench then failed to load the file with `一般错误 / 无法加载文件`. Codex
rolled the external source back to the backup, so the current external
`MY_FOC.stwb6` again reads `"algorithm": "sixStep"`. This proves the one-field
manual edit is not a valid FOC conversion path. Packet A is still not accepted.
Hardware action is not a P2 state.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
- No flash or board run from a generated motor-control project.

## Feature Sentence

The P2 readiness snapshot consolidates Packet A/B/C, PB3/SWO, signal-contract,
and build-only gate status so future turns can see exactly what is ready,
blocked, or only a planning artifact.

## Current Gate Decision

| Gate | Current decision | Why |
| --- | --- | --- |
| P2 no-power planning | In progress | P2 documents, reviews, and blocker governance exist. |
| Packet A MCSDK / MotorControl evidence | Partial clue / Preparation only / stopped | `My_First_FOC.stwb6` is preserved as a legacy learning leftover, the 2026-05-16 custom NUCLEO + STDRIVE101 capture package exists, the 2026-05-17 vendor motor / G431 pin-table intake and 2026-05-18 motor wiring image add only candidate clues, the 2026-05-18 task package fixes the future capture path, and the 2026-05-19 Workbench attempt shows launch plus `NUCLEO-G474RE` / `STM32G474RETx` control-board context. The user clarified the driver board is self-developed around the STDRIVE101 chip, so built-in ST boards cannot substitute for the project power board. No new project-specific `.stwb6` or selected-field screenshots are accepted yet. |
| Generated-project trust | Not allowed | `future_build_only_gate_2026-05-15.md` requires accepted Packet A selected fields first. |
| No-power build-only generated project | Not allowed now | Build-only work is a future state after accepted Packet A evidence. |
| Packet B CN8 / board-route proof | Partial clue / current PCB2 mapping source, Hall/PWM conflicts clarified | The 2026-05-19 `.epro` and Gerber PCB2 package show board-side `CN3`, `U1`, `J_HALL`, `J_MOTOR`, shunt, protection, and output pad/net clues. The 2026-05-19 mapping packet adds P1-P15 endpoint rows and clarifies current PCB2 Hall route as `IA/IB/IC -> PA0/PA1/PB4`; Packet A selected fields and continuity remain missing. |
| Packet C STDRIVE101 protection proof | Partial clue / current board-intent statement, still blocked for final proof | The `.epro`, Gerber, and 2026-05-19 mapping packet now show `DT/MODE -> GND`, `CP -> 100 nF -> GND`, `SCREF` divider, `nFAULT` pull-up, no separate `STBY`, `REG12`, bootstrap, output, and MOSFET bridge clues. Threshold math, STM32 endpoint handling, continuity, and powered validation remain unresolved. |
| Hardware supplement handoff | Open / ready | `hardware_supplement_handoff_2026-05-19.md` converts the remaining board-side blockers into exact hardware teammate requests. It is workflow/evidence governance only and does not upgrade Packet B/C, PB3/SWO, `J_HALL`, continuity, or readiness. |
| Minimal hardware request | Open / ready | `hardware_teammate_min_request_2026-05-19.md` is the short first packet to send to the hardware teammate: exact Gerber PCB2 revision confirmation, complete `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping, and marked `CN3` / `J_HALL` pin-1 evidence. |
| Packet A Workbench asset probe | Partial clue / local tool path found / blocked | `packet_a_workbench_asset_probe_2026-05-19.md` found Workbench references to Board Designer / Board Manager and local executables, but no accepted self-developed STDRIVE101 board definition, `.stwb6`, or selected-field screenshots. |
| Current PCB2 Hall/PWM strategy | No-power strategy review opened / no PCB change first | `current_pcb2_hall_pwm_strategy_2026-05-19.md` downgrades the old standard `TIM1` PWM and `PA15/PB3/PB10` Hall drafts to historical or alternate candidates only. Current PCB2 routes need Packet A / firmware feasibility review and do not upgrade Hall readiness. |
| Current PCB2 Packet A / firmware feasibility | No-PCB-change route remains feasibility only / Packet A not accepted | `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md` reviews the current PWM and Hall routes against local pin-function clues. It does not clear standard MCSDK TIM1 selected fields, same-timer hardware Hall, generated-project trust, or build-only work. |
| Software Hall adapter design review | Software Hall adapter remains no-power design review / Packet A not accepted | `software_hall_adapter_design_review_2026-05-19.md` defines future GPIO/EXTI sampling, timestamping, valid-state filtering, bounce/repeated-state rejection, minimal ISR responsibility, MCSDK integration boundaries, and `hardware-rework planning` hard stops. It does not add firmware, runtime APIs, generated source, Hall readiness, generated-project trust, or build-only clearance. |
| Packet A Board Designer / Board Manager path review | Board Designer / Board Manager path exists as local documentation and tool clue / Packet A still blocked | `packet_a_board_designer_manager_path_review_2026-05-19.md` confirms local Workbench external-tool entries, Board Designer / Board Manager executables, and Board Designer manual custom-board workflow clues. It does not accept Packet A, does not create the self-developed STDRIVE101 board source, and does not add generated-project trust. |
| Packet A Board Designer / Manager GUI-only checklist | GUI-only checklist prepared / Packet A still blocked | `packet_a_board_designer_manager_gui_checklist_2026-05-19.md` defines later screenshot names, save directory, custom/import/create board screens, Power/Control/Inverter board flows, Board Aggregation, Finalize/save prompt, Board Manager import/list path, and hard stops. It does not launch GUI or add generated-project trust. |
| MY_FOC generated project source review | Partial clue / generated project quarantined / Packet A not accepted | `source_packet_review_2026-05-19_005_my_foc_generated_project.md` archives selected files from the user-created `MY_FOC` project and records that it is `SIX_STEP`, not FOC. Pins can be changed later, but that requires a new reviewable FOC configuration and matching physical route. No generated-project trust, build-only clearance, or powered readiness is added. |
| MY_FOC manual FOC edit rollback | Manual FOC source edit failed Workbench reload / rolled back / Packet A still not accepted | `my_foc_foc_candidate_edit_2026-05-19.md` records the external `.stwb6` source edit attempt, Workbench load failure, and rollback to the backup. The current external `MY_FOC.stwb6` again reads `"algorithm": "sixStep"`; the failed FOC candidate is negative evidence only. |
| PB3 Hall B readiness | Not the current PCB2 Hall path / still blocked for any alternate use | Current `.ioc` still records `PB3.Signal=SYS_JTDO-SWO`. The 2026-05-17 pin table does not release SWO by itself. The 2026-05-19 clarification says current PCB2 uses `PB3` for `LIN1`, while `PC7/PB3/PB10` Hall was only an alternate suggestion. |
| P3 powered or motor work | Not allowed | P2 has no continuity checks, current-limited bring-up record, waveform checks, or rollback evidence. |

## Readiness Matrix

| Track | Current evidence | Current status | Unlock condition |
| --- | --- | --- | --- |
| Packet A | `packet_a_local_probe_2026-05-15.md`, `packet_a_capture_checklist_2026-05-15.md`, `source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`, `source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`, `source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`, `source_packet_review_2026-05-18_001_motor_wiring_definition.md`, `packet_a_capture_task_2026-05-18.md`, `source_packet_review_2026-05-19_001_packet_a_workbench_capture_attempt.md`, `packet_a_workbench_asset_probe_2026-05-19.md`, and `source_packet_review_2026-05-19_005_my_foc_generated_project.md` | Partial clue / Preparation only / generated project quarantined | Find or create a reviewable FOC Workbench configuration for the self-developed STDRIVE101 board. If pins will be changed, the new route must be timer-compatible and physically matched; if pins will not be changed, the software Hall path remains design review only. Built-in ST boards may not be treated as board-match substitutes. |
| Packet B | `source_packet_review_2026-05-15_001_cn8_stdrive101_schematic_candidate.md`, `source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`, `mcu_pin_compatibility_check_2026-05-17.md`, `source_packet_review_2026-05-19_002_prodoc_p1_epro.md`, `source_packet_review_2026-05-19_003_gerber_pcb2.md`, and `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md` | Partial clue / current PCB2 mapping source, Hall/PWM conflicts clarified | Current PCB2 endpoint mapping is now clear at source level: `PB3=LIN1`, `PB10=HIN2`, and Hall is `IA/IB/IC -> PA0/PA1/PB4`. Still need Packet A/CubeMX/Workbench selected fields and later continuity before trusting generated pins or readiness. |
| Packet C | `stdrive101_protection_path_review_2026-05-14.md`, `source_packet_review_2026-05-19_002_prodoc_p1_epro.md`, `source_packet_review_2026-05-19_003_gerber_pcb2.md`, and `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md` | Partial clue / current board-intent statement, still blocked for final proof | Finish protection review for `DT/MODE`, `STBY`, `NFAULT`, `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, and VDS monitoring, including threshold math, STM32 endpoint handling, continuity, and later powered validation. |
| Hardware supplement handoff | `hardware_supplement_handoff_2026-05-19.md`, `hardware_teammate_min_request_2026-05-19.md`, `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md` | Mostly answered / Packet A strategy needed | Current PCB2 version, mapping, pin-1, Hall relationship, PB3/SWO guidance, and protection-chain statements were provided. The next request is not more hardware mapping; it is a no-power Packet A / firmware decision for software Hall on `PA0/PA1/PB4` or future hardware rework. |
| Current PCB2 Hall/PWM strategy | `current_pcb2_hall_pwm_strategy_2026-05-19.md`, `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md`, local MCSDK `STM32G474RETx.json` pin-function clue | No-power strategy review opened / no PCB change first | Packet A / firmware review must decide whether current PCB2 can proceed without PCB changes. `PA0/PA1/PB4` is not a same-timer hardware Hall set, and the current `HIN/LIN` route is not accepted as a standard MCSDK TIM1 complementary PWM set. |
| Current PCB2 Packet A / firmware feasibility | `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md`, local MCSDK `STM32G474RETx.json` pin-function clue, `future_build_only_gate_2026-05-15.md` | Feasibility only / Packet A not accepted | The current no-PCB-change route can proceed only as later firmware design review. It does not open generated-project trust or build-only clearance. |
| Software Hall adapter design review | `software_hall_adapter_design_review_2026-05-19.md`, `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md`, `future_build_only_gate_2026-05-15.md` | No-power design review only / Packet A not accepted | The software Hall path can proceed only as a future implementation design after Packet A is accepted. If MCSDK / Workbench needs same-timer hardware Hall, or the adapter would invade the high-frequency FOC path, open `hardware-rework planning` instead. |
| Packet A Board Designer / Board Manager path review | `packet_a_board_designer_manager_path_review_2026-05-19.md`, `packet_a_workbench_asset_probe_2026-05-19.md`, local `STMCBD-UM.pdf`, `wb2mx.properties` | Local path clue / Packet A still blocked | Use a later GUI-only Board Designer / Board Manager capture only to prove a reviewable custom/user board artifact for the self-developed STDRIVE101 board. Built-in ST boards cannot be treated as board-match evidence, and this review does not open generated-project trust or build-only clearance. |
| Packet A Board Designer / Manager GUI-only checklist | `packet_a_board_designer_manager_gui_checklist_2026-05-19.md`, `packet_a_board_designer_manager_path_review_2026-05-19.md` | Checklist ready / Packet A still blocked | The user can later capture GUI-only screenshots under `packet_a_sources/2026-05-19_board_designer_manager_path/screenshots/`. The capture must stop before Generate, Motor Profiler, Motor Pilot, Flash, source generation, fake board saving, or any hardware action. |
| MY_FOC generated project | `source_packet_review_2026-05-19_005_my_foc_generated_project.md`, `packet_a_sources/2026-05-19_my_foc_generated_project/` | Generated project quarantined / Packet A not accepted | Useful clue only. The next acceptable update is not to build this source tree; it is to correct the Workbench project to FOC, restore required current-sense and fault choices, and make Hall/PWM match either changed pins or a documented software Hall route. |
| MY_FOC manual FOC edit rollback | `my_foc_foc_candidate_edit_2026-05-19.md`, `MY_FOC.codex_foc_candidate_2026-05-19.stwb6` | Failed manual edit / rolled back / Packet A still not accepted | Do not use the failed FOC candidate as a source. Reopen the restored `MY_FOC.stwb6` only to confirm the original project loads, then use Workbench GUI flow or a new complete FOC project for the next Packet A attempt. Stop before Generate, build, flash, Motor Profiler, Motor Pilot, or hardware action. |
| PB3 / SWO | Saved NUCLEO `.ioc` shows SWO ownership; 2026-05-19 clarification says current PCB2 uses `PB3` as `LIN1`, not Hall | Blocked only for alternate Hall use | Do not use `PB3` as current PCB2 Hall. Any alternate Hall use of `PB3` would still need SWO release/isolation and a new accepted route. |
| STM32 signal contract | `stm32_side_signal_contract_2026-05-15.md` | Planning contract | Update only after Packet A/B/C or PB3/SWO evidence changes. |
| Future build-only gate | `future_build_only_gate_2026-05-15.md` | Dormant | Use only after Packet A exists and the generated project is explicitly no-power. |

## Claim Matrix

Allowed current claims:

- The repo has a P2 no-power evidence governance layer.
- The repo has a saved NUCLEO CubeMX `.ioc` draft and GUI fallback evidence.
- The repo has local STDRIVE101 official-source review material.
- The repo has a `Partial clue` schematic candidate for Packet B/C review.
- The repo has written signal-contract and future build-only rules.
- The repo has a local MCSDK 6 `.stwb6` legacy learning file reviewed as
  `Partial clue`.
- The repo has a 2026-05-16 custom NUCLEO + STDRIVE101 Packet A capture
  package reviewed as `Partial clue / Preparation only`.
- The repo has a 2026-05-17 supplier motor source and hardware teammate pin
  table reviewed as `Partial clue`; local MCSDK assets confirm the compared
  key G431/G474 MCU pin functions, but not board routing.
- The repo has a 2026-05-18 workflow-only Packet A capture task package that
  fixes the future `.stwb6` path, screenshot names, stop conditions, and field
  acceptance matrix.
- The repo has a 2026-05-18 motor wiring definition image reviewed as
  `Partial clue`; it records candidate U/V/W and Hall wire colors, but not
  physical harness verification, Hall power behavior, phase/Hall alignment, or
  `J_HALL` numbering.
- The repo has a 2026-05-19 Workbench capture attempt reviewed as
  `Partial clue / stopped`; Workbench 6.4.2 launches and
  `NUCLEO-G474RE` / `STM32G474RETx` control-board context is visible, but no
  accepted self-made STDRIVE101 power-stage context or selected-field
  screenshot was captured.
- The repo has a user-confirmed 2026-05-19 EDA Pro schematic source for the
  self-developed STDRIVE101 driver board. It supports board-side schematic
  clues for `U1=STDRIVE101`, `CN3` 15-pin control connector, `J_HALL`,
  `J_MOTOR`, MOSFETs, shunts, `NFAULT`, `REG12`, `SCREF`, bootstrap, and
  output nets. It does not contain PCB layout data.
- The repo has a 2026-05-19 Gerber PCB2 manufacturing package with
  `FlyingProbeTesting.json`. It supports board-side pad-net clues for `CN3`,
  `U1=STDRIVE101`, PWM input paths, shunt/current-sense nets, `J_HALL`,
  `J_MOTOR`, `NFAULT`, `REG12`, `SCREF`, bootstrap, and output nets. It does
  not prove NUCLEO `CN8` or STM32 endpoint mapping.
- The repo has a 2026-05-19 hardware supplement handoff that defines the next
  hardware teammate evidence request after the `.epro` and Gerber reviews.
  It is a request/governance artifact and does not upgrade any hardware
  readiness claim.
- The repo has a 2026-05-19 minimal hardware-teammate request that can be sent
  first. It asks for exact Gerber PCB2 revision confirmation,
  `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping, and marked `CN3` / `J_HALL`
  pin-1 evidence.
- The repo has a 2026-05-19 Workbench asset probe showing that Board Designer
  and Board Manager executables are installed and referenced by Workbench
  config. This is only a local path clue, not a custom-board Packet A source.
- The repo has a 2026-05-19 current PCB2 mapping / pin-1 / protection packet
  reviewed as `Partial clue / accepted current PCB2 mapping source; Hall/PWM
  conflicts clarified`. It answers many previously open items and clarifies
  current Hall routing as `IA/IB/IC -> PA0/PA1/PB4`.
- The repo has a 2026-05-19 current PCB2 Hall/PWM no-power strategy review.
  It opens the no-PCB-change path first, but it records only a feasibility
  review direction: current PCB2 PWM/Hall routing is not accepted Packet A
  configuration evidence and software Hall is not hardware validation.
- The repo has a 2026-05-19 current PCB2 Packet A / firmware feasibility
  review. It concludes that the no-PCB-change route remains feasibility only:
  Packet A is not accepted, generated-project trust is not allowed, and
  build-only clearance remains closed.
- The repo has a 2026-05-19 software Hall adapter design review. It defines
  no-power GPIO/EXTI sampling, edge timestamping, valid-state filtering,
  minimal ISR responsibility, MCSDK integration boundaries, and
  `hardware-rework planning` fallback conditions for `PA0/PA1/PB4`.
- The repo has a 2026-05-19 Packet A Board Designer / Board Manager path
  review. It confirms local Workbench external-tool entries, installed Board
  Designer / Board Manager executables, and local Board Designer manual clues
  for custom board creation/import and Board Aggregation for the
  self-developed STDRIVE101 board path, but Packet A still blocked.
- The repo has a 2026-05-19 Packet A Board Designer / Manager GUI-only
  checklist. It tells the user which screenshots to capture, where to save
  them, and when to stop, while keeping Packet A still blocked and no
  generated-project trust.
- The repo has a 2026-05-19 MY_FOC generated project source review. It records
  a real Workbench 6.4.2 generated project as a clue, but quarantines it
  because it is `SIX_STEP`, not FOC. The user's statement that pins can be
  changed is recorded as an editable future route, not as Packet A acceptance.
- The repo has a 2026-05-19 MY_FOC manual FOC edit rollback record. It proves
  a one-field `.stwb6` algorithm edit made Workbench unable to load the file,
  and that Codex restored the external source from backup. It does not prove
  generated source, build readiness, or hardware readiness.

Forbidden current claims:

- MCSDK MotorControl configuration is complete for the competition board.
- A software Hall adapter has been implemented or accepted by MCSDK.
- A generated motor-control project is trusted or ready to build.
- CN8 routing is proven.
- NUCLEO-to-driver-board endpoint routing is proven.
- STDRIVE101 protection paths are proven on this board.
- `PB3` is ready for Hall B.
- `J_HALL` numbering is confirmed.
- Phase/Hall wire-color mapping has been verified on the physical motor.
- The vendor motor parameters are measured project data.
- Workbench captured or accepted the self-made STDRIVE101 driver board.
- Board Designer / Board Manager has created, imported, saved, or accepted the
  project self-developed STDRIVE101 board.
- The GUI-only checklist proves a custom/user board path or accepts Packet A.
- The user-created `MY_FOC` generated project is trusted, buildable for this
  project, FOC-complete, or accepted as Packet A.
- The failed manual `MY_FOC.stwb6` FOC candidate can be used as a valid source,
  regenerated source, or built/flashed without another Packet A review.
- Built-in ST power-board entries such as `EVALSTDRIVE101` or `STEVAL-LVLP01`
  are board-match evidence for the self-developed driver board.
- cannot claim Gate PWM, Motor Profiler, Hall, motor, power-stage, or sensorless behavior is validated.

## Promotion Rules

Before moving from current P2 planning to build-only generated-project work:

1. Packet A must be accepted through `source_packet_review_template_2026-05-14.md`.
2. `evidence_packet_2026-05-14.md` must name the exact accepted Packet A fields.
3. `workflow/evidence_register.md` must state that the result is build-only
   configuration evidence.
4. Packet B/C and PB3/SWO blockers must be copied forward if still unresolved.
5. `python -m unittest discover -s tests` must pass after the updates.

Before moving from P2 to any powered or motor stage:

1. Packet A, Packet B, Packet C, and PB3/SWO status must be accepted where used.
2. No-power continuity / short checks must be recorded in a later hardware-stage artifact.
3. Current-limited bring-up settings, measurement points, stop conditions, and
   rollback image must be written before any powered command.
4. The phase gate must explicitly allow the hardware action.

## Next Smallest Actions

1. Treat the current `MY_FOC` project as a correction target, not as trusted
   generated firmware. The next useful Packet A work is to create or edit a
   no-power Workbench configuration so it is FOC, not `SIX_STEP`, and so
   current sensing, fault input, self-developed STDRIVE101 board context, and
   Hall/PWM route are reviewable. If pins are changed, capture the new matching
   physical route before Packet A acceptance.
2. Use `packet_a_board_designer_manager_gui_checklist_2026-05-19.md`,
   `packet_a_board_designer_manager_path_review_2026-05-19.md`, and
   `packet_a_workbench_asset_probe_2026-05-19.md` to plan the next no-power
   Packet A GUI/documentation check around Board Designer / Board Manager. If
   that path supports a custom/user board, then use
   `packet_a_capture_task_2026-05-18.md` and the 2026-05-16 custom NUCLEO +
   STDRIVE101 capture package to create the new `.stwb6` and selected-field
   screenshots. If Workbench requires a motor entry, use
   `57BLF01_VENDOR_CANDIDATE` only as a supplier-clue label. If the path is
   not reviewable, record Packet A as blocked and choose surrogate build-only
   planning without generated-project trust or separate hardware-rework
   planning.
   Stable fallback phrase: surrogate build-only planning without generated-project trust.
3. Use `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md` to drive the
   current no-PCB-change boundary, and use
   `software_hall_adapter_design_review_2026-05-19.md` as the software Hall
   boundary record. The software path remains no-power design review only; it
   does not authorize generated-project trust or powered work.
   Stable prior decision phrase: deeper software Hall adapter design review.
   Stable phrasing: software Hall adapter design review or hardware-rework planning task.
4. Finish Packet C protection review for `CP`, `STBY`, `SCREF` threshold,
   `NFAULT` break-input handling, and later no-power continuity checks.
5. Use `future_build_only_gate_2026-05-15.md` only after Packet A is accepted.
6. Keep this snapshot current after any evidence upgrade.

## Current Decision

P2 can continue no-power source intake, hardware supplement handoff, Packet A
capture preparation, interface-contract maintenance, and delivery cleanup.
P2 cannot currently trust, generate for use, build, flash, power, or run a
motor-control project.
