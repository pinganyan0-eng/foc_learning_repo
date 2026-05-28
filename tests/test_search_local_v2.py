import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SearchLocalV2Tests(unittest.TestCase):
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
