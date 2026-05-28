# P2 Readiness Snapshot - 2026-05-15

This snapshot answers one control question:

`Can the project move from P2 no-power planning to generated-project trust,
build-only work, or hardware action?`

Current answer: partial no-power progress only. P2 remains in progress. Packet
A selected fields are now accepted as no-power configuration evidence by
`source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md`.
The 2026-05-28 software Hall firmware-entry plan is now added as a
Chinese-first debug-only no-power boundary:
`software_hall_firmware_entry_plan_2026-05-28.md`. Decision is
`Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.
It locks `PA0/PA1/PB4` as the future software GPIO/EXTI Hall route, keeps
`PB3=LIN1` out of Hall, defines state-machine order, ISR limits, debug fields,
MCSDK hard stops, and the current user checkpoint. It does not open firmware
implementation, generated-code edits, MCSDK hook, flash, powered work, Gate
PWM, motor, or Hall closed-loop readiness.
The build-only source prerequisite is satisfied, and a local no-power Debug
build-only record now exists:
`build_only_result_2026-05-27_qiansai_g474_stdrive101_foc_p2_debug.md`.
Hardware action is still not allowed.
The 2026-05-22 DMM continuity / short-check request is now the next real-world
evidence gate before software Hall adapter implementation. The build-only pass
does not replace `IA/IB/IC -> PA0/PA1/PB4`, `PB3=LIN1`, `P14/P15`, and
`nFAULT->PB12` DMM checks.
The 2026-05-22 software Hall no-power algorithm prep is allowed to proceed
while PCB2 is unpopulated because it is only a state-machine and test-contract
artifact. The DMM gate is hardware-side deferred, not passed, and still blocks
firmware implementation, MCSDK hook claims, powered work, and Hall readiness.
The 2026-05-22 software Hall state-machine exercise card is the next
algorithm-side user action. It asks the user to answer five checks and fill a
four-row Hall transition table before Codex generates any pseudocode draft.
This is a learning check only and does not open firmware implementation,
MCSDK integration, build, hardware, or Hall readiness.
The 2026-05-27 software Hall adapter pseudocode draft is now added as the next
algorithm-side no-power design artifact. It records future function
responsibilities, state fields, ISR limits, and MCSDK hard stops for the
`PA0/PA1/PB4` route. It is pseudocode only and does not open firmware
implementation, MCSDK Hall integration, build, hardware, Gate PWM, motor, or
Hall readiness.
The 2026-05-27 software Hall adapter processing-order teaching card is now
added because the user can classify table rows but cannot yet restate the
adapter sequence. It explains raw read -> illegal-state check -> first-valid
check -> repeated-state check -> bounce/timing check -> forward/reverse
adjacent check -> abnormal-jump count. It is a repair card only and does not
open firmware implementation, MCSDK Hall integration, build, hardware, Gate
PWM, motor, or Hall readiness.
The 2026-05-27 software Hall host model is now added as executable no-power
algorithm evidence. `src/software_hall_model.py` and
`tests/test_software_hall_model.py` verify the software Hall state-machine
rules on the host only. This is not STM32 firmware, not GPIO/EXTI behavior,
not MCSDK Hall integration, not DMM proof, and not Hall readiness.
The 2026-05-27 software Hall golden vectors are now added as replayable
no-power algorithm-contract evidence. `tests/fixtures/software_hall_golden_vectors.json`
and `tests/test_software_hall_vectors.py` capture expected input/output
decisions for forward cycle, illegal state, repeated state, bounce candidate,
abnormal jump, and reverse adjacent step. This is still host-side only; it is
not firmware, not GPIO/EXTI behavior, not MCSDK Hall integration, not DMM
proof, and not Hall readiness.
The 2026-05-27 software Hall MCSDK integration probe is now added as read-only
generated-source clue evidence. It identifies the standard MCSDK Hall route as
TIM2 hardware Hall through `MX_TIM2_Init()`, `HALL_M1`, `SpeednTorqCtrlM1`,
`PIDSpeedHandle_M1`, `M1_SPEED_SENSOR=HALL_SENSOR`, and generated
`hall_speed_pos_fdbk` / `speed_torq_ctrl` file names. This confirms the
current `PA0/PA1/PB4` software Hall route is not directly connected to MCSDK
standard TIM2 Hall and still needs a separate firmware-integration review.
The 2026-05-27 software Hall timestamp-source review is now added as a
no-power boundary draft. It records `TIM1` as a hard no because generated
clues tie it to PWM, ADC injected triggering, and FOC timing through
`MX_TIM1_Init()`, `TIM1_UP_TIM16_IRQn`, and `ADC_EXTERNALTRIGINJEC_T1_TRGO`.
It records `TIM2` as current hard stop because the generated route uses
`HAL_TIMEx_HallSensor_Init` and `M1_HALL_TIMER_SELECTION=HALL_TIM2` for
standard MCSDK Hall, not current `PA0/PA1/PB4` software Hall. It limits
`HAL_GetTick()` / SysTick to coarse logs because the local HAL clue is
`uwTickFreq = HAL_TICK_FREQ_DEFAULT; /* 1KHz */`, and it keeps a future
`dedicated free-running timer` plus `unsigned delta` as a review target only.
The 2026-05-27 software Hall debug-output route review is now added as a
no-power boundary draft. It defines low-frequency debug snapshot fields such
as `current_raw_state`, `last_accepted_state`, `edge_count`,
`illegal_state_count`, `abnormal_jump_count`, `last_edge_dt_ticks`,
`direction_candidate`, and `speed_candidate`. It blocks every-edge streaming,
ISR `printf`, JSON formatting, UART transmit, ESP32/WebSocket, SWO, and direct
MCSDK speed feedback. It is not firmware, not UART implementation, and not
Hall readiness.
The 2026-05-27 software Hall MCSDK firmware-integration boundary review is now
added as a no-power boundary draft. It records that future software Hall output
is only `direction_candidate` and `speed_candidate` until accepted MCSDK
interface evidence exists. `HALL_M1`, `SpeednTorqCtrlM1`, `PIDSpeedHandle_M1`,
`pSTC`, `MCI_Handle_t`, `FOCVars`, `SPD_HALL_TIM_M1_IRQHandler`,
`M1_SPEED_SENSOR=HALL_SENSOR`, `M1_HALL_TIMER_SELECTION=HALL_TIM2`, and the
log-only `hall_speed_pos_fdbk.c/.h`, `speed_torq_ctrl.c/.h`, and
`mc_app_hooks.c/.h` clues are not MCSDK hooks. This is not firmware
implementation, not MCSDK hook evidence, and not Hall readiness.
The 2026-05-27 software Hall MCSDK hook evidence request checklist is now
added as a no-power source-evidence request. It converts log-only generated
file names into an exact request for generated / MCSDK interface source files,
call-timing evidence, data-unit evidence, ownership evidence, and rollback
evidence before any hook proposal. It is not firmware implementation, not a
MCSDK hook, not MCSDK integration, and not Hall readiness.
The 2026-05-27 full Workbench `Src/Inc` snapshot is now archived from the
existing external project path
`C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`.
This resolves the source-availability part of the MCSDK hook evidence request:
exact generated `Src/`, `Inc/`, `cmake/`, and project/build metadata now exist
in the repo for read-only interface review. It still does not open firmware
implementation, generated-code edits, MCSDK hook work, no-power build claims,
DMM proof, Hall closed-loop, Gate PWM, motor, power-stage, or sensorless
readiness.
The 2026-05-27 software Hall MCSDK speed / position feedback interface review is now added as read-only source-interface evidence. It traces the archived generated chain from TIM2 Hall ISR into `HALL_M1`, `HALL_CalcAvrgMecSpeedUnit`, `STC_GetSpeedSensor`, `SPD_GetAvrgMecSpeedUnit`, and `SPD_GetElAngle`. It records that MCSDK consumes electrical angle, speed units, timing, and reliability behavior, not just `direction_candidate` and `speed_candidate`. `speed_pos_fdbk.h` is missing from the archived project `Src/Inc` snapshot, so a custom `SpeednPosFdbk` component is not accepted. Software Hall remains debug-only unless a separate reviewed component proposal, DMM evidence, no-power build record, hook list, and rollback plan exist.
The 2026-05-21 current PCB2 software Hall route is now confirmed for
no-power adapter planning: `P14/P15=3V3/GND`, `PB3=LIN1`, and
`HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`. This removes P14/P15 and PB3/Hall
ambiguity from the route-selection discussion, but it does not prove
continuity, firmware integration, Hall closed-loop behavior, or powered
readiness.
The 2026-05-18 Packet A capture task package is workflow-only preparation, not
accepted Packet A evidence. The 2026-05-19 Workbench capture attempt adds only
launch/control-board visibility and then stops because no acceptable self-made
STDRIVE101 power-stage context was captured. The 2026-05-19 ProDoc `.epro`
intake adds a current schematic-source clue for the self-developed STDRIVE101
driver board, but it has no PCB layout data and does not prove NUCLEO `CN8` or
STM32 endpoint mapping. The 2026-05-19 Gerber PCB2 intake adds board-side
manufacturing-output and flying-probe pad-net clues, but still does not prove
NUCLEO `CN8`, STM32 endpoint mapping, continuity, or powered readiness.
The 2026-05-19 hardware supplement handoff is now the current exact request
pack for board-revision confirmation, endpoint mapping, connector orientation,
PB3/SWO, STDRIVE101 protection details, PCB source, and later no-power
continuity records. The 2026-05-19 minimal hardware request narrows the first
hardware-teammate packet to exact Gerber PCB2 revision confirmation,
`CN3 -> NUCLEO/CN8 -> STM32 pin` mapping, and marked `CN3` / `J_HALL` pin-1
evidence. The 2026-05-19 Workbench asset probe found installed Board Designer
and Board Manager executables referenced by Workbench config, but it did not
produce an accepted custom board definition or `.stwb6`. The 2026-05-19 PCB2
mapping / pin-1 / protection packet adds a current PCB2 source statement,
P1-P15 endpoint table, connector-orientation images, Hall relationship, PB3/SWO
handling, and STDRIVE101 protection-chain intent. A later clarification image
states `PC7/PB3/PB10` was an alternate suggestion, not current PCB2 physical
routing; current PCB2 Hall routing is `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`.
The 2026-05-19 current PCB2 Hall/PWM strategy review opens the no-PCB-change
path first: current PWM / driver-input routing
`HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10` and software
Hall feasibility on `PA0/PA1/PB4` need Packet A / firmware design review.
The 2026-05-19 Packet A / firmware feasibility review concludes that this
no-PCB-change route remains feasibility only: current PWM is not cleared as
standard MCSDK `TIM1` complementary PWM selected-field evidence, and
`PA0/PA1/PB4` is not cleared as same-timer hardware Hall. Packet A is not
accepted.
The 2026-05-19 software Hall adapter design review keeps the same boundary:
`PA0/PA1/PB4` may be discussed only as future GPIO/EXTI sampling, edge
timestamping, valid-state filtering, minimal ISR responsibility, and MCSDK
integration design. It does not implement an adapter, does not define a runtime
API, does not accept Packet A, and provides no generated-project trust.
The 2026-05-19 Packet A Board Designer / Board Manager path review concludes
that the local Board Designer / Board Manager path exists as documentation and
tool clue for a self-developed STDRIVE101 board, but Packet A still blocked:
no custom/user board artifact, project-specific `.stwb6`, or selected-field
screenshot is accepted, and there is no generated-project trust.
The 2026-05-19 Packet A Board Designer / Manager GUI-only checklist now defines
the next user-side screenshot capture path and hard stops. It does not launch
GUI tools, does not create a board, does not create a `.stwb6`, and does not
accept Packet A.
The 2026-05-19 MY_FOC generated project source review records the user's new
Workbench project as `Partial clue / generated project quarantined / Packet A
not accepted`. It proves a real Workbench 6.4.2 generated project exists, but
the project is `SIX_STEP`, not FOC; current sensing and fault/break are
disabled, the motor entry is a demo clue, and Hall/PWM pins still need either
an accepted physical change or a new matching Workbench route. The user says
pins can be changed, so the mismatch is editable future work, not a permanent
rejection. No generated-project trust is added.
The 2026-05-19 MY_FOC manual FOC edit attempt changed the source Workbench
`MY_FOC.stwb6` from `"algorithm": "sixStep"` to `"algorithm": "FOC"`, but
Workbench then failed to load the file with `婵炴垶鎸撮崑鎾绘煠閸撴彃澧撮柡浣革功閹?/ 闂佸搫鍟版慨鐢垫兜閸洖绀夐柣妯煎劋缁佷即鏌￠崒姘煑婵炲棭鏅? Codex
rolled the external source back to the backup, so the current external
`MY_FOC.stwb6` again reads `"algorithm": "sixStep"`. This proves the one-field
manual edit is not a valid FOC conversion path. Packet A is still not accepted.
The 2026-05-19 Packet A FOC route decision narrows the next valid path:
Workbench GUI must create or convert a complete FOC source, or another complete
reviewable FOC `.stwb6` must be supplied. Do not retry partial text edits. The
next source must show FOC, `NUCLEO-G474RE`, the self-developed/custom
STDRIVE101 board path, enabled current sensing, enabled fault/break handling,
and a reviewable Hall/PWM route before any generated-project trust can change.
The 2026-05-20 Packet C STDRIVE101 protection detail review narrows
`DT/MODE`, `CP`, `SCREF`, `nFAULT`, `REG12`, bootstrap, `STBY`, and VDS
monitoring. It marks the old `V_DSth = 0.249V` / `I_trip ~= 55A` note as not
accepted because the current repo-local official extraction supports
`VDSth = VSCREF`. Packet C remains only `Partial clue`; P3 remains blocked.
Hardware action is not a P2 state.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
- No flash or board run from a generated motor-control project.

