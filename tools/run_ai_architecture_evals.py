from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.ask_local import answer_query, format_report  # noqa: E402


EVAL_FILES = (
    ROOT / "evals" / "hardware_safety_eval.jsonl",
    ROOT / "evals" / "internet_required_eval.jsonl",
    ROOT / "evals" / "fact_conflict_eval.jsonl",
)

REQUIRED_FIELDS = (
    "id",
    "question",
    "must_include",
    "must_not_include",
    "expected_risk_level",
    "expected_requires_internet",
)


@dataclass(frozen=True)
class EvalFailure:
    eval_id: str
    question: str
    message: str
    output: str


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            record = json.loads(stripped)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSONL: {exc}") from exc
        missing = [field for field in REQUIRED_FIELDS if field not in record]
        if missing:
            raise ValueError(f"{path}:{line_number}: missing required fields: {', '.join(missing)}")
        for list_field in ("must_include", "must_not_include"):
            if not isinstance(record[list_field], list):
                raise ValueError(f"{path}:{line_number}: {list_field} must be a list")
        if not isinstance(record["expected_requires_internet"], bool):
            raise ValueError(f"{path}:{line_number}: expected_requires_internet must be a boolean")
        records.append(record)
    return records


def contains(output: str, phrase: str) -> bool:
    return phrase.lower() in output.lower()


def output_without_question_line(output: str) -> str:
    return "\n".join(line for line in output.splitlines() if not line.startswith("问题："))


def output_for_forbidden_phrase_check(output: str) -> str:
    answer_sections = output.split("\n命中文件：", 1)[0]
    return output_without_question_line(answer_sections)


def evaluate_case(case: dict[str, Any]) -> tuple[bool, str, str]:
    result = answer_query(case["question"], top_k=3)
    output = format_report(result)
    answer_only_output = output_for_forbidden_phrase_check(output)
    classification = result["classification"]
    failures: list[str] = []

    actual_risk = classification["risk_level"]
    if actual_risk != case["expected_risk_level"]:
        failures.append(f"risk level expected {case['expected_risk_level']!r}, got {actual_risk!r}")

    actual_internet = bool(classification["requires_internet"])
    if actual_internet != case["expected_requires_internet"]:
        failures.append(
            f"requires_internet expected {case['expected_requires_internet']!r}, got {actual_internet!r}"
        )

    for phrase in case["must_include"]:
        if not contains(output, str(phrase)):
            failures.append(f"missing required phrase: {phrase!r}")

    for phrase in case["must_not_include"]:
        if contains(answer_only_output, str(phrase)):
            failures.append(f"forbidden phrase present: {phrase!r}")

    return not failures, "\n".join(failures), output


def run_evals(verbose: bool = False) -> int:
    cases: list[dict[str, Any]] = []
    for path in EVAL_FILES:
        cases.extend(load_jsonl(path))

    failures: list[EvalFailure] = []
    for case in cases:
        ok, message, output = evaluate_case(case)
        if verbose or not ok:
            status = "ok" if ok else "FAIL"
            print(f"{status} {case['id']} - {case['question']}")
        if not ok:
            failures.append(
                EvalFailure(
                    eval_id=str(case["id"]),
                    question=str(case["question"]),
                    message=message,
                    output=output,
                )
            )

    if failures:
        print()
        print(f"AI architecture evals: FAIL ({len(failures)}/{len(cases)} failed)")
        for failure in failures:
            print()
            print(f"[{failure.eval_id}] {failure.question}")
            print(failure.message)
            print("Output excerpt:")
            print("\n".join(failure.output.splitlines()[:28]))
        return 1

    print(f"AI architecture evals: ok ({len(cases)} cases)")
    return 0


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Run offline AI architecture safety/retrieval evals.")
    parser.add_argument("--verbose", action="store_true", help="Print every eval case result.")
    args = parser.parse_args()
    raise SystemExit(run_evals(verbose=args.verbose))


if __name__ == "__main__":
    main()
