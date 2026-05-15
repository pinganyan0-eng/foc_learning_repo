# P2 User Action Queue - 2026-05-14

这个文件只回答一个问题：现在需要用户提供什么，Codex 收到后怎么验收。

它不是接线指导，不是固件生成记录，不是连续性检查，也不是硬件验证。

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## 你现在要做的事

### Task 1 - 先交 Packet B：当前版板级走线源包

这是当前最卡进度、也最需要你提供的证据。

请提供当前功率板对应的任一来源：

- EDA source；
- schematic PDF；
- netlist；
- high-resolution schematic or PCB crop。

必须同时说明：

| Field | 你需要给的信息 |
| --- | --- |
| Source path | 文件放在仓库里的路径，优先放到 `hardware/schematic/` 或清楚命名的 board-source 路径。 |
| Source date/version | 文件日期、版本号或导出时间。 |
| Board revision match | 这个文件是否对应你手上的当前功率板。 |
| CN8 mapping | `NFAULT`、PWM inputs、current-sense nets、Hall nets、`3V3`、ground。 |
| STDRIVE101 endpoints | `nFAULT`、`DT/MODE`、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、`STBY`、VDS monitoring。 |
| Readability | net names、pin names、reference designators、values 必须能看清。 |

Codex 收到后只做无功率审查：把能证明的 CN8 / board-route 项写入
`evidence_packet_2026-05-14.md`，不能证明的仍保持 `Blocked`。

### Task 2 - 交 Packet A：MCSDK / MotorControl 配置源包

如果你能在 GUI 里拿到配置证据，请提供以下任一项：

- real Workbench `.stmcx`；
- MotorControl / Workbench configuration screenshot；
- exact launcher path plus captured version/config screen。

必须能看到或记录：

- MCU / board context：`STM32G474RETx`、NUCLEO 或明确的 custom-board context；
- TIM1 complementary PWM choices；
- fault input selection，当前草案优先看 `PB12/TIM1_BKIN`；
- current-sense mode；
- Hall / sensorless selection or explicit absence；
- `PA2/PA3` 是否排除出 FOC 通信；
- `PB3` 当前由 SWO 还是 Hall B 占用。

不要运行 Motor Profiler，也不要输出 Gate PWM。这个包只能证明配置意图，
不能证明电机、功率级、Hall 闭环或 SMO 行为。

### Task 3 - 补 PB3 / SWO 释放证据

如果后续还计划把 `PB3` 用作 Hall B，请提供以下之一：

- NUCLEO 焊桥、手册页或板级设置截图，证明 SWO 已释放或隔离；
- Workbench / CubeMX 配置截图，证明 `PB3` 已从 `SYS_JTDO-SWO` 变成明确的 Hall B 输入；
- 与当前板子匹配的 CN8 / EDA / netlist 证据，说明 Hall B 实际到哪里。

没有这项证据时，`PB3` 只能继续作为候选，不能登记为 Hall 可用。

## 不接受的来源

这些只能当线索，不能升级证据：

- low-resolution screenshots；
- oral descriptions；
- old or unknown-version EDA/PDF/netlist files；
- partial crops without endpoints or board revision；
- generated MCSDK source without matching `.stmcx` or configuration screen；
- excluded WeChat-side `netlist_PADS.net` candidate。

## 你发给 Codex 的最短模板

```text
我提供 Packet B。
文件路径：
来源日期/版本：
是否匹配当前功率板：
需要你审查的网络：
我没有接 24V、没有接功率板、没有接电机、没有运行 Motor Profiler。
```

如果提供 Packet A，把第一行改成 `我提供 Packet A`，并写清 `.stmcx` 或
截图路径。

## Codex 收到后做什么

1. 按 `source_packet_intake_checklist_2026-05-14.md` 判断来源是否可接受。
2. 填 `source_packet_review_template_2026-05-14.md` 或它的日期副本，做
   Accept / Partial clue / Reject 判断。
3. 只升级源包直接证明的字段。
4. 更新 `evidence_packet_2026-05-14.md` 和 `workflow/evidence_register.md`。
5. 保持未证明项为 `Blocked`。
6. 运行 `python -m unittest discover -s tests`。
7. 重建 `vector_store/`。

## 当前结论

下一步最有价值的是 Packet B：当前版 CN8 / board-route / STDRIVE101
保护路径源包。没有这个源包前，P2 仍不能声明 CN8 routing proof、
STDRIVE101 protection-path proof、power-stage readiness、Hall readiness、
sensorless readiness，且仍不授权任何上电或电机动作。
