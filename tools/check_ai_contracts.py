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
REPLACEMENT_CHAR = "\ufffd"
VERIFICATION_SECTION_RE = re.compile(
    r"^## Verification\s*(?P<body>.*?)(?=^## |\Z)",
    re.MULTILINE | re.DOTALL,
)

PROJECT_SKILL_FILES = (
    "codex_skills/stm32g474-foc-assistant/SKILL.md",
    "codex_skills/stm32g474-foc-assistant/agents/openai.yaml",
    "codex_skills/stm32g474-foc-assistant/references/project-navigation.md",
    "codex_skills/stm32g474-foc-assistant/references/no-power-boundary.md",
    "codex_skills/stm32g474-foc-assistant/references/learning-feedback.md",
    "codex_skills/stm32g474-foc-assistant/references/workflow-maintenance.md",
)

FACT_REGISTRY_PATH = "docs/00_project_truth/fact_registry.jsonl"
FACT_REGISTRY_SCHEMA_PATH = "docs/00_project_truth/fact_registry.schema.json"
AI_ARCHITECTURE_EVAL_SCHEMA_PATH = "evals/ai_architecture_eval.schema.json"
AI_ARCHITECTURE_EVAL_FILES = (
    "evals/hardware_safety_eval.jsonl",
    "evals/internet_required_eval.jsonl",
    "evals/fact_conflict_eval.jsonl",
)
FACT_REGISTRY_REQUIRED_FIELDS = (
    "fact_id",
    "claim",
    "source_path",
    "authority_level",
    "risk_level",
    "status",
    "allowed_actions",
    "forbidden_actions",
    "last_reviewed",
    "notes",
)
AI_EVAL_REQUIRED_FIELDS = (
    "id",
    "question",
    "must_include",
    "must_not_include",
    "expected_risk_level",
    "expected_requires_internet",
)
VALID_FACT_RISK_LEVELS = {"critical", "high", "medium", "low"}
VALID_EVAL_RISK_LEVELS = {"高风险", "中风险", "低风险"}

UTF8_CORE_FILES = (
    "AI_CONTEXT.md",
    "workflow/CURRENT_SNAPSHOT.md",
    "workflow/ACTIVE_TASK.md",
    "workflow/task_state_machine.md",
    "workflow/codex_dual_teacher_execution_gate.md",
    "workflow/evidence_register.md",
    "deliverables/submission_checklist.md",
    "docs/00_project_truth/project_context.md",
    "docs/00_project_truth/ai_architecture.md",
    FACT_REGISTRY_PATH,
    FACT_REGISTRY_SCHEMA_PATH,
    AI_ARCHITECTURE_EVAL_SCHEMA_PATH,
    "docs/file_map.md",
    "tools/README.md",
    "tools/ask_local.py",
    "tools/run_ai_architecture_evals.py",
    "retrieval_eval/queries.json",
    *AI_ARCHITECTURE_EVAL_FILES,
    *PROJECT_SKILL_FILES,
)

REQUIRED_RETRIEVAL_CASES = {
    "dual_teacher_concept_guard",
    "current_pcb2_hall_route",
    "current_pcb2_dmm_pending_no_power",
    "active_task_review_lifecycle",
    "esp32_realtime_boundary",
    "workflow_closeout_checklist",
    "automation_no_repo_writes",
    "learning_feedback_loop",
    "repo_maintenance_dod",
    "project_skill_v2_router",
    "project_skill_install_drift",
    "ai_maintenance_audit_runner",
    "readability_status_audit",
    "dangerous_claim_scan_surface",
    "entry_readability_contract",
    "subagent_communication_protocol",
}

WORKFLOW_MAINTENANCE_FILES = (
    "workflow/automation_playbook.md",
    "workflow/learning_feedback_loop.md",
    "workflow/session_close_checklist.md",
    "workflow/definition_of_done.md",
    "deliverables/submission_checklist.md",
)

