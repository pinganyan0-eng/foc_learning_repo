# Current Learning Sprint

Last updated: 2026-05-14

This is the short execution layer for the current teaching plan. It turns the long B algorithm delivery plan into a concrete sprint with deliverables, review priority, and exit criteria.

## Sprint Identity

- Sprint ID: P2-S1-MCSDK-NO-POWER-PRECHECK
- Stage: P2 MCSDK no-power precheck.
- Status: in progress. P1 concept-layer checks are passed, and the P2 artifact now contains a tool/version status table, baseline `.ioc` readback, pin/config draft, local ST PDF mirror note, online ST source cross-check, pin-function conflict resolution pass, shell GUI evidence probe, expanded future Motor Profiler stop plan, and a dedicated no-power planning directory at `apps/stm32_g474_foc/mcsdk_no_power_precheck/`. CubeMX path `F:\STMCubeMX\STM32CubeMX.exe` was proven and launched, CubeMX Home screenshot `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png` exists, `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md` defines the next-ring pin/config safety review, and `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md` records the current missing blockers. 2026-05-14 手把手实操已保存 NUCLEO-G474RE CubeMX `.ioc` 草案 `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`，读回 `PB12/TIM1_BKIN`、`PB14/TIM1_CH2N`、`PA2/PA3` VCP 和 `PB3` SWO。本轮新增 `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_result_2026-05-14.md` 和两张 CubeMX `Pinout & Configuration` 截图，证明该 `.ioc` 可由 GUI 打开查看；又新增 `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`，证明 MCSDK MotorControl package 数据存在但没有发现 `.stmcx` 或独立 Workbench launcher。随后新增 `source_packet_intake_checklist_2026-05-14.md`、`source_packet_request_pack_2026-05-14.md`、`user_action_queue_2026-05-14.md` 和 `source_packet_review_template_2026-05-14.md`，把后续 `.stmcx` / MotorControl 截图、CN8/EDA/netlist、STDRIVE101 保护路径证据、用户下一步动作顺序和 Codex 审查模板固化。当前仍没有真实 `.stmcx`，没有 MCSDK MotorControl 配置页截图，没有 CN8/EDA/netlist 走线证明，也没有板级 STDRIVE101 保护路径证明。
- Owner split: ChatGPT teaches tool roles and safety boundaries; Codex writes artifacts, verifies files, records evidence, and keeps unsafe hardware actions blocked.
- Safety boundary: no 24V, no power board, no motor, no PWM Gate, no real Motor Profiler run, no Hall closed-loop, no SMO claim, and no claim that `SET_RPM` controls real speed.

2026-05-15 Packet A follow-up: Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_local_probe_2026-05-15.md`
and
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_checklist_2026-05-15.md`.
The first local probe found no `.stmcx` and no MotorControl / Workbench
configuration screenshot in the checked locations. A follow-up resolved the
Start Menu shortcut to
`F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\STMCWB.exe`, found
`F:\STMCSDK\My_First_FOC.stwb6`, preserved it under
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`,
and reviewed it in
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`.
Packet A is now `Partial clue`; this does not upgrade generated-project trust
or any hardware evidence.

2026-05-16 Packet A correction: the user clarified that
`My_First_FOC.stwb6` was only a previous toolchain-learning leftover and that
its `EVALSTDRIVE101` power-board selection was arbitrary. Codex added the new
project-specific capture package
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`
and review
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`.
The target is `NUCLEO-G474RE` plus a Custom / Generic STDRIVE101 power stage,
FOC, Hall fallback, 3-shunt current sensing, supplier-clue motor label,
no-power motor measurement, and a pin assignment table. Status remains
`Partial clue / Preparation only` until the real `.stwb6` and selected-field
screenshots exist.

2026-05-17 source intake: the repo now archives a supplier motor parameter
image for `57BLF01`, a hardware teammate `STM32G431RB` pin-assignment PDF, an
extracted note for each source, `mcu_pin_compatibility_check_2026-05-17.md`,
and
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`.
The hardware teammate states the relevant G431/G474 pins are the same, and the
local MCSDK asset comparison supports the compared key rows. This only reduces
MCU pin-function uncertainty. `57BLF01_VENDOR_CANDIDATE` may be used as a
supplier-clue motor label in Workbench, but `J_HALL` numbering, CN8 endpoint
proof, `PB3` SWO release, OPAMP2 feasibility, and measured motor parameters
remain unresolved.

2026-05-15 signal/build-gate follow-up: Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/stm32_side_signal_contract_2026-05-15.md`
and
`apps/stm32_g474_foc/mcsdk_no_power_precheck/future_build_only_gate_2026-05-15.md`.
These standalone artifacts turn the inline non-hardware track draft into
reviewable rules: STM32-side signal responsibilities stay candidate/blocked
until Packet A/B/C or PB3/SWO evidence exists, and any future generated project
is currently `Not allowed` for trust because Packet A is only `Partial clue`.