## Feature Sentence

The P2 readiness snapshot consolidates Packet A/B/C, PB3/SWO, signal-contract,
and build-only gate status so future turns can see exactly what is ready,
blocked, or only a planning artifact.

## Current Gate Decision

| Gate | Current decision | Why |
| --- | --- | --- |
| P2 no-power planning | In progress | P2 documents, reviews, and blocker governance exist. |
| Packet A MCSDK / MotorControl evidence | Accepted for no-power selected-field configuration | `workbench_foc_capture_success_2026-05-21.md` plus `source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md` accept FOC, `NUCLEO-G474RE`, `STM32G474RETx`, custom STDRIVE101 power-board model, TIM1 complementary PWM, `PB12/TIM1_BKIN`, three-shunt current sensing, TIM2 Hall, and USART2 ASPEP/MCP as configuration evidence only. |
| Generated-project trust | Build-only Debug pass recorded / no runtime or hardware trust | Packet A selected fields are accepted and the generated project has a local no-power Debug build-only record. Trust remains limited to no-power configuration and compile evidence; no firmware runtime, route, or hardware behavior is proven. |
| No-power build-only generated project | Passed on local STM32Cube bundled toolchain | `cmake --build ... --config Debug` returned exit code `0`; Ninja reported `ninja: no work to do`; `.elf` and `.map` artifacts were confirmed. This is an up-to-date build-only pass, not a clean rebuild and not a powered test. |
| Packet B CN8 / board-route proof | Partial clue / current PCB2 mapping source, Hall/PWM conflicts clarified | The 2026-05-19 `.epro` and Gerber PCB2 package show board-side `CN3`, `U1`, `J_HALL`, `J_MOTOR`, shunt, protection, and output pad/net clues. The 2026-05-19 mapping packet adds P1-P15 endpoint rows and clarifies current PCB2 Hall route as `IA/IB/IC -> PA0/PA1/PB4`; the accepted Packet A Workbench route does not prove this physical route, and continuity remains missing. |
| Packet C STDRIVE101 protection proof | Partial clue / current board-intent statement, still blocked for final proof | The `.epro`, Gerber, and 2026-05-19 mapping packet now show `DT/MODE -> GND`, `CP -> 100 nF -> GND`, `SCREF` divider, `nFAULT` pull-up, no separate `STBY`, `REG12`, bootstrap, output, and MOSFET bridge clues. Threshold math, STM32 endpoint handling, continuity, and powered validation remain unresolved. |
| Packet C STDRIVE101 protection detail review | Packet C detail narrowed / protection proof still partial clue / P3 still blocked | `packet_c_stdrive101_protection_detail_review_2026-05-20.md` separates `DT/MODE`, `CP`, `SCREF`, `nFAULT`, `REG12`, bootstrap, `STBY`, and VDS monitoring into sub-items. The old `55A` VDS claim is not accepted; no powered readiness is added. |
| Hardware supplement handoff | Open / ready | `hardware_supplement_handoff_2026-05-19.md` converts the remaining board-side blockers into exact hardware teammate requests. It is workflow/evidence governance only and does not upgrade Packet B/C, PB3/SWO, `J_HALL`, continuity, or readiness. |
| Minimal hardware request | Open / ready | `hardware_teammate_min_request_2026-05-19.md` is the short first packet to send to the hardware teammate: exact Gerber PCB2 revision confirmation, complete `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping, and marked `CN3` / `J_HALL` pin-1 evidence. |
| Packet A Workbench asset probe | Partial clue / local tool path found / blocked | `packet_a_workbench_asset_probe_2026-05-19.md` found Workbench references to Board Designer / Board Manager and local executables, but no accepted self-developed STDRIVE101 board definition, `.stwb6`, or selected-field screenshots. |
| Current PCB2 Hall/PWM strategy | No-power strategy review opened / no PCB change first | `current_pcb2_hall_pwm_strategy_2026-05-19.md` downgrades the old standard `TIM1` PWM and `PA15/PB3/PB10` Hall drafts to historical or alternate candidates only. Current PCB2 routes need Packet A / firmware feasibility review and do not upgrade Hall readiness. |
| Current PCB2 Packet A / firmware feasibility | No-PCB-change route remains feasibility only / Packet A not accepted | `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md` reviews the current PWM and Hall routes against local pin-function clues. It does not clear standard MCSDK TIM1 selected fields, same-timer hardware Hall, generated-project trust, or build-only work. |
| Software Hall adapter design review | Software Hall adapter remains no-power design review / Packet A not accepted | `software_hall_adapter_design_review_2026-05-19.md` defines future GPIO/EXTI sampling, timestamping, valid-state filtering, bounce/repeated-state rejection, minimal ISR responsibility, MCSDK integration boundaries, and `hardware-rework planning` hard stops. It does not add firmware, runtime APIs, generated source, Hall readiness, generated-project trust, or build-only clearance. |
| Current PCB2 software Hall route confirmation | Software Hall route confirmed for no-power adapter planning / no firmware implementation / no Hall readiness | User confirmed `P14/P15=3V3/GND`, `PB3=LIN1`, and Hall `IA/IB/IC -> PA0/PA1/PB4`. Software Hall is now the preferred no-PCB-change direction. MCSDK standard TIM2 Hall `PA15/PB3/PB10` is not the current PCB2 Hall route. |
| DMM continuity / short-check request | Requested / no measurement result yet / software Hall implementation blocked | `dmm_continuity_short_check_request_2026-05-22.md` defines the exact no-power table for `IA->PA0`, `IB->PA1`, `IC->PB4`, `PB3->LIN1`, `P14->3V3`, `P15->GND`, `nFAULT->PB12`, signal-to-rail shorts, and Hall-line pair shorts. |
| Software Hall no-power algorithm prep | Algorithm-side no-power preparation / no firmware implementation / no Hall readiness | `software_hall_no_power_algorithm_prep_2026-05-22.md` defines valid states, illegal-state handling, transition rules, candidate forward/reverse sequences, debug observables, ISR limits, and MCSDK hard stops. It is allowed while DMM is hardware-side deferred because it is not firmware implementation or hardware validation. |
| Software Hall state-machine exercise | User Hall state-machine exercise requested / no firmware implementation / no Hall readiness | `software_hall_state_machine_exercise_card_2026-05-22.md` gives the user five Chinese checks and a four-row response table for `001 -> 101`, `001 -> 001`, `001 -> 010`, and `000`. It is a learning check only and does not open firmware implementation. |
| Software Hall adapter pseudocode draft | Pseudocode draft added / no firmware implementation / no MCSDK Hall integration / no Hall readiness | `software_hall_adapter_pseudocode_draft_2026-05-27.md` records function responsibilities, decision order, state fields, ISR limits, and MCSDK hard stops for the future `PA0/PA1/PB4` software Hall adapter. It is not source code and does not open build, flash, Gate PWM, motor, or powered work. |
| Software Hall adapter processing-order card | Teaching card added / no firmware implementation / no MCSDK Hall integration / no Hall readiness | `software_hall_adapter_processing_order_card_2026-05-27.md` explains the adapter sequence after the user could not restate it. It is a no-power repair artifact only and does not open firmware, build, flash, Gate PWM, motor, or powered work. |
| Software Hall host model | Host-side software Hall reference model / no firmware implementation / no MCSDK Hall integration / no Hall readiness | `src/software_hall_model.py` and `tests/test_software_hall_model.py` make the state-machine rules executable on the host. It is not STM32 source, GPIO/EXTI proof, MCSDK integration, DMM proof, or Hall readiness. |
| Software Hall golden vectors | Host-side software Hall golden vectors / no firmware implementation / no MCSDK Hall integration / no Hall readiness | `tests/fixtures/software_hall_golden_vectors.json` and `tests/test_software_hall_vectors.py` provide replayable input/output expectations for future adapter review. It is not STM32 source, GPIO/EXTI proof, MCSDK integration, DMM proof, or Hall readiness. |
| Software Hall MCSDK integration probe | MCSDK Hall integration points identified as read-only clues / no firmware implementation / no MCSDK Hall integration / no Hall readiness | `software_hall_mcsdk_integration_probe_2026-05-27.md` records that generated MCSDK clues point to standard TIM2 hardware Hall, not current PCB2 `PA0/PA1/PB4` software Hall. It does not open firmware integration. |
| Software Hall firmware-entry checklist | Software Hall firmware-entry checklist / no firmware implementation / no MCSDK Hall integration / no Hall readiness | `software_hall_firmware_entry_checklist_2026-05-27.md` defines the entry conditions before any future adapter code: populated board, DMM table, GPIO/EXTI boundary review, timestamp source, debug route, build-only result awareness, and a separate MCSDK integration review. It does not open firmware implementation. |
| Software Hall GPIO/EXTI boundary review | Software Hall GPIO/EXTI boundary review draft / no firmware implementation / no GPIO runtime proof / no Hall readiness | `software_hall_gpio_exti_boundary_review_2026-05-27.md` records the static future boundary: `PA0/PA1/PB4` as input candidates, `EXTI0/EXTI1/EXTI4` as event-capture candidates, minimal ISR duties, and pull/timestamp/debug blockers. It does not write firmware or prove runtime behavior. |
| Software Hall timestamp-source review | Software Hall timestamp-source review draft / no firmware implementation / no timer configuration / no Hall readiness | `software_hall_timestamp_source_review_2026-05-27.md` records `TIM1` as unavailable for software Hall timestamping, `TIM2` as the generated MCSDK Hall clue path rather than current software Hall clearance, `HAL_GetTick` / SysTick as coarse-only, and a future `dedicated free-running timer` with `unsigned delta` as review target only. It does not configure a timer or open firmware implementation. |
| Software Hall debug-output route review | Software Hall low-frequency debug-output route review draft / no firmware implementation / no UART implementation / no Hall readiness | `software_hall_debug_output_route_review_2026-05-27.md` records future low-frequency debug snapshot fields and blocks ISR printing, JSON formatting, UART transmit, ESP32/WebSocket, SWO, every-edge streaming, and direct MCSDK speed feedback. It does not implement UART or firmware. |
| Software Hall MCSDK firmware-integration boundary review | Software Hall MCSDK firmware-integration boundary review draft / no firmware implementation / no MCSDK hook / no Hall readiness | `software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md` records that future `direction_candidate` and `speed_candidate` must not be written into `HALL_M1`, `SpeednTorqCtrlM1`, speed PID, JEOC / FOC ISR, or TIM1 PWM without accepted interface evidence. It is not firmware and not a MCSDK hook. |
| Software Hall MCSDK hook evidence request checklist | Software Hall MCSDK hook evidence request checklist / no firmware implementation / no MCSDK hook / no Hall readiness | `software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md` converts log-only generated file names into a request for exact generated or MCSDK interface source files before any hook proposal. It is not firmware and not a MCSDK hook. |
| Full Workbench `Src/Inc` snapshot | Full generated Src/Inc snapshot archived / source interface evidence available for read-only review / no firmware implementation / no MCSDK hook / no Hall readiness | `source_packet_review_2026-05-27_001_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot.md` and `packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/` archive exact generated source/interface evidence. This enables read-only MCSDK interface review only; it does not open implementation, build, flash, or hardware readiness. |
| Packet A Board Designer / Board Manager path review | Board Designer / Board Manager path exists as local documentation and tool clue / Packet A still blocked | `packet_a_board_designer_manager_path_review_2026-05-19.md` confirms local Workbench external-tool entries, Board Designer / Board Manager executables, and Board Designer manual custom-board workflow clues. It does not accept Packet A, does not create the self-developed STDRIVE101 board source, and does not add generated-project trust. |
| Packet A Board Designer / Manager GUI-only checklist | GUI-only checklist prepared / Packet A still blocked | `packet_a_board_designer_manager_gui_checklist_2026-05-19.md` defines later screenshot names, save directory, custom/import/create board screens, Power/Control/Inverter board flows, Board Aggregation, Finalize/save prompt, Board Manager import/list path, and hard stops. It does not launch GUI or add generated-project trust. |
| MY_FOC generated project source review | Partial clue / generated project quarantined / Packet A not accepted | `source_packet_review_2026-05-19_005_my_foc_generated_project.md` archives selected files from the user-created `MY_FOC` project and records that it is `SIX_STEP`, not FOC. Pins can be changed later, but that requires a new reviewable FOC configuration and matching physical route. No generated-project trust, build-only clearance, or powered readiness is added. |
| MY_FOC manual FOC edit rollback | Manual FOC source edit failed Workbench reload / rolled back / Packet A still not accepted | `my_foc_foc_candidate_edit_2026-05-19.md` records the external `.stwb6` source edit attempt, Workbench load failure, and rollback to the backup. The current external `MY_FOC.stwb6` again reads `"algorithm": "sixStep"`; the failed FOC candidate is negative evidence only. |
| Packet A FOC route decision after MY_FOC rollback | Route narrowed / GUI-created FOC source required / Packet A still blocked | `packet_a_foc_route_decision_2026-05-19.md` compares the legacy FOC source, restored `MY_FOC` six-step source, and failed manual FOC candidate. The next valid source must be created through Workbench GUI or supplied as a complete reviewable FOC `.stwb6`; partial text edits are rejected. |
| Packet A Workbench FOC source capture | Workbench FOC source captured / no-power source evidence upgraded / generated-source and hardware trust blocked | `workbench_foc_capture_success_2026-05-21.md` archives `QIANSAI_G474_STDRIVE101_FOC_P2_2026-05-21.stwb6` and `MY-STDRIVE101_POWER_BOARD.foc_no_power_2026-05-21.json`. Read-only checks confirm `FOC`, `NUCLEO-G474RE`, `STM32G474RETx`, `MY-STDRIVE101_POWER_BOARD`, Hall selection, three-shunt current sensing, and `PB12/TIM1_BKIN`. This is source evidence only; it does not authorize build, flash, 24V, Gate PWM, Hall closed-loop, motor, power-stage, or sensorless claims. |
| Packet A generated-source side-effect review | Packet A selected fields accepted / build-only source prerequisite satisfied / later build-only pass recorded | `source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md` accepts the generated project side-effect as no-power configuration evidence for FOC, TIM1 complementary PWM, `PB12/TIM1_BKIN`, three-shunt current sensing, TIM2 Hall, and USART2 ASPEP/MCP. The 2026-05-27 build-only result adds local compile evidence only. Current PCB2 Hall/PWM route trust, Packet B/C, continuity, hardware, and powered claims remain blocked. |
| PB3 Hall B readiness | Not the current PCB2 Hall path / still blocked for any alternate use | Current `.ioc` still records `PB3.Signal=SYS_JTDO-SWO`. The 2026-05-17 pin table does not release SWO by itself. The 2026-05-19 clarification says current PCB2 uses `PB3` for `LIN1`, while `PC7/PB3/PB10` Hall was only an alternate suggestion. |
| P3 powered or motor work | Not allowed | P2 has no continuity checks, current-limited bring-up record, waveform checks, or rollback evidence. |

## Readiness Matrix

| Track | Current evidence | Current status | Unlock condition |
| --- | --- | --- | --- |
| Packet A | `packet_a_local_probe_2026-05-15.md`, `packet_a_capture_checklist_2026-05-15.md`, `source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`, `source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`, `source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`, `source_packet_review_2026-05-18_001_motor_wiring_definition.md`, `packet_a_capture_task_2026-05-18.md`, `source_packet_review_2026-05-19_001_packet_a_workbench_capture_attempt.md`, `packet_a_workbench_asset_probe_2026-05-19.md`, `source_packet_review_2026-05-19_005_my_foc_generated_project.md`, `workbench_foc_capture_success_2026-05-21.md`, and `source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md` | Packet A selected fields accepted for no-power configuration / hardware trust still blocked | The generated route is acceptable for build-only configuration evidence after toolchain path is available. It does not reconcile the Workbench Hall route `PA15/PB3/PB10` with current PCB2 `PA0/PA1/PB4`, and it does not prove current PCB2 PWM/Hall routing, Packet B/C, continuity, or powered readiness. |
| Packet B | `source_packet_review_2026-05-15_001_cn8_stdrive101_schematic_candidate.md`, `source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`, `mcu_pin_compatibility_check_2026-05-17.md`, `source_packet_review_2026-05-19_002_prodoc_p1_epro.md`, `source_packet_review_2026-05-19_003_gerber_pcb2.md`, and `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md` | Partial clue / current PCB2 mapping source, Hall/PWM conflicts clarified | Current PCB2 endpoint mapping is now clear at source level: `P14/P15=3V3/GND`, `PB3=LIN1`, `PB10=HIN2`, and Hall is `IA/IB/IC -> PA0/PA1/PB4`. Still need later no-power continuity before trusting generated pins or readiness. |
| Packet C | `stdrive101_protection_path_review_2026-05-14.md`, `source_packet_review_2026-05-19_002_prodoc_p1_epro.md`, `source_packet_review_2026-05-19_003_gerber_pcb2.md`, and `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md` | Partial clue / current board-intent statement, still blocked for final proof | Finish protection review for `DT/MODE`, `STBY`, `NFAULT`, `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, and VDS monitoring, including threshold math, STM32 endpoint handling, continuity, and later powered validation. |
| Packet C detail | `packet_c_stdrive101_protection_detail_review_2026-05-20.md`, `docs/03_hardware_notes/protection_thresholds.md`, repo-local STDRIVE101 extracted text | Detail narrowed / old `55A` VDS claim not accepted / P3 blocked | Human-check the PDF table, correct the threshold note, prove the named `CP` route, prove `VS/VM`, and add later no-power continuity before any P3 action. |
| Hardware supplement handoff | `hardware_supplement_handoff_2026-05-19.md`, `hardware_teammate_min_request_2026-05-19.md`, `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md` | Mostly answered / Packet A strategy needed | Current PCB2 version, mapping, pin-1, Hall relationship, PB3/SWO guidance, and protection-chain statements were provided. The next request is not more hardware mapping; it is a no-power Packet A / firmware decision for software Hall on `PA0/PA1/PB4` or future hardware rework. |
| Current PCB2 Hall/PWM strategy | `current_pcb2_hall_pwm_strategy_2026-05-19.md`, `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md`, local MCSDK `STM32G474RETx.json` pin-function clue | Software Hall route confirmed for no-power adapter planning | Current PCB2 proceeds with no-PCB-change software Hall first: `PA0/PA1/PB4` GPIO/EXTI sampling, `PB3=LIN1`, and P14/P15 confirmed as `3V3/GND`. Hardware rework is fallback only. |
| Current PCB2 Packet A / firmware feasibility | `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md`, local MCSDK `STM32G474RETx.json` pin-function clue, `future_build_only_gate_2026-05-15.md` | Feasibility only / Packet A not accepted | The current no-PCB-change route can proceed only as later firmware design review. It does not open generated-project trust or build-only clearance. |
| Software Hall adapter design review | `software_hall_adapter_design_review_2026-05-19.md`, `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md`, `future_build_only_gate_2026-05-15.md` | Software Hall route confirmed for no-power adapter planning / no firmware implementation / no Hall readiness | A later firmware task may configure `PA0/PA1/PB4` as GPIO/EXTI, read three Hall bits, reject `000/111`, capture edge timestamps, and keep ISR work minimal. It still does not claim MCSDK Hall integration, Hall closed-loop, Gate PWM, or powered readiness. |
| DMM continuity / short-check request | `dmm_continuity_short_check_request_2026-05-22.md` | Requested / no measurement result yet | The user should return `Signal | STM32 pin | DMM result | Beep? | Note / photo ID` rows before any software Hall adapter implementation or powered planning. |
| Software Hall no-power algorithm prep | `software_hall_no_power_algorithm_prep_2026-05-22.md` | Algorithm-side no-power preparation only | The algorithm role can review Hall state-machine rules, candidate sequences, debug observables, ISR limits, and MCSDK entry research while PCB2 is unpopulated. This does not implement firmware and does not pass the DMM gate. |
| Software Hall state-machine exercise card | `software_hall_state_machine_exercise_card_2026-05-22.md` | Waiting for user answer | The user fills the four-row transition table and answers the five checks. Codex reviews the answer before writing any pseudocode or firmware-boundary draft. |
| Software Hall adapter pseudocode draft | `software_hall_adapter_pseudocode_draft_2026-05-27.md` | Pseudocode draft only / no implementation | Future implementation still needs DMM continuity / short-check evidence, GPIO/EXTI boundary review, timestamp-source decision, no-power build boundary, and an explicit MCSDK integration decision. |
| Software Hall adapter processing-order card | `software_hall_adapter_processing_order_card_2026-05-27.md` | Teaching card only / no implementation | The next learner proof is a one-sentence teach-back of the processing order. This still does not pass DMM, implement firmware, open MCSDK Hall integration, or prove Hall readiness. |
| Software Hall host model | `src/software_hall_model.py`, `tests/test_software_hall_model.py`, `software_hall_host_model_review_2026-05-27.md` | Host-side executable specification only | Host tests verify the algorithm contract without touching STM32 firmware. Firmware work still needs DMM, GPIO/EXTI boundary review, timestamp-source decision, no-power build boundary, and MCSDK integration decision. |
| Software Hall golden vectors | `tests/fixtures/software_hall_golden_vectors.json`, `tests/test_software_hall_vectors.py`, `software_hall_golden_vectors_review_2026-05-27.md` | Host-side replay contract only | Golden vectors let future adapter behavior be compared against fixed no-power examples. Firmware work still needs DMM, GPIO/EXTI boundary review, timestamp-source decision, no-power build boundary, and MCSDK integration decision. |
| Software Hall MCSDK integration probe | `software_hall_mcsdk_integration_probe_2026-05-27.md`, generated-project clue files | Read-only integration clue only | Identifies `HALL_M1`, `TIM2`, `SpeednTorqCtrlM1`, and generated feedback file names as clues. A separate firmware-integration review is required before any MCSDK hook or speed-loop claim. |
| Software Hall firmware-entry checklist | `software_hall_firmware_entry_checklist_2026-05-27.md` | Entry checklist only / no implementation | Freezes the minimum entry conditions before the first software Hall adapter firmware commit. The missing blockers remain DMM, GPIO/EXTI boundary, timestamp source, debug route, and separate MCSDK integration review; the build-only result is now recorded but does not open firmware implementation. |
| Software Hall GPIO/EXTI boundary review | `software_hall_gpio_exti_boundary_review_2026-05-27.md` | Boundary draft only / no runtime proof | Drafts `PA0/PA1/PB4` as software input candidates and `EXTI0/EXTI1/EXTI4` as event-capture candidates. Implementation remains blocked by DMM, pull-mode decision, timestamp source, debug route, build-only record, and MCSDK integration review. |
| Software Hall timestamp-source review | `software_hall_timestamp_source_review_2026-05-27.md` | Timestamp-source draft only / no timer configuration | Drafts the future timestamp-source boundary. `TIM1` is excluded, current `TIM2` clues are standard MCSDK Hall, `HAL_GetTick` is coarse-only, and an isolated free-running timer remains a future review target. Firmware work still needs exact timer-instance review, DMM, debug route, build-only record, and MCSDK integration decision. |
| Software Hall debug-output route review | `software_hall_debug_output_route_review_2026-05-27.md` | Debug-output route draft only / no UART implementation | Drafts low-frequency snapshot fields and output hard stops. Firmware work still needs DMM, exact output-route review, UART ownership review if used, build-only record, and MCSDK integration decision. |
| Software Hall MCSDK firmware-integration boundary review | `software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md`, generated-project clue files | Boundary draft only / no MCSDK hook | Records `HALL_M1`, `SpeednTorqCtrlM1`, `PIDSpeedHandle_M1`, `pSTC`, `MCI_Handle_t`, `FOCVars`, `SPD_HALL_TIM_M1_IRQHandler`, `M1_SPEED_SENSOR=HALL_SENSOR`, `M1_HALL_TIMER_SELECTION=HALL_TIM2`, `hall_speed_pos_fdbk.c/.h`, `speed_torq_ctrl.c/.h`, and `mc_app_hooks.c/.h` as clues or hard stops. Any hook still needs accepted interface evidence, no-power build record, DMM, and rollback plan. |
| Software Hall MCSDK hook evidence request checklist | `software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md`, generated-project log clues | Evidence request only / no MCSDK hook | Requests exact source/interface evidence including `hall_speed_pos_fdbk.c/.h`, `speed_torq_ctrl.c/.h`, `mc_tasks.c/.h`, `mc_tasks_foc.c`, `mc_interface.c/.h`, `mc_api.c/.h`, `mc_app_hooks.c/.h`, `mc_parameters.c/.h`, `motorcontrol.c/.h`, interrupt sources, current-feedback backend files, and ASPEP / register-interface files before any hook proposal. |
| Full Workbench `Src/Inc` snapshot | `source_packet_review_2026-05-27_001_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot.md`, `packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/` | Exact source snapshot archived / read-only review only | Archives generated `Src/`, `Inc/`, `cmake/`, and top-level project/build metadata with manifest and hashes. Static review confirms generated MCSDK Hall remains TIM2 `PA15/PB3/PB10`, while current PCB2 remains `PA0/PA1/PB4` software Hall with `PB3=LIN1`; no hook, build, or hardware claim is opened. |
| Packet A Board Designer / Board Manager path review | `packet_a_board_designer_manager_path_review_2026-05-19.md`, `packet_a_workbench_asset_probe_2026-05-19.md`, local `STMCBD-UM.pdf`, `wb2mx.properties` | Local path clue / Packet A still blocked | Use a later GUI-only Board Designer / Board Manager capture only to prove a reviewable custom/user board artifact for the self-developed STDRIVE101 board. Built-in ST boards cannot be treated as board-match evidence, and this review does not open generated-project trust or build-only clearance. |
| Packet A Board Designer / Manager GUI-only checklist | `packet_a_board_designer_manager_gui_checklist_2026-05-19.md`, `packet_a_board_designer_manager_path_review_2026-05-19.md` | Checklist ready / Packet A still blocked | The user can later capture GUI-only screenshots under `packet_a_sources/2026-05-19_board_designer_manager_path/screenshots/`. The capture must stop before Generate, Motor Profiler, Motor Pilot, Flash, source generation, fake board saving, or any hardware action. |
| MY_FOC generated project | `source_packet_review_2026-05-19_005_my_foc_generated_project.md`, `packet_a_sources/2026-05-19_my_foc_generated_project/` | Generated project quarantined / Packet A not accepted | Useful clue only. The next acceptable update is not to build this source tree; it is to correct the Workbench project to FOC, restore required current-sense and fault choices, and make Hall/PWM match either changed pins or a documented software Hall route. |
| MY_FOC manual FOC edit rollback | `my_foc_foc_candidate_edit_2026-05-19.md`, `MY_FOC.codex_foc_candidate_2026-05-19.stwb6` | Failed manual edit / rolled back / Packet A still not accepted | Do not use the failed FOC candidate as a source. Reopen the restored `MY_FOC.stwb6` only to confirm the original project loads, then use Workbench GUI flow or a new complete FOC project for the next Packet A attempt. Stop before Generate, build, flash, Motor Profiler, Motor Pilot, or hardware action. |
| Packet A FOC route decision after MY_FOC rollback | `packet_a_foc_route_decision_2026-05-19.md`, `My_First_FOC.stwb6`, `MY_FOC.original_2026-05-19.stwb6`, and `MY_FOC.codex_foc_candidate_2026-05-19.stwb6` | Route narrowed / GUI-created FOC source required / Packet A still blocked | The next acceptable capture is a Workbench GUI-created or complete reviewable FOC source with self-developed/custom STDRIVE101 board path, current sensing, fault/break, Hall/PWM, and motor-entry fields visible. No generated-project trust changes until a dated Packet A source review accepts those fields. |
| Packet A Workbench FOC source capture | `workbench_foc_capture_success_2026-05-21.md`, `QIANSAI_G474_STDRIVE101_FOC_P2_2026-05-21.stwb6`, `MY-STDRIVE101_POWER_BOARD.foc_no_power_2026-05-21.json`, and `packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/` | Workbench FOC source captured / superseded by generated-source review for selected fields | The archived generated project has now been reviewed by `source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md`. The Workbench route uses `PA15/PB3/PB10` Hall while current PCB2 clues still record `PA0/PA1/PB4` and `PB3=LIN1`, so Hall readiness and powered work remain blocked. |
| PB3 / SWO | Saved NUCLEO `.ioc` shows SWO ownership; 2026-05-19 clarification says current PCB2 uses `PB3` as `LIN1`, not Hall | Blocked only for alternate Hall use | Do not use `PB3` as current PCB2 Hall. Any alternate Hall use of `PB3` would still need SWO release/isolation and a new accepted route. |
| STM32 signal contract | `stm32_side_signal_contract_2026-05-15.md` | Planning contract | Update only after Packet A/B/C or PB3/SWO evidence changes. |
| Future build-only gate | `future_build_only_gate_2026-05-15.md`, `source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md`, and `build_only_result_2026-05-27_qiansai_g474_stdrive101_foc_p2_debug.md` | Source prerequisite satisfied / no-power Debug build-only pass recorded | Build-only has passed on the local bundled toolchain. This remains no-power compile evidence only and does not authorize flash, Run / Debug, Gate PWM, Motor Profiler, Hall closed-loop, motor, or power-stage work. |

