# Current Learning Sprint

Last updated: 2026-05-14

This is the short execution layer for the current teaching plan. It turns the long B algorithm delivery plan into a concrete sprint with deliverables, review priority, and exit criteria.

## Sprint Identity

- Sprint ID: P2-S1-MCSDK-NO-POWER-PRECHECK
- Stage: P2 MCSDK no-power precheck.
- Status: in progress. P1 concept-layer checks are passed, and the P2 artifact now contains a tool/version status table, baseline `.ioc` readback, pin/config draft, local ST PDF mirror note, online ST source cross-check, pin-function conflict resolution pass, shell GUI evidence probe, expanded future Motor Profiler stop plan, and a dedicated no-power planning directory at `apps/stm32_g474_foc/mcsdk_no_power_precheck/`. CubeMX path `F:\STMCubeMX\STM32CubeMX.exe` was proven and launched, CubeMX Home screenshot `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png` exists, `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md` defines the next-ring pin/config safety review, and `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md` records the current missing blockers. 2026-05-14 鎵嬫妸鎵嬪疄鎿嶅凡淇濆瓨 NUCLEO-G474RE CubeMX `.ioc` 鑽夋 `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`锛岃鍥?`PB12/TIM1_BKIN`銆乣PB14/TIM1_CH2N`銆乣PA2/PA3` VCP 鍜?`PB3` SWO銆傛湰杞柊澧?`apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_result_2026-05-14.md` 鍜屼袱寮?CubeMX `Pinout & Configuration` 鎴浘锛岃瘉鏄庤 `.ioc` 鍙敱 GUI 鎵撳紑鏌ョ湅锛涘張鏂板 `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`锛岃瘉鏄?MCSDK MotorControl package 鏁版嵁瀛樺湪浣嗘病鏈夊彂鐜?`.stmcx` 鎴栫嫭绔?Workbench launcher銆傞殢鍚庢柊澧?`source_packet_intake_checklist_2026-05-14.md`銆乣source_packet_request_pack_2026-05-14.md`銆乣user_action_queue_2026-05-14.md` 鍜?`source_packet_review_template_2026-05-14.md`锛屾妸鍚庣画 `.stmcx` / MotorControl 鎴浘銆丆N8/EDA/netlist銆丼TDRIVE101 淇濇姢璺緞璇佹嵁銆佺敤鎴蜂笅涓€姝ュ姩浣滈『搴忓拰 Codex 瀹℃煡妯℃澘鍥哄寲銆傚綋鍓嶄粛娌℃湁鐪熷疄 `.stmcx`锛屾病鏈?MCSDK MotorControl 閰嶇疆椤垫埅鍥撅紝娌℃湁 CN8/EDA/netlist 璧扮嚎璇佹槑锛屼篃娌℃湁鏉跨骇 STDRIVE101 淇濇姢璺緞璇佹槑銆?- Owner split: ChatGPT teaches tool roles and safety boundaries; Codex writes artifacts, verifies files, records evidence, and keeps unsafe hardware actions blocked.
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

2026-05-21 Packet A generated-source follow-up: Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md`.
The review accepts selected Packet A fields for no-power configuration
evidence: FOC, NUCLEO-G474RE, STM32G474RETx,
MY-STDRIVE101_POWER_BOARD, TIM1 complementary PWM, PB12/TIM1_BKIN,
three-shunt current sensing, TIM2 Hall PA15/PB3/PB10, USART2 PA2/PA3, and no
six-step legacy path in the archived generated-source clue folder. The
build-only source prerequisite is satisfied. The 2026-05-27 no-power Debug
build-only result records exit code `0`, `ninja: no work to do`, and confirmed
`.elf` / `.map` artifacts. Current PCB2 Hall PA0/PA1/PB4, current PCB2
PB3=LIN1, Packet B/C, continuity, and all powered claims remain blocked.

2026-05-21 current PCB2 software Hall follow-up: the route-selection ambiguity
is closed for no-power planning. User confirmed `P14/P15=3V3/GND`,
`PB3=LIN1`, and `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`. The active route is
software Hall adapter first, using future GPIO/EXTI sampling on `PA0/PA1/PB4`;
hardware rework is fallback only. The Workbench generated TIM2 Hall route
`PA15/PB3/PB10` remains generated configuration evidence only and is not
current PCB2 Hall proof.

2026-05-22 DMM no-power follow-up: the next real-world action is not CLI
toolchain setup. Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/dmm_continuity_short_check_request_2026-05-22.md`
so the user can return one filled table for continuity and short checks before
software Hall adapter implementation.

