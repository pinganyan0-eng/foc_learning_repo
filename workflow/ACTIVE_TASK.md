# Current Task

This is the current single task. It records the no-power software Hall firmware
entry plan for the future `PA0/PA1/PB4` adapter. It is not STM32 firmware
implementation, not generated-code editing, not CubeMX / Workbench editing,
not flashing, not Run / Debug, not hardware validation, and not powered
testing.

## Current 2026-06-17 AI Maintenance Audit Readability Status Addendum

- Task:
  `TASK-2026-06-17-ai-maintenance-audit-readability-status`.
- Evidence:
  `EV-2026-06-17-AI-MAINTENANCE-AUDIT-READABILITY-STATUS-001`.
- Decision:
  `AI maintenance audit readability status / entry-header versus legacy-debt handoff / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with
  `readability_status_from_repo()`, `readability_header_status_from_repo()`,
  and `readability_legacy_debt_status_from_repo()`. The audit now exposes
  top-level `readability_status` with `entry_headers_ok`,
  `guarded_entry_files`, `legacy_debt_present`, `legacy_debt_count`,
  `legacy_debt_paths`, `full_legacy_cleanup_claimed`, and
  `hardware_validation: false`. Updated contract checks, tests, retrieval
  expansion/eval, low-token docs, file index, tools README, and project Skill
  workflow-maintenance reference.
- Verification:
  passed with
  `python -m py_compile tools\run_ai_maintenance_audit.py tools\check_ai_contracts.py tools\search_local_v2.py tests\test_ai_architecture_contracts.py`,
  `python -m unittest tests.test_ai_architecture_contracts`,
  `python tools\check_ai_contracts.py` with 0 errors and the two known
  review-lifecycle warnings,
  `python tools\build_vector_store.py`,
  `python tools\search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git diff --check` with only existing CRLF conversion warnings,
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`,
  `python tools\check_project_skill_install.py --repo-only --json`,
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`,
  `python tools\check_project_skill_install.py`,
  `python tools\build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  and `python tools\run_ai_maintenance_audit.py --json --max-output-chars 700`.
  The full audit returned `ok: true`, `repo_maintenance_closeout_ok: true`,
  `readability_status.entry_headers_ok: true`,
  `readability_status.legacy_debt_present: true`, and
  `hardware_validation: false`.
- Boundary:
  `readability_status` is repo-text handoff evidence only. It separates the
  guarded entry headers from broader legacy mojibake debt and does not claim
  full historical cleanup, inspect hardware, run firmware, clean the worktree,
  or validate readiness. No DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-10 Entry Readability Contract Addendum

- Task:
  `TASK-2026-06-10-entry-readability-contract`.
- Evidence:
  `EV-2026-06-10-ENTRY-READABILITY-CONTRACT-001`.
- Decision:
  `High-value entry readability repair / UTF-8 header contract / no hardware or firmware action`.
- Scope:
  restored the readable entry header and weekly/phase template fields in
  `deliverables/submission_checklist.md`, restored the title and evidence
  boundary in `workflow/evidence_register.md`, and extended
  `tools/check_ai_contracts.py` with `READABILITY_HEADER_REQUIREMENTS`,
  `READABILITY_MOJIBAKE_MARKERS`, and `check_readability_headers()`. Added
  unit coverage, retrieval expansion/eval, architecture/index/tool docs, and
  project Skill workflow-maintenance guidance.
