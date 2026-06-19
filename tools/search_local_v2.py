from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|[\u4e00-\u9fff]")
DEFAULT_MIN_SCORE = 0.18


SOURCE_PRIORITY: tuple[tuple[str, float], ...] = (
    ("workflow/CURRENT_SNAPSHOT.md", 0.18),
    ("docs/00_project_truth/project_context.md", 0.16),
    ("docs/00_project_truth/ai_architecture.md", 0.14),
    ("AI_CONTEXT.md", 0.12),
    ("tools/check_ai_contracts.py", 0.16),
    ("tools/check_project_skill_install.py", 0.16),
    ("tools/run_ai_maintenance_audit.py", 0.16),
    ("codex_skills/stm32g474-foc-assistant/SKILL.md", 0.18),
    ("codex_skills/stm32g474-foc-assistant/references/", 0.16),
    ("workflow/ACTIVE_TASK.md", 0.12),
    ("workflow/codex_dual_teacher_execution_gate.md", 0.12),
    ("workflow/task_state_machine.md", 0.12),
    ("workflow/automation_playbook.md", 0.18),
    ("workflow/learning_feedback_loop.md", 0.18),
    ("workflow/session_close_checklist.md", 0.18),
    ("workflow/definition_of_done.md", 0.18),
    ("docs/protocol.md", 0.12),
    ("templates/jeoc_interrupt_review_template.md", 0.12),
    ("apps/stm32_g474_foc/AGENTS.md", 0.10),
    ("workflow/phase_gate_checklist.md", 0.10),
    ("workflow/risk_gate_matrix.md", 0.10),
    ("apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md", 0.10),
    ("CURRENT_STATUS.md", 0.04),
    ("materials/extracted/", -0.03),
    ("materials/raw/", -0.04),
)

QUERY_EXPANSIONS: tuple[tuple[tuple[str, ...], str], ...] = (
    (
        ("jeoc", "isr", "中断", "printf"),
        "JEOC FOC ISR 禁止 printf HAL_Delay JSON WebSocket dynamic allocation 动态内存 长耗时 实时",
    ),
    (
        ("esp32", "实时", "foc"),
        "STM32 owns FOC ESP32 displays forwards alerts only 不进入 实时 控制环",
    ),
    (
        ("hall", "pa0", "pa1", "pb4", "pb3"),
        "HALL_A HALL_B HALL_C IA IB IC PA0 PA1 PB4 PB3 LIN1 current PCB2 route",
    ),
    (
        ("dmm", "continuity", "short-check", "pending"),
        "PCB2 DMM continuity short-check no-power pending not passed board unpowered no powered action",
    ),
    (
        ("review", "lifecycle", "reviewed", "strict"),
        "ACTIVE_TASK done Review Required reviewed user review clears strict warnings task_state_machine check_ai_contracts",
    ),
    (
        ("ai_maintenance", "contract", "architecture"),
        "AI Architecture v2 ai_maintenance build_context_pack check_ai_contracts retrieval_eval strict warnings dangerous positive claims",
    ),
    (
        ("dangerous claim", "positive claim", "hardware claim", "dmm passed", "gate pwm ready"),
        "check_ai_contracts DANGEROUS_POSITIVE_CLAIMS DANGEROUS_CLAIM_SCAN_PATHS iter_dangerous_claim_scan_files is_dangerous_claim_scan_candidate no-power hardware readiness claim scan surface",
    ),
    (
        (
            "readability",
            "mojibake",
            "乱码",
            "submission checklist",
            "evidence register",
        ),
        "check_ai_contracts READABILITY_HEADER_REQUIREMENTS READABILITY_MOJIBAKE_MARKERS check_readability_headers evidence_register submission_checklist strict UTF-8 readable entry header",
    ),
    (
        ("readability_status", "legacy debt", "legacy mojibake debt", "entry headers ok"),
        "run_ai_maintenance_audit readability_status_from_repo readability_header_status_from_repo readability_legacy_debt_status_from_repo legacy_debt_present full_legacy_cleanup_claimed audit report",
    ),
    (
        ("project skill", "skill v2", "stm32g474-foc-assistant"),
        "stm32g474-foc-assistant Project Skill v2 router references no-power boundary workflow maintenance quick_validate install_project_skill",
    ),
    (
        ("skill install", "install drift", "check_project_skill_install"),
        "check_project_skill_install repo-only installed_compare missing_installed_files changed_installed_files global Skill install drift",
    ),
    (
        ("ai maintenance audit", "run_ai_maintenance_audit", "maintenance audit"),
        "run_ai_maintenance_audit no-power AI maintenance audit quick full repo-only-skill write-report Markdown report build_vector_store retrieval_eval git_status git status --short dirty worktree preserve_output output_policy workspace_status path_groups classify_path_group status_paths summarize_status_paths focus_groups summarize_focus_groups handoff_review_queue build_handoff_review_queue GROUP_REVIEW_FOCUS contract_status contract_status_from_results parse_contract_output closeout_summary closeout_summary_from_statuses repo_maintenance_closeout_ok review lifecycle warnings strict_ready implementation_closeout_ok status_counts paths items full output diff_check",
    ),
    (
        ("workflow_maintenance", "closeout", "收工", "session"),
        "workflow_maintenance session_close_checklist closeout build_vector_store unittest git status phase gate no commit push",
    ),
    (
        ("automation", "automations", "repo writes", "no repo writes"),
        "automation_playbook No repo writes commit push delete reorder user work no generated firmware no hardware parameters",
    ),
    (
        ("learning", "feedback", "weak_points", "review_queue"),
        "learning_feedback_loop session_notes weak_points review_queue normalize_learning_loop evidence levels L0-L6",
    ),
    (
        ("definition", "done", "仓库维护", "repo maintenance"),
        "definition_of_done 仓库维护 CURRENT_STATUS docs/file_map git status no firmware control logic",
    ),
    (
        ("24v", "power", "motor", "gate"),
        "No 24V No power-board connection No motor connection No Gate PWM output phase gate safety boundary",
    ),
)


