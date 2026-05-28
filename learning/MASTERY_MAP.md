# MASTERY_MAP

Last updated: 2026-05-27

This file summarizes what has evidence, what is only partially repaired, and what must not be claimed yet. It complements `weak_points.md`: weak points show repair targets; this map prevents repeated low-value review of already demonstrated basics.

## Evidence Scale Reminder

- L1: recognized after explanation.
- L2: can restate in own words.
- L3: can solve a guided example.
- L4: can solve a similar problem independently.
- L5: can apply it in firmware, hardware, or debugging work.
- L6: can teach it back and catch edge cases.

## Demonstrated Strengths

| Area | Evidence | Current Level | Teaching Decision |
| --- | --- | --- | --- |
| NUCLEO baseline serial observation | VOFA+/COM5 showed `mode` and `mode_name` moving through `IDLE`, `ARMED`, `RUN_SIM` | L5 for observed firmware output | Do not keep drilling simple mode-number mapping unless logs become confusing again. |
| Basic state-machine idea | User explained current state + event -> next state and one event should cause one transition | L2 | Use as foundation for command guards, not as a fresh beginner topic. |
| ARM command risk direction | User recognized ARM moves toward a run-like state and should be guarded | L2 | Review exact allowed state only when tied to command table. |
| PING/MODE? read-only idea | User can classify `PING` and `MODE?` as read-only after explanation | L1-L2 | Keep one compact check, then move to side-effect table. |
| `strcmp(...) == 0` command matching | User stated they understand that `strcmp` returning 0 means strings match | L2 | Review only inside actual branch-reading practice. |
| STOP command side effects | User independently predicted both `ARMED + STOP` and `IDLE + STOP`, including unconditional `target_rpm=0` and conditional `mode_change_count++` | L4 | Do not drill the same STOP table again; use it as the example for branch side-effect reading. |
| `Size` count/index repair | User independently answered `Size = 10` -> process indices `0..9` with loop condition `i < Size`, and later repaired a callback wording slip by distinguishing changing index `i` from batch count `Size` | L4 | Do not repeat standalone count/index drills; use this only inside full callback-flow reading. |
| SET_RPM guard behavior | User classified parse error, range error, bad state, and allowed ARMED target update | L2; COM5 path validated by Codex at L5 for firmware behavior | Treat as communication-layer learning, not motor-control validation. |
| DMA + IDLE callback structure | User described DMA batch receive, UART IDLE batch-ready meaning, loop `i < Size` over `rx_buf[0..Size-1]`, `AppFeedRxByte(...)` parser feeding, and receive restart | L4 for current concept layer | Move from concept drills to implementation/verification only when the repo task calls for real callback work. |
| P2 MCSDK no-power boundary | User explained that Motor Profiler needs real motor and power chain, and that generated MCSDK projects without hardware prove toolchain/config familiarity but not motor parameters or power-chain behavior | L3 | Continue with P2 artifact planning before any MCSDK implementation or hardware action. |
| P2 no-power artifact planning | User listed pin map, motor-parameter table/template, no-power configuration file, risk/no-go checklist, and Motor Profiler plan; user separated real measured motor parameters as later hardware evidence | L3-L4 | Begin creating the P2 artifact set; keep measured motor parameters explicitly out of P2. |
| P2 MCSDK config evidence boundary | User explained that `.stmcx` proves planned/saved configuration choices such as MCU, PWM pins, current sensing, Hall/sensorless mode, and protection input; user also stated that a compiled MCSDK project still lacks nFAULT, PWM, sensing, Hall, power-board, current-limit, and rollback evidence | L3-L4 | Next review should use a real Workbench/CubeMX screenshot or `.stmcx` and ask which fields are planning evidence versus hardware-stage proof. |
| STDRIVE101 source ingestion | Official STDRIVE101 datasheet DS13472 Rev 2 is now in the repo-local ST mirror, hash-recorded, text-extracted, and digested for no-power review | L5 for source-management workflow | Use the local PDF/text/digest for gate-driver protection review; do not treat it as hardware validation. |
| P2 NUCLEO CubeMX hands-on pin evidence | User used the NUCLEO-G474RE Board Selector flow, identified SWD, VCP, SWO, `PB12/TIM1_BKIN`, and `PB14/TIM1_CH2N`, saved a readable `.ioc` draft, and Codex captured that `.ioc` reopened in CubeMX `Pinout & Configuration` | L4 for hands-on configuration evidence classification; L5 for saved repo artifact and GUI fallback evidence | Move next to MCSDK/Workbench MotorControl evidence, CN8/EDA/netlist, and STDRIVE101 protection-path evidence; do not repeat basic board-selector navigation. |
| Software Hall state-machine table classification | User correctly classified `100 -> 110`, `100 -> 101`, `100 -> 011`, `000`, and `111` after earlier guided Hall exercises | L4 for table-level no-power algorithm classification | Move from concept tables to adapter processing-order review and pseudocode boundary. Do not treat this as firmware, GPIO/EXTI, MCSDK Hall, Gate PWM, power-board, motor, or Hall closed-loop evidence. |

## Active Transfer Gaps

| Gap | Why It Still Matters | Next Proof Needed |
| --- | --- | --- |
| Software Hall adapter processing order | The user can classify individual Hall transition rows but could not restate why the adapter order is raw read, illegal-state check, first-valid check, repeated-state check, bounce/timing check, adjacent direction check, then abnormal-jump count. This order is needed before writing safe GPIO/EXTI software Hall code. | One-sentence teach-back from `software_hall_adapter_processing_order_card_2026-05-27.md`, then a no-power pseudocode walkthrough that keeps ISR work minimal and does not claim firmware or hardware readiness. |
| Branch condition vs side effect in future code | Current UART command and callback examples are repaired, but this distinction must be rechecked when real HAL callback or new commands are implemented | During implementation/review, mark match condition, guard, assignment side effect, counter side effect, response line, and callback-only responsibilities. |
| P2 artifact implementation | First artifact file exists and now contains current no-power tool/status evidence, baseline `.ioc` readback, pin/config draft, ST source cross-check, local ST PDF mirror note, pin-function conflict resolution, expanded future Motor Profiler stop/rollback plan, dedicated no-power draft directory, proven CubeMX launch path, a saved NUCLEO-G474RE CubeMX `.ioc` draft, CubeMX `Pinout & Configuration` fallback screenshots, and a Workbench entry probe showing MotorControl package data exists. `.stmcx`, MCSDK MotorControl config screenshot, and board-routing proof are still missing | Add MCSDK/Workbench `.stmcx` or MotorControl config screenshot, confirm `PB12/TIM1_BKIN` nFAULT and `PB14/TIM1_CH2N` against CN8/EDA/netlist, and keep all hardware actions blocked. |

## Do Not Claim Yet

These are not mastered or validated yet, regardless of calendar schedule:

- MCSDK motor-control project generation.
- Motor Profiler parameter capture.
- Hall closed-loop motor run.
- Software Hall adapter firmware implementation.
- Power-board bring-up, 24V, Gate waveform, nFAULT checks, current sampling checks.
- CORDIC/FMAC performance gain.
- SMO/PLL sensorless startup.
- ESP32-C3 real gateway implementation.

## Promotion Rules

- Move an item from active gap to demonstrated strength only after L4 or above evidence.
- Do not close safety-critical items from a single verbal answer.
- Board logs, build output, screenshots, or experiment records can raise evidence level, but only for the exact layer they validate.
- `SET_RPM` validation proves command parsing and guard behavior only; it does not prove real motor speed control.
