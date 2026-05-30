# AI Architecture

This page is the project-side architecture contract for AI assistance in this
repository. It explains how Codex, ChatGPT, local retrieval, workflow files,
learning memory, automation, and future probe scripts should cooperate without
weakening the hardware-safety evidence gates.

## Goal

The AI system should behave like a small evidence-first engineering operating
system. In short, it is an evidence-first engineering operating system:

```text
short context -> grounded retrieval -> task packet -> safe execution
-> evidence record -> learning update -> verification
```

The target is not more autonomous hardware action. The target is less repeated
context loading, better local search, clearer handoff, stronger static checks,
and more useful experiment analysis while keeping no-power boundaries explicit.

## Layers

| Layer | Current files or tools | Responsibility | Must not do |
| --- | --- | --- | --- |
| Fact source | `docs/00_project_truth/project_context.md`, `workflow/CURRENT_SNAPSHOT.md`, `CURRENT_STATUS.md` | Define current project truth, stage, and evidence-backed state. | Hide conflicts or promote historical notes over current evidence. |
| Context pack | `AI_CONTEXT.md`, future `tools/build_context_pack.py` | Produce the smallest useful task-specific context. | Read full manuals or long history by default. |
| Retrieval | `tools/ask_local.py`, `tools/build_vector_store.py` | Find local evidence and source snippets. | Treat retrieval hits as hardware validation. |
| Task control | `workflow/ACTIVE_TASK.md`, `workflow/task_state_machine.md`, `workflow/definition_of_done.md` | Keep one executable task, scope, and completion standard. | Execute `draft` tasks or bypass blocked tasks. |
| Safety gate | `workflow/risk_gate_matrix.md`, `workflow/phase_gate_checklist.md` | Protect PWM, 24V, power board, motor, Hall/SMO, and STDRIVE101 paths. | Claim powered readiness from config, build, screenshot, or generated source alone. |
| Learning memory | `learning/MASTERY_MAP.md`, `learning/weak_points.md`, `learning/review_queue.md` | Track observed understanding, weak points, and spaced review. | Claim mastery without evidence level L4 or higher. |
| Contract checks | future `tools/check_ai_contracts.py` | Detect broken links, missing safety phrases, stale tasks, and drift. | Replace human review for hardware evidence. |
| Probe scripts | future `tools/probes/` | Verify no-power file, toolchain, generated-source, and configuration facts. | Prove continuity, soldering, powered behavior, or motor safety. |
| Experiment analysis | future `tools/experiment_analyzer/`, `tools/uart_frame_tester/`, `tools/plot_current_speed/` | Parse logs and data into repeatable evidence and defense assets. | Turn a single noisy run into a stable performance claim. |

## Dual-Teacher Role Policy

- Concept-only role guard: theory, concept, "I do not understand", "teach me",
  "what should I learn", `我不懂`, `教我`, and `还要学什么` turns are ChatGPT
  teaching turns when no repo file, command, build output, test, log,
  screenshot, learning-record write, GitHub, or hardware-safety state is
  needed.
- Codex must not teach the full lesson for those turns. Codex provides a
  concrete ChatGPT prompt/task packet and says what should come back to Codex.
- If ChatGPT has GitHub write access, it may open a learning-evidence PR for a
  ChatGPT-taught concept lesson. That PR remains a teaching artifact until
  Codex syncs, reviews, verifies, and records it.
- Codex reviews and records returned learning evidence, updates the repo-side
  workflow when needed, and decides the next engineering step.
- Codex still owns real repository work: files, code, commands, build/test
  output, screenshots, evidence records, GitHub/PR work, and hardware-safety
  state.

## Read Policy

Default AI turns should read in this order:

1. `AI_CONTEXT.md`
2. `workflow/CURRENT_SNAPSHOT.md`
3. `workflow/ACTIVE_TASK.md`
4. `docs/00_project_truth/project_context.md`
5. Mode-specific context from `tools/build_context_pack.py`

Long files such as `CURRENT_STATUS.md`, `workflow/evidence_register.md`,
`materials/extracted/*`, `materials/raw/*`, and historical Packet records are
opened only for a concrete task that needs them.

## Retrieval Policy

Local retrieval remains useful because it is cheap, deterministic, and offline.
It should be upgraded in stages rather than deleted:

1. Keep the existing lexical index as the baseline.
2. Add source priority metadata, so current truth beats historical material.
3. Add a minimum score threshold and report "no reliable local hit" when needed.
4. Add a small retrieval evaluation set for known questions such as JEOC / ISR
   forbidden work, UART DMA + IDLE, Packet A, and Hall route boundaries.
5. Add optional embedding or reranking only after the deterministic checks pass.

Any retrieval-generated answer must show source paths and must preserve the
current safety boundary.

## Multi-Agent Policy

Multiple agents or subagents may be used only as read-only helpers unless a
specific task explicitly authorizes otherwise.

Allowed helper roles:

- Research helper: read official manuals or local references and summarize.
- Review helper: check whether a proposed task violates safety or evidence
  rules.
- Test helper: propose missing tests or static checks.

Only the main Codex execution path should write project truth files such as
`CURRENT_STATUS.md`, `workflow/ACTIVE_TASK.md`, `workflow/evidence_register.md`,
and `learning/*`.

## Automation Policy

Automations should stay cheap and conservative:

- Daily health checks may inspect task state, evidence links, review queue size,
  and dangerous claims.
- Weekly reviews may summarize evidence, gaps, weak points, and next actions.
- Experiment follow-ups may remind the user to attach logs, screenshots, CSV, or
  photos after a user-initiated test.

Automations must not commit, push, delete, reorder user work, edit generated
firmware, change hardware parameters, run powered tests, or claim hardware
readiness.

## Safety Boundary

Unless a later dated phase-gate decision explicitly opens the action:

- No flash.
- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Motor Pilot run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
- No powered readiness, motor readiness, or power-stage readiness claim.

Scripts, retrieval, generated-source review, local builds, screenshots, and
tool launches are no-power evidence only unless paired with the required
hardware evidence.

## First Implementation Batch

The first practical batch is intentionally small:

1. Add this architecture contract.
2. Add `workflow/CURRENT_SNAPSHOT.md` as the short current state.
3. Add `tools/build_context_pack.py` to produce task-specific context.
4. Add `tools/check_ai_contracts.py` to detect obvious workflow drift.
5. Add tests that keep these entries wired into the project.

Embedding search, subagents, probe scripts, and experiment analysis should come
after this foundation is stable.
