from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FACT_REGISTRY_PATH = ROOT / "docs" / "00_project_truth" / "fact_registry.jsonl"
TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|[\u4e00-\u9fff]")

HIGH_RISK_KEYWORDS = (
    "24v",
    "24 v",
    "gate",
    "gate pwm",
    "outx",
    "out1",
    "out2",
    "out3",
    "bootx",
    "boot1",
    "boot2",
    "boot3",
    "vgs",
    "pwm",
    "dead time",
    "deadtime",
    "motor",
    "hall",
    "sensorless",
    "foc runtime",
    "runtime foc",
    "overcurrent",
    "bkin",
    "nfault",
    "b1",
    "stop latch",
    "电机",
    "接电机",
    "上电",
    "死区",
    "过流",
    "无感",
    "高边",
)

INTERNET_REQUIRED_KEYWORDS = (
    "mcsdk",
    "cubemx",
    "cubeide",
    "stm32cube",
    "hal/ll",
    "codex",
    "openai",
    "plugin",
    "version",
    "stock",
    "replacement",
    "substitute",
    "lcsc",
    "比赛",
    "赛题",
    "规则",
    "报名",
    "提交",
    "库存",
    "替代",
    "替代料",
    "器件",
    "版本",
    "插件",
    "联网",
)

AI_ARCHITECTURE_KEYWORDS = (
    "ask_local",
    "search_local",
    "fact_registry",
    "eval",
    "evals",
    "retrieval",
    "vector_store",
    "ai architecture",
    "本地检索",
    "事实账本",
    "评测",
)

USER_FACING_SOURCE_EXCLUDED_PREFIXES = ("evals/",)

DEFAULT_HARDWARE_FORBIDS = (
    "不授权 24 V / 24V 上电。",
    "不授权接电机或新增功率板连接。",
    "不授权 Gate PWM 输出、Gate 测量或高边 Vgs 测量。",
    "不授权 Motor Pilot / Motor Profiler。",
    "不授权 Hall 闭环、无感/SMO 或 FOC runtime 测试。",
    "本地检索、build、eval 结果都不是硬件验证。",
)

FACT_HINT_RULES: tuple[tuple[tuple[str, ...], tuple[str, ...]], ...] = (
    (("24v", "24 v", "上电"), ("FACT-0013", "FACT-0018", "FACT-0031")),
    (("gate", "pwm", "vgs", "高边"), ("FACT-0015", "FACT-0028", "FACT-0031")),
    (("outx", "out1", "out2", "out3"), ("FACT-0026", "FACT-0027")),
    (("bootx", "boot1", "boot2", "boot3"), ("FACT-0027", "FACT-0028")),
    (("motor", "电机", "接电机"), ("FACT-0014", "FACT-0016", "FACT-0018")),
    (("hall", "sensorless", "无感"), ("FACT-0017", "FACT-0020", "FACT-0033")),
    (("mcsdk", "cubemx", "cubeide", "codex", "比赛", "规则", "库存", "替代"), ("FACT-0002", "FACT-0003", "FACT-0032")),
    (("cn3", "cn8"), ("FACT-0022", "FACT-0023")),
    (("bkin", "nfault", "b1", "stop"), ("FACT-0024", "FACT-0025", "FACT-0029", "FACT-0030")),
    (("eval", "retrieval", "ask_local", "本地检索", "评测"), ("FACT-0018", "FACT-0034")),
)


def tokenize(text: str) -> list[str]:
    raw = [m.group(0).lower() for m in TOKEN_RE.finditer(text)]
    tokens = list(raw)
    chinese = [t for t in raw if len(t) == 1 and "\u4e00" <= t <= "\u9fff"]
    tokens.extend(a + b for a, b in zip(chinese, chinese[1:]))
    return tokens


def query_vector(query: str, idf: dict[str, float]) -> dict[str, float]:
    counts = Counter(tokenize(query))
    weights = {term: count * idf.get(term, 1.0) for term, count in counts.items()}
    norm = math.sqrt(sum(value * value for value in weights.values())) or 1.0
    return {term: value / norm for term, value in weights.items()}


def score(qv: dict[str, float], dv: dict[str, float]) -> float:
    if len(qv) > len(dv):
        qv, dv = dv, qv
    return sum(weight * dv.get(term, 0.0) for term, weight in qv.items())


def snippet(text: str, limit: int = 260) -> str:
    one_line = re.sub(r"\s+", " ", text).strip()
    return one_line[:limit] + ("..." if len(one_line) > limit else "")


def normalized_query(text: str) -> tuple[str, str]:
    lower = text.lower()
    compact = re.sub(r"\s+", "", lower)
    return lower, compact


