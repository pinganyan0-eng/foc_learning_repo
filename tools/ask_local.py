from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|[\u4e00-\u9fff]")


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


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    query = " ".join(sys.argv[1:]).strip()
    if not query:
        print("用法：python tools/ask_local.py \"你的问题\"")
        raise SystemExit(2)

    index = json.loads((ROOT / "vector_store" / "index.json").read_text(encoding="utf-8"))
    chunks = [
        json.loads(line)
        for line in (ROOT / "vector_store" / "chunks.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    qv = query_vector(query, index["idf"])
    ranked = sorted(((score(qv, item["vector"]), item) for item in chunks), reverse=True, key=lambda x: x[0])[:5]

    print("本地检索问答结果")
    print(f"问题：{query}")
    print()
    print("简答：")
    print("下面答案只基于本仓库资料检索，不联网、不替代真实硬件验证。优先按命中的资料片段执行；如果涉及上电或电机运行，先回到限流、波形和故障状态证据。")
    print()
    print("命中文件：")
    for rank, (value, item) in enumerate(ranked, start=1):
        print(f"{rank}. {item['path']}#{item['chunk']} score={value:.3f}")
        print(f"   {snippet(item['text'])}")


if __name__ == "__main__":
    main()