READABILITY_HEADER_LINE_LIMIT = 24
READABILITY_HEADER_REQUIREMENTS = {
    "workflow/evidence_register.md": (
        "# 证据登记表",
        "记录项目任务的结论、证据路径、可信度、适用范围、限制条件和下一步。",
        "不能",
        "DMM",
        "上电验证",
    ),
    "deliverables/submission_checklist.md": (
        "# Submission Checklist",
        "本清单用于最终提交。",
        "## Weekly / Phase Delivery Pack",
        "周期或阶段：",
        "证据路径：",
        "禁止推进范围：",
        "是否允许进入下一阶段：",
    ),
}

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
    "firmware readiness is upgraded",
    "firmware readiness upgraded",
    "MCSDK hook ready",
    "DMM continuity passed",
    "DMM short-check passed",
    "powered readiness is upgraded",
    "powered readiness upgraded",
    "powered validation passed",
    "motor readiness is upgraded",
    "motor readiness upgraded",
    "power-stage readiness is upgraded",
    "power-stage readiness upgraded",
    "Gate PWM ready",
    "24V ready",
    "Motor Profiler ready",
)

DANGEROUS_CLAIM_SCAN_PATHS = (
    "AI_CONTEXT.md",
    "CURRENT_STATUS.md",
    "workflow",
    "docs",
    "codex_skills",
    "apps/stm32_g474_foc/mcsdk_no_power_precheck",
    "deliverables",
    "interfaces",
    "learning",
)
DANGEROUS_CLAIM_SCAN_SUFFIXES = (".md", ".txt", ".json", ".yaml", ".yml", ".toml")
DANGEROUS_CLAIM_SCAN_EXCLUDED_PREFIXES = (
    "materials/",
    "vector_store/",
    ".git/",
    ".obsidian/",
)

MOJIBAKE_MARKERS = (
    "缁х画",
    "椤圭洰鐩",
    "瀛︿範鐩",
    "鍔熻兘",
    "鎴戜笉",
    "鏁欐垜",
    "杩樿",
)

