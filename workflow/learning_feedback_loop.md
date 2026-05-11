# Learning Feedback Loop

This workflow turns teaching into persistent learning progress.

## Trigger

Use this workflow after any turn where Codex teaches, explains, checks homework, reviews code/logs as a learning exercise, or diagnoses a user's misunderstanding.

Do not use it for purely administrative tasks unless they reveal a learning gap.

## Before Teaching

Read, in this order when available:

1. `CURRENT_STATUS.md`
2. `workflow/teaching_contract.md`
3. `learning/LEARNING_STATUS.md`
4. `learning/weak_points.md`
5. `learning/review_queue.md`

Use the active project stage and weak points to choose the depth of explanation.

## During Teaching

- Prefer one small executable task over broad theory.
- Teach plainly before formally: start with a concrete analogy, visible board behavior, code line, UART log, or measurement, then introduce the technical term.
- Explain new terms, concepts, and abbreviations in plain language before using them in the lesson.
- For code lessons, use the sequence in `workflow/teaching_contract.md`: feature sentence -> rule table -> function responsibilities -> C code -> test.
- Tie concepts to STM32G474, MCSDK, FOC, STDRIVE101, ESP32-C3, or the current project artifact when possible.
- Use evidence levels L0-L6 from `learning/README.md`.
- Ask one teach-back or practice question when it would reveal whether the user actually understood.
- Avoid repeated low-value simple questions after the user has clearly answered the same pattern; batch the conclusion and move to practice, debugging, or the next meaningful concept.
- Mark safety-critical weak points clearly.

## After Teaching

Update learning memory when there is new evidence:

- Append a concise entry to `learning/session_notes.md`.
- Add or update rows in `learning/weak_points.md`.
- Add the next review prompt to `learning/review_queue.md`.
- Add reusable questions to `learning/question_bank.md` when a pattern repeats.

Prefer `python tools/record_learning_session.py` for simple append-only updates.
The script now assigns stable `WP-001` style IDs automatically when a weak point is recorded with the default `WP-new` placeholder.

After several learning turns, run:

```powershell
python tools/normalize_learning_loop.py
```

This keeps `learning/weak_points.md` and `learning/review_queue.md` sorted into their tables, replaces any temporary weak-point IDs, and updates review references.

Use the session helpers when useful:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\start_learning_session.ps1
powershell -ExecutionPolicy Bypass -File .\tools\end_learning_session.ps1 -Topic "topic" -Summary "what happened" -Weak "observed gap" -Next "next check"
```

On macOS/Linux:

```bash
bash tools/start_learning_session.sh
bash tools/end_learning_session.sh --topic "topic" --summary "what happened" --weak "observed gap" --next "next check"
```

## Quality Bar

- Record what was observed, not what was guessed.
- Keep weak points specific enough to repair.
- Include the next check that can prove improvement.
- Do not claim mastery unless the user shows L4+ evidence.
- Do not let note-taking consume the lesson; one precise note is better than a long diary.
