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

## AI Architecture v2

The v2 maintenance target is to make the AI workflow auditable rather than more
autonomous. It adds one maintenance context mode, stronger static checks, and
retrieval regression cases for the current safety-sensitive handoff questions.

- `tools/build_context_pack.py --mode ai_maintenance` is the default context
  pack for AI architecture, retrieval, workflow-contract, and handoff updates.
- `tools/build_context_pack.py --mode workflow_maintenance` is the default
  context pack for automation, learning-loop, closeout, definition-of-done,
  submission-checklist, and workflow-index maintenance.
- `tools/check_ai_contracts.py` is the no-power static contract checker. It
  checks entry files, safety phrases, task review lifecycle, UTF-8 readability,
  index coverage, retrieval-eval coverage, project workflow contracts, and
  dangerous positive claims across project truth, workflow, Skill, no-power
  precheck, deliverable, interface, and learning text. It also guards the
  readable entry headers of `workflow/evidence_register.md` and
  `deliverables/submission_checklist.md`, while leaving broader legacy
  mojibake cleanup as separately reviewed maintenance work.
- `retrieval_eval/queries.json` must include regression cases for the
  dual-teacher guard, current PCB2 Hall route, DMM pending/no-power boundary,
  ACTIVE_TASK review lifecycle, ESP32 real-time boundary, automation no-write
  boundary, learning feedback loop, closeout checklist, and repo-maintenance
  definition of done.
- `tools/search_local_v2.py --eval` verifies local retrieval behavior. Passing
  retrieval eval is source-finding evidence only, never hardware validation.
- `codex_skills/stm32g474-foc-assistant/SKILL.md` is the project Skill v2
  router. It keeps the loaded Skill concise and points to one-level references
  for project navigation, no-power boundaries, learning feedback, and workflow
  maintenance.
- `tools/check_project_skill_install.py` is the read-only install drift checker
  for the project Skill. It compares repo-local source with the installed user
  Skill and reports missing, extra, or changed files.
- `tools/run_ai_maintenance_audit.py` is the consolidated no-power AI
  maintenance audit runner. It can run the full closeout command set or a quick
  repo-only Skill/context/contract audit for handoff checks, and can write a
  human-readable Markdown report with `--write-report`. It records
  `git status --short` as dirty-worktree handoff evidence before
  `git diff --check`; the `git_status` step preserves full output even when
  other step output is tail-limited by `--max-output-chars`, and exposes a
  parsed `workspace_status` summary with `status_paths`, `path_groups`, and
  ordered `focus_groups`, plus `handoff_review_queue` review-focus items for
  handoff. It also exposes `contract_status`, a machine-readable summary of
  contract errors, review-lifecycle warnings, unexpected warnings,
  `strict_ready`, and `implementation_closeout_ok`, and `closeout_summary`,
  a top-level repo-maintenance closeout decision with dirty-worktree state,
  review-needed flag, next review focus, and explicit hardware-validation
  falsehood. This is not a cleanup or hardware validation step.

### Review Lifecycle Policy

The checker intentionally warns when `workflow/ACTIVE_TASK.md` is `done` while
`Review Required: yes` or pending verification remains. Codex must not clear
that warning by silently marking a task `reviewed`; user review clears strict warnings. Before that review, the acceptable implementation closeout is no
contract errors and only the known review-lifecycle warnings.

## Layers

