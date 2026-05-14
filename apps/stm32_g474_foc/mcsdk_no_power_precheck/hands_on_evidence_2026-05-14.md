# P2 手把手无功率实操证据 - 2026-05-14

本记录来自本轮 NUCLEO-G474RE / CubeMX 手把手实操。它只记录 GUI 配置层证据，
不授权任何功率板、电机、Gate PWM、Motor Profiler、Hall 闭环或 SMO 操作。

## 本轮产物

| 项目 | 结果 |
| --- | --- |
| CubeMX 工程 | `mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc` |
| 工程入口 | NUCLEO-G474RE Board Selector |
| MCU | `STM32G474RETx` / `STM32G474RET6` |
| Package | `LQFP64` |
| Toolchain | CMake |
| `.stmcx` | 仍未产生 |
| MCSDK MotorControl 工程 | 仍未产生 |

## 关键 `.ioc` 读回

| 证据点 | `.ioc` 读回 | P2 含义 |
| --- | --- | --- |
| 板卡 | `Mcu.IP0=NUCLEO-G474RE` | 这是按真实 NUCLEO-G474RE 板卡入口创建的草案，不是裸芯片猜测。 |
| 调试口 | `PA13.Signal=SYS_JTMS-SWDIO`, `PA14.Signal=SYS_JTCK-SWCLK` | SWD 调试口必须保留，不应挪作 FOC 外设。 |
| VCP 串口 | `PA2.Signal=LPUART1_TX`, `PA3.Signal=LPUART1_RX` | `PA2/PA3` 是 NUCLEO VCP 路径，不能默认复用为 FOC 通信口。 |
| SWO / Hall 冲突 | `PB3.Signal=SYS_JTDO-SWO` | `PB3` 当前被 SWO 占用；以后若作为 Hall B，必须先有释放或隔离 SWO 的证据。 |
| nFAULT 候选 | `PB12.Signal=TIM1_BKIN` | CubeMX 接受 `PB12` 作为 TIM1 break 输入候选。还不能证明 STDRIVE101 `nFAULT` 已连到 PB12。 |
| V 低侧 PWM 候选 | `PB14.Signal=TIM1_CH2N` | CubeMX 接受 `PB14` 作为 TIM1 CH2N 候选。还不能证明它连到目标 STDRIVE101 输入。 |

## 当前结论

本轮把 P2 从“口头/截图观察”推进到“可读 `.ioc` 配置草案”。这个草案可以作为
CubeMX 配置层证据，用来证明：

- NUCLEO-G474RE 入口已使用；
- `PB12/TIM1_BKIN` 和 `PB14/TIM1_CH2N` 在 CubeMX 配置层可保存；
- `PA2/PA3` 和 `PB3` 的 NUCLEO 默认占用已经被保存进文件。

它不能证明：

- 已经生成 MCSDK MotorControl 工程；
- 已经存在 Workbench `.stmcx`；
- `PB12` 真的接到了 STDRIVE101 `nFAULT`；
- `PB14` 真的接到了 STDRIVE101 V 相低侧输入；
- Hall、PWM Gate、Motor Profiler、功率板或电机行为已经验证。

## 下一步证据

1. 补 CN8 / EDA / netlist，证明 `nFAULT`、PWM 输入、电流采样、Hall、电源轨和地的实际走线。
2. 补 STDRIVE101 板级保护路径证据：`DT/MODE`、`nFAULT` pull-up、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、standby、VDS 监测。
3. 如果后续能进入 MCSDK/Workbench，再保存真实 `.stmcx` 或配置页截图。
