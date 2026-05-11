# LEARNING_STATUS

Last updated: 2026-05-11

## Current Learning Mode

Project-centered FOC learning assistant mode.

The assistant should teach through small executable tasks, evidence checks, and follow-up review rather than long one-off explanations.

## Active Focus

- Build a reliable STM32G474 + NUCLEO/MCSDK/FOC foundation before advanced sensorless optimization.
- Keep hardware safety, measurement evidence, and toolchain reproducibility ahead of performance claims.
- Convert meaningful evidence into a short learning memory, but keep the active review queue small.

## Default Teaching Contract

For teaching or Q&A turns:

1. Start from the current project stage and the learner's known weak points.
2. Read `workflow/teaching_contract.md` before continuing a lesson.
3. Teach in plain language first: use a concrete analogy, the current board/code/log, or a small visible behavior before naming formal terms.
4. Explain new terms, concepts, and abbreviations before using them heavily.
5. For code lessons, use: feature sentence -> rule table -> function responsibilities -> C code -> test.
6. Explain only the minimum theory needed for the next action.
7. Add at least one teach-back or small practice question when useful.
8. Do not keep asking very simple repeated questions after the learner has clearly answered them; summarize the mastered point and move to the next practical step or a higher-value check.
9. Record observed weak points and next review work only when there is real evidence or a safety-critical check.
10. Do not claim mastery without evidence.
11. Prefer parking old low-risk weak points over letting every historical item stay in the active queue.

## Active Weak Point Summary

Current evidence is mainly L1-L2 from NUCLEO-G474RE baseline practice, plus one L5 serial-log validation. Active review should now focus on UART command handling rather than repeating early button/state-machine basics:

- Read-only query commands versus state-changing commands.
- Guarded transitions for ARM and idempotent STOP behavior.
- C string command matching with `strcmp(...) == 0`.
- Distinguishing branch conditions from side-effect assignments.
- UART line assembly: receive characters, detect newline, terminate string, dispatch command, handle overflow.
