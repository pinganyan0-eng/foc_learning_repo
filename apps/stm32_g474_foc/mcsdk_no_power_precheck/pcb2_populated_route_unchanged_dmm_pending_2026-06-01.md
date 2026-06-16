# PCB2 Populated / Route Unchanged / DMM Pending - 2026-06-01

## User Status

The user reported:

```text
PCB2 soldered / in hand: yes
Current route still PA0/PA1/PB4 + PB3=LIN1 + P14/P15=3V3/GND: yes
```

## Decision

`PCB2 populated / current route unchanged / DMM continuity and short-check opened as no-power pending / no powered action`

This updates the previous waiting-hardware state. It does not prove continuity,
no-shorts, GPIO runtime behavior, MCSDK Hall integration, Gate PWM safety, motor
readiness, power-stage readiness, or Hall closed-loop readiness.

## Current Route For No-Power DMM

| Item | Current decision |
| --- | --- |
| Hall route | `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4` |
| `PB3` role | `LIN1`; not current Hall |
| `P14/P15` role | `3V3/GND` |
| Workbench TIM2 Hall | `PA15/PB3/PB10` is generated configuration evidence only, not current PCB2 Hall proof |

## Open No-Power User Action

Fill the DMM table in:

`apps/stm32_g474_foc/mcsdk_no_power_precheck/dmm_continuity_short_check_request_2026-05-22.md`

Required continuity rows:

- `IA/HALL_A -> PA0`
- `IB/HALL_B -> PA1`
- `IC/HALL_C -> PB4`
- `LIN1 -> PB3`
- `P14 -> 3V3`
- `P15 -> GND`
- `nFAULT -> PB12`

Required short-check rows:

- `3V3 -> GND`
- `PA0/PA1/PB4/PB3/PB12 -> 3V3`
- `PA0/PA1/PB4/PB3/PB12 -> GND`
- `IA -> IB`
- `IA -> IC`
- `IB -> IC`

Record raw readings, meter beep state, and photo IDs. Do not infer a pass from
route memory or schematic expectations.

## Safety Boundary

- Board unpowered only.
- Do not connect 24V.
- Do not connect the power board to a powered supply.
- Do not connect the motor.
- Do not flash or Run / Debug firmware.
- Do not output Gate PWM.
- Do not run Motor Profiler or Motor Pilot.
- Do not claim Hall closed-loop, power-stage readiness, or motor readiness.

## Next Decision After DMM Table

1. If continuity matches and no shorts are found, Codex may review the table and
   open the next no-power software Hall adapter code-review plan.
2. If any row mismatches or a short is found, stop software progress and open a
   hardware correction / recheck task.
3. If a reading is ambiguous, request photos and repeat only the unclear rows;
   do not power the board.
