# Current PCB2 Hall/PWM No-Power Strategy Review - 2026-05-19

This is a P2 no-power strategy review for the current PCB2 control mapping.
It is not a wiring instruction, not a Workbench project, not generated source,
not a build record, and not hardware validation.

## Gate

| Field | Decision |
| --- | --- |
| Project goal | Review whether the current PCB2 PWM and Hall routes can progress first without a PCB change. |
| Learning goal | Separate board-route clues, Packet A / Workbench configuration evidence, and hardware validation. |
| Default route | First review the no-PCB-change path. |
| Change scope | Documentation, P2 evidence governance, and contract tests only. |
| Forbidden scope | No GUI launch, no source generation, no build, no flash, no 24V, no power-board connection, no motor connection, no Gate PWM output, no Motor Profiler run. |

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop validation.
- No SMO / sensorless claim.
- No generated-project trust.

## Source Inputs

| Source | Current use |
| --- | --- |
| `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md` | Accepted current PCB2 mapping source, still only a partial clue. |
| `hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/pcb2_mapping_pin1_protection_note_2026-05-19.md` | Current board-side P1-P15 mapping and later Hall clarification. |
| `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\assets\hardware\mcu\STM32G474RETx.json` | Local MCSDK MCU pin-function clue; not Packet A evidence by itself. |
| `p2_readiness_snapshot_2026-05-15.md` | Current P2 gate decision and generated-project trust boundary. |

## Current PCB2 Routes Under Review

| Signal group | Current PCB2 route | No-power strategy decision |
| --- | --- | --- |
| PWM / driver inputs | `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10` | Current route is under Packet A / firmware feasibility review. It is not accepted as a standard MCSDK TIM1 complementary PWM set. |
| Hall inputs | `J_HALL -> IA/IB/IC -> PA0/PA1/PB4` | Current route is under software Hall feasibility review. It is not a same-timer hardware Hall set. |
| Current sensing | `ADC_U/ADC_V/ADC_W -> PA4/PB0/PA5` | Current-sense route is a source clue only; Workbench selected fields and continuity are still missing. |
| Fault input | `nFAULT -> PB12` | Supports the `PB12/TIM1_BKIN` candidate, but Packet A/C proof and later validation remain missing. |

## Local Pin-Function Clues

Local MCSDK 6.4.2 `STM32G474RETx.json` exposes these relevant functions:

| Pin | Relevant local functions | Strategy implication |
| --- | --- | --- |
| `PA0` | `GPIO_EXTI0`, `TIM2_CH1`, ADC/COMP functions | Can be a Hall input clue, but only one channel of a possible timer set. |
| `PA1` | `GPIO_EXTI1`, `TIM2_CH2`, ADC/OPAMP functions | Can pair with `PA0` for TIM2 timing, but also has current-sense-related functions in older drafts. |
| `PB4` | `GPIO_EXTI4`, `TIM3_CH1`, debug/JTRST-related function | It is not `TIM2_CH3`; current Hall route is split across timers. |
| `PA15/PB3/PB10` | `TIM2_CH1/TIM2_CH2/TIM2_CH3` plus debug/SWO constraints on `PB3` | This remains an alternate hardware Hall-style clue, not current PCB2 Hall routing. |

Because current Hall is `PA0/PA1/PB4`, the project must not claim standard
same-timer hardware Hall readiness. The next no-PCB-change path is a firmware
design review for software Hall sampling/edge handling on `PA0/PA1/PB4`, plus
a Workbench/MCSDK feasibility check for how that state would be consumed.
In this task, software Hall is only a feasibility-review topic.

## Historical Candidates Downgraded

| Historical candidate | New status |
| --- | --- |
| Standard TIM1 complementary PWM draft `PA8/PB13`, `PA9/PB14`, `PA10/PB15` | Historical candidate only. It does not match the current PCB2 P1-P6 mapping and cannot be treated as the current board route. |
| Hardware Hall draft `PA15/PB3/PB10` | Alternate route only. It is not the current PCB2 physical Hall route, and any use of `PB3` as Hall would still need SWO release/isolation and a new accepted route. |
| `PB3` Hall B blocker as the main current-board Hall blocker | Reframed. `PB3` is current PCB2 `LIN1`, not current PCB2 Hall B. `PB3` still needs Packet A timer/pin-function proof as a driver-input pin. |

## Decision Matrix

| Option | Decision | Why |
| --- | --- | --- |
| No PCB change, software Hall review first | Default current path | It preserves current PCB2 and turns the next work into Packet A / firmware feasibility review. |
| Direct MCSDK hardware Hall claim on `PA0/PA1/PB4` | Not allowed | The three Hall inputs are not a normal same-timer three-channel Hall set. |
| Direct generated-project trust | Not allowed | Packet A selected fields are still missing. |
| Hardware rework to timer-compatible Hall pins | Fallback only | Open this only if the no-PCB-change Workbench/firmware review fails. No rework is executed in this task. |
| Powered Hall or motor validation | Not allowed | P2 has no continuity, current-limited bring-up, Gate waveform, Hall powered behavior, or motor evidence. |

## Required Follow-Up

1. Create a no-power Packet A / firmware design review for current PCB2 PWM and
   Hall routing.
2. In that review, check whether Workbench can represent the current driver
   input route and whether generated code can be kept build-only.
3. Separately review a software Hall adapter concept for `PA0/PA1/PB4` without
   claiming hardware Hall readiness.
4. If the review fails, open a separate hardware-rework planning task for a
   timer-compatible Hall and PWM route.

## Evidence Limit

Decision: `No-power strategy review opened / no PCB change first`.

This document can be used to explain why the next step is a Packet A /
firmware strategy review. It cannot be used to claim:

- no MCSDK MotorControl completion;
- no generated-project trust;
- no CN8 routing proof;
- no final STDRIVE101 protection proof;
- no Gate PWM behavior;
- no Motor Profiler readiness;
- no Hall closed-loop behavior;
- no motor readiness;
- no power-stage readiness;
- no sensorless validation.