- Verification:
  passed with
  `python -m py_compile tools\check_ai_contracts.py tools\search_local_v2.py`,
  `python -m unittest tests.test_ai_architecture_contracts`,
  `python tools/check_ai_contracts.py` with 0 errors and the two known
  review-lifecycle warnings,
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`,
  `python tools/check_project_skill_install.py --repo-only --json`,
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`,
  `python tools/check_project_skill_install.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest tests.test_search_local_v2 tests.test_ai_architecture_contracts tests.test_workflow_contracts`,
  and `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
  The full audit passed with 143 discovered tests, retrieval eval, compileall,
  Skill install drift check, `closeout_summary.repo_maintenance_closeout_ok:
  true`, and `git diff --check`; diff check output only contained existing
  CRLF conversion warnings.
- Boundary:
  this repairs and guards the high-value entry headers only. It does not claim
  that every legacy historical mojibake row is repaired, change task state,
  inspect hardware, run firmware, or validate readiness. No DMM table fill, no
  firmware implementation, no generated-code edit, no CubeMX/MCSDK edit, no
  flash, no 24V, no power-board connection, no motor connection, no Gate PWM,
  no Motor Profiler, no Hall closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-10 AI Maintenance Audit Closeout Summary Addendum

- Task:
  `TASK-2026-06-10-ai-maintenance-audit-closeout-summary`.
- Evidence:
  `EV-2026-06-10-AI-MAINTENANCE-AUDIT-CLOSEOUT-SUMMARY-001`.
- Decision:
  `AI maintenance audit closeout summary / top-level repo-maintenance handoff / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with
  `closeout_summary_from_statuses()` and top-level `closeout_summary`. The
  summary reports `repo_maintenance_closeout_ok`, `strict_ready`,
  `needs_user_review`, dirty-worktree state, dirty entry count, next review
  group/focus, `no_power_boundary_active`, and `hardware_validation: false`.
  Updated tests, contract checks, retrieval eval, low-token docs, file index,
  tools README, and project Skill workflow-maintenance reference.
- Verification:
  passed with
  `python -m py_compile tools\run_ai_maintenance_audit.py tools\check_ai_contracts.py tools\search_local_v2.py`,
  `python -m unittest tests.test_ai_architecture_contracts`,
  `python tools/check_ai_contracts.py` with 0 errors and the two known
  review-lifecycle warnings,
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`,
  `python tools/check_project_skill_install.py --repo-only --json`,
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`,
  `python tools/check_project_skill_install.py`,
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest tests.test_search_local_v2 tests.test_ai_architecture_contracts`,
  and `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
  The full audit passed with `closeout_summary.repo_maintenance_closeout_ok:
  true`, `strict_ready: false`, `needs_user_review: true`, 0 contract errors,
  0 unexpected warnings, 2 known review-lifecycle warnings, 142 discovered unit
  tests, compileall, Skill install drift check, retrieval eval, and
  `git diff --check`; diff check output only contained existing CRLF
  conversion warnings.
- Boundary:
  `closeout_summary` is derived from audit outputs only. It does not
  self-clear required review, change task state, inspect hardware, run
  firmware, clean the worktree, or validate readiness. No external GitHub Skill
  install, no DMM table fill, no firmware implementation, no generated-code
  edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no
  motor connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-10 AI Maintenance Audit Contract Status Addendum

- Task:
  `TASK-2026-06-10-ai-maintenance-audit-contract-status`.
- Evidence:
  `EV-2026-06-10-AI-MAINTENANCE-AUDIT-CONTRACT-STATUS-001`.
