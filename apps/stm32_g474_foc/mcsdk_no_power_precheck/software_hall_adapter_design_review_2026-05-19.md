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

## 2026-05-21 Route Confirmation Update

User confirmation upgrades this review from open feasibility discussion to the
current no-PCB-change software Hall route decision, still under no-power
boundaries:

- `P14/P15` are confirmed as `3V3/GND`; they are no longer a route-selection
  blocker, although continuity and short checks are still required before P3.
- Current PCB2 Hall route is `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3` is fixed as current PCB2 `LIN1` / low-side PWM driver input, not a
  current Hall candidate.
- MCSDK standard TIM2 Hall `PA15/PB3/PB10` is not the current PCB2 Hall route
  and cannot be used directly as current-board Hall proof.
- The active direction is `software Hall adapter first`; hardware rework is
  only a fallback if later MCSDK integration cannot safely consume or isolate
  this route.

## Current Hall Route

Current PCB2 Hall inputs remain:

```text
J_HALL -> IA/IB/IC -> PA0/PA1/PB4
```

| Hall net | STM32 pin | Candidate no-power use | Current decision |
| --- | --- | --- | --- |
| `IA` / future `HALL_A` | `PA0` | GPIO/EXTI sampling candidate with timestamped edge capture. | Current software Hall route for no-power adapter planning only. |
| `IB` / future `HALL_B` | `PA1` | GPIO/EXTI sampling candidate with timestamped edge capture. | Current software Hall route for no-power adapter planning only. |
| `IC` / future `HALL_C` | `PB4` | GPIO/EXTI sampling candidate with timestamped edge capture. | Current software Hall route for no-power adapter planning only; it is split from the `TIM2` pair. |

Decision: `Software Hall route confirmed for no-power adapter planning / no
firmware implementation / no Hall readiness`. `PA0/PA1/PB4` is not cleared as a
same-timer hardware Hall interface and does not upgrade Hall readiness.

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
- do not run `printf`, JSON formatting/parsing, blocking delay, dynamic
  allocation, or long control decisions inside the EXTI/timer ISR.
- keep minimal ISR responsibility as a design rule for any later implementation.

This review intentionally does not define function names, buffers, public
runtime APIs, MCSDK hooks, or generated-project edits.

## 2026-05-22 Algorithm-Side Preparation Update

Added:
`software_hall_no_power_algorithm_prep_2026-05-22.md`.

Decision:
`Algorithm-side no-power preparation / no firmware implementation / no Hall readiness`.

The new artifact is allowed while PCB2 is unpopulated because it is only a
state-machine and test-contract preparation record. The DMM continuity /
short-check gate is hardware-side deferred, not passed, and still blocks any
firmware implementation, MCSDK hook, powered action, or Hall-readiness claim.

It locks the algorithm exercise contract:

- valid state candidates are `001`, `010`, `011`, `100`, `101`, and `110`;
- `000` and `111` are illegal;
- repeated states do not count as new accepted edges;
- non-adjacent jumps are abnormal and are not normal rotor movement;
- candidate forward sequence is
  `001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001`;
- candidate reverse sequence is
  `001 -> 011 -> 010 -> 110 -> 100 -> 101 -> 001`;
- low-frequency debug observables include raw/accepted state, edge count,
  illegal count, abnormal-jump count, repeat count, bounce-candidate count,
  edge delta, direction candidate, and speed candidate.

## MCSDK Integration Boundary

The software adapter cannot be treated as Packet A evidence by itself.

Before any generated project is trusted, a later Packet A review must prove how
Workbench / MCSDK can represent or safely isolate the current PCB2 choice:

- current PWM / driver-input route
  `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10`;
- software Hall inputs on `PA0/PA1/PB4`;
- `P14/P15` as confirmed `3V3/GND` rail/return pins, not Hall blockers;
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

Decision: `Software Hall route confirmed for no-power adapter planning / no firmware implementation / no Hall readiness`.

Historical 2026-05-19 decision retained for traceability:
`Software Hall adapter remains no-power design review / Packet A not accepted`.

This review advances the no-PCB-change path by defining the future software
Hall adapter responsibilities and hard stops. It does not create an adapter,
does not edit firmware, does not define runtime APIs, and provides no
current-board Hall readiness.

This review cannot be used to claim:

- MCSDK MotorControl configuration is not complete;
- no generated-project trust has been granted;
- no build-only generated project is cleared;
- Hall closed-loop behavior is not validated;
- Gate PWM output is not safe or observed;
- Motor Profiler cannot run;
- power-stage readiness, motor readiness, or sensorless readiness exists.