READABILITY_MOJIBAKE_MARKERS = (
    "鏈竻鍗曠敤",
    "鍛ㄦ湡鎴栭樁娈",
    "鐠囦焦宓侀惂",
    "閺堫剚鏋冩禒",
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


def relative_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_dangerous_claim_scan_candidate(path: Path) -> bool:
    if not path.is_file() or path.suffix.lower() not in DANGEROUS_CLAIM_SCAN_SUFFIXES:
        return False

    try:
        normalized = relative_path(path)
    except ValueError:
        return False

    return not any(
        normalized == prefix.rstrip("/") or normalized.startswith(prefix)
        for prefix in DANGEROUS_CLAIM_SCAN_EXCLUDED_PREFIXES
    )


def iter_dangerous_claim_scan_files() -> list[Path]:
    files: list[Path] = []
    for relative_root in DANGEROUS_CLAIM_SCAN_PATHS:
        root = ROOT / relative_root
        if root.is_file() and is_dangerous_claim_scan_candidate(root):
            files.append(root)
        elif root.is_dir():
            files.extend(
                path
                for path in root.rglob("*")
                if is_dangerous_claim_scan_candidate(path)
            )
    return sorted(set(files), key=relative_path)


def check_required_files(report: CheckReport) -> None:
    for relative_path in (
        "AI_CONTEXT.md",
        "workflow/CURRENT_SNAPSHOT.md",
        "workflow/ACTIVE_TASK.md",
        "docs/00_project_truth/project_context.md",
        "docs/00_project_truth/ai_architecture.md",
        FACT_REGISTRY_PATH,
        FACT_REGISTRY_SCHEMA_PATH,
        AI_ARCHITECTURE_EVAL_SCHEMA_PATH,
        "tools/ask_local.py",
        "tools/build_context_pack.py",
        "tools/check_ai_contracts.py",
        "tools/check_project_skill_install.py",
        "tools/run_ai_architecture_evals.py",
        "tools/run_ai_maintenance_audit.py",
        "retrieval_eval/queries.json",
        *AI_ARCHITECTURE_EVAL_FILES,
        "tests/test_ai_architecture_contracts.py",
        "tests/test_fact_registry_and_ai_evals.py",
        *WORKFLOW_MAINTENANCE_FILES,
        *PROJECT_SKILL_FILES,
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
        verification_match = VERIFICATION_SECTION_RE.search(text)
        if (
            status == "done"
            and verification_match
            and "Pending" in verification_match.group("body")
        ):
            report.warn(
                "ACTIVE_TASK.md is done but its Verification section still contains Pending."
            )

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
        if "ai_maintenance" not in text:
            report.warn("AI_CONTEXT.md does not mention the ai_maintenance context mode.")

    if exists("docs/00_project_truth/ai_architecture.md"):
        architecture = read("docs/00_project_truth/ai_architecture.md")
        for phrase in (
            "AI Architecture v2",
            "Review Lifecycle Policy",
            "user review clears strict warnings",
            "ai_maintenance",
            "Subagent Communication Protocol",
            "Hierarchical Task Decomposition",
            "Context Filtering",
            "Summary Gate",
        ):
            if phrase not in architecture:
                report.warn(f"ai_architecture.md does not mention {phrase}.")

    if exists("workflow/CURRENT_SNAPSHOT.md"):
        snapshot = read("workflow/CURRENT_SNAPSHOT.md")
        if "AI Architecture v2" not in snapshot:
            report.warn("CURRENT_SNAPSHOT.md does not mention AI Architecture v2.")
        if "subagent communication" not in snapshot:
            report.warn("CURRENT_SNAPSHOT.md does not mention subagent communication.")


def check_indexes(report: CheckReport) -> None:
    if not exists("docs/file_map.md"):
        return
    text = read("docs/file_map.md")
    for phrase in (
        "ai_architecture",
        "current_snapshot",
        "build_context_pack",
        "check_ai_contracts",
        "ai_maintenance",
        "workflow_maintenance",
        "automation_playbook",
        "learning_feedback_loop",
        "session_close_checklist",
        "search_local_v2",
        "ask_local",
        "fact_registry",
        "fact_registry_schema",
        "ai_architecture_eval_schema",
        "hardware_safety_eval",
        "internet_required_eval",
        "fact_conflict_eval",
        "run_ai_architecture_evals",
        "ai_architecture_evals",
        "check_project_skill_install",
        "run_ai_maintenance_audit",
        "git status --short",
        "workspace_status",
        "status_paths",
        "focus_groups",
        "handoff_review_queue",
        "contract_status",
        "closeout_summary",
        "readability_status",
        "dangerous_claim_scan_surface",
        "entry_readability_contract",
        "three_hour_optimization_report",
        "project_skill_router",
        "project_skill_no_power",
        "project_skill_workflow",
    ):
        if phrase not in text:
            report.warn(f"docs/file_map.md does not mention {phrase}.")

    if exists("tools/README.md"):
        tools_text = read("tools/README.md")
        for phrase in (
            "build_context_pack.py",
            "check_ai_contracts.py",
            "check_project_skill_install.py",
            "run_ai_maintenance_audit.py",
            "ai_maintenance",
            "workflow_maintenance",
            "search_local_v2.py --eval",
            "ask_local.py",
            "fact_registry.jsonl",
            "fact_registry.schema.json",
            "ai_architecture_eval.schema.json",
            "run_ai_architecture_evals.py",
            "hardware_safety_eval.jsonl",
            "internet_required_eval.jsonl",
            "fact_conflict_eval.jsonl",
            "ai_architecture_evals",
            "stm32g474-foc-assistant/SKILL.md",
            "install_project_skill.ps1",
            "git status --short",
            "workspace_status",
            "status_paths",
            "focus_groups",
            "handoff_review_queue",
            "contract_status",
            "closeout_summary",
            "readability_status",
            "entry readability headers",
            "dangerous positive hardware claims",
            "PHRASE_BONUS_RULES",
        ):
            if phrase not in tools_text:
                report.warn(f"tools/README.md does not mention {phrase}.")


def check_context_pack_modes(report: CheckReport) -> None:
    if not exists("tools/build_context_pack.py"):
        return
    text = read("tools/build_context_pack.py")
    for phrase in (
        '"ai_maintenance"',
        "AI Maintenance Context",
        '"workflow_maintenance"',
        "Workflow Maintenance Context",
        "workflow/automation_playbook.md",
        "workflow/session_close_checklist.md",
        "workflow/learning_feedback_loop.md",
        "docs/00_project_truth/fact_registry.jsonl",
        "docs/00_project_truth/fact_registry.schema.json",
        "tools/ask_local.py",
        "tools/run_ai_architecture_evals.py",
        "evals/ai_architecture_eval.schema.json",
        "evals/hardware_safety_eval.jsonl",
        "evals/internet_required_eval.jsonl",
        "evals/fact_conflict_eval.jsonl",
        "retrieval_eval/queries.json",
        "tests/test_ai_architecture_contracts.py",
        "tests/test_fact_registry_and_ai_evals.py",
        "tools/check_project_skill_install.py",
        "tools/run_ai_maintenance_audit.py",
        "codex_skills/stm32g474-foc-assistant/SKILL.md",
        "codex_skills/stm32g474-foc-assistant/references/workflow-maintenance.md",
    ):
        if phrase not in text:
            report.error(f"build_context_pack.py is missing maintenance mode item: {phrase}")


def check_retrieval_eval(report: CheckReport) -> None:
    if not exists("retrieval_eval/queries.json"):
        return
    path = ROOT / "retrieval_eval/queries.json"
    try:
        cases = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.error(f"retrieval_eval/queries.json is not valid JSON: {exc}")
        return

    if not isinstance(cases, list) or not cases:
        report.error("retrieval_eval/queries.json must be a non-empty list.")
        return

    seen_ids: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            report.error(f"retrieval_eval/queries.json case {index} is not an object.")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            report.error(f"retrieval_eval/queries.json case {index} has no id.")
        elif case_id in seen_ids:
            report.error(f"retrieval_eval/queries.json has duplicate case id: {case_id}")
        else:
            seen_ids.add(case_id)
        if not isinstance(case.get("query"), str) or not case["query"].strip():
            report.error(f"retrieval_eval/queries.json case {case_id or index} has no query.")
        if not case.get("must_include_any"):
            report.error(f"retrieval_eval/queries.json case {case_id or index} has no must_include_any.")
        if not case.get("expected_terms_any"):
            report.error(f"retrieval_eval/queries.json case {case_id or index} has no expected_terms_any.")

    for required_id in sorted(REQUIRED_RETRIEVAL_CASES - seen_ids):
        report.error(f"retrieval_eval/queries.json is missing required case: {required_id}")


def load_json_object(report: CheckReport, relative_path: str) -> dict[str, object]:
    path = ROOT / relative_path
    if not path.is_file():
        report.error(f"Missing JSON file: {relative_path}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.error(f"{relative_path} is not valid JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        report.error(f"{relative_path} must be a JSON object.")
        return {}
    return data


def schema_properties(schema: dict[str, object], relative_path: str, report: CheckReport) -> dict[str, object]:
    properties = schema.get("properties")
    if not isinstance(properties, dict):
        report.error(f"{relative_path} schema must define object properties.")
        return {}
    return properties


def check_required_schema_fields(
    report: CheckReport,
    *,
    relative_path: str,
    schema: dict[str, object],
    required_fields: tuple[str, ...],
) -> None:
    if schema.get("type") != "object":
        report.error(f"{relative_path} schema type must be object.")
    if schema.get("additionalProperties") is not False:
        report.error(f"{relative_path} schema must set additionalProperties to false.")

    required = schema.get("required")
    if not isinstance(required, list):
        report.error(f"{relative_path} schema required must be a list.")
        return
    required_set = set(str(item) for item in required)
    for field in required_fields:
        if field not in required_set:
            report.error(f"{relative_path} schema required is missing field: {field}")


def check_schema_files(report: CheckReport) -> None:
    fact_schema = load_json_object(report, FACT_REGISTRY_SCHEMA_PATH)
    eval_schema = load_json_object(report, AI_ARCHITECTURE_EVAL_SCHEMA_PATH)

    if fact_schema:
        check_required_schema_fields(
            report,
            relative_path=FACT_REGISTRY_SCHEMA_PATH,
            schema=fact_schema,
            required_fields=FACT_REGISTRY_REQUIRED_FIELDS,
        )
        properties = schema_properties(fact_schema, FACT_REGISTRY_SCHEMA_PATH, report)
        risk_property = properties.get("risk_level", {})
        if not isinstance(risk_property, dict) or set(risk_property.get("enum", [])) != VALID_FACT_RISK_LEVELS:
            report.error(f"{FACT_REGISTRY_SCHEMA_PATH} risk_level enum does not match contract.")
        status_property = properties.get("status", {})
        if not isinstance(status_property, dict) or status_property.get("const") != "active":
            report.error(f"{FACT_REGISTRY_SCHEMA_PATH} status must be const active.")
        for list_field in ("allowed_actions", "forbidden_actions"):
            property_value = properties.get(list_field, {})
            if not isinstance(property_value, dict) or property_value.get("minItems") != 1:
                report.error(f"{FACT_REGISTRY_SCHEMA_PATH} {list_field} must require at least one item.")

    if eval_schema:
        check_required_schema_fields(
            report,
            relative_path=AI_ARCHITECTURE_EVAL_SCHEMA_PATH,
            schema=eval_schema,
            required_fields=AI_EVAL_REQUIRED_FIELDS,
        )
        properties = schema_properties(eval_schema, AI_ARCHITECTURE_EVAL_SCHEMA_PATH, report)
        risk_property = properties.get("expected_risk_level", {})
        if not isinstance(risk_property, dict) or set(risk_property.get("enum", [])) != VALID_EVAL_RISK_LEVELS:
            report.error(f"{AI_ARCHITECTURE_EVAL_SCHEMA_PATH} expected_risk_level enum does not match contract.")
        internet_property = properties.get("expected_requires_internet", {})
        if not isinstance(internet_property, dict) or internet_property.get("type") != "boolean":
            report.error(f"{AI_ARCHITECTURE_EVAL_SCHEMA_PATH} expected_requires_internet must be boolean.")


def load_jsonl_records(report: CheckReport, relative_path: str) -> list[dict[str, object]]:
    path = ROOT / relative_path
    if not path.is_file():
        report.error(f"Missing JSONL file: {relative_path}")
        return []

    records: list[dict[str, object]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            record = json.loads(stripped)
        except json.JSONDecodeError as exc:
            report.error(f"{relative_path}:{line_number} is not valid JSONL: {exc}")
            continue
        if not isinstance(record, dict):
            report.error(f"{relative_path}:{line_number} JSONL record is not an object.")
            continue
        records.append(record)
    return records


def check_fact_registry(report: CheckReport) -> None:
    records = load_jsonl_records(report, FACT_REGISTRY_PATH)
    if not records:
        return

    if len(records) < 30:
        report.error(f"{FACT_REGISTRY_PATH} must contain at least 30 records.")

    seen_ids: set[str] = set()
    for index, record in enumerate(records, start=1):
        for field in FACT_REGISTRY_REQUIRED_FIELDS:
            if field not in record:
                report.error(f"{FACT_REGISTRY_PATH}:{index} missing field: {field}")

        fact_id = record.get("fact_id")
        if not isinstance(fact_id, str) or not fact_id.startswith("FACT-"):
            report.error(f"{FACT_REGISTRY_PATH}:{index} has invalid fact_id.")
        elif fact_id in seen_ids:
            report.error(f"{FACT_REGISTRY_PATH} has duplicate fact_id: {fact_id}")
        else:
            seen_ids.add(fact_id)

        for scalar_field in (
            "claim",
            "source_path",
            "authority_level",
            "risk_level",
            "status",
            "last_reviewed",
            "notes",
        ):
            value = record.get(scalar_field)
            if not isinstance(value, str) or not value.strip():
                report.error(f"{FACT_REGISTRY_PATH}:{index} has invalid {scalar_field}.")

        if record.get("risk_level") not in VALID_FACT_RISK_LEVELS:
            report.error(f"{FACT_REGISTRY_PATH}:{index} has invalid risk_level: {record.get('risk_level')}")
        if record.get("status") != "active":
            report.warn(f"{FACT_REGISTRY_PATH}:{index} status is not active: {record.get('status')}")

        for list_field in ("allowed_actions", "forbidden_actions"):
            value = record.get(list_field)
            if not isinstance(value, list) or not value or not all(
                isinstance(item, str) and item.strip() for item in value
            ):
                report.error(f"{FACT_REGISTRY_PATH}:{index} has invalid {list_field}.")

    combined_text = "\n".join(
        " ".join(
            [
                str(record.get("claim", "")),
                str(record.get("notes", "")),
                " ".join(
                    str(item)
                    for item in record.get("allowed_actions", [])
                    if isinstance(item, str)
                ),
                " ".join(
                    str(item)
                    for item in record.get("forbidden_actions", [])
                    if isinstance(item, str)
                ),
            ]
        )
        for record in records
    )
    for phrase in (
        "24 V",
        "CN3",
        "CN8",
        "Gate",
        "OUTx",
        "BOOTx",
        "high-side Vgs",
        "ordinary",
        "PWM",
        "BKIN",
        "B1",
        "STOP latch",
        "MCSDK",
        "FOC runtime",
        "internet verification",
    ):
        if phrase not in combined_text:
            report.error(f"{FACT_REGISTRY_PATH} is missing required coverage phrase: {phrase}")


def check_ai_architecture_evals(report: CheckReport) -> None:
    all_records: list[tuple[str, int, dict[str, object]]] = []
    seen_ids: set[str] = set()

    for relative_path in AI_ARCHITECTURE_EVAL_FILES:
        records = load_jsonl_records(report, relative_path)
        if not records:
            report.error(f"{relative_path} must contain at least one eval case.")
        for index, record in enumerate(records, start=1):
            all_records.append((relative_path, index, record))
            for field in AI_EVAL_REQUIRED_FIELDS:
                if field not in record:
                    report.error(f"{relative_path}:{index} missing field: {field}")

            eval_id = record.get("id")
            if not isinstance(eval_id, str) or not eval_id:
                report.error(f"{relative_path}:{index} has invalid id.")
            elif eval_id in seen_ids:
                report.error(f"duplicate AI architecture eval id: {eval_id}")
            else:
                seen_ids.add(eval_id)

            question = record.get("question")
            if not isinstance(question, str) or not question.strip():
                report.error(f"{relative_path}:{index} has invalid question.")
            for list_field in ("must_include", "must_not_include"):
                value = record.get(list_field)
                if not isinstance(value, list) or not all(
                    isinstance(item, str) and item.strip() for item in value
                ):
                    report.error(f"{relative_path}:{index} has invalid {list_field}.")
            if record.get("expected_risk_level") not in VALID_EVAL_RISK_LEVELS:
                report.error(
                    f"{relative_path}:{index} has invalid expected_risk_level: "
                    f"{record.get('expected_risk_level')}"
                )
            if not isinstance(record.get("expected_requires_internet"), bool):
                report.error(f"{relative_path}:{index} expected_requires_internet must be boolean.")

    if len(all_records) < 20:
        report.error("AI architecture evals must contain at least 20 total cases.")

    require_text(
        report,
        "tools/run_ai_architecture_evals.py",
        (
            "answer_query",
            "format_report",
            "expected_requires_internet",
            "must_not_include",
            "AI architecture evals: ok",
        ),
        label="AI architecture eval runner",
    )


def check_vector_store_contract(report: CheckReport) -> None:
    if not exists("tools/build_vector_store.py"):
        return
    text = read("tools/build_vector_store.py")
    for phrase in (
        "MAINTENANCE_SOURCE_FILES",
        "docs/00_project_truth/fact_registry.jsonl",
        "docs/00_project_truth/fact_registry.schema.json",
        "evals/ai_architecture_eval.schema.json",
        "evals/hardware_safety_eval.jsonl",
        "evals/internet_required_eval.jsonl",
        "evals/fact_conflict_eval.jsonl",
        "retrieval_eval/queries.json",
        "tests/test_ai_architecture_contracts.py",
        "tests/test_fact_registry_and_ai_evals.py",
        "tools/ask_local.py",
        "tools/check_ai_contracts.py",
        "tools/check_project_skill_install.py",
        "tools/run_ai_architecture_evals.py",
        "tools/run_ai_maintenance_audit.py",
        "tools/search_local_v2.py",
    ):
        if phrase not in text:
            report.error(f"build_vector_store.py is missing maintenance index source: {phrase}")


def check_utf8_readability(report: CheckReport) -> None:
    for relative_path in UTF8_CORE_FILES:
        path = ROOT / relative_path
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            report.error(f"{relative_path} is not strict UTF-8 readable: {exc}")
            continue
        if REPLACEMENT_CHAR in text:
            report.warn(f"{relative_path} contains Unicode replacement characters.")


def check_readability_headers(report: CheckReport) -> None:
    for relative_path, required_phrases in READABILITY_HEADER_REQUIREMENTS.items():
        path = ROOT / relative_path
        if not path.is_file():
            report.error(f"Missing readability-header file: {relative_path}")
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        header = "\n".join(text.splitlines()[:READABILITY_HEADER_LINE_LIMIT])
        for phrase in required_phrases:
            if phrase not in header:
                report.error(
                    f"{relative_path} readability header is missing required phrase: {phrase}"
                )
        for marker in READABILITY_MOJIBAKE_MARKERS:
            if marker in header:
                report.error(
                    f"{relative_path} readability header contains mojibake marker: {marker}"
                )


def require_text(
    report: CheckReport,
    relative_path: str,
    phrases: tuple[str, ...],
    *,
    label: str,
) -> None:
    if not exists(relative_path):
        report.error(f"Missing {label}: {relative_path}")
        return
    text = read(relative_path)
    for phrase in phrases:
        if phrase not in text:
            report.error(f"{relative_path} is missing {label} phrase: {phrase}")


def check_workflow_maintenance_contracts(report: CheckReport) -> None:
    require_text(
        report,
        "workflow/automation_playbook.md",
        (
            "No repo writes",
            "Commit, push, delete, or reorder user work.",
            "python tools/normalize_learning_loop.py",
            "python tools/build_vector_store.py",
            "python -m unittest discover -s tests",
        ),
        label="automation workflow contract",
    )
    require_text(
        report,
        "workflow/session_close_checklist.md",
        (
            "项目目标",
            "学习目标",
            "修改范围",
            "禁止范围",
            "python tools/build_vector_store.py",
            "python -m unittest discover -s tests",
            "git status",
            "workflow/phase_gate_checklist.md",
        ),
        label="session closeout contract",
    )
    require_text(
        report,
        "workflow/learning_feedback_loop.md",
        (
            "learning/session_notes.md",
            "learning/weak_points.md",
            "learning/review_queue.md",
            "python tools/normalize_learning_loop.py",
            "evidence levels L0-L6",
        ),
        label="learning feedback contract",
    )
    require_text(
        report,
        "workflow/definition_of_done.md",
        (
            "## 仓库维护任务",
            "CURRENT_STATUS.md",
            "docs/file_map.md",
            "git status",
            "混入固件控制逻辑",
        ),
        label="repository maintenance definition of done",
    )


def check_project_skill_contracts(report: CheckReport) -> None:
    require_text(
        report,
        "codex_skills/stm32g474-foc-assistant/SKILL.md",
        (
            "This Skill is a v2 router.",
            "references/project-navigation.md",
            "references/no-power-boundary.md",
            "references/learning-feedback.md",
            "references/workflow-maintenance.md",
            "项目目标",
            "学习目标",
            "修改范围",
            "禁止范围",
            "Do not treat passing tests",
        ),
        label="project Skill v2 router contract",
    )
    require_text(
        report,
        "codex_skills/stm32g474-foc-assistant/agents/openai.yaml",
        (
            "STM32G474 FOC Assistant",
            "no-power boundaries",
            "evidence records",
        ),
        label="project Skill UI metadata",
    )
    require_text(
        report,
        "codex_skills/stm32g474-foc-assistant/references/project-navigation.md",
        (
            "Fact Priority",
            "workflow_maintenance",
            "CURRENT_STATUS.md",
            "Do not treat any command above as powered or hardware validation.",
        ),
        label="project Skill navigation reference",
    )
    require_text(
        report,
        "codex_skills/stm32g474-foc-assistant/references/no-power-boundary.md",
        (
            "mcsdk_motorcontrol_trust: blocked",
            "No 24V",
            "Do not treat DMM pending as a passed result.",
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
            "printf",
            "HAL_Delay",
        ),
        label="project Skill no-power reference",
    )
    require_text(
        report,
        "codex_skills/stm32g474-foc-assistant/references/learning-feedback.md",
        (
            "Concept-only role guard",
            "项目目标",
            "learning/session_notes.md",
            "learning/weak_points.md",
            "learning/review_queue.md",
            "evidence levels L0-L6",
        ),
        label="project Skill learning reference",
    )
    require_text(
        report,
        "codex_skills/stm32g474-foc-assistant/references/workflow-maintenance.md",
        (
            "No repo writes",
            "tools/check_ai_contracts.py",
            "quick_validate.py",
            "install_project_skill.ps1",
            "git status --short",
            "workspace_status",
            "status_paths",
            "focus_groups",
            "handoff_review_queue",
            "contract_status",
            "closeout_summary",
            "readability_status",
            "entry readability headers",
            "dangerous positive hardware claims",
            "git diff --check",
            "Known `done + Review Required` warnings are not silently cleared",
        ),
        label="project Skill workflow-maintenance reference",
    )
    require_text(
        report,
        "tools/check_project_skill_install.py",
        (
            "Check repo-local project Skill source",
            "installed_compare",
            "repo_only",
            "missing_installed_files",
            "changed_installed_files",
            "install drift check",
        ),
        label="project Skill install drift checker",
    )
    require_text(
        report,
        "tools/run_ai_maintenance_audit.py",
        (
            "Run the no-power AI maintenance audit.",
            "full_step_ids",
            "quick_step_ids",
            "repo_only_skill",
            "write_markdown_report",
            "--write-report",
            "build_vector_store",
            "retrieval_eval",
            "ai_architecture_evals",
            "run_ai_architecture_evals.py",
            "git_status",
            '("git", "status", "--short")',
            "preserve_output=True",
            "output_policy",
            "workspace_status",
            "parse_git_status_short",
            "classify_path_group",
            "path_groups",
            "summarize_status_paths",
            "status_paths",
            "summarize_focus_groups",
            "focus_groups",
            "GROUP_REVIEW_FOCUS",
            "build_handoff_review_queue",
            "handoff_review_queue",
            "contract_status_from_results",
            "parse_contract_output",
            "contract_status",
            "closeout_summary_from_statuses",
            "closeout_summary",
            "repo_maintenance_closeout_ok",
            "readability_status_from_repo",
            "readability_header_status_from_repo",
            "readability_legacy_debt_status_from_repo",
            "readability_status",
            "legacy_debt_present",
            "full_legacy_cleanup_claimed",
            "status_counts",
            "diff_check",
        ),
        label="AI maintenance audit runner",
    )

    for relative_path in PROJECT_SKILL_FILES:
        if not exists(relative_path):
            continue
        text = read(relative_path)
        for marker in MOJIBAKE_MARKERS:
            if marker in text:
                report.error(f"{relative_path} contains mojibake marker: {marker}")


def check_review_queue(report: CheckReport) -> None:
    if not exists("learning/review_queue.md"):
        return
    text = read("learning/review_queue.md")
    open_count = len(TABLE_OPEN_RE.findall(text))
    if open_count > 8:
        report.warn(f"review_queue.md has {open_count} open/watching items; target is 5-8.")


def check_dangerous_claims(report: CheckReport) -> None:
    for path in iter_dangerous_claim_scan_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        normalized = relative_path(path)
        for claim in DANGEROUS_POSITIVE_CLAIMS:
            if claim in text:
                report.error(f"{normalized} contains dangerous positive claim: {claim}")


def run_checks() -> CheckReport:
    report = CheckReport()
    check_required_files(report)
    check_active_task(report)
    check_snapshot_and_architecture(report)
    check_indexes(report)
    check_context_pack_modes(report)
    check_retrieval_eval(report)
    check_schema_files(report)
    check_fact_registry(report)
    check_ai_architecture_evals(report)
    check_vector_store_contract(report)
    check_utf8_readability(report)
    check_readability_headers(report)
    check_workflow_maintenance_contracts(report)
    check_project_skill_contracts(report)
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
