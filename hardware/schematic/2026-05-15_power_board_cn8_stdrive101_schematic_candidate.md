# 2026-05-15 CN8 / STDRIVE101 原理图截图候选源包

## 文件

- 仓库内截图：`hardware/schematic/2026-05-15_power_board_cn8_stdrive101_schematic_candidate.png`
- 原始来源路径：`C:\Users\gregrg\Documents\xwechat_files\wxid_5gjwrl5pj20022_32b0\temp\RWTemp\2026-05\f58e987b7111e29ff5447e3bca4c0b2e.png`
- 来源：用户在 2026-05-15 对话中提供，并询问“这个可以吗?”。
- 来源补充：用户在 2026-05-15 确认这是当前功率板，来源/版本口径为硬件同学自绘；截图本身没有正式标题栏、修订号或导出日期。
- 图片尺寸：1492 x 980 px。
- 当前 P2 判定：`Partial clue`。它可以作为 Packet B / Packet C 的候选硬件源包，且 current physical power board match 已由用户确认；但在缺少正式 source date/version、STM32 端点映射、`DT/MODE` 端点证明和 `STBY` 证明前，不能升级为 accepted board-route proof。

## 截图可见内容

### CN8 接口

截图可见 `CN8` 15pin，网络名包括：

- `HIN1`、`LIN1`
- `HIN2`、`LIN2`
- `HIN3`、`LIN3`
- `ADC_U`、`ADC_V`、`ADC_W`
- `IA`、`IB`、`IC`
- `NFAULT`
- `3V3`
- `GND_SIGNAL`

这能支持“功率板侧 CN8 网络名可读”的候选证据。它仍不能单独证明这些网络在 NUCLEO / STM32 侧对应到哪些 MCU pins。

### STDRIVE101 与输入网络

截图可见 `U1 STDRIVE101`，并可读出：

- `HIN1/HIN2/HIN3`、`LIN1/LIN2/LIN3` 通过 `R17/R18/R20/R21/R19/R22` 进入 STDRIVE101 输入脚，电阻标注为 `10Ω`。
- `nFAULT` 网络从 STDRIVE101 引出，看到 `R3 10kΩ` 上拉到 `3V3`，并接 `LED1` 到 `GND_SIGNAL`。
- `REG12`、`CP`、`SCREF`、`VS`、`BOOT1/2/3`、`OUT1/2/3`、`GHS1/2/3`、`GLS1/2/3` 等网络名可见。
- `SCREF` 分压候选为 `R1 33kΩ` 到 `3V3`、`R2 20kΩ` 到 `GND_SIGNAL`。
- `REG12` 去耦候选为 `C4 4.7uF` 和 `C5 100nF`。
- bootstrap 候选为 `C22/C23/C24 1uF` 与 `D1/D2/D3 SS34`。

`DT/MODE` 名称可见，但截图仍不足以独立证明其最终端点、阻值或接地状态。
`STBY` 路径未在本截图中形成可接受证据。

### 功率级与采样

截图可见：

- 上桥 MOSFET：`Q1/Q3/Q5`，标注 `NCEP40T11G`。
- 下桥 MOSFET：`Q2/Q4/Q6`，标注 `NCEP40T11G`。
- Gate 电阻：`R23/R24/R26/R28/R29/R31`，标注 `22Ω`。
- Gate-source 下拉候选：`R36/R37/R42`、`R32/R41/R43`，标注 `10kΩ`。
- 低侧采样电阻：`R25/R27/R30`，标注 `20mΩ`。
- 电机相输出：`OUT1/OUT2/OUT3` 到 `CN7 J_MOTOR`。

这些内容可以作为后续 Packet B / C 审查线索，但不授权 Gate PWM、功率级测试或电机连接。

### Hall / IA IB IC

截图可见 `J7 J_HALL`，包含 `+5V`、`GND_SIGNAL`、`IA`、`IB`、`IC`。
`IA/IB/IC` 有 `R38/R39/R40 100Ω` 串联候选、`R34/R33/R35 4.7kΩ` 上拉候选和 `C27/C28/C29 10nF` 滤波候选。

这只能说明功率板侧 Hall/IA/IB/IC 接口线索，不能证明 `PB3` 已释放或 Hall B 在 STM32 侧可用。

## 仍缺的接受条件

这张截图要从 `Partial clue` 升级为 accepted source，至少还需要：

1. 如果存在正式 EDA/PDF/netlist，补正式 source date/version 或修订号。
2. 若要证明 STM32 pin mapping，需要补 NUCLEO / STM32 侧 CN8 到 MCU pins 的源证据。
3. 若要证明 `DT/MODE` 和 `STBY`，需要更清晰的端点、阻值或 netlist。
4. 若要证明保护阈值，需要结合 STDRIVE101 datasheet 和当前板元件值计算，不能只看截图下结论。

## 当前结论

这张图“可以用”，但当前只能登记为可读的硬件源包候选和 `Partial clue`。
它不能单独证明 CN8 routing proof、STDRIVE101 protection-path proof、
power-stage readiness、Hall readiness、Gate PWM readiness、Motor Profiler
readiness、motor readiness 或 sensorless readiness。
