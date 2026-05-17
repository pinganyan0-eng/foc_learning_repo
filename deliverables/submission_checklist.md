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
- Packet A 2026-05-15 update: `packet_a_local_probe_2026-05-15.md`,
  `packet_a_capture_checklist_2026-05-15.md`, and
  `source_packet_review_2026-05-15_002_my_first_foc_stwb6.md` now exist. A
  local MCSDK 6 Workbench project candidate,
  `packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`, was found and
  reviewed as `Partial clue`; selected-field Workbench screenshots are still
  required before build-only generated-project trust.
- Non-hardware 2026-05-15 update:
  `stm32_side_signal_contract_2026-05-15.md` and
  `future_build_only_gate_2026-05-15.md` now exist. They preserve STM32 signal
  responsibilities and future build-only rules without upgrading Packet A/B/C
  or any hardware evidence.
- Readiness 2026-05-15 update:
  `p2_readiness_snapshot_2026-05-15.md` now exists. It records that P2 remains
  in progress, Packet A is `Partial clue`, generated-project trust is `Not allowed`,
  and P3 powered or motor work is not allowed.
- Packet A 2026-05-16 update:
  `packet_a_sources/2026-05-16_custom_nucleo_stdrive101/` and
  `source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`
  now exist. The package prepares a new project-specific Workbench capture for
  `NUCLEO-G474RE` plus a Custom / Generic STDRIVE101 power stage, Hall
  fallback, 3-shunt current sensing, supplier-clue motor label
  `57BLF01_VENDOR_CANDIDATE`, no-power motor measurement, and pin assignment
  review. It is `Partial clue / Preparation
  only` until the real `.stwb6` and selected-field screenshots are added.
- Packet A/B 2026-05-17 source intake:
  `source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md` and
  `mcu_pin_compatibility_check_2026-05-17.md` now exist. Supplier motor data
  for `57BLF01` and the hardware teammate `STM32G431RB` pin table are archived
  as `Partial clue`; the hardware teammate says the relevant G431/G474 pins are
  the same, and local MCSDK assets support the compared key rows. This does not
  accept CN8 routing, `J_HALL` numbering, `PB3` SWO release, OPAMP2 feasibility,
  measured motor parameters, or generated-project trust.
- Phase-gate 2026-05-15 update:
  `workflow/phase_gate_checklist.md` now contains a P2 no-power insert. It
  blocks direct NUCLEO-to-Motor-Profiler jumps and requires Packet A before any
  build-only generated-project work.
