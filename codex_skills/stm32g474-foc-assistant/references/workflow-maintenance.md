# Workflow Maintenance Reference

Use this reference for AI architecture, context packs, retrieval, contract
checks, project Skill edits, install flow, automation boundaries, closeout, or
repo-maintenance definition of done.

## Scope

Workflow maintenance may update:

- AI architecture docs and low-token handoff files.
- `tools/build_context_pack.py` modes.
- `tools/check_ai_contracts.py` contract checks.
- `tools/search_local_v2.py` retrieval priority or eval support.
- `retrieval_eval/queries.json` source-finding cases.
- Project Skill source under `codex_skills/`.
- Workflow indexes, closeout checklists, learning-loop contracts, and tool
  README entries.

Workflow maintenance must not edit firmware logic, generated projects,
CubeMX/MCSDK configuration, hardware parameters, DMM result tables, powered-test
evidence, or readiness claims.

## Automation Boundary

Automation jobs are read/report only unless the user explicitly authorizes a
repo-writing task.

Required phrase: `No repo writes`.

Automation must not commit, push, delete, reorder user work, edit generated
firmware, change hardware parameters, run powered tests, or claim hardware
readiness.

## Project Skill Maintenance

When updating `codex_skills/stm32g474-foc-assistant`:

1. Keep `SKILL.md` as a concise router.
2. Move task-specific detail to one-level `references/*.md` files.
3. Keep frontmatter to `name` and `description`.
4. Update `agents/openai.yaml` when display text becomes stale.
5. Extend `tools/check_ai_contracts.py` and tests when a new required Skill
   contract is introduced.
6. Validate the Skill folder:

```powershell
python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant
python tools/check_project_skill_install.py --repo-only --json
```

7. Install only after validation:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1
```

Restart Codex after installation if the updated Skill does not appear
immediately.

After installation, check drift:

```powershell
python tools/check_project_skill_install.py
```

This command is read-only. It compares the repo-local Skill files with the
installed user Skill and reports missing, extra, or changed installed files.

For a consolidated no-power maintenance audit, run:

```powershell
python tools/run_ai_maintenance_audit.py
python tools/run_ai_maintenance_audit.py --write-report workflow/ai_maintenance_audit_report.md
```

The audit records `git status --short` as dirty-worktree handoff evidence
before `git diff --check`; it does not clean, reorder, or validate the dirty
worktree. The `git_status` step preserves full output even when
`--max-output-chars` tail-limits other audit steps, and the report exposes a
parsed `workspace_status` summary with `status_paths`, `path_groups`, and
ordered `focus_groups`, plus `handoff_review_queue` review-focus items for
handoff. The report also exposes `contract_status` so future Codex turns can
distinguish contract errors from known review-lifecycle warnings and strict
readiness, and `closeout_summary` for the top-level repo-maintenance closeout
decision, dirty-worktree state, review-needed flag, and next review focus.

For a lightweight environment-independent audit, run:

```powershell
python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json
```

The `--write-report` output is repository-maintenance evidence only and must
not be treated as hardware validation.

`tools/check_ai_contracts.py` scans project truth, workflow, project Skill,
no-power precheck, deliverable, interface, and learning text for dangerous positive hardware claims such as DMM pass, Gate PWM readiness, powered
readiness, Hall readiness, motor readiness, power-stage readiness, or
sensorless readiness.

It also guards entry readability headers for
`workflow/evidence_register.md` and `deliverables/submission_checklist.md`.
This keeps the high-value AI handoff surface readable without treating all
legacy historical mojibake as silently repaired.

## Closeout Commands

Use the smallest meaningful subset, and use the full set before claiming a
workflow-maintenance task is complete:

```powershell
python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350
python tools/check_ai_contracts.py
python tools/check_project_skill_install.py
python tools/run_ai_maintenance_audit.py
python tools/build_vector_store.py
python tools/search_local_v2.py --eval
python -m unittest discover -s tests
python -m compileall src tests
git status --short
git diff --check
```

Passing these commands is repository-maintenance evidence only. It is not DMM,
firmware runtime, Gate PWM, Hall closed-loop, motor, power-stage, or sensorless
validation.

## Definition Of Done

For repo-maintenance tasks, make sure:

- `CURRENT_STATUS.md` records the dated decision and verification.
- `workflow/ACTIVE_TASK.md` records the task addendum or current task state.
- `workflow/evidence_register.md` has a matching evidence row when the task
  changes project truth.
- `docs/file_map.md`, `tools/README.md`, and low-token context entries point to
  the new maintenance surface.
- `tools/check_ai_contracts.py` has no errors.
- Known `done + Review Required` warnings are not silently cleared by Codex.
