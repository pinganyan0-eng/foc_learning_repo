# 2026-05-09 功率板原理图截图记录

## 文件

- 仓库内截图：`hardware/schematic/2026-05-09_power_board_schematic_screenshot.jpg`
- 原始来源路径：`C:\Users\gregrg\Documents\xwechat_files\wxid_5gjwrl5pj20022_32b0\temp\RWTemp\2026-05\ed3da1fa0ac2e2f714133b633b71e2fa.jpg`
- 来源：用户在 2026-05-09 对话中提供。
- 可信度：原理图截图，可用于位号和连接关系初审；不替代 EDA 源文件、PDF、正式 BOM、Datasheet 或 PCB 审查。

## 截图可直接看到的内容

### 输入与母线

- 24V 输入连接器：`CN6`，网络标注 `J_PWR`，输入为 `24V` 和 `GND_POWER`。
- 输入保护链路：`24V -> F1(SMD1812P050TF) -> D6(SS34) -> 24V_FUSED`。
- TVS：`D5 SMCJ33A`，接在 `24V_FUSED` 与 `GND_POWER` 之间。
- 母线电容：`C_BUS1 470uF`、`C_BUS2 470uF`、`C_BUS_HF 100nF`，接在 `24V_FUSED` 与 `GND_POWER` 之间。

### 电源模块

- 5V 模块符号：`P1 J_IN_5V` 输入接 `24V_FUSED/GND_POWER`，`P2 J_OUT_5V` 输出 `+5V/GND_POWER`。
- 3.3V 模块符号：`P3 J_IN_3V3` 输入接 `+5V/GND_POWER`，`P4 J_OUT_3V3` 输出 `3V3/GND_POWER`。
- 截图只能看到模块化接口符号，不能直接证明模块实物型号是 LM2596S。

### STDRIVE101 与驱动外围

- 驱动芯片：`U1 STDRIVE101`。
- `CP` 电荷泵电容：`C1 100nF`。
- `VS/24V_FUSED` 附近去耦：`C2 0.1uF`、`C3 100uF`。
- `SCREF` 分压：`R1 33K` 到 `3V3`，`R2 20K` 到 `GND_SIGNAL`。
- `REG12` 去耦：`C4 4.7uF`、`C5 0.1uF` 到 `GND_SIGNAL`。
- `nFAULT`：`R3 10K` 上拉到 `3V3`，并接 `LED1` 到 `GND_SIGNAL`。
- 输入串联电阻：`R17/R18/R20/R21/R19/R22` 均为 `10Ω`，位于 `HIN1/HIN2/HIN3/LIN1/LIN2/LIN3` 到 STDRIVE101 输入之间。
- 自举网络：`C22/C23/C24 1uF`，`D1/D2/D3 SS34`，网络标注 `BOOTx/OUTx/REG12`。
- 截图中 `DT/MODE` 到 GND 的连接不明显，需用 EDA 源文件或局部高清图确认。

### 功率级与采样

- MOSFET：`Q1/Q3/Q5` 上桥，`Q2/Q4/Q6` 下桥，均标注 `NCEP40T11G`。
- Gate 电阻：`R23/R24/R26/R28/R29/R31` 均为 `22Ω`。
- Gate-Source 泄放/下拉电阻可见：`R36/R37/R42`、`R32/R41/R43` 均为 `10K`。
- 低侧采样电阻：`R25/R27/R30` 均为 `20mΩ`，接在低侧 MOS 源极节点与 `GND_POWER` 之间。
- 相输出：`OUT1/OUT2/OUT3` 接到 `CN7 J_MOTOR`。

### 接口与地

- 主控接口：`CN8` 15pin，含 `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3/ADC_U/ADC_V/ADC_W/IA/IB/IC/NFAULT/3V3/GND_SIGNAL`。
- Hall 接口：`J7 J_HALL`，含 `+5V`、`GND_SIGNAL`、`IA/IB/IC`；`IA/IB/IC` 线上有 `R38/R39/R40 100Ω`，并有 `R34/R33/R35 4.7K` 上拉和 `C27/C28/C29 10nF` 到地。
- ESP32 接口：`U10 J_ESP32`，含 `3V3`、`PC10`、`PC11`、`GND_SIGNAL`。
- OLED 接口：`U9 J_OLED`，含 `3V3`、`PB8`、`PB9`、`GND_SIGNAL`。
- 地隔离/单点连接：`R_GND_ISO 0Ω`，连接 `GND_POWER` 与 `GND_SIGNAL`。

## 截图暴露的待复核点

- `DT/MODE` 配置连接在截图中不清楚；需要 EDA 源文件、局部放大图或网络表确认。
- 5V/3.3V 模块符号没有显示 LM2596S 具体型号；模块实物和 BOM 仍需确认。
- 端子型号 KF128-5.08 在截图中不可见；只能确认连接器位号/网络，不能确认物料型号。
- `SMD1812P050TF` 0.5A 额定与电机目标电流是否匹配，需要按 24V 输入功率和实际工况核算。
- `D6 SS34` 串联防反接的压降与热损耗需要复核；若 3A、0.55V，则功耗约 1.65W。
- `REG12` 去耦回到 `GND_SIGNAL`，而 STDRIVE101 EP/VS 去耦涉及 `GND_POWER`；需要结合 PCB 确认回流路径和 0Ω 单点连接是否合理。
- 55A VDS 硬件保护阈值不是截图本身能证明的结论，仍需 STDRIVE101 Datasheet 和 NCEP40T11G 热态参数复核。