- Status: in progress; tool/status table, pin/config draft, ST source cross-check, pin-function conflict resolution pass, shell GUI evidence probe, expanded future Motor Profiler stop plan, dedicated no-power planning directory, proven CubeMX launch path, CubeMX Home screenshot, next-ring pin/config safety review, current P2 evidence packet, a saved NUCLEO-G474RE CubeMX `.ioc` draft, CubeMX `Pinout & Configuration` fallback screenshots, a Workbench entry probe, STDRIVE101 protection-path review, source packet intake checklist, source packet request pack, user action queue, source packet review template, a 2026-05-15 schematic screenshot candidate review, a non-hardware parallel track, a 2026-05-15 Packet A `.stwb6` legacy source candidate review, a 2026-05-16 custom Packet A capture package, and a 2026-05-17 vendor motor / G431 pin-table source review now exist. The `.ioc` confirms `PB12/TIM1_BKIN`, `PB14/TIM1_CH2N`, `PA2/PA3` VCP, and `PB3` SWO at configuration level; `My_First_FOC.stwb6` is now treated as a legacy learning leftover and remains only `Partial clue` because it uses arbitrary `EVALSTDRIVE101` context. The 2026-05-16 package prepares the intended `NUCLEO-G474RE` plus Custom / Generic STDRIVE101 Workbench path, and the 2026-05-17 review reduces G431/G474 key-pin uncertainty while keeping the motor data and pin table as `Partial clue` only. The protection-path review defines the missing evidence for `DT/MODE`, `nFAULT`, `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, standby, and VDS monitoring. The 2026-05-15 schematic screenshot is useful `Partial clue`; user confirmed it matches the current physical power board and was drawn by the hardware teammate, but formal source revision/date, STM32 endpoint mapping, accepted `DT/MODE` proof, and `STBY` proof are still missing. The non-hardware parallel track records that skipping Packet B/C is a scheduling choice, not clearance. Accepted final MotorControl config evidence, accepted board-routing proof, accepted `J_HALL` numbering, `PB3` SWO release, and accepted board-specific STDRIVE101 protection-path proof are still missing.

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
- [x] Workbench entry probe captured MotorControl package data at `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`; the later 2026-05-15 follow-up resolved the real launcher under `F:\STMCSDK`.
- [x] CN8 / STDRIVE101 route review exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/cn8_stdrive101_route_review_2026-05-14.md`.
- [x] STDRIVE101 protection-path review exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`.
- [x] Source packet intake checklist exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_intake_checklist_2026-05-14.md` and defines accepted / rejected sources before any missing evidence can be upgraded.
- [x] Source packet request pack exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_request_pack_2026-05-14.md` and defines the next `.stmcx` / MotorControl screenshot, CN8 / EDA / netlist, and STDRIVE101 protection-path handoff.
- [x] User action queue exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md` and tells the user to provide Packet B board-route / STDRIVE101 source evidence first, without upgrading any blocker.
- [x] Source packet review template exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_template_2026-05-14.md` and requires Accept / Partial clue / Reject before any blocker can be upgraded.
- [x] 2026-05-15 CN8 / STDRIVE101 schematic screenshot candidate is preserved and reviewed as `Partial clue`, not accepted proof.
- [x] Non-hardware parallel track exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/non_hardware_parallel_track_2026-05-15.md` and keeps Packet B/C skipped-but-blocked while Packet A / signal-contract / build-gate work can continue.
- [x] Packet A local probe exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_local_probe_2026-05-15.md`; the follow-up found `F:\STMCSDK\My_First_FOC.stwb6` and the ST MC Workbench 6.4.2 launcher.
- [x] Packet A `.stwb6` candidate is preserved at `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6` and reviewed at `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_002_my_first_foc_stwb6.md` as `Partial clue`.
- [x] Packet A capture checklist exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_checklist_2026-05-15.md` and defines the next accepted no-power `.stwb6` / legacy `.stmcx` / screenshot / launcher-path capture.
- [x] Packet A custom capture package exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/` with Workbench guide, no-power motor measurement template, pin assignment table, and screenshot inbox.
- [x] Packet A custom capture package review exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md` and marks the package as `Partial clue / Preparation only`.
- [x] 2026-05-17 supplier motor and hardware teammate pin-table sources are archived under `hardware/motor/` and `hardware/schematic/`, reviewed at `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`, and paired with `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcu_pin_compatibility_check_2026-05-17.md`; they remain `Partial clue` only.
- [x] STM32-side signal contract exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/stm32_side_signal_contract_2026-05-15.md` and keeps CN8-facing responsibilities blocked/candidate until source evidence exists.
- [x] Future build-only gate exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/future_build_only_gate_2026-05-15.md` and records generated-project trust as currently `Not allowed` while Packet A is only `Partial clue`.
- [x] P2 readiness snapshot exists at `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md` and records that generated-project trust, build-only work, and hardware action are still not allowed in the current state.
- [x] Phase gate checklist contains a 2026-05-15 P2 no-power insert that separates P2-S1 no-power precheck, P2-S2 build-only generated-project work, and P2-to-P3 blockers.
- [x] The excluded WeChat-side `netlist_PADS.net` candidate was not imported and is not used as current board evidence.
- [x] 当前证据包已记录缺失的 `.stmcx`、配置页截图、CN8/EDA/netlist、STDRIVE101 保护路径和 SWO 释放阻塞项。
- [x] NUCLEO-G474RE CubeMX `.ioc` 草案已保存：`apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`。
- [x] `.ioc` 已读回 `PB12.Signal=TIM1_BKIN`、`PB14.Signal=TIM1_CH2N`、`PA2/PA3` VCP 和 `PB3` SWO。
- [x] Motor Profiler future plan expanded with required hardware, current limit, stop conditions, and abort criteria.
- [ ] Workbench/MCSDK selected-field screenshots captured, or final `.stwb6` / legacy `.stmcx` accepted beyond `Partial clue`.
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
