# Pin Assignment Table - Custom NUCLEO + STDRIVE101 - 2026-05-16

This table is a planning and review artifact for Packet A. It does not prove
board routing, continuity, power-stage readiness, or signal behavior.

Status values:

- `Accepted`: visible in accepted source and not hardware-dependent.
- `Candidate`: planned or visible in a draft, but still needs another source.
- `Blocked`: cannot be used until a named conflict or missing source is fixed.
- `Rejected`: explicitly excluded from the current draft.

No row may be promoted to `Accepted` for board routing without Packet B/C
source evidence.

## 2026-05-17 Hardware Teammate Pin Table Clue

New source clue:
`hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.pdf`.

Extracted note:
`hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.md`.

Review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`.

MCU cross-check:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/mcu_pin_compatibility_check_2026-05-17.md`.

This source improves the candidate map, especially for `PA8/PB13/PA9/PB14/PA10/PB15`,
`PB12/TIM1_BKIN`, `PA1/PA7/PB0` current-sense candidates, `PA15/PB3/PB10`
Hall candidates, `PA2/PA3` VCP policy, `PB3` SWO conflict, `3V3`, and
`GND_SIGNAL`.

The G431-to-G474 MCU pin-function concern is reduced because the local MCSDK
assets for `STM32G431RBTx` and `STM32G474RETx` both expose the compared key
TIM1, TIM2, USART, and OPAMP-capable rows on the same LQFP64 pin positions.

It still does not promote any row to `Accepted` because:

- the user warned that `J_HALL` pin numbering is uncertain;
- CN8 endpoint claims still need current board EDA, schematic PDF, netlist, or
  high-resolution route proof;
- `PB3` remains blocked by SWO until release / isolation evidence exists.

## Assignment Table

| Function | Workbench selection | STM32 AF / signal | NUCLEO header / connection | CN8 / power-board net | Evidence source | Status |
| --- | --- | --- | --- | --- | --- | --- |
| U high PWM | TIM1 high-side PWM | `PA8 / TIM1_CH1` | TBD by NUCLEO header review | HIN/LIN mapping TBD | `config_draft.md` candidate only | Candidate |
| U low PWM | TIM1 low-side PWM | `PB13 / TIM1_CH1N` | TBD by NUCLEO header review | HIN/LIN mapping TBD | `config_draft.md` candidate only | Candidate |
| V high PWM | TIM1 high-side PWM | `PA9 / TIM1_CH2` | TBD by NUCLEO header review | HIN/LIN mapping TBD | `config_draft.md` candidate only | Candidate |
| V low PWM | TIM1 low-side PWM | `PB14 / TIM1_CH2N` | TBD by NUCLEO header review | HIN/LIN mapping TBD | saved CubeMX draft plus `config_draft.md` | Candidate |
| W high PWM | TIM1 high-side PWM | `PA10 / TIM1_CH3` | TBD by NUCLEO header review | HIN/LIN mapping TBD | `config_draft.md` candidate only | Candidate |
| W low PWM | TIM1 low-side PWM | `PB15 / TIM1_CH3N` | TBD by NUCLEO header review | HIN/LIN mapping TBD | `config_draft.md` candidate only | Candidate |
| Fault / break input | Break / fault input | `PB12 / TIM1_BKIN` | TBD by NUCLEO header review | `NFAULT` endpoint TBD | saved CubeMX draft plus `pin_config_review_2026-05-14.md` | Candidate |
| Current U | 3-shunt internal amplification | `PA1` OPAMP/PGA candidate | TBD by NUCLEO header review | current-sense net TBD | `config_draft.md` candidate only | Candidate |
| Current V | 3-shunt internal amplification | `PA7` OPAMP/PGA candidate | TBD by NUCLEO header review | current-sense net TBD | `config_draft.md` candidate only | Candidate |
| Current W | 3-shunt internal amplification | `PB0` OPAMP/PGA candidate | TBD by NUCLEO header review | current-sense net TBD | `config_draft.md` candidate only | Candidate |
| Hall A | Hall sensor A | `PA15 / TIM2_CH1` candidate | TBD by NUCLEO header review | Hall net TBD | `config_draft.md` candidate only | Candidate |
| Hall B | Hall sensor B | `PB3 / TIM2_CH2` candidate | SWO currently owns `PB3` | Hall net TBD | saved CubeMX draft shows `PB3.Signal=SYS_JTDO-SWO` | Blocked |
| Hall C | Hall sensor C | `PB10 / TIM2_CH3` candidate | TBD by NUCLEO header review | Hall net TBD | `config_draft.md` candidate only | Candidate |
| P1 VCP TX | Keep for NUCLEO debug/VCP | `PA2 / LPUART1_TX` | ST-LINK VCP path | Not a FOC UART net | saved CubeMX draft | Candidate |
| P1 VCP RX | Keep for NUCLEO debug/VCP | `PA3 / LPUART1_RX` | ST-LINK VCP path | Not a FOC UART net | saved CubeMX draft | Candidate |
| Default FOC UART on PA2/PA3 | Excluded | `PA2/PA3` | ST-LINK VCP path | N/A | `pin_config_review_2026-05-14.md` | Rejected |
| SWO ownership | SWO currently active | `PB3 / SYS_JTDO-SWO` | ST-LINK SWO path | Conflicts with Hall B | saved CubeMX draft | Blocked |
| 3V3 reference | Board supply reference only | `3V3` | NUCLEO 3V3 source TBD | `3V3` | schematic screenshot clue only | Blocked |
| Signal ground | Common signal ground only | `GND` | NUCLEO ground TBD | `GND_SIGNAL` | schematic screenshot clue only | Blocked |
| STBY | TBD | TBD | TBD | `STBY` endpoint TBD | not proven | Blocked |
| DT/MODE | Hardware strap / mode TBD | TBD | TBD | `DT/MODE` endpoint TBD | not proven | Blocked |

## Required Evidence Before Promotion

| Field group | Required next evidence |
| --- | --- |
| Workbench selections | New `.stwb6` plus screenshots from this directory. |
| NUCLEO header / connection | UM2505 / board source review or clear CubeMX/NUCLEO mapping. |
| CN8 / power-board net | Current-version EDA, schematic PDF, netlist, or high-resolution route evidence. |
| `PB3` Hall B | SWO release / isolation evidence plus Workbench and board-route Hall proof. |
| `DT/MODE` / `STBY` | Board-level endpoint proof from accepted hardware source. |

## Current Decision

This table is ready for Packet A capture, but no selected field is upgraded by
the table alone.
