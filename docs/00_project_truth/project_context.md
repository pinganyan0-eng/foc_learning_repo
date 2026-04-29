# project_context

这是本仓库的最高优先级项目事实源。后续如果 V9、技术报告、聊天记录、临时笔记互相冲突，先读这里。

## 当前项目事实

- 项目名称：基于 STM32G474 的边缘网关型无感 FOC 驱动系统。
- 竞赛方向：嵌入式芯片与系统设计竞赛，ST 赛道，工业 4.0 方向。
- 主控：NUCLEO-G474RE / STM32G474RE。
- 功率驱动：STDRIVE101 自研三相功率板。
- 电流采样：低侧三电阻，Kelvin 走线，G474 内部 OPAMP/PGA + ADC injected。
- 网关：ESP32-C3，本地 AP/WebSocket/ECharts/OLED，负责边缘看板和告警展示。
- 实时控制：STM32 负责 FOC 实时环，ESP32 不进入实时控制环。
- 算法路线：先 Motor Profiler + MCSDK，Hall 有感闭环保底，再冲刺 SMO/PLL 无感。
- 实时时序：TIM1 center-aligned PWM -> TIM1_TRGO2 -> ADC injected -> JEOC -> FOC。

## 当前团队策略

- 不从零手写完整 FOC 数学，优先使用 ST 官方 MCSDK 生成工程框架。
- 不一开始追求无感，先把 Hall 闭环稳定跑起来。
- 不在 JEOC/FOC ISR 内放 `printf`、`HAL_Delay`、JSON 解析、WebSocket、动态内存或长耗时逻辑。
- UART 通信默认采用 DMA + IDLE + 一行一个 JSON 帧，`\n` 结尾。
- 第一次上电和接电机之前，必须先完成限流、空载 PWM、Gate 波形、nFAULT、VS/REG12/VREG 和采样链路检查。

## 项目内部文件优先级

1. 本文件。
2. `materials/extracted/v9_final.txt`。
3. `materials/extracted/tech_report_v1.txt`。
4. `docs/hardware_risks.md`、`materials/drive_core_notes.md`、V8/V7.1/工程盲区排查/交叉核查笔记。
5. 旧聊天记录、临时笔记、早期采购清单。

## 外部动态事实

以下内容不由 V9 最终决定，必须联网核查官方或高可信来源：

- MCSDK、CubeMX、CubeIDE、STM32Cube for VS Code、HAL/LL 库版本。
- STM32G474、STDRIVE101、CORDIC、FMAC、OPAMP、TIM1、ADC、EVLDRIVE101-HPD 官方资料。
- 器件库存、替代料、LCSC/立创价格和封装。
- OpenAI Codex、VS Code 插件、网络权限和 CLI 行为。
- 比赛时间、规则、提交要求。

## 冲突处理

- V9 与早期方案冲突：默认采用 V9。
- V9 与官方 Datasheet 冲突：默认相信官方 Datasheet，先提示风险，不直接改硬件参数。
- 官方资料与实测数据冲突：先检查测试条件、仪器、接线和版本，再判断是否需要修正文档。
- AI 生成内容与任何官方资料冲突：AI 生成内容降级为参考。

## 三句话原则

```text
V9 决定“我们项目当前怎么做”。
联网搜索决定“外部世界现在到底是不是这样”。
实测数据决定“我们的板子实际上有没有跑通”。
```
