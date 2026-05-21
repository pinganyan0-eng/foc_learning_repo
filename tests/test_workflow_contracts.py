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


class CurrentPcb2HallPwmStrategyTests(unittest.TestCase):
    def test_strategy_review_exists_and_keeps_no_power_boundary(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "current_pcb2_hall_pwm_strategy_2026-05-19.md"
        )

        for phrase in (
            "No-power strategy review opened / no PCB change first",
            "No 24V",
            "No power-board connection",
            "No motor connection",
            "No Gate PWM output",
            "No Motor Profiler run",
            "No Hall closed-loop validation",
            "No generated-project trust",
        ):
            self.assertIn(phrase, text)

    def test_strategy_review_locks_current_pcb2_hall_and_pb3_roles(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "current_pcb2_hall_pwm_strategy_2026-05-19.md"
        )

        for phrase in (
            "HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10",
            "J_HALL -> IA/IB/IC -> PA0/PA1/PB4",
            "PB3` is current PCB2 `LIN1`, not current PCB2 Hall B",
            "not a same-timer hardware Hall set",
            "software Hall is only a feasibility-review topic",
        ):
            self.assertIn(phrase, text)

    def test_p2_readiness_keeps_packet_a_and_build_only_blocked(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )

        for phrase in (
            "Current PCB2 Hall/PWM strategy",
            "Packet A / firmware feasibility review",
            "Generated-project trust",
            "Not allowed",
            "No-power build-only generated project",
            "Not allowed now",
            "software Hall is not hardware validation",
        ):
            self.assertIn(phrase, text)


class CurrentPcb2PacketAFirmwareFeasibilityTests(unittest.TestCase):
    def test_feasibility_review_exists_and_blocks_packet_a(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "current_pcb2_packet_a_firmware_feasibility_2026-05-19.md"
        )

        for phrase in (
            "No-PCB-change route remains feasibility only / Packet A not accepted",
            "No generated-project trust",
            "No build-only generated-project clearance",
            "not cleared as a standard MCSDK TIM1 complementary PWM",
            "not cleared as a same-timer hardware Hall",
        ):
            self.assertIn(phrase, text)

    def test_feasibility_review_keeps_no_power_scope(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "current_pcb2_packet_a_firmware_feasibility_2026-05-19.md"
        )

        for phrase in (
            "No 24V",
            "No power-board connection",
            "No motor connection",
            "No Gate PWM output",
            "No Motor Profiler run",
            "No Hall closed-loop validation",
            "no source generation",
            "no build-only generated project",
        ):
            self.assertIn(phrase, text)

    def test_readiness_points_to_next_feasibility_decision(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )

        for phrase in (
            "Current PCB2 Packet A / firmware feasibility",
            "Feasibility only / Packet A not accepted",
            "does not open generated-project trust or build-only clearance",
            "deeper software Hall adapter design review",
            "hardware-rework planning task",
        ):
            self.assertIn(phrase, text)


class SoftwareHallAdapterDesignReviewTests(unittest.TestCase):
    def test_software_hall_review_exists_and_keeps_no_power_boundary(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_adapter_design_review_2026-05-19.md"
        )

        for phrase in (
            "software Hall adapter design review",
            "PA0/PA1/PB4",
            "No 24V",
            "No Gate PWM output",
            "No Motor Profiler run",
            "Packet A not accepted",
            "no generated-project trust",
            "hardware-rework planning",
        ):
            self.assertIn(phrase, text)

    def test_software_hall_review_defines_adapter_boundaries(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_adapter_design_review_2026-05-19.md"
        )

        for phrase in (
            "GPIO/EXTI",
            "timestamp Hall edges",
            "valid-state filtering",
            "repeated states",
            "minimal ISR responsibility",
            "MCSDK Integration Boundary",
            "does not define function names",
        ):
            self.assertIn(phrase, text)

    def test_readiness_points_to_software_hall_boundary(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )

        for phrase in (
            "Software Hall adapter design review",
            "Software Hall adapter remains no-power design review / Packet A not accepted",
            "does not add firmware, runtime APIs, generated source, Hall readiness",
            "software Hall adapter design review or hardware-rework planning task",
        ):
            self.assertIn(phrase, text)