## Claim Matrix

Allowed current claims:

- The repo has a P2 no-power evidence governance layer.
- The repo has a saved NUCLEO CubeMX `.ioc` draft and GUI fallback evidence.
- The repo has local STDRIVE101 official-source review material.
- The repo has a `Partial clue` schematic candidate for Packet B/C review.
- The repo has written signal-contract and future build-only rules.
- The repo has a local MCSDK 6 `.stwb6` legacy learning file reviewed as
  `Partial clue`.
- The repo has a 2026-05-16 custom NUCLEO + STDRIVE101 Packet A capture
  package reviewed as `Partial clue / Preparation only`.
- The repo has a 2026-05-17 supplier motor source and hardware teammate pin
  table reviewed as `Partial clue`; local MCSDK assets confirm the compared
  key G431/G474 MCU pin functions, but not board routing.
- The repo has a 2026-05-18 workflow-only Packet A capture task package that
  fixes the future `.stwb6` path, screenshot names, stop conditions, and field
  acceptance matrix.
- The repo has a 2026-05-18 motor wiring definition image reviewed as
  `Partial clue`; it records candidate U/V/W and Hall wire colors, but not
  physical harness verification, Hall power behavior, phase/Hall alignment, or
  `J_HALL` numbering.
- The repo has a 2026-05-19 Workbench capture attempt reviewed as
  `Partial clue / stopped`; Workbench 6.4.2 launches and
  `NUCLEO-G474RE` / `STM32G474RETx` control-board context is visible, but no
  accepted self-made STDRIVE101 power-stage context or selected-field
  screenshot was captured.
