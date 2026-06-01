# 2026-06-01 24V 0.2A static power-on operation sheet

本单用于自研 STDRIVE101 功率板首次 24V/0.2A 限流静态上电。它只验证静态供电是否基本健康，不授权接电机、不授权输出 PWM、不授权放开限流。

## Fixed Boundary

- 功率板单独上电。
- 电机不连接。
- NUCLEO/MCU 驱动线不连接。
- PWM 不输出。
- 示波器不参与本步骤；只使用可调限流电源和万用表。
- 通过本单后，下一步仍只能进入 MCU 连接/空载 PWM/Gate 波形检查计划，不能直接接电机。

## Before Power

| Check | Required state | Record |
| --- | --- | --- |
| Power supply output | Off before wiring | TODO |
| Supply CV setting | 24V | TODO |
| Supply current limit | 0.2A level | TODO |
| Board input wiring | Supply + to board 24V, supply - to board GND | TODO |
| Motor | Not connected | TODO |
| NUCLEO/MCU/PWM lines | Not connected | TODO |
| DMM black probe | Fixed to confirmed GND, preferably CN8 Pin15/GND_SIGNAL or known GND pad | TODO |
| DMM mode | DC voltage | TODO |
| No-power evidence | `experiments/2026-06-01_power_board_no_power_dmm/logs/2026-06-01_hall_control_connector_dmm_check.md` reviewed | TODO |

If any row above is not clearly satisfied, stop here and do not turn on the supply output.

## Power-On Steps

| Step | Action | Expected result | Record |
| --- | --- | --- | --- |
| 1 | Keep supply output off; confirm 24V and 0.2A limit on the supply display. | Settings match this sheet. | TODO |
| 2 | Connect board input 24V/GND only. | No motor, no NUCLEO/MCU/PWM wires attached. | TODO |
| 3 | Turn on supply output and watch CC/CV and input current immediately. | Supply should not enter CC; current should stay below the 0.2A limit and not climb rapidly. | TODO |
| 4 | If Step 3 is stable, record steady input current. | Stable current below limit. | TODO |
| 5 | Measure 5V to GND. | Near 5V and not dropping. | TODO |
| 6 | Measure 3V3 to GND. | Near 3.3V and not dropping. | TODO |
| 7 | Measure REG12 to GND. | Near the STDRIVE101 REG12 target, normally about 12V, and not dropping. | TODO |
| 8 | Measure nFAULT to GND. | Non-fault/high state, expected near 3V3 because the project record shows a 10k pull-up to 3V3. | TODO |
| 9 | Observe smell, sound, smoke, and fast heating around DCDC, STDRIVE101, D6, TVS, MOS, PTC, and bus capacitor without touching unknown-hot parts. | No abnormal smell, sound, smoke, or fast heating. | TODO |
| 10 | Turn off supply output after measurements and wait before handling the board. | Board is no longer powered; do not touch until the bus has fallen from 24V. | TODO |

## Immediate Stop Conditions

出现任一情况立即关闭电源输出，记录现象，不连续重复尝试：

- 电源进入 CC，或输入电流快速顶到 0.2A 限流。
- 冒烟、异味、火花、异响。
- DCDC、STDRIVE101、D6、TVS、MOS、PTC 或母线电容明显快速发热。
- 5V、3V3 或 REG12 明显偏离预期、快速跌落或状态不明。
- nFAULT 为故障/低电平，或状态不明。
- 表笔、夹子、供电线接触不可靠。
- 发现电机、NUCLEO/MCU 或 PWM 线仍连接。

## Measurement Record

| Item | Expected | Actual | Pass/Fail | Note |
| --- | --- | --- | --- | --- |
| Supply mode | CV, not CC | TODO | TODO | TODO |
| Input current | Stable and below 0.2A limit | TODO | TODO | TODO |
| 5V -> GND | Near 5V | TODO | TODO | TODO |
| 3V3 -> GND | Near 3.3V | TODO | TODO | TODO |
| REG12 -> GND | Near REG12 target, normally about 12V | TODO | TODO | TODO |
| nFAULT -> GND | Non-fault/high, expected near 3V3 | TODO | TODO | TODO |
| Abnormal smell/smoke/sound | None | TODO | TODO | TODO |
| Fast heating | None | TODO | TODO | TODO |

## Result Gate

| Gate | Required condition | Record |
| --- | --- | --- |
| Static power result | Pass only if all measurement rows pass and no stop condition occurred | TODO |
| Motor connection | Always No after this sheet | No |
| PWM output | Always No after this sheet | No |
| Next allowed work | If static power passes, plan MCU connection and empty PWM/Gate waveform check separately | TODO |
| If failed | Power off, keep motor/PWM disconnected, return to no-power debug | TODO |

## Notes

- Do not use this sheet to claim the power stage can drive a motor.
- Do not increase current limit during this test.
- Do not retry after a stop condition without a new root-cause note.
