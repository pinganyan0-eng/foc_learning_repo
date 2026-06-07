# 2026-06-07 MCU pre-join and PWM/Gate preparation

Evidence ID: `EV-2026-06-07-HW-GATE-PREP-001`

## Scope

本目录只用于自研 STDRIVE101 功率板的 MCU 接入前审查和空载 PWM/Gate 波形检查准备。

本任务不执行或指挥以下动作：

- 接电机或相线负载。
- 输出 PWM 或重复上电。
- 提高母线电压或放开限流。
- 修改 PWM、死区、Gate、保护阈值或 FOC 实时代码。
- 使用普通示波器探头测量高边 `Vgs` 或把地夹接到 `OUT1/2/3`。

## Current Evidence

| Item | Current evidence | Decision |
| --- | --- | --- |
| 无电短路检查 | `EV-2026-06-01-HW-DMM-001` | 局部通过；不等于动态放行。 |
| 24V/0.2A 静态上电 | `EV-2026-06-05-HW-STATIC-PWR-001` | 静态供电初步通过。 |
| CN8 接口 | 截图显示六路 HIN/LIN、ADC、Hall、nFAULT、3V3、GND_SIGNAL | 引脚名称可用，供电方向和 MCU 六路映射仍需确认。 |
| DT/MODE | 截图中连接不清；用户记录称短接 GND | 未通过正式证据确认。 |
| PWM 固件 | 仓库只有 NUCLEO baseline，无三相互补 PWM/MCSDK 工程 | 未准备。 |
| Gate 波形 | 无示波器截图 | 未验证。 |

## Key Review Result

STDRIVE101 官方 Datasheet 说明：

- `DT/MODE` 通过电阻接地时使用 `ENx/INx` 模式，并由芯片内部生成死区。
- `DT/MODE` 直接短接地时使用六路 `INHx/INLx` 模式，芯片不生成死区，只提供同桥臂互锁。
- 所有输入内部下拉；输入全低时器件可进入 standby。
- `nFAULT` 为开漏故障输出；UVLO、VDS 保护、过流和过温均可能使其拉低。

当前原理图截图把 CN8 标为六路 `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3`。如果实物 `DT/MODE` 确实直接短接地，则 MCU 固件必须自行保证互补输出和死区。由于缺少原始 EDA/netlist、实物局部照片和 PWM 固件，本任务结论是：

**尚不满足空载 PWM/Gate 动态检查的执行条件，只满足准备清单建立条件。**

## Required Inputs Before A Future Dynamic Task

- 功率板全景和 CN8 丝印近照。
- STDRIVE101 `DT/MODE` 周边高清照片或 EDA/netlist。
- NUCLEO 到 CN8 的六路信号映射表。
- 3V3 电源归属说明，避免 NUCLEO 与功率板双向供电。
- 示波器、普通探头和差分探头的型号与额定值。
- 可回滚的 PWM 固件 commit、CubeMX/MCSDK 配置和默认安全态证据。
- 不带电的接线图审查结果。

## Files

- `2026-06-07_mcu_prejoin_review_checklist.md`
- `2026-06-07_pwm_gate_waveform_prep_sheet.md`
- `2026-06-07_scope_grounding_safety_table.md`
- `photos/README.md`
- `waveforms/README.md`

## Official Sources

- STMicroelectronics, [STDRIVE101 Datasheet DS13472 Rev 2](https://www.st.com/resource/en/datasheet/stdrive101.pdf), June 2022.
- STMicroelectronics, [STDRIVE101 product page](https://www.st.com/en/power-management/stdrive101.html).
- STMicroelectronics, [EVALSTDRIVE101 product and design resources](https://www.st.com/en/evaluation-tools/evalstdrive101.html).
- Tektronix, [Floating Measurements Selection Guide](https://www.tek.com/en/datasheet/floating-measurements-selection-guide).
- Tektronix, [The Three Facets of Floating Measurement Solutions](https://www.tek.com/en/documents/application-note/three-facets-floating-measurement-solutions).

