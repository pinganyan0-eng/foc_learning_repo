# Hardware Teammate Pin Assignment Source - STM32G431RB - 2026-05-17

This note records a PDF pin-assignment table provided by the hardware teammate.
It is useful as a structured source clue, but it is not accepted board-routing
proof by itself.

Source PDF:
`hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.pdf`

## Source Metadata

| Field | Value |
| --- | --- |
| Source title in PDF | `STM32G431RB NUCLEO - BLDC power board pin assignment table` |
| Target device in PDF | `STM32G431RB (LQFP-64) on NUCLEO-G431RB` |
| Project target | `STM32G474RETx` / `NUCLEO-G474RE` |
| Driver chip in PDF | `STDRIVE101` |
| Current sensing in PDF | 3-shunt + internal OPAMP |
| Provided by | User, from hardware teammate |
| User caveat | Not guaranteed 100% correct; `J_HALL` pin numbering is uncertain. |
| Hardware teammate follow-up | G431 and G474 pins are stated to be the same for this table. |
| Local cross-check | `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcu_pin_compatibility_check_2026-05-17.md` confirms the key rows against local MCSDK 6.4.2 `STM32G431RBTx.json` and `STM32G474RETx.json` assets. |
| Review status | Partial clue only |

## Extracted Pin Clues

| Function | PDF mapping | PDF status | Repo review |
| --- | --- | --- | --- |
| U high PWM | `HIN1`, `PA8 / TIM1_CH1`, `CN8-P1` | Candidate | Candidate only. |
| U low PWM | `LIN1`, `PB13 / TIM1_CH1N`, `CN8-P2` | Candidate | Candidate only. |
| V high PWM | `HIN2`, `PA9 / TIM1_CH2`, `CN8-P3` | Candidate | Candidate only. |
| V low PWM | `LIN2`, `PB14 / TIM1_CH2N`, `CN8-P4` | Candidate | Candidate only. |
| W high PWM | `HIN3`, `PA10 / TIM1_CH3`, `CN8-P5` | Candidate | Candidate only. |
| W low PWM | `LIN3`, `PB15 / TIM1_CH3N`, `CN8-P6` | Candidate | Candidate only. |
| Fault / break | `FAULT`, `PB12 / TIM1_BKIN`, `CN8-P12` | Candidate | Candidate only; still needs current board route proof. |
| U current | `IA`, `PA1 -> OPAMP1`, `PA0 -> ADC1_IN1`, `CN8-P9` | Candidate | Candidate only. |
| V current | `IB`, `PA7 -> OPAMP2`, internal output to `ADC1_IN4`, `CN8-P10` | Blocked | Blocked by `PA3` VCP / OPAMP2 output conflict unless internal OPAMP output is proven. |
| W current | `IC`, `PB0 -> OPAMP3`, `PB1 -> ADC1_IN12`, `CN8-P11` | Candidate | Candidate only. |
| U phase voltage | `ADC_U`, `PA4 / ADC1_IN17`, `CN8-P7` | Candidate | Candidate only. |
| V phase voltage | `ADC_V`, `PA6 / ADC1_IN7`, `CN8-P8` | Candidate | Candidate only. |
| Hall A | `HALL_A`, `PA15 / TIM2_CH1`, `J_HALL-P3` | Candidate | Candidate only; `J_HALL` pin number uncertain. |
| Hall B | `HALL_B`, `PB3 / TIM2_CH2`, `J_HALL-P4` | Blocked | Blocked while SWO owns `PB3`; `J_HALL` pin number uncertain. |
| Hall C | `HALL_C`, `PB10 / TIM2_CH3`, `J_HALL-P5` | Candidate | Candidate only; `J_HALL` pin number uncertain. |
| NUCLEO VCP TX | `PA2 / USART2_TX`, not connected to CN8 | Blocked | Keep out of FOC UART by default. |
| NUCLEO VCP RX | `PA3 / USART2_RX`, not connected to CN8 | Blocked | Keep for VCP; conflicts with OPAMP2 external output. |
| PB3 / SWO | `PB3 / SWO`, CN5-D3 | Blocked | SWO release / isolation evidence required before Hall B use. |
| 3V3 | `CN4-3V3`, `CN8-P15` | Candidate | Candidate only. |
| GND_SIGNAL | `CN4-GND`, `CN5-GND`, `J_HALL-GND`, `R_GND_ISO` | Candidate | Candidate only. |

## Key Risks

- The PDF is for `STM32G431RB`, while the project target remains
  `STM32G474RETx`; however, the hardware teammate states the relevant pins are
  the same, and the local MCSDK asset cross-check confirms the key TIM1, TIM2,
  USART, and OPAMP-capable rows used by this table.
- The PDF contains CN8 and J_HALL pin numbers, but user explicitly warned that
  `J_HALL` numbering is not certain.
- Rows that mention CN8 networks are not accepted CN8 proof until the current
  board EDA, schematic PDF, netlist, or high-resolution route evidence confirms
  board revision and endpoints.
- The `PA3` / OPAMP2 internal-output strategy is a candidate firmware detail,
  not a Workbench-supported or hardware-validated fact yet.
- The `PB3` Hall B path remains blocked until SWO release / isolation evidence
  and Hall route evidence exist.

## Current Decision

This PDF improves the candidate pin map and gives a useful review target for
Workbench / CubeMX. The G431-to-G474 MCU pin-function concern is reduced by the
local cross-check, but CN8 routing, `J_HALL` numbering, `PB3` / SWO release,
and OPAMP/VCP policy still need separate evidence. It does not authorize
generated-project trust, build-only work, flashing, 24V, power-board
connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
sensorless / SMO claims.