class PacketABoardDesignerManagerPathReviewTests(unittest.TestCase):
    def test_board_designer_manager_review_exists_and_blocks_packet_a(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "packet_a_board_designer_manager_path_review_2026-05-19.md"
        )

        for phrase in (
            "Board Designer / Board Manager path",
            "self-developed STDRIVE101 board",
            "Packet A still blocked",
            "no generated-project trust",
            "No 24V",
            "No Gate PWM output",
            "No Motor Profiler run",
        ):
            self.assertIn(phrase, text)

    def test_board_designer_manager_review_separates_built_in_boards(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "packet_a_board_designer_manager_path_review_2026-05-19.md"
        )

        for phrase in (
            "EVALSTDRIVE101",
            "STEVAL-LVLP01",
            "EVLDRIVE101-HPD",
            "custom/user board",
            "project-specific `.stwb6`",
            "selected-field screenshots",
            "hardware-rework planning",
        ):
            self.assertIn(phrase, text)

    def test_readiness_points_to_board_designer_manager_path(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )

        for phrase in (
            "Packet A Board Designer / Board Manager path review",
            "Board Designer / Board Manager path exists as local documentation and tool clue / Packet A still blocked",
            "self-developed STDRIVE101 board",
            "does not open generated-project trust or build-only clearance",
            "surrogate build-only planning without generated-project trust",
        ):
            self.assertIn(phrase, text)


class PacketABoardDesignerManagerGuiChecklistTests(unittest.TestCase):
    def test_gui_checklist_exists_and_keeps_packet_a_blocked(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "packet_a_board_designer_manager_gui_checklist_2026-05-19.md"
        )

        for phrase in (
            "Board Designer / Board Manager",
            "self-developed STDRIVE101 board",
            "GUI-only",
            "No 24V",
            "No Gate PWM output",
            "No Motor Profiler run",
            "Packet A still blocked",
            "no generated-project trust",
        ):
            self.assertIn(phrase, text)

    def test_gui_checklist_defines_screenshots_and_hard_stops(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "packet_a_board_designer_manager_gui_checklist_2026-05-19.md"
        )

        for phrase in (
            "packet_a_sources/2026-05-19_board_designer_manager_path/screenshots/",
            "custom/import/create board",
            "Power Board",
            "Control Board",
            "Inverter Board",
            "Board Aggregation",
            "Finalize/save prompt",
            "Board Manager import/list path",
            "Do not save a placeholder or fake project board",
            "No Generate click",
        ):
            self.assertIn(phrase, text)

    def test_readiness_points_to_gui_checklist(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )

        for phrase in (
            "Packet A Board Designer / Manager GUI-only checklist",
            "GUI-only checklist prepared / Packet A still blocked",
            "packet_a_board_designer_manager_gui_checklist_2026-05-19.md",
            "does not launch GUI or add generated-project trust",
            "stop before Generate, Motor Profiler, Motor Pilot, Flash",
        ):
            self.assertIn(phrase, text)


class MyFocGeneratedProjectReviewTests(unittest.TestCase):
    def test_my_foc_review_exists_and_keeps_packet_a_blocked(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "source_packet_review_2026-05-19_005_my_foc_generated_project.md"
        )

        for phrase in (
            "MY_FOC",
            "SIX_STEP",
            "Packet A not accepted",
            "no generated-project trust",
            "No 24V",
            "No Gate PWM output",
            "No Motor Profiler run",
            "self-developed STDRIVE101 board",
        ):
            self.assertIn(phrase, text)

    def test_my_foc_review_records_editable_pin_mismatch_and_blockers(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "source_packet_review_2026-05-19_005_my_foc_generated_project.md"
        )

        for phrase in (
            "M1_POWERBOARD_NAME=~MY-STDRIVE101_POWER_BOARD",
            "M1_PWM_DRIVER_PN=STDRIVE101",
            "PA15/PB3/PB10",
            "PA0/PA1/PB4",
            "PA8/PB13/PA9/PB14/PA10/PB15",
            "M1_CUR_READING=false",
            "TIM1.BreakState=TIM_BREAK_DISABLE",
            "R57BLB50L2",
            "pins can be changed",
            "not a permanent rejection",
        ):
            self.assertIn(phrase, text)

    def test_readiness_points_to_my_foc_quarantine(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )

        for phrase in (
            "MY_FOC generated project source review",
            "generated project quarantined / Packet A not accepted",
            "SIX_STEP",
            "pins can be changed",
            "No generated-project trust",
        ):
            self.assertIn(phrase, text)


class MyFocFocCandidateEditTests(unittest.TestCase):
    def test_my_foc_manual_foc_edit_rollback_is_recorded(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "my_foc_foc_candidate_edit_2026-05-19.md"
        )

        for phrase in (
            "Manual FOC source edit failed Workbench reload / rolled back / Packet A still not accepted",
            "MY_FOC.stwb6",
            "一般错误",
            "无法加载文件",
            "rolled back",
            "\"algorithm\": \"sixStep\"",
            "\"algorithm\": \"FOC\"",
            "pre_codex_foc_edit_2026-05-19.bak",
            "MY_FOC.codex_foc_candidate_2026-05-19.stwb6",
            "no generated-project trust",
        ):
            self.assertIn(phrase, text)

    def test_my_foc_foc_candidate_edit_keeps_no_power_boundary(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "my_foc_foc_candidate_edit_2026-05-19.md"
        )

        for phrase in (
            "No Generate",
            "No build",
            "No flash",
            "No 24V",
            "No Gate PWM output",
            "No Motor Profiler run",
            "R57BLB50L2",
            "Number.NaN",
            "generated six-step outputs",
        ):
            self.assertIn(phrase, text)


