# Drive 核心文档固化笔记

这些笔记来自共享链接中的 Google Docs 阅读结果，用于本地检索问答。若与早期方案冲突，以最新硬件审查、问题修复、V9/V8 和实测数据优先。

## STM32无感FOC边缘网关项目

- 项目：基于 STM32G474 的边缘网关型无感 FOC 驱动系统。
- 赛道：ST 工业 4.0 方向。
- 架构：NUCLEO-G474RE + STDRIVE101 功率板 + 低侧三电阻 Kelvin 采样 + ESP32-C3 边缘网关。
- 软件路线：Motor Profiler + MCSDK；前期 Hall 有感闭环保底，后期 SMO/PLL 无感冲刺。
- 实时时序：TIM1_TRGO2 硬件触发 ADC injected，JEOC 中断内执行 FOC 核心控制。

## STM32FOC 工业驱动系统实战指南

- 目标电气边界：24V、约 5A 级别演示系统。
- STDRIVE101：REG12/VREG 按手册接电容到地，BOOT 电容和栅极电阻必须按参考设计核对。
- 采样：低侧三电阻，推荐 20mΩ 合金采样电阻，Kelvin 差分走线。
- 版图：四层板、完整地平面、功率环路短、小信号采样避开开关节点。

## STM32G474 无感 FOC 终极指南

- G474 的价值：内部 OPAMP/PGA、CORDIC、FMAC、HRTIM/TIM1、高速 ADC。
- 不从零手写 FOC：先用 MCSDK 生成框架，再做参数、状态机、日志和加速资源优化。
- 无感不是第一天目标：Hall 闭环稳定后再冲 SMO/PLL；若短期不稳定，保留 Hall 方案。

## 嵌入式大赛项目汇报书

- 表达主线：高集成芯片降维、官方工具链、局域网边缘计算、断网可控。
- 答辩重点：G474 片上资源、硬件触发链、边缘网关、本地可视化、工业级保护、实测证据。

## STM32G474 STDRIVE101 电路审查

- 重大风险：原理图缺少真实 NUCLEO Morpho 物理连接器，只有网络名不等于可插接。
- 重大风险：缺少 24V 输入端子、电机 U/V/W 输出端子、保险丝/PTC/TVS 等完整功率接口。
- 电源风险：MP2459 电流能力偏弱；SY6288A 不是 5V 到 3.3V buck，不能当降压芯片。
- 保护风险：SCREF/VDS 阈值必须重新核算，早期 33k/20k 方案有严重误导风险。
- 采样风险：低侧采样信号必须真实引到 G474 OPAMP/ADC，不能只放采样电阻。
- 命名风险：Hall 信号不能命名成 IA/IB/IC，避免与三相电流混淆。

## 原理图审查与问题修复

- 仍需复核：SCREF/VDS、VS 去耦、保险丝/PTC、外部飞线供电、Hall 命名、NUCLEO 接口。
- 设计原则：数据手册 + 最新审查意见 + 实测验证优先于早期采购清单或早期方案。
- 上电前必须逐项核对：电源、驱动、保护、采样、接口、Gate 波形、nFAULT。

## 算法工程师八周冲刺学习清单

- 主线：CubeIDE/CubeMX/MCSDK -> UART DMA + IDLE -> MCSDK 3-shunt -> Motor Profiler -> Hall -> PI -> CORDIC/FMAC -> SMO -> 故障状态机 -> 报告。
- 禁区：不在 FOC ISR 中放 printf/delay/JSON/WebSocket；不一开始追求无感。

## 主控同学嵌入式竞赛学习计划

- 大一可行路线：依赖 HAL/CubeMX/MCSDK，不手推整套 FOC 数学。
- 先会工具和验证，再追求底层优化。
- 无 RTOS 裸机前后台即可，FOC 实时环保持短而确定。

## STM32 串口非阻塞通信学习笔记

- 推荐：UART DMA + IDLE + ring/FIFO。
- 关键 API：`HAL_UARTEx_ReceiveToIdle_DMA()` 和 `HAL_UARTEx_RxEventCallback()`。
- 避免断帧：关闭半满中断或明确处理半满事件；每帧用 `\n` 结尾；限制帧长；主循环解析 JSON。

## IoT工程师40天速成学习计划

- ESP32-C3 只做本地 AP/WebSocket/ECharts/OLED 和故障展示。
- STM32 与 ESP32 使用 UART DMA + IDLE + JSON over UART。
- ESP32 转发整帧时优先 `Serial.write(buffer, length)`，避免多次 `print()` 拼接造成 IDLE 误判。

## 硬件工程师速成 35 天学习计划

- A 同学优先读 STDRIVE101 数据手册、官方参考、四层板布局、Kelvin 采样、首次上电流程。
- 先证明电源和 Gate 波形安全，再接电机。

## 采购清单与导师建议

- 预算目标约 600 RMB，但采购方案遇到硬件审查冲突时，不按早期清单盲买。
- 导师沟通重点：电源保护、驱动器连接、采样链路、上电流程、版图审查、实测证据。