def keyword_matches(query: str, keywords: tuple[str, ...]) -> list[str]:
    lower, compact = normalized_query(query)
    matches: list[str] = []
    for keyword in keywords:
        key = keyword.lower()
        compact_key = re.sub(r"\s+", "", key)
        if re.search(r"[\u4e00-\u9fff]", key) or " " in key or "/" in key or "-" in key:
            found = key in lower or compact_key in compact
        elif any(char.isdigit() for char in key):
            found = compact_key in compact
        else:
            found = re.search(rf"(?<![a-z0-9_]){re.escape(key)}(?![a-z0-9_])", lower) is not None
        if found:
            matches.append(keyword)
    return matches


def classify_query(query: str) -> dict[str, Any]:
    risk_triggers = keyword_matches(query, HIGH_RISK_KEYWORDS)
    internet_triggers = keyword_matches(query, INTERNET_REQUIRED_KEYWORDS)
    architecture_triggers = keyword_matches(query, AI_ARCHITECTURE_KEYWORDS)
    requires_internet = bool(internet_triggers or risk_triggers)

    if risk_triggers:
        risk_level = "高风险"
        task_type = "硬件安全 / 功率级相关"
    elif internet_triggers:
        risk_level = "中风险"
        task_type = "外部动态事实核查"
    elif architecture_triggers:
        risk_level = "低风险"
        task_type = "AI 架构 / 本地检索维护"
    else:
        risk_level = "低风险"
        task_type = "本地资料检索"

    if internet_triggers and risk_triggers:
        task_type = "硬件安全 + 外部动态事实核查"

    return {
        "task_type": task_type,
        "risk_level": risk_level,
        "requires_internet": requires_internet,
        "risk_triggers": risk_triggers,
        "internet_triggers": internet_triggers,
        "architecture_triggers": architecture_triggers,
    }


def load_fact_registry(path: Path = FACT_REGISTRY_PATH) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    facts: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            record = json.loads(stripped)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSONL in {path} line {line_number}: {exc}") from exc
        record["_line_number"] = line_number
        facts.append(record)
    return facts


def fact_search_text(record: dict[str, Any]) -> str:
    fields: list[str] = [
        str(record.get("fact_id", "")),
        str(record.get("claim", "")),
        str(record.get("source_path", "")),
        str(record.get("risk_level", "")),
        str(record.get("status", "")),
        str(record.get("notes", "")),
    ]
    for key in ("allowed_actions", "forbidden_actions"):
        value = record.get(key, [])
        if isinstance(value, list):
            fields.extend(str(item) for item in value)
        else:
            fields.append(str(value))
    return " ".join(fields)


def hint_fact_ids(query: str) -> set[str]:
    lower, compact = normalized_query(query)
    matched: set[str] = set()
    for keywords, fact_ids in FACT_HINT_RULES:
        for keyword in keywords:
            key = keyword.lower()
            compact_key = re.sub(r"\s+", "", key)
            if key in lower or compact_key in compact:
                matched.update(fact_ids)
                break
    return matched


def rank_fact_hits(query: str, facts: list[dict[str, Any]], limit: int = 6) -> list[dict[str, Any]]:
    query_terms = set(tokenize(query))
    hinted_ids = hint_fact_ids(query)
    ranked: list[tuple[float, dict[str, Any]]] = []
    for record in facts:
        text = fact_search_text(record)
        text_terms = set(tokenize(text))
        overlap = len(query_terms & text_terms)
        exact_bonus = 0
        lower_text = text.lower()
        for term in query_terms:
            if len(term) > 2 and term in lower_text:
                exact_bonus += 1
        hint_bonus = 8 if record.get("fact_id") in hinted_ids else 0
        risk_bonus = 1 if record.get("risk_level") in {"critical", "high"} else 0
        total = overlap + exact_bonus + hint_bonus + risk_bonus
        if total > 0:
            ranked.append((float(total), record))
    ranked.sort(key=lambda item: (-item[0], str(item[1].get("fact_id", ""))))
    return [record for _, record in ranked[:limit]]