class PacketAFocRouteDecisionTests(unittest.TestCase):
    def test_route_decision_exists_and_blocks_packet_a(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "packet_a_foc_route_decision_2026-05-19.md"
        )

        for phrase in (
            "Route narrowed / GUI-created FOC source required / Packet A still blocked",
            "My_First_FOC.stwb6",
            "MY_FOC.original_2026-05-19.stwb6",
            "MY_FOC.codex_foc_candidate_2026-05-19.stwb6",
            "Do not attempt another partial text edit",
            "self-developed STDRIVE101 board",
            "No Generate",
            "No 24V",
            "no generated-project trust",
        ):
            self.assertIn(phrase, text)

    def test_route_decision_defines_next_capture_fields(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "packet_a_foc_route_decision_2026-05-19.md"
        )

        for phrase in (
            "FOC or field-oriented control",
            "NUCLEO-G474RE",
            "custom/user STDRIVE101 board",
            "Current sensing selected",
            "Fault / break path selected",
            "Hall or speed-sensor route",
            "PWM route selected",
            "Motor entry labeled as a source-level candidate",
        ):
            self.assertIn(phrase, text)

    def test_readiness_keeps_route_decision_and_active_task_points_to_foc_capture(self):
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        active_task = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        capture = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "packet_a_sources/2026-05-16_custom_nucleo_stdrive101/"
            "workbench_foc_capture_success_2026-05-21.md"
        )

        for phrase in (
            "Packet A FOC route decision after MY_FOC rollback",
            "Route narrowed / GUI-created FOC source required / Packet A still blocked",
            "complete reviewable FOC source",
        ):
            self.assertIn(phrase, readiness)

        for phrase in (
            "TASK-2026-05-21-packet-a-workbench-foc-source-capture",
            "EV-2026-05-21-P2-WORKBENCH-FOC-SOURCE-CAPTURE-001",
            "Workbench FOC source captured / no-power Packet A source evidence upgraded / hardware and build trust still blocked",
            "`algorithm`: `FOC`",
            "`MY-STDRIVE101_POWER_BOARD`",
            "`PB12/TIM1_BKIN`",
            "No Gate PWM output",
            "No Motor Profiler",
        ):
            self.assertIn(phrase, active_task + register + capture)


class PacketCStdrive101ProtectionDetailReviewTests(unittest.TestCase):
    def test_packet_c_detail_review_exists_and_keeps_p3_blocked(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "packet_c_stdrive101_protection_detail_review_2026-05-20.md"
        )

        for phrase in (
            "Packet C detail narrowed / protection proof still partial clue / P3 still blocked",
            "no powered readiness",
            "No 24V",
            "No Gate PWM output",
            "No Motor Profiler run",
            "No source generation, build, flash",
            "Packet C is more precise but still not accepted",
        ):
            self.assertIn(phrase, text)

    def test_packet_c_detail_review_downgrades_old_threshold_claim(self):
        detail = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "packet_c_stdrive101_protection_detail_review_2026-05-20.md"
        )
        thresholds = read_repo_text("docs/03_hardware_notes/protection_thresholds.md")
        combined = " ".join((detail + thresholds).split())

        for phrase in (
            "VDSth = VSCREF",
            "VSCREF,en = 2.54 V",
            "VSCREF,dis = 2.9 V",
            "33k / 20k",
            "1.245 V",
            "55A",
            "Not accepted",
            "must not be used",
            "CP -> 100nF -> GND",
            "does not prove the CP overcurrent comparator input network",
        ):
            self.assertIn(phrase, combined)

    def test_packet_c_detail_is_linked_from_readiness_and_active_task(self):
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        active_task = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")

        for phrase in (
            "Packet C STDRIVE101 protection detail review",
            "Packet C detail narrowed / protection proof still partial clue / P3 still blocked",
            "old `55A` VDS claim is not accepted",
            "EV-2026-05-20-P2-PACKET-C-STDRIVE101-PROTECTION-DETAIL-001",
            "TASK-2026-05-20-p2-packet-c-stdrive101-protection-detail-review",
        ):
            self.assertIn(phrase, readiness + active_task + register)


if __name__ == "__main__":
    unittest.main()