- Decision:
  `AI maintenance audit contract status / review-lifecycle warning classification / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with
  `REVIEW_LIFECYCLE_WARNING_MARKERS`, `parse_contract_output()`, and
  `contract_status_from_results()`. The audit now exposes top-level
  `contract_status` with error and warning counts, review-lifecycle warning
  count, unexpected warning count, `strict_ready`, and
  `implementation_closeout_ok`. Markdown reports now include a `Contract
  Status` section. Updated tests, retrieval eval, low-token docs, file index,
  tools README, and project Skill workflow-maintenance reference. Added
  `MAINTENANCE_SOURCE_FILES` in `tools/build_vector_store.py` so maintenance
  tool scripts, tests, and eval JSON stay indexed for local retrieval. Updated
  `tools/search_local_v2.py` with path-aware topic-entry scoring so workflow
  entry files and the `tools/check_ai_contracts.py` dangerous-claim
  implementation remain discoverable after status/evidence docs grow.
- Verification:
  passed with
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  `python tools/check_ai_contracts.py` with 0 errors and the two known
  review-lifecycle warnings, `python tools/check_project_skill_install.py`,
  `python tools/build_vector_store.py`, `python tools/search_local_v2.py --eval`,
  `python -m unittest tests.test_search_local_v2 tests.test_ai_architecture_contracts`
  with 18 tests OK, and
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
  The full audit passed with retrieval eval, 142 discovered unit tests,
  compileall, Skill install drift check, and `git diff --check`; diff check
  output only contained existing CRLF conversion warnings.
- Boundary:
  `contract_status` is a parsed contract-output handoff summary only. It does
  not self-clear required review, change task state, inspect hardware, run
  firmware, clean the worktree, or validate readiness. No external GitHub Skill
  install, no DMM table fill, no firmware implementation, no generated-code
  edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no
  motor connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 Dangerous Claim Scan Surface Addendum

- Task:
  `TASK-2026-06-09-ai-contract-dangerous-claim-scan-surface`.
- Evidence:
  `EV-2026-06-09-AI-CONTRACT-DANGEROUS-CLAIM-SCAN-SURFACE-001`.
- Decision:
  `AI contract dangerous claim scan surface / broader no-power static text scan / no hardware or firmware action`.
- Scope:
  extended `tools/check_ai_contracts.py` with `DANGEROUS_CLAIM_SCAN_PATHS`,
  `DANGEROUS_CLAIM_SCAN_SUFFIXES`, `is_dangerous_claim_scan_candidate()`, and
  `iter_dangerous_claim_scan_files()`, so dangerous positive hardware claims
  are scanned across project truth, workflow, project Skill, no-power
  precheck, deliverable, interface, and learning text rather than only a few
  entry files. Updated tests, retrieval eval, docs, and project Skill
  workflow-maintenance reference.
- Verification:
  `python tools/check_ai_contracts.py`,
  targeted dangerous-claim-scan tests in
  `tests/test_ai_architecture_contracts.py`,
  `python tools/build_vector_store.py`,
  `python -m json.tool retrieval_eval\queries.json`,
  targeted `rg` dangerous-phrase sweep across the scanned maintenance surface,
  `python tools/search_local_v2.py --eval`,
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`,
  `python tools/check_project_skill_install.py --repo-only --json`,
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`,
  `python tools/check_project_skill_install.py`,
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  and `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
- Boundary:
  this is a static text scan only; it does not inspect hardware, run firmware,
  clean the worktree, or validate readiness. No external GitHub Skill install,
  no DMM table fill, no firmware implementation, no generated-code edit, no
  CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no motor
  connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 AI Maintenance Audit Handoff Review Queue Addendum

- Task:
  `TASK-2026-06-09-ai-maintenance-audit-handoff-review-queue`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-HANDOFF-REVIEW-QUEUE-001`.
- Decision:
  `AI maintenance audit handoff review queue / group-specific dirty-worktree review focus / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with `GROUP_REVIEW_FOCUS` and
  `build_handoff_review_queue()`, added
  `workspace_status.handoff_review_queue`, added Markdown
  `Handoff Review Queue` output, and updated tests, contracts, retrieval,
  docs, and project Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --check git_status --json --max-output-chars 1`,
  targeted audit tests in `tests/test_ai_architecture_contracts.py`,
  `python tools/check_ai_contracts.py`,
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`,
  `python tools/check_project_skill_install.py --repo-only --json`,
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`,
  `python tools/check_project_skill_install.py`,
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  and `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
- Boundary:
  `handoff_review_queue` is parsed handoff guidance only; it does not hide,
  clean, reorder, revert, stage, commit, or validate the dirty worktree. No
  external GitHub Skill install, no DMM table fill, no firmware
  implementation, no generated-code edit, no CubeMX/MCSDK edit, no flash, no
  24V, no power-board connection, no motor connection, no Gate PWM, no Motor
  Profiler, no Hall closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 AI Maintenance Audit Focus Groups Addendum

