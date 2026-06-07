# 当前任务

## Task ID

- ID：TASK-2026-06-07-L2-nucleo-pa8-square-wave
- 主题：NUCLEO-G474RE 单板 PA8/D7 方波与示波器基础检查
- Status：in_progress
- User Approval：2026-06-07，用户在明确“只测 NUCLEO 单板、不连接功率板”的范围后回复“测”
- Risk Level：L2
- Definition of Done：`workflow/definition_of_done.md#工程代码任务`
- Evidence ID：EV-2026-06-07-NUCLEO-PA8-WAVE-001
- Review Required：yes

## 目标

在现有 `nucleo_g474re_baseline` 中加入可回滚的 PA8/D7 GPIO 方波测试模式，完成本地构建，并准备仅针对 NUCLEO 单板的示波器测量记录。

## 允许做

- 只修改 baseline 工程的 `USER CODE` 区。
- 将 PA8 配置为推挽 GPIO 输出。
- 在主循环测试模式下每 1 ms 翻转 PA8，形成约 500 Hz、0~3.3 V 方波。
- 构建、静态检查、记录固件路径和回滚方式。
- 指导用户在功率板完全断开的情况下测量 NUCLEO PA8/D7 对 GND。

## 禁止做

- 不连接功率板、24V 或电机。
- 不修改或启用 TIM1/TIM8 PWM、互补输出、死区、Break、Gate 或 FOC。
- 不烧录 MCSDK 工程。
- 不测 OUTx、BOOTx、GHSx 或 GLSx。
- 不把本测试结果写成 Gate/PWM 功率级通过。

## 输出

- baseline 中可切换的 PA8 方波测试代码。
- 本地 Debug 构建结果。
- `experiments/2026-06-07_nucleo_pa8_square_wave/README.md`
- 用户示波器截图和读数待填记录。

## 验收

- 代码只位于 `USER CODE` 区。
- `APP_PA8_WAVEFORM_TEST=1` 时 PA8 每 1 ms 翻转。
- `APP_PA8_WAVEFORM_TEST=0` 时恢复原 baseline 主循环行为。
- 构建成功或明确记录工具链阻塞。
- 测量步骤只涉及 NUCLEO、USB、PA8/D7、GND 和普通无源探头。

## Codex 结果区

- 执行状态：固件修改、静态检查、Debug 构建和 HEX 生成均已完成；现场示波器读数与截图待用户补齐。
- 构建工具链：ST GNU Tools for STM32 14.3.1。
- 构建结果：通过；FLASH 14572 B，RAM 2208 B。
- 下载文件：`apps/stm32_g474_foc/nucleo_g474re_baseline/build/Debug/nucleo_g474re_pa8_square_wave.hex`。
- HEX SHA-256：`b50c582cd29308fe95e29f024d48b14748473d98992eaa2f20f273e1b2482fb0`。
- 前置任务：`TASK-2026-06-07-L4-power-board-mcu-prejoin-pwm-gate-prep` 已完成文档准备；本任务不改变其“功率板动态检查未放行”结论。
