# Learning Feedback Loop

This workflow turns teaching into persistent learning progress.

## Trigger

Use this workflow after any turn where Codex teaches, explains, checks homework, reviews code/logs as a learning exercise, or diagnoses a user's misunderstanding.

Do not use it for purely administrative tasks unless they reveal a learning gap.

## Before Teaching

Read, in this order when available:

1. `CURRENT_STATUS.md`
2. `learning/LEARNING_STATUS.md`
3. `learning/weak_points.md`
4. `learning/review_queue.md`

Use the active project stage and weak points to choose the depth of explanation.

## During Teaching

- Prefer one small executable task over broad theory.
- Tie concepts to STM32G474, MCSDK, FOC, STDRIVE101, ESP32-C3, or the current project artifact when possible.
- Use evidence levels L0-L6 from `learning/README.md`.
- Ask one teach-back or practice question when it would reveal whether the user actually understood.
- Mark safety-critical weak points clearly.

## After Teaching

Update learning memory when there is new evidence:

- Append a concise entry to `learning/session_notes.md`.
- Add or update rows in `learning/weak_points.md`.
- Add the next review prompt to `learning/review_queue.md`.
- Add reusable questions to `learning/question_bank.md` when a pattern repeats.

Prefer `python tools/record_learning_session.py` for simple append-only updates.

## Quality Bar

- Record what was observed, not what was guessed.
- Keep weak points specific enough to repair.
- Include the next check that can prove improvement.
- Do not claim mastery unless the user shows L4+ evidence.
- Do not let note-taking consume the lesson; one precise note is better than a long diary.
