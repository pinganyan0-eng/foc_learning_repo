# Submission Checklist

本清单用于最终提交；阶段性学习和工程上交物以 `workflow/algo_b_teaching_delivery_plan.md` 为准。每周或每个 P 阶段结束时，至少补一份周交付包，说明当前阶段、已完成证据、进度债和是否允许进入下一阶段。

## Weekly / Phase Delivery Pack

- 周期或阶段：
- 对应原计划：
- 当前真实阶段：
- 本周完成：
- 本周上交物：
- 证据路径：
- 用户已掌握：
- 仍需复习：
- 进度债：
- 下周目标：
- 禁止推进范围：
- 是否允许进入下一阶段：

## Current P1 Catch-up Pack

Use this section before claiming P1 is on-track.

- Pack file: `deliverables/2026-05-12_p1_catchup_pack.md`
- Status: artifacts packaged; learner P0 transfer check still gates `on-track`.

- [x] UART command side-effect table exists in a repo file.
- [x] DMA + IDLE receive flow exists in a repo file.
- [x] Existing COM5 serial evidence is linked from the pack.
- [x] User mastery evidence cites `learning/MASTERY_MAP.md`.
- [x] Open weak points cite `learning/review_queue.md`.
- [x] The pack says explicitly whether P2 MCSDK no-power precheck may start.
- [x] Forbidden scope repeats: no 24V, no power board, no motor, no PWM Gate, no Motor Profiler, no Hall/SMO.

This checklist confirms the P1 catch-up pack exists. It does not by itself prove learner mastery or authorize P2/P3 hardware work.

## Current P2 No-Power Precheck Pack

Use this section before claiming P2 is ready to generate or build an MCSDK project.

- Pack file: `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`
- Status: in progress; tool/status table, pin/config draft, ST source cross-check, pin-function conflict resolution pass, shell GUI evidence probe, expanded future Motor Profiler stop plan, dedicated no-power planning directory, proven CubeMX launch path, CubeMX Home screenshot, next-ring pin/config safety review, current P2 evidence packet, a saved NUCLEO-G474RE CubeMX `.ioc` draft, CubeMX `Pinout & Configuration` fallback screenshots, a Workbench entry probe, and STDRIVE101 protection-path review now exist. The `.ioc` confirms `PB12/TIM1_BKIN`, `PB14/TIM1_CH2N`, `PA2/PA3` VCP, and `PB3` SWO at configuration level; the Workbench probe confirms MotorControl package data exists; the protection-path review defines the missing evidence for `DT/MODE`, `nFAULT`, `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, standby, and VDS monitoring. Real `.stmcx`, MCSDK MotorControl config evidence, board-routing proof, and board-specific STDRIVE101 protection-path proof are still missing. 也就是说：P2 证据包已经把一部分配置草案落成文件并补到 GUI 可视证据，也把 STDRIVE101 保护路径审查规则落成文件，但硬件和 MCSDK MotorControl 配置缺口还没有补齐。

- [x] P2 no-power card exists in a repo file.
- [x] Tool version/status table records current local evidence and missing PATH/GUI proof.
- [x] Baseline `.ioc` readback is separated from future MCSDK configuration.
- [x] Pin/config draft is explicitly marked as not applied and not a wiring instruction.
- [x] `PA2/PA3` UART-vs-OPAMP, `PC5` nFAULT-vs-OPAMP, and `PB3` SWO-vs-Hall conflicts are visible.
- [x] Frequently used ST PDFs, including STDRIVE101, are mirrored locally under `materials/raw/st_manuals/` and indexed for future retrieval.
- [x] `PC5` / nFAULT conflict is resolved at official pin-function level: reject `PC5`, prefer `PB12/TIM1_BKIN` as draft candidate.
- [x] `PA2/PA3` UART-vs-OPAMP policy is decided for the P2 draft: do not reuse P1 VCP pins as FOC UART unless CubeMX/MCSDK proves it safe.
- [x] Shell probe recorded that no `.stmcx` or Workbench executable path was proven in this turn.
- [x] Dedicated no-power planning directory exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/`.
- [x] Pin/config safety review exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md`.
- [x] CubeMX launch path is proven as `F:\STMCubeMX\STM32CubeMX.exe`.
- [x] CubeMX Home screenshot captured at `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png`.
- [x] Saved `.ioc` was reopened in CubeMX and captured at `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_launch_attempt.png` and `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`.
- [x] Workbench entry probe captured MotorControl package data and the missing `.stmcx` / launcher blocker at `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`.
- [x] CN8 / STDRIVE101 route review exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/cn8_stdrive101_route_review_2026-05-14.md`.
- [x] STDRIVE101 protection-path review exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`.
- [x] The excluded WeChat-side `netlist_PADS.net` candidate was not imported and is not used as current board evidence.
- [x] 当前证据包已记录缺失的 `.stmcx`、配置页截图、CN8/EDA/netlist、STDRIVE101 保护路径和 SWO 释放阻塞项。
- [x] NUCLEO-G474RE CubeMX `.ioc` 草案已保存：`apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`。
- [x] `.ioc` 已读回 `PB12.Signal=TIM1_BKIN`、`PB14.Signal=TIM1_CH2N`、`PA2/PA3` VCP 和 `PB3` SWO。
- [x] Motor Profiler future plan expanded with required hardware, current limit, stop conditions, and abort criteria.
- [ ] Workbench/MCSDK `.stmcx` or MotorControl configuration screenshot captured.
- [ ] 已捕获 `NFAULT`、PWM 输入、电流采样、Hall、电源轨和地的 CN8 / EDA / netlist 走线证明。
- [ ] 已捕获板级 STDRIVE101 `DT/MODE`、`nFAULT`、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、standby 和 VDS monitoring 当前版源证据。当前只有缺证矩阵，不是通过证明。
- [ ] MCSDK MotorControl generated project created. The current saved `.ioc` is a CubeMX NUCLEO draft only.
- [ ] No-power generated project build record captured.
- [ ] `PB12/TIM1_BKIN` nFAULT candidate confirmed against CubeMX/Workbench and power-board CN8/EDA/netlist evidence.

This checklist confirms only P2 planning progress. It does not authorize Motor Profiler, power-board connection, motor connection, PWM Gate output, Hall closed-loop, or SMO work.

## Final Submission Items

- 报告
- PPT
- 演示视频
- 源码归档
- BOM / 原理图 / PCB 关键截图
- 实测证据索引
- 版本说明
