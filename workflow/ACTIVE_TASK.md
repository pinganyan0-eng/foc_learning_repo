# 当前任务

这是当前唯一任务，不是长期计划。每次执行前先读本文件，再按任务边界执行；任务完成后由 Codex 更新结果区，并由 ChatGPT 继续教学、拆解或复盘。

## Task ID

- ID：TASK-2026-05-18-p2-packet-a-capture-prep
- 主题：P2 Packet A Workbench 捕获任务包整理
- Status：open/ready
- Risk Level：L0
- Definition of Done：`workflow/definition_of_done.md#仓库维护任务`
- Evidence ID：EV-2026-05-18-P2-PACKET-A-TASK-PACKAGE-001
- Review Required：yes

## 背景

P2 MCSDK 无功率预检已经有旧 `My_First_FOC.stwb6`、2026-05-16 自定义 NUCLEO + STDRIVE101 捕获包，以及 2026-05-17 供应商电机和 G431/G474 pin 表线索。它们仍然只是 `Partial clue / Preparation only`，因为还没有项目专用 `.stwb6` 和 Workbench 选项截图。

## 当前阶段

真实工程仍处于 P2 无功率预检。Packet A 尚未被接受，generated-project trust 仍为 `Not allowed`。本任务只整理下一步 Packet A 捕获任务包，不打开 GUI，不生成代码，不构建，不烧录，不接硬件。

## 任务目标

新增 2026-05-18 Packet A 捕获任务包，固定未来 `.stwb6` 保存路径、截图清单、停止条件和字段验收矩阵，并刷新状态入口，确保下一次 GUI 捕获可以直接执行且不会越过 P2 安全边界。

## 允许做

- 新增 `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_task_2026-05-18.md`。
- 更新 `workflow/ACTIVE_TASK.md`。
- 更新 `CURRENT_STATUS.md`。
- 更新 `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`。
- 更新 `apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md`。
- 更新 `workflow/evidence_register.md`。
- 运行文档索引和回归测试命令。

## 禁止做

- 不启动 Workbench GUI。
- 不创建新的 `.stwb6`。
- 不新增截图。
- 不生成 MCSDK/CubeMX 源码。
- 不构建、烧录或运行生成的电机控制工程。
- 不接 24V。
- 不接功率板。
- 不接电机。
- 不输出 Gate PWM。
- 不运行 Motor Profiler。
- 不升级 Packet A、Packet B/C、`PB3`/SWO 或 generated-project trust 结论。
- 不自动 commit。
- 不自动 push。

## 输入文件

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/workbench_no_power_configuration_guide_2026-05-16.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/README.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_checklist_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `workflow/evidence_register.md`
- `CURRENT_STATUS.md`

## 输出文件

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_task_2026-05-18.md`
- `workflow/ACTIVE_TASK.md`
- `CURRENT_STATUS.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md`
- `workflow/evidence_register.md`

## 验收证据

- 任务包写明未来 `.stwb6` 路径：
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/custom_nucleo_stdrive101_2026-05-16.stwb6`。
- 任务包写明未来截图目录和必需截图名。
- 字段验收矩阵覆盖 MCU/board、custom/generic power stage、FOC、Hall first path、3-shunt/OPAMP、TIM1 complementary PWM、`PB12/TIM1_BKIN`、`PA2/PA3` 排除策略和 `PB3`/SWO 状态。
- 状态文件明确这是 workflow-only 任务治理证据，不升级任何 Packet A/B/C 或硬件结论。
- `python -m unittest discover -s tests` 通过。
- `python tools/build_vector_store.py` 运行完成。

## 安全边界

本任务不允许任何 GUI、生成、构建、烧录或硬件动作。未来如果用户明确要求执行 Workbench 捕获，也必须继续保持无功率：只保存 `.stwb6` 和截图，不生成代码，不进入 Motor Profiler，不连接功率板或电机。

## 执行步骤

1. 读取现有 Packet A 捕获包、capture checklist、P2 readiness snapshot 和 evidence register。
2. 新增 2026-05-18 Packet A capture task package。
3. 更新活跃任务和状态入口。
4. 登记 workflow-only evidence。
5. 运行 `python -m unittest discover -s tests`。
6. 运行 `python tools/build_vector_store.py`。
7. 输出修改摘要、命令结果、`git status` 摘要和建议 commit message。

## Definition of Done

- 下一次 Packet A GUI 捕获不需要重新决定保存路径、截图清单、字段验收或停止条件。
- Packet A 仍保持 `Partial clue / Preparation only`。
- Generated-project trust 仍保持 `Not allowed`。
- 未修改固件、接口、CubeMX/MCSDK 生成目录、硬件参数、PWM、Gate 或 FOC 实时控制代码。

## Blocked Handling

如果命令失败、文件冲突或发现本任务会升级证据等级，Codex 应停止并记录失败命令、报错摘要、可能原因和下一步建议，不得绕过限制继续执行。

## Codex 结果区

- 执行状态：ready；任务包刷新已完成，未来真实 GUI 捕获仍待执行
- 修改文件：`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_task_2026-05-18.md`、`workflow/ACTIVE_TASK.md`、`CURRENT_STATUS.md`、`apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`、`apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md`、`workflow/evidence_register.md`
- 证据：`workflow/evidence_register.md` 中新增 `EV-2026-05-18-P2-PACKET-A-TASK-PACKAGE-001`；`python -m unittest discover -s tests` 成功，41 tests OK；`python tools\build_vector_store.py` 成功
- Evidence ID：EV-2026-05-18-P2-PACKET-A-TASK-PACKAGE-001
- 失败命令：无
- 剩余风险：Packet A 仍需未来真实 `.stwb6` 和 Workbench selected-field screenshots；Packet B/C、`PB3`/SWO、`J_HALL` 和 STDRIVE101 保护路径仍未接受。

## 建议 commit message

```text
docs: add P2 Packet A capture task package
```
