# STM32-Side Signal Contract - 2026-05-15

This is a no-power planning contract for the STM32 side of the future
STDRIVE101 / CN8 interface. It records intended firmware responsibilities and
current blockers. It is not connector routing proof and not hardware
validation.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## Feature Sentence

The STM32 owns future real-time motor-control signals, while this P2 contract
only defines candidate responsibilities and evidence gaps before any generated
MCSDK project is trusted.

## Evidence Classes Used Here

| Class | Meaning | Current use |
| --- | --- | --- |
| Candidate | A planned STM32-side responsibility exists, but source evidence is incomplete. | Allowed for planning language only. |
| Blocked | Required Packet A/B/C evidence is missing. | Do not use for generated-project trust. |
| Partial clue | A screenshot or source gives direction but misses required fields. | Useful for review, not for closure. |
| Proven | Accepted packet proves the exact field. | Not currently used by this contract. |

## Signal Responsibility Contract

| Signal group | Intended STM32-side responsibility | Current candidate or policy | Required evidence before trust | Current status |
| --- | --- | --- | --- | --- |
| TIM1 PWM command outputs for `HINx` / `LINx` or equivalent driver inputs | Generate the input pattern expected by STDRIVE101 and MCSDK. | Must match MCSDK TIM1 output mode and the board's `DT/MODE` strategy. | Packet A MotorControl config plus Packet B STM32 endpoint mapping plus Packet C `DT/MODE` proof. | Blocked. |
| `NFAULT` | Feed STDRIVE101 fault state into the STM32 break/fault path. | Draft candidate remains `PB12/TIM1_BKIN`. | Packet A confirms selected break input; Packet B proves CN8 / MCU endpoint; Packet C proves board-level route, pull-up/loading, and active-low handling. | Blocked. |
| `STBY` | Define whether STM32 controls driver wake/standby or whether the board fixes it. | Unknown. Do not infer wake behavior from future `nFAULT` alone. | Packet B/C source showing `STBY` net, pull state, MCU route if any, and wake assumptions. | Blocked. |
| `DT/MODE` | Determine whether firmware should use ENx/INx style or complementary INHx/INLx style. | Unknown; must be proven before trusting TIM1 output semantics. | Packet C endpoint plus resistor/strap value or ground state. | Blocked. |
| Current-sense ADC / OPAMP inputs | Provide current feedback to MCSDK current-control code. | Must match 3-shunt / OPAMP / ADC mode and avoid silent `PA2/PA3` reuse. | Packet A current-sense selection plus Packet B endpoint mapping for current-sense nets. | Blocked. |
| Hall fallback inputs | Provide future Hall state timing if Hall closed-loop is used later. | `PB3` cannot be claimed for Hall B while SWO owns it. | Packet A Hall assignment plus Packet B endpoint mapping plus NUCLEO/SWO release evidence. | Blocked. |
| `PA2/PA3` debug UART | P1 learning/debug path through NUCLEO VCP only. | Excluded from default FOC communication draft. | Packet A must explicitly prove safe reuse before this policy changes. | Candidate for debug only. |
| `3V3` and `GND_SIGNAL` | Shared logic reference and signal return for later interface checks. | Planning only. Must not be treated as continuity proof. | Packet B source plus later no-power continuity checks in a hardware stage. | Partial clue only. |
| ESP32 gateway interface | Monitoring, forwarding, and alert display outside the real-time control loop. | ESP32 does not own FOC timing, PWM, current-loop, Hall decoding, or protection ISR decisions. | Interface contract and later UART/ESP32 implementation evidence. | Planning policy. |

## Rules Before Any Generated Project Uses This Contract

1. Packet A must prove the MCSDK / MotorControl choices it uses.
2. Packet B must prove the STM32 endpoint mapping for every CN8-facing signal
   that the generated project depends on.
3. Packet C must prove STDRIVE101 `DT/MODE`, `STBY`, `nFAULT`, protection, and
   supply-support paths that affect firmware interpretation.
4. If Packet B/C are still skipped for scheduling, generated-project trust stays
   blocked even if the project can compile.
5. `PB3` remains SWO-owned until release or isolation evidence exists.
6. `PA2/PA3` remain P1 VCP/debug evidence only unless Packet A proves a safe
   FOC communication decision.

## What This Contract Proves

- The project now has a written STM32-side responsibility map for the future
  CN8-facing signals.
- The map separates firmware intent from connector routing and power-board
  proof.
- Packet B/C can remain skipped for scheduling without being silently cleared.

## What This Contract Does Not Prove

- It does not prove CN8 routing.
- It does not prove STDRIVE101 protection-path implementation.
- It does not prove a saved MCSDK MotorControl configuration.
- It does not prove build success, flash success, Gate PWM behavior, Motor
  Profiler readiness, Hall readiness, motor readiness, or sensorless readiness.

## Next Update Trigger

Update this contract only when one of these changes:

- Packet A adds real `.stmcx` or MotorControl configuration evidence.
- Packet B adds accepted STM32 endpoint mapping.
- Packet C adds accepted `DT/MODE`, `STBY`, `nFAULT`, or protection-path proof.
- PB3/SWO release evidence arrives.
- A future build-only generated project needs a precise signal list.
