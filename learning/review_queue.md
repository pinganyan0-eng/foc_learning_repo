# Review Queue

Use this as a lightweight spaced review queue. Each item should be small enough to check in 3-10 minutes.

| Due | Topic | Prompt | Source Weak Point | Status |
| --- | --- | --- | --- | --- |
| next learning turn | NUCLEO mode-name serial validation | Explain what evidence proves `mode` and `mode_name` changed together, then move to UART receive. | WP-021 | open |
| next learning turn | NUCLEO UART query command semantics | Classify PING, MODE?, ARM, STOP, and FAULT_CLEAR as read-only or state-changing. | WP-022 | open |
| next learning turn | NUCLEO ARM command state guard | Write the accepted transition for IDLE + ARM and rejected transition for RUN_SIM + ARM. | WP-023 | open |
| next learning turn | NUCLEO STOP command idempotence | Explain why IDLE + STOP and RUN_SIM + STOP are both accepted, but only one changes state. | WP-024 | open |
| next learning turn | NUCLEO MODE query code reading | Identify what `strcmp` returns when the command equals MODE?, and why `== 0` means matched. | WP-027 | open |
| next learning turn | NUCLEO command matching versus side effect | Identify the line that changes state in ARM and the line that only prints output in PING. | WP-028 | open |
| next learning turn | NUCLEO ARM branch state assignment | Explain why the APP_MODE_IDLE guard must come before the ARM assignment. | - | open |
| next learning turn | NUCLEO AppPollCommand line assembly | Explain receive-char accumulation, newline detection, string termination, dispatch, and overflow handling. | - | open |

## Review Cadence

- Keep the active queue small, normally 5-8 open items.
- Do not queue every next step; queue only real weak points or safety-critical checks.
- Same day: check whether the user can restate the concept.
- Next day: check a small problem or configuration decision.
- 3-7 days: check transfer to a new but similar situation.
- Before hardware/power actions: re-check safety-critical weak points.