@dataclass(frozen=True)
class SearchHit:
    final_score: float
    vector_score: float
    source_bonus: float
    phrase_bonus: float
    item: dict


@dataclass(frozen=True)
class PhraseBonusRule:
    name: str
    bonus: float
    query_any: tuple[str, ...] = ()
    text_any: tuple[str, ...] = ()
    path: str = ""


PHRASE_BONUS_RULES: tuple[PhraseBonusRule, ...] = (
    PhraseBonusRule(
        "audit_runner_path",
        0.52,
        query_any=(
            "ai maintenance audit",
            "run_ai_maintenance_audit",
            "maintenance audit runner",
        ),
        path="tools/run_ai_maintenance_audit.py",
    ),
    PhraseBonusRule(
        "readability_status_path",
        0.52,
        query_any=(
            "readability_status",
            "legacy debt",
            "legacy mojibake debt",
            "entry headers ok",
        ),
        path="tools/run_ai_maintenance_audit.py",
    ),
    PhraseBonusRule(
        "readability_contract_path",
        0.52,
        query_any=("readability", "mojibake", "submission checklist", "evidence register"),
        path="tools/check_ai_contracts.py",
    ),
    PhraseBonusRule(
        "workflow_closeout_path",
        0.32,
        query_any=("workflow_maintenance", "closeout", "收工"),
        text_any=("session_close_checklist", "收工检查清单"),
        path="workflow/session_close_checklist.md",
    ),
    PhraseBonusRule(
        "automation_path",
        0.32,
        query_any=("automation",),
        text_any=("no repo writes",),
        path="workflow/automation_playbook.md",
    ),
    PhraseBonusRule(
        "learning_feedback_path",
        0.32,
        query_any=("learning", "feedback"),
        text_any=("learning_feedback_loop", "learning feedback loop"),
        path="workflow/learning_feedback_loop.md",
    ),
    PhraseBonusRule(
        "repo_maintenance_path",
        0.32,
        query_any=("repo maintenance", "仓库维护"),
        text_any=("仓库维护任务",),
        path="workflow/definition_of_done.md",
    ),
)


def normalize_path(path: str) -> str:
    return path.replace("\\", "/")


def tokenize(text: str) -> list[str]:
    raw = [m.group(0).lower() for m in TOKEN_RE.finditer(text)]
    tokens = list(raw)
    chinese = [t for t in raw if len(t) == 1 and "\u4e00" <= t <= "\u9fff"]
    tokens.extend(a + b for a, b in zip(chinese, chinese[1:]))
    return tokens


