# Weak Points

Track weak points only when there is evidence from the user's questions, mistakes, explanations, logs, code, measurements, or failed practice.

| ID | Topic | Evidence Level | Symptom | Repair Plan | Next Check | Status |
| --- | --- | --- | --- | --- | --- | --- |
| WP-000 | Learning loop startup | L0 | No project-specific weak point recorded yet. | Record the first real weak point after teaching or review. | Next learning turn | open |
| WP-001 | NUCLEO nonblocking tick scheduler | L1 | Earlier tendency to treat run success as mastery; reinforce concept check before moving on. | Explain why LED full on-off cycle is twice the toggle interval, then add a simple status counter or button event using the same scheduler pattern. | Explain why LED full on-off cycle is twice the toggle interval, then add a simple status counter or button event using the same scheduler pattern. | open |
| WP-002 | NUCLEO multi-rate task counter | L1 | Non-integer task-rate ratios need one more reinforcement: average rate can be fractional, but integer counters change in discrete +2/+3 patterns. | Add a button event counter with the same nonblocking scheduler pattern; ask user to predict counter changes before running. | Add a button event counter with the same nonblocking scheduler pattern; ask user to predict counter changes before running. | open |
| WP-003 | NUCLEO B1 button event counter | L1 | Need confirm understanding of edge detection: btn is current sampled level, btn_press is accumulated rising-edge event count; if only checking button_state==PRESSED, a held button would be counted repeatedly. | Ask user to explain why button_last_state is needed and why btn can be 0 while btn_press has already increased. | Ask user to explain why button_last_state is needed and why btn can be 0 while btn_press has already increased. | open |
| WP-004 | NUCLEO button edge detection and debounce | L1 | Clarify distinction between btn current sampled level and btn_press historical event count when interpreting logs. | Introduce a tiny finite state machine using the same button event: press B1 to cycle mode 0/1/2 and report mode over UART. | Introduce a tiny finite state machine using the same button event: press B1 to cycle mode 0/1/2 and report mode over UART. | open |
| WP-005 | NUCLEO minimal app state machine | L1 | Need confirm why state transitions must be event-gated and why motor-control FAULT states should not jump directly back to RUN. | Ask user to explain current state + event = next state, and why safety states require explicit acknowledgement before returning to run-like states. | Ask user to explain current state + event = next state, and why safety states require explicit acknowledgement before returning to run-like states. | open |
| WP-006 | NUCLEO state machine concept check | L1 | Next reinforce explicit transition tables instead of ad hoc app_mode++ logic before mapping to IDLE/RUN/FAULT. | Teach a named-state transition table for IDLE/ARMED/RUN_SIM and make B1 cycle through explicit cases. | Teach a named-state transition table for IDLE/ARMED/RUN_SIM and make B1 cycle through explicit cases. | open |
| WP-007 | NUCLEO explicit state transition table | L1 | Next reinforce named states and source layout: move mode defines out of main block and avoid macro definitions inside executable code regions. | Refactor APP_MODE_* definitions into USER CODE BEGIN PD or an enum, then discuss why embedded projects keep state definitions near top-level declarations. | Refactor APP_MODE_* definitions into USER CODE BEGIN PD or an enum, then discuss why embedded projects keep state definitions near top-level declarations. | open |

## Update Rules

- Do not add a weak point from guesswork alone.
- Prefer one precise weak point over a broad label.
- Include a concrete next check that can prove improvement.
- Close or downgrade weak points only when the user shows evidence at L4 or above.
