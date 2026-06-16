# Project Navigation Reference

Use this reference when a turn needs project routing, fact priority, context
selection, or command selection.

## Fact Priority

When project materials conflict, prefer facts in this order:

1. `docs/00_project_truth/project_context.md`
2. `CURRENT_STATUS.md` for current progress only
3. `workflow/CURRENT_SNAPSHOT.md` for low-token current handoff
4. `learning/` for learner state only
5. `materials/extracted/v9_final.txt`
6. `materials/extracted/tech_report_v1.txt`
7. Hardware risk notes, drive core notes, V8/V7.1, and workflow records
8. Old chats, temporary notes, early purchase lists

Dynamic external facts do not come from V9. Verify software versions, official
STM32/STDRIVE101/MCSDK details, component stock, competition dates, OpenAI or
Codex behavior, and hardware-risk parameters from official or high-trust
current sources before presenting them as current.

## Context Modes

- Use `codex_task` for the current executable repo task.
- Use `teaching` for learning turns that remain Codex-owned because they touch
  repo artifacts, logs, commands, learning records, or hardware-safety state.
- Use `hardware_review` for hardware-adjacent no-power evidence review.
- Use `mcsdk_packet` for Packet A/B/C, generated-source clues, build-only
  gates, or MCSDK evidence packets.
- Use `experiment_analysis` for logs, serial data, plots, or experiment records.
- Use `report_defense` for report, PPT, or defense claims.
- Use `ai_maintenance` for AI architecture, retrieval, handoff, and contract
  checker maintenance.
- Use `workflow_maintenance` for automation, learning feedback, closeout,
  definition of done, submission checklist, workflow index, and project Skill
  maintenance.

## Task Routing

- For repo edits, inspect current status and active task before implementation.
- For reviews, lead with concrete findings, file paths, and line references.
- For debugging, ask for measurable evidence: supply voltage/current limit,
  board version, CubeMX/MCSDK settings, firmware version, UART logs, nFAULT,
  and waveforms.
- For new materials, use `workflow/intake_checklist.md`, update current status
  and indexes when the material changes project state, then rebuild retrieval.
- For deliverables, treat unmeasured performance claims as hypotheses and tie
  each claim to evidence.

## Minimum Useful Commands

```powershell
python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350
python tools/ask_local.py "your question"
python tools/build_vector_store.py
python tools/search_local_v2.py --eval
python tools/check_ai_contracts.py
python -m unittest discover -s tests
python -m compileall src tests
git diff --check
```

Do not treat any command above as powered or hardware validation.
