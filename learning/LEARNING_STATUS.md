# LEARNING_STATUS

Last updated: 2026-05-13

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
2. Read `learning/NEXT_LESSON.md` for the immediate teaching target when present.
3. Read `learning/MASTERY_MAP.md` so already-demonstrated basics are not drilled again without reason.
4. Read `workflow/current_learning_sprint.md`, `workflow/algo_b_teaching_delivery_plan.md`, and `workflow/teaching_contract.md` before continuing a lesson.
5. Start with a short progress checkpoint: current real stage, planned milestone, lesson target, deliverable, pace status, and forbidden scope.
6. Tie each lesson to a small submission or catch-up item so teaching keeps pace with the B algorithm plan.
7. Teach in plain language first: use a concrete analogy, the current board/code/log, or a small visible behavior before naming formal terms.
8. Explain new terms, concepts, and abbreviations before using them heavily.
9. For code lessons, use: feature sentence -> rule table -> function responsibilities -> C code -> test.
10. Explain only the minimum theory needed for the next action.
11. Add at least one teach-back or small practice question when useful.
12. Do not keep asking very simple repeated questions after the learner has clearly answered them; summarize the mastered point and move to the next practical step or a higher-value check.
13. Record observed weak points and next review work only when there is real evidence or a safety-critical check.
14. Do not claim mastery without evidence.
15. Prefer parking old low-risk weak points over letting every historical item stay in the active queue.

## Active Weak Point Summary

Current evidence includes L4 P1 concept checks for STOP side effects, DMA `Size` count/index, command side-effect reading, and DMA + IDLE callback flow, plus L5 serial-log validation for the NUCLEO command path. Active review should now focus on P2 MCSDK no-power artifact implementation rather than repeating early button/state-machine basics:

- Separating P2 no-power planning evidence from real MCSDK, Motor Profiler, Hall, power-board, or motor validation.
- Explaining why a generated or drafted config does not prove motor-control behavior.
- Resolving `PA2/PA3` UART-vs-OPAMP, `PC5` nFAULT-vs-OPAMP, and `PB3` SWO-vs-Hall pin conflicts before any generated project.
- Keeping Motor Profiler as a later hardware-stage plan with current limits, stop conditions, and abort criteria.

## Current Execution Layer

- Immediate lesson card: `learning/NEXT_LESSON.md`.
- Mastery / not-yet-mastery map: `learning/MASTERY_MAP.md`.
- Current sprint: `workflow/current_learning_sprint.md`.
- Sprint status: P2 no-power precheck started; current artifact has tool/status and pin/config draft evidence, but still needs Workbench/CubeMX or `.stmcx` evidence and pin-conflict resolution.
