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
- Status: in progress; tool/status table, pin/config draft, ST source cross-check, pin-function conflict resolution pass, shell GUI evidence probe, and expanded future Motor Profiler stop plan exist, but Workbench GUI evidence and board-routing proof are still missing.

- [x] P2 no-power card exists in a repo file.
- [x] Tool version/status table records current local evidence and missing PATH/GUI proof.
- [x] Baseline `.ioc` readback is separated from future MCSDK configuration.
- [x] Pin/config draft is explicitly marked as not applied and not a wiring instruction.
- [x] `PA2/PA3` UART-vs-OPAMP, `PC5` nFAULT-vs-OPAMP, and `PB3` SWO-vs-Hall conflicts are visible.
- [x] Frequently used ST PDFs, including STDRIVE101, are mirrored locally under `materials/raw/st_manuals/` and indexed for future retrieval.
- [x] `PC5` / nFAULT conflict is resolved at official pin-function level: reject `PC5`, prefer `PB12/TIM1_BKIN` as draft candidate.
- [x] `PA2/PA3` UART-vs-OPAMP policy is decided for the P2 draft: do not reuse P1 VCP pins as FOC UART unless CubeMX/MCSDK proves it safe.
- [x] Shell probe recorded that no `.stmcx` or Workbench executable path was proven in this turn.
- [x] Motor Profiler future plan expanded with required hardware, current limit, stop conditions, and abort criteria.
- [ ] Workbench/CubeMX screenshot or real `.stmcx` placeholder captured.
- [ ] MCSDK generated project path chosen and created.
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
