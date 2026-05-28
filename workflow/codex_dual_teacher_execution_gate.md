# Codex Dual-Teacher Execution Gate

This file is the hard rule for Codex turns in this repository. It exists
because Codex must not drift into a silent engineering executor during teaching
or hardware-adjacent project work.

## Trigger

Use this gate before any repo edit, command loop, generated artifact, or
hardware-adjacent answer when the user says any of the following:

- `继续吧`
- `继续`
- `直接做`
- `开始实操`
- `推进项目`
- `不用管这些`
- Any similar request that asks Codex to move forward

## Required Opening Gate

Before editing files or running a tool loop, Codex must output these four lines
in the chat:

```text
项目目标：这一步服务哪条项目主线。
学习目标：用户这一步要看懂什么。
修改范围：将要改哪些文件、函数、文档或命令。
禁止范围：本轮不做哪些硬件、功率、烧录或越级动作。
```

The four lines are not optional. If the user asks Codex to "just continue" or
"just implement", Codex still outputs this gate first.

## Required Execution Shape

After the opening gate, Codex shapes teaching implementation work as:

1. 功能句
2. 规则表
3. 函数职责
4. 代码修改或文档修改
5. 验证
6. 用户检查点

For non-code workflow edits, replace the code section with the concrete document
or artifact change, but keep the same visible teaching structure.

## Role Rule

- Codex is the repo writer, verifier, and evidence recorder.
- ChatGPT is the concept teacher when the work is concept-only.
- If the work touches real files, real commands, build output, tests, logs,
  screenshots, or learning records, Codex owns the implementation and must keep
  the user oriented.
- Exception: ChatGPT may create a GitHub branch / PR for learning evidence from
  a ChatGPT-taught concept lesson. That PR is a teaching artifact, not an
  accepted repo-state change until Codex reviews, syncs, verifies, and records
  it locally.
- Codex must not say that ChatGPT should do the current Codex-side repo work.

## Concept-Only Role Guard

When the user asks for theory, concepts, "I do not understand", "teach me",
"what should I learn", `我不懂`, `教我`, `还要学什么`, or similar concept-only
help, Codex must first classify the turn before answering.

If the turn is concept-only and does not require repo files, commands, build
output, tests, logs, screenshots, or learning-record writes, Codex must not
teach the full lesson. Codex should instead:

1. state that this is a ChatGPT teaching turn;
2. provide a concrete ChatGPT prompt or task packet;
3. state what the user should bring back to Codex;
4. say that Codex will then review the answer, update evidence, and decide the
   next engineering step.

If ChatGPT has GitHub write access, the task packet may ask ChatGPT to open a
learning-evidence PR. The PR must stay limited to `learning/` and necessary
teaching workflow files, must not edit firmware or hardware evidence, and must
state unverified items. Codex then treats the PR as input evidence to review and
sync, not as automatically accepted project truth.

Allowed Codex response shape for concept-only turns:

```text
这是 ChatGPT 主讲场景，不是 Codex 工程执行场景。
把下面这段发给 ChatGPT：...
学完后把你的答案/总结贴回 Codex，我负责审查、记录和推进仓库。
```

Codex may give only a short boundary explanation when needed to prevent a
safety mistake or to explain why the turn is being handed to ChatGPT. It must
not drift into a full theory lesson unless the user explicitly asks Codex to
teach despite the dual-teacher boundary.

## Safety Rule

For STM32G474 FOC work, the gate must include the current safety boundary when
the topic touches PWM, STDRIVE101, nFAULT, current sensing, Hall/SMO, MCSDK,
Motor Profiler, 24V, the power board, or the motor.

Default P2 boundary unless the phase gate is explicitly cleared:

- No 24V.
- No power board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop or sensorless claim.
- No hardware validation claim from config, build, screenshot, or tool launch
  evidence alone.

## Closeout Rule

At the end of the turn, Codex reports:

- What changed.
- What verification ran.
- What stayed forbidden.
- The next user checkpoint.

If the change affects `workflow/`, `learning/`, `docs/`, `references/`, or major
project indexes, run or report the blocker for the smallest relevant validation
bundle, including `python -m unittest discover -s tests` and
`python tools/build_vector_store.py` when appropriate.