- The repo has a user-confirmed 2026-05-19 EDA Pro schematic source for the
  self-developed STDRIVE101 driver board. It supports board-side schematic
  clues for `U1=STDRIVE101`, `CN3` 15-pin control connector, `J_HALL`,
  `J_MOTOR`, MOSFETs, shunts, `NFAULT`, `REG12`, `SCREF`, bootstrap, and
  output nets. It does not contain PCB layout data.
- The repo has a 2026-05-19 Gerber PCB2 manufacturing package with
  `FlyingProbeTesting.json`. It supports board-side pad-net clues for `CN3`,
  `U1=STDRIVE101`, PWM input paths, shunt/current-sense nets, `J_HALL`,
  `J_MOTOR`, `NFAULT`, `REG12`, `SCREF`, bootstrap, and output nets. It does
  not prove NUCLEO `CN8` or STM32 endpoint mapping.
- The repo has a 2026-05-19 hardware supplement handoff that defines the next
  hardware teammate evidence request after the `.epro` and Gerber reviews.
  It is a request/governance artifact and does not upgrade any hardware
  readiness claim.
- The repo has a 2026-05-19 minimal hardware-teammate request that can be sent
  first. It asks for exact Gerber PCB2 revision confirmation,
  `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping, and marked `CN3` / `J_HALL`
  pin-1 evidence.
- The repo has a 2026-05-19 Workbench asset probe showing that Board Designer
  and Board Manager executables are installed and referenced by Workbench
  config. This is only a local path clue, not a custom-board Packet A source.
- The repo has a 2026-05-19 current PCB2 mapping / pin-1 / protection packet
  reviewed as `Partial clue / accepted current PCB2 mapping source; Hall/PWM
  conflicts clarified`. It answers many previously open items and clarifies
  current Hall routing as `IA/IB/IC -> PA0/PA1/PB4`.
- The repo has a 2026-05-19 current PCB2 Hall/PWM no-power strategy review.
  It opens the no-PCB-change path first, but it records only a feasibility
  review direction: current PCB2 PWM/Hall routing is not accepted Packet A
  configuration evidence and software Hall is not hardware validation.
- The repo has a 2026-05-19 current PCB2 Packet A / firmware feasibility
  review. It concludes that the no-PCB-change route remains feasibility only:
  Packet A is not accepted, generated-project trust is not allowed, and
  build-only clearance remains closed.
- The repo has a 2026-05-19 software Hall adapter design review. It defines
  no-power GPIO/EXTI sampling, edge timestamping, valid-state filtering,
  minimal ISR responsibility, MCSDK integration boundaries, and
  `hardware-rework planning` fallback conditions for `PA0/PA1/PB4`.
- The repo has a 2026-05-21 current PCB2 software Hall route confirmation:
  `P14/P15=3V3/GND`, `PB3=LIN1`, and
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`. This confirms the no-PCB-change
  software Hall direction only; it does not add firmware implementation,
  continuity proof, MCSDK Hall integration, or powered readiness.
