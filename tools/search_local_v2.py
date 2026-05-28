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
    ("AI_CONTEXT.md", 0.12),
    ("workflow/ACTIVE_TASK.md", 0.12),
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


def phrase_bonus(query: str, text: str) -> float:
    query_terms = set(tokenize(query))
    text_lower = text.lower()
    bonus = 0.0

    if {"j", "e", "o", "c"} & query_terms and "jeoc" in text_lower:
        bonus += 0.03
    if "printf" in query.lower() and "printf" in text_lower:
        bonus += 0.06
    if "中断" in query and ("isr" in text_lower or "中断" in text):
        bonus += 0.04
    if "hall" in query.lower() and all(term.lower() in text_lower for term in ("pa0", "pa1", "pb4")):
        bonus += 0.08
    if "esp32" in query.lower() and "foc" in text_lower and ("实时" in text or "real-time" in text_lower):
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
        p_bonus = phrase_bonus(query, item["text"])
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
