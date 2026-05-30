# Current PCB2 Packet A / Firmware Feasibility Review - 2026-05-19

This is a P2 no-power review of whether the current PCB2 route can progress
without changing the PCB. It is not a Workbench project, not generated source,
not firmware implementation, not a build record, and not hardware validation.

## Gate

| Field | Decision |
| --- | --- |
| Project goal | Decide whether the current PCB2 route is ready for Packet A selected-field capture or only for further firmware feasibility work. |
| Learning goal | Understand why board-route clues are not the same as MCSDK / Workbench configuration evidence. |
| Scope | File-level pin-function review, firmware feasibility boundaries, and evidence-governance updates. |
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
- No build-only generated-project clearance.

## Inputs Reviewed

| Input | Role in this review |
| --- | --- |
| `current_pcb2_hall_pwm_strategy_2026-05-19.md` | Previous no-PCB-change strategy note. |
| `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md` | Current PCB2 source mapping and Hall clarification. |
| Local MCSDK `STM32G474RETx.json` | Pin-function clue for `PA15/PB3/PB10/PA8/PA9/PA10` and `PA0/PA1/PB4`. |
| `future_build_only_gate_2026-05-15.md` | Rule that build-only work needs accepted Packet A first. |

## 2026-05-21 Route Confirmation Update

User confirmed `P14/P15=3V3/GND`, `PB3=LIN1`, and
`HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`. This confirms the current
no-PCB-change software Hall route for later adapter design only. It does not
implement the adapter, prove MCSDK integration, or upgrade Hall readiness.

## PWM / Driver-Input Feasibility

Current PCB2 routes driver inputs as:

```text
HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10
```

Local pin-function clues show:

| Current PCB2 signal | STM32 pin | Relevant local function clue | Review decision |
| --- | --- | --- | --- |
| `HIN1` | `PA15` | `TIM2_CH1`, `TIM1_BKIN`, `TIM8_CH1` | Not accepted as `TIM1_CH1`. |
| `LIN1` | `PB3` | `TIM2_CH2`, `TIM8_CH1N`, `SYS_JTDO-SWO` | Not accepted as standard `TIM1_CH1N`; also needs Packet A proof because it is current PCB2 `LIN1`. |
| `HIN2` | `PB10` | `TIM2_CH3`, `TIM1_BKIN` | Not accepted as `TIM1_CH2`. |
| `LIN2` | `PA8` | `TIM1_CH1` | Timer-capable clue, but it is not a matched low-side partner in the old TIM1 draft. |
| `HIN3` | `PA9` | `TIM1_CH2`, `TIM2_CH3` | Timer-capable clue, but current signal role needs Packet A proof. |
| `LIN3` | `PA10` | `TIM1_CH3`, `TIM2_CH4` | Timer-capable clue, but current signal role needs Packet A proof. |

Decision: current PCB2 PWM / driver-input route is not cleared for a standard
MCSDK TIM1 complementary PWM selected-field claim. Workbench must explicitly
prove any accepted representation. Until then, generated-project trust remains
`Not allowed`.

Summary: current PCB2 PWM is not cleared as a standard MCSDK TIM1 complementary PWM route.

## Hall Feasibility

Current PCB2 routes Hall as:

```text
J_HALL -> IA/IB/IC -> PA0/PA1/PB4
```

Local pin-function clues show:

| Hall signal | STM32 pin | Relevant local function clue | Review decision |
| --- | --- | --- | --- |
| `HALL_A` / `IA` | `PA0` | `GPIO_EXTI0`, `TIM2_CH1` | Candidate input for software Hall review only. |
| `HALL_B` / `IB` | `PA1` | `GPIO_EXTI1`, `TIM2_CH2` | Candidate input for software Hall review only. |
| `HALL_C` / `IC` | `PB4` | `GPIO_EXTI4`, `TIM3_CH1` | Candidate input for software Hall review only; it is split from TIM2. |

Decision: `PA0/PA1/PB4` is not cleared as a same-timer hardware Hall interface.
The no-PCB-change software Hall route is now confirmed for adapter planning:
a later design review may define minimal EXTI/GPIO sampling, timestamping,
valid-state filtering, and MCSDK integration boundaries. This task does not
implement that adapter and does not upgrade Hall readiness.

## Packet A Decision

| Question | Current answer |
| --- | --- |
| Can Packet A be accepted now? | Selected Workbench fields are accepted by the later 2026-05-21 generated-source review, but not as current PCB2 Hall proof. |
| Can build-only generated-project work open now? | Source gate is open after the 2026-05-21 review, but CLI build tools are still missing and any build remains no-power compile evidence only. |
| Can current PCB2 continue without PCB change? | Yes, as the software Hall adapter priority route for no-power design only, not as Hall readiness. |
| Is hardware rework required now? | Not decided. Rework is a fallback if Workbench/firmware feasibility fails. |

## Firmware Review Boundaries For A Later Task

A later no-power firmware design review may propose these responsibilities:

- sample `PA0/PA1/PB4` through GPIO/EXTI or equivalent no-power configuration;
- timestamp Hall edges with a timer that is not part of the FOC current loop;
- reject invalid Hall states and repeated bounce-like transitions;
- keep high-frequency ISR work minimal;
- define an MCSDK integration boundary before any generated project is trusted.

That later review must still avoid `printf`, `HAL_Delay`, JSON parsing,
WebSocket work, dynamic allocation, or long blocking logic in any future
high-frequency motor-control path.

## Decision

Decision: `Software Hall route confirmed for no-power adapter planning / no firmware implementation / no Hall readiness`.

Historical 2026-05-19 decision retained for traceability:
`No-PCB-change route remains feasibility only / Packet A not accepted`.

This review narrows the next step from "can we use the current mapping?" to
"which no-power firmware or Workbench evidence would be needed to keep the
current PCB2 without rework?" It does not authorize:

- no GUI launch;
- no source generation;
- no build-only generated project;
- no flash;
- no Gate PWM output;
- no Motor Profiler run;
- no Hall closed-loop validation;
- no motor readiness;
- no power-stage readiness;
- no sensorless validation.
