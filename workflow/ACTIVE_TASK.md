# 当前任务

这是当前唯一任务，不是长期计划。每次执行前先读本文件，再按任务边界执行；任务完成后由 Codex 更新结果区，并由 ChatGPT 继续教学、拆解或复盘。

## Task ID

- ID: `TASK-2026-05-19-p2-pcb2-mapping-pin1-protection-intake`
- 主题：P2 当前 PCB2 映射、pin-1 与 STDRIVE101 保护链入仓审查
- Status：open/ready
- Risk Level：L0 documentation / no-power governance
- Definition of Done：`workflow/definition_of_done.md#仓库维护任务`
- Evidence ID：`EV-2026-05-19-P2-PCB2-MAPPING-PIN1-PROTECTION-001`
- Review Required：yes

## 背景

P2 MCSDK 无功率预检已经接收并审查了多类 2026-05-19 新线索：

- Packet A Workbench 捕获尝试：Workbench 6.4.2 能看到 `NUCLEO-G474RE` /
  `STM32G474RETx` 控制板上下文，但没有捕获到可接受的自研 STDRIVE101
  功率板 Custom / Generic 上下文。
- ProDoc `.epro`：证明自研 STDRIVE101 驱动板的当前原理图线索，但没有 PCB
  layout 数据，也不证明 NUCLEO `CN8` 或 STM32 endpoint。
- Gerber PCB2：证明板侧 Gerber / flying-probe pad-net 线索，但不证明
  NUCLEO `CN8`、STM32 引脚、线束、连续性或上电安全。
- 当前 PCB2 映射与 pin-1 图片：用户说明它对应当前 PCB2，并给出
  P1-P15 映射、Hall 对应、PB3/SWO 说明和 STDRIVE101 保护链接法；后续
  澄清图说明 `PC7/PB3/PB10` 是替代建议，当前 PCB2 Hall 实际走
  `IA/IB/IC -> PA0/PA1/PB4`。

## 当前阶段

真实工程仍处于 P2 无功率预检。Packet A 尚未被接受，generated-project trust 仍为 `Not allowed`。本任务把用户刚提供的当前 PCB2 映射、pin-1 图片、Hall 对应、PB3/SWO 和 STDRIVE101 保护链说明归档并审查。

## 功能句

创建 2026-05-19 current PCB2 source review，把已经回答的问题登记为当前 PCB2 线索，同时把下一步阻塞项改为 `PA0/PA1/PB4` 软件 Hall / Workbench 策略选择。

## 规则表

| 项 | 决策 |
| --- | --- |
| 允许做 | 归档图片和文字来源，新增 source review，更新 `CURRENT_STATUS.md`、P2 README、P2 readiness snapshot、evidence packet、evidence register、user action queue 和本文件。 |
| 并行保留 | Packet A 继续寻找 Workbench 支持自研 STDRIVE101 板的 Custom / Generic / Board Designer / Board Manager 路径。 |
| 不升级 | Packet A selected fields、generated-project trust、continuity、power-stage readiness、Hall readiness、motor readiness。 |
| 禁止做 | 不启动 GUI，不生成源码，不构建，不烧录，不接 24V，不接功率板，不接电机，不输出 Gate PWM，不运行 Motor Profiler。 |

## 输入文件

- `CURRENT_STATUS.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_001_packet_a_workbench_capture_attempt.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_002_prodoc_p1_epro.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_003_gerber_pcb2.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/hardware_supplement_handoff_2026-05-19.md`
- User-provided current PCB2 mapping text and two pin-1 images from the current thread.
- `workflow/evidence_register.md`

## 输出文件

- `hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/pcb2_mapping_pin1_protection_note_2026-05-19.md`
- `hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/pcb2_cn3_control_connector_pin1_layout_2026-05-19.png`
- `hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/pcb2_blue_connector_pin1_3d_2026-05-19.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md`
- `workflow/ACTIVE_TASK.md`
- `CURRENT_STATUS.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md`
- `workflow/evidence_register.md`

## 验收证据

