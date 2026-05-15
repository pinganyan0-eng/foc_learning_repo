# P2 Source Packet Review Template - 2026-05-14

这个模板用于 Codex 收到 Packet A、Packet B、Packet C 或 `PB3` / SWO 证据后做
无功率审查。先填本模板，再决定是否更新 `evidence_packet_2026-05-14.md`。

它不是接线指导，不是固件生成记录，不是连续性检查，也不是硬件验证。

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## Review Header

| Field | Value |
| --- | --- |
| Review ID | `P2-SOURCE-REVIEW-YYYY-MM-DD-###` |
| Reviewer | Codex |
| Packet type | Packet A / Packet B / Packet C / PB3-SWO |
| Source path | `TBD` |
| Source date/version | `TBD` |
| Source owner | `TBD` |
| Current board match statement | `TBD` |
| Intake checklist used | `source_packet_intake_checklist_2026-05-14.md` |
| User action queue used | `user_action_queue_2026-05-14.md` |
| Initial decision | Accept / Partial clue / Reject |

## Decision Rules

| Decision | Meaning | Allowed update |
| --- | --- | --- |
| Accept | The source type, version, readability, and required fields are enough for the exact packet. | Upgrade only the proven fields in `evidence_packet_2026-05-14.md`. |
| Partial clue | The source is useful but misses version, endpoint, readability, or board-match evidence. | Record as clue only; keep related blockers `Blocked`. |
| Reject | The source is low-resolution, oral-only, old/unknown-version, incomplete, generated without matching config evidence, or the excluded WeChat `netlist_PADS.net`. | Do not upgrade evidence; record why it is not usable. |

## Packet A - MCSDK / MotorControl Configuration Review

| Required field | Evidence observed | Decision |
| --- | --- | --- |
| Real `.stmcx` or MotorControl / Workbench configuration screenshot | `TBD` | Blocked |
| MCU / board context: `STM32G474RETx`, NUCLEO, or intended custom-board context | `TBD` | Blocked |
| TIM1 complementary PWM choices are visible | `TBD` | Blocked |
| Fault input selection is visible, especially `PB12/TIM1_BKIN` if used | `TBD` | Blocked |
| Current-sense mode is visible | `TBD` | Blocked |
| Hall / sensorless mode or explicit absence is visible | `TBD` | Blocked |
| `PA2/PA3` exclusion or documented reuse decision is visible | `TBD` | Blocked |
| `PB3` ownership is visible: SWO or Hall B | `TBD` | Blocked |

Packet A can prove configuration intent only. It cannot prove Gate PWM,
Motor Profiler results, motor behavior, Hall closed-loop behavior, power-stage
readiness, or sensorless readiness.

## Packet B - CN8 / Board Route Review

| Required field | Evidence observed | Decision |
| --- | --- | --- |
| Current-version EDA, schematic PDF, netlist, or high-resolution crop | `TBD` | Blocked |
| Source date/version is readable or recorded | `TBD` | Blocked |
| Current physical board match is stated | `TBD` | Blocked |
| CN8 `NFAULT` mapping is visible | `TBD` | Blocked |
| CN8 PWM input nets are visible | `TBD` | Blocked |
| CN8 current-sense nets are visible | `TBD` | Blocked |
| CN8 Hall nets are visible | `TBD` | Blocked |
| CN8 `3V3` and ground nets are visible | `TBD` | Blocked |
| STM32 endpoints or connector endpoints are visible | `TBD` | Blocked |
| STDRIVE101 endpoints are visible | `TBD` | Blocked |
| Net names, pin names, reference designators, and values are readable | `TBD` | Blocked |

Packet B can upgrade board-route evidence only. It does not authorize continuity
checks, powered testing, Gate PWM output, Motor Profiler, or motor actions.

## Packet C - STDRIVE101 Protection Path Review

| Protection item | Evidence observed | Decision |
| --- | --- | --- |
| `DT/MODE` endpoint and resistor/strap value or ground state | `TBD` | Blocked |
| `nFAULT` route, pull-up voltage, loading, active-low handling, CN8/STM32 endpoint | `TBD` | Blocked |
| `REG12` capacitor values, loads, and return path | `TBD` | Blocked |
| `CP` comparator network, filter components, and threshold inputs | `TBD` | Blocked |
| `SCREF` divider/bias values and VDS monitoring decision | `TBD` | Blocked |
| `VS/VM` relation to MOSFET bus and `24V_FUSED` | `TBD` | Blocked |
| Bootstrap capacitors and diode/component orientation for U/V/W | `TBD` | Blocked |
| `STBY` pull state, MCU route if any, and wake path | `TBD` | Blocked |
| VDS monitoring threshold path and fault-release path | `TBD` | Blocked |

Packet C can upgrade STDRIVE101 protection-path review only when it proves
current-board implementation. ST datasheet facts alone remain device
requirements, not board proof.

## PB3 / SWO Release Review

| Required field | Evidence observed | Decision |
| --- | --- | --- |
| Current `.ioc` no longer owns `PB3` as `SYS_JTDO-SWO`, or release evidence exists | `TBD` | Blocked |
| NUCLEO bridge/manual/source evidence supports the release or isolation decision | `TBD` | Blocked |
| Hall B endpoint is proven by Workbench/CubeMX and board-route evidence | `TBD` | Blocked |

Without this evidence, `PB3` remains a Hall B candidate only.

## Required Output After Review

1. Intake result: Accept / Partial clue / Reject.
2. Exact fields upgraded, if any.
3. Exact blockers that remain `Blocked`.
4. Files updated.
5. Tests run.
6. Vector store rebuild status.

## Forbidden Conclusions

Do not write any of these as positive conclusions from this review:

- MCSDK MotorControl configuration completion unless Packet A proves it.
- CN8 routing proof unless Packet B proves it.
- STDRIVE101 protection-path proof unless Packet C proves it.
- `PB3` Hall readiness unless SWO release plus Hall endpoint evidence proves it.
- 24V readiness, power-stage readiness, Gate PWM readiness, Motor Profiler
  readiness, Hall closed-loop readiness, motor readiness, or sensorless
  readiness.

## Review Record Stub

```text
Review ID:
Packet type:
Source path:
Decision:
Accepted fields:
Rejected or blocked fields:
Evidence packet updates:
Evidence register updates:
Tests:
Vector store:
Safety statement: no 24V, no power-board connection, no motor connection,
no Gate PWM output, no Motor Profiler run, no Hall closed-loop claim,
no sensorless / SMO claim.
```
