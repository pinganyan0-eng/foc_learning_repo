from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEARNING = ROOT / "learning"
STABLE_ID_RE = re.compile(r"^WP-(\d{3,})$")


@dataclass
class NormalizeResult:
    weak_rows: int
    review_rows: int
    assigned_ids: dict[str, str]
    removed_weak_duplicates: int
    removed_review_duplicates: int


def split_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    if not cells:
        return None
    if all(set(cell) <= {"-", " ", ":"} for cell in cells):
        return None
    return cells


def table_rows(path: Path, column_count: int, header_first_cell: str) -> list[list[str]]:
    rows: list[list[str]] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        cells = split_table_row(line)
        if cells is None or len(cells) != column_count:
            continue
        if cells[0] == header_first_cell:
            continue
        rows.append(cells)
    return rows


def next_available_id(used_ids: set[str]) -> str:
    highest = 0
    for weak_id in used_ids:
        match = STABLE_ID_RE.match(weak_id)
        if match:
            highest = max(highest, int(match.group(1)))
    while True:
        highest += 1
        candidate = f"WP-{highest:03d}"
        if candidate not in used_ids:
            return candidate


def normalize_weak_rows(rows: list[list[str]]) -> tuple[list[list[str]], dict[str, str], int]:
    normalized: list[list[str]] = []
    assigned_by_topic: dict[str, str] = {}
    used_ids = {row[0] for row in rows if STABLE_ID_RE.match(row[0])}
    seen: set[tuple[str, str, str, str]] = set()
    removed = 0

    for row in rows:
        weak_id, topic, evidence, symptom, repair, next_check, status = row
        key = (topic, symptom, repair, next_check)
        if key in seen:
            removed += 1
            continue
        seen.add(key)

        if not STABLE_ID_RE.match(weak_id):
            weak_id = next_available_id(used_ids)
            used_ids.add(weak_id)
            assigned_by_topic[topic] = weak_id
        else:
            assigned_by_topic.setdefault(topic, weak_id)

        normalized.append([weak_id, topic, evidence, symptom, repair, next_check, status])

    return normalized, assigned_by_topic, removed


def normalize_review_rows(
    rows: list[list[str]], assigned_by_topic: dict[str, str]
) -> tuple[list[list[str]], int]:
    normalized: list[list[str]] = []
    seen: set[tuple[str, str, str, str]] = set()
    removed = 0

    for row in rows:
        due, topic, prompt, source, status = row
        if not STABLE_ID_RE.match(source) and topic in assigned_by_topic:
            source = assigned_by_topic[topic]
        key = (due, topic, prompt, source)
        if key in seen:
            removed += 1
            continue
        seen.add(key)
        normalized.append([due, topic, prompt, source, status])

    return normalized, removed


def render_weak_points(rows: list[list[str]]) -> str:
    table = [
        "| ID | Topic | Evidence Level | Symptom | Repair Plan | Next Check | Status |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    table.extend("| " + " | ".join(row) + " |" for row in rows)
    return (
        "# Weak Points\n\n"
        "Track weak points only when there is evidence from the user's questions, mistakes, explanations, logs, code, measurements, or failed practice.\n\n"
        + "\n".join(table)
        + "\n\n"
        "## Update Rules\n\n"
        "- Do not add a weak point from guesswork alone.\n"
        "- Prefer one precise weak point over a broad label.\n"
        "- Include a concrete next check that can prove improvement.\n"
        "- Close or downgrade weak points only when the user shows evidence at L4 or above.\n"
    )


def render_review_queue(rows: list[list[str]]) -> str:
    table = [
        "| Due | Topic | Prompt | Source Weak Point | Status |",
        "| --- | --- | --- | --- | --- |",
    ]
    table.extend("| " + " | ".join(row) + " |" for row in rows)
    return (
        "# Review Queue\n\n"
        "Use this as a lightweight spaced review queue. Each item should be small enough to check in 3-10 minutes.\n\n"
        + "\n".join(table)
        + "\n\n"
        "## Review Cadence\n\n"
        "- Same day: check whether the user can restate the concept.\n"
        "- Next day: check a small problem or configuration decision.\n"
        "- 3-7 days: check transfer to a new but similar situation.\n"
        "- Before hardware/power actions: re-check safety-critical weak points.\n"
    )


def write_lf(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def normalize_files(
    weak_path: Path = LEARNING / "weak_points.md",
    review_path: Path = LEARNING / "review_queue.md",
    *,
    dry_run: bool = False,
) -> NormalizeResult:
    weak_rows = table_rows(weak_path, 7, "ID")
    review_rows = table_rows(review_path, 5, "Due")

    normalized_weak, assigned_by_topic, removed_weak = normalize_weak_rows(weak_rows)
    normalized_review, removed_review = normalize_review_rows(review_rows, assigned_by_topic)

    if not dry_run:
        write_lf(weak_path, render_weak_points(normalized_weak))
        write_lf(review_path, render_review_queue(normalized_review))

    return NormalizeResult(
        weak_rows=len(normalized_weak),
        review_rows=len(normalized_review),
        assigned_ids=assigned_by_topic,
        removed_weak_duplicates=removed_weak,
        removed_review_duplicates=removed_review,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize weak-point IDs and review queue references.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    result = normalize_files(dry_run=args.dry_run)
    action = "would normalize" if args.dry_run else "normalized"
    print(
        f"{action} {result.weak_rows} weak points and {result.review_rows} review items; "
        f"mapped {len(result.assigned_ids)} topics to stable IDs; "
        f"removed {result.removed_weak_duplicates} weak duplicates and "
        f"{result.removed_review_duplicates} review duplicates"
    )


if __name__ == "__main__":
    main()
