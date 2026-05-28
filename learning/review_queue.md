# Review Queue

Use this as a lightweight spaced review queue. Each item should be small enough to check in 3-10 minutes.

| Due | Topic | Prompt | Source Weak Point | Status |
| --- | --- | --- | --- | --- |
| completed 2026-05-13 | MCSDK config evidence boundary | Explain what `.stmcx` can prove in P2, why compiled generated code still cannot prove motor safety, and why Motor Profiler remains a later hardware-stage action. | - | done |
| completed 2026-05-27 | Hall state-machine transition classification | Classify `100 -> 110`, `100 -> 101`, `100 -> 011`, `000`, and `111` using the current candidate sequence. | `learning/session_notes/2026-05-27_hall_state_machine_review_followup.md` | done |
| before software Hall firmware | Software Hall adapter processing order | Say the one-sentence rule: first read `PA0/PA1/PB4`, reject `000/111`, first valid state is only a baseline, repeated states do not count as edges, too-fast changes are bounce candidates, adjacent changes define direction candidates, and non-adjacent legal changes are abnormal jumps. | `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_processing_order_card_2026-05-27.md` | open |
| completed 2026-05-13 | MCSDK no-power artifact planning | List the P2 no-power artifacts and identify which later artifacts require real motor/power hardware. | - | done |
| P2-S1 P1 | MCSDK no-power artifact implementation | Continue from the saved NUCLEO-G474RE CubeMX `.ioc` draft, CubeMX `Pinout & Configuration` fallback screenshots, and Workbench entry probe: explain why MotorControl package data is not the same as a saved `.stmcx`, then add real MCSDK/Workbench `.stmcx` or MotorControl screenshot, CN8/EDA/netlist routing evidence, and STDRIVE101 `nFAULT` / `DT/MODE` / protection-path evidence. Skip basic toolchain navigation unless explicitly requested. | - | open |
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