- The repo has a 2026-05-22 DMM continuity / short-check request. It asks for
  the filled `Signal | STM32 pin | DMM result | Beep? | Note / photo ID`
  table before software Hall adapter implementation. It is not a measurement
  result.
- The repo has a 2026-05-19 Packet A Board Designer / Board Manager path
  review. It confirms local Workbench external-tool entries, installed Board
  Designer / Board Manager executables, and local Board Designer manual clues
  for custom board creation/import and Board Aggregation for the
  self-developed STDRIVE101 board path, but Packet A still blocked.
- The repo has a 2026-05-19 Packet A Board Designer / Manager GUI-only
  checklist. It tells the user which screenshots to capture, where to save
  them, and when to stop, while keeping Packet A still blocked and no
  generated-project trust.
- The repo has a 2026-05-19 MY_FOC generated project source review. It records
  a real Workbench 6.4.2 generated project as a clue, but quarantines it
  because it is `SIX_STEP`, not FOC. The user's statement that pins can be
  changed is recorded as an editable future route, not as Packet A acceptance.
- The repo has a 2026-05-19 MY_FOC manual FOC edit rollback record. It proves
  a one-field `.stwb6` algorithm edit made Workbench unable to load the file,
  and that Codex restored the external source from backup. It does not prove
  generated source, build readiness, or hardware readiness.
