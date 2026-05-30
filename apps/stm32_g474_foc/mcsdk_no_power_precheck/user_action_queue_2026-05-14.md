# 2026-05-22 Current User Action

Current next action is no-power DMM evidence, not CLI toolchain work.

Fill:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/dmm_continuity_short_check_request_2026-05-22.md`.

Return one table with:
`Signal | STM32 pin | DMM result | Beep? | Note / photo ID`.

Required continuity rows:
`IA->PA0`, `IB->PA1`, `IC->PB4`, `PB3->LIN1`, `P14->3V3`, `P15->GND`,
`nFAULT->PB12`.

Required short-check rows:
`3V3-GND`, `PA0/PA1/PB4/PB3/PB12` to `3V3/GND`, and Hall pairs
`IA-IB`, `IA-IC`, `IB-IC`.

Do this only with the board unpowered. No 24V, no motor, no Gate PWM, no Motor
Profiler, and no waveform probing in this step.

## 2026-05-21 Current PCB2 route override

Current route is now confirmed for no-power planning:
`P14/P15=3V3/GND`, `PB3=LIN1`, and
`HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.

Do not ask for `PB3/SWO` release as a current Hall blocker. `PB3` is the
current PCB2 low-side driver input `LIN1`. `PB3/SWO` evidence applies only if a
future alternate Hall or hardware-rework route tries to use `PB3/TIM2_CH2` as
Hall.

# 2026-05-19 你现在直接做什么

## 先处理刚才的报错

你刚才看到 Workbench 报：

`一般错误 / 无法加载文件: C:/Users/gregrg/.st_workbench/projects/MY_FOC.stwb6`

我已经把这个文件恢复回备份了：

`C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6`

现在它又是原来的六步工程，顶层字段是：

`"algorithm": "sixStep"`

这说明：不能只靠手改 `.stwb6` 里一个 `algorithm` 字段把六步工程变成 FOC。这个方法已经被 Workbench 报错证明不可用。

你现在只需要重新打开 `MY_FOC`。如果能打开，就停在工程首页，不要点 `Generate`。如果还报错，继续截图给我。

## 接下来真正要做的事

1. 在 Workbench 里用正常 GUI 流程新建或转换成 FOC 工程，不要手改 `.stwb6`。
2. 功率板仍然按自研 STDRIVE101 板处理，不要用内置 `EVALSTDRIVE101`、`STEVAL-LVLP01`、`EVLDRIVE101-HPD` 冒充项目板。
3. 既然你说引脚可以改，优先把 Hall/PWM 改到 Workbench/MCSDK 能正常表达的定时器兼容引脚组合；后面硬件或飞线去匹配它。
4. 确认 current sensing 不再是 disabled，fault/break 也不要是 disabled。
5. 每看到一个关键配置页就截图给我审，不要直接生成工程。

## 必须停止的地方

- 不点 `Generate`。
- 不 `Build`。
- 不 `Flash`。
- 不接 24V。
- 不接功率板。
- 不接电机。
- 不输出 Gate PWM。
- 不运行 Motor Profiler。
- 不运行 Motor Pilot。

## 当前结论

`MY_FOC` 现在仍然只能作为线索，不能作为 Packet A 通过证据。

Packet A still blocked.

no generated-project trust.

## 仍然保留的旧证据任务

你现在要做的事不是上电，而是继续补无功率证据。

Task 1 - 先交 Packet B：当前版板级走线源包，例如 `netlist_PADS.net`、CN3/CN8 到 STM32 引脚表、J_HALL 引脚方向。

Task 2 - 交 Packet A：MCSDK / MotorControl 配置源包，也就是能审查的 Workbench `.stwb6`、配置截图或等价源文件。

Task 3 - 补 PB3 / SWO 释放证据：closed for current Hall route. `PB3` is `LIN1`,
not Hall. Only reopen PB3/SWO release evidence for a future alternate Hall or
hardware-rework route.

你发给 Codex 的最短模板：把源文件、截图、板子版本、你点到哪一步、有没有报错一起发来。

源包审查规则仍按 `source_packet_intake_checklist_2026-05-14.md` 执行。

仍不授权任何上电或电机动作。

No 24V. No Gate PWM output. No Motor Profiler run.

## 2026-05-19 Packet A FOC route decision

Latest route: `Route narrowed / GUI-created FOC source required / Packet A
still blocked`.

Do not ask Codex to retry a partial `.stwb6` text edit. The next acceptable
Packet A source must come from Workbench GUI creation/conversion, or from a
complete reviewable FOC `.stwb6` supplied as a source packet.

Minimum next screenshots/source packet:

1. FOC / field-oriented control selected, not `SIX_STEP`.
2. `NUCLEO-G474RE` / `STM32G474RETx` selected.
3. Self-developed/custom STDRIVE101 board path visible, not built-in
   `EVALSTDRIVE101`, `STEVAL-LVLP01`, or `EVLDRIVE101-HPD` as a substitute.
4. Current sensing enabled and reviewable.
5. Fault / break input enabled and reviewable.
6. Hall/PWM route visible, with a note whether pins will be changed to a
   timer-compatible physical route or whether `PA0/PA1/PB4` stays a software
   Hall design topic.
7. Stop before Generate, Build, Flash, Motor Profiler, Motor Pilot, 24V,
   power-board connection, motor connection, or Gate PWM output.

## 2026-05-20 Packet C protection detail

Latest protection route: `Packet C detail narrowed / protection proof still
partial clue / P3 still blocked`.

Do not use the old `V_DSth = 0.249V` / `I_trip ~= 55A` note as a board
threshold. The next useful Packet C evidence is:

1. PDF/table-backed confirmation of the STDRIVE101 `SCREF` / `VDSth` formula.
2. A corrected threshold note for the current `33k / 20k` divider.
3. Named `CP` route proof and component interpretation, not only
   `CP -> 100nF -> GND`.
4. `VS/VM` relationship proof for the exact board.
5. A later no-power DMM continuity / short-check table before any P3 action.

This does not replace Packet A. It does not allow Generate, Build, Flash, 24V,
power-board connection, motor connection, Gate PWM, Motor Profiler, Motor
Pilot, Hall closed-loop, or sensorless / SMO work.
