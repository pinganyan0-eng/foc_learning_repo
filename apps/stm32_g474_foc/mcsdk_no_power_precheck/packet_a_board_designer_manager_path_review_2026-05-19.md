# Packet A Board Designer / Board Manager Path Review - 2026-05-19

This is a no-power Packet A path review for MCSDK 6.4.2 Workbench custom-board
support. It reviews local installed-tool paths, Workbench config, built-in board
assets, and local Board Designer documentation only.

It does not launch GUI tools, create a Workbench project, generate source,
build, flash, connect 24V, connect the power board, connect the motor, output
Gate PWM, run Motor Profiler, or validate hardware.

## Gate

| Field | Decision |
| --- | --- |
| Project goal | Decide whether MCSDK 6.4.2 exposes a Board Designer / Board Manager path for a self-developed STDRIVE101 board. |
| Learning goal | Separate a formal custom/user board workflow clue from accepted Packet A evidence. |
| Change scope | Local file and documentation review; status/evidence/test updates only. |
| Forbidden scope | No 24V, no power-board connection, no motor connection, No Gate PWM output, No Motor Profiler run, no Motor Pilot, no source generation, no build, no flash. |

## Inputs Reviewed

- `packet_a_workbench_asset_probe_2026-05-19.md`.
- `packet_a_capture_task_2026-05-18.md`.
- `packet_a_sources/2026-05-16_custom_nucleo_stdrive101/workbench_no_power_configuration_guide_2026-05-16.md`.
- `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\config\wb2mx.properties`.
- `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCBD\`.
- `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCBM\`.
- `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCBD\resources\docs\STMCBD-UM.pdf`.
- `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\assets\hardware\board\`.

## Local Path Findings

| Item | Local evidence | Review decision |
| --- | --- | --- |
| Workbench external tool registry | `wb2mx.properties` lists `editor` label `Board Designer` at `../STMCBD/STMCBoardDesigner.exe` and `manager` label `Board Manager` at `../STMCBM/STMCBoardManager.exe`. | Board Designer / Board Manager path exists as a Workbench-integrated local tool clue. |
| Board Designer executable | `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCBD\STMCBoardDesigner.exe`. | Present; not launched in this review. |
| Board Manager executable | `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCBM\STMCBoardManager.exe`. | Present; not launched in this review. |
| User config override | `wb2mx.properties` says `~/.st_motor_control/wb2mx.properties` can override app config. | Useful configuration clue only; the earlier asset probe did not find that user directory. |
| Board Designer local manual | `STMCBD-UM.pdf` exists and was parsed read-only. | Supports a formal custom-board creation/import/aggregation workflow clue. |
| Built-in STDRIVE101 assets | `EVALSTDRIVE101.json`, `STEVAL-LVLP01.json`, `EVLDRIVE101-HPD.json`. | Built-in ST boards cannot substitute for this project self-developed STDRIVE101 board. |

## Board Designer Manual Findings

The local `STMCBD-UM.pdf` supports these no-power conclusions:

- ST Motor Control Board Designer is intended to create Power, Control, and
  Inverter board descriptions for later use in ST Motor Control Workbench.
- The home workflow includes creating a new board from scratch, combining
  existing power and control boards into an inverter board, and importing an
  external board.
- The board list distinguishes stock boards and custom boards.
- Stock boards are view-only; clone, modify, and delete operations are
  described for custom boards.
- A new board flow exists for Power Board, Control Board, and Inverter Board.
- The Power Board flow requires describing the minimum features needed for
  compatibility with Workbench.
- Board Aggregation selects existing Control and Power boards, defines the
  connection between the control-board connector and the power-board motor
  feature, then finalizes and saves a new inverter board.

These points make the custom/user board route plausible and locally
documented. They do not prove that the self-developed STDRIVE101 board has
already been created, imported, saved, or accepted by Workbench.

## Built-In Board Boundary

The following built-in entries are useful examples only:

- `EVALSTDRIVE101`
- `STEVAL-LVLP01`
- `EVLDRIVE101-HPD`

They remain non-substitutes because the project power stage is a
self-developed STDRIVE101 board. Packet A must not treat those built-in ST
boards as board-match proof for the current PCB2 driver board.

## Decision

Decision: `Board Designer / Board Manager path exists as local documentation
and tool clue / Packet A still blocked`.

Accepted in this review:

- The Workbench config exposes a Board Designer / Board Manager path.
- Board Designer and Board Manager executables are installed locally.
- Local Board Designer documentation describes custom board creation, import,
  clone/modify/delete for custom boards, and board aggregation.
- The route is credible enough to define the next no-power `.stwb6` and
  screenshot capture task.

Still blocked:

- Packet A not accepted.
- No self-developed STDRIVE101 board definition was created, imported, saved,
  or reviewed.
- No project-specific `.stwb6` exists for the current custom board path.
- No selected-field screenshots exist for PWM, current sensing, Hall, fault,
  pin usage, UART, or `PB3` ownership.
- No generated-project trust and no build-only generated-project clearance.
- No firmware, runtime API, MCSDK project, build, flash, continuity evidence,
  Hall readiness, Motor Profiler readiness, motor readiness, power-stage
  readiness, or sensorless readiness is upgraded.

## Next No-Power Capture If Path Is Used

If a later GUI-only task uses this path, it may only do path confirmation and
screenshots. It must not generate source, run Motor Profiler, run Motor Pilot,
flash, or touch hardware.

The next valid Packet A capture should:

1. Open Board Designer / Board Manager only to create or inspect a project
   board definition for the self-developed STDRIVE101 board.
2. Save any tool-created project board source under the Packet A source area
   with a dated source-packet review.
3. Use the existing 2026-05-16 custom NUCLEO + STDRIVE101 capture target for
   the later `.stwb6` and screenshots if Workbench accepts the custom/user
   board.
4. Review the result with `source_packet_review_template_2026-05-14.md`.
5. Keep Packet B/C, current PCB2 `PA0/PA1/PB4` Hall boundary, PWM routing,
   `PB3`, continuity, and powered readiness blockers copied forward.

If Board Designer / Board Manager cannot create or expose a reviewable
custom/user board path for this project, Packet A remains blocked and the next
decision is either surrogate build-only planning without generated-project
trust, or a separate hardware-rework planning task.

## Hard Stops

Stop and record the blocker instead of improvising if:

- Workbench or MCSDK requires selecting `EVALSTDRIVE101`, `STEVAL-LVLP01`, or
  `EVLDRIVE101-HPD` as if it were the project self-developed STDRIVE101 board.
- The tool path requires source generation before a board definition or
  `.stwb6` can be saved.
- The tool path requires powered hardware, Motor Profiler, Motor Pilot, flash,
  24V, motor connection, or any live driver action.
- The tool cannot make a reviewable custom/user board artifact.
- The route cannot preserve a verifiable build-only boundary after Packet A is
  accepted.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Motor Pilot run.
- No source generation.
- No build.
- No flash.
- No Hall closed-loop validation.
- No sensorless / SMO claim.
- no generated-project trust.