2026-05-22 software Hall algorithm follow-up: because PCB2 is not populated
yet, the DMM gate is hardware-side deferred, not passed. Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_no_power_algorithm_prep_2026-05-22.md`
so the algorithm role can progress on no-power state-machine rules, candidate
sequences, debug observables, ISR limits, and MCSDK boundary research without
claiming firmware implementation or Hall readiness.

2026-05-22 software Hall exercise follow-up: Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_state_machine_exercise_card_2026-05-22.md`.
This is the next user-side algorithm action: answer five Hall state-machine
checks and fill the four-row transition table. It is a learning check only and
does not open firmware implementation, DMM clearance, build, powered work, or
Hall readiness.

2026-05-27 software Hall pseudocode follow-up: PR #4 recorded the Hall
state-machine lesson as L2 concept evidence. Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_pseudocode_draft_2026-05-27.md`
to turn that understanding into a future adapter boundary: function
responsibilities, state fields, decision order, ISR limits, debug observables,
MCSDK hard stops, and code-entry conditions. This is pseudocode only and does
not implement firmware, pass DMM, open MCSDK Hall integration, or prove Hall
readiness.

2026-05-27 software Hall processing-order follow-up: after the user could
classify individual Hall rows but could not restate the adapter sequence,
Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_processing_order_card_2026-05-27.md`.
This is a Chinese-first repair card for raw read -> illegal-state check ->
first-valid check -> repeated-state check -> bounce/timing check ->
forward/reverse adjacent check -> abnormal-jump count. It is not firmware,
not build evidence, not MCSDK Hall integration, and not Hall readiness.

2026-05-27 software Hall host-model follow-up: Codex added
`src/software_hall_model.py`, `tests/test_software_hall_model.py`, and
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_host_model_review_2026-05-27.md`.
This makes the Hall state-machine rules executable on the host only. It is not
STM32 firmware, not GPIO/EXTI proof, not MCSDK Hall integration, not DMM proof,
and not Hall readiness.

2026-05-27 software Hall golden-vector follow-up: Codex added
`tests/fixtures/software_hall_golden_vectors.json`,
`tests/test_software_hall_vectors.py`, and
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_golden_vectors_review_2026-05-27.md`.
This makes the no-power Hall state-machine examples replayable as a fixed
input/output contract for later adapter review. It is not STM32 firmware, not
GPIO/EXTI proof, not MCSDK Hall integration, not DMM proof, and not Hall
readiness.

2026-05-27 software Hall MCSDK integration-probe follow-up: Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_integration_probe_2026-05-27.md`.
The read-only probe found standard MCSDK TIM2 Hall clues such as `HALL_M1`,
`MX_TIM2_Init()`, `M1_SPEED_SENSOR=HALL_SENSOR`, and generated
`hall_speed_pos_fdbk` / `speed_torq_ctrl` file names. This records that the
current `PA0/PA1/PB4` software Hall route is not directly connected to MCSDK
standard Hall and still needs a separate firmware-integration review.

2026-05-27 software Hall firmware-entry follow-up: Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_checklist_2026-05-27.md`.
The checklist freezes the missing conditions before any future adapter code:
populated PCB2, DMM continuity / short-check table, GPIO/EXTI boundary review,
timestamp source decision, debug-output route, and separate MCSDK
firmware-integration review. The build-only record now exists but does not
open firmware implementation, MCSDK Hall integration, or Hall readiness.