- The repo has a 2026-05-19 Packet A FOC route decision after the `MY_FOC`
  rollback. It compares legacy FOC, restored six-step, and failed manual-edit
  sources, and narrows the next valid Packet A path to a Workbench GUI-created
  or complete reviewable FOC source.
- The repo has a 2026-05-21 Packet A generated-source side-effect review. It
  accepts selected Workbench fields as no-power configuration evidence and
  opens the source side of the build-only gate. The 2026-05-27 build-only
  result records a local Debug build pass through the bundled STM32Cube Ninja
  and GNU Arm GCC paths, but this adds compile evidence only.
- The repo has a 2026-05-20 Packet C STDRIVE101 protection detail review. It
  narrows the protection sub-items and explicitly marks the old `55A` VDS
  threshold claim as not accepted.

Forbidden current claims:

- MCSDK MotorControl configuration is complete for the competition board.
- A software Hall adapter has been implemented or accepted by MCSDK.
- A DMM continuity / short-check table has been completed.
- `PB3` is a current PCB2 Hall input.
- MCSDK standard TIM2 Hall `PA15/PB3/PB10` is the current PCB2 Hall route.
- A generated motor-control project has a successful build record or is ready
  for flash/hardware use.
- CN8 routing is proven.
- NUCLEO-to-driver-board endpoint routing is proven.
- STDRIVE101 protection paths are proven on this board.
- `PB3` is ready for Hall B.
- `J_HALL` numbering is confirmed.
- Phase/Hall wire-color mapping has been verified on the physical motor.
- The vendor motor parameters are measured project data.
- Workbench captured or accepted the self-made STDRIVE101 driver board.
- Board Designer / Board Manager has created, imported, saved, or accepted the
  project self-developed STDRIVE101 board.
