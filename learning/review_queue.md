# Review Queue

Use this as a lightweight spaced review queue. Each item should be small enough to check in 3-10 minutes.

| Due | Topic | Prompt | Source Weak Point | Status |
| --- | --- | --- | --- | --- |
| next learning turn | NUCLEO UART query command semantics | Classify PING, MODE?, ARM, STOP, and FAULT_CLEAR as read-only or state-changing. | WP-022 | open |
| next learning turn | NUCLEO ARM command state guard | Write the accepted transition for IDLE + ARM and rejected transition for RUN_SIM + ARM. | WP-023 | open |
| next learning turn | NUCLEO STOP command idempotence | Given ARMED,target_rpm=1200,count=5 and STOP, predict final mode,target_rpm,count; then compare with IDLE,target_rpm=1200,count=5 and STOP. | WP-024 | open |
| next learning turn | NUCLEO MODE query code reading | Identify what `strcmp` returns when the command equals MODE?, and why `== 0` means matched. | WP-027 | open |
| next learning turn | NUCLEO command matching versus side effect | Classify PING, MODE?, ARM, SET_RPM, and STOP by which variables they may change: app_mode, target_rpm, mode_change_count, or none. | WP-028 | open |
| next learning turn | NUCLEO DMA receive size/index | Explain why a future DMA callback should loop through `rx_buf[0..Size-1]` and call `AppFeedRxByte(...)` for each byte. | WP-029 | open |
| next learning turn | NUCLEO DMA + IDLE callback structure | Explain that DMA fills `rx_buf`, IDLE signals one batch is ready, CPU loops through `0..Size-1`, and reception must be restarted. | - | open |
| completed 2026-05-12 | NUCLEO UART command serial validation | Flash/run firmware, send PING, MODE?, ARM, STOP, SET_RPM abc, SET_RPM 999999, IDLE + SET_RPM 1200, and ARM + SET_RPM 1200 over COM5; capture a serial log proving responses and mode/target changes match the command table. | - | done |

## Review Cadence

- Keep the active queue small, normally 5-8 open items.
- Do not queue every next step; queue only real weak points or safety-critical checks.
- Same day: check whether the user can restate the concept.
- Next day: check a small problem or configuration decision.
- 3-7 days: check transfer to a new but similar situation.
- Before hardware/power actions: re-check safety-critical weak points.
