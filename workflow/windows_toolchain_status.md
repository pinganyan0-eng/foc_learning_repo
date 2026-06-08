# Windows 工具链状态

最后更新：2026-06-07

## 2026-06-07 命令行复查

- `cmake` 可用：`C:\Program Files\CMake\bin\cmake.exe`。
- `mingw32-make.exe` 可用：`C:\mingw64\bin\mingw32-make.exe`。
- `STM32_Programmer_CLI.exe` 可用：
  `F:\STMCubePROG\bin\STM32_Programmer_CLI.exe`。
- `arm-none-eabi-gcc.exe` 和 `arm-none-eabi-g++.exe` 未在 PATH 或已搜索的
  ST/Cube/VS Code 工具目录中找到。
- `apps/stm32_g474_foc/cn8_pin_probe/` 暂时不能从命令行生成 `.elf`、
  `.hex` 或 `.bin`。当前缺口是 ARM GCC，不是烧录 CLI。
- `STM32_Programmer_CLI.exe -l` 当前显示：No ST-Link detected，Total
  number of serial ports available: 0。烧录前还需要把 NUCLEO/ST-LINK 接入并
  重新确认。
- 下方 2026-05-09 bundle 记录保留为历史证据；用于当前烧录或构建结论前，
  需要重新验证 bundle 实际路径。

## 状态

- 结论：CubeMX 生成链路已可用；STM32CubeIDE for VS Code 扩展本体已安装；扩展托管的 CMake/Ninja/GNU Arm GCC bundle 已可用于构建。
- 证据等级：已有命令输出证据。
- 已验证可用：系统 PATH 中 `cmake --version` 返回 4.3.2。
- 已验证可用：STM32Cube bundle `cmake` 返回 4.3.1。
- 已验证可用：STM32Cube bundle `ninja` 返回 1.13.2。
- 已验证可用：STM32Cube bundle `arm-none-eabi-gcc` 返回 GNU Tools for STM32 14.3.1。
- 未加入系统 PATH：`ninja`、`arm-none-eabi-gcc`。这是 VS Code bundle 托管工具链下的正常状态，不代表 VS Code 内不可构建。
- 待验证：`STM32_Programmer_CLI` 或 VS Code 调试/下载所用 ST-LINK 后端。
- 已验证安装：`stmicroelectronics.stm32-vscode-extension-3.9.0` 及 `stm32cube-ide-*` VS Code 扩展组件。
- 已验证构建：`apps/stm32_g474_foc/nucleo_g474re_baseline/` 的 Debug 构建通过，生成 `build/Debug/nucleo_g474re_baseline.elf`。
- 阶段闸门：CubeMX 生成和空工程编译通过；下载、调试、串口和板上运行仍待验证。

## 当前工具链口径

- 主 IDE/编辑调试：VS Code + STM32CubeIDE 插件。
- 配置与代码生成：STM32CubeMX + MCSDK。
- 命令行工具链：STM32CubeIDE for VS Code 3.x 优先通过 Bundle Manager 下载和管理所需 CLI tools；独立 STM32CubeCLT 只作为 bundle 路线失败时的备选方案。
- 调试/连接：ST-LINK。
- 串口工具：已由用户确认可用，具体工具名待补。
- 项目不以独立 STM32CubeIDE 作为主 IDE。

## NUCLEO-G474RE 官方板卡事实

- `LD2`：官方 UM2505 确认由 `PA5` 驱动，`PA5=1` 点亮。
- ST-LINK Virtual COM：官方 UM2505 确认默认连接到 `LPUART1 PA2/PA3`。
- 默认 VCP 焊桥：`SB17/SB23 ON`，`SB18/SB22/SB12/SB20 OFF`。
- 不要把本板默认 VCP 写成 USART2；USART1 `PC4/PC5` 只有改焊桥后才接 ST-LINK VCP。

## 建议补充的证据

- VS Code 版本。
- STM32CubeIDE 插件 / STM32Cube for VS Code 版本或截图。
- STM32CubeMX 版本。
- MCSDK / Motor Control Workbench 版本。
- ST-LINK 驱动或 STM32CubeProgrammer 版本。
- 串口工具名称和可打开 ST-LINK Virtual COM 的截图或记录。
- NUCLEO-G474RE 是否能在工具链里被识别。
- `ninja --version` 输出。
- `arm-none-eabi-gcc --version` 输出。
- `STM32_Programmer_CLI --version` 输出。

## 下一步

- 用 VS Code/STM32Cube 扩展下载 Debug 构建到 NUCLEO-G474RE，确认 ST-LINK 连接和调试入口。
- 最小目标：不接 24V、不接功率板、不接电机，只做下载、点灯、串口打印、定时器和 UART DMA + IDLE 的最小验证。
