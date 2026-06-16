# Learning Feedback Reference

Use this reference for teaching, concept confusion, homework review,
debugging-as-learning, weak-point updates, dual-teacher routing, or learning
record writes.

## Dual-Teacher Boundary

Concept-only role guard: theory, concepts, "I do not understand", "teach me",
"what should I learn", `我不懂`, `教我`, or `还要学什么` turns are ChatGPT
teaching turns when no repo file, command, build output, test, log, screenshot,
learning-record write, GitHub action, or hardware-safety state is needed.

For concept-only turns, Codex should provide:

1. A concrete ChatGPT prompt/task packet.
2. What the user should bring back to Codex.
3. The repo-side review or evidence step Codex will do after the user returns.

Codex still owns repo edits, verification, evidence recording, GitHub work, and
hardware-safety state.

## Four-Line Execution Gate

Before repo edits, command loops, artifact creation, or hardware-adjacent
answers for project-execution intents, output:

```text
项目目标：...
学习目标：...
修改范围：...
禁止范围：...
```

Then show the work as:

```text
功能句 -> 规则表 -> 函数职责 -> 代码修改或文档修改 -> 验证 -> 用户检查点
```

## Learning Records

When a turn reveals understanding, confusion, repeated mistakes, or a
safety-critical misconception, update the learning loop with short durable
records:

- `learning/session_notes.md`
- `learning/weak_points.md`
- `learning/review_queue.md`

Prefer:

```powershell
python tools/record_learning_session.py --topic "Hall sensors" --summary "..." --weak "..." --next "..."
python tools/normalize_learning_loop.py
```

Do not put every next step into `review_queue.md`. Queue observed weak points,
repeated misconceptions, safety-critical checks, or deliberately chosen
milestone reviews. Keep the active queue small, normally 5-8 open items.

## Evidence Levels

Use evidence levels L0-L6 from `learning/README.md`. Do not claim mastery
without L4 or higher evidence. A note, explanation, or retrieval hit is not a
mastery claim by itself.

## Teaching Style

- Start from concrete behavior: board signal, UART log, code line,
  measurement, or project artifact.
- Use the path: feature sentence -> rule table -> function responsibilities ->
  C code or pseudocode -> concrete test.
- Prefer one small executable step, one project link, and one useful check for
  understanding.
- Do not ask every open review item in one turn.
