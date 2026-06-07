# 2026-06-01 first limited power precheck record

本表用于自研 STDRIVE101 功率板首次限流上电前准备。它不是上电授权单；只有所有前置项确认后，才允许按 `2026-06-01_24v_0p2a_static_power_on_operation_sheet.md` 另起现场操作记录。

## Safety Boundary

- 禁止接电机。
- 禁止输出 PWM。
- 禁止放开电源限流。
- 禁止绕过 nFAULT、REG12、5V、3V3 或其他保护检查。
- 若任何项不确定，停止，不进入通电。

## Bench Setup

| 项目 | 要求 | 记录 |
| --- | --- | --- |
| 板卡版本/照片编号 | 写明实物板版本或照片编号 | TODO |
| 供电方式 | 实验室可调限流电源 | 汉晟普源 HSPY-30-05 |
| 初始电压 | 24V 目标，实际旋钮设置需现场记录 | 24V target; static run measurement record dated 2026-06-05 |
| 初始限流 | 0.2A 级别起步 | 0.2A level |
| 万用表 | 可测 DCV、电阻/蜂鸣 | TODO |
| 电机 | 不连接 | TODO |
| PWM | 不输出 | TODO |
| NUCLEO/MCU | 如未明确需要，保持不驱动功率输出 | TODO |

## Pre-Power Evidence Gate

| 项目 | 证据路径 | 状态 | 备注 |
| --- | --- | --- | --- |
| 无电 DMM 检查 | `experiments/2026-06-01_power_board_no_power_dmm/logs/2026-06-01_hall_control_connector_dmm_check.md` | Pass/partial | 多数低风险短路检查通过；不代表可接电机。 |
| 原理图截图/审查 | `hardware/schematic/2026-05-09_power_board_schematic_screenshot.md` | Present | 仍缺原始 EDA/PDF。 |
| 用户确认版器件记录 | `hardware/bom/2026-05-09_user_provided_power_stage_parts.md` | Present | 不是正式 BOM。 |
| 证据包清单 | `docs/03_hardware_notes/power_board_evidence_package.md` | Present | 缺口需持续补。 |
| Datasheet/规格页包 | `references/` | Partial | 部分官方 ST/MCU 资料已摄入；STDRIVE101、MOS、DCDC、TVS、SS34、PTC、采样电阻、母线电容、电机等功率级器件规格页仍应尽量补齐。 |
| 24V/0.2A 静态上电操作单 | `experiments/2026-06-01_power_board_first_limited_power_precheck/2026-06-01_24v_0p2a_static_power_on_operation_sheet.md` | Present | 现场逐项执行；不接电机、不接 NUCLEO/MCU、不输出 PWM。 |

## Power-On Observation Points

| 顺序 | 测量/观察点 | 预期 | 实测 | 判定 |
| --- | --- | --- | --- | --- |
| 1 | 电源是否进入恒流 CC | 不应进入 CC | CV | Pass |
| 2 | 输入电流 | 应在 0.2A 限流内，且无异常上升 | 0.04A | Pass |
| 3 | 5V 对 GND | 接近设计值，无异常跌落 | 5V | Pass |
| 4 | 3V3 对 GND | 接近设计值，无异常跌落 | 3.34V | Pass |
| 5 | REG12 对 GND | 接近 STDRIVE101 内部 REG12 输出目标，无异常跌落 | 12V | Pass |
| 6 | nFAULT | 保持非故障状态；若低电平/异常，停止 | 3.3V | Pass |
| 7 | 异味/冒烟/异常发热 | 无 | 无 | Pass |
| 8 | D6/TVS/DCDC/STDRIVE101/MOS 温升 | 手靠近或温度计观察，无快速异常发热 | 无快速异常发热 | Pass |

## Immediate Stop Conditions

出现任一情况立即断电，记录现象，不重复尝试：

- 电源进入恒流 CC 或输入电流快速顶到 0.2A 限流。
- 出现异味、冒烟、火花或异常声响。
- STDRIVE101、DCDC、MOS、TVS、D6、PTC、母线电容明显发热。
- 5V、3V3 或 REG12 明显偏离预期或快速跌落。
- nFAULT 处于故障状态或状态不明。
- 表笔、夹子、供电线接触不可靠。

## Result

| 项目 | 记录 |
| --- | --- |
| 是否执行上电 | Yes, 2026-06-05, 24V/0.2A level static limited power-on |
| 是否接电机 | No |
| 是否输出 PWM | No |
| 是否允许进入下一步 | Yes, but only to separately planned MCU connection/empty PWM/Gate waveform checks; not to motor connection |
| 复盘备注 | HSPY-30-05 reported CV, input current 0.04A, 5V/3V3/REG12/nFAULT rails normal, no abnormal smell/sound/fast heating. |
