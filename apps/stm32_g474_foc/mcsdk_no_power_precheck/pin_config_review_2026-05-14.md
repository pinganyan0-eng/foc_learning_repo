# P2 Pin / Config Safety Review - 2026-05-14

This is the next project ring after basic toolchain familiarity. It turns the
P2 pin/config draft into reviewable acceptance rules before any MCSDK generated
project is trusted.

It is still a no-power artifact. It is not a wiring instruction, not generated
firmware, and not hardware validation.

## Source Set Used

| Source | Repo Evidence | Use |
| --- | --- | --- |
| STM32G474RE datasheet | `materials/raw/st_manuals/st_stm32g474re_datasheet.pdf`; extracted text `materials/extracted/st_manuals/st_stm32g474re_datasheet.txt` | Alternate-function and pin-function checks for `PB12`, `PB14`, `PC5`, `PA2/PA3`, and `PB3`. |
| NUCLEO-G474RE / UM2505 | `materials/raw/st_manuals/st_um2505_nucleo64_mb1367.pdf`; extracted text `materials/extracted/st_manuals/st_um2505_nucleo64_mb1367.txt` | ST-LINK VCP, SWO, Arduino/ST morpho connector, and solder-bridge conflict checks. |
| RM0440 STM32G4 reference manual | `materials/raw/st_manuals/st_rm0440_stm32g4_reference_manual.pdf`; extracted text `materials/extracted/st_manuals/st_rm0440_stm32g4_reference_manual.txt` | TIM break-input and debug/SWO behavior background. |
| STDRIVE101 datasheet | `materials/raw/st_manuals/st_stdrive101_datasheet.pdf`; digest `materials/extracted/st_manuals/st_stdrive101_datasheet_digest.md` | `nFAULT`, `DT/MODE`, `REG12`, `SCREF`, VDS monitoring, UVLO, overcurrent, and thermal protection review. |

Current online official-source spot check on 2026-05-14:

- ST STM32G474RE datasheet page/PDF path remains the official source for the MCU pin tables.
- ST UM2505 NUCLEO-G474RE user-manual page/PDF path remains the official source for NUCLEO connector and VCP/SWO routing.
- ST STDRIVE101 datasheet page/PDF path remains the official source for gate-driver protection behavior.

## Evidence Classes

| Class | Evidence | Required For |
| --- | --- | --- |
| A | Workbench/CubeMX screenshot or real `.stmcx` showing selected MCU and critical pins | Treating the draft as a saved MCSDK/CubeMX configuration. |
| B | NUCLEO connector/solder-bridge evidence from UM2505 plus local board setting record | Trusting a NUCLEO pin path such as VCP or SWO ownership. |
| C | Power-board schematic PDF, EDA source, or netlist proving CN8 routing | Trusting that a STM32 pin reaches the intended STDRIVE101 or sensing net. |
| D | No-power continuity/no-short measurements | Moving from document review toward hardware bring-up. |
| E | Current-limited, instrumented powered logs/waveforms | Any P3 or later power/motor claim. |

P2 may collect A/B/C document evidence. P2 does not collect D/E powered evidence.

## Review Decisions

