# Review Queue

Use this as a lightweight spaced review queue. Each item should be small enough to check in 3-10 minutes.

| Due | Topic | Prompt | Source Weak Point | Status |
| --- | --- | --- | --- | --- |
| next learning turn | NUCLEO UART query command semantics | Classify PING, MODE?, ARM, STOP, and FAULT_CLEAR as read-only or state-changing. | WP-022 | open |
| next learning turn | NUCLEO ARM command state guard | Write the accepted transition for IDLE + ARM and rejected transition for RUN_SIM + ARM. | WP-023 | open |
| next learning turn | NUCLEO STOP command idempotence | Explain why IDLE + STOP and RUN_SIM + STOP are both accepted, but only one changes state. | WP-024 | open |
| next learning turn | NUCLEO MODE query code reading | Identify what `strcmp` returns when the command equals MODE?, and why `== 0` means matched. | WP-027 | open |
| next learning turn | NUCLEO command matching versus side effect | Identify the line that changes state in ARM and the line that only prints output in PING. | WP-028 | open |
| next learning turn | NUCLEO DMA receive size/index | Given `Size = N`, state the processed indices, the loop condition `i < Size`, and the final index `Size - 1`. | WP-029 | open |
| next learning turn | NUCLEO DMA + IDLE callback structure | Explain that DMA fills `rx_buf`, IDLE signals one batch is ready, CPU loops through `0..Size-1`, and reception must be restarted. | - | open |
| next Codex validation | NUCLEO UART command serial validation | Flash/run firmware, send PING, MODE?, ARM, STOP over COM5, and capture a serial log proving responses and mode changes match the command table. | - | open |

## Review Cadence

- Keep the active queue small, normally 5-8 open items.
- Do not queue every next step; queue only real weak points or safety-critical checks.
- Same day: check whether the user can restate the concept.
- Next day: check a small problem or configuration decision.
- 3-7 days: check transfer to a new but similar situation.
- Before hardware/power actions: re-check safety-critical weak points.
