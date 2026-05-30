# Session Notes

Append one entry after teaching, Q&A, homework review, debugging help, or experiment review when the turn reveals learning progress or weak points.

## 2026-05-30 Hall state-machine ChatGPT follow-up

- Summary: User pasted back the ChatGPT-taught five-question Hall software state-machine review. The answer correctly classified `110 -> 010` as forward adjacent, `010 -> 110` as reverse adjacent, `111` as illegal, computed `60 / 7 = 8.57 deg` mechanical for a 7-pole-pair motor, and explained why `PB3=LIN1` cannot be reused as Hall.
- Evidence level: L4 for no-power Hall transition classification and PB3 route constraint; L2-L3 for electrical-to-mechanical angle conversion.
- Confidence: medium-high for the corrected concept that reverse adjacent transitions are not abnormal.
- Weak point update: reverse adjacent vs abnormal jump is repaired. The full software Hall adapter processing order remains the next check.
- Next review: Ask for one-sentence teach-back of raw read -> illegal-state check -> first-valid baseline -> repeat check -> bounce/timing check -> forward/reverse adjacent check -> abnormal-jump count.
- Source:
  `learning/review_items/2026-05-30_hall_state_machine_chatgpt_followup.md`

## 2026-05-27 Software Hall adapter processing-order repair

- Summary: User could correctly classify individual Hall transition rows, but
  answered `我不知道啊` when asked to restate the adapter processing order.
  Codex added a Chinese-first processing-order card that explains raw read,
  illegal-state check, first-valid handling, repeat handling, bounce/timing
  check, adjacent direction check, and abnormal-jump count.
- Evidence level: L1 repair artifact for processing-order understanding; not
  a new mastery upgrade.
- Confidence: medium for identifying the weak point; low for mastery until the
  user gives a one-sentence teach-back.
- Weak point observed: software Hall adapter processing order is not yet
  independently explainable.
- Next review: Ask the user to say the one-sentence rule from
  `software_hall_adapter_processing_order_card_2026-05-27.md`.
