# 2026-06-01 Software Hall Mixed-Sequence Review

## Scope

- Review item: WP-030, Software Hall adapter processing order.
- User report: the hardware teammate is close to finishing PCB2 soldering on 2026-06-01.
- Hardware status decision: this is a scheduling clue only. It is not populated-board evidence and does not open DMM, firmware, flash, power, motor, Gate PWM, Motor Profiler, or Hall closed-loop work.

## Given Sequence

- Samples: `(1000,100), (1600,100), (2200,110), (2210,010), (3000,111), (3800,011)`.
- Bounce threshold: `50` ticks.

## User Classification

| Sample | Classification | Reason |
| --- | --- | --- |
| `(1000,100)` | Baseline | First valid Hall-like state; store as the trusted baseline and do not count an edge. |
| `(1600,100)` | Repeat | Same as the trusted state; do not count an edge and do not judge direction. |
| `(2200,110)` | Adjacent direction candidate | `100 -> 110` is adjacent in the expected sequence, so it is a forward candidate and may be accepted for this debug trace. |
| `(2210,010)` | Bounce candidate | `dt = 10 < 50`; do not accept it and do not update the trusted state. |
| `(3000,111)` | Illegal state | `111` is rejected before direction or jump classification. |
| `(3800,011)` | Abnormal jump | The last trusted state is still `110`; `110 -> 011` is a non-adjacent legal-state jump, so record abnormal-jump evidence. |

## Review Result

- Result: pass.
- Evidence level: L4 for no-power mixed-sequence transfer of the software Hall adapter processing order.
- Confidence: medium-high for debug-only sequence classification.
- Boundary preserved: the user correctly stated that this proves only offline / debug classification from `PA0/PA1/PB4`, not MCSDK Hall speed / position feedback readiness.

## Boundary Explanation Accepted

The user explicitly kept `direction_candidate` and `speed_candidate` as debug-only candidate quantities. They did not claim these satisfy MCSDK's speed / position feedback contract, timer capture behavior, electrical-angle interpolation, speed filtering, error handling, object-state update rules, or real-time FOC synchronization.

## Not Proven

- No populated-board DMM continuity / short-check table.
- No GPIO / EXTI runtime behavior.
- No STM32 firmware adapter implementation.
- No MCSDK Hall integration or `SpeednPosFdbk`-compatible component.
- No build, flash, Run / Debug, serial log, Motor Profiler, 24V, power-board connection, motor connection, Gate PWM, Hall closed-loop, or powered readiness.

## Next Review

- Before any software Hall firmware adapter implementation, do a no-power pseudocode walkthrough that separates ISR-only capture from low-priority state-machine classification and preserves the MCSDK hard stops.
- For MCSDK concept review, use the PR #5 review item to classify `SPD_GetElAngle(...)`, `SPD_GetAvrgMecSpeedUnit(...)`, raw `PA0/PA1/PB4`, `direction_candidate`, and `speed_candidate` by destination: current loop, speed loop, debug log, or nowhere.
