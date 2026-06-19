import subprocess
import sys
import unittest
from pathlib import Path

from tools.search_local_v2 import PHRASE_BONUS_RULES, configured_phrase_bonus, phrase_bonus


ROOT = Path(__file__).resolve().parents[1]


class SearchLocalV2Tests(unittest.TestCase):
    def test_phrase_bonus_rules_keep_path_specific_boosts(self):
        audit_bonus = phrase_bonus(
            "AI maintenance audit runner",
            "repo maintenance handoff",
            "tools/run_ai_maintenance_audit.py",
        )
        unrelated_bonus = phrase_bonus(
            "AI maintenance audit runner",
            "repo maintenance handoff",
            "docs/file_map.md",
        )
        closeout_bonus = phrase_bonus(
            "workflow_maintenance 收工 closeout",
            "session_close_checklist 收工检查清单",
            "workflow/session_close_checklist.md",
        )

        self.assertGreaterEqual(audit_bonus, 0.52)
        self.assertLess(unrelated_bonus, audit_bonus)
        self.assertGreaterEqual(closeout_bonus, 0.48)

    def test_configured_phrase_bonus_table_is_not_half_inlined(self):
        source = (ROOT / "tools/search_local_v2.py").read_text(encoding="utf-8")
        rule_names = {rule.name for rule in PHRASE_BONUS_RULES}
        bonus = configured_phrase_bonus(
            query_lower="workflow_maintenance closeout",
            text_lower="session_close_checklist",
            normalized_path="workflow/session_close_checklist.md",
        )

        self.assertIn("workflow_closeout_path", rule_names)
        self.assertGreaterEqual(bonus, 0.32)
        self.assertNotIn('"收工检查清单" in text', source)

    def test_jeoc_printf_query_hits_realtime_boundary_sources(self):
        result = subprocess.run(
            [sys.executable, "tools/search_local_v2.py", "JEOC 中断里能不能 printf"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

        self.assertIn("本地检索 v2", result.stdout)
        self.assertTrue(
            "docs/protocol.md" in result.stdout
            or "templates/jeoc_interrupt_review_template.md" in result.stdout
            or "apps/stm32_g474_foc/AGENTS.md" in result.stdout
        )
        self.assertIn("printf", result.stdout)

    def test_retrieval_eval_passes(self):
        result = subprocess.run(
            [sys.executable, "tools/search_local_v2.py", "--eval"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

        self.assertIn("retrieval eval: ok", result.stdout)


if __name__ == "__main__":
    unittest.main()
