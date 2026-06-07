# MCU pre-join review checklist

本表是 L4 高风险任务的准备审查，不是接线或上电操作单。

## Phase Gate

| Check | Evidence | Status |
| --- | --- | --- |
| 静态限流上电记录 | `EV-2026-06-05-HW-STATIC-PWR-001` | Pass for static supply only |
| 电机保持断开 | 需要新的现场全景照片 | TODO |
| 电源限流策略 | 首次静态测试为 24V/0.2A | Known; future setting requires separate approval |
| 原始 EDA/netlist | 未入库 | BLOCKED |
| DT/MODE 实物连接 | 截图不清；仅有用户线索 | BLOCKED |
| 六路 PWM MCU 映射 | 仅确认 PB3->LIN1；其余未知 | BLOCKED |
| 可回滚 PWM 固件 | baseline 无三相 PWM | BLOCKED |
| 示波器/探头型号 | 未提供 | BLOCKED |
| Gate 波形 | 尚无 | NOT STARTED |

结论：阶段 5 尚未通过。禁止接电机、放开限流或进入动态 PWM/Gate 测试。

## CN8 Current Pin Evidence

以下映射来自原理图截图，不替代 EDA/netlist：

| CN8 pin | Net | Current evidence | Open question |
| --- | --- | --- | --- |
| 1 | HIN1 | Schematic screenshot | MCU pin unknown |
| 2 | LIN1 | Screenshot + PB3 continuity | Baseline PB3 is configured as SWO |
| 3 | HIN2 | Schematic screenshot | MCU pin unknown |
| 4 | LIN2 | Schematic screenshot | MCU pin unknown |
| 5 | HIN3 | Schematic screenshot | MCU pin unknown |
| 6 | LIN3 | Schematic screenshot | MCU pin unknown |
| 7 | ADC_U | Schematic screenshot | ADC input range/scaling unknown |
| 8 | ADC_V | Schematic screenshot | ADC input range/scaling unknown |
| 9 | ADC_W | Schematic screenshot | ADC input range/scaling unknown |
| 10 | IA | Screenshot + PA0 continuity | Hall signal direction/level must be confirmed |
| 11 | IB | Screenshot + PA1 continuity | Hall signal direction/level must be confirmed |
| 12 | IC | Screenshot + PB4 continuity | Hall signal direction/level must be confirmed |
| 13 | nFAULT | Screenshot + PB12 continuity | MCU input configuration still unverified |
| 14 | 3V3 | Screenshot + rail continuity | Do not join supplies until power ownership is defined |
| 15 | GND_SIGNAL | Screenshot + DMM continuity | PCB return path still lacks layout evidence |

## Mandatory Review Before Any Cable Is Installed

- [ ] Power board and NUCLEO are both unpowered.
- [ ] CN8 orientation and pin 1 are visible in a photo.
- [ ] Every cable has a source pin, destination pin and net name in a table.
- [ ] MCU and power-board grounds share exactly the reviewed connection.
- [ ] The 3V3 pin is classified as source, sink or do-not-connect.
- [ ] No USB/NUCLEO 5V or 3V3 supply can back-power the power board.
- [ ] All six HIN/LIN mappings are confirmed from schematic/netlist and MCU pinout.
- [ ] `nFAULT` pull-up voltage is confirmed compatible with the MCU input.
- [ ] Default/reset state of all six MCU outputs is low or high-impedance.
- [ ] PWM firmware has a commit ID and a documented rollback.
- [ ] TIM break/fault behavior and startup order are documented.
- [ ] DT/MODE mode is confirmed from physical or EDA evidence.
- [ ] Deadtime ownership is explicit: STDRIVE101 or STM32, never assumed.

## Risk Classification

| Topic | Risk | Current decision |
| --- | --- | --- |
| 24V bus | L4 | No further action in this task |
| PWM/Gate/deadtime | L4 | Preparation only |
| nFAULT/fault clear | L3/L4 | Read-only review; no fault clearing sequence |
| Current sensing/ADC | L3/L4 | Scaling and common-mode range unverified |
| SCREF/VDS | L3/L4 | Divider evidence incomplete; no threshold change |
| Hall interface | L3/L4 | Mapping partly known; no motor/Hall run |
| Motor connection | L4 | Prohibited |

## Evidence Still Required From User

- [ ] Power-board overview photo.
- [ ] CN8 close-up showing pin 1 and silkscreen.
- [ ] DT/MODE area close-up.
- [ ] NUCLEO connector and intended cable photo.
- [ ] Oscilloscope model.
- [ ] Passive probe model and x10 rating.
- [ ] Differential probe model, or explicit statement that none is available.
- [ ] Current firmware commit and `.ioc`/MCSDK project path.

