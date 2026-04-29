from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "vector_store"
TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|[\u4e00-\u9fff]")


def tokenize(text: str) -> list[str]:
    raw = [m.group(0).lower() for m in TOKEN_RE.finditer(text)]
    tokens = list(raw)
    chinese = [t for t in raw if len(t) == 1 and "\u4e00" <= t <= "\u9fff"]
    tokens.extend(a + b for a, b in zip(chinese, chinese[1:]))
    return tokens


def chunk_text(text: str, size: int = 1200) -> list[str]:
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks: list[str] = []
    current = ""
    for para in paras:
        if len(para) > size:
            if current:
                chunks.append(current.strip())
                current = ""
            for start in range(0, len(para), size):
                part = para[start : start + size].strip()
                if part:
                    chunks.append(part)
            continue
        if len(current) + len(para) + 2 > size and current:
            chunks.append(current.strip())
            current = para
        else:
            current = f"{current}\n\n{para}".strip()
    if current:
        chunks.append(current.strip())
    return chunks


def source_files() -> list[Path]:
    files: list[Path] = []
    files.extend(p for p in ROOT.glob("*.md") if p.is_file())
    for folder in [
        "apps",
        "assets",
        "deliverables",
        "docs",
        "experiments",
        "interfaces",
        "materials",
        "materials/extracted",
        "references",
        "templates",
        "tools",
        "workflow",
    ]:
        base = ROOT / folder
        if base.exists():
            files.extend(sorted(p for p in base.rglob("*") if p.suffix.lower() in {".md", ".txt"}))
    return sorted(set(files))


def main() -> None:
    OUT.mkdir(exist_ok=True)
    chunks = []
    df: dict[str, int] = defaultdict(int)

    for path in source_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for i, chunk in enumerate(chunk_text(text)):
            terms = Counter(tokenize(chunk))
            if not terms:
                continue
            for term in terms:
                df[term] += 1
            chunks.append(
                {
                    "id": f"{path.as_posix()}#{i}",
                    "path": str(path.relative_to(ROOT)),
                    "chunk": i,
                    "text": chunk,
                    "tf": dict(terms),
                }
            )

    total = max(len(chunks), 1)
    idf = {term: math.log((1 + total) / (1 + freq)) + 1.0 for term, freq in df.items()}
    for item in chunks:
        weights = {term: count * idf[term] for term, count in item.pop("tf").items()}
        norm = math.sqrt(sum(value * value for value in weights.values())) or 1.0
        item["vector"] = {term: value / norm for term, value in weights.items()}

    (OUT / "chunks.jsonl").write_text(
        "\n".join(json.dumps(item, ensure_ascii=False) for item in chunks) + "\n",
        encoding="utf-8",
    )
    (OUT / "index.json").write_text(
        json.dumps({"chunks": len(chunks), "idf": idf}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"built {len(chunks)} chunks")


if __name__ == "__main__":
    main()
