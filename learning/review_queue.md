# Review Queue

Use this as a lightweight spaced review queue. Each item should be small enough to check in 3-10 minutes.

| Due | Topic | Prompt | Source Weak Point | Status |
| --- | --- | --- | --- | --- |
| completed 2026-05-13 | MCSDK config evidence boundary | Explain what `.stmcx` can prove in P2, why compiled generated code still cannot prove motor safety, and why Motor Profiler remains a later hardware-stage action. | - | done |
| completed 2026-05-13 | MCSDK no-power artifact planning | List the P2 no-power artifacts and identify which later artifacts require real motor/power hardware. | - | done |
| P2-S1 P1 | MCSDK no-power artifact implementation | Finish the P2 card by adding Workbench/CubeMX or `.stmcx` evidence, confirming `PB12/TIM1_BKIN` nFAULT and `PB14/TIM1_CH2N` against board routing, and expanding the Motor Profiler stop-condition plan without running hardware. | - | open |
| completed 2026-05-13 | STDRIVE101 local source digestion | Add the official STDRIVE101 datasheet to the repo-local ST mirror, extract searchable text, and record hash/official URL before using it for power-stage protection decisions. | - | done |
| completed 2026-05-13 | NUCLEO DMA + IDLE callback structure | Explain that DMA fills `rx_buf`, UART IDLE means one batch is ready, CPU loops through `0..Size-1`, feeds `AppFeedRxByte(...)`, and reception must be restarted. | - | done |
| completed 2026-05-12 | NUCLEO UART command serial validation | Flash/run firmware, send PING, MODE?, ARM, STOP, SET_RPM abc, SET_RPM 999999, IDLE + SET_RPM 1200, and ARM + SET_RPM 1200 over COM5; capture a serial log proving responses and mode/target changes match the command table. | - | done |

## Review Cadence

- Keep the active queue small, normally 5-8 open items.
- Do not queue every next step; queue only real weak points or safety-critical checks.
- Same day: check whether the user can restate the concept.
- Next day: check a small problem or configuration decision.
- 3-7 days: check transfer to a new but similar situation.
- Before hardware/power actions: re-check safety-critical weak points.
