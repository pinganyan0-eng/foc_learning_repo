# Software Hall Code-Entry Boundary After DMM - 2026-06-19

Decision:
`Software Hall code-entry boundary after DMM summary / PA0-PA1-PB4 debug-only
adapter planning allowed / no firmware implementation / no MCSDK hook / no Hall
readiness`.

This file is a no-power post-DMM boundary review. It does not create STM32
firmware, does not edit generated MCSDK code, does not edit CubeMX or
Workbench, does not flash hardware, and does not run a powered test.

## Current Evidence Now Available

- PCB2 route remains:
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3 = LIN1`; it is not a Hall input.
- `P14/P15 = 3V3/GND`.
- The user-reported no-power DMM summary is recorded in
  `pcb2_no_power_dmm_continuity_short_check_result_2026-06-19.md`.
- The DMM summary reports expected continuity for:
  `CN3_10-PA0`, `CN3_11-PA1`, `CN3_12-PB4`, `CN3_2-PB3`,
  `CN3_14-3V3`, `CN3_15-GND`, and `CN3_13-PB12`.
- The DMM summary reports no rail, signal-to-rail, or Hall-line hard short.
- Raw ohm values were not provided, so this remains a summary-level DMM record.

## What Changed After DMM

Before this result, the immediate real-world blocker was the no-power DMM
table. After this result, the project may move to no-power code-entry planning
for the future software Hall adapter.

This does not mean firmware is allowed yet. It only means the next useful
engineering work is to define the exact first-code boundary and review rules.

## First-Code Shape Allowed Later

If a later task explicitly authorizes a no-power firmware draft, the first
version must remain isolated and debug-only:

```text
PA0/PA1/PB4 raw read
-> EXTI event latch stores raw_state + timestamp + event count only
-> low-priority state machine consumes events
-> debug snapshot exposes counters and candidates
-> no MCSDK speed feedback hook
```

Candidate module names are planning names only:

```text
software_hall_adapter.h/.c
software_hall_debug.h/.c
```

No source files are created by this review.

## Layer Responsibilities

| Layer | Future responsibility | Hard boundary |
| --- | --- | --- |
| GPIO read | Pack `PA0/PA1/PB4` into a 3-bit `raw_state` | Does not decide direction or speed |
| EXTI ISR latch | Store `raw_state`, `timestamp_ticks`, and a lightweight event count | No `printf`, JSON, UART transmit, allocation, or MCSDK calls |
| State machine | Reject `000/111`, repeats, bounce candidates, and abnormal jumps; update direction and speed candidates only | Does not close the speed loop |
| Debug snapshot | Copy stable counters and candidate fields at low rate | Not every-edge streaming and not ISR output |
| MCSDK boundary | Remain read-only / not connected | No writes to `HALL_M1`, speed loop, FOC ISR, or TIM1 PWM |

## State-Machine Contract

The future firmware behavior must stay aligned with the host-side reference
model in `src/software_hall_model.py` and `tests/test_software_hall_model.py`.

Valid states:

```text
001, 010, 011, 100, 101, 110
```

Illegal states:

```text
000, 111
```

Forward candidate sequence:

```text
001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001
```

Reverse candidate sequence:

```text
001 -> 011 -> 010 -> 110 -> 100 -> 101 -> 001
```

Processing order:

1. Read `raw_state`.
2. Reject `000/111`.
3. Treat the first valid state as the baseline only.
4. Treat repeated states as no edge.
5. Treat too-fast transitions as bounce candidates.
6. Count adjacent forward or reverse transitions as candidate edges.
7. Count legal but non-adjacent transitions as abnormal jumps.

Real mechanical direction names still need later powered phase/Hall alignment.
Until then, use only `direction_candidate` and `speed_candidate`.

## Remaining Decisions Before Firmware Draft

| Item | Status after DMM | Required before code |
| --- | --- | --- |
| GPIO input mode | Candidate only | choose pull mode and EXTI trigger policy |
| Timestamp source | Draft only | choose exact isolated timer or approved equivalent |
| Debug output | Draft only | choose low-frequency snapshot route; no ISR printing |
| MCSDK hook | Not allowed | separate interface evidence and rollback plan |
| Build boundary | Existing Debug build-only record is for generated project | rerun only after an authorized no-power draft exists |
| Hardware power | Not allowed | separate powered gate required |

## Prohibited In The Next Step

- Do not edit generated MCSDK files.
- Do not edit CubeMX or Workbench configuration.
- Do not flash or Run / Debug on the board.
- Do not connect 24 V or a motor.
- Do not output Gate PWM.
- Do not run Motor Pilot or Motor Profiler.
- Do not write into `HALL_M1`, `SpeednTorqCtrlM1`, speed PID, FOC ISR, JEOC,
  ADC injected paths, or TIM1 PWM paths.
- Do not treat `speed_candidate` as closed-loop speed feedback.

## Next Allowed Work

The next allowed work is no-power document-side preparation for a future
software Hall adapter draft:

1. Define the exact file list for a debug-only draft.
2. Define the GPIO pull / EXTI trigger policy to review before code.
3. Define the timestamp-source selection criteria.
4. Define the debug snapshot fields and output route.
5. Define the no-power build and rollback checklist for the future draft.

## Not Claimed

- No software Hall adapter implementation is claimed.
- No GPIO/EXTI runtime proof is claimed.
- No MCSDK hook is claimed.
- No Hall closed-loop behavior is claimed.
- No Gate PWM safety is claimed.
- No 24 V or powered behavior is claimed.
- No power-stage readiness, motor readiness, or sensorless validation is
  claimed.
