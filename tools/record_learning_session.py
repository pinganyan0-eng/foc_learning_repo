from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEARNING = ROOT / "learning"
WEAK_ID_RE = re.compile(r"\|\s*WP-(\d{3,})\s*\|")


def append(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    separator = "" if existing.endswith("\n") or not existing else "\n"
    path.write_text(existing + separator + text.strip() + "\n", encoding="utf-8")


def next_weak_id(path: Path = LEARNING / "weak_points.md") -> str:
    if not path.exists():
        return "WP-001"

    highest = 0
    for match in WEAK_ID_RE.finditer(path.read_text(encoding="utf-8", errors="ignore")):
        highest = max(highest, int(match.group(1)))
    return f"WP-{highest + 1:03d}"


def build_entries(args: argparse.Namespace) -> dict[Path, str]:
    now = args.date or datetime.now().strftime("%Y-%m-%d %H:%M")
    source = f"\n- Source: {args.source}" if args.source else ""

    session = f"""
## {now} {args.topic}

- Summary: {args.summary}
- Evidence level: {args.evidence}
- Confidence: {args.confidence}
- Weak point observed: {args.weak or "None recorded."}
- Next review: {args.next or "None recorded."}{source}
"""

    entries: dict[Path, str] = {LEARNING / "session_notes.md": session}

    if args.weak:
        weak = f"| {args.weak_id} | {args.topic} | {args.evidence} | {args.weak} | {args.repair or args.next or 'Define a repair task.'} | {args.next or 'Next learning turn'} | open |"
        entries[LEARNING / "weak_points.md"] = weak

    if args.next:
        review = f"| {args.due} | {args.topic} | {args.next} | {args.weak_id if args.weak else '-'} | open |"
        entries[LEARNING / "review_queue.md"] = review

    return entries


def main() -> None:
    parser = argparse.ArgumentParser(description="Append a structured learning session record.")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--weak", default="")
    parser.add_argument("--weak-id", default="WP-new")
    parser.add_argument("--repair", default="")
    parser.add_argument("--next", default="")
    parser.add_argument("--due", default="next learning turn")
    parser.add_argument("--evidence", default="L1")
    parser.add_argument("--confidence", default="medium")
    parser.add_argument("--source", default="")
    parser.add_argument("--date", default="")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.weak and args.weak_id == "WP-new":
        args.weak_id = next_weak_id()

    entries = build_entries(args)
    for path, text in entries.items():
        if args.dry_run:
            print(f"--- {path.relative_to(ROOT)}")
            print(text.strip())
        else:
            append(path, text)


if __name__ == "__main__":
    main()
