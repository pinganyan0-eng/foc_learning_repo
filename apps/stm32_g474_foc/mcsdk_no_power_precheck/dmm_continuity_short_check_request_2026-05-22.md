# DMM Continuity / Short-Check Request - 2026-05-22

This is the next real-world no-power evidence request before any software Hall
adapter implementation or powered FOC step. It is a measurement template, not a measurement result,
not firmware, not a build record, and not hardware readiness.

## Safety Boundary

- Power off only.
- Do not connect 24V.
- Do not connect the motor.
- Do not power the STDRIVE101 board.
- Do not output Gate PWM.
- Do not run Motor Profiler or Motor Pilot.
- Do not measure live PWM waveforms in this step.

## Route Locked For This Check

| Item | Current decision |
| --- | --- |
| Hall route | `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4` |
| `PB3` role | `LIN1` / low-side PWM driver input, not Hall |
| `P14/P15` role | `3V3/GND` |
| Workbench TIM2 Hall | `PA15/PB3/PB10` is generated configuration evidence only, not current PCB2 Hall proof |

## Continuity Table To Fill

Fill this table from DMM continuity or resistance mode. Record the raw result;
do not infer "pass" from memory.

| Signal | STM32 pin | Expected no-power result | DMM result | Beep? | Note / photo ID |
| --- | --- | --- | --- | --- | --- |
| `IA` / `HALL_A` | `PA0` | Continuous from Hall net to `PA0` endpoint | TBD | TBD | TBD |
| `IB` / `HALL_B` | `PA1` | Continuous from Hall net to `PA1` endpoint | TBD | TBD | TBD |
| `IC` / `HALL_C` | `PB4` | Continuous from Hall net to `PB4` endpoint | TBD | TBD | TBD |
| `LIN1` | `PB3` | Continuous from `LIN1` to `PB3`; not a Hall net | TBD | TBD | TBD |
| `3V3` | `P14` | Continuous to the intended 3.3 V logic rail | TBD | TBD | TBD |
| `GND` | `P15` | Continuous to signal ground | TBD | TBD | TBD |
| `nFAULT` | `PB12` | Continuous from `nFAULT` path to `PB12/TIM1_BKIN` endpoint | TBD | TBD | TBD |

## Short-Check Table To Fill

Use resistance or continuity mode while unpowered. Record the reading or
whether the meter beeps.

| Check | Expected no-power result | DMM result | Beep? | Note / photo ID |
| --- | --- | --- | --- | --- |
| `3V3` to `GND` | No short | TBD | TBD | TBD |
| `PA0` to `3V3` | No direct short | TBD | TBD | TBD |
| `PA0` to `GND` | No direct short | TBD | TBD | TBD |
| `PA1` to `3V3` | No direct short | TBD | TBD | TBD |
| `PA1` to `GND` | No direct short | TBD | TBD | TBD |
| `PB4` to `3V3` | No direct short | TBD | TBD | TBD |
| `PB4` to `GND` | No direct short | TBD | TBD | TBD |
| `PB3` to `3V3` | No direct short | TBD | TBD | TBD |
| `PB3` to `GND` | No direct short | TBD | TBD | TBD |
| `PB12` to `3V3` | No direct short; note pull-up behavior if resistance is not open | TBD | TBD | TBD |
| `PB12` to `GND` | No direct short | TBD | TBD | TBD |
| `IA` to `IB` | No Hall-line short | TBD | TBD | TBD |
| `IA` to `IC` | No Hall-line short | TBD | TBD | TBD |
| `IB` to `IC` | No Hall-line short | TBD | TBD | TBD |

## Acceptance Rule

This request is complete only after the user returns the filled DMM table. Until
then, the project must keep these claims blocked:

- software Hall adapter implementation readiness;
- MCSDK Hall integration;
- Hall closed-loop readiness;
- Gate PWM safety;
- Motor Profiler readiness;
- motor readiness;
- power-stage readiness.

## Board Population Note

If PCB2 is not populated yet, this DMM gate is hardware-side deferred. Deferred
does not mean passed.

Algorithm-side no-power state-machine and test-contract preparation may proceed
while this request is deferred, but firmware implementation, MCSDK hook claims,
build evidence for the adapter, flash, 24V, Gate PWM, motor work, Hall
closed-loop, and powered readiness remain blocked until later hardware evidence
is returned and reviewed.

## Next Decision After The Table

After the filled DMM table is reviewed, choose the next no-power step:

1. If the table is internally consistent and no shorts are found, proceed to
   software Hall adapter interface design and no-power compile boundary.
2. If any continuity mismatch or short appears, stop software work and open a
   hardware correction / recheck task.
3. If results are ambiguous, request photos and repeat only the unclear DMM
   rows; do not power the board.
