from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class ModeSpec:
    title: str
    files: tuple[str, ...]
    purpose: str


COMMON_FILES = (
    "AI_CONTEXT.md",
    "workflow/CURRENT_SNAPSHOT.md",
    "workflow/ACTIVE_TASK.md",
    "docs/00_project_truth/project_context.md",
)

PROJECT_SKILL_FILES = (
    "codex_skills/stm32g474-foc-assistant/SKILL.md",
    "codex_skills/stm32g474-foc-assistant/references/project-navigation.md",
    "codex_skills/stm32g474-foc-assistant/references/no-power-boundary.md",
    "codex_skills/stm32g474-foc-assistant/references/learning-feedback.md",
    "codex_skills/stm32g474-foc-assistant/references/workflow-maintenance.md",
)


MODES: dict[str, ModeSpec] = {
    "codex_task": ModeSpec(
        title="Codex Task Context",
        purpose="Execute the current approved or in-progress repository task.",
        files=COMMON_FILES
        + (
            "workflow/task_state_machine.md",
            "workflow/definition_of_done.md",
            "workflow/risk_gate_matrix.md",
        ),
    ),
    "teaching": ModeSpec(
        title="Teaching Context",
        purpose="Continue a learning turn from current stage and observed weak points.",
        files=COMMON_FILES
        + (
            "workflow/algo_b_teaching_delivery_plan.md",
            "learning/NEXT_LESSON.md",
            "learning/MASTERY_MAP.md",
            "learning/weak_points.md",
            "learning/review_queue.md",
        ),
    ),
    "hardware_review": ModeSpec(
        title="Hardware Review Context",
        purpose="Review hardware-adjacent evidence without opening powered actions.",
        files=COMMON_FILES
        + (
            "workflow/phase_gate_checklist.md",
            "workflow/risk_gate_matrix.md",
            "docs/00_project_truth/project_context.md",
        ),
    ),
    "mcsdk_packet": ModeSpec(
        title="MCSDK Packet Context",
        purpose="Review Packet A/B/C, build-only gates, or generated-source clues.",
        files=COMMON_FILES
        + (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md",
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/future_build_only_gate_2026-05-15.md",
            "workflow/evidence_register.md",
        ),
    ),
    "experiment_analysis": ModeSpec(
        title="Experiment Analysis Context",
        purpose="Analyze logs, serial data, plots, or experiment records.",
        files=COMMON_FILES
        + (
            "experiments/_template/README.md",
            "logs/experiment_000_template.md",
            "workflow/definition_of_done.md",
        ),
    ),
    "report_defense": ModeSpec(
        title="Report And Defense Context",
        purpose="Prepare report, PPT, or defense claims from evidence-backed facts.",
        files=COMMON_FILES
        + (
            "docs/file_map.md",
            "deliverables/submission_checklist.md",
            "workflow/evidence_register.md",
        ),
    ),
    "ai_maintenance": ModeSpec(
        title="AI Maintenance Context",
        purpose="Maintain AI workflow architecture, retrieval, checks, and handoff contracts.",
        files=COMMON_FILES
        + (
            "docs/00_project_truth/ai_architecture.md",
            "docs/00_project_truth/fact_registry.jsonl",
            "docs/00_project_truth/fact_registry.schema.json",
            "workflow/codex_dual_teacher_execution_gate.md",
            "workflow/task_state_machine.md",
            "workflow/definition_of_done.md",
            "tools/ask_local.py",
            "tools/build_context_pack.py",
            "tools/check_ai_contracts.py",
            "tools/check_project_skill_install.py",
            "tools/run_ai_architecture_evals.py",
            "tools/run_ai_maintenance_audit.py",
            "tools/search_local_v2.py",
            "evals/ai_architecture_eval.schema.json",
            "evals/hardware_safety_eval.jsonl",
            "evals/internet_required_eval.jsonl",
            "evals/fact_conflict_eval.jsonl",
            "retrieval_eval/queries.json",
            "tests/test_ai_architecture_contracts.py",
            "tests/test_fact_registry_and_ai_evals.py",
            "docs/file_map.md",
            "tools/README.md",
            *PROJECT_SKILL_FILES,
        ),
    ),
    "workflow_maintenance": ModeSpec(
        title="Workflow Maintenance Context",
        purpose="Maintain project workflow, learning loop, automation boundaries, and closeout checks.",
        files=COMMON_FILES
        + (
            "docs/00_project_truth/ai_architecture.md",
            "workflow/automation_playbook.md",
            "workflow/learning_feedback_loop.md",
            "workflow/session_close_checklist.md",
            "workflow/definition_of_done.md",
            "workflow/task_state_machine.md",
            "deliverables/submission_checklist.md",
            "docs/file_map.md",
            "tools/README.md",
            "docs/00_project_truth/fact_registry.jsonl",
            "docs/00_project_truth/fact_registry.schema.json",
            "tools/ask_local.py",
            "tools/build_context_pack.py",
            "tools/check_ai_contracts.py",
            "tools/check_project_skill_install.py",
            "tools/run_ai_architecture_evals.py",
            "tools/run_ai_maintenance_audit.py",
            "tools/search_local_v2.py",
            "evals/ai_architecture_eval.schema.json",
            "evals/hardware_safety_eval.jsonl",
            "evals/internet_required_eval.jsonl",
            "evals/fact_conflict_eval.jsonl",
            "retrieval_eval/queries.json",
            "tests/test_ai_architecture_contracts.py",
            "tests/test_fact_registry_and_ai_evals.py",
            *PROJECT_SKILL_FILES,
        ),
    ),
}


