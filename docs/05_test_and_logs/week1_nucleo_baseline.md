# week1_nucleo_baseline

NUCLEO-G474RE 基础工程记录入口。

## 官方板卡事实

- 用户 LED `LD2`：`PA5`，写高电平点亮。
- 默认 ST-LINK Virtual COM：`LPUART1 PA2/PA3`。
- 默认 VCP 焊桥：`SB17/SB23 ON`，`SB18/SB22/SB12/SB20 OFF`。
- 本阶段不改焊桥，不使用 USART2 作为默认 VCP。

## 当前练习记录

- `experiments/2026-05-09_nucleo_baseline/README.md`

## P1 交付物：UART 命令分类和副作用表

本表只覆盖 NUCLEO baseline 的学习用命令路径。它证明的是“串口命令解析、状态保护和模拟目标值更新”这层逻辑，不证明真实电机、功率板、MCSDK 或 Hall/SMO 已经验证。

证据来源：

- 板上串口验证：`experiments/2026-05-09_nucleo_baseline/logs/2026-05-12_com5_set_rpm_validation.md`
- 当前实现：`apps/stm32_g474_foc/nucleo_g474re_baseline/Core/Src/main.c`

| 命令或场景 | 分类 | 匹配/保护条件 | `app_mode` 副作用 | `target_rpm` 副作用 | `mode_change_count` 副作用 | 典型响应 | 禁止误解 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PING` | read-only query | `strcmp(cmd, "PING") == 0` | 不变 | 不变 | 不变 | `PONG` | 不能因为收到命令就改变状态。 |
| `MODE?` | read-only query | `strcmp(cmd, "MODE?") == 0` | 不变 | 不变 | 不变 | `OK unchanged mode=...` | 查询当前状态不是状态迁移。 |
| `SET_RPM abc` | guarded target command, parse reject | 参数不能解析为整数 | 不变 | 不变 | 不变 | `ERR parse cmd=SET_RPM` | 格式错不能落到目标值变量。 |
| `SET_RPM 999999` | guarded target command, range reject | 超出 `APP_TARGET_RPM_MIN..APP_TARGET_RPM_MAX` | 不变 | 不变 | 不变 | `ERR range cmd=SET_RPM ...` | 范围错不能被截断后悄悄接受。 |
| `IDLE + SET_RPM 1200` | guarded target command, state reject | `app_mode == APP_MODE_IDLE` | 不变 | 不变 | 不变 | `ERR bad_state cmd=SET_RPM ...` | 未 ARM 不能写入运行目标。 |
| `ARMED/RUN_SIM + SET_RPM 1200` | guarded target command, accepted | 参数合法且不在 `IDLE` | 不变 | 写入模拟 `target_rpm` | 不变 | `OK target_rpm=1200 ...` | 这仍是学习变量，不是电机转速闭环。 |
| `IDLE + ARM` | guarded state command, accepted | `app_mode == APP_MODE_IDLE` | 变为 `APP_MODE_ARMED` | 不变 | `+1` | `OK changed mode=1 mode_name=ARMED` | ARM 只能从安全起点进入预备态。 |
| `ARMED/RUN_SIM + ARM` | guarded state command, reject | `app_mode != APP_MODE_IDLE` | 不变 | 不变 | 不变 | `ERR bad_state cmd=ARM ...` | 不能用 ARM 倒退、重复或绕过顺序。 |
| `IDLE + STOP` | safe command, idempotent | `app_mode == APP_MODE_IDLE` | 保持 `IDLE` | 清零 | 不变 | `OK unchanged ... target_rpm=0` | STOP 可接受，但已在 IDLE 时不算状态变化。 |
| `ARMED/RUN_SIM + STOP` | safe command, accepted | `app_mode != APP_MODE_IDLE` | 变为 `APP_MODE_IDLE` | 清零 | `+1` | `OK changed mode=0 mode_name=IDLE` | STOP 的安全方向必须回到 IDLE。 |
| unknown command | reject | 无已知分支匹配 | 不变 | 不变 | 不变 | `ERR unknown_cmd ...` | 未知命令不能有任何隐藏副作用。 |

## P1 复习锚点

下次教学只需要先检查两个迁移点，不要重新讲完整状态机：

1. `ARMED,target_rpm=1200,mode_change_count=5 + STOP`：
   - 结果应为 `mode=IDLE`、`target_rpm=0`、`mode_change_count=6`。
2. `IDLE,target_rpm=1200,mode_change_count=5 + STOP`：
   - 结果应为 `mode=IDLE`、`target_rpm=0`、`mode_change_count=5`。

核心区别：`STOP` 中 `target_rpm=0` 是无条件安全副作用；`app_mode=IDLE` 和 `mode_change_count++` 只在原来不是 `IDLE` 时执行。

## P1 结论

- UART 命令副作用表已经形成仓库资产。
- 当前仍不能进入 24V、功率板、电机、PWM Gate、Motor Profiler、Hall/SMO。
- P1 是否能从 `catch-up` 变为 `on-track`，还取决于学习者是否能独立通过 `learning/NEXT_LESSON.md` 的 P0 检查，以及文档更新后的工具验证是否通过。
