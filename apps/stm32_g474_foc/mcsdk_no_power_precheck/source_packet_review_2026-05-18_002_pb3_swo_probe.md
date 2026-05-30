# PB3 / SWO Source Packet Review - 2026-05-18

This is a no-power review of the `PB3` / SWO blocker. It records CubeMX
configuration evidence only. It is not a wiring instruction, not generated
firmware, not a continuity check, and not hardware validation.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
- No source generation, build, flash, or generated motor-control project.

## Review Header

| Field | Value |
| --- | --- |
| Review ID | `P2-SOURCE-REVIEW-2026-05-18-002` |
| Reviewer | Codex |
| Packet type | `PB3-SWO` |
| Source path | `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`; `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/pb3_tim2_ch2_probe_2026-05-18.ioc`; `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-18_cubemx_pb3_current_swo_fullscreen.png`; `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-18_cubemx_pb3_tim2_ch2_probe_fullscreen.png` |
| Source date/version | 2026-05-18 local CubeMX no-power capture; original draft was created 2026-05-14 |
| Source owner | Codex local no-power probe |
| Current board match statement | Original `.ioc` is the existing NUCLEO-G474RE no-power draft; probe `.ioc` is a dated configuration-layer copy only |
| Intake checklist used | `source_packet_intake_checklist_2026-05-14.md` |
| User action queue used | `user_action_queue_2026-05-14.md` |
| Initial decision | `Partial clue` |

## Evidence Observed

| Required field | Evidence observed | Decision |
| --- | --- | --- |
| Current `.ioc` no longer owns `PB3` as `SYS_JTDO-SWO`, or release evidence exists | Original `.ioc` still records `PB3.GPIO_Label=T_SWO` and `PB3.Signal=SYS_JTDO-SWO`; screenshot `2026-05-18_cubemx_pb3_current_swo_fullscreen.png` shows the CubeMX pinout page with `PB3` labeled `T_SWO`. | `Blocked`; current accepted draft still owns `PB3` as SWO. |
| NUCLEO bridge/manual/source evidence supports the release or isolation decision | No NUCLEO solder-bridge, manual-page annotation, board-setting photo, or physical isolation record was provided in this packet. | `Blocked`. |
| Hall B endpoint is proven by Workbench/CubeMX and board-route evidence | Probe `.ioc` changes only the copied file to `PB3.GPIO_Label=HALL_B_PROBE` and `PB3.Signal=TIM2_CH2`; screenshot `2026-05-18_cubemx_pb3_tim2_ch2_probe_fullscreen.png` shows CubeMX can open the probe and display `PB3` as `HALL_B_PROBE`. There is no accepted Workbench Hall assignment and no CN8 / `J_HALL` board-route endpoint proof. | `Partial clue` for configuration-layer feasibility only; Hall B endpoint remains `Blocked`. |

## Decision

Decision: `Partial clue`.

Accepted exact evidence:

- The existing NUCLEO-G474RE no-power draft still records `PB3` as
  `SYS_JTDO-SWO`; therefore SWO ownership remains active in the accepted draft.
- A separate dated probe `.ioc` can be opened in CubeMX with `PB3` relabeled as
  `HALL_B_PROBE` and `PB3.Signal=TIM2_CH2`; this is useful only as a
  configuration-layer clue.

Blocked fields that remain unchanged:

- No NUCLEO SWO release or isolation evidence exists.
- No Workbench / MCSDK Hall B selected-field evidence exists.
- No CN8 / EDA / netlist / `J_HALL` endpoint proof exists.
- `PB3` cannot be registered as Hall-ready.
- Packet A, Packet B/C, generated-project trust, Hall closed-loop, motor,
  power-stage, PWM Gate, Motor Profiler, and sensorless readiness remain
  unchanged.

## Required Follow-Up

Before `PB3` can become more than a Hall B candidate, the repo still needs:

1. NUCLEO SWO release or isolation evidence from board/manual/bridge settings,
   or an accepted current CubeMX/Workbench configuration that removes SWO.
2. Workbench / MCSDK evidence that Hall B is actually assigned to `PB3/TIM2_CH2`.
3. Packet B board-route evidence proving the Hall B net endpoint through CN8 /
   `J_HALL`.

## Review Record Stub

```text
Review ID: P2-SOURCE-REVIEW-2026-05-18-002
Packet type: PB3-SWO
Source path: original .ioc, PB3 TIM2_CH2 probe .ioc, and two CubeMX screenshots
Decision: Partial clue
Accepted fields: current draft still owns PB3 as SYS_JTDO-SWO; probe copy can
show PB3 as TIM2_CH2 / HALL_B_PROBE in CubeMX
Rejected or blocked fields: SWO release/isolation, Hall B endpoint, CN8/J_HALL
mapping, Hall readiness
Evidence packet updates: PB3 status remains blocked with a new configuration
clue
Evidence register updates: EV-2026-05-18-P2-PB3-SWO-PROBE-001
Tests: `python -m unittest discover -s tests` passed, 41 tests OK
Vector store: `python tools\build_vector_store.py` completed, 8029 chunks built
Safety statement: no 24V, no power-board connection, no motor connection,
no Gate PWM output, no Motor Profiler run, no Hall closed-loop claim,
no sensorless / SMO claim.
```
