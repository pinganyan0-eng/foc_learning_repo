# 2026-06-01 24V 0.2A static power-on operation sheet

本单用于自研 STDRIVE101 功率板首次 24V/0.2A 限流静态上电。它只验证静态供电是否基本健康，不授权接电机、不授权输出 PWM、不授权放开限流。

## Execution Record

| Item | Record |
| --- | --- |
| Execution date | 2026-06-05 |
| Power supply | 汉晟普源 HSPY-30-05 |
| Operator-reported result | Static 24V/0.2A limited power-on normal |
| Evidence source | User-reported bench measurements in Codex chat |
| Evidence boundary | No motor/PWM/MCU drive authorization; no oscilloscope Gate waveform evidence yet |

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
| Power supply output | Off before wiring | User confirmed setup before power-on. |
| Supply CV setting | 24V | 24V target on HSPY-30-05. |
| Supply current limit | 0.2A level | 0.2A level. |
| Board input wiring | Supply + to board 24V, supply - to board GND | Board input 24V/GND only per static-test boundary. |
| Motor | Not connected | Not connected per static-test boundary. |
| NUCLEO/MCU/PWM lines | Not connected | Not connected per static-test boundary. |
| DMM black probe | Fixed to confirmed GND, preferably CN8 Pin15/GND_SIGNAL or known GND pad | DMM readings reported relative to GND. |
| DMM mode | DC voltage | DC voltage readings reported. |
| No-power evidence | `experiments/2026-06-01_power_board_no_power_dmm/logs/2026-06-01_hall_control_connector_dmm_check.md` reviewed | Reviewed before this operation sheet was created. |

If any row above is not clearly satisfied, stop here and do not turn on the supply output.

## Power-On Steps

| Step | Action | Expected result | Record |
| --- | --- | --- | --- |
| 1 | Keep supply output off; confirm 24V and 0.2A limit on the supply display. | Settings match this sheet. | User confirmed HSPY-30-05 can set current limit with output off; 24V/0.2A level used. |
| 2 | Connect board input 24V/GND only. | No motor, no NUCLEO/MCU/PWM wires attached. | Static-test boundary maintained. |
| 3 | Turn on supply output and watch CC/CV and input current immediately. | Supply should not enter CC; current should stay below the 0.2A limit and not climb rapidly. | CV, 0.04A. |
| 4 | If Step 3 is stable, record steady input current. | Stable current below limit. | 0.04A. |
| 5 | Measure 5V to GND. | Near 5V and not dropping. | 5V. |
| 6 | Measure 3V3 to GND. | Near 3.3V and not dropping. | 3.34V. |
| 7 | Measure REG12 to GND. | Near the STDRIVE101 REG12 target, normally about 12V, and not dropping. | 12V. |
| 8 | Measure nFAULT to GND. | Non-fault/high state, expected near 3V3 because the project record shows a 10k pull-up to 3V3. | 3.3V. |
| 9 | Observe smell, sound, smoke, and fast heating around DCDC, STDRIVE101, D6, TVS, MOS, PTC, and bus capacitor without touching unknown-hot parts. | No abnormal smell, sound, smoke, or fast heating. | None reported. |
| 10 | Turn off supply output after measurements and wait before handling the board. | Board is no longer powered; do not touch until the bus has fallen from 24V. | User was instructed to power off and wait after measurements; final power-down confirmation not separately recorded. |

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
| Supply mode | CV, not CC | CV | Pass | HSPY-30-05 display reported by user. |
| Input current | Stable and below 0.2A limit | 0.04A | Pass | Well below 0.2A current limit. |
| 5V -> GND | Near 5V | 5V | Pass | User-reported DMM reading. |
| 3V3 -> GND | Near 3.3V | 3.34V | Pass | User-reported DMM reading. |
| REG12 -> GND | Near REG12 target, normally about 12V | 12V | Pass | User-reported DMM reading. |
| nFAULT -> GND | Non-fault/high, expected near 3V3 | 3.3V | Pass | High/non-fault state. |
| Abnormal smell/smoke/sound | None | None reported | Pass | User reported no abnormal smell/sound/heating. |
| Fast heating | None | None reported | Pass | User reported no fast heating. |

## Result Gate

| Gate | Required condition | Record |
| --- | --- | --- |
| Static power result | Pass only if all measurement rows pass and no stop condition occurred | Pass for static limited power-on only, based on 2026-06-05 user-reported measurements. |
| Motor connection | Always No after this sheet | No |
| PWM output | Always No after this sheet | No |
| Next allowed work | If static power passes, plan MCU connection and empty PWM/Gate waveform check separately | Plan MCU connection/empty PWM/Gate waveform check separately; do not connect motor yet. |
| If failed | Power off, keep motor/PWM disconnected, return to no-power debug | Not applicable; no stop condition reported in this run. |

## Notes

- Do not use this sheet to claim the power stage can drive a motor.
- Do not increase current limit during this test.
- Do not retry after a stop condition without a new root-cause note.
