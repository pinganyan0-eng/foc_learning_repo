from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.check_ai_contracts import (  # noqa: E402
    READABILITY_HEADER_LINE_LIMIT,
    READABILITY_HEADER_REQUIREMENTS,
    READABILITY_MOJIBAKE_MARKERS,
)

PROJECT_SKILL_PATH = Path("codex_skills") / "stm32g474-foc-assistant"
QUICK_VALIDATE = (
    Path.home()
    / ".codex"
    / "skills"
    / ".system"
    / "skill-creator"
    / "scripts"
    / "quick_validate.py"
)
DEFAULT_OUTPUT_LIMIT = 4000
NO_POWER_BOUNDARY = (
    "No flash, no 24V, no power-board connection, no motor connection, "
    "no Gate PWM output, no Motor Profiler, no Hall closed-loop claim, "
    "and no sensorless / SMO claim."
)
PATH_GROUP_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("personal_notes_or_obsidian", (".obsidian/", "notes/")),
    ("ai_maintenance", ("AI_CONTEXT.md", "tools/", "retrieval_eval/", "tests/")),
    ("project_skill", ("codex_skills/",)),
    ("workflow_status", ("CURRENT_STATUS.md", "workflow/")),
    ("project_truth_docs", ("docs/", "deliverables/")),
    ("learning_memory", ("learning/",)),
    ("no_power_precheck", ("apps/stm32_g474_foc/mcsdk_no_power_precheck/",)),
    ("interfaces", ("interfaces/",)),
)
GROUP_FOCUS_ORDER: tuple[str, ...] = (
    "ai_maintenance",
    "workflow_status",
    "project_skill",
    "no_power_precheck",
    "project_truth_docs",
    "learning_memory",
    "interfaces",
    "personal_notes_or_obsidian",
    "other",
)
GROUP_REVIEW_FOCUS: dict[str, str] = {
    "ai_maintenance": (
        "Review AI maintenance scripts, contracts, retrieval evals, and tests before merge."
    ),
    "workflow_status": (
        "Review task state, evidence records, and current-status text; do not self-clear required review."
    ),
    "project_skill": (
        "Review the project Skill router, references, metadata, validation, and install drift."
    ),
    "no_power_precheck": (
        "Review no-power precheck handoff files only; do not treat pending DMM data as passed."
    ),
    "project_truth_docs": (
        "Review architecture, file-map, and submission-truth docs for scope and boundary consistency."
    ),
    "learning_memory": (
        "Review learning notes, weak points, mastery records, and spaced-review queue updates."
    ),
    "interfaces": (
        "Review interface contracts without treating them as firmware runtime or hardware evidence."
    ),
    "personal_notes_or_obsidian": (
        "Review personal notes or Obsidian changes separately from project truth files."
    ),
    "other": "Review uncategorized paths manually before merge.",
}
REVIEW_LIFECYCLE_WARNING_MARKERS: tuple[str, ...] = (
    "still requires review",
    "Verification section still contains Pending",
)
READABILITY_LEGACY_SCAN_FILES: tuple[str, ...] = (
    "AI_CONTEXT.md",
    "CURRENT_STATUS.md",
    "workflow/CURRENT_SNAPSHOT.md",
    "workflow/ACTIVE_TASK.md",
    "workflow/evidence_register.md",
    "deliverables/submission_checklist.md",
    "docs/00_project_truth/ai_architecture.md",
    "docs/file_map.md",
    "tools/README.md",
    "workflow/automation_playbook.md",
    "workflow/definition_of_done.md",
    "workflow/learning_feedback_loop.md",
    "workflow/session_close_checklist.md",
    "codex_skills/stm32g474-foc-assistant/references/workflow-maintenance.md",
)
READABILITY_CLEANUP_CLAIM_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(
        r"\b(?:full legacy mojibake cleanup|full historical mojibake cleanup)\s+"
        r"(?:is\s+)?(?:complete|completed|done)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:all|every)\s+legacy\s+(?:historical\s+)?mojibake\s+rows?\s+"
        r"(?:are|is)\s+(?:repaired|fixed|clean)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\ball legacy history is repaired\b",
        re.IGNORECASE,
    ),
)
READABILITY_CLEANUP_NEGATION_MARKERS: tuple[str, ...] = (
    "does not claim",
    "do not claim",
    "not claim",
    "without claiming",
    "without treating",
    "not usable to claim",
    "no claim",
)


