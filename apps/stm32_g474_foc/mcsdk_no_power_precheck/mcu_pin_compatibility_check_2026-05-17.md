# MCU Pin Compatibility Check - G431RB To G474RE - 2026-05-17

This check compares local MCSDK 6.4.2 MCU assets for the hardware teammate's
`STM32G431RB` pin table against the project target `STM32G474RETx`.

It is a no-power configuration review. It does not prove board routing,
continuity, signal behavior, or power-stage readiness.

## Source Files

| MCU | Local MCSDK asset | Package |
| --- | --- | --- |
| `STM32G431RBTx` | `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\assets\hardware\mcu\STM32G431RBTx.json` | `LQFP64` |
| `STM32G474RETx` | `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\assets\hardware\mcu\STM32G474RETx.json` | `LQFP64` |

## Compared Pin Functions

| Function | Pin | `STM32G431RBTx` local asset | `STM32G474RETx` local asset | Review status |
| --- | --- | --- | --- | --- |
| U high PWM | `PA8` | `TIM1_CH1`, position 42 | `TIM1_CH1`, position 42 | Compatible clue |
| U low PWM | `PB13` | `TIM1_CH1N`, position 35 | `TIM1_CH1N`, position 35 | Compatible clue |
| V high PWM | `PA9` | `TIM1_CH2`, position 43 | `TIM1_CH2`, position 43 | Compatible clue |
| V low PWM | `PB14` | `TIM1_CH2N`, position 36 | `TIM1_CH2N`, position 36 | Compatible clue |
| W high PWM | `PA10` | `TIM1_CH3`, position 44 | `TIM1_CH3`, position 44 | Compatible clue |
| W low PWM | `PB15` | `TIM1_CH3N`, position 37 | `TIM1_CH3N`, position 37 | Compatible clue |
| Fault / break | `PB12` | `TIM1_BKIN`, position 34 | `TIM1_BKIN`, position 34 | Compatible clue |
| Hall A | `PA15` | `TIM2_CH1`, position 51 | `TIM2_CH1`, position 51 | Compatible clue |
| Hall B | `PB3` | `TIM2_CH2` and `SYS_JTDO-SWO`, position 56 | `TIM2_CH2` and `SYS_JTDO-SWO`, position 56 | Compatible clue, still blocked by SWO |
| Hall C | `PB10` | `TIM2_CH3`, position 30 | `TIM2_CH3`, position 30 | Compatible clue |
| VCP TX candidate | `PA2` | `USART2_TX`, `LPUART1_TX`, position 14 | `USART2_TX`, `LPUART1_TX`, position 14 | Compatible clue; keep reserved for VCP policy |
| VCP RX candidate | `PA3` | `USART2_RX`, `LPUART1_RX`, `ADC1_IN4`, position 17 | `USART2_RX`, `LPUART1_RX`, `ADC1_IN4`, position 17 | Compatible clue; OPAMP/VCP conflict still needs policy |

The local asset comparison supports the hardware teammate's statement that the
relevant `STM32G431RB` table rows can be used as candidate clues for
`STM32G474RETx` in this package.

## Remaining Limits

- This check compares MCU pin capability only; it does not prove CN8 board
  routing, STDRIVE101 endpoint wiring, or connector numbering.
- `J_HALL` pin numbering remains uncertain until board source or continuity
  evidence confirms it.
- `PB3` remains blocked for Hall B until SWO release / isolation evidence
  exists.
- The OPAMP2 / `PA3` internal-output approach remains a candidate detail until
  Workbench/CubeMX and firmware configuration prove the intended path.
