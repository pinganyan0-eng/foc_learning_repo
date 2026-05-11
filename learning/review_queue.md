# Review Queue

Use this as a lightweight spaced review queue. Each item should be small enough to check in 3-10 minutes.

| Due | Topic | Prompt | Source Weak Point | Status |
| --- | --- | --- | --- | --- |
| next learning turn | Learning loop usage | Ask one teach-back question and record the result. | WP-000 | open |
| next learning turn | NUCLEO nonblocking tick scheduler | Explain why LED full on-off cycle is twice the toggle interval, then add a simple status counter or button event using the same scheduler pattern. | WP-001 | open |
| next learning turn | NUCLEO multi-rate task counter | Add a button event counter with the same nonblocking scheduler pattern; ask user to predict counter changes before running. | WP-002 | open |
| next learning turn | NUCLEO B1 button event counter | Ask user to explain why button_last_state is needed and why btn can be 0 while btn_press has already increased. | WP-003 | open |
| next learning turn | NUCLEO button edge detection and debounce | Introduce a tiny finite state machine using the same button event: press B1 to cycle mode 0/1/2 and report mode over UART. | WP-004 | open |
| next learning turn | NUCLEO minimal app state machine | Ask user to explain current state + event = next state, and why safety states require explicit acknowledgement before returning to run-like states. | WP-005 | open |
| next learning turn | NUCLEO state machine concept check | Teach a named-state transition table for IDLE/ARMED/RUN_SIM and make B1 cycle through explicit cases. | WP-006 | open |
| next learning turn | NUCLEO explicit state transition table | Refactor APP_MODE_* definitions into USER CODE BEGIN PD or an enum, then discuss why embedded projects keep state definitions near top-level declarations. | WP-007 | open |
| next learning turn | NUCLEO app mode labels | Ask user to map mode=2 and then explain why a label table should sit above the main loop. | WP-008 | open |
| next learning turn | NUCLEO mode number mapping | Use a classroom name-list analogy to explain why state labels belong in the enum/type area above main(). | WP-009 | open |
| next learning turn | NUCLEO enum placement intuition | Ask user to identify which part is the fixed state dictionary and which part is the repeated transition logic in the current main.c. | WP-010 | open |
| next learning turn | NUCLEO switch state transition | Ask user to map the remaining transitions and explain why an unknown state should return to IDLE. | WP-011 | open |
| next learning turn | NUCLEO full state cycle | Ask user why an unknown state should not jump directly into RUN_SIM, then connect that to motor-control FAULT safety. | WP-012 | open |
| next learning turn | NUCLEO default safe fallback | Have user restate the full state machine as current state, button event, next state, then connect IDLE fallback to future FAULT handling. | WP-013 | open |
| next learning turn | NUCLEO state machine formula teach-back | Ask what happens to app_mode when no B1 press event occurs, then map that to the if-condition around the switch. | WP-014 | open |
| next learning turn | NUCLEO event-gated transition | Show the button edge if-condition and ask the user which three conditions must be true before switch(app_mode) runs. | WP-015 | open |
| next learning turn | NUCLEO debounce as state-machine gate | Ask user to predict the final mode if one physical press is mistakenly counted as three valid press events starting from IDLE. | WP-016 | open |
| next learning turn | NUCLEO debounce multiple transition prediction | Ask user to predict the final state for three mistaken events from IDLE, then connect this to why motor start logic needs strong event gating. | WP-017 | open |
| next learning turn | NUCLEO debounce three-transition prediction | Ask user why a motor-control system should not let one noisy button press move through IDLE, ARMED, and RUN-like states in one burst. | WP-018 | open |
| next learning turn | NUCLEO one-event-one-transition rule | Ask user to explain what checks could be skipped if a noisy start button jumps directly from IDLE to RUN. | WP-019 | open |
| next learning turn | NUCLEO ARMED as pre-run check state | Ask user to name two checks that should happen before a motor enters RUN, then map them to voltage/current/nFAULT/PWM readiness. | WP-020 | open |
| next learning turn | NUCLEO UART mode name logging | Flash/run the NUCLEO baseline and check that mode and mode_name change together when B1 is pressed. | - | open |
| next learning turn | NUCLEO mode-name serial validation | Use the validated serial log to introduce UART receive: first receive one simple command line such as MODE? or PING without touching power-board or motor hardware. | WP-021 | open |
| next learning turn | NUCLEO UART query command semantics | Classify PING, MODE?, ARM, STOP, and FAULT_CLEAR as read-only queries or state-changing commands, then explain which ones are allowed to change app_mode. | WP-022 | open |
| next learning turn | NUCLEO ARM vs STOP command safety | Ask user to name two guard conditions that should be checked before accepting ARM, then map them to future voltage/current/nFAULT/PWM readiness checks. | - | open |
| next learning turn | NUCLEO ARM command state guard | Ask user to write the accepted transition for IDLE + ARM and the rejected transition for RUN_SIM + ARM. | WP-023 | open |
| next learning turn | NUCLEO STOP command idempotence | Ask user to classify IDLE + STOP as accepted with no state change, then explain why repeated STOP commands must not move the system elsewhere. | WP-024 | open |
| next learning turn | NUCLEO STOP from run-like state | Ask user to compare IDLE + STOP and RUN_SIM + STOP, and explain why both are accepted but only RUN_SIM + STOP changes app_mode. | WP-025 | open |
| next learning turn | NUCLEO STOP from ARMED state | Ask user to complete the three STOP transitions using explicit state names instead of the word safety. | WP-026 | open |
| next learning turn | NUCLEO UART command side-effect classification | Ask user to write next state and response category for IDLE + ARM, RUN_SIM + ARM, IDLE + STOP, and RUN_SIM + MODE?. | - | open |
| next learning turn | NUCLEO UART command table confidence | Move from table lookup to implementation structure: design a command handler that separates parsing, read-only queries, guarded transitions, and response text. | - | open |
| next learning turn | NUCLEO UART polling command handler | Flash the rebuilt firmware, send PING, MODE?, ARM, STOP over COM5, and capture a serial log proving command responses and mode changes match the command table. | - | open |
| next learning turn | NUCLEO MODE query code reading | Ask user to identify what strcmp returns when cmd equals MODE?, and why == 0 means matched. | WP-027 | open |
| next learning turn | NUCLEO strcmp command matching | Apply strcmp understanding to the PING and ARM branches: identify command matching, output, and state-change lines. | - | open |
| next learning turn | NUCLEO command matching versus side effect | Ask user to identify the line that changes state in the ARM branch and the line that only prints output in the PING branch. | WP-028 | open |
| next learning turn | NUCLEO PING branch output and no side effect | Move to the ARM branch and identify separately the command match condition, state guard, state assignment, counter update, and response output. | - | open |
| next learning turn | NUCLEO ARM branch state assignment | Explain why the APP_MODE_IDLE guard must come before that assignment, then ask what would go wrong if ARM always assigned ARMED. | - | open |
| next learning turn | NUCLEO ARM guard prevents invalid transition | Move to STOP branch and explain accepted unchanged versus accepted changed behavior. | - | open |
| next learning turn | NUCLEO STOP unchanged counter rule | Teach AppPollCommand line assembly: receive chars, detect newline, terminate string, dispatch command, handle overflow. | - | open |
| next learning turn | NUCLEO UART raw buffer vs C string | Given partial input AB without newline, identify rx_line contents, rx_len, whether it is a valid C string, then repeat after newline adds the null terminator. | WP-029 | open |

## Review Cadence

- Same day: check whether the user can restate the concept.
- Next day: check a small problem or configuration decision.
- 3-7 days: check transfer to a new but similar situation.
- Before hardware/power actions: re-check safety-critical weak points.
