from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALID_TASK_STATUSES = {"draft", "approved", "in_progress", "blocked", "done", "reviewed"}
TASK_ID_RE = re.compile(r"TASK-\d{4}-\d{2}-\d{2}-[A-Za-z0-9_-]+")
EVIDENCE_ID_RE = re.compile(r"EV-\d{4}-\d{2}-\d{2}-[A-Z0-9-]+")
STATUS_RE = re.compile(r"Status:\s*`?([A-Za-z_]+)`?")
TABLE_OPEN_RE = re.compile(r"\|\s*(open|watching)\s*\|", re.IGNORECASE)

SAFETY_PHRASES = (
    "No flash",
    "No 24V",
    "No power-board connection",
    "No motor connection",
    "No Gate PWM output",
    "No Motor Profiler run",
    "No Hall closed-loop claim",
    "No sensorless / SMO claim",
)

DANGEROUS_POSITIVE_CLAIMS = (
    "Hall readiness is upgraded",
    "Hall readiness upgraded",
    "powered readiness is upgraded",
    "powered readiness upgraded",
    "motor readiness is upgraded",
    "motor readiness upgraded",
    "power-stage readiness is upgraded",
    "power-stage readiness upgraded",
    "Gate PWM ready",
    "24V ready",
    "Motor Profiler ready",
)


@dataclass
class CheckReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    @property
    def ok(self) -> bool:
        return not self.errors


def read(relative_path: str) -> str:
    path = ROOT / relative_path
    return path.read_text(encoding="utf-8", errors="ignore")


def exists(relative_path: str) -> bool:
    return (ROOT / relative_path).is_file()


def check_required_files(report: CheckReport) -> None:
    for relative_path in (
        "AI_CONTEXT.md",
        "workflow/CURRENT_SNAPSHOT.md",
        "workflow/ACTIVE_TASK.md",
        "docs/00_project_truth/project_context.md",
        "docs/00_project_truth/ai_architecture.md",
        "tools/build_context_pack.py",
        "tools/check_ai_contracts.py",
    ):
        if not exists(relative_path):
            report.error(f"Missing required AI architecture file: {relative_path}")


def check_active_task(report: CheckReport) -> None:
    if not exists("workflow/ACTIVE_TASK.md"):
        return
    text = read("workflow/ACTIVE_TASK.md")

    task_ids = TASK_ID_RE.findall(text)
    if not task_ids:
        report.error("ACTIVE_TASK.md has no TASK-YYYY-MM-DD-* task id.")

    match = STATUS_RE.search(text)
    if not match:
        report.error("ACTIVE_TASK.md has no parseable Status field.")
    else:
        status = match.group(1)
        if status not in VALID_TASK_STATUSES:
            report.error(f"ACTIVE_TASK.md has invalid status: {status}")
        if status == "done" and "Review Required: yes" in text:
            report.warn("ACTIVE_TASK.md is done and still requires review.")

    evidence_ids = EVIDENCE_ID_RE.findall(text)
    if not evidence_ids:
        report.error("ACTIVE_TASK.md has no EV-YYYY-MM-DD-* evidence id.")
    else:
        evidence_text = read("workflow/evidence_register.md") if exists("workflow/evidence_register.md") else ""
        status_text = read("CURRENT_STATUS.md") if exists("CURRENT_STATUS.md") else ""
        for evidence_id in sorted(set(evidence_ids)):
            if evidence_id not in evidence_text and evidence_id not in status_text:
                report.warn(f"Evidence id from ACTIVE_TASK.md is not yet referenced in evidence register or CURRENT_STATUS: {evidence_id}")

    if "## Safety Boundary" not in text:
        report.error("ACTIVE_TASK.md is missing a Safety Boundary section.")


def check_snapshot_and_architecture(report: CheckReport) -> None:
    for relative_path in ("workflow/CURRENT_SNAPSHOT.md", "docs/00_project_truth/ai_architecture.md"):
        if not exists(relative_path):
            continue
        text = read(relative_path)
        for phrase in SAFETY_PHRASES:
            if phrase not in text:
                report.error(f"{relative_path} is missing safety phrase: {phrase}")

    if exists("AI_CONTEXT.md"):
        text = read("AI_CONTEXT.md")
        if "workflow/CURRENT_SNAPSHOT.md" not in text:
            report.warn("AI_CONTEXT.md does not point to workflow/CURRENT_SNAPSHOT.md.")


def check_indexes(report: CheckReport) -> None:
    if not exists("docs/file_map.md"):
        return
    text = read("docs/file_map.md")
    for phrase in (
        "ai_architecture",
        "current_snapshot",
        "build_context_pack",
        "check_ai_contracts",
    ):
        if phrase not in text:
            report.warn(f"docs/file_map.md does not mention {phrase}.")

    if exists("tools/README.md"):
        tools_text = read("tools/README.md")
        for phrase in ("build_context_pack.py", "check_ai_contracts.py"):
            if phrase not in tools_text:
                report.warn(f"tools/README.md does not mention {phrase}.")


def check_review_queue(report: CheckReport) -> None:
    if not exists("learning/review_queue.md"):
        return
    text = read("learning/review_queue.md")
    open_count = len(TABLE_OPEN_RE.findall(text))
    if open_count > 8:
        report.warn(f"review_queue.md has {open_count} open/watching items; target is 5-8.")


def check_dangerous_claims(report: CheckReport) -> None:
    scan_files = (
        "AI_CONTEXT.md",
        "workflow/CURRENT_SNAPSHOT.md",
        "workflow/ACTIVE_TASK.md",
        "docs/00_project_truth/ai_architecture.md",
    )
    for relative_path in scan_files:
        if not exists(relative_path):
            continue
        text = read(relative_path)
        for claim in DANGEROUS_POSITIVE_CLAIMS:
            if claim in text:
                report.error(f"{relative_path} contains dangerous positive claim: {claim}")


def run_checks() -> CheckReport:
    report = CheckReport()
    check_required_files(report)
    check_active_task(report)
    check_snapshot_and_architecture(report)
    check_indexes(report)
    check_review_queue(report)
    check_dangerous_claims(report)
    return report


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Check AI architecture and workflow contracts.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    args = parser.parse_args()

    report = run_checks()

    if args.json:
        print(json.dumps({"errors": report.errors, "warnings": report.warnings}, ensure_ascii=False, indent=2))
    else:
        if report.errors:
            print("AI contract errors:")
            for item in report.errors:
                print(f"- {item}")
        else:
            print("AI contract errors: none")

        if report.warnings:
            print("AI contract warnings:")
            for item in report.warnings:
                print(f"- {item}")
        else:
            print("AI contract warnings: none")

    if report.errors or (args.strict and report.warnings):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
