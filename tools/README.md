# Tools

## AI Architecture v2 Maintenance

- `python tools/build_context_pack.py --mode ai_maintenance --max-chars 350`
  builds the low-token handoff for AI workflow maintenance.
- `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`
  builds the low-token handoff for project workflow, automation, learning-loop,
  closeout, definition-of-done, and submission-checklist maintenance.
- `python tools/check_ai_contracts.py` checks AI entry files, safety phrases,
  review lifecycle, index coverage, retrieval-eval coverage, UTF-8 readability,
  project workflow contracts, and dangerous positive hardware claims across
  project truth, workflow, Skill, no-power precheck, deliverable, interface,
  and learning text. It also guards entry readability headers for
  `workflow/evidence_register.md` and `deliverables/submission_checklist.md`;
  this prevents header/template regression without claiming that all legacy
  historical rows have been repaired.
- `python tools/check_ai_contracts.py --strict` is the post-review target.
  User review clears strict warnings; Codex must not self-clear a required
  review.
- `python tools/search_local_v2.py --eval` runs local retrieval regression
  cases from `retrieval_eval/queries.json`. Passing eval is source-finding
  evidence only, not hardware validation.
- `codex_skills/stm32g474-foc-assistant/SKILL.md` is the project Skill v2
  router. Its references cover project navigation, no-power boundaries,
  learning feedback, and workflow maintenance.
- `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`
  validates the project Skill folder before installation.
- `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`
  installs the repo-local project Skill into the user Codex skills directory.
  Restart Codex after install if the updated Skill does not appear immediately.
- `python tools/check_project_skill_install.py` compares the repo-local project
  Skill with the installed user Skill and reports install drift.
- `python tools/check_project_skill_install.py --repo-only --json` validates
  only the repo-local project Skill source and is safe for tests or CI.
- `python tools/run_ai_maintenance_audit.py` runs the full no-power AI
  maintenance audit: Skill validation, install drift check, context pack,
  AI contracts, vector-store rebuild, retrieval eval, unit tests, compileall,
  `git status --short` dirty-worktree handoff capture, and `git diff --check`.
  The audit preserves full `git_status` output even when other step output is
  tail-limited by `--max-output-chars`, and exposes a parsed
  `workspace_status` summary with dirty state, total entry count, status-code
  counts, `status_paths` status-code path lists, path groups by repository
  area, `focus_groups` ordered handoff groups, `handoff_review_queue` review
  focus items, `contract_status` review-lifecycle warning summaries,
  `closeout_summary` for the top-level repo-maintenance closeout decision,
  paths, and items.
- `python tools/run_ai_maintenance_audit.py --write-report workflow/ai_maintenance_audit_report.md`
  writes a human-readable Markdown report for handoff or review, including a
  `Closeout Summary` section.
- `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json`
  runs a lightweight environment-independent audit for tests or handoff checks:
  repo-local Skill, context pack, AI contracts, and `git status --short`.

- `build_vector_store.py`：构建本地检索索引。
- `ask_local.py`：基于本地资料问答。
- `search_local_v2.py`：带最低分阈值、事实源优先级、查询扩展和检索评测的本地证据检索。
- `build_context_pack.py`：按任务模式生成低 token 上下文包，避免每次读取长历史文件；`workflow_maintenance` 覆盖自动化、学习闭环、收工、DoD 和上交清单维护。
- `check_ai_contracts.py`：检查 AI 架构入口、当前任务、安全边界、学习队列、项目工作流契约和索引是否漂移。
- `record_learning_session.py`：追加学习记录，并在出现薄弱点时自动分配稳定 `WP-001` 编号。
- `normalize_learning_loop.py`：整理 `learning/weak_points.md` 与 `learning/review_queue.md`，修复临时 `WP-new` 引用。
- `start_learning_session.ps1` / `start_learning_session.sh`：开工入口，更新项目 Skill、整理学习队列、显示当前状态与复习项。
- `end_learning_session.ps1` / `end_learning_session.sh`：收工入口，记录学习摘要、整理学习队列、重建检索索引并跑测试。
- `sync_project.ps1` / `sync_project.sh`：Windows/Mac 双机同步入口；`push` 前会整理学习队列、重建检索索引并跑测试。
- `run_rehearsal.py`：Suggest -> Auto Edit -> 验证 -> 回滚演练。
- `log_parser/`：后续放串口日志解析工具。
- `plot_current_speed/`：后续放电流/速度画图工具。
- `uart_frame_tester/`：后续放 UART 帧测试工具。