- Task:
  `TASK-2026-06-09-ai-maintenance-audit-focus-groups`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-FOCUS-GROUPS-001`.
- Decision:
  `AI maintenance audit focus groups / ordered dirty-worktree handoff / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with `GROUP_FOCUS_ORDER` and
  `summarize_focus_groups()`, added `workspace_status.focus_groups`, added
  Markdown `Focus Groups` output, and updated tests, contracts, retrieval,
  docs, and project Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`,
  `python tools/check_project_skill_install.py`,
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git status --short`, and `git diff --check`.
- Boundary:
  `focus_groups` are parsed handoff evidence only; they do not hide, clean,
  reorder, revert, stage, commit, or validate the dirty worktree. No external
  GitHub Skill install, no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 AI Maintenance Audit Status Paths Addendum

- Task:
  `TASK-2026-06-09-ai-maintenance-audit-status-paths`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-STATUS-PATHS-001`.
- Decision:
  `AI maintenance audit status paths / status-code dirty-worktree handoff / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with
  `summarize_status_paths()` and `workspace_status.status_paths`, added
  Markdown `Status Paths` output, and updated tests, contracts, retrieval,
  docs, and project Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`,
  `python tools/check_project_skill_install.py`,
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git status --short`, and `git diff --check`.
- Boundary:
  `status_paths` are parsed handoff evidence only; they do not hide, clean,
  reorder, revert, stage, commit, or validate the dirty worktree. No external
  GitHub Skill install, no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 AI Maintenance Audit Workspace Path Groups Addendum

- Task:
  `TASK-2026-06-09-ai-maintenance-audit-workspace-path-groups`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-WORKSPACE-PATH-GROUPS-001`.
- Decision:
  `AI maintenance audit workspace path groups / repository-area dirty-worktree handoff / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with
  `classify_path_group()` and `workspace_status.path_groups`, added Markdown
  `Path Groups` output, and updated tests, contracts, retrieval, docs, and
  project Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`,
  `python tools/check_project_skill_install.py`,
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git status --short`, and `git diff --check`.
- Boundary:
  `path_groups` are parsed handoff evidence only; they do not hide, clean,
  reorder, revert, stage, commit, or validate the dirty worktree. No external
  GitHub Skill install, no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 AI Maintenance Audit Workspace Status Addendum

- Task:
  `TASK-2026-06-09-ai-maintenance-audit-workspace-status-summary`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-WORKSPACE-STATUS-SUMMARY-001`.
- Decision:
  `AI maintenance audit workspace-status summary / machine-readable dirty-worktree handoff / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with
  `parse_git_status_short()` and a top-level `workspace_status` object derived
  from the existing full `git_status` output. Updated Markdown report output,
  tests, contracts, retrieval, docs, and project Skill workflow-maintenance
  reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`,
  `python tools/check_project_skill_install.py`,
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git status --short`, and `git diff --check`.
- Boundary:
  `workspace_status` is parsed handoff evidence only; it does not run extra git
  commands, clean, reorder, revert, stage, commit, or validate the dirty
  worktree. No external GitHub Skill install, no DMM table fill, no firmware
  implementation, no generated-code edit, no CubeMX/MCSDK edit, no flash, no
  24V, no power-board connection, no motor connection, no Gate PWM, no Motor
  Profiler, no Hall closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 AI Maintenance Audit Full Git Status Addendum

- Task:
  `TASK-2026-06-09-ai-maintenance-audit-preserve-git-status-output`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-PRESERVE-GIT-STATUS-OUTPUT-001`.
- Decision:
  `AI maintenance audit full git-status output / dirty-worktree handoff evidence not truncated / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with per-step output policy;
  normal steps remain tail-limited, while `git_status` uses
  `preserve_output=True` and reports `output_policy: full`. Updated tests,
  contracts, retrieval, docs, and project Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`,
  `python tools/check_project_skill_install.py`,
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git status --short`, and `git diff --check`.
- Boundary:
  full `git_status` output is handoff evidence only; it does not clean,
  reorder, revert, stage, commit, or validate the dirty worktree. No external
  GitHub Skill install, no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-08 AI Maintenance Audit Git Status Addendum

- Task:
  `TASK-2026-06-08-ai-maintenance-audit-git-status-step`.
- Evidence:
  `EV-2026-06-08-AI-MAINTENANCE-AUDIT-GIT-STATUS-001`.
