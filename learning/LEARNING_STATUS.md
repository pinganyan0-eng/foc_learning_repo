# LEARNING_STATUS

Last updated: 2026-05-11

## Current Learning Mode

Project-centered FOC learning assistant mode.

The assistant should teach through small executable tasks, evidence checks, and follow-up review rather than long one-off explanations.

## Active Focus

- Build a reliable STM32G474 + NUCLEO/MCSDK/FOC foundation before advanced sensorless optimization.
- Keep hardware safety, measurement evidence, and toolchain reproducibility ahead of performance claims.
- Convert every meaningful lesson into weak-point tracking and review prompts.

## Default Teaching Contract

For teaching or Q&A turns:

1. Start from the current project stage and the learner's known weak points.
2. Teach in plain language first: use a concrete analogy, the current board/code/log, or a small visible behavior before naming formal terms.
3. Explain only the minimum theory needed for the next action.
4. Add at least one teach-back or small practice question when useful.
5. Do not keep asking very simple repeated questions after the learner has clearly answered them; summarize the mastered point and move to the next practical step or a higher-value check.
6. Record observed weak points and next review work.
7. Do not claim mastery without evidence.

## Active Weak Point Summary

Current evidence is mainly L1 from NUCLEO-G474RE baseline practice. Active review should focus on:

- Nonblocking tick scheduling and the difference between toggle interval and full LED cycle.
- Multi-rate task counters, especially fractional average rates versus discrete counter changes.
- B1 button edge detection, debounce, and the distinction between current level and historical event count.
- Event-gated state transitions, explicit transition tables, and safe FAULT recovery logic.
- Embedded source layout: keep state definitions near top-level declarations instead of inside executable code blocks.
