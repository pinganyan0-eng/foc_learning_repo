# STM32 工程规则

1. 不要随意改 CubeMX / MCSDK 自动生成区域。
2. 优先只改 `USER CODE BEGIN` 与 `USER CODE END` 区间，或新增独立用户模块。
3. 涉及 PWM、TIM1、ADC、OPAMP、DMA、FOC ISR、过流保护时，必须先说明风险。
4. 修改后必须说明如何编译、如何测试、如何不上电验证、如何限流上电验证。
5. 不要把 `printf`、`HAL_Delay`、JSON 解析、WebSocket、malloc/free 或长耗时逻辑放进 JEOC / FOC 高频中断。
6. 真实工程导入前，本目录只作为占位骨架。
