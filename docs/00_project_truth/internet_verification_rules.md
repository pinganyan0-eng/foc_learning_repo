# internet_verification_rules

## 什么时候必须联网

只要问题涉及外部动态事实，就必须联网核查：

- 软件版本：MCSDK、CubeMX、CubeIDE、HAL/LL、STM32Cube for VS Code。
- 官方资料：STM32G474、STDRIVE101、EVLDRIVE101-HPD、CORDIC、FMAC、OPAMP、TIM1、ADC。
- 器件事实：MPS、MOSFET、DC-DC、LCSC/立创库存、替代料、封装。
- Codex 事实：CLI、IDE 插件、网络权限、AGENTS.md、Cloud 行为。
- 比赛事实：报名、赛题、提交时间、材料要求。
- 高风险工程参数：PWM、死区、保护阈值、24V、电机带载、Max Modulation、Hall/无感切换。

## 来源优先级

1. 官方 Datasheet / Reference Manual / User Manual / Application Note。
2. 官方产品页、官方工具文档、官方 Help Center。
3. 厂商官网、LCSC/立创商城、比赛官网。
4. ST Community、GitHub issue、论坛实测帖。
5. 二手教程只作线索，不作结论。

## 输出格式

每次联网核查必须输出：

- 结论。
- 来源：标明官方来源和辅助来源。
- 与本项目关系。
- 与 V9/project_context 是否冲突。
- 风险等级。
- 下一步最小动作。

## 安全边界

联网结果不能直接触发上电、接电机或修改保护阈值。涉及硬件安全时，必须先给不上电验证步骤、限流电源设置、仪器检查项和回退方案。
