# hardware_risk_checklist

上电前硬件风险清单。P0/P1 未关闭前不接电机。当前条目来自用户确认版器件记录，尚未由 Datasheet、PCB 或实测复核。

## P0 待关闭项

- LM2596S-5V、LM2596S-3.3V 成品模块的真实芯片、模块质量、纹波、散热和连续电流能力尚未复核。
- SMD1812P050TF 0.5A 额定、1.0A 动作值可能与 1.2A 电机额定电流、3A 峰值目标存在匹配风险。
- SS34 串联防反接 D6 在 2A/3A 工况下可能有明显发热，用户记录中的 3A 压降和 2A 功耗需分开复核。
- STDRIVE101 VDS/SCREF 约 55A 硬件保护目标尚未按 Datasheet 和热态 Rds(on) 复核。
- NCEP40T11G 的 Rds(on)、Qg、tOFF、SOA、热阻和 40V 耐压尖峰余量尚未复核。
- 20mΩ / 2W / 2512 采样电阻在 8A 软件限流和短时故障下的功耗、温漂、Kelvin 走线尚未复核。
- SMCJ33A、母线电容和输入端布局尚未形成完整浪涌/钳位/纹波结论。
- 原理图截图已入库，但 EDA 源文件、导出 PDF、PCB 截图/布局文件、正式 BOM、Datasheet 包还没有入库。
- 截图中 `DT/MODE` 到 GND 的连接不明显，需要用 EDA 源文件或网络表确认。
- `REG12` 去耦回到 `GND_SIGNAL`，而 STDRIVE101 EP/VS 去耦涉及 `GND_POWER`；需要结合 `R_GND_ISO 0Ω` 和 PCB 回流路径复核。

## 上电前必须有的证据

- 原理图截图、原理图 PDF/EDA 源文件、PCB 截图或布局文件、正式 BOM。
- STDRIVE101、NCEP40T11G、LM2596S-5V/3.3V 模块、SMD1812P050TF、SMCJ33A、SS34、20mΩ 采样电阻、红宝石 ZLH 电容 Datasheet 或商家规格页。
- 保护阈值计算：VDS/SCREF、ADC/软件过流、PTC 动作、电源模块限流、SS34 热损耗、TVS 钳位、欠压/UVLO。
- 万用表无电检查：24V-GND、5V-GND、3.3V-GND、REG12-GND、BOOTx-OUTx 无短路。
- 首次通电使用限流电源，从 24V、0.2A 级别起步，不接电机。

## 首次通电观察点

- 24V 输入电流是否在限流内，F1/PTC 是否发热或动作。
- D6 SS34 两端压降和温升。
- 5V、3.3V、REG12 是否稳定，无异常纹波或跌落。
- nFAULT 是否保持正常状态。
- 不输出 PWM 前，BOOTx/OUTx、Gate、U/V/W 无异常电压。
- 确认 `DT/MODE` 配置、`R_GND_ISO` 单点连接、REG12/VS 去耦回流路径与原理图/PCB 一致。
