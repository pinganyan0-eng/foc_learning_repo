# 证据登记表

本文件登记项目证据，帮助后续复盘、答辩和风险判断。证据可以来自构建输出、测试、串口日志、截图、波形、实验记录、Datasheet、人工复核或工具输出。

| Evidence ID | 日期 | 阶段 | 结论 | 证据类型 | 文件路径 | 关联任务 | 可信度 | 是否可用于答辩 | 待复核项 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EV-2026-05-09-NUCLEO-BUILD-001 | 2026-05-09 | NUCLEO 基础工程 | NUCLEO baseline 已构建通过但尚未板上运行验证 | 构建记录 | `apps/stm32_g474_foc/nucleo_g474re_baseline/` | NUCLEO baseline 工程建立 | 中：构建结论可信，板上运行未由本条证据证明 | 可用于说明“工程可构建”，不可用于说明“板上已跑通” | 需要补充下载运行、串口日志、LD2 观察或调试截图；如已有后续证据，应新增记录而不是覆盖本条 |
| EV-2026-05-11-WORKFLOW-HARDENING-001 | 2026-05-11 | 阶段 0/流程固化 | 双师制流程已补齐状态机、完成定义、证据登记、风险矩阵和提示词模板，维护命令通过 | 文档审计与命令结果 | `workflow/ACTIVE_TASK.md`、`workflow/task_state_machine.md`、`workflow/definition_of_done.md`、`workflow/evidence_register.md`、`workflow/risk_gate_matrix.md`、`workflow/prompt_recipes.md` | TASK-2026-05-11-dual-teacher-workflow | 高：文件和命令结果可复查；不代表硬件验证 | 可用于说明项目流程管理能力，不可用于说明电机或功率级已验证 | 需要 ChatGPT 或用户复盘后把任务状态从 `done` 升级为 `reviewed` |
| EV-2026-05-12-NUCLEO-SET-RPM-001 | 2026-05-12 | NUCLEO 基础工程 | NUCLEO baseline 通过 COM5 验证 `PING`、`MODE?`、`ARM`、`STOP` 和学习用 `SET_RPM <rpm>` 命令路径；`target_rpm` 仅为模拟变量 | 串口日志 | `experiments/2026-05-09_nucleo_baseline/logs/2026-05-12_com5_set_rpm_validation.md` | NUCLEO UART command validation | 高：板上串口日志可复查；仅证明 NUCLEO 命令路径，不证明电机或功率级能力 | 可用于说明 NUCLEO 串口命令和安全门验证，不可用于说明真实电机控制 | 仍需补 LD2 肉眼证据、UART DMA + IDLE 实现、后续 MCSDK/Hall/功率级分阶段验证 |
| EV-2026-05-12-WORKFLOW-PLAN-001 | 2026-05-12 | 阶段 0/教学与交付计划固化 | 两份 B 算法/主控 HTML 学习计划已消化为阶段化教学与交付总计划，并加入教学契约、Skill 源文件、提示词和收工检查；计划经 ST/ESP 官方资料重新核验关键边界 | 文档审计与官方来源核验 | `workflow/algo_b_teaching_delivery_plan.md`、`workflow/teaching_contract.md`、`workflow/prompt_recipes.md`、`codex_skills/stm32g474-foc-assistant/SKILL.md` | B algorithm teaching delivery plan optimization | 高：文件可复查，官方链接记录在计划内；不代表任何新增硬件或固件验证 | 可用于说明项目学习管理和交付治理能力，不可用于说明电机、功率级、MCSDK 或 ESP32 已验证 | 需要后续每周执行周交付包，并把 P1 当前上交物补齐 |
| EV-2026-05-12-LEARNING-SPRINT-001 | 2026-05-12 | P1 学习执行层 | P1 下一课执行卡、掌握证据地图和当前学习 sprint 已建立，复习队列按 P0/P1/P2 优先级重排，入口文件已指向执行层 | 文档审计与学习计划整理 | `learning/NEXT_LESSON.md`、`learning/MASTERY_MAP.md`、`workflow/current_learning_sprint.md`、`learning/review_queue.md` | P1 learning execution layer optimization | 高：文件可复查；不代表新增 firmware、板级或硬件验证 | 可用于说明教学执行层和学习闭环治理，不可用于说明新功能或硬件进度 | 需要下一次教学实际执行 P0 检查，并补 UART 命令副作用表、DMA + IDLE 流程图和 P1 交付包 |
| EV-2026-05-12-P1-PACK-001 | 2026-05-12 | P1 NUCLEO 基础与 UART 命令 | P1 catch-up 交付包已补齐：UART 命令副作用表、DMA + IDLE 接收流程和阶段复盘均进入仓库 | 文档交付包 | `docs/05_test_and_logs/week1_nucleo_baseline.md`、`docs/04_iot_gateway/uart_dma_idle.md`、`deliverables/2026-05-12_p1_catchup_pack.md` | P1 catch-up delivery packaging | 高：文件可复查；只证明教学资产已沉淀，不证明新增板级功能 | 可用于说明 P1 教学交付管理和 NUCLEO 命令防护设计；不可用于说明 MCSDK、功率级、电机、Hall 或 SMO | 需要学习者独立通过 P0 STOP/DMA 迁移检查；需要运行学习整理和测试命令 |
| EV-2026-05-13-P2-PRECHECK-001 | 2026-05-13 | P2 MCSDK 无功率预检 | P2 precheck card 已开始：记录本机工具版本/status、baseline `.ioc` 读回、MCSDK pin/config 草案、ST 官方来源交叉核验、pin-function 冲突处理、shell GUI 证据探测和未来 Motor Profiler 停止/回退计划；不代表 MCSDK 工程、Motor Profiler 或硬件验证 | 文档交付包、本机命令检查、官方来源核验 | `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`、`workflow/windows_toolchain_status.md`、`apps/stm32_g474_foc/nucleo_g474re_baseline/nucleo_g474re_baseline.ioc` | P2 MCSDK no-power precheck artifact | 高：文件和本机命令输出可复查；只证明无功率计划、冲突识别、缺失 GUI 证据和 pin-function 级决策，不证明 GUI 生成、构建、下载、功率级或电机行为 | 可用于说明 P2 安全预检和配置规划；不可用于说明 MCSDK 工程可构建、Motor Profiler 参数、Hall 闭环、PWM Gate 或功率板验证 | 需要补 Workbench/CubeMX 截图或真实 `.stmcx`、确认 `PB12/TIM1_BKIN` nFAULT 与 CN8/EDA/netlist、再决定是否生成无功率 MCSDK 工程 |
| EV-2026-05-13-ST-MANUAL-MIRROR-001 | 2026-05-13 | 资料治理 | 常用 ST 官方 PDF 已镜像到仓库并配套 manifest/hash/官方 URL；当前包括 RM0440、STM32G474 datasheet、UM2505、AN5306、UM3027、AN5397、AN4144、NUCLEO-G474RE brief 和 STDRIVE101 datasheet | 官方资料归档与索引 | `materials/raw/st_manuals/manifest.json`、`materials/raw/st_manuals/README.md`、`references/st_manuals_index.md`、`materials/extracted/st_manuals/` | ST official docs local mirror | 高：仓库内 PDF/hash/提取文本可复查；STDRIVE101 PDF 由用户浏览器下载后已归档并用 pypdf 抽取验证 | 可用于说明项目资料治理和离线检索能力；安全关键参数仍需对 PDF 页表和当前官网版本复核 | 后续若 ST 官网版本更新，需刷新 PDF、hash、提取文本和向量索引 |

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
