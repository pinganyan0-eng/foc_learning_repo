# STM32G474 FOC 工程

这里放真实 STM32CubeMX / MCSDK 生成工程。本项目日常编辑、构建和调试使用 VS Code + STM32CubeIDE 插件，不使用独立 STM32CubeIDE 作为主 IDE。

## 保留原则

- 保持 CubeMX / MCSDK 原生结构，不为了目录好看拆散 `Core/`、`Drivers/`、`Middlewares/`、`MotorControl/`。
- `.ioc`、`CMakeLists.txt` 或 `Makefile` 放在本目录根部。
- 用户新增模块优先放在 CubeMX 允许保留的位置，或放入独立 `User/` 后在构建系统里显式引用。

## NUCLEO-only probe firmware

- `cn8_pin_probe/`: hand-scoped NUCLEO-only GPIO identification firmware for
  PA15/PB3/PB10/PA8/PA9/PA10, matching the recovered PCB2 CN8 P1-P6 mapping.
- It must be used only with the power board disconnected. It is not an MCSDK,
  FOC, Gate, 24 V, or motor validation project.
- Current local build status: source/static checks complete; CMake configure is
  blocked until `arm-none-eabi-gcc.exe` and `arm-none-eabi-g++.exe` are
  available. The preset uses the installed `mingw32-make.exe`, not Ninja.

## 待放入

- `STM32G474_FOC.ioc`
- `Core/`
- `Drivers/`
- `Middlewares/`
- `MotorControl/`
- `CMakeLists.txt` 或 `Makefile`
