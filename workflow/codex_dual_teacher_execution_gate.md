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
- Codex must not say that ChatGPT should do the current Codex-side repo work.

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