def expand_query(query: str) -> str:
    lowered = query.lower()
    additions: list[str] = []
    for triggers, expansion in QUERY_EXPANSIONS:
        if any(trigger in lowered for trigger in triggers):
            additions.append(expansion)
    if not additions:
        return query
    return query + " " + " ".join(additions)


def query_vector(query: str, idf: dict[str, float]) -> dict[str, float]:
    counts = Counter(tokenize(expand_query(query)))
    weights = {term: count * idf.get(term, 1.0) for term, count in counts.items()}
    norm = math.sqrt(sum(value * value for value in weights.values())) or 1.0
    return {term: value / norm for term, value in weights.items()}


def vector_score(qv: dict[str, float], dv: dict[str, float]) -> float:
    if len(qv) > len(dv):
        qv, dv = dv, qv
    return sum(weight * dv.get(term, 0.0) for term, weight in qv.items())


def source_bonus(path: str) -> float:
    normalized = normalize_path(path)
    bonus = 0.0
    for prefix, value in SOURCE_PRIORITY:
        if normalized == prefix or normalized.startswith(prefix):
            bonus += value
    return bonus


def contains_any(haystack: str, needles: tuple[str, ...]) -> bool:
    return any(needle in haystack for needle in needles)


def configured_phrase_bonus(
    *,
    query_lower: str,
    text_lower: str,
    normalized_path: str,
) -> float:
    bonus = 0.0
    for rule in PHRASE_BONUS_RULES:
        if rule.query_any and not contains_any(query_lower, rule.query_any):
            continue
        if rule.text_any and not contains_any(text_lower, rule.text_any):
            continue
        if rule.path and normalized_path != rule.path:
            continue
        bonus += rule.bonus
    return bonus


def phrase_bonus(query: str, text: str, path: str = "") -> float:
    query_lower = query.lower()
    query_terms = set(tokenize(query))
    text_lower = text.lower()
    normalized_path = normalize_path(path)
    bonus = configured_phrase_bonus(
        query_lower=query_lower,
        text_lower=text_lower,
        normalized_path=normalized_path,
    )

    if {"j", "e", "o", "c"} & query_terms and "jeoc" in text_lower:
        bonus += 0.03
    if "printf" in query_lower and "printf" in text_lower:
        bonus += 0.06
    if "中断" in query and ("isr" in text_lower or "中断" in text):
        bonus += 0.04
    if "hall" in query_lower and all(term.lower() in text_lower for term in ("pa0", "pa1", "pb4")):
        bonus += 0.08
    if "dmm" in query_lower and "pending" in query_lower and "dmm" in text_lower and "pending" in text_lower:
        bonus += 0.08
    if "review" in query_lower and "lifecycle" in query_lower and ("reviewed" in text_lower or "review required" in text_lower):
        bonus += 0.07
    if "ai_maintenance" in query_lower and "ai_maintenance" in text:
        bonus += 0.07
    if (
        "dangerous" in query_lower
        or "positive claim" in query_lower
        or "hardware claim" in query_lower
    ) and (
        "dangerous_claim_scan_paths" in text_lower
        or "dangerous_positive_claims" in text_lower
    ):
        bonus += 0.16
        if normalized_path == "tools/check_ai_contracts.py":
            bonus += 0.24
    if ("skill" in query_lower or "stm32g474-foc-assistant" in query_lower) and (
        "this skill is a v2 router" in text_lower
        or "project skill maintenance" in text_lower
        or "stm32g474-foc-assistant" in text_lower
    ):
        bonus += 0.16
    if (
        ("workflow_maintenance" in query_lower or "closeout" in query_lower)
        and "session_close_checklist" in text_lower
    ):
        bonus += 0.16
    if "automation" in query_lower and "no repo writes" in text_lower:
        bonus += 0.16
    if ("learning" in query_lower or "feedback" in query_lower) and (
        "learning_feedback_loop" in text_lower or "learning feedback loop" in text_lower
    ):
        bonus += 0.16
    if ("repo maintenance" in query_lower or "仓库维护" in query) and "仓库维护任务" in text:
        bonus += 0.16
    if "esp32" in query_lower and "foc" in text_lower and ("实时" in text or "real-time" in text_lower):
        bonus += 0.06

    return bonus


