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
| 六路 PWM MCU 映射 | 2026-05-19 PCB2 映射证据已恢复：P1-P6 -> PA15/PB3/PB10/PA8/PA9/PA10 | EVIDENCE FOUND; needs firmware/cable reconciliation |
| 可回滚 PWM 固件 | baseline 无三相 PWM | BLOCKED |
| 示波器/探头型号 | 未提供 | BLOCKED |
| Gate 波形 | 尚无 | NOT STARTED |

结论：阶段 5 尚未通过。禁止接电机、放开限流或进入动态 PWM/Gate 测试。

## CN8 Current Pin Evidence

以下映射来自原理图截图，不替代 EDA/netlist：

| CN8 pin | Net | Current evidence | Open question |
| --- | --- | --- | --- |
| 1 | HIN1 | Schematic screenshot + 2026-05-19 PCB2 mapping | PA15; confirm current firmware and cable |
| 2 | LIN1 | Screenshot + PB3 continuity + 2026-05-19 PCB2 mapping | PB3; baseline still configures PB3 as SWO |
| 3 | HIN2 | Schematic screenshot + 2026-05-19 PCB2 mapping | PB10; confirm current firmware and cable |
| 4 | LIN2 | Schematic screenshot + 2026-05-19 PCB2 mapping | PA8; confirm current firmware and cable |
| 5 | HIN3 | Schematic screenshot + 2026-05-19 PCB2 mapping | PA9; confirm current firmware and cable |
| 6 | LIN3 | Schematic screenshot + 2026-05-19 PCB2 mapping | PA10; confirm current firmware and cable |
| 7 | ADC_U | Schematic screenshot | ADC input range/scaling unknown |
| 8 | ADC_V | Schematic screenshot | ADC input range/scaling unknown |
| 9 | ADC_W | Schematic screenshot | ADC input range/scaling unknown |
| 10 | IA | Screenshot + PA0 continuity | Hall signal direction/level must be confirmed |
| 11 | IB | Screenshot + PA1 continuity | Hall signal direction/level must be confirmed |
| 12 | IC | Screenshot + PB4 continuity | Hall signal direction/level must be confirmed |
| 13 | nFAULT | Screenshot + PB12 continuity | MCU input configuration still unverified |
| 14 | 3V3 | Screenshot + rail continuity | Do not join supplies until power ownership is defined |
| 15 | GND_SIGNAL | Screenshot + DMM continuity | PCB return path still lacks layout evidence |

## 2026-06-07 Correction: Recovered Six-Channel Mapping Evidence

The earlier 2026-05-19 PCB2 mapping packet has been recovered into this synced
master workspace:

`hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/pcb2_mapping_pin1_protection_note_2026-05-19.md`

Accepted mapping clue for CN8 P1-P6:

| CN8 | Signal | NUCLEO position | STM32 pin |
| --- | --- | --- | --- |
| P1 | HIN1 | CN10-D11 | PA15 |
| P2 | LIN1 | CN10-D12 | PB3 |
| P3 | HIN2 | CN10-D13 | PB10 |
| P4 | LIN2 | CN10-D7 | PA8 |
| P5 | HIN3 | CN10-D9 | PA9 |
| P6 | LIN3 | CN10-D10 | PA10 |

Decision: the six-channel mapping is no longer treated as absent. It still
does not prove that the current `.ioc`/PWM firmware owns these pins, that the
physical cable is wired this way, or that dynamic Gate testing is approved.

## 2026-06-07 CN8 Pin Probe Firmware Source

Added source-only NUCLEO probe firmware:

`apps/stm32_g474_foc/cn8_pin_probe/`

This probe drives the recovered CN8 P1-P6 STM32 pins with identification square
waves:

| CN8 | Signal | STM32 pin | Probe waveform |
| --- | --- | --- | --- |
| P1 | HIN1 | PA15 | about 50 Hz |
| P2 | LIN1 | PB3 | about 100 Hz |
| P3 | HIN2 | PB10 | about 200 Hz |
| P4 | LIN2 | PA8 | about 400 Hz |
| P5 | HIN3 | PA9 | about 1 kHz |
| P6 | LIN3 | PA10 | about 2 kHz |

Decision: this closes the "we need a firmware task" gap only at source level.
It is still not build, flash, waveform, Gate, or motor evidence. Local CMake
configure has been moved to the installed `mingw32-make.exe` generator and is
currently blocked because `arm-none-eabi-gcc.exe` and
`arm-none-eabi-g++.exe` are not available in PATH or detected local ST tool
directories.

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

- [x] Power-board overview photo: archived as `photos/2026-06-07_power_board_top_overview.jpg`.
- [x] CN8 close-up showing connector orientation: archived as `photos/2026-06-07_cn3_cn8_closeup.jpg`.
- [x] DT/MODE area close-up: archived as `photos/2026-06-07_stdrive101_dt_mode_area_closeup.jpg`; this is photo evidence only and does not close DT/MODE mode.
- [x] Six-channel NUCLEO-to-CN8 mapping source packet: recovered as `hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/pcb2_mapping_pin1_protection_note_2026-05-19.md`.
- [x] NUCLEO-only CN8 pin-probe firmware source: added as `apps/stm32_g474_foc/cn8_pin_probe/`.
- [ ] NUCLEO connector and intended cable photo.
- [x] Oscilloscope model: RIGOL DS1102E Plus from `photos/2026-06-07_rigol_front_model.jpg`.
- [x] Passive probe model and x10 rating: RIGOL RP2200-class passive probe from `photos/2026-06-07_rigol_rp2200_passive_probe.jpg`; verify physical marking before use.
- [ ] Differential probe model, or explicit statement that none is available.
- [ ] Current firmware commit and `.ioc`/MCSDK project path.

## Photo Review Update - 2026-06-07

New photos close several preparation-record gaps, but they do not approve
burning a PWM firmware or measuring Gate waveforms.

Still blocking any dynamic PWM/Gate task:

- Six-channel NUCLEO-to-CN8 mapping evidence has been recovered from the
  2026-05-19 PCB2 mapping packet, but the current firmware and physical cable
  still need to be reconciled against it.
- DT/MODE is not conclusively proven by the close-up photo; use EDA/netlist or
  a targeted no-power continuity/resistance check.
- PWM firmware commit, rollback path, reset/default safe-state proof, and
  exact `.ioc`/MCSDK project are not provided.
- The new `cn8_pin_probe` source is not yet a built/flashed artifact because
  local command-line build tools are missing.
- No NUCLEO connector/cable photo or reviewed wiring table is provided.
- No differential probe is shown, so high-side Vgs, OUTx, and BOOTx
  measurements remain prohibited.

