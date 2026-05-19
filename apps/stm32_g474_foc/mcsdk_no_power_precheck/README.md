# MCSDK No-Power Precheck

This directory is the P2 no-power MCSDK practice area.

It is not a generated MCSDK motor-control project yet. It exists to hold the
planning artifacts that must be checked before any later generated project,
Motor Profiler step, power-board connection, motor connection, or PWM Gate
output.

## Current Status

- Created: 2026-05-14.
- Scope: configuration planning only.
- Existing evidence in this directory: draft configuration, tool probe notes,
  a CubeMX Home screenshot, a CubeMX `.ioc` pinout screenshot, pin/config safety
  review, GUI capture result, a current P2 证据包, source packet intake rules,
  a source packet request pack, a source packet review template, and a user
  action queue, STM32-side signal/build gates, a P2 readiness snapshot, a
  2026-05-16 custom Workbench capture package, 2026-05-17 vendor motor /
  hardware teammate pin-table source clues, a 2026-05-18 Packet A capture
  task package, and a 2026-05-19 Workbench capture attempt stopped on the
  self-made STDRIVE101 power-stage context blocker.
- Missing evidence: accepted final Workbench selected-field screenshots,
  CN8 / EDA / netlist confirmation, no-power continuity checks, and all
  powered hardware behavior evidence.

## Safety Boundary

Forbidden in this directory and this P2 stage:

- no 24V;
- no power-board connection;
- no motor connection;
- no PWM Gate output;
- no Motor Profiler run;
- no Hall closed-loop validation;
- no SMO / sensorless claim;
- no claim that `SET_RPM` controls real motor speed.

## Files

- `config_draft.md`: no-power MCSDK configuration draft and conflict policy.
- `pin_config_review_2026-05-14.md`: next-ring pin/config safety review and
  hard-stop checklist before trusting any generated MCSDK configuration.
- `evidence_packet_2026-05-14.md`: 当前证据等级、仓库库存和信任任何生成
  MCSDK 配置前的阻塞项。
- `source_packet_intake_checklist_2026-05-14.md`: accepted / rejected source
  rules before any missing P2 evidence can be upgraded.
- `source_packet_request_pack_2026-05-14.md`: concrete request pack for the
  next `.stmcx`, MotorControl screenshot, CN8/EDA/netlist, and STDRIVE101
  protection-path handoff.
- `source_packet_review_template_2026-05-14.md`: repeatable review form for
  accepting, downgrading to clue-only, or rejecting Packet A/B/C and PB3/SWO
  evidence before updating the evidence packet.
- `source_packet_review_2026-05-15_001_cn8_stdrive101_schematic_candidate.md`:
  review of the user-provided CN8 / STDRIVE101 schematic screenshot candidate;
  current decision is `Partial clue`.
- `packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`: preserved
  local MCSDK 6 Workbench project candidate.
- `source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`: Packet A review
  of the local `.stwb6`; current decision is `Partial clue`, not build-only
  clearance.
- `packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`: prepared capture
  package for a new project-specific Workbench configuration targeting
  `NUCLEO-G474RE` plus a Custom / Generic STDRIVE101 power stage. It contains a
  GUI guide, no-power motor measurement template, pin assignment table, and
  screenshot inbox. It does not yet contain an accepted `.stwb6`.
- `source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`:
  review of the 2026-05-16 capture package. Current decision is
  `Partial clue / Preparation only`; generated-project trust remains
  `Not allowed`.
- `mcu_pin_compatibility_check_2026-05-17.md`: local MCSDK asset comparison for
  `STM32G431RBTx` versus `STM32G474RETx`. It supports the hardware teammate's
  statement that the compared key rows are pin-function compatible, but it does
  not prove CN8 routing, `J_HALL` numbering, or `PB3` / SWO release.
- `source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`:
  review of the vendor `57BLF01` motor source and hardware teammate
  `STM32G431RB` pin table. Current decision is `Partial clue`; motor values are
  supplier clues, and board-route / Hall connector blockers remain.
- `source_packet_review_2026-05-18_001_motor_wiring_definition.md`: review of
  the user-provided 57BLF01 phase/Hall wire-color definition image. Current
  decision is `Partial clue`; wire colors are candidate clues only and do not
  prove physical harness inspection, Hall powering, phase/Hall alignment, or
  `J_HALL` numbering.