2026-05-15 readiness follow-up: Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`.
It consolidates Packet A/B/C, PB3/SWO, STM32-side signal-contract, and
build-only gate status into one current gate decision. P2 remains in progress;
Packet A is `Partial clue`; generated-project trust is still `Not allowed`; P3
powered or motor work is not allowed.

2026-05-15 phase-gate follow-up: Codex updated
`workflow/phase_gate_checklist.md` with explicit P2-S1 no-power precheck,
P2-S2 build-only generated-project, and P2-to-P3 blocker rules. The project may
not jump from NUCLEO basics directly to Motor Profiler or generated-project
trust.

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
| Workbench/CubeMX config evidence | future MotorControl screenshot or `.stwb6` / legacy `.stmcx` source | partial clue / preparation only | CubeMX Home screenshot, NUCLEO `.ioc` draft, CubeMX `Pinout & Configuration` fallback screenshots, Workbench entry probe, and `My_First_FOC.stwb6` legacy review are captured. The 2026-05-16 custom capture package defines the intended `NUCLEO-G474RE` plus Custom / Generic STDRIVE101 path, and the 2026-05-17 source intake adds the `57BLF01_VENDOR_CANDIDATE` supplier-clue label plus a G431/G474 key-pin compatibility check. Selected-field screenshots or an accepted final project source are still required without running Motor Profiler or touching power hardware. |
| NUCLEO CubeMX `.ioc` draft | `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc` | saved | `.ioc` preserves the user hands-on Board Selector result and reads back NUCLEO, SWD, VCP, SWO, `PB12/TIM1_BKIN`, and `PB14/TIM1_CH2N` choices. |
| Pin/config conflict resolution | same card plus `apps/stm32_g474_foc/mcsdk_no_power_precheck/config_draft.md` | partially resolved | `PA2/PA3`, `PC5`/nFAULT, `PB3`, and V low-side PWM conflicts are resolved at pin-function and CubeMX `.ioc` level; board-routing evidence still must confirm the choices. |
| Pin/config safety review | `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md` | filled | Review defines evidence classes, hard stops, and the minimum evidence packet before trusting generated MCSDK configuration. |
| P2 证据包 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md` | 已按当前库存填写并补 GUI fallback | 证据包记录 `.stmcx`、MotorControl 配置页截图、CN8/EDA/netlist 走线证明、板级 STDRIVE101 保护路径证明和 SWO 释放证据仍是阻塞项；新增截图只证明 `.ioc` 可由 CubeMX GUI 打开。 |
| Source packet intake / request | `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_intake_checklist_2026-05-14.md`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_request_pack_2026-05-14.md` | filled | Intake rules define accepted/rejected source packets; request pack tells the team exactly what `.stmcx`, MotorControl screenshot, CN8/EDA/netlist, and STDRIVE101 protection-path evidence to collect next. |
| User action queue | `apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md` | filled | Queue tells the user to provide Packet B board-route / STDRIVE101 source evidence first, Packet A MCSDK/MotorControl evidence second, and PB3/SWO release evidence if Hall B remains planned. |
| Source packet review template | `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_template_2026-05-14.md` | filled | Template defines Accept / Partial clue / Reject review states before any Packet A/B/C or PB3/SWO source can upgrade the evidence packet. |
| 2026-05-15 schematic candidate review | `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_001_cn8_stdrive101_schematic_candidate.md` | partial clue | User-provided screenshot is preserved and reviewed. User confirmed it matches the current physical power board and was drawn by the hardware teammate. It can guide Packet B/C review, but formal source revision/date, STM32 endpoint mapping, accepted `DT/MODE`, and `STBY` proof are still missing. |
| Non-hardware parallel track | `apps/stm32_g474_foc/mcsdk_no_power_precheck/non_hardware_parallel_track_2026-05-15.md` | filled | Records that hardware source work can be skipped for scheduling only while Packet A, STM32-side signal contract, future build-only gate, and delivery cleanup progress. |
| Packet A local probe, source candidate, and capture checklist | `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_local_probe_2026-05-15.md`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_checklist_2026-05-15.md` | filled; Packet A partial clue | Probe records the Workbench launcher and `.stwb6` candidate. Review accepts the file as a source candidate, but selected fields and custom-board context remain incomplete. Checklist defines the next screenshots without authorizing generated-project trust or hardware action. |
| Packet A custom capture package | `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md` | filled; preparation only | Package gives the exact Workbench no-power path, motor no-power measurement template, pin assignment table, and screenshot inbox for a new project-specific `.stwb6`; it does not yet accept Packet A or allow generation/build. |
| STM32-side signal contract | `apps/stm32_g474_foc/mcsdk_no_power_precheck/stm32_side_signal_contract_2026-05-15.md` | filled; all hardware-dependent fields still blocked/candidate | Defines intended STM32 responsibilities for future CN8-facing signals while preserving Packet A/B/C and PB3/SWO blockers. |
| Future build-only gate | `apps/stm32_g474_foc/mcsdk_no_power_precheck/future_build_only_gate_2026-05-15.md` | filled; generated-project trust currently not allowed | Defines prerequisites and forbidden actions for any later MCSDK generated project. The current `.stwb6` is only `Partial clue`; compile success, if later achieved, can prove only no-power build evidence. |
| P2 readiness snapshot | `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md` | filled; P2 remains in progress and generated-project trust is not allowed | Consolidates Packet A/B/C, PB3/SWO, signal-contract, and build-only status into one gate decision before any later generated-project or hardware claim. |
| Phase gate P2 insert | `workflow/phase_gate_checklist.md` | filled; formal gate now blocks direct NUCLEO-to-Profiler jumps | Adds P2-S1 no-power, P2-S2 build-only, and P2-to-P3 blocker rules tied to Packet A/B/C, PB3/SWO, continuity checks, current limits, stop conditions, and rollback evidence. |
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
- MCSDK/Workbench MotorControl screenshot or accepted final `.stwb6` / legacy `.stmcx` exists and is linked; CubeMX `.ioc` pinout screenshots and the current partial-clue `.stwb6` alone are not enough to close this item.
- P2 证据包已经记录所有缺失阻塞项，或已更新为真实新增证据链接。
- Source packet request pack has been used for the next evidence handoff, or the missing source packets are explicitly still unavailable.
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