def read_text(relative_path: str) -> str | None:
    path = ROOT / relative_path
    if not path.exists() or not path.is_file():
        return None
    return path.read_text(encoding="utf-8", errors="ignore")


def excerpt(text: str, max_chars: int) -> str:
    stripped = text.strip()
    if len(stripped) <= max_chars:
        return stripped
    return stripped[:max_chars].rstrip() + "\n\n[...truncated by build_context_pack.py...]"


def render_pack(mode: str, max_chars: int) -> str:
    spec = MODES[mode]
    lines: list[str] = [
        f"# {spec.title}",
        "",
        f"- Mode: `{mode}`",
        f"- Purpose: {spec.purpose}",
        "- Boundary: no-power context pack only; it does not authorize flash, 24V, power-board, motor, Gate PWM, Motor Profiler, Hall closed-loop, or sensorless claims.",
        "",
        "## Source Files",
    ]

    existing_files: list[str] = []
    missing_files: list[str] = []
    for relative_path in dict.fromkeys(spec.files):
        if (ROOT / relative_path).exists():
            existing_files.append(relative_path)
            lines.append(f"- `{relative_path}`")
        else:
            missing_files.append(relative_path)

    if missing_files:
        lines.extend(["", "## Missing Optional Files"])
        lines.extend(f"- `{relative_path}`" for relative_path in missing_files)

    lines.extend(["", "## Context Excerpts"])

    for relative_path in existing_files:
        text = read_text(relative_path)
        if text is None:
            continue
        lines.extend(
            [
                "",
                f"### {relative_path}",
                "",
                "```text",
                excerpt(text, max_chars),
                "```",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Build a low-token context pack for a project task.")
    parser.add_argument(
        "--mode",
        choices=sorted(MODES),
        default="codex_task",
        help="Context mode to generate.",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=2200,
        help="Maximum characters to include per source file.",
    )
    parser.add_argument(
        "--list-modes",
        action="store_true",
        help="Print available modes and exit.",
    )
    args = parser.parse_args()

    if args.list_modes:
        for name, spec in sorted(MODES.items()):
            print(f"{name}: {spec.purpose}")
        return

    print(render_pack(args.mode, max(200, args.max_chars)), end="")


if __name__ == "__main__":
    main()