def load_index() -> tuple[dict, list[dict]]:
    index = json.loads((ROOT / "vector_store" / "index.json").read_text(encoding="utf-8"))
    chunks = [
        json.loads(line)
        for line in (ROOT / "vector_store" / "chunks.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    return index, chunks


def search(query: str, *, limit: int = 5, min_score: float = DEFAULT_MIN_SCORE) -> list[SearchHit]:
    index, chunks = load_index()
    qv = query_vector(query, index["idf"])
    hits: list[SearchHit] = []

    for item in chunks:
        v_score = vector_score(qv, item["vector"])
        s_bonus = source_bonus(item["path"])
        p_bonus = phrase_bonus(query, item["text"], item["path"])
        final = v_score + s_bonus + p_bonus
        if final >= min_score:
            hits.append(SearchHit(final, v_score, s_bonus, p_bonus, item))

    return sorted(hits, key=lambda hit: hit.final_score, reverse=True)[:limit]


def snippet(text: str, limit: int = 300) -> str:
    one_line = re.sub(r"\s+", " ", text).strip()
    return one_line[:limit] + ("..." if len(one_line) > limit else "")


def run_eval(path: Path, *, min_score: float = DEFAULT_MIN_SCORE) -> tuple[bool, list[str]]:
    cases = json.loads(path.read_text(encoding="utf-8"))
    failures: list[str] = []

    for case in cases:
        hits = search(case["query"], limit=5, min_score=min_score)
        hit_paths = [normalize_path(hit.item["path"]) for hit in hits]
        hit_text = "\n".join(hit.item["text"] for hit in hits)

        if not hits:
            failures.append(f"{case['id']}: no hits above min_score={min_score}")
            continue

        expected_paths = [normalize_path(path) for path in case.get("must_include_any", [])]
        if expected_paths and not any(any(hit_path.startswith(expected) for hit_path in hit_paths) for expected in expected_paths):
            failures.append(f"{case['id']}: expected one of {expected_paths}, got {hit_paths}")

        expected_terms = case.get("expected_terms_any", [])
        if expected_terms and not any(term in hit_text for term in expected_terms):
            failures.append(f"{case['id']}: expected one of terms {expected_terms}")

    return not failures, failures


def print_hits(query: str, hits: list[SearchHit], *, min_score: float) -> None:
    print("本地检索 v2")
    print(f"问题：{query}")
    print(f"最低可信分：{min_score:.3f}")
    print()

    if not hits:
        print("结论：仓库本地索引没有找到足够可靠的命中。不要据此做项目或硬件结论。")
        return

    print("结论：下面是本地证据命中，不联网、不替代真实硬件验证。涉及上电、PWM、Gate、Hall/SMO 或电机时，仍以阶段闸门和证据登记为准。")
    print()
    print("命中文件：")
    for rank, hit in enumerate(hits, start=1):
        item = hit.item
        print(
            f"{rank}. {normalize_path(item['path'])}#{item['chunk']} "
            f"score={hit.final_score:.3f} "
            f"(vector={hit.vector_score:.3f}, source={hit.source_bonus:.3f}, phrase={hit.phrase_bonus:.3f})"
        )
        print(f"   {snippet(item['text'])}")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Search local project evidence with source priority and thresholds.")
    parser.add_argument("query", nargs="*", help="Search query.")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--min-score", type=float, default=DEFAULT_MIN_SCORE)
    parser.add_argument("--eval", action="store_true", help="Run retrieval evaluation cases.")
    parser.add_argument("--eval-file", default="retrieval_eval/queries.json")
    args = parser.parse_args()

    if args.eval:
        ok, failures = run_eval(ROOT / args.eval_file, min_score=args.min_score)
        if ok:
            print("retrieval eval: ok")
            return
        print("retrieval eval: failed")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    query = " ".join(args.query).strip()
    if not query:
        print("用法：python tools/search_local_v2.py \"你的问题\"")
        print("评测：python tools/search_local_v2.py --eval")
        raise SystemExit(2)

    print_hits(query, search(query, limit=args.limit, min_score=args.min_score), min_score=args.min_score)


if __name__ == "__main__":
    main()
