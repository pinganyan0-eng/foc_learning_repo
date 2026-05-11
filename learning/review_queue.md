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

## Review Cadence

- Same day: check whether the user can restate the concept.
- Next day: check a small problem or configuration decision.
- 3-7 days: check transfer to a new but similar situation.
- Before hardware/power actions: re-check safety-critical weak points.
