import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

from tools.normalize_learning_loop import normalize_files
from tools.record_learning_session import build_entries, next_weak_id


class RecordLearningSessionTests(unittest.TestCase):
    def test_next_weak_id_uses_highest_existing_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "weak_points.md"
            path.write_text(
                "| ID | Topic | Evidence Level | Symptom | Repair Plan | Next Check | Status |\n"
                "| --- | --- | --- | --- | --- | --- | --- |\n"
                "| WP-001 | A | L1 | s | r | n | open |\n"
                "| WP-009 | B | L1 | s | r | n | open |\n",
                encoding="utf-8",
            )

            self.assertEqual(next_weak_id(path), "WP-010")

    def test_build_entries_reuses_resolved_weak_id_for_review(self):
        args = Namespace(
            date="2026-05-11 08:00",
            topic="State transitions",
            summary="Explained explicit state transitions.",
            evidence="L1",
            confidence="medium",
            weak="Confused event-gated transitions.",
            weak_id="WP-012",
            repair="Write one transition table.",
            next="Explain IDLE -> ARMED -> RUN_SIM.",
            due="next learning turn",
            source="",
        )

        entries = build_entries(args)
        weak_text = next(text for path, text in entries.items() if path.name == "weak_points.md")
        review_text = next(text for path, text in entries.items() if path.name == "review_queue.md")

        self.assertIn("| WP-012 | State transitions |", weak_text)
        self.assertIn("| next learning turn | State transitions |", review_text)
        self.assertIn("| WP-012 | open |", review_text)


class NormalizeLearningLoopTests(unittest.TestCase):
    def test_normalize_assigns_stable_ids_and_updates_review_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            weak_path = Path(tmp) / "weak_points.md"
            review_path = Path(tmp) / "review_queue.md"
            weak_path.write_text(
                "# Weak Points\n\n"
                "| ID | Topic | Evidence Level | Symptom | Repair Plan | Next Check | Status |\n"
                "| --- | --- | --- | --- | --- | --- | --- |\n"
                "| WP-000 | Startup | L0 | none | record | next | open |\n"
                "\n## Update Rules\n\n"
                "| WP-new | Button edge | L1 | held button counted repeatedly | add edge detector | explain last state | open |\n",
                encoding="utf-8",
            )
            review_path.write_text(
                "# Review Queue\n\n"
                "| Due | Topic | Prompt | Source Weak Point | Status |\n"
                "| --- | --- | --- | --- | --- |\n"
                "| next learning turn | Button edge | explain last state | WP-new | open |\n",
                encoding="utf-8",
            )

            result = normalize_files(weak_path, review_path)

            self.assertEqual(result.assigned_ids["Button edge"], "WP-001")
            self.assertIn("| WP-001 | Button edge |", weak_path.read_text(encoding="utf-8"))
            self.assertIn("| next learning turn | Button edge | explain last state | WP-001 | open |", review_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
