# Weak Points

Track weak points only when there is evidence from the user's questions, mistakes, explanations, logs, code, measurements, or failed practice.

| ID | Topic | Evidence Level | Symptom | Repair Plan | Next Check | Status |
| --- | --- | --- | --- | --- | --- | --- |
| WP-022 | NUCLEO UART query command semantics | L3 | User can classify simple query commands and reported that the current read-only query questions are too simple. | Park low-value query drills for now; reopen only if later command work shows query/state-changing confusion. | Reopen before adding FAULT_CLEAR or another command whose side effects are ambiguous. | parked |
| WP-023 | NUCLEO ARM command state guard | L4 | User correctly predicted that RUN_SIM + ARM is rejected, leaves `app_mode` unchanged, and does not increment `mode_change_count`. | Keep as current-layer evidence; reopen only when a new start/arm command or real motor pre-run guard is introduced. | Reopen before mapping ARM to real voltage/current/nFAULT/PWM readiness checks. | parked |
| WP-024 | NUCLEO STOP command idempotence | L4 | User independently predicted both ARMED + STOP and IDLE + STOP final values, including unconditional target_rpm clear and conditional mode_change_count increment. | Use STOP as a branch-reading example instead of repeating the same table. | Reopen only if future command branches confuse unconditional side effects with guarded state changes. | parked |
| WP-027 | NUCLEO MODE query code reading | L3 | User identified the MODE? match and `printf("mode=... mode_name=...");` output evidence, then said the question was too simple. | Park current-layer MODE? drills; use the same code-reading method only in harder multi-line branches. | Reopen only if future query branch reading confuses output with state assignment. | parked |
| WP-028 | NUCLEO command matching versus side effect | L4 | User completed the current-layer DMA + IDLE callback flow: DMA fills `rx_buf`, UART IDLE marks a ready batch, CPU loops `i < Size` over `rx_buf[0..Size-1]`, bytes feed `AppFeedRxByte(...)`, and reception restarts. | Park current concept drill. Reopen when implementing or reviewing the real HAL callback, especially if command handling is placed in the callback or loop bounds slip. | Reopen during real callback implementation/validation. | parked |
| WP-029 | NUCLEO DMA receive size/index | L4 | User repaired the callback wording by explaining that `i` is the changing current index, `Size` is the total byte count for this batch, and indices start at 0. | Keep as current-layer evidence; use the rule inside the full callback flow instead of drilling standalone count/index again. | Reopen only if future callback code reading slips on `i < Size` or final index `Size - 1`. | parked |
| WP-000 | Learning loop startup | L0 | Bootstrap placeholder, not a real learner weak point. | Keep as historical marker only. | None. | parked |
| WP-001 | NUCLEO nonblocking tick scheduler | L1 | Earlier tendency to treat run success as mastery. | Revisit only if later scheduling work shows confusion. | Explain toggle interval versus full LED cycle if needed. | parked |
| WP-002 | NUCLEO multi-rate task counter | L1 | Non-integer task-rate ratios needed reinforcement. | Revisit only when adding another multi-rate task. | Predict counter changes for uneven periods if needed. | parked |
| WP-003 | NUCLEO B1 button event counter | L1 | Needed distinction between current button level and accumulated event count. | Revisit only if log interpretation slips. | Explain why `btn` can be 0 while `btn_press` is already higher. | parked |
| WP-004 | NUCLEO button edge detection and debounce | L1 | Needed current level versus historical event count clarification. | Covered by later state-machine debounce work. | Reopen only if one-press/many-count symptoms reappear. | parked |
| WP-005 | NUCLEO minimal app state machine | L1 | Needed event-gated transition and FAULT-safety framing. | Folded into command-guard work. | Revisit before real motor-control FAULT handling. | parked |
| WP-006 | NUCLEO state machine concept check | L1 | Needed explicit transition tables instead of ad hoc increment logic. | Baseline table work completed; keep as reference. | Reopen if table reading becomes fuzzy. | parked |
| WP-007 | NUCLEO explicit state transition table | L1 | Needed named states and source layout reinforcement. | Enum/source-layout work was practiced. | Revisit when introducing larger firmware modules. | parked |
| WP-008 | NUCLEO app mode labels | L1 | Needed separation of state labels from transition logic. | Later mode_name validation made this concrete. | Reopen only if labels and transitions get mixed again. | parked |
| WP-009 | NUCLEO mode number mapping | L1 | Needed mode-number-to-name mapping reinforcement. | User later mapped IDLE/ARMED/RUN_SIM correctly. | None unless logs become confusing again. | parked |
| WP-010 | NUCLEO enum placement intuition | L1 | Needed refine why fixed state dictionaries do not belong in repeated behavior code. | Keep for future source-layout lessons. | Revisit when moving helpers out of `main.c`. | parked |
| WP-011 | NUCLEO switch state transition | L1 | Needed remaining transition-table mapping. | Covered by full state-cycle practice. | Reopen only if switch cases become confusing. | parked |
| WP-012 | NUCLEO full state cycle | L1 | Needed default fallback framing. | Covered by later safe fallback discussion. | Revisit before adding FAULT state. | parked |
| WP-013 | NUCLEO default safe fallback | L1 | Needed safety idea that unknown state returns to safe state. | Keep as safety reference; not current drill. | Reopen before real FAULT recovery implementation. | parked |
| WP-014 | NUCLEO state machine formula teach-back | L1 | Needed no-event means no state change. | Now folded into UART command side-effect work. | Reopen if commands trigger unintended transitions. | parked |
| WP-015 | NUCLEO event-gated transition | L1 | Needed edge/debounce conditions around transition. | Keep as reference for command guard logic. | Reopen if event gates are bypassed. | parked |
| WP-016 | NUCLEO debounce as state-machine gate | L1 | Needed connect debounce failure to skipped modes. | Covered by multi-transition predictions. | Revisit when handling real button/noisy input. | parked |
| WP-017 | NUCLEO debounce multiple transition prediction | L1 | Needed understand accidental multi-step transitions. | Covered by follow-up prediction. | Reopen if symptoms show mode skipping. | parked |
| WP-018 | NUCLEO debounce three-transition prediction | L1 | Needed connect accidental multi-transition to motor-start safety. | Keep as safety reference. | Revisit before physical run controls. | parked |
| WP-019 | NUCLEO one-event-one-transition rule | L1 | Needed safety connection to skipped pre-run checks. | Folded into ARM guard work. | Reopen if one command/action causes multiple transitions. | parked |
| WP-020 | NUCLEO ARMED as pre-run check state | L1 | Needed specify checks before RUN. | Keep for later voltage/current/nFAULT/PWM readiness work. | Reopen before real motor startup sequence. | parked |
| WP-021 | NUCLEO mode-name serial validation | L5 | The readable mode log has already been used to move into UART receive/DMA+IDLE; avoid repeating simple mode-number mapping. | Keep as historical evidence and only reopen if serial log interpretation becomes confusing. | None unless mode/mode_name evidence is disputed. | parked |
| WP-025 | NUCLEO STOP from run-like state | L1 | Needed map safety wording to explicit IDLE. | Merged into WP-024 STOP idempotence. | Compare STOP transitions only if needed. | parked |
| WP-026 | NUCLEO STOP from ARMED state | L1 | Needed map safety wording to explicit IDLE. | Merged into WP-024 STOP idempotence. | Complete STOP table only if needed. | parked |

## Update Rules

- Do not add a weak point from guesswork alone.
- Prefer one precise weak point over a broad label.
- Include a concrete next check that can prove improvement.
- Park older low-risk weak points when they are no longer the next useful review.
- Close weak points only when the user shows strong evidence, normally L4 or above.