- Decision:
  `AI maintenance audit git-status step / dirty-worktree handoff evidence / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with a read-only
  `git_status` step that runs `git status --short`, included it in full and
  quick audits, and updated tests, contracts, retrieval, docs, and project
  Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 300`,
  `python tools/check_project_skill_install.py`,
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git status --short`, and `git diff --check`.
- Boundary:
  git-status capture is handoff evidence only; it does not clean, reorder,
  revert, stage, commit, or validate the dirty worktree. No external GitHub
  Skill install, no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-08 AI Maintenance Audit Markdown Report Addendum

- Task:
  `TASK-2026-06-08-ai-maintenance-audit-markdown-report`.
- Evidence:
  `EV-2026-06-08-AI-MAINTENANCE-AUDIT-MARKDOWN-REPORT-001`.
- Decision:
  `AI maintenance audit Markdown report output / explicit write-report mode / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with explicit
  `--write-report <path>` output, added temp-file test coverage, and updated
  contracts, retrieval, docs, and project Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 500`,
  `python tools/check_project_skill_install.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`, and `git diff --check`.
- Boundary:
  explicit Markdown report output only, repo-local project Skill reinstall only,
  no external GitHub Skill install, no DMM table fill, no firmware
  implementation, no generated-code edit, no CubeMX/MCSDK edit, no flash, no
  24V, no power-board connection, no motor connection, no Gate PWM, no Motor
  Profiler, no Hall closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-08 AI Maintenance Audit Runner Addendum

- Task:
  `TASK-2026-06-08-ai-maintenance-audit-runner`.
- Evidence:
  `EV-2026-06-08-AI-MAINTENANCE-AUDIT-RUNNER-001`.
- Decision:
  `AI maintenance audit runner / consolidated no-power closeout checks / no hardware or firmware action`.
- Scope:
  added `tools/run_ai_maintenance_audit.py`, wired it into context packs,
  contract checks, retrieval eval, docs, and tests, then used it to run the
  full no-power AI maintenance closeout set.
- Verification:
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 800`
  returned `ok: true`, including Skill validation, installed Skill drift
  check, `workflow_maintenance` context pack, AI contracts, vector-store
  rebuild, retrieval eval, unit tests, compileall, and `git diff --check`.
- Boundary:
  repo-local project Skill reinstall only, no external GitHub Skill install,
  no DMM table fill, no firmware implementation, no generated-code edit, no
  CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no motor
  connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-08 Project Skill Install Drift Checker Addendum

- Task:
  `TASK-2026-06-08-project-skill-install-drift-checker`.
- Evidence:
  `EV-2026-06-08-PROJECT-SKILL-INSTALL-DRIFT-CHECK-001`.
- Decision:
  `Project Skill install drift checker / repo-local versus installed Skill comparison / no hardware or firmware action`.
- Scope:
  added `tools/check_project_skill_install.py`, wired it into context packs,
  contract checks, retrieval eval, docs, and tests, and reinstalled the
  validated repo-local project Skill after the checker detected expected drift
  from the new workflow-maintenance reference update.
- Verification:
  `python tools/check_project_skill_install.py --repo-only --json`,
  `python tools/check_project_skill_install.py`,
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`, and `git diff --check`.
- Boundary:
  repo-local project Skill reinstall only, no external GitHub Skill install,
  no DMM table fill, no firmware implementation, no generated-code edit, no
  CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no motor
  connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-08 Project Skill v2 Optimization Addendum

- Task:
  `TASK-2026-06-08-project-skill-v2-optimization`.
- Evidence:
  `EV-2026-06-08-PROJECT-SKILL-V2-OPT-001`.
- Decision:
  `Project Skill v2 router / no-power references / contract-checked workflow maintenance / no hardware or firmware action`.
- Scope:
  refactored `codex_skills/stm32g474-foc-assistant/SKILL.md` into a concise
  router, added `references/project-navigation.md`,
  `references/no-power-boundary.md`, `references/learning-feedback.md`, and
  `references/workflow-maintenance.md`, then wired the Skill source into
  context packs, contract checks, retrieval eval, docs, and tests.
- Verification:
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`,
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`, and `git diff --check`.
- Boundary:
  repo-local project Skill install only, no external GitHub Skill install, no
  DMM table fill, no firmware implementation, no generated-code edit, no
  CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no motor
  connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-08 Project Workflow / AI Architecture Maintenance Addendum

- Task:
  `TASK-2026-06-08-project-workflow-ai-architecture-optimization`.
- Evidence:
  `EV-2026-06-08-PROJECT-WORKFLOW-AI-ARCHITECTURE-OPT-001`.
- Decision:
  `Project workflow and AI architecture maintenance / workflow_maintenance context / project workflow contract checks / no hardware or firmware action`.
- Scope:
  added `workflow_maintenance` context, project workflow contract checks,
  workflow retrieval regression cases, and updated AI/workflow entry indexes.
- Verification:
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`, and `git diff --check`.
- Boundary:
  no DMM table fill, no firmware implementation, no generated-code edit, no
  CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no motor
  connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current Waiting-Hardware Addendum