2026-05-27 software Hall GPIO/EXTI follow-up: Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_gpio_exti_boundary_review_2026-05-27.md`.
The draft records `PA0/PA1/PB4` as software Hall input candidates,
`EXTI0/EXTI1/EXTI4` as event-capture candidates, and the minimal ISR boundary.
It is not STM32 source, not GPIO runtime proof, not MCSDK integration, and not
Hall readiness.

2026-05-27 software Hall timestamp-source follow-up: Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_timestamp_source_review_2026-05-27.md`.
The draft records `TIM1` as unavailable for software Hall timestamping because
it is tied to PWM / ADC injected / FOC timing, keeps current `TIM2` as the
generated MCSDK Hall clue path, limits `HAL_GetTick()` / SysTick to coarse
logging because of the `1KHz` `uwTickFreq` clue, and leaves an isolated
free-running timer plus `unsigned delta` as a future review target. It is not
STM32 source, not timer configuration, not MCSDK integration, and not Hall
readiness.

2026-05-27 software Hall debug-output follow-up: Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_debug_output_route_review_2026-05-27.md`.
The draft defines low-frequency snapshot fields for the future software Hall
adapter and blocks ISR printing, JSON formatting, UART transmit, ESP32 /
WebSocket, SWO, every-edge streaming, and direct MCSDK speed feedback. It is
not STM32 source, not UART implementation, not MCSDK integration, and not Hall
readiness.

2026-05-27 software Hall MCSDK firmware-integration boundary follow-up: Codex
added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md`.
The draft records that software Hall may produce only `direction_candidate`
and `speed_candidate` until accepted MCSDK interface evidence exists.
Generated clues such as `HALL_M1`, `SpeednTorqCtrlM1`,
`PIDSpeedHandle_M1`, `pSTC`, `MCI_Handle_t`, `FOCVars`,
`SPD_HALL_TIM_M1_IRQHandler`, `M1_SPEED_SENSOR=HALL_SENSOR`, and
`M1_HALL_TIMER_SELECTION=HALL_TIM2` are not hooks. It is not STM32 source, not
MCSDK hook evidence, not MCSDK integration, and not Hall readiness.

