# V9 Errata

This file records project-truth corrections for conflicts found inside
`materials/extracted/v9_final.txt`. These corrections override the raw V9 text
for the listed items, but they do not authorize wiring, flashing, powered tests,
Motor Profiler, or motor operation.

## 2026-05-19: PC5 nFAULT Conflict

Decision: reject `PC5` as the `nFAULT` / break-input pin for P2. Keep
`PB12 / TIM1_BKIN` as the current no-power draft candidate only.

Why:

- V9 lists `nFAULT` as `PC5 / CN10-6 / EXTI5`.
- The same V9 table lists `OPAMP2 VINM0 = PC5`.
- The same V9 OPAMP note says that in PGA mode the external `VINM` pins
  `PA3 / PC5 / PB2` must be left floating.
- `nFAULT` is a pulled-up, externally driven STDRIVE101 fault signal, so it
  cannot share a pin that the same plan requires to remain floating for OPAMP2
  PGA feedback.

Current repository policy:

- `PC5` is unavailable for `nFAULT` unless a future written exception resolves
  the OPAMP/PGA conflict, timer-break behavior, and board routing evidence.
- `PB12 / TIM1_BKIN` remains the preferred draft candidate because later P2
  review and current PCB2 mapping sources point `nFAULT` toward `PB12`.
- This is still not a hardware-valid route. Before use, Packet A must show the
  selected Workbench/CubeMX break input, and Packet C must prove the board route
  from STDRIVE101 `nFAULT` through the connector to the STM32 pin.

Repo evidence:

- Raw V9 conflict: `materials/extracted/v9_final.txt` lines 688-692 and
  768-780.
- Draft decision: `apps/stm32_g474_foc/mcsdk_no_power_precheck/config_draft.md`.
- Acceptance rule: `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md`.
- Current PCB2 mapping clue:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md`.
