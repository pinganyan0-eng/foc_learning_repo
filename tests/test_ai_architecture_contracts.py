import json
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def load_check_ai_contracts_module():
    spec = importlib.util.spec_from_file_location(
        "check_ai_contracts_under_test",
        ROOT / "tools/check_ai_contracts.py",
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_build_vector_store_module():
    spec = importlib.util.spec_from_file_location(
        "build_vector_store_under_test",
        ROOT / "tools/build_vector_store.py",
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


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
            "AI Architecture v2",
            "Review Lifecycle Policy",
            "Subagent Communication Protocol",
            "Hierarchical Task Decomposition",
            "Context Filtering",
            "Summary Gate",
            "ai_maintenance",
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
            "AI Architecture v2",
            "subagent communication",
            "context filtering",
            "summary gate",
            "ai_maintenance",
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
            "ai_maintenance",
            "user review clears strict warnings",
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

    def test_high_value_readability_headers_are_clean(self):
        checker = read("tools/check_ai_contracts.py")
        evidence = read("workflow/evidence_register.md")
        submission = read("deliverables/submission_checklist.md")

        for phrase in (
            "READABILITY_HEADER_REQUIREMENTS",
            "READABILITY_MOJIBAKE_MARKERS",
            "check_readability_headers",
            "workflow/evidence_register.md",
            "deliverables/submission_checklist.md",
        ):
            self.assertIn(phrase, checker)

        for phrase in (
            "# 证据登记表",
            "记录项目任务的结论、证据路径、可信度、适用范围、限制条件和下一步。",
            "DMM",
            "上电验证",
        ):
            self.assertIn(phrase, "\n".join(evidence.splitlines()[:24]))

        for phrase in (
            "本清单用于最终提交。",
            "周期或阶段：",
            "证据路径：",
            "禁止推进范围：",
            "是否允许进入下一阶段：",
        ):
            self.assertIn(phrase, "\n".join(submission.splitlines()[:24]))

        for marker in (
            "鏈竻鍗曠敤",
            "鍛ㄦ湡鎴栭樁娈",
            "鐠囦焦宓侀惂",
            "閺堫剚鏋冩禒",
        ):
            self.assertNotIn(marker, "\n".join(evidence.splitlines()[:24]))
            self.assertNotIn(marker, "\n".join(submission.splitlines()[:24]))

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

    def test_ai_maintenance_context_pack_is_available(self):
        modes = subprocess.run(
            [sys.executable, "tools/build_context_pack.py", "--list-modes"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertIn("ai_maintenance", modes.stdout)

        result = subprocess.run(
            [
                sys.executable,
                "tools/build_context_pack.py",
                "--mode",
                "ai_maintenance",
                "--max-chars",
                "350",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

        self.assertIn("# AI Maintenance Context", result.stdout)
        self.assertIn("docs/00_project_truth/ai_architecture.md", result.stdout)
        self.assertIn("docs/00_project_truth/fact_registry.jsonl", result.stdout)
        self.assertIn("docs/00_project_truth/fact_registry.schema.json", result.stdout)
        self.assertIn("tools/run_ai_architecture_evals.py", result.stdout)
        self.assertIn("evals/ai_architecture_eval.schema.json", result.stdout)
        self.assertIn("evals/hardware_safety_eval.jsonl", result.stdout)
        self.assertIn("retrieval_eval/queries.json", result.stdout)
        self.assertIn("tools/check_ai_contracts.py", result.stdout)

    def test_workflow_maintenance_context_pack_is_available(self):
        modes = subprocess.run(
            [sys.executable, "tools/build_context_pack.py", "--list-modes"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertIn("workflow_maintenance", modes.stdout)

        result = subprocess.run(
            [
                sys.executable,
                "tools/build_context_pack.py",
                "--mode",
                "workflow_maintenance",
                "--max-chars",
                "350",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

        self.assertIn("# Workflow Maintenance Context", result.stdout)
        self.assertIn("workflow/automation_playbook.md", result.stdout)
        self.assertIn("workflow/session_close_checklist.md", result.stdout)
        self.assertIn("workflow/learning_feedback_loop.md", result.stdout)
        self.assertIn("workflow/definition_of_done.md", result.stdout)
        self.assertIn("tools/check_project_skill_install.py", result.stdout)
        self.assertIn("tools/run_ai_architecture_evals.py", result.stdout)
        self.assertIn("docs/00_project_truth/fact_registry.jsonl", result.stdout)
        self.assertIn("docs/00_project_truth/fact_registry.schema.json", result.stdout)
        self.assertIn("evals/ai_architecture_eval.schema.json", result.stdout)
        self.assertIn("tools/run_ai_maintenance_audit.py", result.stdout)
        self.assertIn("codex_skills/stm32g474-foc-assistant/SKILL.md", result.stdout)
        self.assertIn(
            "codex_skills/stm32g474-foc-assistant/references/workflow-maintenance.md",
            result.stdout,
        )

    def test_project_skill_v2_router_and_references_are_wired(self):
        skill = read("codex_skills/stm32g474-foc-assistant/SKILL.md")
        navigation = read(
            "codex_skills/stm32g474-foc-assistant/references/project-navigation.md"
        )
        no_power = read(
            "codex_skills/stm32g474-foc-assistant/references/no-power-boundary.md"
        )
        learning = read(
            "codex_skills/stm32g474-foc-assistant/references/learning-feedback.md"
        )
        workflow = read(
            "codex_skills/stm32g474-foc-assistant/references/workflow-maintenance.md"
        )

        for phrase in (
            "This Skill is a v2 router.",
            "references/project-navigation.md",
            "references/no-power-boundary.md",
            "references/learning-feedback.md",
            "references/workflow-maintenance.md",
            "项目目标",
            "学习目标",
            "修改范围",
            "禁止范围",
        ):
            self.assertIn(phrase, skill)

        self.assertIn("Fact Priority", navigation)
        self.assertIn("workflow_maintenance", navigation)
        self.assertIn("mcsdk_motorcontrol_trust: blocked", no_power)
        self.assertIn("Do not treat DMM pending as a passed result.", no_power)
        self.assertIn("Concept-only role guard", learning)
        self.assertIn("learning/session_notes.md", learning)
        self.assertIn("No repo writes", workflow)
        self.assertIn("quick_validate.py", workflow)
        self.assertIn("install_project_skill.ps1", workflow)

    def test_project_skill_install_checker_repo_only_json(self):
        result = subprocess.run(
            [
                sys.executable,
                "tools/check_project_skill_install.py",
                "--repo-only",
                "--json",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        report = json.loads(result.stdout)

        self.assertTrue(report["ok"])
        self.assertEqual("repo_only", report["mode"])
        repo_files = {item["path"] for item in report["repo_files"]}
        self.assertTrue(
            {
                "SKILL.md",
                "agents/openai.yaml",
                "references/project-navigation.md",
                "references/no-power-boundary.md",
                "references/learning-feedback.md",
                "references/workflow-maintenance.md",
            }.issubset(repo_files)
        )

    def test_ai_maintenance_audit_quick_repo_only_json(self):
        audit = read("tools/run_ai_maintenance_audit.py")
        for phrase in (
            "contract_status_from_results",
            "parse_contract_output",
            "REVIEW_LIFECYCLE_WARNING_MARKERS",
            "closeout_summary_from_statuses",
            "readability_status_from_repo",
            "readability_header_status_from_repo",
            "readability_legacy_debt_status_from_repo",
        ):
            self.assertIn(phrase, audit)

        command = [
            sys.executable,
            "tools/run_ai_maintenance_audit.py",
            "--quick",
            "--repo-only-skill",
            "--json",
            "--max-output-chars",
            "300",
        ]
        result = subprocess.run(
            command,
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        report = json.loads(result.stdout)

        self.assertTrue(report["ok"])
        self.assertTrue(report["repo_only_skill"])
        self.assertEqual(
            ["project_skill_install", "context_pack", "ai_contracts", "git_status"],
            [step["id"] for step in report["steps"]],
        )
        self.assertEqual("full", report["steps"][-1]["output_policy"])
        workspace_status = report["workspace_status"]
        self.assertTrue(workspace_status["available"])
        self.assertIn("dirty", workspace_status)
        self.assertIn("total", workspace_status)
        self.assertIn("items", workspace_status)
        self.assertIn("path_groups", workspace_status)
        self.assertIn("status_paths", workspace_status)
        self.assertIn("focus_groups", workspace_status)
        self.assertIn("handoff_review_queue", workspace_status)
        if workspace_status["dirty"]:
            self.assertGreater(workspace_status["total"], 0)
            self.assertTrue(workspace_status["status_paths"])
            self.assertGreater(len(workspace_status["focus_groups"]), 0)
            self.assertGreater(len(workspace_status["handoff_review_queue"]), 0)
            first_review_group = workspace_status["handoff_review_queue"][0]["group"]
            self.assertEqual(
                first_review_group,
                workspace_status["focus_groups"][0]["group"],
            )
        else:
            self.assertEqual(0, workspace_status["total"])
            self.assertEqual([], workspace_status["items"])
            self.assertEqual({}, workspace_status["path_groups"])
            self.assertEqual({}, workspace_status["status_paths"])
            self.assertEqual([], workspace_status["focus_groups"])
            self.assertEqual([], workspace_status["handoff_review_queue"])
        self.assertIn("contract_status", report)
        self.assertTrue(report["contract_status"]["available"])
        self.assertEqual(0, report["contract_status"]["error_count"])
        self.assertGreaterEqual(report["contract_status"]["warning_count"], 1)
        self.assertGreaterEqual(
            report["contract_status"]["review_lifecycle_warning_count"],
            1,
        )
        self.assertEqual(0, report["contract_status"]["unexpected_warning_count"])
        self.assertFalse(report["contract_status"]["strict_ready"])
        self.assertTrue(report["contract_status"]["implementation_closeout_ok"])
        self.assertIn("closeout_summary", report)
        self.assertTrue(report["closeout_summary"]["available"])
        self.assertTrue(report["closeout_summary"]["repo_maintenance_closeout_ok"])
        self.assertFalse(report["closeout_summary"]["strict_ready"])
        self.assertTrue(report["closeout_summary"]["needs_user_review"])
        self.assertEqual(
            workspace_status["dirty"],
            report["closeout_summary"]["dirty_worktree"],
        )
        self.assertEqual(
            workspace_status["total"],
            report["closeout_summary"]["dirty_entry_count"],
        )
        if workspace_status["dirty"]:
            self.assertEqual(
                workspace_status["focus_groups"][0]["group"],
                report["closeout_summary"]["next_review_group"],
            )
        else:
            self.assertIsNone(report["closeout_summary"]["next_review_group"])
        self.assertFalse(report["closeout_summary"]["hardware_validation"])
        self.assertTrue(report["closeout_summary"]["no_power_boundary_active"])
        self.assertIn("readability_status", report)
        self.assertTrue(report["readability_status"]["available"])
        self.assertTrue(report["readability_status"]["entry_headers_ok"])
        self.assertTrue(report["readability_status"]["legacy_debt_present"])
        self.assertGreaterEqual(report["readability_status"]["legacy_debt_count"], 1)
        self.assertFalse(report["readability_status"]["full_legacy_cleanup_claimed"])
        self.assertFalse(report["readability_status"]["hardware_validation"])
        self.assertEqual(
            [
                "workflow/evidence_register.md",
                "deliverables/submission_checklist.md",
            ],
            report["readability_status"]["guarded_entry_files"],
        )
        self.assertIn("CURRENT_STATUS.md", report["readability_status"]["legacy_debt_paths"])

    def test_ai_maintenance_audit_preserves_full_git_status_output(self):
        result = subprocess.run(
            [
                sys.executable,
                "tools/run_ai_maintenance_audit.py",
                "--check",
                "git_status",
                "--json",
                "--max-output-chars",
                "1",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        raw_status = subprocess.run(
            ["git", "status", "--short"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        report = json.loads(result.stdout)
        git_status_step = report["steps"][0]

        self.assertEqual("git_status", git_status_step["id"])
        self.assertEqual("full", git_status_step["output_policy"])
        self.assertEqual(raw_status.stdout, git_status_step["stdout_tail"])
        self.assertEqual(
            len(raw_status.stdout.splitlines()),
            report["workspace_status"]["total"],
        )
        self.assertIn("status_counts", report["workspace_status"])
        self.assertIn("paths", report["workspace_status"])
        self.assertIn("path_groups", report["workspace_status"])
        self.assertIn("status_paths", report["workspace_status"])
        self.assertEqual(
            report["workspace_status"]["status_counts"].get("??", 0),
            len(report["workspace_status"]["status_paths"].get("??", [])),
        )
        self.assertIn("focus_groups", report["workspace_status"])
        self.assertGreater(len(report["workspace_status"]["focus_groups"]), 0)
        self.assertIn("handoff_review_queue", report["workspace_status"])
        self.assertGreater(len(report["workspace_status"]["handoff_review_queue"]), 0)
        if "ai_maintenance" in report["workspace_status"]["path_groups"]:
            self.assertIn("ai_maintenance", {
                group["group"] for group in report["workspace_status"]["focus_groups"]
            })

    def test_ai_maintenance_audit_can_write_markdown_report(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = Path(temp_dir) / "audit.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/run_ai_maintenance_audit.py",
                    "--quick",
                    "--repo-only-skill",
                    "--json",
                    "--max-output-chars",
                    "300",
                    "--write-report",
                    str(report_path),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            report = json.loads(result.stdout)
            markdown = report_path.read_text(encoding="utf-8")

        self.assertTrue(report["ok"])
        self.assertEqual(str(report_path), report["report_path"])
        self.assertIn("# AI Maintenance Audit Report", markdown)
        self.assertIn("repository maintenance evidence only", markdown)
        self.assertIn("| Step | Status | Output | Command |", markdown)
        self.assertIn("## Closeout Summary", markdown)
        self.assertIn("Repo maintenance closeout ok", markdown)
        self.assertIn("Hardware validation: False", markdown)
        self.assertIn("## Contract Status", markdown)
        self.assertIn("Review lifecycle warnings are allowed before user review", markdown)
        self.assertIn("### Review Lifecycle Warnings", markdown)
        self.assertIn("## Readability Status", markdown)
        self.assertIn("## Workspace Status", markdown)
        self.assertIn("### Focus Groups", markdown)
        self.assertIn("### Handoff Review Queue", markdown)
        self.assertIn("### Path Groups", markdown)
        self.assertIn("### Status Paths", markdown)
        self.assertIn("This is a parsed `git status --short` handoff summary only.", markdown)
        self.assertIn(
            "This status separates guarded entry headers from broader legacy mojibake debt.",
            markdown,
        )
        self.assertIn("Review AI maintenance scripts", markdown)
        self.assertIn("project_skill_install", markdown)
        self.assertIn("ai_contracts", markdown)
        self.assertIn("git_status", markdown)
        self.assertIn("full", markdown)

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

    def test_ai_contract_checker_covers_workflow_maintenance(self):
        checker = read("tools/check_ai_contracts.py")

        for phrase in (
            "WORKFLOW_MAINTENANCE_FILES",
            "check_workflow_maintenance_contracts",
            "workflow/automation_playbook.md",
            "workflow/session_close_checklist.md",
            "workflow/learning_feedback_loop.md",
            "repo_maintenance_dod",
            "FACT_REGISTRY_PATH",
            "FACT_REGISTRY_SCHEMA_PATH",
            "AI_ARCHITECTURE_EVAL_SCHEMA_PATH",
            "AI_ARCHITECTURE_EVAL_FILES",
            "check_schema_files",
            "check_fact_registry",
            "check_ai_architecture_evals",
            "run_ai_architecture_evals.py",
            "fact_registry.jsonl",
            "fact_registry.schema.json",
            "ai_architecture_eval.schema.json",
            "hardware_safety_eval.jsonl",
            "internet_required_eval.jsonl",
            "fact_conflict_eval.jsonl",
            "ai_architecture_evals",
            "PROJECT_SKILL_FILES",
            "check_project_skill_contracts",
            "check_project_skill_install.py",
            "run_ai_maintenance_audit.py",
            "DANGEROUS_CLAIM_SCAN_PATHS",
            "DANGEROUS_CLAIM_SCAN_SUFFIXES",
            "iter_dangerous_claim_scan_files",
            "is_dangerous_claim_scan_candidate",
            "git_status",
            "git status --short",
            "preserve_output",
            "output_policy",
            "workspace_status",
            "parse_git_status_short",
            "path_groups",
            "classify_path_group",
            "status_paths",
            "summarize_status_paths",
            "focus_groups",
            "summarize_focus_groups",
            "handoff_review_queue",
            "build_handoff_review_queue",
            "GROUP_REVIEW_FOCUS",
            "contract_status",
            "closeout_summary",
            "readability_status",
            "readability_status_from_repo",
            "readability_header_status_from_repo",
            "readability_legacy_debt_status_from_repo",
            "legacy_debt_present",
            "full_legacy_cleanup_claimed",
            "codex_skills/stm32g474-foc-assistant/references/workflow-maintenance.md",
        ):
            self.assertIn(phrase, checker)

    def test_dangerous_claim_scan_surface_is_project_truth_not_tool_constants(self):
        checker = load_check_ai_contracts_module()
        scan_paths = {
            checker.relative_path(path) for path in checker.iter_dangerous_claim_scan_files()
        }

        self.assertIn("CURRENT_STATUS.md", scan_paths)
        self.assertIn("workflow/ACTIVE_TASK.md", scan_paths)
        self.assertIn("docs/00_project_truth/ai_architecture.md", scan_paths)
        self.assertIn(
            "codex_skills/stm32g474-foc-assistant/references/workflow-maintenance.md",
            scan_paths,
        )
        self.assertNotIn("tools/check_ai_contracts.py", scan_paths)
        self.assertTrue(
            checker.is_dangerous_claim_scan_candidate(ROOT / "CURRENT_STATUS.md")
        )
        self.assertFalse(
            checker.is_dangerous_claim_scan_candidate(ROOT / "tools/check_ai_contracts.py")
        )

    def test_ai_contract_checker_warns_for_review_required_but_not_pending_verification(self):
        result = subprocess.run(
            [sys.executable, "tools/check_ai_contracts.py", "--json"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        report = json.loads(result.stdout)

        self.assertIn(
            "ACTIVE_TASK.md is done and still requires review.",
            report["warnings"],
        )
        self.assertNotIn(
            "ACTIVE_TASK.md is done but its Verification section still contains Pending.",
            report["warnings"],
        )

    def test_retrieval_eval_covers_ai_v2_boundaries(self):
        cases = json.loads(read("retrieval_eval/queries.json"))
        case_ids = {case["id"] for case in cases}

        self.assertTrue(
            {
                "dual_teacher_concept_guard",
                "current_pcb2_hall_route",
                "current_pcb2_dmm_pending_no_power",
                "active_task_review_lifecycle",
                "esp32_realtime_boundary",
                "workflow_closeout_checklist",
                "automation_no_repo_writes",
                "learning_feedback_loop",
                "repo_maintenance_dod",
                "project_skill_v2_router",
                "project_skill_install_drift",
                "ai_maintenance_audit_runner",
                "readability_status_audit",
                "dangerous_claim_scan_surface",
                "subagent_communication_protocol",
            }.issubset(case_ids)
        )

    def test_vector_store_indexes_maintenance_source_files(self):
        builder = load_build_vector_store_module()
        source_paths = {
            path.relative_to(ROOT).as_posix()
            for path in builder.source_files()
        }

        self.assertTrue(
            {
                "retrieval_eval/queries.json",
                "docs/00_project_truth/fact_registry.jsonl",
                "docs/00_project_truth/fact_registry.schema.json",
                "evals/ai_architecture_eval.schema.json",
                "evals/hardware_safety_eval.jsonl",
                "evals/internet_required_eval.jsonl",
                "evals/fact_conflict_eval.jsonl",
                "tests/test_ai_architecture_contracts.py",
                "tests/test_fact_registry_and_ai_evals.py",
                "tools/ask_local.py",
                "tools/check_ai_contracts.py",
                "tools/check_project_skill_install.py",
                "tools/run_ai_architecture_evals.py",
                "tools/run_ai_maintenance_audit.py",
                "tools/search_local_v2.py",
            }.issubset(source_paths)
        )


if __name__ == "__main__":
    unittest.main()
