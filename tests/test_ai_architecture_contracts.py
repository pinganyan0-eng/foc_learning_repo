import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class AiArchitectureContractTests(unittest.TestCase):
    def test_architecture_and_snapshot_exist_with_safety_boundary(self):
        architecture = read("docs/00_project_truth/ai_architecture.md")
        snapshot = read("workflow/CURRENT_SNAPSHOT.md")

        for phrase in (
            "evidence-first engineering operating system",
            "Context pack",
            "Retrieval",
            "Contract checks",
            "Dual-Teacher Role Policy",
            "Multi-Agent Policy",
            "Concept-only role guard",
            "No 24V",
            "No Gate PWM output",
            "No Motor Profiler run",
            "No powered readiness",
        ):
            self.assertIn(phrase, architecture)

        for phrase in (
            "Current Snapshot",
            "Current PCB2 Route",
            "Current Software Hall State",
            "Current AI Architecture Work",
            "Dual-teacher concept-only role guard",
            "No 24V",
            "No Gate PWM output",
            "No Hall closed-loop claim",
            "No powered readiness",
        ):
            self.assertIn(phrase, snapshot)

    def test_low_token_entry_points_reference_snapshot_and_architecture(self):
        ai_context = read("AI_CONTEXT.md")
        file_map = read("docs/file_map.md")
        tools_readme = read("tools/README.md")

        for phrase in (
            "workflow/CURRENT_SNAPSHOT.md",
            "docs/00_project_truth/ai_architecture.md",
            "Concept-only role guard",
            "ChatGPT teaching turn",
            "Codex reviews and records",
        ):
            self.assertIn(phrase, ai_context)

        for phrase in (
            "ai_architecture",
            "current_snapshot",
            "build_context_pack",
            "check_ai_contracts",
        ):
            self.assertIn(phrase, file_map)

        self.assertIn("build_context_pack.py", tools_readme)
        self.assertIn("check_ai_contracts.py", tools_readme)

    def test_context_pack_tool_outputs_mode_pack(self):
        result = subprocess.run(
            [
                sys.executable,
                "tools/build_context_pack.py",
                "--mode",
                "codex_task",
                "--max-chars",
                "350",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

        self.assertIn("# Codex Task Context", result.stdout)
        self.assertIn("workflow/CURRENT_SNAPSHOT.md", result.stdout)
        self.assertIn("workflow/ACTIVE_TASK.md", result.stdout)
        self.assertIn("no-power context pack only", result.stdout)

    def test_ai_contract_checker_has_no_errors(self):
        result = subprocess.run(
            [sys.executable, "tools/check_ai_contracts.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

        self.assertIn("AI contract errors: none", result.stdout)


if __name__ == "__main__":
    unittest.main()
