# protection_thresholds

## 2026-05-20 Packet C Review Status

Current decision: `Packet C detail narrowed / protection proof still partial clue / P3 still blocked`.

The earlier `V_DSth = 0.249V` and `I_trip ~= 55A` record is not accepted as a
project threshold. The repo-local STDRIVE101 extracted text currently says
`VDSth = VSCREF`, with `VSCREF,en = 2.54V` and `VSCREF,dis = 2.9V`. With the
current source clue `R1=33k` to `3V3` and `R2=20k` to ground, the divider gives
about `VSCREF = 1.245V`, which is below the extracted enable threshold. Treat
this only as a no-power source-level clue that VDS monitoring is intended
enabled; it is not powered validation and not a safe current-limit value.

`CP -> 100nF -> GND` is also only a source clue. It does not prove the CP
overcurrent comparator input network or threshold. Before any P3 action, the
project still needs a PDF/table-backed threshold review, named `CP` route proof,
`VS/VM` proof, no-power continuity checks, current-limited bring-up settings,
measurement points, and a rollback path.

SCREF/VDS、过流、欠压、TVS、保险丝/PTC 等保护阈值记录。当前内容来自用户按原理图确认和 2026-05-09 原理图截图初审，但用户说明不能保证全部正确；它是硬件审查输入，不是已验证结论。

## 当前已知电压/器件线索

| 项目 | 当前记录 | 状态 |
| --- | --- | --- |
| 输入母线 | 24V，J_PWR 输入，经 F1 和 D6 后形成 24V_FUSED | 目标工作电压，不能直接大电流上电。 |
| 5V 电源轨 | LM2596S-5V 成品模块，24V_FUSED -> 5V，3A 连续 | 已替换原 MP2459GJ-Z 记录，模块参数待实物/Datasheet 复核。 |
| 3.3V 电源轨 | LM2596S-3.3V 成品模块，5V -> 3.3V，3A 连续 | 已记录，模块参数待实物/Datasheet 复核。 |
| REG12 去耦 | 4.7μF / 25V X7R / 0805 + 100nF / 50V X7R / 0402 | 仅作 STDRIVE101 相关去耦，不能外供。 |
| BOOT 自举网络 | 1μF / 50V X7R / 0603 ×3，加 SS34 / SMA ×3 外部自举二极管 | 需按 STDRIVE101 Datasheet 和版图位置复核。 |
| VS 去耦 | C2 0.1μF + C3 100μF，接在 24V_FUSED/VS 附近 | 截图可见，需按 STDRIVE101 Datasheet 和 PCB 位置复核。 |
| 母线电容 | 470μF / 50V ×2 + 100nF / 50V X7R | 用户推荐红宝石 ZLH 470μF/50V，需复核纹波、ESR、寿命和浪涌。 |
| MOSFET | NCEP40T11G，40V，Rds(on) 计算用 4.5mΩ | 需按 Datasheet/SOA 和温度修正复核。 |

## 目标电流

| 项目 | 当前记录 | 审查备注 |
| --- | --- | --- |
| 电机额定电流 | 1.2A，42BLF01-2430HE 官方标称 | 需补电机 Datasheet 或截图。 |
| 电机峰值电流 | 3A，短时堵转/加速工况 | 需定义允许持续时间和散热条件。 |
| 软件限流阈值 | 8A，STM32 ADC 采样触发 | 需与 20mΩ / PGA / ADC 标定 / MCSDK 参数一致。 |
| 硬件 VDS 过流保护目标 | 约 55A | 用户计算值，必须复核；该值远高于运行电流，不能替代软件限流。 |

## VDS/SCREF 过流计算记录

| 项目 | 当前记录 |
| --- | --- |
| SCREF 上臂 | 33kΩ / 1% / 0402，R1，3.3V -> SCREF |
| SCREF 下臂 | 20kΩ / 1% / 0402，R2，SCREF -> GND_SIGNAL |
| 用户计算 V_SCREF | 3.3V × 20kΩ / (33kΩ + 20kΩ) = 1.245V |
| 用户记录 V_DSth | 0.249V |
| 用户计算 Rds(on) | 4.5mΩ |
| 用户计算 I_trip | 0.249V / 0.0045Ω ≈ 55A |
| 必须复核 | STDRIVE101 中 SCREF 与 VDS 阈值比例、NCEP40T11G 热态 Rds(on)、VDS blanking/filter、PCB 寄生和短路能量。 |

## 截图相关复核

- `DT/MODE` 连接在截图中不清楚；若该脚配置错误，会直接影响 STDRIVE101 输入模式/死区策略。
- `R_GND_ISO 0Ω` 连接 `GND_POWER` 与 `GND_SIGNAL`，需确认 SCREF、REG12、nFAULT、ADC/Hall 小信号回流不会被功率电流污染。

## 输入保护阈值/热风险

| 保护项 | 当前记录 | 审查备注 |
| --- | --- | --- |
| PTC | SMD1812P050TF，0.5A 额定，1.0A 动作 | 需复核 24V 输入实际工作电流；可能与 1.2A/3A 电机目标存在匹配风险。 |
| 防反接二极管 | SS34，串联 24V 正极，D6 | 用户记录 2A 时约 1.1W；若 3A 且 0.55V，则约 1.65W，需要温升和封装功耗复核。 |
| TVS | SMCJ33A 单向，D5，阴极 24V_FUSED，阳极 GND_POWER | 需查 Vrwm、Vbr、Vc、峰值功率和 24V 母线尖峰场景。 |
| 母线电容 | 470μF/50V ×2 + 100nF/50V | 需复核纹波电流、ESR、耐温、寿命和安装位置。 |

## 调试限流不是板上阈值

- 首次上电按项目安全流程从 24V、0.2A 级别限流起步。
- 该 0.2A 是实验电源调试保护设置，不代表 PTC 动作电流、VDS 过流阈值或软件电流限幅。
- 在 VDS/SCREF、PTC、SS34 热损耗、TVS 钳位和电源模块参数未复核前，不接电机。
