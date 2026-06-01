# hardware_risk_checklist

上电前硬件风险清单。P0/P1 未关闭前不接电机。当前条目来自用户确认版器件记录、已消化方案/报告和原理图截图，尚未由原始 EDA、PCB、正式 BOM、功率级器件规格页或上电实测完成签核。

## P0 待关闭项

- LM2596S-5V、LM2596S-3.3V 成品模块的真实芯片、模块质量、纹波、散热和连续电流能力尚未复核。
- SMD1812P050TF 0.5A 额定、1.0A 动作值可能与 1.2A 电机额定电流、3A 峰值目标存在匹配风险。
- SS34 串联防反接 D6 在 2A/3A 工况下可能有明显发热，用户记录中的 3A 压降和 2A 功耗需分开复核。
- STDRIVE101 VDS/SCREF 约 55A 硬件保护目标尚未按 Datasheet 和热态 Rds(on) 复核。
- NCEP40T11G 的 Rds(on)、Qg、tOFF、SOA、热阻和 40V 耐压尖峰余量尚未复核。
- 20mΩ / 2W / 2512 采样电阻在 8A 软件限流和短时故障下的功耗、温漂、Kelvin 走线尚未复核。
- SMCJ33A、母线电容和输入端布局尚未形成完整浪涌/钳位/纹波结论。
- 方案、报告、原理图截图、用户确认版硬件清单和部分官方 ST/MCU 资料已入库；硬件签核层仍缺 EDA 源文件、导出 PDF、PCB 源文件/关键截图、正式 BOM、Gerber/坐标和功率级器件规格页。
- 截图中 `DT/MODE` 到 GND 的连接不明显，需要用 EDA 源文件或网络表确认。
- `REG12` 去耦回到 `GND_SIGNAL`，而 STDRIVE101 EP/VS 去耦涉及 `GND_POWER`；需要结合 `R_GND_ISO 0Ω` 和 PCB 回流路径复核。

## 上电前必须有的证据

- 现有方案/报告/截图/BOM 线索已可作背景证据；上电签核还需要原理图 PDF/EDA 源文件、PCB 截图或布局文件、正式 BOM。
- STDRIVE101、NCEP40T11G、LM2596S-5V/3.3V 模块、SMD1812P050TF、SMCJ33A、SS34、20mΩ 采样电阻、红宝石 ZLH 电容等功率级器件 Datasheet 或商家规格页。
- 保护阈值计算：VDS/SCREF、ADC/软件过流、PTC 动作、电源模块限流、SS34 热损耗、TVS 钳位、欠压/UVLO。
- 万用表无电检查：24V-GND、5V-GND、3.3V-GND、REG12-GND、BOOTx-OUTx 无短路。
- 首次通电使用限流电源，从 24V、0.2A 级别起步，不接电机。

## 已收到的无电 DMM 局部证据

- 2026-06-01：用户提供 Hall、LIN1、nFAULT 和部分连接器电源脚的无电 DMM 表，记录在 `experiments/2026-06-01_power_board_no_power_dmm/logs/2026-06-01_hall_control_connector_dmm_check.md`。
- 局部结论：IA/IB/IC 到 PA0/PA1/PB4 连通；Hall 三路到 3V3 约 4.7kΩ；nFAULT 到 PB12 连通且到 3V3 约 10kΩ；PB3/LIN1 约 10Ω 串阻；24V-GND、5V-GND、REG12-GND、BOOTx-OUTx、OUTx 对 GND/24V/相间均为 OL 且不蜂鸣；R1 本体 33.3kΩ、R2 本体 19.8kΩ、R_GND_ISO 本体 0Ω、CN8 Pin15 到 GND_SIGNAL 约 0.2Ω 且蜂鸣；GHS/GLS 到 GND 均 OL 且不蜂鸣，GHS/GLS 到对应 MOS Gate 均约 22Ω 且蜂鸣；这些读数符合预期。
- SCREF 说明：早先 `SCREF->3V3` 和 `SCREF->GND` 均为 OL，现已证明 R1/R2 本体正确；用户确认 R1/R2 中点不在顶层裸露，不能安全直接 DMM 探测。既有 `hardware/schematic/2026-05-09_power_board_schematic_screenshot.md` 和 `hardware/bom/2026-05-09_user_provided_power_stage_parts.md` 已记录 R1/R2 中点连接到 STDRIVE101 Pin3/SCREF。
- 仍缺上电前关键项：原始 EDA/netlist/PCB-source、原理图 PDF、PCB 源文件/关键截图、正式 BOM、Gerber/坐标、功率级器件规格页和关键保护阈值复核仍未入库。
- 2026-06-01 已新增证据包清单 `docs/03_hardware_notes/power_board_evidence_package.md`、首次限流上电前记录表 `experiments/2026-06-01_power_board_first_limited_power_precheck/2026-06-01_first_limited_power_precheck_record.md` 和 24V/0.2A 静态上电操作单 `experiments/2026-06-01_power_board_first_limited_power_precheck/2026-06-01_24v_0p2a_static_power_on_operation_sheet.md`；这些文件不是接电机或 PWM 授权。

## 首次通电观察点

- 24V 输入电流是否在限流内，F1/PTC 是否发热或动作。
- D6 SS34 两端压降和温升。
- 5V、3.3V、REG12 是否稳定，无异常纹波或跌落。
- nFAULT 是否保持正常状态。
- 不输出 PWM 前，BOOTx/OUTx、Gate、U/V/W 无异常电压。
- 确认 `DT/MODE` 配置、`R_GND_ISO` 单点连接、REG12/VS 去耦回流路径与原理图/PCB 一致。
