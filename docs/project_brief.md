# project_brief

## 项目一句话

基于 STM32G474 的边缘网关型无感 FOC 驱动系统：用 G474 片上高精度模拟外设与硬件加速资源完成电机实时控制，用 ESP32-C3 做本地边缘网关，实现断网可控、可视化监测和故障上报。

## 竞赛定位

- 赛道：嵌入式芯片与系统设计竞赛，ST 赛道，工业 4.0 方向。
- 核心板卡：NUCLEO-G474RE。
- 功率驱动：STDRIVE101 自研三相功率板。
- 采样：低侧三电阻，Kelvin 走线，STM32G474 内部 OPAMP/PGA + ADC injected。
- 网关：ESP32-C3，本地 AP/WebSocket/ECharts/OLED，不进入 FOC 实时控制环。
- 工具链：VS Code + STM32CubeIDE 插件 + STM32CubeMX + MCSDK；不使用独立 STM32CubeIDE 作为主 IDE。

## 团队角色

- A 硬件：功率板、采样链路、保护链路、上电安全、版图与实测波形。
- B 算法/主控：VS Code + STM32CubeIDE 插件、CubeMX、MCSDK、Motor Profiler、Hall 闭环、PI 调参、JEOC 时序、UART DMA + IDLE、SMO 冲刺。
- C IoT：ESP32-C3 网关、WebSocket 看板、OLED、报警转发、断网演示。

## B 同学默认学习路线

1. 工具链认知：VS Code、STM32CubeIDE 插件、CubeMX、MCSDK、Motor Profiler、CubeMonitor 各干什么。
2. NUCLEO 基础：GPIO、USART、TIM、ADC、DMA、调试输出。
3. 通信基础：`HAL_UARTEx_ReceiveToIdle_DMA()` + `HAL_UARTEx_RxEventCallback()` + 环形缓冲。
4. MCSDK 起步：Motor Profiler 测 Rs/Ls/Ke，先生成 Hall FOC 工程。
5. 有感闭环保底：相序、Hall 顺序、PI 参数、电流环、速度环。
6. 实时时序：TIM1 center-aligned PWM -> TRGO2 -> ADC injected -> JEOC -> FOC。
7. 优化加分：CORDIC、FMAC、OPAMP/PGA、故障状态机、日志证据。
8. 无感冲刺：SMO/PLL + I/F 强拖启动；三天不稳定则保留 Hall 作为最终可靠方案。

## 助手回答原则

- 先确认阶段：工具环境、硬件审查、MCSDK、Hall、SMO、UART/IoT、报告答辩。
- 给当天可执行动作，不把问题讲成抽象大课。
- 遇到故障先要证据：电源限流、示波器波形、CubeMX/MCSDK 参数、串口日志、错误码、状态机状态。
- 对上电、接电机、改保护阈值、进实时中断等高风险动作要先拦一下。
