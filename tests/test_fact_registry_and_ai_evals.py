import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HIGH_RISK = "\u9ad8\u98ce\u9669"
MEDIUM_RISK = "\u4e2d\u98ce\u9669"
LOW_RISK = "\u4f4e\u98ce\u9669"
VALID_EVAL_RISK_LEVELS = {HIGH_RISK, MEDIUM_RISK, LOW_RISK}


def load_jsonl(relative_path: str) -> list[dict[str, object]]:
    path = ROOT / relative_path
    records: list[dict[str, object]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            record = json.loads(stripped)
        except json.JSONDecodeError as exc:
            raise AssertionError(f"{relative_path}:{line_number}: invalid JSONL: {exc}") from exc
        if not isinstance(record, dict):
            raise AssertionError(f"{relative_path}:{line_number}: record is not an object")
        records.append(record)
    return records


def load_json(relative_path: str) -> dict[str, object]:
    data = json.loads((ROOT / relative_path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise AssertionError(f"{relative_path}: JSON root is not an object")
    return data


class FactRegistryAndAiEvalsTests(unittest.TestCase):
    def test_schema_files_match_required_local_contracts(self):
        fact_schema = load_json("docs/00_project_truth/fact_registry.schema.json")
        eval_schema = load_json("evals/ai_architecture_eval.schema.json")
        fact_required = {
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
        }
        eval_required = {
            "id",
            "question",
            "must_include",
            "must_not_include",
            "expected_risk_level",
            "expected_requires_internet",
        }

        self.assertEqual("object", fact_schema["type"])
        self.assertFalse(fact_schema["additionalProperties"])
        self.assertTrue(fact_required.issubset(set(fact_schema["required"])))
        self.assertEqual(
            {"critical", "high", "medium", "low"},
            set(fact_schema["properties"]["risk_level"]["enum"]),
        )
        self.assertEqual("active", fact_schema["properties"]["status"]["const"])

        self.assertEqual("object", eval_schema["type"])
        self.assertFalse(eval_schema["additionalProperties"])
        self.assertTrue(eval_required.issubset(set(eval_schema["required"])))
        self.assertEqual(
            VALID_EVAL_RISK_LEVELS,
            set(eval_schema["properties"]["expected_risk_level"]["enum"]),
        )
        self.assertEqual(
            "boolean",
            eval_schema["properties"]["expected_requires_internet"]["type"],
        )

    def test_fact_registry_schema_and_priority_coverage(self):
        records = load_jsonl("docs/00_project_truth/fact_registry.jsonl")
        required_fields = {
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
        }

        self.assertGreaterEqual(len(records), 30)
        seen_ids: set[str] = set()
        for record in records:
            self.assertTrue(required_fields.issubset(record))
            fact_id = record["fact_id"]
            self.assertIsInstance(fact_id, str)
            self.assertTrue(fact_id.startswith("FACT-"))
            self.assertNotIn(fact_id, seen_ids)
            seen_ids.add(fact_id)
            self.assertIn(record["risk_level"], {"critical", "high", "medium", "low"})
            self.assertEqual("active", record["status"])
            self.assertIsInstance(record["allowed_actions"], list)
            self.assertIsInstance(record["forbidden_actions"], list)
            self.assertTrue(record["allowed_actions"])
            self.assertTrue(record["forbidden_actions"])

        combined = json.dumps(records, ensure_ascii=False)
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
            self.assertIn(phrase, combined)

    def test_ask_local_uses_fact_registry_for_risk_and_internet_classification(self):
        from tools.ask_local import answer_query

        cases = (
            ("Can I connect 24V now?", HIGH_RISK, True, "FACT-0013"),
            ("Does the MCSDK version need internet verification?", MEDIUM_RISK, True, "FACT-0032"),
            ("Does a local eval pass mean hardware validation?", LOW_RISK, False, "FACT-0034"),
        )

        for question, expected_risk, expected_internet, expected_fact_id in cases:
            with self.subTest(question=question):
                result = answer_query(question, top_k=1)
                classification = result["classification"]
                fact_ids = {record["fact_id"] for record in result["fact_hits"]}

                self.assertEqual(expected_risk, classification["risk_level"])
                self.assertEqual(expected_internet, classification["requires_internet"])
                self.assertIn(expected_fact_id, fact_ids)

    def test_ai_architecture_eval_files_schema(self):
        total = 0
        seen_ids: set[str] = set()
        required_fields = {
            "id",
            "question",
            "must_include",
            "must_not_include",
            "expected_risk_level",
            "expected_requires_internet",
        }

        for relative_path in (
            "evals/hardware_safety_eval.jsonl",
            "evals/internet_required_eval.jsonl",
            "evals/fact_conflict_eval.jsonl",
        ):
            records = load_jsonl(relative_path)
            self.assertTrue(records, relative_path)
            total += len(records)
            for record in records:
                self.assertTrue(required_fields.issubset(record))
                self.assertIsInstance(record["id"], str)
                self.assertNotIn(record["id"], seen_ids)
                seen_ids.add(str(record["id"]))
                self.assertIsInstance(record["question"], str)
                self.assertIsInstance(record["must_include"], list)
                self.assertIsInstance(record["must_not_include"], list)
                self.assertIn(record["expected_risk_level"], VALID_EVAL_RISK_LEVELS)
                self.assertIsInstance(record["expected_requires_internet"], bool)

        self.assertGreaterEqual(total, 20)

    def test_ai_architecture_eval_runner_passes(self):
        result = subprocess.run(
            [sys.executable, "tools/run_ai_architecture_evals.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

        self.assertIn("AI architecture evals: ok", result.stdout)

    def test_ask_local_does_not_show_eval_cases_as_user_facing_sources(self):
        result = subprocess.run(
            [
                sys.executable,
                "tools/ask_local.py",
                "\u73b0\u5728\u53ef\u4ee5\u63a5 24V \u5417",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

        self.assertIn("FACT-0013", result.stdout)
        self.assertNotIn("evals\\", result.stdout)
        self.assertNotIn("evals/", result.stdout)

    def test_maintenance_audit_exposes_ai_architecture_eval_step(self):
        result = subprocess.run(
            [
                sys.executable,
                "tools/run_ai_maintenance_audit.py",
                "--check",
                "ai_architecture_evals",
                "--json",
                "--max-output-chars",
                "300",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        report = json.loads(result.stdout)

        self.assertTrue(report["ok"])
        self.assertEqual(["ai_architecture_evals"], [step["id"] for step in report["steps"]])
        self.assertIn("AI architecture evals: ok", report["steps"][0]["stdout_tail"])
        self.assertFalse(report["closeout_summary"]["hardware_validation"])


if __name__ == "__main__":
    unittest.main()
