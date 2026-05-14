import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_repo_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class CodexDualTeacherGateTests(unittest.TestCase):
    def test_gate_doc_contains_required_opening_and_shape(self):
        text = read_repo_text("workflow/codex_dual_teacher_execution_gate.md")

        for phrase in (
            "项目目标",
            "学习目标",
            "修改范围",
            "禁止范围",
            "继续吧",
            "直接做",
            "开始实操",
            "功能句",
            "规则表",
            "函数职责",
            "代码修改或文档修改",
            "验证",
            "用户检查点",
        ):
            self.assertIn(phrase, text)

    def test_gate_doc_contains_power_boundary(self):
        text = read_repo_text("workflow/codex_dual_teacher_execution_gate.md")

        for phrase in (
            "No 24V",
            "No power board connection",
            "No motor connection",
            "No Gate PWM output",
            "No Motor Profiler run",
            "No Hall closed-loop or sensorless claim",
        ):
            self.assertIn(phrase, text)

    def test_gate_doc_avoids_vague_maybe_wording(self):
        text = read_repo_text("workflow/codex_dual_teacher_execution_gate.md")

        self.assertNotIn("\u53ef\u80fd", text)

    def test_entrypoints_reference_gate_doc(self):
        entrypoints = (
            "AGENTS.md",
            "workflow/teaching_contract.md",
            "workflow/prompt_recipes.md",
            "workflow/session_close_checklist.md",
            "codex_skills/stm32g474-foc-assistant/SKILL.md",
        )

        for relative_path in entrypoints:
            with self.subTest(relative_path=relative_path):
                text = read_repo_text(relative_path)
                self.assertIn("workflow/codex_dual_teacher_execution_gate.md", text)

    def test_codex_role_is_not_redirected_to_chatgpt(self):
        gate = read_repo_text("workflow/codex_dual_teacher_execution_gate.md")
        skill = read_repo_text("codex_skills/stm32g474-foc-assistant/SKILL.md")

        self.assertIn("Codex is the repo writer, verifier, and evidence recorder", gate)
        self.assertIn("Codex is the repo writer, verifier, and evidence recorder", skill)
        self.assertIn("must not say that ChatGPT should do the current Codex-side repo work", gate)
        self.assertIn("do not redirect current Codex-side repo work to ChatGPT", skill)


if __name__ == "__main__":
    unittest.main()