def load_vector_index() -> tuple[dict[str, Any], list[dict[str, Any]], str | None]:
    index_path = ROOT / "vector_store" / "index.json"
    chunks_path = ROOT / "vector_store" / "chunks.jsonl"
    if not index_path.exists() or not chunks_path.exists():
        return {}, [], "vector_store index is missing; run python tools/build_vector_store.py first."
    index = json.loads(index_path.read_text(encoding="utf-8"))
    chunks = [json.loads(line) for line in chunks_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return index, chunks, None


def search_local(query: str, top_k: int = 5) -> tuple[list[tuple[float, dict[str, Any]]], str | None]:
    index, chunks, warning = load_vector_index()
    if warning:
        return [], warning
    qv = query_vector(query, index["idf"])
    ranked = sorted(((score(qv, item["vector"]), item) for item in chunks), reverse=True, key=lambda item: item[0])
    filtered = [
        item
        for item in ranked
        if not is_user_facing_excluded_source(str(item[1].get("path", "")))
    ]
    return filtered[:top_k], None


def is_user_facing_excluded_source(path: str) -> bool:
    normalized = path.replace("\\", "/")
    return any(
        normalized == prefix.rstrip("/") or normalized.startswith(prefix)
        for prefix in USER_FACING_SOURCE_EXCLUDED_PREFIXES
    )


def forbidden_reminders(classification: dict[str, Any], fact_hits: list[dict[str, Any]], limit: int = 10) -> list[str]:
    reminders: list[str] = []
    if classification["risk_level"] == "高风险":
        reminders.extend(DEFAULT_HARDWARE_FORBIDS)
    if classification["requires_internet"]:
        reminders.append("涉及联网核查时，离线结果不能替代官方或高可信来源复核。")
    for record in fact_hits:
        forbidden = record.get("forbidden_actions", [])
        if isinstance(forbidden, list):
            reminders.extend(str(item) for item in forbidden)
    deduped: list[str] = []
    seen: set[str] = set()
    for reminder in reminders:
        clean = reminder.strip()
        if clean and clean not in seen:
            seen.add(clean)
            deduped.append(clean)
    return deduped[:limit]


def answer_query(query: str, top_k: int = 5) -> dict[str, Any]:
    classification = classify_query(query)
    facts = load_fact_registry()
    fact_hits = rank_fact_hits(query, facts)
    search_hits, vector_warning = search_local(query, top_k=top_k)
    return {
        "query": query,
        "classification": classification,
        "fact_hits": fact_hits,
        "forbidden_reminders": forbidden_reminders(classification, fact_hits),
        "search_hits": search_hits,
        "vector_warning": vector_warning,
    }


def yes_no(value: bool) -> str:
    return "是" if value else "否"


def short_answer(result: dict[str, Any]) -> str:
    classification = result["classification"]
    if classification["risk_level"] == "高风险":
        return (
            "保守结论：当前本地事实不能授权任何新的上电、24 V、接电机、Gate/PWM、"
            "Hall 闭环、无感或 FOC runtime 测试；只能把检索结果当作 no-power/source-review 线索。"
        )
    if classification["requires_internet"]:
        return "保守结论：这个问题涉及外部动态事实，需要联网核查官方或高可信来源；离线检索只能提供本项目上下文。"
    return "保守结论：下面结果只基于本仓库离线资料检索，不联网，也不替代真实硬件验证。"


def format_fact_hit(record: dict[str, Any], rank: int) -> str:
    fact_id = record.get("fact_id", "UNKNOWN")
    risk = record.get("risk_level", "unknown")
    source = record.get("source_path", "unknown")
    claim = record.get("claim", "")
    return f"{rank}. {fact_id} [{risk}] {claim} (source: {source})"


def format_report(result: dict[str, Any]) -> str:
    classification = result["classification"]
    lines: list[str] = [
        "本地检索问答结果",
        f"问题：{result['query']}",
        "",
        f"任务类型判断：{classification['task_type']}",
        f"风险等级：{classification['risk_level']}",
        f"是否需要联网核查：{yes_no(classification['requires_internet'])}",
    ]

    triggers = classification["risk_triggers"] + classification["internet_triggers"]
    if triggers:
        lines.append(f"触发词：{', '.join(triggers)}")

    lines.extend(["", "命中的结构化事实："])
    if result["fact_hits"]:
        for rank, record in enumerate(result["fact_hits"], start=1):
            lines.append(format_fact_hit(record, rank))
    else:
        lines.append("- 未命中 fact_registry.jsonl；仅使用本地 TF-IDF 检索。")

    lines.extend(["", "禁止动作提醒："])
    if result["forbidden_reminders"]:
        for reminder in result["forbidden_reminders"]:
            lines.append(f"- {reminder}")
    else:
        lines.append("- 本地检索输出不授权硬件动作。")

    lines.extend(["", "简答：", short_answer(result), ""])

    if result["vector_warning"]:
        lines.extend(["命中文件：", f"- {result['vector_warning']}"])
    else:
        lines.append("命中文件：")
        for rank, (value, item) in enumerate(result["search_hits"], start=1):
            lines.append(f"{rank}. {item['path']}#{item['chunk']} score={value:.3f}")
            lines.append(f"   {snippet(item['text'])}")

    return "\n".join(lines)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    query = " ".join(sys.argv[1:]).strip()
    if not query:
        print('用法：python tools/ask_local.py "你的问题"')
        raise SystemExit(2)

    result = answer_query(query)
    print(format_report(result))


if __name__ == "__main__":
    main()