- New handoff:
  `TASK-2026-05-31-p2-pcb2-waiting-hardware-handoff`.
- Evidence:
  `EV-2026-05-31-P2-PCB2-WAITING-HARDWARE-HANDOFF-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/pcb2_waiting_hardware_handoff_2026-05-31.md`.
- Decision:
  `PCB2 waiting for population / DMM gate deferred / no powered action / no firmware implementation`.
- Boundary: PCB2 has not yet been accepted as populated for measurement. Do
  not fill the DMM table until populated hardware exists; ask for the hardware
  teammate status and any updated source packet. The no-power Hall
  mixed-sequence check is now completed and parked at L4.

## Current 2026-06-01 Learning Evidence Addendum

- PR #5, `learning notes`, was reviewed and merged into `master` with merge
  commit `2b614b4aae4eb40a5b2a882c5f2252dadbe06079`.
- PR scope accepted: L2 MCSDK Hall speed / position feedback concept evidence
  only; no MCSDK Hall closed-loop, Motor Profiler, power-board, motor, PWM,
  serial, build, or powered validation claim.
- WP-030 mixed-sequence trace is now passed at L4 and recorded in
  `learning/review_items/2026-06-01_software_hall_mixed_sequence_review.md`.
- Hardware note: the user reported that the hardware teammate is close to
  finishing soldering on 2026-06-01. This does not open DMM until populated-board
  evidence exists.

## Current 2026-06-01 PCB2 Populated Addendum

- User reported: PCB2 soldered / in hand, and current route still
  `PA0/PA1/PB4 + PB3=LIN1 + P14/P15=3V3/GND`.
- Evidence:
  `EV-2026-06-01-P2-PCB2-POPULATED-ROUTE-UNCHANGED-DMM-PENDING-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/pcb2_populated_route_unchanged_dmm_pending_2026-06-01.md`.
- Decision:
  `PCB2 populated / current route unchanged / DMM continuity and short-check opened as no-power pending / no powered action`.
- Boundary: DMM may now be filled only with the board unpowered. This is not a
  DMM pass and does not authorize firmware implementation, flash, 24V, motor,
  Gate PWM, Motor Profiler, or Hall closed-loop claims.

## Current Workflow Guard Addendum

- User-reported issue: Codex kept drifting into concept teaching even though the
  dual-teacher workflow says ChatGPT should teach pure theory.
- Hotfix task:
  `TASK-2026-05-28-workflow-dual-teacher-concept-guard`.
- Evidence:
  `EV-2026-05-28-WORKFLOW-DUAL-TEACHER-CONCEPT-GUARD-001`.
- Decision:
  `Dual-teacher concept-only role guard / ChatGPT teaches theory / Codex reviews records and executes repo work`.
- Boundary: workflow-control only; no firmware, no Workbench regeneration, no
  flash, no 24V, no power-board connection, no motor connection, no Gate PWM,
  no Motor Profiler, no Hall closed-loop, and no powered readiness.

## Task ID

- ID: `TASK-2026-05-28-p2-software-hall-firmware-entry-plan`
- Topic: software Hall firmware-entry plan for future debug-only
  `PA0/PA1/PB4` adapter