| Item | Current P2 Decision | Must See Before Trusting | Fail Condition |
| --- | --- | --- | --- |
| `PB12 / TIM1_BKIN` for `nFAULT` | Keep as preferred draft candidate. | A: CubeMX/Workbench accepts `PB12` as TIM1 break input. C: CN8/EDA/netlist proves STDRIVE101 `nFAULT` reaches this STM32 input. STDRIVE101 review confirms open-drain pull-up voltage and active-low fault semantics. | Any config routes `nFAULT` to `PC5` or to a pin without TIM1 break behavior and routing proof. |
| `PC5` as `nFAULT` | Rejected in this draft. | Only reopen with a written exception that resolves OPAMP/VCP conflicts, timer-break behavior, and board routing. | Treating old `PC5` notes as valid without new evidence. |
| `PB14 / TIM1_CH2N` for V low-side PWM | Keep as preferred candidate over `PA12`. | A: CubeMX/Workbench selects `PB14/TIM1_CH2N`. C: CN8/EDA/netlist proves it reaches the intended V low-side gate-drive input. | A generated config silently uses `PA12` or another alternate without board-route proof. |
| `PA2/PA3` for FOC communication | Exclude from default FOC communication draft. P1 VCP remains learning/debug evidence only. | A: CubeMX/Workbench shows OPAMP/PGA and UART can coexist. B: UM2505/VCP solder-bridge setting is recorded. | Reusing P1 VCP pins in MCSDK while current sensing still needs OPAMP/PGA constraints. |
| `PB3` for Hall B | Candidate only if SWO is released or isolated. | A: CubeMX/Workbench assigns Hall B to `PB3/TIM2_CH2`. B: UM2505/SB15 or board setting proves SWO is not also owning PB3. | Claiming Hall B and SWO trace both own PB3. |
| `DT/MODE` and PWM style | Open hardware-review dependency. | C: EDA/netlist proves whether `DT/MODE` is grounded or resistor-set. A: MCSDK PWM/control mode matches the STDRIVE101 input mode. | Generating/trusting TIM1 complementary PWM without knowing whether STDRIVE101 expects ENx/INx or INHx/INLx style inputs. |
| STDRIVE101 protection path | Open hardware-review dependency. | C: EDA/netlist proves `nFAULT`, `REG12`, `CP`, `SCREF`, `VS/VM`, and bootstrap capacitor networks. Future D/E evidence is required before power. | Treating `nFAULT` route alone as enough for power-stage readiness. |

## Minimum Next Evidence Packet

Before this sprint can move beyond P2 written review, collect all of these:

1. Workbench/CubeMX config screenshot or `.stmcx` showing:
   - MCU `STM32G474RETx`;
   - `PB12/TIM1_BKIN`;
   - `PB14/TIM1_CH2N`;
   - `PA2/PA3` not silently reused as FOC UART;
   - Hall `PB3` choice plus SWO decision if Hall is enabled.
2. Board-routing packet:
   - CN8 schematic PDF or EDA/netlist excerpt for `NFAULT`, `HIN/LIN`,
     `ADC_U/V/W`, `IA/IB/IC`, `3V3`, and `GND_SIGNAL`;
   - explicit map from CN8 nets to STM32 pins.
3. STDRIVE101 protection packet:
   - `DT/MODE` network;
   - `nFAULT` pull-up voltage and route;
   - `REG12` capacitor/load;
   - `CP` and `SCREF` networks;
   - statement whether VDS monitoring is enabled or intentionally disabled.

## Hard Stops

Stop the P2-to-P3 transition if any of these remain true:

- `nFAULT` route is not proven from STDRIVE101 pin to STM32 input.
- `PB12/TIM1_BKIN` is not accepted by CubeMX/Workbench.
- PWM low-side choice differs from board routing.
- `DT/MODE` is unknown.
- `PA2/PA3` are reused without OPAMP/PGA conflict proof.
- `PB3` is used for Hall while SWO ownership is still active.
- There is no current-limited, instrumented bring-up plan.

## 2026-05-14 Route Review Update

Route review artifact:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/cn8_stdrive101_route_review_2026-05-14.md`

Current decision:

- The repo has no accepted current EDA source, schematic PDF, netlist, or
  high-resolution route crop for CN8 / STDRIVE101 route proof.
- The existing schematic screenshot remains a low-grade clue only.
- The WeChat-side `netlist_PADS.net` candidate is excluded and is not used as
  current board evidence.
- `PB12/TIM1_BKIN` and `PB14/TIM1_CH2N` stay at draft confidence until both
  Workbench/CubeMX evidence and accepted board-route evidence exist.

## Boundary

No 24V, no power board connection, no motor connection, no Gate PWM output, no
Motor Profiler run, no Hall closed-loop claim, and no sensorless claim are
authorized by this review.
