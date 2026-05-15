# 阶段闸门表

用途：防止项目还没满足前置条件就跳到高风险步骤。每次说“进入下一阶段”前，先对照本表。

## 总原则

- 不能用口头感觉替代证据。每个阶段至少要有文件、日志、截图、波形或测试结果之一。
- 涉及上电、PWM、电机、保护阈值和无感切换时，必须先回到限流、仪器和回退方案。
- Hall 闭环是保底路线，SMO 无感是冲刺路线。无感不稳定时，不影响项目以 Hall 方案完成演示和答辩。

## 阶段闸门

| 阶段 | 进入条件 | 产出证据 | 通过标准 | 禁止动作 |
| --- | --- | --- | --- | --- |
| 0. 助手与资料准备 | 已读 `CURRENT_STATUS.md`、`AGENTS.md`、`project_context.md` | 本仓库入口文件、资料索引、本地检索可用 | 能明确项目主线、资料优先级和安全红线 | 不把旧聊天或早期采购清单当最终事实 |
| 1. Windows 工具链 | 准备安装或核查 VS Code、STM32CubeIDE 插件、CubeMX、MCSDK、ST-LINK、串口工具 | 工具版本记录、安装截图或命令输出 | 能在 VS Code + STM32CubeIDE 插件和 CubeMX 中识别 NUCLEO-G474RE，串口工具可用 | 不在版本未知时照搬教程参数，不把独立 STM32CubeIDE 当成本项目主 IDE |
| 2. NUCLEO 基础工程 | 有 NUCLEO-G474RE，尚未接功率板 | 点灯、串口、定时器、UART DMA + IDLE 的最小工程记录 | 能稳定下载、复位、打印日志，DMA IDLE 能收完整帧 | 不接 24V，不接电机，不开三相功率输出 |
| 3. MCSDK Motor Profiler | 工具链可用，电机和功率链路准备接受低风险测试 | Motor Profiler 配置、扫描参数、生成工程 | 获取电机参数，能生成可编译工程 | 不跳过限流，不用未核查的功率板大电流测试 |
| 4. Hall 闭环保底 | MCSDK 工程可编译，Hall 和相线接入方案明确 | Hall 顺序、相序、PI 参数、串口日志、速度曲线 | 空载低速稳定运行，无异常过流、过温、nFAULT | 不直接冲高转速，不带载长时间运行 |
| 5. 自研板首次上电 | 原理图、BOM、关键器件和保护阈值已审查 | 上电检查记录、万用表读数、示波器 Gate 波形 | VS/REG12/VREG/nFAULT 正常，同桥臂 Gate 不重叠，死区符合设计 | 不接电机，不放开电源限流，不绕过保护 |
| 6. 自研板 Hall 运行 | 首次上电和空载 PWM 已通过 | 串口日志、示波器截图、实验记录 | 低速空载稳定，电流和温升可解释，故障链路可复现 | 不直接做 SMO，不做 24V 大电流带载 |
| 7. SMO/PLL 无感冲刺 | Hall 闭环可用，电机参数和电流采样可信 | I/F 启动参数、SMO/PLL 观测日志、失败记录 | 至少能说明成功区间、失败边界和回退策略 | 不把不稳定无感写成已完成能力 |
| 8. ESP32-C3 网关 | STM32 端协议稳定，实时环不依赖 ESP32 | UART 帧日志、WebSocket 页面、离线控制策略 | ESP32 只显示和转发，不影响 FOC 实时控制 | 不让 ESP32 进入实时控制环 |
| 9. 答辩交付 | 至少有一个可稳定演示的闭环方案 | 报告、PPT、视频脚本、实验证据索引 | 每个卖点能对应来源、数据或演示锚点 | 不写未经验证的性能指标 |

## 每次阶段推进时要更新

- `CURRENT_STATUS.md`：当前阶段、已通过闸门、下一步最小动作。
- `experiments/YYYY-MM-DD_topic/`：真实实验条件、步骤、现象和结论。
- `deliverables/submission_checklist.md`：如果阶段变化影响答辩材料。

## 2026-05-15 P2 No-Power Gate Insert

The phase table above is the long project ladder. The current project is not allowed to jump from NUCLEO basics directly to Motor Profiler. The following
insert is mandatory before stage 3 or any generated motor-control project is
trusted.

### P2-S1 - MCSDK No-Power Precheck

Entry condition:

- P1 NUCLEO command/log evidence exists.
- No power board, motor, 24V, Gate PWM, Motor Profiler, Hall closed-loop, or
  sensorless action is part of the work.

Required evidence:

- `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_intake_checklist_2026-05-14.md`

Pass condition:

- The repo can state exactly which evidence is present, which Packet A/B/C
  fields are blocked, and which hardware actions remain forbidden.
- Passing this gate does not authorize generated-project trust, flashing,
  power-board connection, motor connection, Gate PWM output, Motor Profiler,
  Hall closed-loop, or sensorless / SMO claims.

### P2-S2 - Build-Only Generated Project Gate

Entry condition:

- Packet A is accepted through
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_template_2026-05-14.md`.
- `future_build_only_gate_2026-05-15.md` has been applied.
- Packet B/C and PB3/SWO blockers are copied forward if still unresolved.

Allowed evidence:

- Generated project path.
- No-power build command and output.
- Compiler warnings, binary path, and size.
- Evidence wording that says build-only configuration familiarity.

Forbidden conclusions:

- Do not claim CN8 routing proof.
- Do not claim STDRIVE101 protection-path proof.
- Do not claim current-sense, Hall, Gate PWM, Motor Profiler, motor,
  power-stage, or sensorless behavior.
- Do not flash or run the generated project.

### P2 To P3 Blocker List

P3 Motor Profiler or any powered stage stays closed until all of these exist:

1. Accepted Packet A for MCSDK / MotorControl configuration.
2. Accepted Packet B for STM32 endpoint mapping and board route evidence.
3. Accepted Packet C for STDRIVE101 `DT/MODE`, `STBY`, `NFAULT`, `REG12`,
   `CP`, `SCREF`, `VS/VM`, bootstrap, and VDS monitoring proof.
4. PB3/SWO release or isolation evidence if Hall B remains on `PB3`.
5. No-power continuity / short-check record for the actual wiring stage.
6. current-limited bring-up settings, measurement points, stop conditions, and
   rollback image.
7. A new dated phase-gate decision that explicitly opens the powered action.