- Status: `done`
- Risk Level: `L1 no-power design boundary / no firmware / no hardware`
- Definition of Done: `workflow/definition_of_done.md`
- Evidence ID:
  `EV-2026-05-28-P2-SOFTWARE-HALL-FIRMWARE-ENTRY-PLAN-001`
- Related build-only task:
  `TASK-2026-05-27-p2-qiansai-g474-stdrive101-foc-p2-debug-build-only`
- Related MCSDK interface task:
  `TASK-2026-05-27-p2-software-hall-mcsdk-speed-position-feedback-interface-review`
- Related hardware gate:
  `TASK-2026-05-22-p2-dmm-continuity-short-check-request`
- Review Required: yes

## Background

PCB2 is still unpopulated. DMM continuity / short-check evidence is deferred,
not passed. Deferred does not mean passed.

The external Workbench project must remain stable at:

`C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`

The no-power Debug build-only task already recorded local compile evidence.
That build-only pass does not prove current PCB2 physical routing, GPIO/EXTI
runtime behavior, MCSDK Hall integration, Gate PWM safety, Hall closed-loop
behavior, motor readiness, power-stage readiness, or sensorless validation.

## Feature Sentence

The project now has a Chinese-first no-power firmware-entry plan:

```text
accepted current route PA0/PA1/PB4
-> future GPIO/EXTI debug-only capture
-> ISR stores raw_state + timestamp + event count only
-> low-priority state machine rejects 000/111, repeats, bounce candidates, and abnormal jumps
-> low-frequency debug snapshot exposes direction_candidate and speed_candidate
-> no MCSDK hook, no firmware implementation, no Hall readiness
```

## Evidence Decision

- Decision:
  `Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.
- Evidence level: L1 no-power design-boundary evidence.
- New artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_plan_2026-05-28.md`.
- Current route:
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- Fixed constraint: `PB3=LIN1`; it is not current Hall.
- Generated-route reminder: MCSDK standard TIM2 Hall `PA15/PB3/PB10` is
  generated-source evidence only, not current PCB2 Hall proof.
- This artifact is not usable to claim firmware implementation, MCSDK Hall
  integration, MCSDK hook readiness, DMM continuity, Gate PWM safety, Hall
  closed-loop, motor readiness, power-stage readiness, or sensorless
  validation.

## Input Files

- `workflow/CURRENT_SNAPSHOT.md`
- `CURRENT_STATUS.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_checklist_2026-05-27.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_gpio_exti_boundary_review_2026-05-27.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_timestamp_source_review_2026-05-27.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_debug_output_route_review_2026-05-27.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md`

## Output Files

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_plan_2026-05-28.md`
- `CURRENT_STATUS.md`
- `AI_CONTEXT.md`
- `workflow/ACTIVE_TASK.md`
- `workflow/CURRENT_SNAPSHOT.md`
- `workflow/evidence_register.md`
- `workflow/current_learning_sprint.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md`
- `deliverables/submission_checklist.md`
- `tests/test_workflow_contracts.py`

## Carry-Forward Build-Only Contract

The earlier build-only evidence remains active context, but it is not the
current task.

- `TASK-2026-05-27-p2-qiansai-g474-stdrive101-foc-p2-debug-build-only` /
  `EV-2026-05-27-P2-QIANSAI-G474-STDRIVE101-FOC-P2-BUILD-ONLY-001`:
  `No-power build-only Debug pass / local toolchain compiles generated project / no firmware runtime or hardware readiness`.
- Build command:
  `cmake --build "C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2\build\Debug" --config Debug`.
- Result: exit code `0`; Ninja output `ninja: no work to do`.
- Confirmed artifacts:
  `QIANSAI_G474_STDRIVE101_FOC_P2.elf` and
  `QIANSAI_G474_STDRIVE101_FOC_P2.map`.
- The record is `not a clean rebuild record`; it is local no-power compile
  evidence only.

## Carry-Forward Software Hall Contracts

These prior no-power software Hall records remain active context for safety and
review. They are not usable to claim firmware implementation, MCSDK Hall
integration, Hall closed-loop behavior, Gate PWM safety, motor readiness,
power-stage readiness, or sensorless validation.

Stable carry-forward phrases:

- not usable to claim firmware implementation
- Not usable to claim firmware implementation
- not firmware or hardware readiness

- `TASK-2026-05-22-p2-software-hall-no-power-algorithm-prep` /
  `EV-2026-05-22-P2-SOFTWARE-HALL-ALGORITHM-PREP-001`:
  `Algorithm-side no-power preparation only`; `Deferred does not mean passed`.
- `TASK-2026-05-22-p2-software-hall-state-machine-exercise` /
  `EV-2026-05-22-P2-SOFTWARE-HALL-STATE-MACHINE-EXERCISE-001`:
  `Software Hall state-machine exercise`; `Waiting for user answer`; learning
  check only.
- `TASK-2026-05-27-p2-software-hall-adapter-pseudocode-draft` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-PSEUDOCODE-DRAFT-001`:
  `Pseudocode draft added / no firmware implementation / no MCSDK Hall integration / no Hall readiness`;
  DMM remains deferred, not passed.