@dataclass(frozen=True)
class AuditStep:
    step_id: str
    description: str
    command: tuple[str, ...]
    preserve_output: bool = False


def python_command(*args: str) -> tuple[str, ...]:
    return (sys.executable, *args)


def step_catalog(*, repo_only_skill: bool) -> dict[str, AuditStep]:
    skill_check_command = python_command("tools/check_project_skill_install.py")
    if repo_only_skill:
        skill_check_command += ("--repo-only",)

    steps = {
        "skill_validate": AuditStep(
            "skill_validate",
            "Validate the project Skill folder with the Codex skill validator.",
            python_command("-X", "utf8", str(QUICK_VALIDATE), str(PROJECT_SKILL_PATH)),
        ),
        "project_skill_install": AuditStep(
            "project_skill_install",
            "Check repo-local project Skill source and installed Skill drift.",
            skill_check_command,
        ),
        "context_pack": AuditStep(
            "context_pack",
            "Render the workflow_maintenance no-power context pack.",
            python_command(
                "tools/build_context_pack.py",
                "--mode",
                "workflow_maintenance",
                "--max-chars",
                "350",
            ),
        ),
        "ai_contracts": AuditStep(
            "ai_contracts",
            "Run AI and project workflow contract checks.",
            python_command("tools/check_ai_contracts.py"),
        ),
        "build_vector_store": AuditStep(
            "build_vector_store",
            "Rebuild the local retrieval index.",
            python_command("tools/build_vector_store.py"),
        ),
        "retrieval_eval": AuditStep(
            "retrieval_eval",
            "Run local retrieval regression cases.",
            python_command("tools/search_local_v2.py", "--eval"),
        ),
        "unit_tests": AuditStep(
            "unit_tests",
            "Run the repository unit test suite.",
            python_command("-m", "unittest", "discover", "-s", "tests"),
        ),
        "compileall": AuditStep(
            "compileall",
            "Compile Python source and tests.",
            python_command("-m", "compileall", "src", "tests"),
        ),
        "git_status": AuditStep(
            "git_status",
            "Record git status --short for dirty-worktree handoff evidence.",
            ("git", "status", "--short"),
            preserve_output=True,
        ),
        "diff_check": AuditStep(
            "diff_check",
            "Check diff whitespace and conflict markers.",
            ("git", "diff", "--check"),
        ),
    }
    return steps


def full_step_ids() -> tuple[str, ...]:
    return (
        "skill_validate",
        "project_skill_install",
        "context_pack",
        "ai_contracts",
        "build_vector_store",
        "retrieval_eval",
        "unit_tests",
        "compileall",
        "git_status",
        "diff_check",
    )


def quick_step_ids() -> tuple[str, ...]:
    return (
        "project_skill_install",
        "context_pack",
        "ai_contracts",
        "git_status",
    )


def truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[-limit:]


def output_text(text: str, *, limit: int, preserve: bool) -> str:
    if preserve:
        return text
    return truncate(text, limit)