- Source:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_processing_order_card_2026-05-27.md`

## 2026-05-27 Hall state-machine follow-up review

- Summary: User correctly classified `100 -> 110` as forward adjacent, `100 -> 101` as reverse adjacent, `100 -> 011` as abnormal jump, and `000` / `111` as illegal Hall states.
- Evidence level: L4 for table-level no-power Hall state-machine classification.
- Confidence: medium-high for concept transfer.
- Weak point observed: None in the table. Still must separate table mastery from firmware/hardware readiness.
- Next review: Ask user to restate the adapter processing order and why DMM plus GPIO/EXTI boundary review still block firmware work.
- Source: `learning/session_notes/2026-05-27_hall_state_machine_review_followup.md`

## 2026-05-09 Learning Loop Initialized

- Topic: Project learning workflow.
- What happened: Created persistent learning notes, weak-point tracking, review queue, and Skill rules.
- Evidence: Workflow setup, not a knowledge mastery event.
- Weak points observed: None yet.
- Next review: Use this system after the next real learning interaction.
## 2026-05-10 16:36 NUCLEO nonblocking tick scheduler

- Summary: Ran the NUCLEO-G474RE baseline with HAL_GetTick-based nonblocking scheduling. User confirmed that changing LED interval to 250U makes LD2 toggle every 250 ms, and changing report interval to 1000U makes VOFA+ print once per second.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Earlier tendency to treat run success as mastery; reinforce concept check before moving on.
- Next review: Explain why LED full on-off cycle is twice the toggle interval, then add a simple status counter or button event using the same scheduler pattern.
## 2026-05-10 16:54 NUCLEO multi-rate task counter

- Summary: User ran the multi-rate task counter on NUCLEO-G474RE and correctly explained that tick_ms=4000 gives led_toggle=40 at a 100 ms LED task period. User also corrected the 200 ms LED / 1000 ms report case to 5 toggles per report.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Non-integer task-rate ratios need one more reinforcement: average rate can be fractional, but integer counters change in discrete +2/+3 patterns.
- Next review: Add a button event counter with the same nonblocking scheduler pattern; ask user to predict counter changes before running.
## 2026-05-10 17:12 NUCLEO B1 button event counter

- Summary: User ran the NUCLEO-G474RE B1 button event counter. VOFA+ output showed btn_press increasing from 1 to 6 while periodic tick, LED toggle, and report counters continued running.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Need confirm understanding of edge detection: btn is current sampled level, btn_press is accumulated rising-edge event count; if only checking button_state==PRESSED, a held button would be counted repeatedly.
- Next review: Ask user to explain why button_last_state is needed and why btn can be 0 while btn_press has already increased.
## 2026-05-10 17:27 NUCLEO button edge detection and debounce

- Summary: User validated B1 button event counting with 1000 ms and 50 ms debounce thresholds. User explained that button_last_state prevents repeated counting while held, button_last_event_tick/50U controls valid event spacing, and btn_press is cumulative effective press count.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Clarify distinction between btn current sampled level and btn_press historical event count when interpreting logs.
- Next review: Introduce a tiny finite state machine using the same button event: press B1 to cycle mode 0/1/2 and report mode over UART.
## 2026-05-10 17:38 NUCLEO minimal app state machine

- Summary: User ran the B1-driven mode state machine on NUCLEO-G474RE. VOFA+ showed mode cycling 0->1->2->0 with mode_chg tracking effective button events.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Need confirm why state transitions must be event-gated and why motor-control FAULT states should not jump directly back to RUN.
- Next review: Ask user to explain current state + event = next state, and why safety states require explicit acknowledgement before returning to run-like states.
## 2026-05-10 17:43 NUCLEO state machine concept check

- Summary: User explained that mode_chg records state transition count, mode wraps from 2 to 0 because valid modes are 0/1/2 only, and a motor FAULT state must verify fault disappearance, clear the fault, and re-enter a safe state before RUN.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Next reinforce explicit transition tables instead of ad hoc app_mode++ logic before mapping to IDLE/RUN/FAULT.
- Next review: Teach a named-state transition table for IDLE/ARMED/RUN_SIM and make B1 cycle through explicit cases.
## 2026-05-10 19:29 NUCLEO explicit state transition table

- Summary: User updated the state-machine exercise and observed mode transitions. User explained that default returns to IDLE because it is the safest state, and FAULT must not directly return to run-like states because the system is unsafe until fault conditions are cleared.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Next reinforce named states and source layout: move mode defines out of main block and avoid macro definitions inside executable code regions.
- Next review: Refactor APP_MODE_* definitions into USER CODE BEGIN PD or an enum, then discuss why embedded projects keep state definitions near top-level declarations.
## 2026-05-11 13:47 NUCLEO app mode labels

- Summary: User correctly answered that mode=1 means the ARMED/prepared state after plain-language explanation of mode numbers and labels.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Still needs reinforcement on separating state labels from transition logic before introducing enum formally.
- Next review: Ask user to map mode=2 and then explain why a label table should sit above the main loop.
## 2026-05-11 13:47 NUCLEO mode number mapping

- Summary: User correctly answered that mode=2 means RUN_SIM/simulated running state.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Next reinforce why state labels are defined once near the top instead of inside the main loop.
- Next review: Use a classroom name-list analogy to explain why state labels belong in the enum/type area above main().
## 2026-05-11 13:49 NUCLEO enum placement intuition

- Summary: User explained that putting the state label list inside while(1) is troublesome because the loop repeats. This shows an initial intuition for keeping state definitions out of repeated execution logic.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Need refine the reason: state labels are a fixed dictionary for humans and should not visually mix with repeatedly executed behavior code.
- Next review: Ask user to identify which part is the fixed state dictionary and which part is the repeated transition logic in the current main.c.
## 2026-05-11 13:50 NUCLEO switch state transition

- Summary: User correctly answered that pressing B1 in APP_MODE_ARMED transitions to APP_MODE_RUN_SIM.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Next reinforce the full transition table and the role of default returning to IDLE as a safe fallback.
- Next review: Ask user to map the remaining transitions and explain why an unknown state should return to IDLE.
## 2026-05-11 13:52 NUCLEO full state cycle

- Summary: User correctly answered that pressing B1 in APP_MODE_RUN_SIM returns to IDLE/idle state.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Next reinforce default fallback: unknown or broken state should return to IDLE because it is the safest state.
- Next review: Ask user why an unknown state should not jump directly into RUN_SIM, then connect that to motor-control FAULT safety.
## 2026-05-11 13:53 NUCLEO default safe fallback

- Summary: User correctly answered that an invalid app_mode value such as 99 falls back to IDLE/idle state through the switch default case.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Continue reinforcing the safety idea that unknown state should return to a safe state before any run-like behavior, especially before motor-control FAULT/RUN mapping.
- Next review: Have user restate the full state machine as current state, button event, next state, then connect IDLE fallback to future FAULT handling.
## 2026-05-11 13:55 NUCLEO state machine formula teach-back

- Summary: User correctly restated that current state plus an action/event can become the next state.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Next reinforce that without a valid event, the state should stay unchanged; transitions must be event-gated.
- Next review: Ask what happens to app_mode when no B1 press event occurs, then map that to the if-condition around the switch.
## 2026-05-11 13:57 NUCLEO event-gated transition

- Summary: User correctly answered that if the system is in ARMED/prepared state and no B1 press event occurs, it should remain in ARMED instead of moving to RUN_SIM.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Next reinforce event gating with the actual if-condition around the switch: only a release-to-press edge and debounce interval allow state transition.
- Next review: Show the button edge if-condition and ask the user which three conditions must be true before switch(app_mode) runs.
## 2026-05-11 14:00 NUCLEO debounce as state-machine gate

- Summary: User remembered that the button edge/debounce conditions prevent one physical press from being counted multiple times.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Next connect debounce failure to state-machine symptoms: one physical press can trigger multiple transitions and make mode appear to skip or return unexpectedly.
- Next review: Ask user to predict the final mode if one physical press is mistakenly counted as three valid press events starting from IDLE.
## 2026-05-11 14:01 NUCLEO debounce multiple transition prediction

- Summary: User correctly predicted that starting from IDLE, if one physical B1 press is mistakenly counted as two valid press events, the mode ends at RUN_SIM.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Next reinforce that debounce is not only for button counts; it also prevents accidental multi-step state transitions.
- Next review: Ask user to predict the final state for three mistaken events from IDLE, then connect this to why motor start logic needs strong event gating.
## 2026-05-11 14:03 NUCLEO debounce three-transition prediction

- Summary: User correctly predicted that starting from IDLE, if one physical B1 press is mistakenly counted as three valid events, the mode cycles back to IDLE.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Next connect accidental multi-transition behavior to why motor-control start logic must require explicit checks and cannot rely on raw button presses alone.
- Next review: Ask user why a motor-control system should not let one noisy button press move through IDLE, ARMED, and RUN-like states in one burst.
## 2026-05-11 14:05 NUCLEO one-event-one-transition rule

- Summary: User repeated the core rule that a reliable state machine must ensure one real action triggers only one state transition.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Needs one more safety connection: in motor control, accidental multi-step transitions can skip checks before RUN.
- Next review: Ask user to explain what checks could be skipped if a noisy start button jumps directly from IDLE to RUN.
## 2026-05-11 14:06 NUCLEO ARMED as pre-run check state

- Summary: User correctly answered that ARMED exists between IDLE and RUN because the motor must be checked before startup.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Next reinforce what belongs in ARMED checks before mapping the LED demo states to real motor-control states.
- Next review: Ask user to name two checks that should happen before a motor enters RUN, then map them to voltage/current/nFAULT/PWM readiness.
## 2026-05-11 14:11 NUCLEO UART mode name logging

- Summary: Added AppModeName(app_mode) so UART reports both numeric mode and readable mode_name, making the state-machine log easier to inspect. No learner evidence yet; next evidence should come from running the firmware and reading VOFA+/serial output.
- Evidence level: L0
- Confidence: low
- Weak point observed: None recorded.
- Next review: Flash/run the NUCLEO baseline and check that mode and mode_name change together when B1 is pressed.
## 2026-05-11 14:16 NUCLEO mode-name serial validation

- Summary: User provided a VOFA+ screenshot showing COM5 serial output from the NUCLEO baseline firmware: mode=1/mode_name=ARMED, mode=2/mode_name=RUN_SIM, and mode=0/mode_name=IDLE, with btn_press and mode_chg increasing together.
- Evidence level: L5
- Confidence: medium
- Weak point observed: Continue from readable logs into UART receive/DMA+IDLE; avoid repeating already-mastered simple mode-number mapping questions.
- Next review: Use the validated serial log to introduce UART receive: first receive one simple command line such as MODE? or PING without touching power-board or motor hardware.
## 2026-05-11 14:28 NUCLEO UART query command semantics

- Summary: User correctly judged that MODE? should only query current state, but was unsure why read-only serial queries must not change app_mode.
- Evidence level: L1
- Confidence: medium
- Weak point observed: User can classify MODE? as a query but needs reinforcement on separating read-only queries from state-changing commands to avoid accidental mode transitions.
- Next review: Classify PING, MODE?, ARM, STOP, and FAULT_CLEAR as read-only queries or state-changing commands, then explain which ones are allowed to change app_mode.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-11 14:31 NUCLEO ARM vs STOP command safety

- Summary: User correctly answered that ARM is more dangerous than STOP because STOP returns toward a safe state, while ARM moves the system closer to running.
- Evidence level: L1
- Confidence: medium
- Weak point observed: None recorded.
- Next review: Ask user to name two guard conditions that should be checked before accepting ARM, then map them to future voltage/current/nFAULT/PWM readiness checks.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-11 14:33 NUCLEO ARM command state guard

- Summary: User correctly answered that ARM should not be accepted while already in RUN_SIM, recognizing that RUN_SIM is already close to a run-like state.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Need refine command-guard wording: ARM is only valid from IDLE; from RUN_SIM it should be rejected or ignored because it is an out-of-sequence command, not because it is another preparation step.
- Next review: Ask user to write the accepted transition for IDLE + ARM and the rejected transition for RUN_SIM + ARM.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-11 14:36 NUCLEO STOP command idempotence

- Summary: User answered that IDLE + STOP should change state because STOP returns to safety and should generally be allowed.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Need distinguish accepting a safe command from changing state: STOP can be accepted in IDLE, but because IDLE is already safe, the state should remain IDLE.
- Next review: Ask user to classify IDLE + STOP as accepted with no state change, then explain why repeated STOP commands must not move the system elsewhere.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-11 14:36 NUCLEO STOP from run-like state

- Summary: User answered that RUN_SIM + STOP should go to safety, correctly recognizing STOP as a command toward the safe state.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Need map safety wording to explicit state names: in this baseline, the safe state is IDLE, so RUN_SIM + STOP should become IDLE.
- Next review: Ask user to compare IDLE + STOP and RUN_SIM + STOP, and explain why both are accepted but only RUN_SIM + STOP changes app_mode.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-11 14:38 NUCLEO STOP from ARMED state

- Summary: User answered that ARMED + STOP should return to safety, correctly recognizing STOP as a command toward the safe state.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Need map safety wording to explicit baseline state names: in this app, safety means IDLE, so ARMED + STOP should become IDLE.
- Next review: Ask user to complete the three STOP transitions using explicit state names instead of the word safety.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-11 14:42 NUCLEO UART command side-effect classification

- Summary: User correctly classified five serial command cases by whether they change state: MODE? and PING are read-only; IDLE + ARM changes state; ARMED + STOP changes state.
- Evidence level: L2
- Confidence: medium
- Weak point observed: None recorded.
- Next review: Ask user to write next state and response category for IDLE + ARM, RUN_SIM + ARM, IDLE + STOP, and RUN_SIM + MODE?.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-11 14:46 NUCLEO UART command table confidence

- Summary: User said the second layer command table is now understood and noted that next-state/response classification can be looked up from the table.
- Evidence level: L2
- Confidence: medium
- Weak point observed: None recorded.
- Next review: Move from table lookup to implementation structure: design a command handler that separates parsing, read-only queries, guarded transitions, and response text.
- Source: User self-report in Codex chat on 2026-05-11
## 2026-05-11 14:49 NUCLEO UART polling command handler

- Summary: Implemented a minimal polling UART command handler in the NUCLEO baseline firmware. The code accepts newline-terminated PING, MODE?, ARM, and STOP commands; read-only commands do not change app_mode; ARM and STOP use guarded state transitions.
- Evidence level: L0
- Confidence: medium
- Weak point observed: None recorded.
- Next review: Flash the rebuilt firmware, send PING, MODE?, ARM, STOP over COM5, and capture a serial log proving command responses and mode changes match the command table.
- Source: Code change and successful CMake build on 2026-05-11
## 2026-05-11 14:57 NUCLEO MODE query code reading

- Summary: User answered line 3 and line 5 when asked which lines judge the MODE? command and reply current state, showing partial recognition of the response expression but missing that strcmp(...) == 0 is the command-name test.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Need reinforce C code reading: strcmp(cmd, MODE?) == 0 performs command matching, while printf plus its arguments produce the status response.
- Next review: Ask user to identify what strcmp returns when cmd equals MODE?, and why == 0 means matched.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-11 15:49 NUCLEO strcmp command matching

- Summary: User asked how the code judges command names; explained that C strings are compared by strcmp content comparison, and strcmp(...) == 0 means the two strings are equal. User replied that they now know it.
- Evidence level: L2
- Confidence: medium
- Weak point observed: None recorded.
- Next review: Apply strcmp understanding to the PING and ARM branches: identify command matching, output, and state-change lines.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-11 15:51 NUCLEO command matching versus side effect

- Summary: User identified the strcmp PING condition as proof that PING does not change state. Corrected that strcmp only matches the command; the absence of *app_mode = ... in the branch proves there is no state change.
- Evidence level: L1
- Confidence: medium
- Weak point observed: Need distinguish condition checks from side effects: if/strcmp decides which branch runs, but assignments such as *app_mode = ... are what change state.
- Next review: Ask user to identify the line that changes state in the ARM branch and the line that only prints output in the PING branch.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-11 15:52 NUCLEO PING branch output and no side effect

- Summary: User correctly identified printf(PONG) as the output line and confirmed there is no app_mode-changing code in the PING branch.
- Evidence level: L2
- Confidence: medium
- Weak point observed: None recorded.
- Next review: Move to the ARM branch and identify separately the command match condition, state guard, state assignment, counter update, and response output.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-11 15:54 NUCLEO ARM branch state assignment

- Summary: User correctly identified *app_mode = APP_MODE_ARMED; as the line that actually changes state in the ARM branch.
- Evidence level: L2
- Confidence: medium
- Weak point observed: None recorded.
- Next review: Explain why the APP_MODE_IDLE guard must come before that assignment, then ask what would go wrong if ARM always assigned ARMED.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-11 15:57 NUCLEO ARM guard prevents invalid transition

- Summary: User correctly answered that without the APP_MODE_IDLE guard, RUN_SIM + ARM would force app_mode back to ARMED, bypassing the intended command table.
- Evidence level: L2
- Confidence: medium
- Weak point observed: None recorded.
- Next review: Move to STOP branch and explain accepted unchanged versus accepted changed behavior.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-11 16:01 NUCLEO STOP unchanged counter rule

- Summary: User correctly answered that IDLE + STOP should not increment mode_change_count because the state did not actually change.
- Evidence level: L2
- Confidence: medium
- Weak point observed: None recorded.
- Next review: Teach AppPollCommand line assembly: receive chars, detect newline, terminate string, dispatch command, handle overflow.
- Source: User answer in Codex chat on 2026-05-11
## 2026-05-12 NUCLEO UART DMA + IDLE learning closeout

- Topic: UART receive path from polling command assembly into DMA + IDLE batching.
- Summary: User confirmed the previous AppPollCommand line-assembly material was already covered, then passed a short check on newline detection, string termination, command dispatch, and overflow handling. The lesson moved into DMA + IDLE: user correctly identified DMA as the byte mover into `rx_buf`, IDLE as the batch-complete signal, and the need to restart DMA + IDLE reception after handling each batch.
- Evidence level: L2
- Confidence: medium
- Weak point observed: User initially answered that `Size = 6` should process 5 bytes, showing a count-versus-final-index mix-up. After correction, user answered that `Size = 3` processes indices `0, 1, 2`, showing immediate repair at concept-check level.
- Next review: Before showing real HAL callback code, ask the user to restate: `Size` is count, the loop condition is `i < Size`, and the final processed index is `Size - 1`.
- Not validated: No firmware edit, build, flash, or VOFA+/serial log validation was performed in this ChatGPT turn.
- Source: `learning/session_notes/2026-05-12_uart_dma_idle.md` from PR #2.

## 2026-05-12 NUCLEO UART receive layering and Codex workflow correction

- Topic: UART receive layering from polling input toward DMA + IDLE.
- Summary: User corrected the `Size = 10` check to indices `0..9` with final index `9`, explained that a partial `PI` batch must wait for `\n`, and identified `'\0'` as the C string terminator before `strcmp`/`%s` use. User also called out that the dual-teacher workflow had drifted; Codex switched from chat-only teaching to repo execution, refactored `AppFeedRxByte(...)` out of `AppPollCommand(...)`, and rebuilt the NUCLEO baseline successfully.
- Evidence level: L3
- Confidence: medium
- Weak point observed: Earlier `Size` count/index mix-up is repaired at guided-example level, but still needs transfer to real callback code and serial-log validation before closing.
- Next review: Read the new `AppFeedRxByte` / `AppPollCommand` split and explain how a future DMA callback can feed `rx_buf[0..Size-1]` into the same parser without changing `AppHandleCommand`.
- Validation: `cmake --build build\Debug` succeeded after the refactor; no flash or VOFA+/serial-log validation was performed in this turn.
- Source: Codex teaching, code change, and build on 2026-05-12.

## 2026-05-12 STM32 realtime boundary and ESP32 gateway command split

- Topic: STM32 realtime boundary for UART/JSON gateway commands.
- Summary: User correctly answered that a JSON speed command should be handled on the ESP32 gateway side first, then sent to STM32 as a simplified command, rather than being parsed inside the STM32 FOC/JEOC interrupt.
- Evidence level: L2
- Confidence: medium
- Weak point observed: None recorded.
- Next review: Map one gateway command into a safe STM32-side command format and identify which layer may parse JSON, which layer may update command variables, and which layer must remain hard realtime.
- Source: User answer in Codex chat on 2026-05-12.

## 2026-05-12 STM32 command range guard

- Topic: STM32 communication-layer command validation.
- Summary: User correctly answered that an obviously unreasonable target speed such as `rpm = 999999` should be rejected or clamped in the STM32 communication layer before it can affect FOC control. User then correctly classified `IDLE + SET_RPM 1200` as `ERR bad_state`, because the system has not entered an armed/pre-run state, `ARMED + SET_RPM 999999` as `ERR range` because the state is acceptable but the value is out of range, and `SET_RPM abc` as a parse error.
- Evidence level: L2
- Confidence: medium
- Weak point observed: None recorded.
- Next review: Define a simple accepted/rejected response table for a future `SET_RPM` command before wiring it to any motor-control variable.
- Source: User answer in Codex chat on 2026-05-12.

## 2026-05-12 NUCLEO simulation-only SET_RPM implementation

- Topic: Communication-layer `SET_RPM` guard implementation in the NUCLEO baseline.
- Summary: Codex implemented a learning-only `SET_RPM <rpm>` command in `AppHandleCommand`. It parses the numeric argument, rejects malformed input, enforces the documented `-4000..4000` range, rejects valid speed targets in `IDLE`, updates only a simulated `target_rpm` variable in `ARMED`/`RUN_SIM`, and clears that target on `STOP`.
- Evidence level: L0 for user execution, L3 for code path implementation.
- Confidence: medium.
- Weak point observed: None recorded.
- Next review: Flash/run the NUCLEO baseline and validate `SET_RPM abc`, `SET_RPM 999999`, `SET_RPM 1200` in `IDLE`, then `ARM` + `SET_RPM 1200` over COM5/VOFA+.
- Validation: `cmake --build build\Debug` succeeded after the implementation; no flash or serial-log validation was performed in this turn.
- Source: Codex code change and build on 2026-05-12.

## 2026-05-12 NUCLEO SET_RPM serial validation

- Topic: Board-level serial validation of the learning-only `SET_RPM` command.
- Summary: Codex flashed the NUCLEO baseline through ST-LINK mass storage and validated COM5 command responses. `SET_RPM abc` returned parse error, `SET_RPM 999999` returned range error, `IDLE + SET_RPM 1200` returned bad state, `ARM` entered `ARMED`, `ARMED + SET_RPM 1200` updated `target_rpm=1200`, `STOP` returned to `IDLE` and cleared `target_rpm=0`, and `PING` returned `PONG`.
- Evidence level: L5 for firmware behavior, L2 for user's command-guard reasoning.
- Confidence: high for NUCLEO serial command behavior; not evidence for motor or power-stage behavior.
- Weak point observed: None recorded.
- Next review: Explain why this validates only the communication/state guard layer, then move toward UART DMA + IDLE receive without changing the safety boundary.
- Validation: Evidence saved in `experiments/2026-05-09_nucleo_baseline/logs/2026-05-12_com5_set_rpm_validation.md`.
- Source: Codex COM5 serial validation on 2026-05-12.

## 2026-05-12 NUCLEO STOP side-effect practice and dual-teacher handoff

- Topic: Reading command side effects in the `STOP` branch.
- Summary: User correctly identified that `*target_rpm = 0` is the unconditional safe side effect in `STOP`, while `*app_mode = APP_MODE_IDLE` only executes in the non-IDLE branch. User first predicted `ARMED + STOP` would leave `mode = ARMED`, then corrected the related `IDLE + STOP` and `mode_change_count` checks: `IDLE + STOP` leaves `mode = IDLE`, clears `target_rpm`, and does not increment `mode_change_count`.
- Evidence level: L2
- Confidence: medium.
- Weak point observed: STOP branch execution is partly repaired, but one transfer check remains for non-IDLE STOP paths.
- Next review: In the ChatGPT-led concept turn, classify PING, MODE?, ARM, SET_RPM, and STOP as read-only, safety command, or guarded command; then predict final `mode`, `target_rpm`, and `mode_change_count` for both `IDLE + STOP` and `ARMED + STOP`.
- Workflow note: User again reminded Codex to preserve the dual-teacher split. Codex should stop at repo sync/handoff when the next step is concept teaching, and ChatGPT should lead the next concept segment.
- Source: User answers and workflow correction in Codex chat on 2026-05-12.

## 2026-05-13 NUCLEO P0 transfer checks passed

- Topic: STOP side effects and DMA receive `Size` count/index rule.
- Summary: User independently predicted `ARMED,target_rpm=1200,mode_change_count=5 + STOP` as `mode=IDLE`, `target_rpm=0`, `mode_change_count=6`, and `IDLE,target_rpm=1200,mode_change_count=5 + STOP` as `mode=IDLE`, `target_rpm=0`, `mode_change_count=5`. User also answered that `Size = 10` means processing indices `0..9` with loop condition `i < Size`.
- Evidence level: L4 for STOP side-effect transfer and DMA `Size` count/index transfer.
- Confidence: medium.
- Weak point observed: No new weak point. The remaining next check is full DMA + IDLE callback structure: DMA fills the buffer, IDLE marks a ready batch, CPU feeds `rx_buf[0..Size-1]` into `AppFeedRxByte(...)`, then reception restarts.
- Next review: Move to P1 command classification and branch side-effect reading; then ask the user to describe the DMA + IDLE callback flow in five steps.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-13 NUCLEO command variable classification

- Topic: Command side-effect classification across `PING`, `MODE?`, `ARM`, `SET_RPM`, and `STOP`.
- Summary: User correctly classified `PING` and `MODE?` as changing no variables, `ARM` as changing `app_mode` and `mode_change_count`, and `SET_RPM` as changing `target_rpm`. User classified `STOP` as changing `app_mode` and `mode_change_count`, but omitted its unconditional `target_rpm=0` side effect.
- Evidence level: L3 for command variable classification; STOP target clear still needs one compact repair check.
- Confidence: medium.
- Weak point observed: Existing WP-028 remains open: variable classification must include both conditional state/counter side effects and unconditional safety side effects.
- Next review: Ask the user to restate `STOP` as `target_rpm` always changes to 0, while `app_mode` and `mode_change_count` only change when the previous mode is not `IDLE`.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-13 NUCLEO STOP unconditional vs conditional side effects

- Topic: Separating side effects outside and inside the `STOP` branch guard.
- Summary: User correctly answered that `STOP` always clears `target_rpm` to 0, but then listed `app_mode` and `target_rpm` as the conditional side effects. This shows the remaining confusion is not the STOP outcome itself, but separating the line that always runs from the lines inside `if (mode != IDLE)`.
- Evidence level: L2-L3.
- Confidence: medium.
- Weak point observed: Existing WP-028 remains open; emphasize code block location: outside the `if` is unconditional, inside the `if` is conditional.
- Next review: Show the three-line STOP pseudocode and ask which exact two lines are inside the `if`.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-13 NUCLEO STOP branch location repair

- Topic: Reading side effects by code block location.
- Summary: After seeing the STOP pseudocode, user correctly identified the two statements inside `if (mode != IDLE)` as `app_mode = IDLE` and `mode_change_count++`. This repairs the immediate confusion between unconditional `target_rpm=0` and conditional state/counter side effects.
- Evidence level: L3.
- Confidence: medium.
- Weak point observed: Existing WP-028 can move forward from STOP repair to transfer: apply the same outside-if versus inside-if reading to `ARM` and read-only query branches.
- Next review: On the `ARM` branch, label the command match condition, the state guard, the assignment side effect, the counter side effect, and the response output.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-13 NUCLEO ARM branch guard and side effects

- Topic: Reading the `ARM` command guard and successful side effects.
- Summary: User correctly answered that the `ARM` command condition is the current mode being `IDLE`, and that successful `ARM` changes `app_mode` and increments `mode_change_count`.
- Evidence level: L3.
- Confidence: medium.
- Weak point observed: Existing WP-023 is improving, but needs one transfer check for rejected `RUN_SIM + ARM`. Existing WP-028 still needs response-output labeling on the `ARM` branch.
- Next review: Ask what `RUN_SIM + ARM` should do to `app_mode` and `mode_change_count`, then identify which `printf` response line reports accepted versus rejected.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-13 NUCLEO ARM rejected-state transfer

- Topic: Applying the `ARM` guard to a rejected run-like state.
- Summary: User correctly answered that `RUN_SIM + ARM` does not change `app_mode`, does not increment `mode_change_count`, and should return `ERR`.
- Evidence level: L4 for the current `ARM` guard transfer check.
- Confidence: medium.
- Weak point observed: WP-023 can be parked for the current P1 layer. WP-028 remains open for code-reading transfer to response output lines and read-only query branches.
- Next review: Move to `MODE?`: identify that `strcmp(cmd, "MODE?") == 0` selects the branch, `printf(...)` outputs the mode, and no assignment means no state change.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-13 NUCLEO MODE query branch reading

- Topic: Reading the `MODE?` query branch.
- Summary: User correctly identified the first line, `strcmp(cmd, "MODE?") == 0`, as the command-match check and described `MODE?` as a read-only query. The remaining code-reading step is to prove read-only behavior from the branch body: it has `printf(...)` output but no `app_mode = ...` assignment.
- Evidence level: L2-L3.
- Confidence: medium.
- Weak point observed: Existing WP-027 and WP-028 remain open until the user states that `printf` only reports and no assignment means no state change.
- Next review: Ask why a branch with only `printf(...)` and no `app_mode = ...` cannot change `app_mode`.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-13 NUCLEO query branch evidence and difficulty adjustment

- Topic: Closing low-value query-branch drills and raising lesson difficulty.
- Summary: User identified `printf("mode=... mode_name=...");` as the `MODE?` output evidence, then explicitly said the question was too simple. This is enough for the current P1 layer: future teaching should stop drilling simple read-only query recognition and move to callback structure or multi-line branch reading.
- Evidence level: L3 for current-layer query branch reading.
- Confidence: medium.
- Weak point observed: No new weak point. Existing WP-027 should be parked for the current layer; WP-028 should move to higher-value transfer checks rather than more simple fill-in questions.
- Next review: Use a harder exercise: read a DMA + IDLE callback skeleton and identify data movement, loop bounds, parser feeding, and restart responsibilities.
- Source: User answer and difficulty feedback in Codex chat on 2026-05-13.

## 2026-05-13 NUCLEO DMA + IDLE callback skeleton reading

- Topic: Reading callback responsibilities for DMA + IDLE UART receive.
- Summary: User correctly identified `AppFeedRxByte(rx_buf[i], ...)` as the line that feeds bytes into the command parser, `HAL_UARTEx_ReceiveToIdle_DMA(&huart2, rx_buf, sizeof(rx_buf))` as the line that restarts reception, and that the callback should not contain direct `ARM`/`STOP`/`SET_RPM` command logic because it must stay short. User answered the processed range as `0 到 i-1`, which mixes the changing loop index with the fixed batch count; the correct range for one callback batch is `0..Size-1`.
- Evidence level: L3 for callback responsibility reading; L2-L3 for callback loop-bound transfer.
- Confidence: medium.
- Weak point observed: WP-029 should reopen narrowly for callback loop-bound wording: `i` is the current index, while `Size` is the received byte count.
- Next review: Ask the user to state the difference between `i` and `Size` in the callback, then describe the full callback flow in five steps.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-13 NUCLEO DMA index versus batch size repair

- Topic: Distinguishing the loop index from the received-byte count.
- Summary: User correctly explained that `i` is the changing current index inside the loop, `Size` is the total byte count received in the current batch, and array indices start at 0. This repairs the immediate `0..i-1` wording slip from the callback skeleton exercise.
- Evidence level: L4 for the current `i` versus `Size` distinction.
- Confidence: medium.
- Weak point observed: WP-029 can be parked again for the current layer. The remaining useful check is the full DMA + IDLE callback flow in five steps.
- Next review: Ask the user to describe the callback flow: DMA fills `rx_buf`, IDLE marks a batch ready, CPU loops `i < Size`, each byte feeds `AppFeedRxByte(...)`, then DMA + IDLE receive restarts.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-13 NUCLEO DMA + IDLE five-step flow partial

- Topic: Full DMA + IDLE callback flow.
- Summary: User correctly answered that DMA transfers data, each byte is handed to `AppFeedRxByte(rx_buf[i], &app_mode, &mode_change_count, &target_rpm)`, and reception must restart because otherwise the next batch may not be received. User described IDLE as "空闲状态", which needs sharpening: in this context it is UART line idle / no new byte for a short interval, meaning the current receive batch is ready. User left the CPU loop step blank; the needed line is `for (uint16_t i = 0; i < Size; i++)`, processing `rx_buf[0..Size-1]`.
- Evidence level: L3 for parser/restart responsibility; L2-L3 for full callback-flow description.
- Confidence: medium.
- Weak point observed: WP-028 remains open for full callback-flow sequencing; add a narrow review for UART IDLE meaning versus application `IDLE` mode.
- Next review: Ask the user to restate two missing pieces only: what UART IDLE means in this callback, and which loop processes `rx_buf[0..Size-1]`.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-13 NUCLEO DMA + IDLE callback flow completed

- Topic: Completing the full DMA + IDLE callback explanation.
- Summary: User correctly restated that UART IDLE means the current byte batch is temporarily complete and ready to process, and that CPU processes `rx_buf[0..Size-1]` with `for (i = 0; i < Size; i++)`. Combined with the previous answer, the user can now describe the full callback flow: DMA transfers bytes into `rx_buf`, UART IDLE marks a ready batch, CPU loops through valid indices, each byte feeds `AppFeedRxByte(...)`, and reception is restarted for the next batch.
- Evidence level: L4 for current-layer DMA + IDLE callback structure.
- Confidence: medium.
- Weak point observed: No new weak point. WP-028 can be parked for the current P1 layer; reopen only when implementing or reviewing the real HAL callback.
- Next review: Move from concept reading to implementation/verification when appropriate: connect the existing `AppFeedRxByte(...)` parser split to a future real `HAL_UARTEx_RxEventCallback(...)`, then build/validate without adding command logic inside the callback.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-13 P2 MCSDK no-power precheck boundary

- Topic: MCSDK no-power precheck and Motor Profiler boundary.
- Summary: User correctly answered that Motor Profiler cannot be run in P2 because it needs a real motor and power chain. User also correctly distinguished what an MCSDK-generated project can prove without power: familiarity with the toolchain and configuration flow, but not real motor parameters, power-chain behavior, or motor-control validation.
- Evidence level: L3 for P2 no-power boundary understanding.
- Confidence: medium.
- Weak point observed: No new weak point. The next useful check is artifact planning: tool version table, Workbench/config placeholder, pin map draft, Motor Profiler plan, and risk/no-go checklist.
- Next review: Ask the learner to list the P2 no-power artifacts and identify which later artifacts require real hardware.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-13 P2 MCSDK no-power artifact planning

- Topic: P2 no-power artifact list versus later hardware evidence.
- Summary: User listed P2 no-power artifacts as pin map, motor-parameter table, no-power configuration file, risk/no-go checklist, and Motor Profiler plan. User also correctly stated that real motor parameters must wait until a later stage with real motor and power chain. The only wording repair is that P2 may contain a motor-parameter template or placeholder, not measured parameters.
- Evidence level: L3-L4 for P2 artifact planning.
- Confidence: medium.
- Weak point observed: No new weak point. Keep the distinction between planned/template artifacts and measured hardware evidence explicit in future P2 work.
- Next review: Start building the P2 artifact set, beginning with a tool version/status table and pin/config draft, while keeping Motor Profiler as a plan only.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-13 P2 MCSDK config evidence boundary

- Topic: `.stmcx`, generated project, and Motor Profiler evidence boundaries.
- Summary: User correctly explained that a `.stmcx` in P2 can prove the saved/planned MCSDK configuration choices such as MCU, PWM pins, current-sensing approach, Hall versus sensorless selection, and protection input location. User also correctly stated that even a compiled MCSDK project cannot prove safe motor behavior because nFAULT, PWM, current sensing, Hall, power board, current limit, and rollback evidence are still missing. User answered that Motor Profiler needs real hardware; precision added by Codex: the later valid Profiler stage must also include a real motor, verified power chain, current-limited supply, instruments, stop conditions, and rollback path.
- Evidence level: L3-L4 for P2 configuration-evidence boundary; L3 for Motor Profiler hardware-boundary wording.
- Confidence: medium-high.
- Weak point observed: No new weak point. Keep reinforcing that configuration artifacts prove planning/build readiness only, not motor-control behavior.
- Next review: When Workbench/CubeMX screenshot or `.stmcx` evidence arrives, ask the learner to identify which fields are configuration evidence and which still require board-routing or hardware-stage proof.
- Source: User answer in Codex chat on 2026-05-13.

## 2026-05-14 P2 MCSDK no-power practice start

- Topic: Moving from P2 concept checks into no-power MCSDK configuration practice.
- Summary: User asked to stop extending concept-only evidence drills and start practical work. Codex kept the P2 safety boundary, created `apps/stm32_g474_foc/mcsdk_no_power_precheck/`, wrote `config_draft.md` and `tool_probe_2026-05-14.md`, confirmed CubeMX path `F:\STMCubeMX\STM32CubeMX.exe`, and launched CubeMX to a `javaw.exe` process. Repo search still found no `.stmcx`, and no standalone Workbench executable was found under `MCSDK_v6.4.2-Full`.
- Evidence level: L5 for repo/tool execution by Codex; no new learner mastery claim.
- Confidence: high for local file/tool facts; medium for GUI readiness because no screenshot or saved config is present yet.
- Weak point observed: No new learner weak point. The practical gap remains P2 artifact implementation.
- Next review: Once a screenshot or `.stmcx` is captured, ask the learner to classify it as configuration/tool evidence and list which hardware-stage proofs remain blocked.
- Source: Codex execution in `foc_learning_repo` on 2026-05-14.

## 2026-05-14 NUCLEO UART DMA + IDLE implementation

- Topic: Moving project firmware forward instead of adding more tool screenshots.
- Summary: Codex updated `apps/stm32_g474_foc/nucleo_g474re_baseline/Core/Src/main.c` so COM1 receive now uses LPUART1 RX DMA + IDLE. The callback copies bytes into a ring buffer and restarts receive-to-idle DMA; the main loop drains the queue and calls the existing command parser. `stm32g4xx_it.c` and `stm32g4xx_it.h` now include `DMA1_Channel1_IRQHandler()` and `LPUART1_IRQHandler()`. Debug build passed with RAM 2552 B and FLASH 23652 B.
- Evidence level: L5 for repo/tool execution by Codex; no new learner mastery claim.
- Confidence: high for compile-level firmware integration. Board-level serial behavior still needs a COM5 run if the user wants live confirmation.
- Weak point observed: No new learner weak point.
- Next review: If a live NUCLEO check is run later, verify that `PING`, `MODE?`, `ARM`, `SET_RPM`, and `STOP` keep the same semantics under DMA + IDLE.
- Source: Codex execution and Debug build in `foc_learning_repo` on 2026-05-14.

## 2026-05-14 UART protocol line framer model

- Topic: Advancing the ESP32/STM32 UART protocol path with host-verifiable code.
- Summary: Codex added `LineFramer` to `src/protocol_model.py` and expanded `tests/test_protocol_model.py` from 14 to 19 tests. The model accepts DMA/IDLE-like byte chunks, emits complete newline-terminated frames, ignores empty lines, drops oversize partial frames, discards overlong data until line end, and recovers for later frames. The full test suite now has 24 tests including workflow-gate checks.
- Evidence level: L5 for repo/tool execution by Codex; no new learner mastery claim.
- Confidence: high for host protocol behavior because `python -m unittest discover -s tests` passed.
- Weak point observed: No new learner weak point.
- Next review: When embedded C builds can be rerun, move command parsing out of `main.c` toward the tested line-framing/protocol model.
- Source: Codex execution in `foc_learning_repo` on 2026-05-14.

## 2026-05-14 P2 CubeMX Home screenshot capture

- Topic: Turning the opened CubeMX GUI into repo-visible P2 evidence.
- Summary: Codex cropped the visible CubeMX Home window from the desktop screenshot and saved it as `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png`. Codex also added `gui_capture_checklist_2026-05-14.md` to define the next allowed GUI-only capture targets and forbidden hardware actions.
- Evidence level: L5 for repo/tool execution by Codex; no new learner mastery claim.
- Confidence: high for the screenshot file and repo artifact. The screenshot is GUI launch evidence only; it is not an MCSDK draft configuration screenshot or `.stmcx`.
- Weak point observed: No new learner weak point. The practical gap is still a saved Workbench/CubeMX draft or exact GUI block record.
- Next review: After the draft screenshot or `.stmcx` exists, ask the learner to classify each field as configuration evidence, board-routing evidence, or later powered-hardware evidence.
- Source: Codex execution in `foc_learning_repo` on 2026-05-14.

## 2026-05-14 Codex dual-teacher gate hardening

- Topic: Preventing Codex from drifting into silent engineering execution.
- Summary: User corrected that Codex must not only do project work; each continuation must keep the teaching role visible. Codex added `workflow/codex_dual_teacher_execution_gate.md`, linked it from `AGENTS.md`, `workflow/teaching_contract.md`, `workflow/prompt_recipes.md`, `workflow/session_close_checklist.md`, and the project Skill source, then added `tests/test_workflow_contracts.py` to guard the rule.
- Evidence level: L5 for repo/workflow implementation by Codex; no new learner mastery claim.
- Confidence: high for repository rule hardening once tests pass.
- Weak point observed: No learner weak point. The assistant workflow risk is now tracked as a repo rule rather than a chat-only reminder.
- Next review: On the next `继续吧` turn, Codex must begin with `项目目标` / `学习目标` / `修改范围` / `禁止范围` before tool use or edits.
- Source: User correction and Codex execution in `foc_learning_repo` on 2026-05-14.

## 2026-05-14 P2 pin/config safety review start

- Topic: Moving beyond toolchain navigation into the next P2 engineering review ring.
- Summary: User clarified they are already familiar with the toolchain, so Codex should stop hand-holding CubeMX/CubeIDE navigation and begin the next stage directly. Codex added `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md`, which defines evidence classes, acceptance rules, fail conditions, and hard stops for `PB12/TIM1_BKIN`, `PB14/TIM1_CH2N`, `PA2/PA3`, `PB3`, `DT/MODE`, and STDRIVE101 protection paths.
- Evidence level: L5 for repo/workflow implementation by Codex; no new learner mastery claim.
- Confidence: high for repo artifact creation and source linkage; hardware confidence remains P2-only because no `.stmcx`, CN8/EDA/netlist, continuity check, power-board connection, or powered log exists.
- Weak point observed: No learner weak point. Teaching preference recorded separately: skip basic toolchain navigation unless explicitly requested.
- Next review: Use the pin/config safety review as the next checkpoint. Collect `.stmcx` or config screenshot, CN8/EDA/netlist routing evidence, and STDRIVE101 `nFAULT` / `DT/MODE` / protection evidence before trusting generated MCSDK configuration.
- Source: User correction and Codex execution in `foc_learning_repo` on 2026-05-14.

## 2026-05-14 P2 NUCLEO CubeMX hands-on draft

- Topic: Turning the P2 no-power lesson into a user-performed CubeMX Board Selector draft.
- Summary: User corrected the workflow from bare MCU selection to the real `NUCLEO-G474RE` board path, then used CubeMX Pinout to inspect and save a no-power draft. User-provided GUI screenshots showed `PA13/PA14` as SWD, `PA2/PA3` as VCP, `PB3` as SWO, `PB12` as `TIM1_BKIN`, and `PB14` as `TIM1_CH2N`. Codex read back the saved `.ioc` at `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc` and confirmed the same assignments.
- Evidence level: L4 for learner hands-on recognition of NUCLEO board-level pin ownership and CubeMX config evidence; L5 for repo/tool evidence because the `.ioc` is saved and readable.
- Confidence: high for CubeMX config-layer evidence; hardware confidence remains P2-only because there is still no `.stmcx`, CN8/EDA/netlist, continuity check, power-board connection, or powered log.
- Weak point observed: No new learner weak point. The useful next check is whether the learner can explain why the saved `.ioc` proves configuration intent but not STDRIVE101 wiring or safe motor behavior.
- Next review: Ask the learner to classify `PB12/TIM1_BKIN`, `PB14/TIM1_CH2N`, `PA2/PA3` VCP, and `PB3` SWO as configuration evidence, board-ownership evidence, or later hardware-stage proof.
- Source: User hands-on CubeMX screenshots and Codex `.ioc` readback on 2026-05-14.

## 2026-05-14 P2 CubeMX `.ioc` GUI capture

- Topic: Converting the saved NUCLEO `.ioc` into repo-visible GUI fallback evidence.
- Summary: Codex launched `F:\STMCubeMX\STM32CubeMX.exe` with the saved NUCLEO-G474RE `.ioc`, captured CubeMX `Pinout & Configuration` screenshots, and wrote `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_result_2026-05-14.md`. The screenshots show the `.ioc` open in CubeMX with `STM32G474RETx - NUCLEO-G474RE`; `.ioc` readback still confirms `PB12/TIM1_BKIN`, `PB14/TIM1_CH2N`, `PA2/PA3` VCP, and `PB3` SWO. Repo search still found no `.stmcx`, and no MotorControl configuration page was captured.
- Evidence level: L5 for repo/tool evidence that the `.ioc` can be reopened and captured in CubeMX; no new learner mastery claim.
- Confidence: high for the screenshot files and `.ioc` readback. This remains fallback GUI evidence only, not MCSDK/Workbench MotorControl evidence.
- Weak point observed: No new learner weak point. The practical gap remains collecting real `.stmcx` or MotorControl screenshot, CN8/EDA/netlist, and STDRIVE101 protection-path evidence.
- Next review: Ask the learner to explain why a CubeMX pinout screenshot plus `.ioc` readback still cannot prove board wiring, Motor Profiler readiness, or safe motor-control behavior.
- Source: Codex GUI screenshot capture and repo search in `foc_learning_repo` on 2026-05-14.

## 2026-05-14 P2 Workbench entry probe

- Topic: Turning the missing Workbench / `.stmcx` entry into a concrete no-power blocker.
- Summary: Codex added `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`. Targeted checks covered the repo, `F:\STMCubeMX`, the MCSDK package, VS Code STM32 extension folders, `.stm32cubemx`, and common ST program roots. The probe confirmed MCSDK `MotorControl` package data exists, including `MotorControl_Configs.xml`, `MotorControl_Modes.xml`, `MCSDK/`, `templates/`, `libMP/`, and `libHSO/`, but still found no `.stmcx`, no standalone Workbench launcher, and no MotorControl configuration page evidence.
- Evidence level: L5 for repo/tool evidence that MotorControl package data is installed; no new learner mastery claim.
- Confidence: high for the checked local paths. This remains package-presence evidence only, not saved project configuration evidence.
- Weak point observed: No new learner weak point. The next practical gap is to obtain either a real `.stmcx`, a MotorControl screenshot, or board-routing evidence.
- Next review: Ask the learner to distinguish package data, saved configuration, generated firmware, and hardware validation.
- Source: Codex targeted local path probe in `foc_learning_repo` on 2026-05-14.
