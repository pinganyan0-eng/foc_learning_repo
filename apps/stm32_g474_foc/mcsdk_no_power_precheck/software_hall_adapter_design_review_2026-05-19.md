# Software Hall Adapter Design Review - 2026-05-19

This is a P2 no-power software Hall adapter design review for the current
PCB2 Hall route. It is not firmware implementation, not a Workbench project,
not generated source, not a build record, and not hardware validation.

## Gate

| Field | Decision |
| --- | --- |
| Project goal | Review whether current PCB2 Hall inputs can stay on `PA0/PA1/PB4` as a future software Hall adapter concept. |
| Learning goal | Separate GPIO/EXTI sampling feasibility, Hall-state filtering, and MCSDK integration boundaries from real Hall readiness. |
| Scope | No-power design responsibilities, hard stops, evidence limits, and next review path. |
| Forbidden scope | No GUI launch, no source generation, no build, no flash, no 24V, no power-board connection, no motor connection, no Gate PWM output, no Motor Profiler run. |

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop validation.
- No sensorless / SMO claim.
- No generated-project trust.
- No build-only generated-project clearance.

## Inputs Reviewed

| Input | Role in this review |
| --- | --- |
| `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md` | Previous conclusion that the no-PCB-change route remains feasibility only and Packet A is not accepted. |
| `current_pcb2_hall_pwm_strategy_2026-05-19.md` | Current PCB2 route and no-PCB-change default strategy. |
| `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md` | Current PCB2 mapping source: Hall route is `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`. |
| `future_build_only_gate_2026-05-15.md` | Rule that build-only work needs accepted Packet A selected fields first. |

## Current Hall Route

Current PCB2 Hall inputs remain:

```text
J_HALL -> IA/IB/IC -> PA0/PA1/PB4
```

| Hall net | STM32 pin | Candidate no-power use | Current decision |
| --- | --- | --- | --- |
| `IA` / future `HALL_A` | `PA0` | GPIO/EXTI sampling candidate with timestamped edge capture. | Feasibility only. |
| `IB` / future `HALL_B` | `PA1` | GPIO/EXTI sampling candidate with timestamped edge capture. | Feasibility only. |
| `IC` / future `HALL_C` | `PB4` | GPIO/EXTI sampling candidate with timestamped edge capture. | Feasibility only; it is split from the `TIM2` pair. |

Decision: `PA0/PA1/PB4` remains a software Hall adapter design topic only. It
is not cleared as a same-timer hardware Hall interface and does not upgrade
Hall readiness.

## Adapter Responsibilities For A Later Firmware Task

A later implementation task may define a software Hall adapter with these
responsibilities, still under no-power review before any generated project is
trusted:

- configure `PA0/PA1/PB4` as digital Hall inputs through GPIO/EXTI or an
  equivalent no-power configuration;
- timestamp Hall edges with a free-running timer that is not the FOC
  current-loop timer and does not add work to the high-frequency FOC path;
- read a compact three-bit Hall snapshot after an edge instead of relying on a
  same-timer hardware Hall peripheral;
- keep valid-state filtering explicit and treat all results as candidates
  until later physical evidence exists;
- accept only the six normal nonzero, non-all-high Hall states as candidates
  until physical phase/Hall order is proven later;
- reject `000`, `111`, repeated states, and bounce-like transitions that occur
  inside a future documented minimum interval;
- flag suspicious multi-bit transitions for review instead of treating them as
  validated rotor movement;
- keep ISR responsibility minimal: capture timestamp/state and defer decoding,
  logging, JSON formatting, and control decisions to a lower-priority context.
- keep minimal ISR responsibility as a design rule for any later implementation.

This review intentionally does not define function names, buffers, public
runtime APIs, MCSDK hooks, or generated-project edits.

## MCSDK Integration Boundary

The software adapter cannot be treated as Packet A evidence by itself.

Before any generated project is trusted, a later Packet A review must prove how
Workbench / MCSDK can represent or safely isolate the current PCB2 choice:

- current PWM / driver-input route
  `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10`;
- software Hall inputs on `PA0/PA1/PB4`;
- `NFAULT` / break-input policy;
- current-sense mode;
- `PA2/PA3` communication policy;
- `PB3` ownership as current PCB2 `LIN1`, not current PCB2 Hall.

Compile success, if a future generated project ever reaches the build-only
gate, would remain build-only configuration evidence. It would not prove Gate
PWM behavior, Motor Profiler readiness, Hall timing, phase order, current
sensing, power-stage readiness, or motor readiness.

## Hard Stops And Fallback

Open a separate hardware-rework planning task instead of continuing the
software Hall route if any of these are true:

- Workbench / MCSDK requires a same-timer hardware Hall input set for the
  intended generated project path;
- the adapter would require invasive edits inside the high-frequency FOC ISR,
  JEOC path, or generated current-loop timing path;
- the design cannot keep `printf`, `HAL_Delay`, JSON parsing, WebSocket work,
  dynamic allocation, and long blocking logic out of time-critical paths;
- there is no clear build-only verification boundary after Packet A is later
  accepted;
- the project cannot explain how the generated code consumes or ignores the
  software Hall state without making unverified Hall closed-loop claims.

The fallback is hardware-rework planning only. It does not authorize rework,
continuity checks, power-board connection, 24V, Gate PWM, Motor Profiler, motor
connection, Hall closed-loop, or SMO.

## Decision

Decision: `Software Hall adapter remains no-power design review / Packet A not accepted`.

This review advances the no-PCB-change path by defining the future software
Hall adapter responsibilities and hard stops. It does not create an adapter,
does not accept Packet A, and provides no generated-project trust.

This review cannot be used to claim:

- MCSDK MotorControl configuration is not complete;
- no generated-project trust has been granted;
- no build-only generated project is cleared;
- Hall closed-loop behavior is not validated;
- Gate PWM output is not safe or observed;
- Motor Profiler cannot run;
- power-stage readiness, motor readiness, or sensorless readiness exists.
