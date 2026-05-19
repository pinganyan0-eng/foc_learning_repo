# MCSDK No-Power Configuration Draft

Last updated: 2026-05-19

This is a planning artifact only. It is not a wiring instruction, not generated
firmware, and not hardware validation.

Detailed acceptance rules and hard stops now live in
`pin_config_review_2026-05-14.md`. This draft records choices; the review file
defines what evidence must exist before those choices can be trusted.

## Draft Identity

| Item | Draft Value | P2 Status |
| --- | --- | --- |
| Project root | `apps/stm32_g474_foc/mcsdk_no_power_precheck/` | Created for no-power planning only. |
| MCU | `STM32G474RE` / `STM32G474RETx` | Planning value. Must be confirmed in Workbench/CubeMX. |
| Base board | `NUCLEO-G474RE` for learning workflow | Planning value. Future custom power-board routing remains separate. |
| Motor-control source | MCSDK / Motor Control Workbench | Workbench `.stmcx` not generated in this turn. |
| Toolchain target | VS Code + STM32CubeIDE extension + CubeMX/MCSDK | Existing project policy. |
| Saved CubeMX draft | `mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc` | NUCLEO-G474RE Board Selector draft saved on 2026-05-14. This is not a `.stmcx` and not a MotorControl project. |
| CubeMX GUI capture | `gui_capture_result_2026-05-14.md` and `screenshots/2026-05-14_cubemx_ioc_*.png` | The saved `.ioc` was reopened in CubeMX `Pinout & Configuration`. This is fallback GUI evidence, not MotorControl evidence. |

## Draft Peripheral Policy

| Function | Draft Choice | Policy |
| --- | --- | --- |
| PWM / driver-input route | Current PCB2 mapping under review: `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10` | Source clue only. Needs Packet A / Workbench / firmware feasibility review before any generated-project trust. |
| Historical TIM1 complementary PWM draft | `PA8 / PB13`, `PA9 / PB14`, `PA10 / PB15` as `TIM1_CH1/1N/2/2N/3/3N` | Downgraded to historical candidate only; it does not match current PCB2 P1-P6 mapping. |
| Current sensing | Current PCB2 source clue: `ADC_U/ADC_V/ADC_W -> PA4/PB0/PA5`; mode still TBD | Template only; no ADC/current behavior is validated. |
| Historical U/V/W current inputs | `PA1`, `PA7`, `PB0` as OPAMP/PGA candidates | Downgraded to historical candidate only because current PCB2 uses `PA1` as filtered Hall `IB`. |
| nFAULT / break input | `PB12 / TIM1_BKIN` | Preferred draft candidate. `PC5` is rejected for nFAULT in this draft. |
| Current PCB2 Hall A/B/C | `PA0 / PA1 / PB4` from `IA/IB/IC` | Software Hall feasibility review only. This is not a normal same-timer hardware Hall set and does not upgrade Hall readiness. |
| Historical / alternate Hall A/B/C | `PA15 / PB3 / PB10` as `TIM2_CH1/2/3` candidates | Downgraded to alternate route only. It is not current PCB2 physical Hall routing. |
| FOC debug / gateway UART | Do not reuse P1 `PA2/PA3` by default | Prefer a later separate UART candidate such as `PC10/PC11` if needed. |
| Motor parameters | Template only | Do not enter measured `Rs`, `Ls`, `Ke`, or profiler-derived values in P2. |

## Explicit Conflict Decisions

| Conflict | Decision | Required Later Evidence |
| --- | --- | --- |
| `PC5` as nFAULT | Rejected. It is not the draft break-input pin. | Workbench/CubeMX must keep nFAULT away from `PC5`. |
| `PB12/TIM1_BKIN` as nFAULT | Preferred draft candidate. | Workbench/CubeMX acceptance plus CN8/EDA/netlist proof. |
| `PA2/PA3` as FOC UART | Excluded from default FOC communication draft. | Only revisit if CubeMX/MCSDK proves no OPAMP/PGA conflict. |
| Current PCB2 `PB3` role | `PB3` is current PCB2 `LIN1`, not current PCB2 Hall B. | Packet A must prove whether this route can be represented safely; no Gate PWM output in P2. |
| Alternate `PB3` Hall B versus SWO | Alternate Hall B candidate still conflicts with baseline SWO ownership. | Record SWO release/isolation before any alternate Hall-stage use. |
| Historical `PB14` versus `PA12` V low-side PWM | Previous draft preferred `PB14/TIM1_CH2N`; current PCB2 route review supersedes this as the active route. | Keep as historical context unless a future hardware-rework task reopens standard TIM1 complementary PWM. |

## 2026-05-19 Current PCB2 Strategy Update

`current_pcb2_hall_pwm_strategy_2026-05-19.md` is now the controlling
no-power strategy note for the current PCB2 PWM/Hall mismatch. It sets the
default route to "no PCB change first" and records these constraints:

- current PCB2 PWM / driver inputs are
  `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10`;
- current PCB2 Hall inputs are `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`;
- `PA0/PA1/PB4` must not be treated as a same-timer hardware Hall set;
- software Hall is only a feasibility-review topic, not Hall readiness or
  hardware validation;
- generated-project trust remains `Not allowed` until Packet A selected fields
  are accepted.

## 2026-05-14 Saved Draft Readback

`mcsdk_no_power_nucleo_g474re_draft.ioc` currently records:

- `Mcu.IP0=NUCLEO-G474RE`
- `Mcu.UserName=STM32G474RETx`
- `Mcu.CPN=STM32G474RET6`
- `Mcu.Package=LQFP64`
- `PA13.Signal=SYS_JTMS-SWDIO`
- `PA14.Signal=SYS_JTCK-SWCLK`
- `PA2.Signal=LPUART1_TX`
- `PA3.Signal=LPUART1_RX`
- `PB3.Signal=SYS_JTDO-SWO`
- `PB12.Signal=TIM1_BKIN`
- `PB14.Signal=TIM1_CH2N`

This is enough to preserve the no-power CubeMX pin/config draft. It is not enough
to claim MCSDK MotorControl generation, STDRIVE101 routing, Hall readiness, PWM
Gate readiness, Motor Profiler readiness, or power-stage safety.

## No-Power Acceptance Checks

Before this draft can be treated as P2 configuration evidence, the repo must
contain at least one of:

- real Workbench `.stmcx`;
- Workbench/CubeMX screenshot showing the selected MCU and critical pins;
- exact GUI launch path plus captured version/config screen.

Before any later P3 powered action, the repo must also contain:

- CN8 / schematic PDF / EDA / netlist evidence for nFAULT, PWM, current sense,
  bus-voltage, and Hall signals;
- no-power continuity and no-short check records;
- current-limited power plan, instrument list, stop conditions, and rollback
  firmware path.

## P2 Prohibitions

This draft does not authorize:

- connecting 24V;
- connecting the power board;
- connecting a motor;
- generating Gate PWM to a power stage;
- running Motor Profiler;
- claiming Hall closed-loop or sensorless behavior.