2026-05-27 software Hall MCSDK hook evidence request follow-up: Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md`.
The checklist requests exact generated or interface source files before any
future hook, including `hall_speed_pos_fdbk.c/.h`, `speed_torq_ctrl.c/.h`,
`mc_tasks.c/.h`, `mc_tasks_foc.c`, `mc_interface.c/.h`, `mc_api.c/.h`,
 `mc_app_hooks.c/.h`, `mc_parameters.c/.h`, `motorcontrol.c/.h`, interrupt
source files, current-feedback backend files, and ASPEP / register-interface
files. It is not STM32 source, not MCSDK hook evidence, not MCSDK integration,
and not Hall readiness.

2026-05-27 full Workbench `Src/Inc` snapshot follow-up: the user pointed to
the existing external generated project at
`C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`.
Codex confirmed the folder and copied generated `Src/`, `Inc/`, `cmake/`, and
top-level project/build metadata into
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`.
Codex also added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-27_001_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot.md`.
This resolves source availability for read-only MCSDK interface review, but it
is not firmware implementation, not MCSDK hook evidence, not build evidence,
not DMM proof, and not Hall readiness.

2026-05-27 MCSDK speed / position feedback interface review follow-up: Codex read the archived generated `Src/Inc` snapshot and added `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md`. The review traces `SPD_HALL_TIM_M1_IRQHandler`, `HALL_M1`, `HALL_CalcAvrgMecSpeedUnit`, `STC_GetSpeedSensor`, `SPD_GetAvrgMecSpeedUnit`, and `SPD_GetElAngle`. It records that future software Hall cannot push `direction_candidate` / `speed_candidate` directly into MCSDK; it must remain debug-only or wait for a reviewed `SpeednPosFdbk`-compatible component design. This is not firmware implementation, not MCSDK hook evidence, not build evidence, not DMM proof, and not Hall readiness.

2026-05-28 software Hall firmware-entry plan follow-up: Codex added
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_plan_2026-05-28.md`.
Decision:
`Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.
The plan is Chinese-first and records the future debug-only adapter layers,
state-machine order, ISR limits, debug fields, and MCSDK hard stops for the
current `PA0/PA1/PB4` route while keeping `PB3=LIN1` out of Hall. It does not
open STM32 firmware implementation, generated-code edits, flash, powered work,
Gate PWM, motor, Hall closed-loop, or sensorless readiness.
## Why This Sprint

P1 NUCLEO UART command handling and DMA + IDLE concept checks are recorded as passed. The next useful move is no longer more verbal review of STOP/DMA basics; it is creating the P2 no-power artifact set that will let the team approach MCSDK safely.

The first P2 card now exists at `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`. It deliberately found and preserved configuration conflicts instead of hiding them:

- `PA2/PA3` are convenient for P1 ST-LINK VCP but conflict with OPAMP/PGA planning.
- `PC5` appeared as both a V9 nFAULT candidate and an OPAMP2 feedback-related pin; the official pin-function pass now rejects `PC5` and prefers `PB12/TIM1_BKIN` as the draft nFAULT candidate.
- `PB3` is now fixed as current PCB2 `LIN1`, not current PCB2 Hall. SWO release/isolation is only relevant if a future hardware-rework or alternate Hall route reopens `PB3/TIM2_CH2`.
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
| Workbench/CubeMX config evidence | future MotorControl screenshot or `.stwb6` / legacy `.stmcx` source | selected Packet A fields accepted for no-power configuration evidence | CubeMX Home screenshot, NUCLEO `.ioc` draft, CubeMX `Pinout & Configuration` fallback screenshots, Workbench entry probe, legacy `My_First_FOC.stwb6`, 2026-05-16 custom capture package, 2026-05-17 source intake, and the 2026-05-21 generated-source review are captured. The accepted fields are FOC, NUCLEO-G474RE, STM32G474RETx, MY-STDRIVE101_POWER_BOARD, TIM1 complementary PWM, PB12/TIM1_BKIN, three-shunt current sensing, TIM2 Hall PA15/PB3/PB10, and USART2 PA2/PA3. This still does not prove current PCB2 physical routing or hardware readiness. |
| NUCLEO CubeMX `.ioc` draft | `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc` | saved | `.ioc` preserves the user hands-on Board Selector result and reads back NUCLEO, SWD, VCP, SWO, `PB12/TIM1_BKIN`, and `PB14/TIM1_CH2N` choices. |
| Pin/config conflict resolution | same card plus `apps/stm32_g474_foc/mcsdk_no_power_precheck/config_draft.md` | partially resolved | `PA2/PA3`, `PC5`/nFAULT, `PB3`, and V low-side PWM conflicts are resolved at pin-function and CubeMX `.ioc` level; board-routing evidence still must confirm the choices. |
| Pin/config safety review | `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md` | filled | Review defines evidence classes, hard stops, and the minimum evidence packet before trusting generated MCSDK configuration. |
| P2 璇佹嵁鍖?| `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md` | 宸叉寜褰撳墠搴撳瓨濉啓骞惰ˉ GUI fallback | 璇佹嵁鍖呰褰?`.stmcx`銆丮otorControl 閰嶇疆椤垫埅鍥俱€丆N8/EDA/netlist 璧扮嚎璇佹槑銆佹澘绾?STDRIVE101 淇濇姢璺緞璇佹槑鍜?SWO 閲婃斁璇佹嵁浠嶆槸闃诲椤癸紱鏂板鎴浘鍙瘉鏄?`.ioc` 鍙敱 CubeMX GUI 鎵撳紑銆?|
| Source packet intake / request | `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_intake_checklist_2026-05-14.md`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_request_pack_2026-05-14.md` | filled | Intake rules define accepted/rejected source packets; request pack tells the team exactly what `.stmcx`, MotorControl screenshot, CN8/EDA/netlist, and STDRIVE101 protection-path evidence to collect next. |
| User action queue | `apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md` | filled; current route clarified | Queue still records earlier source-packet governance. Current route no longer needs `PB3` as Hall; `PB3/SWO` is only an alternate-route blocker if hardware rework reopens it. |
| Source packet review template | `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_template_2026-05-14.md` | filled | Template defines Accept / Partial clue / Reject review states before any Packet A/B/C or PB3/SWO source can upgrade the evidence packet. |
| 2026-05-15 schematic candidate review | `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_001_cn8_stdrive101_schematic_candidate.md` | partial clue | User-provided screenshot is preserved and reviewed. User confirmed it matches the current physical power board and was drawn by the hardware teammate. It can guide Packet B/C review, but formal source revision/date, STM32 endpoint mapping, accepted `DT/MODE`, and `STBY` proof are still missing. |
| Non-hardware parallel track | `apps/stm32_g474_foc/mcsdk_no_power_precheck/non_hardware_parallel_track_2026-05-15.md` | filled | Records that hardware source work can be skipped for scheduling only while Packet A, STM32-side signal contract, future build-only gate, and delivery cleanup progress. |
| Packet A local probe, source candidate, and capture checklist | `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_local_probe_2026-05-15.md`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_checklist_2026-05-15.md` | filled; Packet A partial clue | Probe records the Workbench launcher and `.stwb6` candidate. Review accepts the file as a source candidate, but selected fields and custom-board context remain incomplete. Checklist defines the next screenshots without authorizing generated-project trust or hardware action. |
| Packet A custom capture package | `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md` | filled; preparation only | Package gives the exact Workbench no-power path, motor no-power measurement template, pin assignment table, and screenshot inbox for a new project-specific `.stwb6`; it does not yet accept Packet A or allow generation/build. |
| STM32-side signal contract | `apps/stm32_g474_foc/mcsdk_no_power_precheck/stm32_side_signal_contract_2026-05-15.md` | filled; all hardware-dependent fields still blocked/candidate | Defines intended STM32 responsibilities for future CN8-facing signals while preserving Packet A/B/C and PB3/SWO blockers. |
| Future build-only gate | `apps/stm32_g474_foc/mcsdk_no_power_precheck/future_build_only_gate_2026-05-15.md` | source prerequisite satisfied; no-power Debug build-only pass recorded | Defines prerequisites and forbidden actions for any MCSDK generated-project build-only work. The 2026-05-27 result proves only local no-power compile evidence. |
| P2 readiness snapshot | `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md` | filled; P2 remains in progress; no-power build-only pass recorded | Consolidates Packet A/B/C, PB3/SWO, signal-contract, and build-only status into one gate decision before any later generated-project or hardware claim. |
| DMM continuity / short-check request | `apps/stm32_g474_foc/mcsdk_no_power_precheck/dmm_continuity_short_check_request_2026-05-22.md` | request prepared; no measurement result yet | User fills the no-power table for `IA->PA0`, `IB->PA1`, `IC->PB4`, `PB3->LIN1`, `P14->3V3`, `P15->GND`, `nFAULT->PB12`, rail shorts, signal-to-rail shorts, and Hall-line shorts before software Hall adapter work. |
| Software Hall no-power algorithm prep | `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_no_power_algorithm_prep_2026-05-22.md` | filled; algorithm-side no-power prep only | Defines valid states `001/010/011/100/101/110`, rejects `000/111`, records transition rules, candidate forward/reverse sequences, debug observables, ISR limits, and MCSDK hard stops while DMM remains deferred, not passed. |
| Software Hall state-machine exercise card | `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_state_machine_exercise_card_2026-05-22.md` | waiting for user answer | User fills `001 -> 101`, `001 -> 001`, `001 -> 010`, and `000` judgments, plus five concept checks, before any pseudocode draft. |
| Software Hall adapter pseudocode draft | `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_pseudocode_draft_2026-05-27.md` | filled; pseudocode draft only | Defines future adapter responsibilities and ISR/MCSDK hard stops after L2 concept evidence. It is not firmware, not build evidence, not MCSDK Hall integration, and not Hall readiness. |
| Software Hall adapter processing-order card | `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_processing_order_card_2026-05-27.md` | filled; teaching card only | Explains the sequence after the user could not restate it. The next proof is a one-sentence user teach-back; this is not firmware, not build evidence, not MCSDK Hall integration, and not Hall readiness. |
| Software Hall host model | `src/software_hall_model.py`, `tests/test_software_hall_model.py` | filled; host-side algorithm model only | Tests valid/illegal states, first valid baseline, repeats, forward/reverse steps, abnormal jumps, bounce candidate, and a full candidate forward cycle without touching STM32 firmware or hardware. |
| Software Hall golden vectors | `tests/fixtures/software_hall_golden_vectors.json`, `tests/test_software_hall_vectors.py` | filled; host-side replay contract only | Replays fixed no-power input/output expectations for forward cycle, illegal/repeat/bounce/jump handling, and reverse adjacent step without touching STM32 firmware or hardware. |
| Software Hall MCSDK integration probe | `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_integration_probe_2026-05-27.md` | filled; read-only integration clue only | Identifies generated standard TIM2 Hall clues and records that current `PA0/PA1/PB4` software Hall is not MCSDK Hall integration. |
| Software Hall firmware-entry checklist | `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_checklist_2026-05-27.md` | filled; entry checklist only | Defines missing conditions before any future adapter code: populated-board DMM, GPIO/EXTI boundary, timestamp source, debug route, and separate MCSDK integration review. The build-only record now exists but does not open firmware implementation. |
| Software Hall GPIO/EXTI boundary review | `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_gpio_exti_boundary_review_2026-05-27.md` | filled; boundary draft only | Records `PA0/PA1/PB4` input candidates, `EXTI0/EXTI1/EXTI4` event-capture candidates, minimal ISR duties, and unresolved pull/timestamp/debug/build/DMM/MCSDK blockers. |
| Software Hall timestamp-source review | `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_timestamp_source_review_2026-05-27.md` | filled; timestamp-source draft only | Records `TIM1` hard stop, current `TIM2` as generated MCSDK Hall clue path, `HAL_GetTick()` coarse-only, and future isolated free-running timer / `unsigned delta` review targets. It does not configure a timer or implement firmware. |
| Software Hall debug-output route review | `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_debug_output_route_review_2026-05-27.md` | filled; debug-output route draft only | Records future low-frequency snapshot fields and blocks ISR printing, JSON formatting, UART transmit, ESP32 / WebSocket, SWO, every-edge streaming, and direct MCSDK speed feedback. It does not implement UART or firmware. |
| Software Hall MCSDK firmware-integration boundary review | `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md` | filled; MCSDK boundary draft only | Records generated MCSDK feedback objects and log-only file names as clues or hard stops, and blocks direct writes to `HALL_M1`, speed loop, speed PID, JEOC / FOC ISR, or TIM1 PWM without accepted interface evidence. |
| Software Hall MCSDK hook evidence request checklist | `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md` | filled; source-evidence request only | Requests exact generated or interface source files before any hook proposal, and rejects log-only names, screenshots, different-version files, host tests, and build-only success by itself as hook evidence. |
| Full Workbench `Src/Inc` snapshot | `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-27_001_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot.md` | filled; read-only generated-source evidence only | Archives exact generated `Src/`, `Inc/`, `cmake/`, and project/build metadata from the existing Workbench project. Enables read-only MCSDK interface review only; no firmware, hook, build, DMM, or Hall readiness claim is opened. |
| Software Hall MCSDK speed / position feedback interface review | `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md` | filled; read-only source-interface review only | Traces generated `HALL_M1`, speed/reliability calculation, speed-loop measurement, and FOC angle consumption; keeps software Hall debug-only unless a reviewed `SpeednPosFdbk`-compatible component proposal exists. |
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
- P2 璇佹嵁鍖呭凡缁忚褰曟墍鏈夌己澶遍樆濉為」锛屾垨宸叉洿鏂颁负鐪熷疄鏂板璇佹嵁閾炬帴銆?- Source packet request pack has been used for the next evidence handoff, or the missing source packets are explicitly still unavailable.
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
