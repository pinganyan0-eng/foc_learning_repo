# B 算法同学教学与交付总计划

本文件把两份 B 算法/主控学习计划转成仓库可执行的教学和交付规则。它不是新的技术事实源，而是把学习路线、每周上交物、教学节奏、补进度机制和安全闸门统一起来。

## 来源与优先级

### 本地计划来源

- `materials/extracted/algo_b_8week.txt`：B 算法/主控 8 周主线，强调每周 Must-Win、Git 交付物和里程碑封存。
- `materials/extracted/algo_56day.txt`：56 天逐日细化计划，强调每日验收、每周 tag、周报、截图、日志、视频和最终交付。

### 官方核验来源

- [ST X-CUBE-MCSDK](https://www.st.com/en/embedded-software/x-cube-mcsdk.html)：MCSDK 当前产品页显示 MCSDK 6.4.2，并确认 Workbench、Motor Profiler、FOC、3-shunt、Hall/encoder、sensorless observer 和 STM32CubeMX workflow 属于官方支持能力。
- [STM32CubeIDE for VS Code Projects](https://dev.st.com/stm32cube-docs/stm32cubeide-vscode/latest/en/docs/markup/development/projects.html)：官方文档确认 VS Code 插件支持 STM32CubeMX 生成工程，适合作为本项目主 IDE 口径。
- [STM32CubeIDE for VS Code Build](https://dev.st.com/stm32cube-docs/stm32cubeide-vscode/latest/en/docs/markup/development/build.html)：官方文档确认构建产物包括 `.elf`、`.hex`、`.bin`、`.map` 和 build logs，这些应作为 Codex 验证证据。
- [STM32G474RE datasheet](https://www.st.com/resource/en/datasheet/stm32g474re.pdf)：确认 G474 具备 CORDIC、FMAC、OPAMP/PGA、advanced motor-control timers、dead time 和 emergency stop 等能力。
- [AN5325 CORDIC application note](https://www.st.com/resource/en/application_note/an5325-getting-started-with-the-cordic-accelerator-using-stm32cubeg4-mcu-package-stmicroelectronics.pdf)：确认 CORDIC 对电机控制坐标变换有用，并给出 NUCLEO-G474RE 示例和性能测量方法；项目性能卖点必须用实测或官方基准支撑。
- [AN5306 OPAMP application note](https://www.st.com/resource/en/application_note/an5306-operational-amplifier-opamp-usage-in-stm32g4-series-stmicroelectronics.pdf)：确认 STM32G4 内置 OPAMP 可用于电机控制电流/电压采样等模拟前端。
- [STDRIVE101 datasheet](https://www.st.com/resource/en/datasheet/stdrive101.pdf)：确认 STDRIVE101 有 5.5 V 到 75 V 工作范围、deadtime/interlocking、VDS monitoring、OCP、UVLO、thermal shutdown 和 nFAULT；任何功率动作必须走阶段闸门。
- [ESP32-C3 serial connection](https://docs.espressif.com/projects/esp-idf/en/stable/esp32c3/get-started/establish-serial-connection.html) 和 [ESP32-C3 UART driver](https://docs.espressif.com/projects/esp-idf/en/stable/esp32c3/api-reference/peripherals/uart.html)：确认 ESP32-C3 可以通过 USB/UART 连接，UART 驱动提供 FIFO、事件和队列机制；ESP32 在本项目只做网关、显示、转发和告警，不进入 STM32 FOC 实时环。

### 冲突处理

1. `CURRENT_STATUS.md` 和 `workflow/phase_gate_checklist.md` 优先于 8 周/56 天计划。
2. 官方 Datasheet、Reference Manual、User Manual、Application Note 优先于 HTML 计划中的经验值。
3. HTML 计划中的日期只作为节奏参考，不作为硬件推进许可。
4. 原计划中的奖励、名次、性能数字和“必成”表述，全部降级为待验证目标。
5. 没有证据的 Motor Profiler、Hall 闭环、24V、功率板、电机、CORDIC/FMAC、SMO 结论不得写成已完成。

## 从两份计划提炼出的硬规则

1. 每次学习都要落到产物：代码、表格、图、日志、截图、问题清单、复盘或 Git 记录之一。
2. 每周必须有一次交付检查：本周做了什么、证据在哪里、没做什么、下周能不能推进。
3. 开工前先看昨天或上次的证据，不在旧功能坏掉时开始新功能。
4. 学习时间按 30/50/20 组织：30% 官方资料，50% 动手，20% 笔记和报告素材。
5. 每个阶段结束必须有可恢复锚点：commit、tag、实验记录、配置备份或证据索引。
6. 进度落后时先补关键交付物，不靠继续讲新概念制造“学过了”的错觉。
7. 硬件风险永远高于进度压力；任何日期都不能强迫进入 24V、功率板、电机或 PWM Gate 动作。

## 每次教学必须执行的进度检查点

ChatGPT 或 Codex 每次开始教学前，必须用 3 到 6 行说明：

```text
进度检查点：
- 当前真实阶段：
- 对应原计划位置：
- 本轮教学目标：
- 本轮要产出的东西：
- 当前是 on-track / catch-up / blocked：
- 本轮禁止范围：
```

如果不能判断，先读取：

1. `CURRENT_STATUS.md`
2. `workflow/algo_b_teaching_delivery_plan.md`
3. `workflow/phase_gate_checklist.md`
4. `workflow/teaching_contract.md`
5. `learning/weak_points.md`
6. `learning/review_queue.md`

## 教学节奏规则

| 情况 | ChatGPT 应做 | Codex 应做 | 不允许 |
| --- | --- | --- | --- |
| 新概念 | 用白话解释，给规则表，出 1-2 个检查题 | 等待接力，不抢主讲 | 不直接塞大段代码 |
| 代码阅读 | 按功能句子 -> 规则表 -> 函数职责 -> C 代码 -> 测试讲 | 打开真实代码、指出行号、验证构建或串口 | 不凭记忆说仓库状态 |
| 用户答错 | 修正原因，记录具体弱点 | 更新 `learning/`，必要时加复习队列 | 不笼统写“基础差” |
| 进度落后 | 停止扩展新知识，生成 catch-up 小任务 | 做最小验证和证据补齐 | 不靠跳过验收赶进度 |
| 需要上交物 | 明确让用户交什么、格式是什么、为什么交 | 把交付物入仓、建索引、验证路径 | 不只说“继续学” |
| 需要真实验证 | 明确交回 Codex | 构建、烧录、串口、日志、截图、证据登记 | 不让 ChatGPT 编造验证 |

## 补进度机制

### 进度状态定义

| 状态 | 定义 | 处理 |
| --- | --- | --- |
| `on-track` | 当前阶段的关键上交物和证据齐全 | 可以继续下一小节 |
| `catch-up` | 学过但缺交付物、缺证据或理解不稳 | 本轮只补一个关键缺口 |
| `blocked` | 缺硬件、缺文件、工具失败或阶段闸门未过 | 停止推进，写 blocked 原因 |
| `ahead-risk` | 日期或兴趣想跳到更高风险阶段 | 回到阶段闸门，先做低风险替代任务 |

### 进度债规则

出现以下任一情况，必须建立“进度债”并优先补：

- 学了概念但没有对应表格、日志、代码或复盘。
- 讲了硬件、PWM、Motor Profiler、Hall、SMO，但当前阶段没有证据。
- 串口、构建或实验只口头说通过，没有文件证据。
- 原计划要求周报、tag、验收清单，但仓库没有对应记录。
- 用户连续两次提醒双师分工或计划节奏，说明工作流失效。

进度债的修复顺序：

1. 安全边界和当前阶段事实。
2. 能证明已有功能的日志/截图/命令输出。
3. 用户已经学过但没有上交的表格/小练习。
4. 低风险代码或文档任务。
5. 更高阶段的预习材料。

## 优化后的阶段路线

本路线保留 8 周计划的交付纪律，但按当前真实阶段重排。阶段编号不是日历周，只有通过闸门才能进入下一阶段。

| 阶段 | 对应原计划 | 当前目标 | 必交产物 | Codex 验证 | 禁止范围 |
| --- | --- | --- | --- | --- | --- |
| P0 项目与助手固化 | Week 0/Week 1 前置 | 资料、仓库、双师工作流、状态页可恢复 | `CURRENT_STATUS.md`、资料索引、教学契约、任务包规则 | 文件存在、索引可查、测试通过 | 不碰硬件 |
| P1 NUCLEO 基础与 UART 命令 | Week 1 降级版 | 点灯、串口、状态机、命令解析、DMA + IDLE 基础 | UART 命令副作用表、COM5 日志、DMA + IDLE 接收流程图、学习复盘 | build、flash、COM5 串口日志、`learning/` 更新 | 不接 24V、功率板、电机、不输出三相 PWM |
| P2 MCSDK 无功率预检 | Week 1/2 过渡 | 熟悉 MCSDK/Workbench、生成工程、做引脚和参数草案 | 工具版本表、`.stmcx`/配置截图、pin map、Motor Profiler 计划、风险清单 | 构建记录、配置文件、无上电证据 | 不做真实 Profiler、不接电机 |
| P3 低风险电机参数与 Hall 保底 | Week 2 | 在满足硬件和限流条件后，获得电机参数并建立 Hall 闭环保底 | Profiler 参数、Hall 顺序表、PI 参数、速度曲线、Hall golden 文档 | Motor Profiler 记录、串口/CubeMonitor、视频或截图、tag | 不跳过限流和保护，不做 SMO |
| P4 自研板上电前审查 | Week 3 前半 | 原理图/BOM/PCB/保护阈值审查和不上电检查 | Datasheet 对照表、BOM 风险表、上电 SOP、仪器清单 | 审查文件、计算表、phase gate 记录 | 不直接上电、不接电机 |
| P5 自研板空载与 Hall 复现 | Week 3 后半 | 只在闸门通过后做空载 Gate 波形和低速 Hall 复现 | VS/REG12/VREG、nFAULT、Gate 波形、空载 PWM、低速日志 | 波形、照片、串口、实验记录 | 不大电流、不带载、不越过异常 |
| P6 G474 加速器与性能证据 | Week 4 | CORDIC/FMAC 学习和可量化性能验证 | CORDIC 笔记、q31 练习、ISR 耗时基线/对比、FMAC 滤波记录 | 构建、示波器或周期计数、图表 | 不夸大性能、不无证据写报告 |
| P7 无感 SMO/Observer 冲刺 | Week 5 | 在 Hall golden 已封存后，做独立无感分支和 GO/NO-GO | I/F 启动日志、Observer 参数表、成功率统计、决策记录 | 分支隔离、日志、50 次启动统计或失败证据 | 不破坏 Hall 版本，不死磕无感 |
| P8 网关、保护与冻结 | Week 6 | STM32 协议稳定，ESP32 只做显示/转发，建立保护状态机 | UART 协议、ESP32 网关日志、4 级故障状态机、冻结声明 | 接口测试、事件日志、evidence register、tag | ESP32 不进实时环，不冻结后加 feature |
| P9 报告、视频与答辩 | Week 7/8 | 把证据转成报告、PPT、视频、答辩 Q&A，随后切换考试/复习 | 报告章节、PPT、视频脚本、源码归档、证据索引 | 文档渲染、素材路径、提交截图 | 不把假设写成已完成 |

## 当前阶段执行计划

截至 2026-05-12，仓库真实阶段是 P1：NUCLEO 基础与 UART 命令。

### 当前执行层入口

长计划负责方向，执行层负责下一课。继续教学或补进度时按这个顺序读：

1. `learning/NEXT_LESSON.md`：下一课执行卡，包含进度检查点、P0/P1/P2 复习顺序、教学流程和验收标准。
2. `learning/MASTERY_MAP.md`：掌握证据地图，避免重复问已经证明的低价值问题，同时明确哪些高阶内容不能声称完成。
3. `workflow/current_learning_sprint.md`：当前 P1-S1 sprint，记录 catch-up 状态、交付物和退出条件。

执行层的目标是防止两种偏差：一是每次都从长计划重新推理，二是把所有 open review item 一次问完。下一课只处理 `NEXT_LESSON.md` 里的 P0/P1/P2 优先级。

### 当前已经有的证据

- NUCLEO baseline 工程已生成并构建通过。
- COM5 串口已验证 `PING`、`MODE?`、`ARM`、`STOP`、`SET_RPM <rpm>` 的学习用命令行为。
- 用户正在学习命令副作用、状态迁移、`target_rpm`、`mode_change_count`、DMA + IDLE 收包边界。
- 2026-05-12 已把 P1 catch-up 交付物包装进仓库：命令副作用表、DMA + IDLE 接收流程和 dated 交付包均已有路径。

### 当前不能上交的东西

- 不能上交 Motor Profiler 参数。
- 不能上交 Hall 闭环视频。
- 不能上交功率板 Gate 波形。
- 不能上交 CORDIC/FMAC 性能数据。
- 不能上交 SMO 无感结果。

这些不是缺勤，而是阶段未到。

### 当前必须补齐的上交物

| 上交物 | 负责人 | 文件建议 | 验收 |
| --- | --- | --- | --- |
| UART 命令分类和副作用表 | ChatGPT 教，用户答，Codex 入仓 | `docs/05_test_and_logs/week1_nucleo_baseline.md` | 已包装；下一步让用户用表独立解释 STOP/SET_RPM 副作用 |
| `STOP` 执行路径复习 | ChatGPT 教，Codex 记学习证据 | `learning/session_notes.md`、`weak_points.md` | 用户能算出 `IDLE + STOP` 与 `ARMED + STOP` 的最终变量 |
| DMA + IDLE 接收流程图 | ChatGPT 主讲，Codex 可画/入仓 | `docs/04_iot_gateway/uart_dma_idle.md` | 已包装；下一步让用户解释 `Size` 是 count，循环 `i < Size`，逐字节喂 `AppFeedRxByte` |
| NUCLEO 串口命令证据同步 | Codex | `experiments/2026-05-09_nucleo_baseline/`、`workflow/evidence_register.md` | 日志已跟踪或在证据登记里明确本地未跟踪状态 |
| 周交付复盘 | Codex 汇总，ChatGPT 复盘 | `deliverables/2026-05-12_p1_catchup_pack.md` | 已包装；仍明确 P2 MCSDK no-power precheck 暂不开始 |

## 每周上交流程

每 7 天，或完成一个 P 阶段后，必须做一次周交付检查。

### 周交付包模板

```text
周交付包：
- 周期：
- 当前阶段：
- 对应原计划：
- 本周完成：
- 本周上交物：
- 证据路径：
- 用户已掌握：
- 仍需复习：
- 进度债：
- 下周目标：
- 禁止推进范围：
- 是否允许进入下一阶段：yes / no
```

### 周交付最低标准

- 至少 1 个真实文件或证据路径。
- 至少 1 个用户理解证据或弱点记录。
- 至少 1 个下周可执行任务。
- 明确说明是否能进入下一阶段。

## 每日或每课上交物规则

每次课不一定都要大文件，但必须有一个小产物。

| 教学类型 | 小产物 |
| --- | --- |
| 概念课 | 1 张规则表或 3 个判断题结果 |
| 代码课 | 指出 2-4 行关键代码的职责 |
| 串口/协议课 | 一条命令的输入、输出、变量变化表 |
| DMA/中断课 | 一个数据流图或伪代码 |
| 硬件预习课 | 一个不上电检查清单 |
| 实验课 | 实验记录、日志、截图或波形 |
| 复盘课 | 本周完成/未完成/下一步列表 |

## ChatGPT 规则补丁

ChatGPT 每轮必须：

1. 先读本文件和 `CURRENT_STATUS.md`。
2. 先说进度检查点。
3. 把教学内容绑定到一个上交物。
4. 如果发现落后，不继续扩展新概念，先安排 catch-up。
5. 每轮最多问 1-2 个问题，但问题必须能推进当前上交物。
6. 涉及真实仓库、构建、串口、Git、学习记录、证据登记时，交回 Codex。
7. 不把原计划里的后续阶段当成当前已完成事实。

## Codex 规则补丁

Codex 每轮必须：

1. 先读 `CURRENT_STATUS.md`、本文件、`workflow/phase_gate_checklist.md` 和任务包。
2. 如果用户要求“继续教”，先判断是不是 ChatGPT 主讲场景；Codex 只在真实仓库、代码、验证、记录环节主导。
3. 任何代码、构建、烧录、串口、日志、截图、证据登记都要给出文件路径或命令结果。
4. 学习结束时更新 `learning/`，但不要让记录动作吞掉教学。
5. 每周或每阶段补齐周交付包。
6. 不自动 commit，不自动 push。
7. 不越过 `phase_gate_checklist.md`。

## 原计划需要优化的地方

1. **日期驱动改为证据驱动**：当前日期已经落后原计划日历，不能因此跳到 Week 4/5；按真实阶段推进。
2. **Week 1 需要拆分**：原计划把工具链、UART、Motor Profiler 和 ADC 核算压在一周，实际应拆成 NUCLEO 基础、MCSDK 无功率预检、再进入低风险电机参数阶段。
3. **硬件动作需要提前闸门**：原计划的 Week 3 上电流程方向正确，但必须先要求原理图 PDF、PCB、正式 BOM、Datasheet、保护阈值和仪器清单齐全。
4. **性能卖点需要证据约束**：CORDIC/FMAC 的性能数字不能照抄，应按 AN5325 或实际周期/示波器结果写。
5. **无感要有退出机制**：Week 5 必须有独立分支、Hall golden 不动、固定调参时间上限、GO/NO-GO 记录。
6. **ESP32 职责需要收窄**：ESP32 只做 JSON/网页/告警网关；STM32 通信层接收简化命令并做范围/状态防护；FOC 实时环不解析 JSON。
7. **每周交付物要纳入双师工作流**：ChatGPT 不只讲概念，Codex 不只改代码；双方都要推动上交物完成。
8. **考试/学业切换保留，但不管理竞赛事实**：Week 8 的学业防线是时间管理建议，不应写进工程完成状态。

## 下一次教学入口

当前最合适的 ChatGPT 教学任务：

```text
请先读取 CURRENT_STATUS.md、learning/NEXT_LESSON.md、learning/MASTERY_MAP.md、
workflow/current_learning_sprint.md、workflow/algo_b_teaching_delivery_plan.md、
workflow/teaching_contract.md、learning/weak_points.md 和 learning/review_queue.md。

进度检查点必须说明：
- 当前真实阶段是 P1 NUCLEO 基础与 UART 命令。
- 本轮上交物是 UART 命令分类和副作用表，或 DMA + IDLE 接收流程图。
- 本轮禁止进入 24V、功率板、电机、PWM Gate、Motor Profiler、Hall/SMO。

然后继续教我：
先按 learning/NEXT_LESSON.md 的 P0 优先级复查 STOP 副作用和 DMA Size/count；
如果通过，再教 PING / MODE? / ARM / SET_RPM / STOP 的命令分类、变量副作用和 DMA + IDLE callback 结构。
每轮最多问 1-2 个问题。

讲完后输出 Codex 接力点：
- 用户答对了什么
- 还错在哪里
- 要更新哪些 learning 文件
- 是否需要 Codex 做代码、编译或串口验证
```

当前最合适的 Codex 工程任务：

```text
补齐 P1 阶段交付物：
- 将 UART 命令分类和副作用表写入仓库
- 将本地 COM5 SET_RPM 验证日志纳入 Git 或在 evidence_register 中明确其未跟踪状态
- 更新周交付复盘
- 不改功率相关代码，不接 24V、不接功率板、不接电机
```
