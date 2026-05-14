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
  review, GUI capture result, and a current P2 证据包。
- Missing evidence: real Workbench `.stmcx`, draft configuration screenshot,
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

The next valid P2 evidence must be one of:

- a real `.stmcx` saved by Motor Control Workbench;
- a screenshot showing the Workbench/CubeMX draft configuration;
- an exact reproducible GUI path plus a captured version/config screen.

Even after that evidence exists, P2 still does not authorize powered hardware
actions.
