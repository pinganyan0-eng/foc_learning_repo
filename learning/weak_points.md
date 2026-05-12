# Weak Points

Track weak points only when there is evidence from the user's questions, mistakes, explanations, logs, code, measurements, or failed practice.

| ID | Topic | Evidence Level | Symptom | Repair Plan | Next Check | Status |
| --- | --- | --- | --- | --- | --- | --- |
| WP-022 | NUCLEO UART query command semantics | L1 | User can classify MODE? as a query but needs reinforcement on separating read-only queries from state-changing commands. | Teach command side effects: MODE? and PING only report/acknowledge state; ARM and STOP request guarded transitions. | Classify PING, MODE?, ARM, STOP, and FAULT_CLEAR as read-only or state-changing. | open |
| WP-023 | NUCLEO ARM command state guard | L1 | ARM is understood as dangerous, but the exact rule still needs sharpening: ARM is valid from IDLE only. | Teach the transition table: IDLE + ARM -> ARMED; RUN_SIM + ARM -> reject/no state change. | Write the accepted transition for IDLE + ARM and rejected transition for RUN_SIM + ARM. | open |
| WP-024 | NUCLEO STOP command idempotence | L2 | User can explain that IDLE + STOP leaves mode_change_count unchanged, but initially predicted ARMED + STOP would keep mode ARMED before correction. | Teach the exact STOP execution path: first clear target_rpm, then IDLE branch reports unchanged, else branch sets app_mode to IDLE and increments mode_change_count. | Given ARMED,target_rpm=1200,count=5 and STOP, predict final mode,target_rpm,count; then compare with IDLE,target_rpm=1200,count=5 and STOP. | open |
| WP-027 | NUCLEO MODE query code reading | L1 | Need reinforce C code reading: `strcmp(cmd, "MODE?") == 0` performs command matching; `printf` produces the status response. | Read the MODE? branch line by line: match condition, format string, numeric mode argument, text mode argument. | Identify what `strcmp` returns when the command equals MODE?, and why `== 0` means matched. | open |
| WP-028 | NUCLEO command matching versus side effect | L2 | User identified assignment lines in ARM and STOP, and distinguished STOP's unconditional target clear from its conditional mode change; one branch-execution miss remains in ARMED + STOP. | Keep marking command branches with three labels: match condition, state/target side effects, and response-only printf lines. | Classify PING, MODE?, ARM, SET_RPM, and STOP by which variables they may change. | open |
| WP-029 | NUCLEO DMA receive size/index | L3 | User initially mixed up byte count with final zero-based index, then correctly solved guided checks: `Size = 10` means indices `0..9` and final index `9`. | Transfer the repaired rule into real callback code: DMA callback loops with `i < Size` and feeds `rx_buf[0..Size-1]` into the line parser. | Explain why a future DMA callback should loop through `rx_buf[0..Size-1]` and call `AppFeedRxByte(...)` for each byte. | open |
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
