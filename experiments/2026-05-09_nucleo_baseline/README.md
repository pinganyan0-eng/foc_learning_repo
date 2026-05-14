# 2026-05-09 NUCLEO-G474RE baseline

## 2026-05-14 Firmware Update

- UART command reception moved from polling to LPUART1 RX DMA + IDLE.
- The DMA/IDLE callback only moves bytes into a ring buffer; command parsing
  and `printf()` stay in the main loop.
- Debug build passed after the change:
  `nucleo_g474re_baseline.elf`, RAM 2552 B, FLASH 23652 B.
- Build log:
  `logs/2026-05-14_uart_dma_idle_build.md`.
- This remains a NUCLEO USB/ST-LINK VCP firmware step. It is not power-board,
  motor, Gate PWM, Motor Profiler, Hall closed-loop, or SMO validation.

## 1. 实验目标

- 日期：2026-05-09
- 负责人：B 同学，算法/主控
- 当前阶段：阶段 2，NUCLEO 基础工程
- 目标：用 CubeMX 新建 NUCLEO-G474RE 工程，完成点灯、串口 BOOT OK、定时器基础和 UART DMA + IDLE 前置验证。

## 2. 安全边界

- 不接 24V。
- 不接自研功率板。
- 不接电机。
- 不输出三相功率 PWM。
- 只使用 NUCLEO-G474RE 板载 USB/ST-LINK 供电和调试。

## 3. 当前任务清单

| 步骤 | 目标 | 状态 | 证据 |
| --- | --- | --- | --- |
| 1 | CubeMX 新建 NUCLEO-G474RE 工程 | 已完成 | `apps/stm32_g474_foc/nucleo_g474re_baseline/`，含 `Core/`、`Drivers/`、`CMakeLists.txt`、`CMakePresets.json` |
| 2 | 空工程编译 | 已完成 | `build/Debug/nucleo_g474re_baseline.elf`，RAM 1776 B，FLASH 10600 B |
| 3 | LED/串口测试固件编译 | 已完成 | `main.c` 已加入 `BSP_LED_Toggle(LED_GREEN)`、`printf("BOOT OK\\r\\n")`、`printf("LD2 toggle\\r\\n")`，构建通过 |
| 4 | 下载到 NUCLEO-G474RE | 已完成 | 2026-05-11 用户提供 VOFA+ 截图显示 COM5 收到当前固件串口输出 |
| 5 | LED 闪烁 | 部分完成 | 串口日志中 `led` 和 `led_toggle` 按 100 ms 任务节奏变化；仍可补肉眼观察或短视频 |
| 6 | LPUART1 串口输出 | 已完成 | `logs/2026-05-11_vofa_mode_name_log.md` |
| 7 | TIM 定时器基础 | 待做 | 配置截图/日志 |
| 8 | UART DMA + IDLE 接收一行命令 | 待做 | 原始串口日志 |

## 4. 工具版本待补

- VS Code：
- STM32CubeIDE 插件 / STM32Cube for VS Code：
- STM32CubeMX：
- MCSDK / Motor Control Workbench：
- STM32CubeProgrammer / ST-LINK 驱动：
- 串口工具：
- CMake：4.3.2，已在 PATH 中验证
- STM32Cube bundle CMake：4.3.1，路径 `C:/Users/gregrg/AppData/Local/stm32cube/bundles/cmake/4.3.1+st.1/bin/cmake.exe`
- STM32Cube bundle Ninja：1.13.2，路径 `C:/Users/gregrg/AppData/Local/stm32cube/bundles/ninja/1.13.2+st.1/bin/ninja.exe`
- STM32Cube bundle GNU Arm GCC：GNU Tools for STM32 14.3.1，路径 `C:/Users/gregrg/AppData/Local/stm32cube/bundles/gnu-tools-for-stm32/14.3.1+st.2/bin/arm-none-eabi-gcc.exe`
- 系统 PATH：`ninja`、`arm-none-eabi-gcc` 未加入 PATH；这是 VS Code bundle 托管工具链下的正常状态，不代表不可编译。
- STM32CubeIDE for VS Code 扩展：已在 VS Code 扩展目录中发现 `stmicroelectronics.stm32-vscode-extension-3.9.0` 及 `stm32cube-ide-*` 组件。
- STM32Cube Bundle：项目 `.settings/bundles.store.json` 锁定 `cmake@4.3.1+st.1`、`ninja@1.13.2+st.1`、`gnu-tools-for-stm32@14.3.1+st.2`、`st-arm-clangd@21.1.0+st.2`；CMake 缓存已解析到实际 bundle 路径。

## 4.1 官方板卡事实

- 官方 UM2505 确认：NUCLEO-G474RE 的用户 LED `LD2` 由 `PA5` 驱动，`PA5=1` 点亮。
- 官方 UM2505 确认：NUCLEO-G474RE 默认 ST-LINK Virtual COM 连接到 `LPUART1`，引脚为 `PA2/PA3`，不是 USART2。
- 默认 VCP 焊桥状态：`SB17/SB23 ON`，`SB18/SB22/SB12/SB20 OFF`。
- 只有改焊桥后，USART1 `PC4/PC5` 才能接到 ST-LINK VCP；本阶段不改焊桥。

## 5. 操作记录

后续每完成一步，在这里补：

- 做了什么：CubeMX 以 `CMake` 工具链生成 NUCLEO-G474RE baseline 工程。
- 遇到什么问题：第一次生成时 `ToolChainLocation` 路径出现嵌套和空格，CubeMX 卡在 `Generating Project...`；已将坏目录归档为 `apps/stm32_g474_foc/nucleo_g474re_baseline_bad_cubemx_stuck_20260509_200431/` 后重新生成成功。
- 编译检查：生成工程完整；虽然系统 PATH 中缺少 `ninja` 和 `arm-none-eabi-gcc`，但 VS Code STM32Cube bundle 路径下的 CMake/Ninja/GCC 可用。2026-05-09 已在沙盒外用 bundle 工具完成 Debug 构建。
- 串口日志：2026-05-11 用户提供 VOFA+ 1.3.10 截图，COM5 / 115200 8N1 收到状态机日志；整理见 `logs/2026-05-11_vofa_mode_name_log.md`。
- 截图文件：待补。
- 构建输出：`nucleo_g474re_baseline.elf`，RAM 1776 B / 128 KB，FLASH 10600 B / 512 KB。
- LED/串口测试固件：已加入 `BOOT OK` 启动打印、`LD2 toggle` 周期打印和 `LD2` 500 ms 翻转；构建输出 RAM 2208 B / 128 KB，FLASH 13892 B / 512 KB。
- 结论：CubeMX 生成、空工程编译、LED/串口测试固件编译、下载运行和 COM5 串口日志验证已完成；当前证据仍限于 NUCLEO baseline，不代表功率板、电机、MCSDK、Hall 闭环或无感 FOC 已验证。

## 6. 下一步

继续在 NUCLEO-G474RE 上做基础固件练习：保留“不接 24V、不接功率板、不接电机”的边界，下一步可以补一段肉眼 LD2 闪烁证据，或继续做 UART DMA + IDLE 接收一行命令。
