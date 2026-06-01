# 证据登记表

本文件登记项目证据，帮助后续复盘、答辩和风险判断。证据可以来自构建输出、测试、串口日志、截图、波形、实验记录、Datasheet、人工复核或工具输出。

| Evidence ID | 日期 | 阶段 | 结论 | 证据类型 | 文件路径 | 关联任务 | 可信度 | 是否可用于答辩 | 待复核项 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV-2026-05-09-NUCLEO-BUILD-001 | 2026-05-09 | NUCLEO 基础工程 | NUCLEO baseline 已构建通过但尚未板上运行验证 | 构建记录 | `apps/stm32_g474_foc/nucleo_g474re_baseline/` | NUCLEO baseline 工程建立 | 中：构建结论可信，板上运行未由本条证据证明 | 可用于说明“工程可构建”，不可用于说明“板上已跑通” | 需要补充下载运行、串口日志、LD2 观察或调试截图；如已有后续证据，应新增记录而不是覆盖本条 |
| EV-2026-05-11-WORKFLOW-HARDENING-001 | 2026-05-11 | 阶段 0/流程固化 | 双师制流程已补齐状态机、完成定义、证据登记、风险矩阵和提示词模板，维护命令通过 | 文档审计与命令结果 | `workflow/ACTIVE_TASK.md`、`workflow/task_state_machine.md`、`workflow/definition_of_done.md`、`workflow/evidence_register.md`、`workflow/risk_gate_matrix.md`、`workflow/prompt_recipes.md` | TASK-2026-05-11-dual-teacher-workflow | 高：文件和命令结果可复查；不代表硬件验证 | 可用于说明项目流程管理能力，不可用于说明电机或功率级已验证 | 需要 ChatGPT 或用户复盘后把任务状态从 `done` 升级为 `reviewed` |
| EV-2026-05-12-NUCLEO-SET-RPM-001 | 2026-05-12 | NUCLEO 基础工程 | NUCLEO baseline 通过 COM5 验证 `PING`、`MODE?`、`ARM`、`STOP` 和学习用 `SET_RPM <rpm>` 命令路径；`target_rpm` 仅为模拟变量 | 串口日志 | `experiments/2026-05-09_nucleo_baseline/logs/2026-05-12_com5_set_rpm_validation.md` | NUCLEO UART command validation | 高：板上串口日志可复查；仅证明 NUCLEO 命令路径，不证明电机或功率级能力 | 可用于说明 NUCLEO 串口命令和安全门验证，不可用于说明真实电机控制 | 仍需补 LD2 肉眼证据、UART DMA + IDLE 实现、后续 MCSDK/Hall/功率级分阶段验证 |
| EV-2026-05-12-WORKFLOW-PLAN-001 | 2026-05-12 | 阶段 0/教学与交付计划固化 | 两份 B 算法/主控 HTML 学习计划已消化为阶段化教学与交付总计划，并加入教学契约、Skill 源文件、提示词和收工检查；计划经 ST/ESP 官方资料重新核验关键边界 | 文档审计与官方来源核验 | `workflow/algo_b_teaching_delivery_plan.md`、`workflow/teaching_contract.md`、`workflow/prompt_recipes.md`、`codex_skills/stm32g474-foc-assistant/SKILL.md` | B algorithm teaching delivery plan optimization | 高：文件可复查，官方链接记录在计划内；不代表任何新增硬件或固件验证 | 可用于说明项目学习管理和交付治理能力，不可用于说明电机、功率级、MCSDK 或 ESP32 已验证 | 需要后续每周执行周交付包，并把 P1 当前上交物补齐 |
| EV-2026-06-01-HW-DMM-001 | 2026-06-01 | 自研板无电检查/局部 | 用户提供 Hall、LIN1、nFAULT、电源轨、BOOTx、三相 OUTx、R1/R2、R_GND_ISO、CN8 Pin15 和 Gate drive 的无电 DMM 读数；Hall/控制接口、主要电源轨、BOOTx、三相输出短路、SCREF 分压电阻本体、CN8 Pin15 到 GND_SIGNAL、Gate 到 GND 和 Gate 串阻路径均符合预期；SCREF 连接已有原理图截图/BOM 级证据，R1/R2 中点不可安全直接 DMM 探测 | 用户实测 DMM 记录 | `experiments/2026-06-01_power_board_no_power_dmm/logs/2026-06-01_hall_control_connector_dmm_check.md` | Power board no-power DMM check | 中：读数来自用户实测且已落档；SCREF 连接证据来自既有截图/BOM；方案、报告和部分官方资料已消化，但原始 EDA/netlist/PCB 源文件仍未入库 | 可用于说明局部无电检查已开始并排除若干明显短路，不可用于说明自研板可上 24V、可输出 PWM 或可接电机 | 后续硬件签核仍建议补原始 EDA/netlist/PCB-source 或高清网络高亮 |
| EV-2026-06-01-HW-POWER-PRECHECK-001 | 2026-06-01 | 自研板首次限流上电前准备 | 已新增功率板证据包缺口清单和首次限流上电前记录表；明确 24V/0.2A 级别限流、5V/3V3/REG12/nFAULT/输入电流观测点、立即断电条件和禁止接电机/PWM | 文档模板与安全检查清单 | `docs/03_hardware_notes/power_board_evidence_package.md`、`experiments/2026-06-01_power_board_first_limited_power_precheck/2026-06-01_first_limited_power_precheck_record.md` | Power board first limited power precheck preparation | 中：模板和证据包清单可复查；未执行上电，不代表硬件通过 | 可用于说明上电前安全流程，不可用于说明已上电或已跑通 | 需要补硬件签核资料：原始 EDA/PDF/PCB/BOM/Gerber/坐标和功率级器件规格页，并在现场执行前另起实际上电记录 |
| EV-2026-06-01-HW-STATIC-PWR-OPSHEET-001 | 2026-06-01 | 自研板首次限流静态上电准备 | 已新增 24V/0.2A 静态上电现场操作单；限定功率板单独上电、无电机、无 NUCLEO/MCU、无 PWM，记录电源 CC/CV、输入电流、5V、3V3、REG12、nFAULT 和异常发热/异味停止条件 | 现场操作单 | `experiments/2026-06-01_power_board_first_limited_power_precheck/2026-06-01_24v_0p2a_static_power_on_operation_sheet.md` | Power board 24V 0.2A static power-on preparation | 中：操作单可复查；尚未执行实际 24V 上电，不代表硬件通过 | 可用于说明首次静态上电流程已定义，不可用于说明已上电、可接电机或可输出 PWM | 现场执行后需把实测电流、电压、nFAULT、发热/异味和是否触发停止条件另行落档 |

## 字段说明

- `Evidence ID`：稳定证据编号，建议使用 `EV-YYYY-MM-DD-topic-序号`。
- `日期`：证据产生日期，不是登记日期。
- `阶段`：对应项目阶段或任务阶段。
- `结论`：只写该证据能支持的结论。
- `证据类型`：构建记录、测试输出、串口日志、截图、波形、实验记录、Datasheet、人工复核等。
- `文件路径`：仓库内相对路径；外部来源应先归档或记录到 `references/`。
- `关联任务`：对应 `workflow/ACTIVE_TASK.md` 或历史任务名。
- `可信度`：低/中/高，并说明限制。
- `是否可用于答辩`：区分可直接使用、只能作背景、不可使用。
- `待复核项`：下一步补证据或复核事项。
