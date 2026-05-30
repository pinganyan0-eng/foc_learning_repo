# Packet A Workbench Asset Probe - 2026-05-19

This is a local no-power file-level probe for the Packet A custom-board path.
It does not launch GUI tools, generate source, build, flash, or validate
hardware.

## Gate

| Field | Decision |
| --- | --- |
| Project goal | Find whether MC Workbench 6.4.2 exposes a plausible path for a self-developed STDRIVE101 driver board. |
| Learning goal | Separate built-in ST board definitions from a possible custom / user board workflow. |
| Change scope | Read-only local installed-tool and asset inspection. |
| Forbidden scope | No GUI launch, no project creation, no source generation, no build, no flash, no 24V, no power-board connection, no motor connection, no Gate PWM output, no Motor Profiler. |

## Local Paths Checked

| Item | Observed path or result | Decision |
| --- | --- | --- |
| Workbench package | `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB` | Present. |
| Workbench launcher | `STMCWB.exe`, `STMCWB_C.exe`, `wb6.jar` | Present; not launched in this probe. |
| Hardware assets | `STMCWB\assets\hardware\board`, `mcu`, `motor` | Present. |
| Built-in STDRIVE101 power board | `board\power\EVALSTDRIVE101.json` | Built-in ST board only; not project-board proof. |
| Built-in STDRIVE101 power board | `board\power\STEVAL-LVLP01.json` | Built-in ST board only; not project-board proof. |
| Built-in STDRIVE101 inverter board | `board\inverter\EVLDRIVE101-HPD.json` | Built-in ST board only; not project-board proof. |
| Control board | `board\control\NUCLEO-G474RE.json` | Supports the control-board context clue only. |
| User config directory | `C:\Users\gregrg\.st_motor_control` | Not present during this probe. |

## Board Designer / Board Manager Clue

`STMCWB\config\wb2mx.properties` records two external tool entries:

- `Board Designer`: `..\STMCBD\STMCBoardDesigner.exe`
- `Board Manager`: `..\STMCBM\STMCBoardManager.exe`

Those executable files are present:

- `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCBD\STMCBoardDesigner.exe`
- `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCBM\STMCBoardManager.exe`

The same properties file says a user config can exist at
`~/.st_motor_control/wb2mx.properties` and has higher priority than the app
config. That user directory was not present during this probe.

This is a useful clue that Workbench may have a Board Designer / Board Manager
route for user hardware definitions. It is not accepted Packet A evidence yet,
because no user board definition, import result, project-specific `.stwb6`, or
selected-field screenshot was produced.

## Search Result

Targeted text search over the checked Workbench `config`, `assets\config`, and
`assets\hardware` paths found the Board Designer / Board Manager properties
entries and ST built-in board JSON files. It did not find an obvious existing
custom self-developed STDRIVE101 board entry for this project.

The `STMCBD` resources directory contains documentation files including
`STMCBD-UM.pdf`, but this probe did not parse the PDF and did not launch the
tool. Any later use of that tool must be a separate no-power GUI task with
screenshots and source-packet review.

## Current Decision

Decision: `Partial clue / local tool path found / Packet A still blocked`.

Accepted exact clues:

- MCSDK 6.4.2 Workbench hardware assets contain built-in STDRIVE101 board
  definitions.
- Workbench config points to Board Designer and Board Manager tools.
- Board Designer and Board Manager executables are installed locally.

Blocked fields:

- No custom self-developed STDRIVE101 board definition is accepted.
- No project-specific `.stwb6` or legacy `.stmcx` was created.
- No selected-field screenshots exist for PWM, fault, current sensing,
  Hall/sensorless, UART, `PB3`, or driver protection.
- Built-in ST boards such as `EVALSTDRIVE101`, `STEVAL-LVLP01`, and
  `EVLDRIVE101-HPD` cannot be treated as project-board proof.
- Generated-project trust remains `Not allowed`.

## Next Valid Packet A Action

The next Packet A step is a separate no-power task to inspect the Board
Designer / Board Manager path, or official local documentation for that path,
and then save a project-specific board definition plus `.stwb6` and screenshots
only if the tool supports it.

Do not modify the installed MCSDK assets by hand as project evidence. If a
manual JSON workaround is considered later, it needs a separate gate decision
and must remain barred from proving hardware readiness.
