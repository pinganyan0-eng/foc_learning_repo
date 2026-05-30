# CN8 / STDRIVE101 Route Review - 2026-05-14

This is a P2 no-power evidence artifact. It records what can be trusted about
the board route and STDRIVE101 protection path before any generated MCSDK
configuration is trusted.

It is not a wiring instruction, not a continuity result, not a generated
firmware result, and not hardware validation.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## Source Policy

Accepted route evidence for this review:

- current-version EDA source;
- current-version schematic PDF;
- current-version netlist;
- current-version high-resolution local schematic crop that clearly shows the
  target net and endpoint pins.

Current low-grade clue only:

- `hardware/schematic/2026-05-09_power_board_schematic_screenshot.jpg`
- `hardware/schematic/2026-05-09_power_board_schematic_screenshot.md`
- `hardware/schematic/2026-05-15_power_board_cn8_stdrive101_schematic_candidate.png`
- `hardware/schematic/2026-05-15_power_board_cn8_stdrive101_schematic_candidate.md`

The 2026-05-15 screenshot is more readable and is preserved as `Partial clue`.
The user confirmed on 2026-05-15 that it matches the current physical power
board and was drawn by the hardware teammate, but it still lacks a formal source
revision/date and STM32-side endpoint mapping. Screenshots can guide what to ask
for next, but they cannot prove final board routing unless the intake
requirements are met.

Explicitly excluded source:

- The WeChat-side `netlist_PADS.net` candidate is not imported and is not used
  as current board evidence.

## Current Evidence State

| Evidence area | Current state | P2 decision |
| --- | --- | --- |
| CN8 route proof | Partial clue. The 2026-05-15 screenshot shows power-board-side CN8 net names, and user confirmed current-board match. No accepted EDA, schematic PDF, netlist, formal source revision/date, or STM32 endpoint mapping exists. | Do not trust that any STM32 pin reaches the intended STDRIVE101 or sensing net. |
| `NFAULT` route | Screenshot-level clue only. The repo has no accepted route proof from STDRIVE101 `nFAULT` to the STM32 break input. | `PB12/TIM1_BKIN` remains a CubeMX draft candidate only. |
| PWM inputs | Screenshot-level clue only. No accepted proof maps HIN/LIN or equivalent STDRIVE101 input nets to STM32 pins. | Do not trust generated TIM1 complementary PWM until board route and `DT/MODE` are proven. |
| Current sense | Screenshot-level clue only. No accepted proof maps `ADC_U/V/W` or shunt/filter endpoints to STM32 ADC/OPAMP pins. | Do not trust current-sense configuration or software limit assumptions. |
| Hall inputs | Screenshot-level clue only. No accepted proof maps Hall nets to STM32 pins, and `PB3` is still blocked by SWO until proven released or isolated. | Do not claim Hall input usability. |
| `3V3` and ground | Screenshot-level clue only. No accepted proof resolves signal ground, power ground, and any single-point connection implementation. | Do not trust board-level return paths from screenshot evidence alone. |
| `DT/MODE` | Screenshot-level clue only. Existing notes say the connection is unclear. | Keep PWM style and MCSDK output mode blocked until accepted route evidence proves the setting. |
| `REG12` / `CP` / `SCREF` | STDRIVE101 datasheet is ingested locally, and screenshot notes list candidate components. Board-level route proof is missing. | Treat datasheet facts as review requirements, not as proof of this board. |
| `VS/VM`, bootstrap, standby, VDS monitoring | Screenshot-level clue only, with no accepted full route proof. | Keep power-stage readiness blocked. |

## Minimum Accepted Packet

Before this review can upgrade any board-route item from missing to proven, the
repo needs one accepted current-version source packet with:

- CN8 pin or connector mapping for `NFAULT`, PWM inputs, current-sense nets,
  Hall nets, `3V3`, and ground;
- STDRIVE101 endpoint mapping for `nFAULT`, input pins, `DT/MODE`, `REG12`,
  `CP`, `SCREF`, `VS/VM`, bootstrap, standby, and VDS monitoring;
- a clear statement that the source matches the current physical board version;
- if the source is a screenshot crop, enough resolution to read all relevant
  net names and component pins.

## Current Decision

P2 may continue written review and GUI/config evidence collection. It may not
claim board-routing proof, STDRIVE101 protection-path proof, generated
MotorControl trust, power-stage readiness, Hall readiness, or sensorless
readiness.