| Layer | Current files or tools | Responsibility | Must not do |
| --- | --- | --- | --- |
| Fact source | `docs/00_project_truth/project_context.md`, `workflow/CURRENT_SNAPSHOT.md`, `CURRENT_STATUS.md` | Define current project truth, stage, and evidence-backed state. | Hide conflicts or promote historical notes over current evidence. |
| Context pack | `AI_CONTEXT.md`, `tools/build_context_pack.py` | Produce the smallest useful task-specific context, including `ai_maintenance` and `workflow_maintenance`. | Read full manuals or long history by default. |
| Retrieval | `tools/ask_local.py`, `tools/search_local_v2.py`, `tools/build_vector_store.py`, `retrieval_eval/queries.json` | Find local evidence and source snippets with regression coverage. | Treat retrieval hits as hardware validation. |
| Task control | `workflow/ACTIVE_TASK.md`, `workflow/task_state_machine.md`, `workflow/definition_of_done.md` | Keep one executable task, scope, and completion standard. | Execute `draft` tasks or bypass blocked tasks. |
| Safety gate | `workflow/risk_gate_matrix.md`, `workflow/phase_gate_checklist.md` | Protect PWM, 24V, power board, motor, Hall/SMO, and STDRIVE101 paths. | Claim powered readiness from config, build, screenshot, or generated source alone. |
| Learning memory | `learning/MASTERY_MAP.md`, `learning/weak_points.md`, `learning/review_queue.md` | Track observed understanding, weak points, and spaced review. | Claim mastery without evidence level L4 or higher. |
| Project Skill | `codex_skills/stm32g474-foc-assistant/SKILL.md`, `codex_skills/stm32g474-foc-assistant/references/*.md`, `tools/check_project_skill_install.py`, `tools/run_ai_maintenance_audit.py` | Route Codex turns to the right project truth, no-power boundary, learning loop, and workflow-maintenance rules with low token load; detect install drift after the repo-local Skill is installed; run consolidated no-power AI maintenance audits that include dirty-worktree status capture. | Hide detailed rules in an oversized Skill, install unreviewed external hardware-safety Skills, assume the installed Skill matches the repo without checking, clean or reorder user work during audit, or treat audit results as hardware validation. |
| Project workflow | `workflow/automation_playbook.md`, `workflow/learning_feedback_loop.md`, `workflow/session_close_checklist.md`, `workflow/definition_of_done.md` | Keep automation, learning updates, closeout, and repo-maintenance completion criteria auditable. | Let automation write repo state, skip closeout checks, or treat note-taking as evidence. |
| Contract checks | `tools/check_ai_contracts.py`, `tests/test_ai_architecture_contracts.py` | Detect missing entries, stale tasks, review lifecycle warnings, missing eval coverage, UTF-8 problems, and dangerous claims. | Replace human review for hardware evidence or self-clear required review. |
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

## Workflow Maintenance Policy

Project workflow maintenance is allowed to update context packs, contract
checks, retrieval regression cases, workflow indexes, learning-loop contracts,
automation boundaries, and closeout checklists. It remains a no-power repository
maintenance task.

Project Skill maintenance follows the same boundary. Keep
`codex_skills/stm32g474-foc-assistant/SKILL.md` as a concise router, move
task-specific detail into one-level references, validate with
`quick_validate.py` and `tools/check_project_skill_install.py --repo-only`,
and install only after repo-side checks pass. After installation, run
`tools/check_project_skill_install.py` to detect drift. Use
`tools/run_ai_maintenance_audit.py` for the full no-power closeout set or
`--quick --repo-only-skill --json` for handoff checks. Use `--write-report`
when a human-readable audit report is needed. The Skill may improve routing and
consistency, but it must not open hardware or firmware actions by itself.

The minimum accepted evidence for this class of work is:

- `tools/check_ai_contracts.py` has no errors.
- `tools/build_context_pack.py --mode workflow_maintenance` renders the
  expected source list.
- `tools/search_local_v2.py --eval` passes after rebuilding the local vector
  store.
- `python -m unittest discover -s tests`, `python -m compileall src tests`,
  `git status --short`, and `git diff --check` complete without new failures
  beyond known CRLF warnings; the status output is preserved as handoff
  context, not treated as a failure by itself.

Workflow maintenance must not edit firmware, generated projects, CubeMX/MCSDK
configuration, hardware parameters, DMM results, or powered-test evidence.

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