- The GUI-only checklist proves a custom/user board path or accepts Packet A.
- The user-created `MY_FOC` generated project is trusted, buildable for this
  project, FOC-complete, or accepted as Packet A.
- The failed manual `MY_FOC.stwb6` FOC candidate can be used as a valid source,
  regenerated source, or built/flashed without another Packet A review.
- Built-in ST power-board entries such as `EVALSTDRIVE101` or `STEVAL-LVLP01`
  are board-match evidence for the self-developed driver board.
- The old `V_DSth = 0.249V` / `I_trip ~= 55A` note is an accepted board
  threshold or current limit.
- cannot claim Gate PWM, Motor Profiler, Hall, motor, power-stage, or sensorless behavior is validated.

## Promotion Rules

Build-only generated-project work status:

1. Packet A must be accepted through `source_packet_review_template_2026-05-14.md`.
   Current status: done for selected fields by
   `source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md`.
2. `evidence_packet_2026-05-14.md` must name the exact accepted Packet A fields.
3. `workflow/evidence_register.md` must state that the result is build-only
   configuration / compile evidence.
4. Packet B/C blockers and alternate-use PB3/SWO blockers must be copied
   forward if still unresolved. Current PCB2 `PB3=LIN1` is fixed and must not
   be treated as a current Hall candidate.