- Source review 记录用户声明该回答对应当前 PCB2。
- Source review 记录 P1-P15 映射、pin-1 图片、Hall 对应、PB3/SWO 说明和 STDRIVE101 保护链。
- Source review 明确当前 PCB2 中 `PB3=LIN1`、`PB10=HIN2`，`PC7/PB3/PB10` 是替代建议；P2 仍不能进入 generated-project trust、build-only、flash、power 或 motor stage。
- `workflow/evidence_register.md` 记录本任务只是 evidence governance，不是硬件验证。
- `python -m unittest discover -s tests` 通过。
- `python tools/build_vector_store.py` 运行完成。

## 安全边界

本任务不允许任何 GUI、生成、构建、烧录或硬件动作。未来收到硬件补证后，也必须先走 source packet review，再更新证据包；不能因为文件到位就自动允许上电。

## 执行步骤

1. 读取 2026-05-19 Packet A/B/C source reviews、P2 readiness snapshot 和 evidence register。
2. 归档当前 PCB2 mapping / pin-1 / protection 来源。
3. 新增 source packet review。
3. 更新当前任务、状态入口和证据登记。
4. 运行 `python -m unittest discover -s tests`。
5. 运行 `python tools/build_vector_store.py`。
6. 输出修改摘要、命令结果、`git status` 摘要和建议 commit message。

## Definition of Done

- 当前 PCB2 映射、pin-1、Hall 对应和保护链说明已入仓审查。
- 下一步不再泛泛要求映射表，而是选择并审查 `PA0/PA1/PB4` 软件 Hall 或硬件改线方案。
- Packet A 仍保持 `Partial clue / Preparation only / stopped`。
- Generated-project trust 仍保持 `Not allowed`。
- 未修改固件、接口、CubeMX/MCSDK 生成目录、硬件参数、PWM、Gate 或 FOC 实时控制代码。

## Blocked Handling

如果命令失败、文件冲突或发现本任务会升级证据等级，Codex 应停止并记录失败命令、报错摘要、可能原因和下一步建议，不得绕过限制继续执行。

## Codex 结果区

- 执行状态：ready；当前 PCB2 映射、pin-1 图片和 STDRIVE101 保护链 source review 已完成，状态入口、证据包和向量索引已刷新。
- 修改文件：`hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/pcb2_mapping_pin1_protection_note_2026-05-19.md`、`hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/pcb2_cn3_control_connector_pin1_layout_2026-05-19.png`、`hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/pcb2_blue_connector_pin1_3d_2026-05-19.png`、`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md`、`workflow/ACTIVE_TASK.md`、`CURRENT_STATUS.md`、`apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`、`apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`、`apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md`、`apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md`、`workflow/evidence_register.md`、`vector_store/chunks.jsonl`、`vector_store/index.json`
- 证据：`workflow/evidence_register.md` 中新增 `EV-2026-05-19-P2-PCB2-MAPPING-PIN1-PROTECTION-001`；`python -m unittest discover -s tests` 成功，41 tests OK；`git diff --check` 成功，仅有行尾提示；项目 dry-run no-power 安全扫描未发现 unsafe added claims；`python tools/build_vector_store.py` 成功，built 8160 chunks
- Evidence ID：`EV-2026-05-19-P2-PCB2-MAPPING-PIN1-PROTECTION-001`
- 失败命令：`python -m unittest discover -s tests` 第一次失败，原因是 `p2_readiness_snapshot_2026-05-15.md` 中测试契约要求的短语 `does not release SWO` 被新表述替换；已补回旧边界短语并重跑通过。
- 剩余风险：Packet A Workbench 自研板路径、`PA0/PA1/PB4` 软件 Hall 策略、Workbench/CubeMX final selected fields 和断电连续性仍待补证。

## 历史任务

- `TASK-2026-05-19-p2-min-hw-request-workbench-asset-probe`：ready；最小补证请求、Workbench 资产探测记录、状态入口、证据包和向量索引刷新已完成。
- `TASK-2026-05-19-p2-hardware-supplement-handoff`：ready；硬件补证完整 handoff 和状态入口刷新已完成。
- `TASK-2026-05-19-p2-packet-a-workbench-capture-attempt`：blocked/stopped；Workbench 能看到控制板上下文，但没有接受自研 STDRIVE101 功率板上下文。
- `TASK-2026-05-18-p2-packet-a-capture-prep`：ready；Packet A 捕获任务包刷新已完成，未来真实 GUI 捕获仍待执行。

## 建议 commit message

```text
docs: review current PCB2 mapping and protection evidence
```
