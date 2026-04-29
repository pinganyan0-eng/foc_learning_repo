from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.strip() + "\n", encoding="utf-8")


def write_json(path: str, data: object) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    write(
        "ROADMAP.md",
        """
# ROADMAP

## 当前阶段

- 学习助手环境已建立。
- 项目事实源、联网核查规则、JEOC 审查模板、实验记录模板、协议模型和本地检索库已落地。
- 正在把仓库升级为“工程可构建 + 学习可追踪 + 答辩可复用”的竞赛工程结构。

## 下一阶段

1. 放入真实 STM32CubeMX / MCSDK 工程到 `apps/stm32_g474_foc/`。
2. 放入真实 ESP32-C3 网关工程到 `apps/esp32_c3_gateway/`。
3. 把每次联调记录放到 `experiments/YYYY-MM-DD_topic/`。
4. 把答辩报告、PPT、视频脚本放到 `deliverables/`。
5. 把官方资料和 Datasheet 索引补齐到 `references/`。
""",
    )
    write(
        "CHANGELOG.md",
        """
# CHANGELOG

## 2026-04-30

- 初始化学习助手仓库。
- 固化 V9、技术报告、学习计划和 Drive 核心笔记。
- 新增 `AGENTS.md`、项目事实源、联网核查规则。
- 新增竞赛工程仓库骨架。
""",
    )

    write_json(
        ".vscode/extensions.json",
        {
            "recommendations": [
                "ms-vscode.cpptools",
                "ms-vscode.cmake-tools",
                "stmicroelectronics.stm32-vscode-extension",
            ]
        },
    )
    write_json(
        ".vscode/settings.json",
        {
            "files.encoding": "utf8",
            "C_Cpp.default.configurationProvider": "ms-vscode.cmake-tools",
            "codex.projectRules": "AGENTS.md",
        },
    )
    write_json(
        ".vscode/launch.json",
        {
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "Placeholder STM32 debug",
                    "type": "cppdbg",
                    "request": "launch",
                    "program": "${workspaceFolder}/apps/stm32_g474_foc/build/firmware.elf",
                    "cwd": "${workspaceFolder}",
                    "preLaunchTask": "",
                    "externalConsole": False,
                }
            ],
        },
    )

    write(
        "apps/stm32_g474_foc/AGENTS.md",
        """
# STM32 工程规则

1. 不要随意改 CubeMX / MCSDK 自动生成区域。
2. 优先只改 `USER CODE BEGIN` 与 `USER CODE END` 区间，或新增独立用户模块。
3. 涉及 PWM、TIM1、ADC、OPAMP、DMA、FOC ISR、过流保护时，必须先说明风险。
4. 修改后必须说明如何编译、如何测试、如何不上电验证、如何限流上电验证。
5. 不要把 `printf`、`HAL_Delay`、JSON 解析、WebSocket、malloc/free 或长耗时逻辑放进 JEOC / FOC 高频中断。
6. 真实工程导入前，本目录只作为占位骨架。
""",
    )
    write(
        "apps/stm32_g474_foc/README.md",
        """
# STM32G474 FOC 工程

这里放真实 STM32CubeMX / MCSDK 生成工程。

## 保留原则

- 保持 CubeMX / MCSDK 原生结构，不为了目录好看拆散 `Core/`、`Drivers/`、`Middlewares/`、`MotorControl/`。
- `.ioc`、`CMakeLists.txt` 或 `Makefile` 放在本目录根部。
- 用户新增模块优先放在 CubeMX 允许保留的位置，或放入独立 `User/` 后在构建系统里显式引用。

## 待放入

- `STM32G474_FOC.ioc`
- `Core/`
- `Drivers/`
- `Middlewares/`
- `MotorControl/`
- `CMakeLists.txt` 或 `Makefile`
""",
    )
    for path in [
        "apps/stm32_g474_foc/Core/.gitkeep",
        "apps/stm32_g474_foc/Drivers/.gitkeep",
        "apps/stm32_g474_foc/Middlewares/.gitkeep",
        "apps/stm32_g474_foc/MotorControl/.gitkeep",
        "apps/stm32_g474_foc/Debug/.gitkeep",
        "apps/stm32_g474_foc/Release/.gitkeep",
    ]:
        write(path, "")

    write(
        "apps/esp32_c3_gateway/AGENTS.md",
        """
# ESP32-C3 网关工程规则

1. UART 协议必须以 `interfaces/uart_protocol.md` 为准。
2. 不要随意改 STM32 侧字段名。
3. WebSocket 推送频率默认 20Hz。
4. 串口收包必须考虑断帧、丢包、checksum、seq。
5. 源文件多时拆 `components/`，不要全部塞进 `main/`。
6. ESP32-C3 只做边缘网关，不进入 STM32 FOC 实时控制环。
""",
    )
    write(
        "apps/esp32_c3_gateway/README.md",
        """
# ESP32-C3 边缘网关工程

这里放真实 ESP32-C3 工程。推荐按 ESP-IDF 习惯组织：

- `main/`：入口和轻量 glue code。
- `components/uart_bridge/`：STM32 UART 透传。
- `components/websocket_server/`：WebSocket 服务。
- `components/web_ui/`：本地看板资源。
- `components/telemetry_protocol/`：帧解析、校验、序号和错误处理。
""",
    )
    write("apps/esp32_c3_gateway/main/app_main.c", "/* Placeholder. Import the real ESP32-C3 app here. */")
    for comp in ["uart_bridge", "websocket_server", "web_ui", "telemetry_protocol"]:
        write(f"apps/esp32_c3_gateway/components/{comp}/README.md", f"# {comp}\n\n真实 ESP-IDF component 导入后补充说明。")
    write("apps/esp32_c3_gateway/sdkconfig.defaults", "# Placeholder for ESP-IDF defaults")
    write("apps/esp32_c3_gateway/CMakeLists.txt", "# Placeholder. Replace with the real ESP-IDF CMakeLists.txt.")

    write(
        "interfaces/uart_protocol.md",
        """
# UART Protocol

STM32 与 ESP32-C3 之间采用 UART DMA + IDLE 接收，一行一个 JSON 帧，`\\n` 结尾。

## 基础命令帧

```json
{"cmd":"set_speed","rpm":1200,"seq":17}
```

## 基础状态帧

```json
{"type":"status","rpm":1180,"target_rpm":1200,"state":"RUNNING","fault":0,"seq":17}
```

## 规则

- 单帧建议不超过 256 字节。
- STM32 端必须做长度、末字节、JSON、字段类型、状态机五层校验。
- 速度命令进入实时环前必须被主循环校验并写入安全目标值。
- JEOC/FOC ISR 不解析 UART。
""",
    )
    write_json(
        "interfaces/uart_protocol.schema.json",
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "STM32 ESP32 UART command frame",
            "type": "object",
            "required": ["cmd"],
            "properties": {
                "cmd": {"type": "string", "enum": ["heartbeat", "arm", "set_speed", "stop", "clear_fault"]},
                "rpm": {"type": "integer", "minimum": -4000, "maximum": 4000},
                "seq": {"type": "integer", "minimum": 0},
            },
            "additionalProperties": True,
        },
    )
    write(
        "interfaces/stm32_status_frame.md",
        """
# STM32 Status Frame

STM32 周期性向 ESP32-C3 上报状态，默认用于 WebSocket 看板和 OLED 展示。

```json
{"type":"status","rpm":1180,"target_rpm":1200,"state":"RUNNING","fault":0,"bus_v":24.0,"iq":0.82}
```
""",
    )
    write(
        "interfaces/esp32_command_frame.md",
        """
# ESP32 Command Frame

ESP32-C3 从网页按钮或本地策略生成命令帧，转发给 STM32。

```json
{"cmd":"set_speed","rpm":1200,"seq":17}
```

ESP32 不直接修改 PI 参数、不直接控制 PWM、不进入 FOC 实时环。
""",
    )
    write(
        "interfaces/fault_codes.md",
        """
# Fault Codes

| Code | Name | Meaning |
| --- | --- | --- |
| 0 | OK | 正常 |
| 100 | ERR_BAD_JSON | JSON 解析失败 |
| 101 | ERR_BAD_FRAME | 帧格式错误 |
| 102 | ERR_UNKNOWN_CMD | 未知命令 |
| 103 | ERR_BAD_VALUE | 字段值非法 |
| 104 | ERR_STATE | 当前状态不允许 |
| 105 | ERR_FAULT | 故障态未清除 |
| 200 | HW_OVERCURRENT | 硬件过流 |
| 201 | HW_UNDERVOLTAGE | 欠压 |
| 202 | HW_NFAULT | STDRIVE101 nFAULT |
""",
    )

    docs = {
        "docs/00_project_truth/file_relationship.md": "# file_relationship\n\nV9、技术报告、Drive 核心笔记、学习计划、接口协议和实验日志的关系图谱。\n",
        "docs/00_project_truth/roles_abc.md": "# roles_abc\n\nA 硬件、B 算法/主控、C IoT 的职责和交接边界。\n",
        "docs/00_project_truth/source_priority.md": "# source_priority\n\n内部事实优先级：project_context -> V9 -> 技术报告 -> 硬件风险/Drive 笔记 -> 旧版本。\n外部动态事实必须联网核查官方来源。\n",
        "docs/00_project_truth/verified_parameters.md": "# verified_parameters\n\n用于沉淀已经由官方资料或实测确认的参数。未确认项必须写 TODO。\n",
        "docs/01_architecture/system_overview.md": "# system_overview\n\nSTM32G474 + STDRIVE101 + ESP32-C3 的系统总览。\n",
        "docs/01_architecture/foc_data_flow.md": "# foc_data_flow\n\nPWM -> ADC injected -> JEOC -> FOC -> SVPWM 更新的数据流。\n",
        "docs/01_architecture/tim1_adc_jeoc_timing.md": "# tim1_adc_jeoc_timing\n\n记录 TIM1_TRGO2、ADC injected、JEOC ISR 的时序。\n",
        "docs/01_architecture/safety_state_machine.md": "# safety_state_machine\n\n记录 IDLE / ARMED / RUNNING / FAULT 状态机和保护动作。\n",
        "docs/01_architecture/edge_gateway_arch.md": "# edge_gateway_arch\n\nESP32-C3 本地 AP、WebSocket、ECharts、OLED 与 STM32 UART 的关系。\n",
        "docs/02_algorithm_b/learning_index.md": "# learning_index\n\nB 同学学习入口：先 UART DMA+IDLE，再 MCSDK/Hall，最后 CORDIC/FMAC/SMO。\n",
        "docs/02_algorithm_b/adc_current_scaling.md": "# adc_current_scaling\n\nADC 电流换算记录。涉及硬件参数必须联网核查 Datasheet 并实测校准。\n",
        "docs/02_algorithm_b/clarke_park_svpwm.md": "# clarke_park_svpwm\n\nClarke/Park/SVPWM 学习笔记入口，不手写替代 MCSDK 主流程。\n",
        "docs/02_algorithm_b/hall_sequence.md": "# hall_sequence\n\nHall 顺序、相序、Phase Shift 和 Workbench 回填记录。\n",
        "docs/02_algorithm_b/pi_tuning.md": "# pi_tuning\n\n电流环/速度环 PI 调参记录。\n",
        "docs/02_algorithm_b/cordic_fmac.md": "# cordic_fmac\n\nCORDIC/FMAC 使用和 profiling 记录。版本相关信息必须联网查 ST 官方资料。\n",
        "docs/02_algorithm_b/smo_pll_sensorless.md": "# smo_pll_sensorless\n\nSMO/PLL 无感冲刺记录。\n",
        "docs/02_algorithm_b/go_nogo_sensorless.md": "# go_nogo_sensorless\n\n无感继续/止损判据。三天不稳定则保留 Hall 作为可靠方案。\n",
        "docs/02_algorithm_b/debug_playbook.md": "# debug_playbook\n\nB 同学调试手册：现象、证据、最小复现、排查树。\n",
        "docs/03_hardware_notes/pinmap.md": "# pinmap\n\nSTM32G474、STDRIVE101、NUCLEO Morpho/Arduino、Hall、UART 引脚映射。\n",
        "docs/03_hardware_notes/stdrive101_notes.md": "# stdrive101_notes\n\nSTDRIVE101 设计注意事项。以 Datasheet 和最新审查为准。\n",
        "docs/03_hardware_notes/current_sampling.md": "# current_sampling\n\n低侧三电阻、Kelvin、OPAMP/PGA、ADC injected 采样链路。\n",
        "docs/03_hardware_notes/protection_thresholds.md": "# protection_thresholds\n\nSCREF/VDS、过流、欠压、TVS、保险丝/PTC 等保护阈值。\n",
        "docs/03_hardware_notes/hardware_risk_checklist.md": "# hardware_risk_checklist\n\n上电前硬件风险清单。P0/P1 未关闭前不接电机。\n",
        "docs/04_iot_gateway/uart_dma_idle.md": "# uart_dma_idle\n\nUART DMA + IDLE 接收和断帧处理。\n",
        "docs/04_iot_gateway/websocket_api.md": "# websocket_api\n\nWebSocket API 和推送节奏，默认 20Hz。\n",
        "docs/04_iot_gateway/web_dashboard.md": "# web_dashboard\n\nECharts 看板字段、布局和演示要点。\n",
        "docs/04_iot_gateway/offline_control_policy.md": "# offline_control_policy\n\n断网不失控策略：STM32 本地保护优先，ESP32 只显示和转发。\n",
        "docs/05_test_and_logs/test_plan.md": "# test_plan\n\n软件、硬件、联调、答辩验收测试计划。\n",
        "docs/05_test_and_logs/bringup_checklist.md": "# bringup_checklist\n\n首次上电、空载 PWM、Gate 波形、限流、nFAULT、接电机前检查。\n",
        "docs/05_test_and_logs/final_acceptance.md": "# final_acceptance\n\n最终验收标准和证据索引。\n",
        "docs/06_defense_pack/b_algorithm_script_4min.md": "# b_algorithm_script_4min\n\nB 同学 4 分钟算法讲解稿。\n",
        "docs/06_defense_pack/defense_30qa.md": "# defense_30qa\n\n评委可能问的 30 个问题与回答。\n",
        "docs/06_defense_pack/judge_hard_questions.md": "# judge_hard_questions\n\n硬问题：为什么 G474、为什么 STDRIVE101、为什么 Hall 保底、为什么 SMO 止损。\n",
        "docs/06_defense_pack/demo_script.md": "# demo_script\n\n演示流程脚本。\n",
        "docs/06_defense_pack/evidence_index.md": "# evidence_index\n\n实测证据索引：日志、波形、截图、视频、提交物。\n",
        "docs/90_archive/v7_1_notes.md": "# v7_1_notes\n\nV7.1 历史版本记录，不作为最终实现第一依据。\n",
        "docs/90_archive/v8_notes.md": "# v8_notes\n\nV8 历史版本记录，用于追溯修正原因。\n",
        "docs/90_archive/v9_summary.md": "# v9_summary\n\nV9 摘要。完整来源见 `materials/extracted/v9_final.txt`。\n",
        "docs/90_archive/hallucination_fixes.md": "# hallucination_fixes\n\n历代 AI 幻觉、计算错误和修正依据。\n",
    }
    for path, content in docs.items():
        write(path, content)

    for week in ["week1_nucleo_baseline", "week2_hall_closed_loop", "week3_self_board", "week4_cordic_fmac_profile", "week5_smo_experiment"]:
        write(f"docs/05_test_and_logs/{week}.md", f"# {week}\n\n按实验记录模板补充。\n")

    write(
        "experiments/README.md",
        """
# Experiments

每次联调按日期和主题建目录：

```text
experiments/2026-05-01_hall_sequence/
├─ README.md
├─ raw_log.csv
├─ scope_screenshot.png
└─ conclusion.md
```

不要只写“成功/失败”，必须保留操作步骤、硬件状态、固件版本、日志、波形和结论。
""",
    )
    write(
        "experiments/_template/README.md",
        """
# 实验记录

## 目标

## 硬件状态

## 固件状态

## 操作步骤

## 原始数据

## 结论

## 给 Codex 定位问题时的最小上下文
""",
    )
    write("experiments/_template/raw_log.csv", "time_ms,event,value\n")
    write("experiments/_template/conclusion.md", "# conclusion\n\n")

    write(
        "tools/README.md",
        """
# Tools

- `build_vector_store.py`：构建本地检索索引。
- `ask_local.py`：基于本地资料问答。
- `run_rehearsal.py`：Suggest -> Auto Edit -> 验证 -> 回滚演练。
- `log_parser/`：后续放串口日志解析工具。
- `plot_current_speed/`：后续放电流/速度画图工具。
- `uart_frame_tester/`：后续放 UART 帧测试工具。
""",
    )
    for name in ["log_parser", "plot_current_speed", "uart_frame_tester"]:
        write(f"tools/{name}/README.md", f"# {name}\n\n待实现。\n")

    write("assets/README.md", "# Assets\n\n放图、视频、drawio 图和答辩素材源文件。\n")
    write("assets/diagrams/README.md", "# Diagrams\n\n系统架构、FOC 数据流、PWM/ADC/ISR 时序图。\n")
    write("assets/images/README.md", "# Images\n\n波形、硬件照片、看板截图。\n")
    write("assets/videos/README.md", "# Videos\n\n演示视频素材。\n")

    write(
        "deliverables/README.md",
        """
# Deliverables

这里放比赛最终交付品，不和工程知识库 `docs/` 混放。

- `report/`
- `slides/`
- `demo_video_script/`
- `submission_checklist.md`
""",
    )
    write("deliverables/report/README.md", "# Report\n\n最终报告和导出 PDF。\n")
    write("deliverables/slides/README.md", "# Slides\n\n答辩 PPT。\n")
    write("deliverables/demo_video_script/README.md", "# Demo Video Script\n\n视频脚本和分镜。\n")
    write(
        "deliverables/submission_checklist.md",
        """
# Submission Checklist

- 报告
- PPT
- 演示视频
- 源码归档
- BOM / 原理图 / PCB 关键截图
- 实测证据索引
- 版本说明
""",
    )

    write(
        "references/official_links.md",
        """
# Official Links

- ST STM32CubeIDE / STM32CubeIDE for VS Code: https://www.st.com/en/development-tools/stm32vscode.html
- ST STM32CubeIDE for VS Code documentation: https://dev.st.com/stm32cube-docs/stm32cubeide-vscode/1.0.0/en/docs/markup/development/projects.html
- ST STM32CubeIDE for VS Code CMake documentation: https://dev.st.com/stm32cube-docs/stm32cubeide-vscode/1.0.0/en/docs/markup/basic_concepts/cmake.html
- ESP-IDF Programming Guide: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/build-system.html
- OpenAI Codex Help Center: https://help.openai.com/en/articles/11369540
""",
    )
    write(
        "references/datasheet_index.md",
        """
# Datasheet Index

待补官方 PDF 路径、版本、发布日期、关键页码。

- STM32G474RE Datasheet
- RM0440 Reference Manual
- DS13472 STDRIVE101 Datasheet
- AN5306 OPAMP Application Note
- EVLDRIVE101-HPD UM3257
- MPS DC-DC Datasheet
- NCEP40T11G MOSFET Datasheet
""",
    )
    write(
        "references/do_not_trust_random_sources.md",
        """
# Do Not Trust Random Sources

以下来源只能作为线索，不能直接作为工程结论：

- CSDN 搬运文
- B 站评论区
- 淘宝详情页
- 不明来源 PDF
- AI 生成博客
- 没有日期、版本号、出处的教程
""",
    )

    write(
        "materials/link_69f259fc_summary.md",
        """
# 链接 t_69f259fc 固化摘要

来源：`https://chatgpt.com/s/t_69f259fcb988819194d1c21ef795da43`

## 核心要求

把仓库从“资料堆放型”升级为“工程可构建 + 学习可追踪 + 答辩可复用”的竞赛工程仓库。

## 落地原则

- 代码、文档、实验数据、答辩材料、AI 指令分层。
- STM32 与 ESP32 分仓管理，分别放在 `apps/stm32_g474_foc/` 与 `apps/esp32_c3_gateway/`。
- V9 事实源和实测数据单独沉淀。
- MCSDK/CubeMX 生成代码不要为了好看乱拆。
- ESP32 源文件多时拆 `components/`，不要全部塞进 `main/`。
- 接口契约单独放入 `interfaces/`。
- `deliverables/` 单独放比赛提交物，不混入 `docs/`。

## 已落实

- 新增 `apps/`、`interfaces/`、分层 `docs/`、`experiments/`、`assets/`、`deliverables/`、`references/`。
- 新增 STM32/ESP32 分层 `AGENTS.md`。
- 新增 `.vscode/` 推荐配置。
- 更新本地检索索引入口。
""",
    )


if __name__ == "__main__":
    main()