def run_step(step: AuditStep, *, output_limit: int) -> dict[str, object]:
    completed = subprocess.run(
        step.command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return {
        "id": step.step_id,
        "description": step.description,
        "command": list(step.command),
        "returncode": completed.returncode,
        "ok": completed.returncode == 0,
        "output_policy": "full" if step.preserve_output else "tail",
        "stdout_tail": output_text(
            completed.stdout,
            limit=output_limit,
            preserve=step.preserve_output,
        ),
        "stderr_tail": output_text(
            completed.stderr,
            limit=output_limit,
            preserve=step.preserve_output,
        ),
    }


def classify_path_group(path: str) -> str:
    normalized = path.replace("\\", "/")
    for group, prefixes in PATH_GROUP_RULES:
        for prefix in prefixes:
            if normalized == prefix.rstrip("/") or normalized.startswith(prefix):
                return group
    return "other"


def summarize_path_groups(items: list[dict[str, str]]) -> dict[str, dict[str, object]]:
    groups: dict[str, dict[str, object]] = {}
    for item in items:
        group_name = classify_path_group(item["path"])
        group = groups.setdefault(
            group_name,
            {"total": 0, "status_counts": {}, "paths": []},
        )
        group["total"] = int(group["total"]) + 1
        status_counts = group["status_counts"]
        if isinstance(status_counts, dict):
            status_counts[item["status"]] = int(status_counts.get(item["status"], 0)) + 1
        paths = group["paths"]
        if isinstance(paths, list):
            paths.append(item["path"])

    return dict(sorted(groups.items()))


def summarize_status_paths(items: list[dict[str, str]]) -> dict[str, list[str]]:
    status_paths: dict[str, list[str]] = {}
    for item in items:
        status_paths.setdefault(item["status"], []).append(item["path"])
    return dict(sorted(status_paths.items()))


def summarize_focus_groups(
    path_groups: dict[str, dict[str, object]],
) -> list[dict[str, object]]:
    priority = {group: index for index, group in enumerate(GROUP_FOCUS_ORDER)}
    focus_groups: list[dict[str, object]] = []

    for group_name, group in path_groups.items():
        if not isinstance(group, dict):
            continue
        focus_groups.append(
            {
                "group": group_name,
                "priority": priority.get(group_name, len(GROUP_FOCUS_ORDER)),
                "total": group.get("total", 0),
                "status_counts": group.get("status_counts", {}),
            }
        )

    return sorted(
        focus_groups,
        key=lambda item: (int(item["priority"]), -int(item.get("total") or 0), str(item["group"])),
    )


def build_handoff_review_queue(
    path_groups: dict[str, dict[str, object]],
    focus_groups: list[dict[str, object]],
) -> list[dict[str, object]]:
    review_queue: list[dict[str, object]] = []

    for focus in focus_groups:
        if not isinstance(focus, dict):
            continue
        group_name = str(focus.get("group") or "")
        group = path_groups.get(group_name, {})
        paths = group.get("paths", []) if isinstance(group, dict) else []
        review_queue.append(
            {
                "group": group_name,
                "priority": focus.get("priority", len(GROUP_FOCUS_ORDER)),
                "total": focus.get("total", 0),
                "status_counts": focus.get("status_counts", {}),
                "review_focus": GROUP_REVIEW_FOCUS.get(group_name, GROUP_REVIEW_FOCUS["other"]),
                "paths": paths if isinstance(paths, list) else [],
            }
        )

    return review_queue


def parse_git_status_short(text: str) -> dict[str, object]:
    items: list[dict[str, str]] = []
    counts: Counter[str] = Counter()

    for raw_line in text.splitlines():
        if not raw_line.strip():
            continue
        status = raw_line[:2] if len(raw_line) >= 2 else raw_line
        path = raw_line[3:] if len(raw_line) >= 3 else ""
        item = {"status": status, "path": path}
        items.append(item)
        counts[status] += 1

    path_groups = summarize_path_groups(items)
    focus_groups = summarize_focus_groups(path_groups)
    return {
        "available": True,
        "dirty": bool(items),
        "total": len(items),
        "status_counts": dict(sorted(counts.items())),
        "status_paths": summarize_status_paths(items),
        "path_groups": path_groups,
        "focus_groups": focus_groups,
        "handoff_review_queue": build_handoff_review_queue(path_groups, focus_groups),
        "paths": [item["path"] for item in items],
        "items": items,
    }


def workspace_status_from_results(results: list[dict[str, object]]) -> dict[str, object]:
    for result in results:
        if result.get("id") == "git_status":
            summary = parse_git_status_short(str(result.get("stdout_tail") or ""))
            summary["source_step_ok"] = bool(result.get("ok"))
            return summary

    return {
        "available": False,
        "source_step_ok": False,
        "dirty": None,
        "total": 0,
        "status_counts": {},
        "status_paths": {},
        "path_groups": {},
        "focus_groups": [],
        "handoff_review_queue": [],
        "paths": [],
        "items": [],
    }


def readability_header_status_from_repo() -> dict[str, object]:
    guarded_entry_files = list(READABILITY_HEADER_REQUIREMENTS)
    missing_entry_files: list[str] = []
    missing_entry_phrases: list[dict[str, str]] = []
    header_marker_hits: list[dict[str, str]] = []

    for relative_path, required_phrases in READABILITY_HEADER_REQUIREMENTS.items():
        path = ROOT / relative_path
        if not path.is_file():
            missing_entry_files.append(relative_path)
            continue

        text = path.read_text(encoding="utf-8", errors="replace")
        header = "\n".join(text.splitlines()[:READABILITY_HEADER_LINE_LIMIT])
        for phrase in required_phrases:
            if phrase not in header:
                missing_entry_phrases.append({"path": relative_path, "phrase": phrase})
        for marker in READABILITY_MOJIBAKE_MARKERS:
            if marker in header:
                header_marker_hits.append({"path": relative_path, "marker": marker})

    return {
        "guarded_entry_files": guarded_entry_files,
        "entry_headers_ok": (
            not missing_entry_files and not missing_entry_phrases and not header_marker_hits
        ),
        "missing_entry_files": missing_entry_files,
        "missing_entry_phrases": missing_entry_phrases,
        "header_marker_hits": header_marker_hits,
    }


def readability_legacy_debt_status_from_repo() -> dict[str, object]:
    legacy_debt_details: list[dict[str, object]] = []
    cleanup_claim_details: list[dict[str, object]] = []
    legacy_debt_count = 0
    cleanup_claim_count = 0

    for relative_path in READABILITY_LEGACY_SCAN_FILES:
        path = ROOT / relative_path
        if not path.is_file():
            continue

        text = path.read_text(encoding="utf-8", errors="replace")
        marker_counts = {
            marker: text.count(marker)
            for marker in READABILITY_MOJIBAKE_MARKERS
            if marker in text
        }
        if marker_counts:
            file_count = sum(marker_counts.values())
            legacy_debt_count += file_count
            legacy_debt_details.append(
                {
                    "path": relative_path,
                    "count": file_count,
                    "markers": sorted(marker_counts),
                }
            )

        claim_markers: list[str] = []
        for pattern in READABILITY_CLEANUP_CLAIM_PATTERNS:
            for match in pattern.finditer(text):
                prefix = text[max(0, match.start() - 80) : match.start()].lower()
                if any(marker in prefix for marker in READABILITY_CLEANUP_NEGATION_MARKERS):
                    continue
                claim_markers.append(match.group(0))
        if claim_markers:
            cleanup_claim_count += len(claim_markers)
            cleanup_claim_details.append(
                {
                    "path": relative_path,
                    "markers": claim_markers,
                }
            )

    return {
        "legacy_debt_present": bool(legacy_debt_details),
        "legacy_debt_count": legacy_debt_count,
        "legacy_debt_paths": [item["path"] for item in legacy_debt_details],
        "legacy_debt_details": legacy_debt_details,
        "full_legacy_cleanup_claimed": bool(cleanup_claim_details),
        "full_legacy_cleanup_claim_count": cleanup_claim_count,
        "full_legacy_cleanup_claim_paths": [
            item["path"] for item in cleanup_claim_details
        ],
        "full_legacy_cleanup_claim_details": cleanup_claim_details,
    }


def readability_status_from_repo() -> dict[str, object]:
    header_status = readability_header_status_from_repo()
    legacy_status = readability_legacy_debt_status_from_repo()
    return {
        "available": True,
        **header_status,
        **legacy_status,
        "hardware_validation": False,
    }


def parse_contract_output(text: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    section: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line == "AI contract errors: none":
            section = None
        elif line == "AI contract errors:":
            section = "errors"
        elif line == "AI contract warnings: none":
            section = None
        elif line == "AI contract warnings:":
            section = "warnings"
        elif line.startswith("- ") and section == "errors":
            errors.append(line[2:])
        elif line.startswith("- ") and section == "warnings":
            warnings.append(line[2:])

    return errors, warnings


def contract_status_from_results(results: list[dict[str, object]]) -> dict[str, object]:
    for result in results:
        if result.get("id") != "ai_contracts":
            continue

        errors, warnings = parse_contract_output(str(result.get("stdout_tail") or ""))
        review_lifecycle_warnings = [
            warning
            for warning in warnings
            if any(marker in warning for marker in REVIEW_LIFECYCLE_WARNING_MARKERS)
        ]
        unexpected_warnings = [
            warning for warning in warnings if warning not in review_lifecycle_warnings
        ]
        return {
            "available": True,
            "source_step_ok": bool(result.get("ok")),
            "error_count": len(errors),
            "warning_count": len(warnings),
            "review_lifecycle_warning_count": len(review_lifecycle_warnings),
            "unexpected_warning_count": len(unexpected_warnings),
            "strict_ready": not errors and not warnings,
            "implementation_closeout_ok": bool(result.get("ok")) and not errors,
            "errors": errors,
            "warnings": warnings,
            "review_lifecycle_warnings": review_lifecycle_warnings,
            "unexpected_warnings": unexpected_warnings,
        }

    return {
        "available": False,
        "source_step_ok": False,
        "error_count": 0,
        "warning_count": 0,
        "review_lifecycle_warning_count": 0,
        "unexpected_warning_count": 0,
        "strict_ready": None,
        "implementation_closeout_ok": None,
        "errors": [],
        "warnings": [],
        "review_lifecycle_warnings": [],
        "unexpected_warnings": [],
    }


def closeout_summary_from_statuses(
    *,
    audit_ok: bool,
    workspace_status: dict[str, object],
    contract_status: dict[str, object],
) -> dict[str, object]:
    contract_available = bool(contract_status.get("available"))
    workspace_available = bool(workspace_status.get("available"))
    handoff_queue = workspace_status.get("handoff_review_queue", [])
    first_review_item = (
        handoff_queue[0]
        if isinstance(handoff_queue, list)
        and handoff_queue
        and isinstance(handoff_queue[0], dict)
        else {}
    )

    contract_errors = int(contract_status.get("error_count") or 0)
    unexpected_warnings = int(contract_status.get("unexpected_warning_count") or 0)
    review_warnings = int(contract_status.get("review_lifecycle_warning_count") or 0)
    contract_closeout_ok = bool(contract_status.get("implementation_closeout_ok"))

    return {
        "available": True,
        "audit_ok": audit_ok,
        "repo_maintenance_closeout_ok": (
            audit_ok
            and contract_available
            and contract_closeout_ok
            and contract_errors == 0
            and unexpected_warnings == 0
        ),
        "strict_ready": contract_status.get("strict_ready") if contract_available else None,
        "needs_user_review": review_warnings > 0 if contract_available else None,
        "contract_error_count": contract_errors if contract_available else None,
        "unexpected_contract_warning_count": (
            unexpected_warnings if contract_available else None
        ),
        "review_lifecycle_warning_count": review_warnings if contract_available else None,
        "dirty_worktree": workspace_status.get("dirty") if workspace_available else None,
        "dirty_entry_count": workspace_status.get("total") if workspace_available else None,
        "next_review_group": first_review_item.get("group"),
        "next_review_focus": first_review_item.get("review_focus"),
        "no_power_boundary_active": True,
        "hardware_validation": False,
        "boundary": NO_POWER_BOUNDARY,
    }


def run_audit(
    *,
    selected_ids: tuple[str, ...],
    repo_only_skill: bool,
    output_limit: int,
) -> dict[str, object]:
    catalog = step_catalog(repo_only_skill=repo_only_skill)
    unknown = [step_id for step_id in selected_ids if step_id not in catalog]
    if unknown:
        return {
            "ok": False,
            "mode": "audit",
            "errors": [f"Unknown audit step: {step_id}" for step_id in unknown],
            "steps": [],
        }

    results = [run_step(catalog[step_id], output_limit=output_limit) for step_id in selected_ids]
    audit_ok = all(result["ok"] for result in results)
    workspace_status = workspace_status_from_results(results)
    contract_status = contract_status_from_results(results)
    readability_status = readability_status_from_repo()
    closeout_summary = closeout_summary_from_statuses(
        audit_ok=audit_ok,
        workspace_status=workspace_status,
        contract_status=contract_status,
    )
    return {
        "ok": audit_ok,
        "mode": "audit",
        "repo_only_skill": repo_only_skill,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "boundary": NO_POWER_BOUNDARY,
        "closeout_summary": closeout_summary,
        "readability_status": readability_status,
        "workspace_status": workspace_status,
        "contract_status": contract_status,
        "steps": results,
        "errors": [
            f"{result['id']} failed with exit code {result['returncode']}"
            for result in results
            if not result["ok"]
        ],
    }


def markdown_escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def command_text(command: object) -> str:
    if not isinstance(command, list):
        return str(command)
    return subprocess.list2cmdline([str(part) for part in command])


def render_markdown_report(report: dict[str, object]) -> str:
    lines = [
        "# AI Maintenance Audit Report",
        "",
        f"- Result: {'ok' if report['ok'] else 'failed'}",
        f"- Generated UTC: {report.get('generated_at_utc', 'unknown')}",
        f"- Project Skill Mode: {'repo-only' if report.get('repo_only_skill') else 'installed compare'}",
        f"- Boundary: {report.get('boundary', NO_POWER_BOUNDARY)}",
        "",
        "This report is repository maintenance evidence only. It is not hardware, firmware runtime, Gate PWM, Hall closed-loop, motor, power-stage, or sensorless validation.",
        "",
        "## Steps",
        "",
        "| Step | Status | Output | Command |",
        "| --- | --- | --- | --- |",
    ]

    for step in report.get("steps", []):
        status = "ok" if step["ok"] else f"failed ({step['returncode']})"
        lines.append(
            f"| `{markdown_escape(step['id'])}` | {markdown_escape(status)} | {markdown_escape(step.get('output_policy', 'tail'))} | `{markdown_escape(command_text(step['command']))}` |"
        )

    errors = report.get("errors", [])
    if errors:
        lines.extend(["", "## Errors", ""])
        lines.extend(f"- {error}" for error in errors)

    closeout_summary = report.get("closeout_summary")
    if isinstance(closeout_summary, dict) and closeout_summary.get("available"):
        lines.extend(
            [
                "",
                "## Closeout Summary",
                "",
                f"- Repo maintenance closeout ok: {closeout_summary.get('repo_maintenance_closeout_ok')}",
                f"- Strict ready: {closeout_summary.get('strict_ready')}",
                f"- Needs user review: {closeout_summary.get('needs_user_review')}",
                f"- Dirty worktree: {closeout_summary.get('dirty_worktree')}",
                f"- Dirty entry count: {closeout_summary.get('dirty_entry_count')}",
                f"- Next review group: {closeout_summary.get('next_review_group')}",
                f"- Next review focus: {closeout_summary.get('next_review_focus')}",
                f"- Hardware validation: {closeout_summary.get('hardware_validation')}",
                "",
                "This summary is derived from audit outputs only. It does not change task state, clean the worktree, or validate hardware readiness.",
            ]
        )

    readability_status = report.get("readability_status")
    if isinstance(readability_status, dict) and readability_status.get("available"):
        guarded_files = readability_status.get("guarded_entry_files", [])
        legacy_paths = readability_status.get("legacy_debt_paths", [])
        lines.extend(
            [
                "",
                "## Readability Status",
                "",
                f"- Entry headers ok: {readability_status.get('entry_headers_ok')}",
                (
                    "- Guarded entry files: "
                    + (
                        ", ".join(f"`{path}`" for path in guarded_files)
                        if isinstance(guarded_files, list) and guarded_files
                        else "none"
                    )
                ),
                f"- Legacy debt present: {readability_status.get('legacy_debt_present')}",
                f"- Legacy debt count: {readability_status.get('legacy_debt_count')}",
                (
                    "- Legacy debt paths: "
                    + (
                        ", ".join(f"`{path}`" for path in legacy_paths)
                        if isinstance(legacy_paths, list) and legacy_paths
                        else "none"
                    )
                ),
                f"- Full legacy cleanup claimed: {readability_status.get('full_legacy_cleanup_claimed')}",
                f"- Hardware validation: {readability_status.get('hardware_validation')}",
                "",
                "This status separates guarded entry headers from broader legacy mojibake debt. It is repo-text only and does not claim full historical cleanup.",
            ]
        )

    contract_status = report.get("contract_status")
    if isinstance(contract_status, dict) and contract_status.get("available"):
        lines.extend(
            [
                "",
                "## Contract Status",
                "",
                f"- Source step ok: {contract_status.get('source_step_ok')}",
                f"- Error count: {contract_status.get('error_count')}",
                f"- Warning count: {contract_status.get('warning_count')}",
                f"- Review lifecycle warning count: {contract_status.get('review_lifecycle_warning_count')}",
                f"- Unexpected warning count: {contract_status.get('unexpected_warning_count')}",
                f"- Strict ready: {contract_status.get('strict_ready')}",
                f"- Implementation closeout ok: {contract_status.get('implementation_closeout_ok')}",
                "",
                "Review lifecycle warnings are allowed before user review; they must not be self-cleared by Codex.",
            ]
        )
        review_warnings = contract_status.get("review_lifecycle_warnings", [])
        if isinstance(review_warnings, list) and review_warnings:
            lines.extend(["", "### Review Lifecycle Warnings", ""])
            lines.extend(f"- {markdown_escape(warning)}" for warning in review_warnings)

    workspace_status = report.get("workspace_status")
    if isinstance(workspace_status, dict) and workspace_status.get("available"):
        status_counts = workspace_status.get("status_counts", {})
        if isinstance(status_counts, dict):
            counts_text = ", ".join(
                f"{key}={value}" for key, value in sorted(status_counts.items())
            )
        else:
            counts_text = ""
        lines.extend(
            [
                "",
                "## Workspace Status",
                "",
                f"- Dirty: {workspace_status.get('dirty')}",
                f"- Total entries: {workspace_status.get('total')}",
                f"- Status counts: {counts_text or 'none'}",
                "",
                "This is a parsed `git status --short` handoff summary only. It does not clean, stage, commit, or validate the dirty worktree.",
            ]
        )
        path_groups = workspace_status.get("path_groups", {})
        focus_groups = workspace_status.get("focus_groups", [])
        if isinstance(focus_groups, list) and focus_groups:
            lines.extend(["", "### Focus Groups", ""])
            for item in focus_groups:
                if isinstance(item, dict):
                    lines.append(f"- `{item.get('group')}`: {item.get('total', 0)}")
        handoff_review_queue = workspace_status.get("handoff_review_queue", [])
        if isinstance(handoff_review_queue, list) and handoff_review_queue:
            lines.extend(["", "### Handoff Review Queue", ""])
            for item in handoff_review_queue:
                if isinstance(item, dict):
                    lines.append(
                        f"- `{item.get('group')}`: {markdown_escape(item.get('review_focus', ''))}"
                    )
        if isinstance(path_groups, dict) and path_groups:
            lines.extend(["", "### Path Groups", ""])
            for group_name, group in sorted(path_groups.items()):
                if isinstance(group, dict):
                    lines.append(f"- `{group_name}`: {group.get('total', 0)}")
        status_paths = workspace_status.get("status_paths", {})
        if isinstance(status_paths, dict) and status_paths:
            lines.extend(["", "### Status Paths", ""])
            for status, paths in sorted(status_paths.items()):
                if isinstance(paths, list):
                    lines.append(f"- `{status}`: {len(paths)}")

    lines.extend(["", "## Output Tails", ""])
    for step in report.get("steps", []):
        stdout_tail = str(step.get("stdout_tail") or "").strip()
        stderr_tail = str(step.get("stderr_tail") or "").strip()
        if not stdout_tail and not stderr_tail:
            continue
        lines.extend([f"### {step['id']}", ""])
        if stdout_tail:
            lines.extend(["stdout:", "", "```text", stdout_tail, "```", ""])
        if stderr_tail:
            lines.extend(["stderr:", "", "```text", stderr_tail, "```", ""])

    return "\n".join(lines).rstrip() + "\n"


def write_markdown_report(report: dict[str, object], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_markdown_report(report), encoding="utf-8")
    report["report_path"] = str(path)


def print_text_report(report: dict[str, object]) -> None:
    print("AI maintenance audit")
    print(f"result: {'ok' if report['ok'] else 'failed'}")
    if report.get("repo_only_skill"):
        print("project Skill mode: repo-only")
    readability_status = report.get("readability_status")
    if isinstance(readability_status, dict) and readability_status.get("available"):
        print(
            "readability_status: "
            f"entry_headers_ok={readability_status.get('entry_headers_ok')}, "
            f"legacy_debt_present={readability_status.get('legacy_debt_present')}, "
            f"legacy_debt_count={readability_status.get('legacy_debt_count')}"
        )
    for step in report.get("steps", []):
        status = "ok" if step["ok"] else f"failed ({step['returncode']})"
        print(f"- {step['id']}: {status}")
    for error in report.get("errors", []):
        print(f"error: {error}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run the no-power AI maintenance audit. This does not authorize "
            "flash, 24V, power-board, motor, Gate PWM, Motor Profiler, "
            "Hall closed-loop, or sensorless claims."
        )
    )
    parser.add_argument(
        "--check",
        action="append",
        choices=full_step_ids(),
        help="Run one audit step. Can be repeated. Defaults to all steps.",
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Run only project Skill, context-pack, AI contract, and git-status checks.",
    )
    parser.add_argument(
        "--repo-only-skill",
        action="store_true",
        help="Do not compare the installed user Skill; validate repo-local Skill source only.",
    )
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--max-output-chars", type=int, default=DEFAULT_OUTPUT_LIMIT)
    parser.add_argument(
        "--write-report",
        type=Path,
        help="Write a Markdown report to the given path after the audit finishes.",
    )
    return parser.parse_args()


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    args = parse_args()
    if args.check:
        selected = tuple(args.check)
    elif args.quick:
        selected = quick_step_ids()
    else:
        selected = full_step_ids()

    report = run_audit(
        selected_ids=selected,
        repo_only_skill=args.repo_only_skill,
        output_limit=max(200, args.max_output_chars),
    )

    if args.write_report:
        write_markdown_report(report, args.write_report)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_text_report(report)

    if not report["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
