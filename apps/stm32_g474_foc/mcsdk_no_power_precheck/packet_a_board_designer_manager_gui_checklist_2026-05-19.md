# Packet A Board Designer / Board Manager GUI-Only Checklist - 2026-05-19

This checklist is for a later no-power GUI-only capture. It tells the user
what to open, what to screenshot, and where to stop when checking whether
Board Designer / Board Manager can expose a custom/user board path for the
self-developed STDRIVE101 board.

This file does not launch GUI tools, create a board, save a `.stwb6`, generate
source, build, flash, connect 24V, connect the power board, connect the motor,
output Gate PWM, run Motor Profiler, run Motor Pilot, or validate hardware.

## Gate

| Field | Decision |
| --- | --- |
| Project goal | Prepare the next Packet A GUI-only path check for Board Designer / Board Manager. |
| Learning goal | Capture only what proves a custom/user board path exists, while keeping Packet A still blocked until real source evidence exists. |
| Change scope | Checklist only; no GUI launch in this task. |
| Forbidden scope | No 24V, no power-board connection, no motor connection, No Gate PWM output, No Motor Profiler run, no Motor Pilot, no Generate click, no Flash, no source generation, no build, no `.stwb6` creation. |

## Known Local Paths

Use these paths only for later GUI navigation and screenshots:

- Workbench:
  `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\STMCWB.exe`
- Board Designer:
  `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCBD\STMCBoardDesigner.exe`
- Board Manager:
  `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCBM\STMCBoardManager.exe`

Preferred route: open Workbench and use its external-tool menu to find Board
Designer / Board Manager.

Fallback route: if the Workbench menu path is not visible, open the local
Board Designer or Board Manager executable directly and capture that as the
path evidence.

## Screenshot Save Directory

Save later screenshots under:

`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-19_board_designer_manager_path/screenshots/`

Do not save screenshots elsewhere unless the source-packet review records the
move and path.

Do not save a placeholder or fake project board.

## Required Screenshots

Capture the smallest screen area that still shows the required context.
Stable evidence phrase: custom/import/create board path.
Stable evidence phrase: Board Manager import/list path.

| Screenshot name | Required visible evidence | Stop rule |
| --- | --- | --- |
| `2026-05-19_workbench_external_tools_board_designer_manager.png` | Workbench entry or external-tool menu showing Board Designer / Board Manager. | If Workbench cannot show the menu, take the fallback direct-exe screenshot instead. |
| `2026-05-19_board_designer_launch_or_about.png` | Board Designer title/version/about context or main window. | Do not start a board save flow from this screen unless only inspecting navigation. |
| `2026-05-19_board_designer_custom_import_create.png` | custom/user board, import external board, or create board from scratch entry. | Stop if only stock built-in board selection is available. |
| `2026-05-19_board_designer_power_board_flow.png` | Power Board creation or feature-definition path. | Screenshot only; do not save a placeholder or fake project board. |
| `2026-05-19_board_designer_control_board_flow.png` | Control Board creation or connector/MCU context path. | Screenshot only; do not change installed ST board assets. |
| `2026-05-19_board_designer_inverter_board_flow.png` | Inverter Board creation path. | Screenshot only; do not claim it matches current PCB2. |
| `2026-05-19_board_designer_board_aggregation.png` | Board Aggregation path combining control board and power board. | Stop before saving any invented board. |
| `2026-05-19_board_designer_finalize_save_prompt.png` | Finalize/save prompt or name/PN prompt for a custom board. | Screenshot the prompt, then cancel unless a separate source-capture task authorizes saving a real project board. |
| `2026-05-19_board_manager_import_list_path.png` | Board Manager import/list/manage path for user or custom boards. | Screenshot only; do not import or delete installed assets in this checklist pass. |
| `2026-05-19_blocked_state_if_no_custom_user_path.png` | Any error, forced built-in board selection, missing custom/import entry, or source-generation requirement. | Record blocked; do not improvise. |

## Built-In Board Boundary

The following built-in boards are not project-board proof:

- `EVALSTDRIVE101`
- `STEVAL-LVLP01`
- `EVLDRIVE101-HPD`

If the GUI only exposes those built-in boards and no custom/user board route,
capture the blocked state and stop. Do not use them as substitutes for the
self-developed STDRIVE101 board.

## Hard Stops

Stop immediately and record the screen as blocked if:

- A button or wizard requires `Generate`, source generation, or MCSDK project
  generation before custom/user board path confirmation.
- A workflow asks for Motor Profiler, Motor Pilot, Flash, powered hardware, or
  a live motor step.
- A workflow requires 24V, power-board connection, motor connection, or any
  Gate PWM output.
- A workflow allows only `EVALSTDRIVE101`, `STEVAL-LVLP01`, or
  `EVLDRIVE101-HPD` and no project custom/user board path.
- A workflow would require editing installed MCSDK assets by hand.
- A save prompt would create a placeholder, fake, or unreviewed board as if it
  represented the project PCB2 driver board.

## Acceptance After Later Capture

Screenshots from this checklist can support only a future source-packet review.
They do not accept Packet A by themselves.

To upgrade Packet A later, a separate review must show:

- reviewable custom/user board artifact for the self-developed STDRIVE101
  board;
- project-specific `.stwb6` or accepted Workbench configuration source;
- selected-field screenshots for PWM, current sensing, Hall/sensorless, fault,
  pin usage, UART policy, and `PB3` ownership;
- blockers copied forward for Packet B/C, continuity, protection path, and all
  powered readiness.

## Current Decision

Decision: `GUI-only checklist prepared / Packet A still blocked`.

This checklist adds no generated-project trust, no build-only clearance, no
custom board source, no `.stwb6`, no firmware, no runtime API, no continuity
evidence, no Motor Profiler result, no Hall readiness, no motor readiness, no
power-stage readiness, and no sensorless readiness.

## Safety Boundary

- GUI-only.
- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Motor Pilot run.
- No Generate click.
- No Flash.
- No source generation.
- No build.
- No `.stwb6` creation.
- Packet A still blocked.
- no generated-project trust.