- `TASK-2026-05-27-p2-software-hall-followup-review` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-FOLLOWUP-REVIEW-001`:
  `L4 table-level no-power Hall state-machine classification / no firmware implementation / no hardware validation`.
- `TASK-2026-05-27-p2-software-hall-processing-order-card` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-PROCESSING-ORDER-CARD-001`:
  `Software Hall Adapter Processing-Order Card`; L1 repair artifact, not a new
  mastery upgrade.
- `TASK-2026-05-27-p2-software-hall-host-model` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-HOST-MODEL-001`:
  `Host-side software Hall reference model / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-golden-vectors` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-GOLDEN-VECTORS-001`:
  `Host-side software Hall golden vectors / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-mcsdk-integration-probe` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-INTEGRATION-PROBE-001`:
  `MCSDK Hall integration points identified as read-only clues / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-firmware-entry-checklist` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-FIRMWARE-ENTRY-CHECKLIST-001`:
  `Software Hall firmware-entry checklist / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-gpio-exti-boundary` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-GPIO-EXTI-BOUNDARY-001`:
  `Software Hall GPIO/EXTI boundary review draft / no firmware implementation / no GPIO runtime proof / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-timestamp-source-review` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-TIMESTAMP-SOURCE-001`:
  `Software Hall timestamp-source review draft / no firmware implementation / no timer configuration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-debug-output-route-review` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-DEBUG-OUTPUT-ROUTE-001`:
  `Software Hall low-frequency debug-output route review draft / no firmware implementation / no UART implementation / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-mcsdk-firmware-integration-boundary` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-FIRMWARE-INTEGRATION-BOUNDARY-001`:
  `Software Hall MCSDK firmware-integration boundary review draft / no firmware implementation / no MCSDK hook / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-mcsdk-hook-evidence-request-checklist` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-HOOK-EVIDENCE-REQUEST-001`:
  `Software Hall MCSDK hook evidence request checklist / no firmware implementation / no MCSDK hook / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-mcsdk-speed-position-feedback-interface-review` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-SPEED-POSITION-INTERFACE-001`:
  `Software Hall MCSDK speed/position feedback interface review / no firmware implementation / no MCSDK hook / no Hall readiness`.

## Next User Checkpoint

The next user checkpoint is the no-power DMM continuity / short-check table.
Keep the external Workbench project path stable. If any Hall line, `PB3=LIN1`,
`P14/P15=3V3/GND`, or `nFAULT->PB12` route changes during measurement, report
it immediately.

Because soldering is now reported complete, resume only the no-power DMM
continuity / short-check table before any firmware adapter, flash,
Run / Debug, or powered work.

## Verification

Pending in this task until repo checks are rerun:

- `python -m unittest discover -s tests`
- `python -m compileall src tests`
- `git diff --check`
- `python tools\check_ai_contracts.py`
- `python tools\build_vector_store.py`

## Safety Boundary

This task does not authorize firmware logic edits, generated-code edits,
CubeMX/Workbench edits, flash, Run / Debug, 24V, power-board connection, motor
connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
sensorless / SMO claims.