5. Bundled `ninja` and `arm-none-eabi-gcc` paths were available through the
   STM32Cube build cache, and the no-power Debug build-only command returned
   exit code `0`.
6. `python -m unittest discover -s tests` must pass after the updates.

Before moving from P2 to any powered or motor stage:

1. Packet A, Packet B, Packet C, and PB3/SWO status must be accepted where used.
2. No-power continuity / short checks must be recorded in a later hardware-stage artifact.
3. Current-limited bring-up settings, measurement points, stop conditions, and
   rollback image must be written before any powered command.
4. The phase gate must explicitly allow the hardware action.

## Next Smallest Actions

1. User fills the DMM continuity / short-check table from
   `dmm_continuity_short_check_request_2026-05-22.md`.
   Do this before any software Hall adapter implementation.
2. Treat the accepted Workbench standard TIM2 Hall route as generated
   configuration evidence only. The current PCB2 route is now fixed for
   no-power design as `PA0/PA1/PB4` software Hall with `PB3=LIN1`; do not
   reopen `PB3` as a current Hall option unless a separate hardware-rework
   task is opened.
3. Re-probe or configure the CLI build tool paths for `ninja` and
   `arm-none-eabi-gcc` only when a no-power build record is the next objective.
   This is not the current real-world hardware-progress blocker.
4. Use `packet_a_board_designer_manager_gui_checklist_2026-05-19.md`,
   `packet_a_board_designer_manager_path_review_2026-05-19.md`, and
   `packet_a_workbench_asset_probe_2026-05-19.md` to plan the next no-power
   Packet A GUI/documentation check around Board Designer / Board Manager. If
   that path supports a custom/user board, then use
   `packet_a_capture_task_2026-05-18.md` and the 2026-05-16 custom NUCLEO +
   STDRIVE101 capture package to create the new `.stwb6` and selected-field
   screenshots. If Workbench requires a motor entry, use
   `57BLF01_VENDOR_CANDIDATE` only as a supplier-clue label. If the path is
   not reviewable, record Packet A as blocked and choose surrogate build-only
   planning without generated-project trust or separate hardware-rework
   planning.
   Stable fallback phrase: surrogate build-only planning without generated-project trust.
5. Use `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md` to drive the
   current no-PCB-change boundary, and use
   `software_hall_adapter_design_review_2026-05-19.md` as the software Hall
   boundary record. The software path is now the priority route for later
   adapter design, but remains no-power design review only; it does not
   authorize generated-project trust or powered work.
   Stable prior decision phrase: deeper software Hall adapter design review.
   Stable phrasing: software Hall adapter design review or hardware-rework planning task.
6. Finish Packet C protection review for `CP`, `STBY`, `SCREF` threshold,
   `NFAULT` break-input handling, and later no-power continuity checks.
   Current Packet C detail status: `Packet C detail narrowed / protection
   proof still partial clue / P3 still blocked`; the old `55A` VDS claim is not
   accepted.
7. Keep this snapshot current after any evidence upgrade.

## Current Decision

P2 can continue no-power source intake, DMM evidence collection,
interface-contract maintenance, and delivery cleanup. P2 can attempt a
no-power build only after CLI `ninja` and `arm-none-eabi-gcc` are available,
but the next real-world hardware-progress gate is the DMM table.
P2 still cannot flash, power, connect, or run a motor-control project.