- `packet_a_capture_task_2026-05-18.md`: workflow-only task package for the
  future project-specific Workbench capture. It fixes the `.stwb6` path,
  required screenshots, stop conditions, and field acceptance matrix. It does
  not add a real `.stwb6`, screenshots, generated source, build evidence, or
  hardware validation.
- `source_packet_review_2026-05-19_001_packet_a_workbench_capture_attempt.md`:
  review of the no-power Workbench capture attempt. Current decision is
  `Partial clue / stopped`; Workbench 6.4.2 launches and
  `NUCLEO-G474RE` / `STM32G474RETx` control-board context is visible, but no
  accepted self-made STDRIVE101 power-stage context or selected-field
  screenshots were captured.
- `non_hardware_parallel_track_2026-05-15.md`: no-power plan for temporarily
  skipping Packet B/C scheduling while keeping blockers visible and progressing
  Packet A, STM32-side signal contract, future build-only gate, and delivery
  cleanup.
- `packet_a_local_probe_2026-05-15.md`: local Packet A recheck covering repo
  `.stmcx`, `.stwb6`, screenshots, common user locations, `.stm32cubemx`,
  CubeMX, STM32Cube Repository, Start Menu, and `F:\STMCSDK`. Current result:
  Packet A has a `Partial clue` source candidate.
- `packet_a_capture_checklist_2026-05-15.md`: next acceptable no-power capture
  checklist for `.stmcx`, MotorControl screenshots, or exact GUI path plus
  captured version/config screen.
- `stm32_side_signal_contract_2026-05-15.md`: no-power planning contract for
  future STM32 responsibilities on CN8-facing signals. It separates candidate
  firmware intent from connector routing and hardware proof.
- `future_build_only_gate_2026-05-15.md`: future gate that allows only
  no-power build evidence after Packet A selected fields are accepted; current
  state is still `Not allowed` because Packet A is only `Partial clue`.
- `p2_readiness_snapshot_2026-05-15.md`: current P2 gate decision. It
  consolidates Packet A/B/C, PB3/SWO, signal-contract, and build-only status
  and records that generated-project trust is still `Not allowed`.
- `user_action_queue_2026-05-14.md`: direct user-facing queue for the next
  Packet B board-route source, Packet A MCSDK/MotorControl source, and PB3/SWO
  release evidence.
- `tool_probe_2026-05-14.md`: local tool and GUI evidence gathered for this
  practice turn.
- `workbench_entry_probe_2026-05-14.md`: targeted probe for Workbench launcher,
  `.stmcx`, and installed MCSDK MotorControl package data.
- `gui_capture_result_2026-05-14.md`: records the GUI follow-up attempt,
  screenshots, `.ioc` readback, and the remaining `.stmcx` / MotorControl
  blocker.
- `gui_capture_checklist_2026-05-14.md`: next GUI-only capture checklist.
- `screenshots/2026-05-14_cubemx_home.png`: CubeMX Home launch evidence. This
  is not a saved MCSDK configuration.
- `screenshots/2026-05-14_cubemx_ioc_launch_attempt.png` and
  `screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`: CubeMX opened
  the saved NUCLEO `.ioc` to `Pinout & Configuration`. These are fallback GUI
  evidence, not Workbench `.stmcx` evidence.

## Next Valid Evidence

Use `user_action_queue_2026-05-14.md` and
`source_packet_request_pack_2026-05-14.md` to collect the next valid P2
evidence. Use `source_packet_review_template_2026-05-14.md` to review it before
upgrading any blocker. The next valid packet must be one of:

- a real `.stwb6` saved by MCSDK 6 Workbench, or legacy `.stmcx`;
- a screenshot showing the Workbench/CubeMX draft configuration;
- an exact reproducible GUI path plus a captured version/config screen;
- the 2026-05-16 custom capture package after a Workbench-supported
  custom/user board entry path is found and its real `.stwb6` plus screenshots
  are added and reviewed;
- current-version CN8 / EDA / netlist / high-resolution route evidence;
- board-level STDRIVE101 protection-path source evidence.

Even after that evidence exists, P2 still does not authorize powered hardware
actions.

If the hardware-source branch is skipped for scheduling, use
`non_hardware_parallel_track_2026-05-15.md`. Skipping is not clearance: Packet
B/C blockers stay blocked.

Before claiming readiness for generated-project trust or build-only work, read
`p2_readiness_snapshot_2026-05-15.md`. Before running the next Packet A GUI
capture, read `packet_a_capture_task_2026-05-18.md`.
