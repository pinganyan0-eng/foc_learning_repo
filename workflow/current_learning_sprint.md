# Current Learning Sprint

Last updated: 2026-05-14

This is the short execution layer for the current teaching plan. It turns the long B algorithm delivery plan into a concrete sprint with deliverables, review priority, and exit criteria.

## Sprint Identity

- Sprint ID: P2-S1-MCSDK-NO-POWER-PRECHECK
- Stage: P2 MCSDK no-power precheck.
- Status: in progress. P1 concept-layer checks are passed, and the P2 artifact now contains a tool/version status table, baseline `.ioc` readback, pin/config draft, local ST PDF mirror note, online ST source cross-check, pin-function conflict resolution pass, shell GUI evidence probe, expanded future Motor Profiler stop plan, and a dedicated no-power planning directory at `apps/stm32_g474_foc/mcsdk_no_power_precheck/`. CubeMX path `F:\STMCubeMX\STM32CubeMX.exe` was proven and launched, CubeMX Home screenshot `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png` exists, `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md` defines the next-ring pin/config safety review, and `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md` records the current missing blockers. 2026-05-14 手把手实操已保存 NUCLEO-G474RE CubeMX `.ioc` 草案 `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`，读回 `PB12/TIM1_BKIN`、`PB14/TIM1_CH2N`、`PA2/PA3` VCP 和 `PB3` SWO。本轮新增 `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_result_2026-05-14.md` 和两张 CubeMX `Pinout & Configuration` 截图，证明该 `.ioc` 可由 GUI 打开查看；又新增 `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`，证明 MCSDK MotorControl package 数据存在但没有发现 `.stmcx` 或独立 Workbench launcher。当前仍没有真实 `.stmcx`，没有 MCSDK MotorControl 配置页截图，没有 CN8/EDA/netlist 走线证明，也没有板级 STDRIVE101 保护路径证明。
- Owner split: ChatGPT teaches tool roles and safety boundaries; Codex writes artifacts, verifies files, records evidence, and keeps unsafe hardware actions blocked.
- Safety boundary: no 24V, no power board, no motor, no PWM Gate, no real Motor Profiler run, no Hall closed-loop, no SMO claim, and no claim that `SET_RPM` controls real speed.

## Why This Sprint

P1 NUCLEO UART command handling and DMA + IDLE concept checks are recorded as passed. The next useful move is no longer more verbal review of STOP/DMA basics; it is creating the P2 no-power artifact set that will let the team approach MCSDK safely.

The first P2 card now exists at `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`. It deliberately found and preserved configuration conflicts instead of hiding them:

- `PA2/PA3` are convenient for P1 ST-LINK VCP but conflict with OPAMP/PGA planning.
- `PC5` appeared as both a V9 nFAULT candidate and an OPAMP2 feedback-related pin; the official pin-function pass now rejects `PC5` and prefers `PB12/TIM1_BKIN` as the draft nFAULT candidate.
- `PB3` is current SWO in the baseline but a Hall B candidate in V9; the current policy is to keep SWD and release/isolate SWO if Hall B stays on `PB3/TIM2_CH2`.
- V-phase low-side PWM differs across materials (`PB14` in V9, `PA12` in older notes); the current draft prefers `PB14/TIM1_CH2N` and treats `PA12` only as a board-routing alternate.
- Frequently used ST PDFs are mirrored under `materials/raw/st_manuals/`, including `st_stdrive101_datasheet` for STDRIVE101 gate-driver protection review.
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/config_draft.md` now records the current no-power draft choices without modifying or replacing the P1 baseline.
- The user has stated they already know the toolchain; skip basic CubeMX navigation and use the pin/config safety review as the next checkpoint.

## Required Deliverables

| Deliverable | Target File | Current Status | Done When |
| --- | --- | --- | --- |
| P2 no-power precheck card | `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md` | in progress | Card includes tool roles, allowed/forbidden scope, tool/status table, baseline `.ioc` readback, pin/config draft, official-source cross-check, conflict resolution pass, Motor Profiler plan, and risk/no-go checklist. |
| Tool version/status evidence | same card plus `workflow/windows_toolchain_status.md` | partially filled | Local evidence states what is available, what is missing from PATH, and what still needs GUI screenshot or exact path proof. |
| ST official local mirror | `materials/raw/st_manuals/`, `references/st_manuals_index.md` | filled, including STDRIVE101 | Frequently used ST PDFs are repo-local, indexed, hash-recorded, and paired with extracted text for retrieval. |
| Workbench/CubeMX config evidence | future MotorControl screenshot or `.stmcx` placeholder | partially started | CubeMX Home screenshot, NUCLEO `.ioc` draft, CubeMX `Pinout & Configuration` fallback screenshots, and Workbench entry probe are captured. MotorControl package data exists, but a real MCSDK/Workbench MotorControl screenshot or `.stmcx` is still required without running Motor Profiler or touching power hardware. |
| NUCLEO CubeMX `.ioc` draft | `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc` | saved | `.ioc` preserves the user hands-on Board Selector result and reads back NUCLEO, SWD, VCP, SWO, `PB12/TIM1_BKIN`, and `PB14/TIM1_CH2N` choices. |
| Pin/config conflict resolution | same card plus `apps/stm32_g474_foc/mcsdk_no_power_precheck/config_draft.md` | partially resolved | `PA2/PA3`, `PC5`/nFAULT, `PB3`, and V low-side PWM conflicts are resolved at pin-function and CubeMX `.ioc` level; board-routing evidence still must confirm the choices. |
| Pin/config safety review | `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md` | filled | Review defines evidence classes, hard stops, and the minimum evidence packet before trusting generated MCSDK configuration. |
| P2 证据包 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md` | 已按当前库存填写并补 GUI fallback | 证据包记录 `.stmcx`、MotorControl 配置页截图、CN8/EDA/netlist 走线证明、板级 STDRIVE101 保护路径证明和 SWO 释放证据仍是阻塞项；新增截图只证明 `.ioc` 可由 CubeMX GUI 打开。 |
| Motor Profiler plan | same card or a later P3 plan file | expanded for future P3 | Plan lists required hardware, current limit, motor information, stop conditions, abort criteria, instrument/log needs, and rollback path; no live profiler run occurs in P2. |
| Evidence register and submission checklist | `workflow/evidence_register.md`, `deliverables/submission_checklist.md` | updated for first P2 card | P2 planning evidence is registered without overstating it as MCSDK, Hall, power, or motor validation. |

## Review Priority

1. P0: safety boundary remains stable: no power, no motor, no Profiler, no PWM Gate.
2. P1: learner can explain why P2 config artifacts do not prove motor-control behavior.
3. P2: finish the artifact set by adding GUI/config evidence and resolving pin conflicts before any generated project.

Use `learning/NEXT_LESSON.md` for the exact teaching script, but treat this file as the current execution state.

## Exit Criteria

The sprint can close when:

- `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md` has all required P2 sections filled.
- MCSDK/Workbench MotorControl screenshot or real `.stmcx` exists and is linked; CubeMX `.ioc` pinout screenshots alone are not enough to close this item.
- P2 证据包已经记录所有缺失阻塞项，或已更新为真实新增证据链接。
- The nFAULT pin decision is no longer internally conflicted and is confirmed against CubeMX/Workbench plus CN8/EDA/netlist evidence.
- The P1 `PA2/PA3` UART path is either explicitly excluded from the MCSDK FOC config or proven safe by CubeMX/MCSDK.
- Any generated project, if created, is built without connecting power hardware.
- `workflow/evidence_register.md` and `deliverables/submission_checklist.md` reflect the final P2 status.
- `python -m unittest discover -s tests` passes after repo updates.

## No-Go Criteria

Do not move to P3 if any of these are true:

- Any config still routes nFAULT to `PC5` or another OPAMP/VCP-related pin without documented safe mode and board-routing proof.
- The MCSDK config reuses `PA2/PA3` without resolving OPAMP/PGA implications.
- Workbench/CubeMX evidence is only verbal, or only shows the CubeMX `.ioc` pinout without MotorControl/Workbench evidence.
- Motor Profiler would require a real motor or power chain.
- Any request would require power-board connection, 24V, PWM Gate output, Hall closed-loop, or SMO validation before phase gates are ready.
