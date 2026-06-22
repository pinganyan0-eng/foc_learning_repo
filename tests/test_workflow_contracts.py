import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_repo_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def assert_current_nfault_fault_tree_checkpoint(testcase: unittest.TestCase, checkpoint: str):
    for phrase in (
        "The current repo-side checkpoint is complete through the STDRIVE101 nFAULT 1.3V\n"
        "fault-tree no-power plan",
        "stdrive101_nfault_1v3_fault_tree_no_power_plan_2026-06-22.md",
        "not as motor power-up permission",
        "Do not repeat residual-voltage isolation",
        "the same candidate 24 V static scope\ncheck",
        "the motor-connected open-loop run",
        "the `LIN1` powered wake",
        "or any\n`HIN1` comparison unless",
        "separate dated teacher-\nreviewed phase gate opens the action",
    ):
        testcase.assertIn(phrase, checkpoint)


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

    def test_concept_only_turns_are_handed_to_chatgpt(self):
        gate = read_repo_text("workflow/codex_dual_teacher_execution_gate.md")
        ai_context = read_repo_text("AI_CONTEXT.md")
        teaching_contract = read_repo_text("workflow/teaching_contract.md")
        skill = read_repo_text("codex_skills/stm32g474-foc-assistant/SKILL.md")
        status = read_repo_text("CURRENT_STATUS.md")
        evidence = read_repo_text("workflow/evidence_register.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")

        combined = "\n".join(
            (gate, ai_context, teaching_contract, skill, status, evidence, active)
        )

        for phrase in (
            "Concept-Only Role Guard",
            "Concept-only role guard",
            "Codex must not teach the full lesson",
            "ChatGPT teaching turn",
            "provide a concrete ChatGPT prompt or task packet",
            "ChatGPT may create a GitHub branch / PR for learning evidence",
            "GitHub learning-evidence handoff",
            "accepted repo-state change until Codex reviews, syncs, verifies",
            "这是 ChatGPT 主讲场景，不是 Codex 工程执行场景",
            "学完后把你的答案/总结贴回 Codex",
            "Codex reviews and records",
            "Dual-teacher concept-only role guard / ChatGPT teaches theory / Codex reviews records and executes repo work",
            "EV-2026-05-28-WORKFLOW-DUAL-TEACHER-CONCEPT-GUARD-001",
            "TASK-2026-05-28-workflow-dual-teacher-concept-guard",
        ):
            self.assertIn(phrase, combined)


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

    def test_p2_readiness_records_build_only_pass_without_hardware_upgrade(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )

        for phrase in (
            "Current PCB2 Hall/PWM strategy",
            "Packet A / firmware feasibility review",
            "Generated-project trust",
            "Build-only Debug pass recorded / no runtime or hardware trust",
            "No-power build-only generated project",
            "Passed on local STM32Cube bundled toolchain",
            "ninja: no work to do",
            "software Hall is not hardware validation",
        ):
            self.assertIn(phrase, text)

    def test_no_power_build_only_result_records_compile_evidence_only(self):
        result = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "build_only_result_2026-05-27_qiansai_g474_stdrive101_foc_p2_debug.md"
        )
        combined = (
            result
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
                "future_build_only_gate_2026-05-15.md"
            )
        )

        for phrase in (
            "No-power build-only Debug pass / local toolchain compiles generated project / no firmware runtime or hardware readiness",
            "TASK-2026-05-27-p2-qiansai-g474-stdrive101-foc-p2-debug-build-only",
            "EV-2026-05-27-P2-QIANSAI-G474-STDRIVE101-FOC-P2-BUILD-ONLY-001",
            "cmake --build",
            "Exit code: 0",
            "ninja: no work to do",
            "QIANSAI_G474_STDRIVE101_FOC_P2.elf",
            "QIANSAI_G474_STDRIVE101_FOC_P2.map",
            "not a clean rebuild record",
            "No flash",
            "No Gate PWM output",
            "No Hall closed-loop claim",
            "current PCB2 physical routing",
            "Gate PWM waveform safety",
        ):
            self.assertIn(phrase, combined)


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


class DmmContinuityShortCheckRequestTests(unittest.TestCase):
    def test_dmm_request_exists_and_blocks_software_hall_implementation(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "dmm_continuity_short_check_request_2026-05-22.md"
        )

        for phrase in (
            "DMM Continuity / Short-Check Request",
            "Power off only",
            "Do not connect 24V",
            "IA` / `HALL_A",
            "PA0",
            "IB` / `HALL_B",
            "PA1",
            "IC` / `HALL_C",
            "PB4",
            "`LIN1`",
            "`PB3`",
            "`3V3`",
            "`P14`",
            "`GND`",
            "`P15`",
            "`nFAULT`",
            "`PB12`",
            "`3V3` to `GND`",
            "`IA` to `IB`",
            "software Hall adapter implementation readiness",
            "This request is complete only after the user returns the filled DMM table",
        ):
            self.assertIn(phrase, text)

    def test_readiness_prioritizes_dmm_before_software_hall_code(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )

        for phrase in (
            "DMM continuity / short-check request",
            "Requested / no measurement result yet / software Hall implementation blocked",
            "not the current real-world hardware-progress blocker",
            "Do this before any software Hall adapter implementation",
            "P2 still cannot flash, power, connect, or run a motor-control project",
        ):
            self.assertIn(phrase, text)


class SoftwareHallNoPowerAlgorithmPrepTests(unittest.TestCase):
    def test_algorithm_prep_exists_and_keeps_no_power_boundary(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_no_power_algorithm_prep_2026-05-22.md"
        )

        for phrase in (
            "Software Hall No-Power Algorithm Prep",
            "中文速读版",
            "中文规则表",
            "中文练习表",
            "中文中断边界",
            "中文验收点",
            "Algorithm-side no-power preparation / no firmware implementation / no Hall readiness",
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
            "PB3 = LIN1",
            "DMM gate is hardware-side deferred",
            "This is not a pass",
            "No fixed debounce threshold is accepted",
            "Forbidden in ISR",
            "MCSDK Boundary",
            "not MCSDK standard",
        ):
            self.assertIn(phrase, text)

    def test_algorithm_prep_defines_state_machine_and_debug_contract(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_no_power_algorithm_prep_2026-05-22.md"
        )

        for phrase in (
            "`001`, `010`, `011`, `100`, `101`, and `110`",
            "Reject `000` and `111`",
            "Repeated state",
            "Cross-state jump",
            "Bounce candidate",
            "001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001",
            "001 -> 011 -> 010 -> 110 -> 100 -> 101 -> 001",
            "current_raw_state",
            "last_accepted_state",
            "edge_count",
            "illegal_state_count",
            "abnormal_jump_count",
            "last_edge_dt_ticks",
            "direction_candidate",
            "speed_candidate",
        ):
            self.assertIn(phrase, text)

    def test_readiness_and_active_task_record_algorithm_prep_as_design_only(self):
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")

        for phrase in (
            "Software Hall no-power algorithm prep",
            "Algorithm-side no-power preparation only",
            "TASK-2026-05-22-p2-software-hall-no-power-algorithm-prep",
            "EV-2026-05-22-P2-SOFTWARE-HALL-ALGORITHM-PREP-001",
            "Deferred does not mean passed",
            "not firmware implementation or hardware validation",
        ):
            self.assertIn(phrase, readiness + active + register)


class SoftwareHallStateMachineExerciseCardTests(unittest.TestCase):
    def test_exercise_card_exists_and_is_user_facing_chinese(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_state_machine_exercise_card_2026-05-22.md"
        )

        for phrase in (
            "软件 Hall 状态机练习卡",
            "本卡给算法/主控同学使用",
            "当前阶段：`P2 no-power`",
            "PB3 = LIN1，不参与 Hall",
            "你现在要回答的 5 个检查点",
            "你要回填的小表",
            "输入序列 | 你的判断 | 是否计边沿 | 是否异常 | 备注",
            "判分规则",
            "Codex 判读标准",
            "禁止结论",
        ):
            self.assertIn(phrase, text)

    def test_exercise_card_rows_and_boundaries_are_locked(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_state_machine_exercise_card_2026-05-22.md"
        )

        for phrase in (
            "`001 -> 101`",
            "合法相邻跳变",
            "`001 -> 001`",
            "重复状态",
            "`001 -> 010`",
            "计异常跳变",
            "`000`",
            "非法 Hall 状态",
            "不需要 DMM",
            "不要上电",
            "不要接电机",
            "不要测 PWM",
            "软件 Hall adapter 已实现",
        ):
            self.assertIn(phrase, text)

    def test_readiness_records_exercise_as_waiting_for_user_answer(self):
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")

        for phrase in (
            "Software Hall state-machine exercise",
            "Waiting for user answer",
            "TASK-2026-05-22-p2-software-hall-state-machine-exercise",
            "EV-2026-05-22-P2-SOFTWARE-HALL-STATE-MACHINE-EXERCISE-001",
            "learning check only",
            "does not open firmware implementation",
        ):
            self.assertIn(phrase, readiness + active + register)


class SoftwareHallAdapterPseudocodeDraftTests(unittest.TestCase):
    def test_pseudocode_draft_exists_and_is_not_firmware(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_adapter_pseudocode_draft_2026-05-27.md"
        )

        for phrase in (
            "软件 Hall Adapter 伪代码草案",
            "Pseudocode only. Not firmware source.",
            "not firmware implementation",
            "not MCSDK integration",
            "not hardware validation",
            "PB3 = LIN1，不参与 Hall",
            "DMM 连续性 / 短路表暂缓，不是通过",
            "Hall_CaptureEdge_ISR()",
            "Hall_ProcessEvent()",
            "No software Hall adapter implementation",
        ):
            self.assertIn(phrase, text)

    def test_pseudocode_draft_locks_algorithm_rules(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_adapter_pseudocode_draft_2026-05-27.md"
        )

        for phrase in (
            "001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001",
            "001 -> 011 -> 010 -> 110 -> 100 -> 101 -> 001",
            "Hall_IsValidState(raw)",
            "Hall_IsForwardAdjacent(prev, cur)",
            "Hall_IsReverseAdjacent(prev, cur)",
            "HALL_DECISION_ILLEGAL_STATE",
            "HALL_DECISION_REPEAT_STATE",
            "HALL_DECISION_ABNORMAL_JUMP",
            "direction_candidate",
            "speed_candidate",
            "MCSDK 接入硬停止",
        ):
            self.assertIn(phrase, text)

    def test_readiness_records_pseudocode_as_design_only(self):
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")

        for phrase in (
            "Software Hall adapter pseudocode draft",
            "Pseudocode draft added / no firmware implementation / no MCSDK Hall integration / no Hall readiness",
            "TASK-2026-05-27-p2-software-hall-adapter-pseudocode-draft",
            "EV-2026-05-27-P2-SOFTWARE-HALL-PSEUDOCODE-DRAFT-001",
            "DMM remains deferred, not passed",
            "not firmware implementation",
            "not usable to claim firmware implementation",
        ):
            self.assertIn(phrase, readiness + active + register)


class SoftwareHallFollowupReviewTests(unittest.TestCase):
    def test_followup_review_records_table_level_mastery_only(self):
        note = read_repo_text(
            "learning/session_notes/2026-05-27_hall_state_machine_review_followup.md"
        )
        completed = read_repo_text(
            "learning/review_items/2026-05-27_hall_state_machine_review_completed.md"
        )
        mastery = read_repo_text("learning/MASTERY_MAP.md")
        queue = read_repo_text("learning/review_queue.md")
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")

        for phrase in (
            "100 -> 110",
            "100 -> 101",
            "100 -> 011",
            "000",
            "111",
            "L4 for table-level no-power Hall state-machine classification",
            "Not L5",
            "no firmware implementation",
            "no MCSDK Hall integration",
            "no DMM proof",
            "no Gate PWM",
        ):
            self.assertIn(phrase, note)

        for phrase in (
            "Hall state-machine review completed",
            "Software Hall state-machine table classification",
            "before software Hall firmware",
            "TASK-2026-05-27-p2-software-hall-followup-review",
            "EV-2026-05-27-P2-SOFTWARE-HALL-FOLLOWUP-REVIEW-001",
            "L4 table-level no-power Hall state-machine classification / no firmware implementation / no hardware validation",
            "not usable to claim firmware implementation",
        ):
            self.assertIn(phrase, completed + mastery + queue + status + active + register)


class SoftwareHallProcessingOrderCardTests(unittest.TestCase):
    def test_processing_order_card_exists_and_keeps_no_power_boundary(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_adapter_processing_order_card_2026-05-27.md"
        )

        for phrase in (
            "Software Hall Adapter Processing-Order Card",
            "Software Hall adapter processing-order teaching card / no firmware implementation / no MCSDK Hall integration / no Hall readiness",
            "P2 no-power",
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
            "PB3 = LIN1",
            "raw read -> illegal-state check -> first-valid check -> repeated-state check",
            "bounce/timing check -> forward/reverse adjacent check -> abnormal-jump count",
            "000/111",
            "first-valid check",
            "This artifact is not usable to claim firmware implementation",
            "No 24V",
            "No Gate PWM output",
            "No Hall closed-loop claim",
        ):
            self.assertIn(phrase, text)

    def test_processing_order_card_is_recorded_as_repair_not_mastery(self):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        session = read_repo_text("learning/session_notes.md")
        weak = read_repo_text("learning/weak_points.md")
        mastery = read_repo_text("learning/MASTERY_MAP.md")
        queue = read_repo_text("learning/review_queue.md")
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        evidence = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "evidence_packet_2026-05-14.md"
        )
        checklist = read_repo_text("deliverables/submission_checklist.md")
        sprint = read_repo_text("workflow/current_learning_sprint.md")

        combined = (
            status
            + active
            + register
            + session
            + weak
            + mastery
            + queue
            + readiness
            + evidence
            + checklist
            + sprint
        )

        for phrase in (
            "software_hall_adapter_processing_order_card_2026-05-27.md",
            "TASK-2026-05-27-p2-software-hall-processing-order-card",
            "EV-2026-05-27-P2-SOFTWARE-HALL-PROCESSING-ORDER-CARD-001",
            "WP-030",
            "L1 repair artifact",
            "not a new mastery upgrade",
            "no firmware implementation",
            "no MCSDK Hall integration",
            "not usable to claim firmware implementation",
            "one-sentence teach-back",
        ):
            self.assertIn(phrase, combined)


class SoftwareHallHostModelWorkflowTests(unittest.TestCase):
    def test_host_model_review_records_executable_algorithm_only(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_host_model_review_2026-05-27.md"
        )

        for phrase in (
            "Software Hall Host Model Review",
            "Host-side software Hall reference model / no firmware implementation / no MCSDK Hall integration / no Hall readiness",
            "src/software_hall_model.py",
            "tests/test_software_hall_model.py",
            "PA0/PA1/PB4",
            "PB3=LIN1",
            "raw state input",
            "illegal-state check",
            "first-valid check",
            "repeated-state check",
            "configurable bounce/timing check",
            "forward/reverse adjacent check",
            "abnormal-jump count",
            "not STM32 firmware",
            "not GPIO/EXTI runtime behavior",
            "No 24V",
            "No Gate PWM output",
            "No Hall closed-loop claim",
        ):
            self.assertIn(phrase, review)

    def test_host_model_is_registered_without_firmware_or_hardware_claim(self):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        evidence = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "evidence_packet_2026-05-14.md"
        )
        checklist = read_repo_text("deliverables/submission_checklist.md")
        sprint = read_repo_text("workflow/current_learning_sprint.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = (
            status
            + active
            + register
            + readiness
            + evidence
            + checklist
            + sprint
            + readme
        )

        for phrase in (
            "Software Hall Host Model Added",
            "TASK-2026-05-27-p2-software-hall-host-model",
            "EV-2026-05-27-P2-SOFTWARE-HALL-HOST-MODEL-001",
            "src/software_hall_model.py",
            "tests/test_software_hall_model.py",
            "software_hall_host_model_review_2026-05-27.md",
            "Host-side software Hall reference model / no firmware implementation / no MCSDK Hall integration / no Hall readiness",
            "host-side algorithm evidence only",
            "not firmware or hardware readiness",
            "not usable to claim firmware implementation",
        ):
            self.assertIn(phrase, combined)


class SoftwareHallGoldenVectorsWorkflowTests(unittest.TestCase):
    def test_golden_vector_review_records_replay_contract_only(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_golden_vectors_review_2026-05-27.md"
        )

        for phrase in (
            "Software Hall Golden Vectors Review",
            "Host-side software Hall golden vectors / no firmware implementation / no MCSDK Hall integration / no Hall readiness",
            "tests/fixtures/software_hall_golden_vectors.json",
            "tests/test_software_hall_vectors.py",
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
            "PB3=LIN1",
            "001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001",
            "illegal state rejection",
            "repeated-state rejection",
            "configurable bounce-candidate rejection",
            "abnormal non-adjacent legal jump",
            "not firmware implementation",
            "not GPIO/EXTI runtime behavior",
            "No 24V",
            "No Gate PWM output",
            "No Hall closed-loop claim",
        ):
            self.assertIn(phrase, review)

    def test_golden_vectors_are_registered_without_firmware_or_hardware_claim(self):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        evidence = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "evidence_packet_2026-05-14.md"
        )
        checklist = read_repo_text("deliverables/submission_checklist.md")
        sprint = read_repo_text("workflow/current_learning_sprint.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = (
            status
            + active
            + register
            + readiness
            + evidence
            + checklist
            + sprint
            + readme
        )

        for phrase in (
            "Software Hall Golden Vectors Added",
            "TASK-2026-05-27-p2-software-hall-golden-vectors",
            "EV-2026-05-27-P2-SOFTWARE-HALL-GOLDEN-VECTORS-001",
            "tests/fixtures/software_hall_golden_vectors.json",
            "tests/test_software_hall_vectors.py",
            "software_hall_golden_vectors_review_2026-05-27.md",
            "Host-side software Hall golden vectors / no firmware implementation / no MCSDK Hall integration / no Hall readiness",
            "host-side no-power",
            "not firmware or hardware readiness",
            "Not usable to claim firmware implementation",
        ):
            self.assertIn(phrase, combined)


class FocCoreHostModelWorkflowTests(unittest.TestCase):
    def test_foc_core_model_review_records_host_side_algorithm_only(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "host_side_no_power_foc_algorithm_model_review_2026-06-22.md"
        )

        for phrase in (
            "Host-Side No-Power FOC Algorithm Model Review",
            "Host-side no-power FOC algorithm model / no firmware implementation / no MCSDK integration / no PWM output / no motor readiness",
            "src/foc_core_model.py",
            "tests/test_foc_core_model.py",
            "MCSDK remains the intended motor-control framework generation path",
            "clarke_abc",
            "inverse_clarke",
            "park",
            "inverse_park",
            "svpwm",
            "pi_step",
            "current_control_step",
            "phase current samples",
            "d/q PI current control",
            "host-side SVPWM duty calculation",
            "externally supplied prior-integrator clamp",
            "q-axis current request phase-duty direction",
            "not a timer driver",
            "not firmware implementation",
            "No 24V",
            "No Gate PWM output",
            "No Hall closed-loop claim",
        ):
            self.assertIn(phrase, review)

    def test_foc_core_model_is_registered_without_hardware_readiness_claim(self):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        snapshot = read_repo_text("workflow/CURRENT_SNAPSHOT.md")
        context = read_repo_text("AI_CONTEXT.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = status + active + register + snapshot + context + readme

        for phrase in (
            "Host-Side No-Power FOC Algorithm Model Added",
            "TASK-2026-06-22-p2-host-side-no-power-foc-algorithm-model",
            "EV-2026-06-22-P2-HOST-SIDE-NO-POWER-FOC-ALGORITHM-MODEL-001",
            "src/foc_core_model.py",
            "tests/test_foc_core_model.py",
            "host_side_no_power_foc_algorithm_model_review_2026-06-22.md",
            "Host-side no-power FOC algorithm model / no firmware implementation / no MCSDK integration / no PWM output / no motor readiness",
            "host-side no-power algorithm evidence only",
            "MCSDK remains the intended motor-control framework generation path",
            "not Gate PWM validation",
            "not power-stage readiness",
            "not motor readiness",
        ):
            self.assertIn(phrase, combined)

    def test_foc_golden_vectors_review_records_host_side_fixture_only(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "host_side_no_power_foc_golden_vectors_review_2026-06-22.md"
        )

        for phrase in (
            "Host-Side No-Power FOC Golden Vectors Review",
            "Host-side no-power FOC golden vectors / no firmware implementation / no MCSDK integration / no PWM output / no motor readiness",
            "tests/fixtures/foc_core_golden_vectors.json",
            "tests/test_foc_core_vectors.py",
            "host-side no-power regression fixtures",
            "They do not configure TIM1",
            "write compare registers",
            "drive gates",
            "validate PWM safety",
            "not proof that MCSDK generated code",
            "Clarke / Park / PI / inverse Park / zero-sequence duty math",
            "large-vector saturation with `scale`",
            "externally supplied prior-integrator clamp",
            "No 24V",
            "No Gate PWM output",
            "No Hall closed-loop claim",
        ):
            self.assertIn(phrase, review)

    def test_foc_golden_vectors_are_registered_without_hardware_claim(self):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        snapshot = read_repo_text("workflow/CURRENT_SNAPSHOT.md")
        context = read_repo_text("AI_CONTEXT.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = status + active + register + snapshot + context + readme

        for phrase in (
            "Host-Side No-Power FOC Golden Vectors Added",
            "TASK-2026-06-22-p2-host-side-no-power-foc-golden-vectors",
            "EV-2026-06-22-P2-HOST-SIDE-NO-POWER-FOC-GOLDEN-VECTORS-001",
            "tests/fixtures/foc_core_golden_vectors.json",
            "tests/test_foc_core_vectors.py",
            "host_side_no_power_foc_golden_vectors_review_2026-06-22.md",
            "Host-side no-power FOC golden vectors / no firmware implementation / no MCSDK integration / no PWM output / no motor readiness",
            "host-side no-power regression fixture evidence only",
            "not MCSDK convention proof",
            "not compare-register evidence",
            "not Gate PWM validation",
            "not power-stage readiness",
            "not motor readiness",
        ):
            self.assertIn(phrase, combined)

    def test_mcsdk_host_side_foc_boundary_plan_records_plan_only(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "mcsdk_host_side_foc_math_comparison_boundary_plan_2026-06-22.md"
        )

        for phrase in (
            "MCSDK / Host-Side FOC Math Comparison Boundary Plan",
            "MCSDK host-side FOC math comparison boundary plan / no firmware implementation / no MCSDK integration / no PWM output / no motor readiness",
            "src/foc_core_model.py",
            "tests/fixtures/foc_core_golden_vectors.json",
            "tests/test_foc_core_vectors.py",
            "MCSDK remains the intended motor-control framework generation path",
            "compare only sign, scaling, saturation, duty representation, and naming assumptions",
            "not proof that MCSDK generated code matches the Python model",
            "not firmware implementation",
            "MCSDK integration",
            "not compare-register evidence",
            "not Gate PWM validation",
            "No 24V",
            "No Gate PWM output",
            "No Hall closed-loop claim",
        ):
            self.assertIn(phrase, review)

    def test_mcsdk_host_side_foc_boundary_plan_is_registered(self):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        snapshot = read_repo_text("workflow/CURRENT_SNAPSHOT.md")
        context = read_repo_text("AI_CONTEXT.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = status + active + register + snapshot + context + readme

        for phrase in (
            "TASK-2026-06-22-p2-mcsdk-host-side-foc-math-comparison-boundary-plan",
            "EV-2026-06-22-P2-MCSDK-HOST-SIDE-FOC-MATH-COMPARISON-BOUNDARY-PLAN-001",
            "mcsdk_host_side_foc_math_comparison_boundary_plan_2026-06-22.md",
            "tests/test_mcsdk_foc_pipeline_static.py",
            "MCSDK host-side FOC math comparison boundary plan / no firmware implementation / no MCSDK integration / no PWM output / no motor readiness",
            "host-side no-power comparison plan only",
            "not MCSDK convention proof",
            "not compare-register evidence",
            "not Gate PWM validation",
            "not power-stage readiness",
            "not motor readiness",
        ):
            self.assertIn(phrase, combined)


class SoftwareHallMcsdkIntegrationProbeWorkflowTests(unittest.TestCase):
    def test_integration_probe_records_read_only_clues_only(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_mcsdk_integration_probe_2026-05-27.md"
        )

        for phrase in (
            "Software Hall MCSDK Integration Probe",
            "MCSDK Hall integration points identified as read-only clues / no firmware implementation / no MCSDK Hall integration / no Hall readiness",
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
            "PB3 = LIN1",
            "TIM_HallSensor_InitTypeDef",
            "HAL_TIMEx_HallSensor_Init",
            "HALL_Handle_t HALL_M1",
            "SpeednTorqCtrlM1",
            "PIDSpeedHandle_M1",
            "M1_SPEED_SENSOR=HALL_SENSOR",
            "SPEED_SENSOR_SELECTION=HALL_SENSORS",
            "M1_HALL_TIMER_SELECTION=HALL_TIM2",
            "hall_speed_pos_fdbk.c/.h",
            "speed_torq_ctrl.c/.h",
            "not software GPIO/EXTI Hall",
            "requires a separate firmware-integration review",
            "No 24V",
            "No Gate PWM output",
            "No Hall closed-loop claim",
        ):
            self.assertIn(phrase, review)

    def test_integration_probe_is_registered_without_hall_readiness_claim(self):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        evidence = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "evidence_packet_2026-05-14.md"
        )
        checklist = read_repo_text("deliverables/submission_checklist.md")
        sprint = read_repo_text("workflow/current_learning_sprint.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = (
            status
            + active
            + register
            + readiness
            + evidence
            + checklist
            + sprint
            + readme
        )

        for phrase in (
            "Software Hall MCSDK Integration Probe Added",
            "TASK-2026-05-27-p2-software-hall-mcsdk-integration-probe",
            "EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-INTEGRATION-PROBE-001",
            "software_hall_mcsdk_integration_probe_2026-05-27.md",
            "MCSDK Hall integration points identified as read-only clues / no firmware implementation / no MCSDK Hall integration / no Hall readiness",
            "standard MCSDK Hall path",
            "current `PA0/PA1/PB4` software Hall route is not directly connected",
            "separate firmware-integration review",
            "not MCSDK Hall integration",
            "Not usable to claim firmware implementation",
        ):
            self.assertIn(phrase, combined)


class SoftwareHallFirmwareEntryChecklistWorkflowTests(unittest.TestCase):
    def test_firmware_entry_checklist_records_entry_gate_only(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_firmware_entry_checklist_2026-05-27.md"
        )

        for phrase in (
            "软件 Hall 固件入口审查清单",
            "Software Hall firmware-entry checklist / no firmware implementation / no MCSDK Hall integration / no Hall readiness",
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
            "PB3 = LIN1，不参与 Hall",
            "PCB2 仍未焊接完成",
            "DMM 连续性 / 短路表暂缓。暂缓不是通过。",
            "FIRM-ENTRY-01",
            "FIRM-ENTRY-10",
            "GPIO/EXTI",
            "时间戳来源",
            "low-frequency debug",
            "separate MCSDK firmware-integration review",
            "不改 TIM1 PWM",
            "不改 JEOC / FOC ISR",
            "不替换 HALL_M1",
            "不写 MCSDK speed feedback",
            "No software Hall adapter implementation",
            "Hall 闭环可运行",
        ):
            self.assertIn(phrase, review)

    def test_firmware_entry_checklist_is_registered_without_implementation_claim(self):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        evidence = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "evidence_packet_2026-05-14.md"
        )
        checklist = read_repo_text("deliverables/submission_checklist.md")
        sprint = read_repo_text("workflow/current_learning_sprint.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = (
            status
            + active
            + register
            + readiness
            + evidence
            + checklist
            + sprint
            + readme
        )

        for phrase in (
            "Software Hall Firmware-Entry Checklist Added",
            "TASK-2026-05-27-p2-software-hall-firmware-entry-checklist",
            "EV-2026-05-27-P2-SOFTWARE-HALL-FIRMWARE-ENTRY-CHECKLIST-001",
            "software_hall_firmware_entry_checklist_2026-05-27.md",
            "Software Hall firmware-entry checklist / no firmware implementation / no MCSDK Hall integration / no Hall readiness",
            "populated-board DMM",
            "GPIO/EXTI boundary review",
            "timestamp-source decision",
            "no-power build-only record",
            "separate MCSDK",
            "not usable to claim firmware implementation",
        ):
            self.assertIn(phrase, combined)


class SoftwareHallGpioExtiBoundaryWorkflowTests(unittest.TestCase):
    def test_gpio_exti_boundary_review_records_static_boundary_only(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_gpio_exti_boundary_review_2026-05-27.md"
        )

        for phrase in (
            "软件 Hall GPIO/EXTI 边界审查草案",
            "Software Hall GPIO/EXTI boundary review draft / no firmware implementation / no GPIO runtime proof / no Hall readiness",
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
            "PB3 = LIN1，不参与 Hall",
            "PA0",
            "GPIO_EXTI0",
            "PA1",
            "GPIO_EXTI1",
            "PB4",
            "GPIO_EXTI4",
            "EXTI0_IRQn",
            "EXTI1_IRQn",
            "EXTI4_IRQn",
            "GPIO_MODE_IT_RISING_FALLING",
            "GPIO_NOPULL",
            "GPIO_PULLUP",
            "GPIO_PULLDOWN",
            "SoftHallExtiEvent",
            "Pseudocode only. Not firmware source.",
            "不替换 `HALL_M1`",
            "不可声明 GPIO/EXTI runtime proof 已完成",
        ):
            self.assertIn(phrase, review)

    def test_gpio_exti_boundary_review_is_registered_without_runtime_claim(self):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        evidence = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "evidence_packet_2026-05-14.md"
        )
        checklist = read_repo_text("deliverables/submission_checklist.md")
        sprint = read_repo_text("workflow/current_learning_sprint.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = (
            status
            + active
            + register
            + readiness
            + evidence
            + checklist
            + sprint
            + readme
        )

        for phrase in (
            "Software Hall GPIO/EXTI Boundary Review Draft Added",
            "TASK-2026-05-27-p2-software-hall-gpio-exti-boundary-review",
            "EV-2026-05-27-P2-SOFTWARE-HALL-GPIO-EXTI-BOUNDARY-001",
            "software_hall_gpio_exti_boundary_review_2026-05-27.md",
            "Software Hall GPIO/EXTI boundary review draft / no firmware implementation / no GPIO runtime proof / no Hall readiness",
            "EXTI0/EXTI1/EXTI4",
            "minimal ISR",
            "not GPIO runtime proof",
            "not usable to claim firmware implementation",
        ):
            self.assertIn(phrase, combined)


class SoftwareHallTimestampSourceWorkflowTests(unittest.TestCase):
    def test_timestamp_source_review_records_timer_boundaries_only(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_timestamp_source_review_2026-05-27.md"
        )

        for phrase in (
            "软件 Hall Timestamp Source 审查草案",
            "Software Hall timestamp-source review draft / no firmware implementation / no timer configuration / no Hall readiness",
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
            "PB3 = LIN1，不参与 Hall",
            "TIM1",
            "MX_TIM1_Init()",
            "TIM1_UP_TIM16_IRQn",
            "ADC_EXTERNALTRIGINJEC_T1_TRGO",
            "TIM2",
            "HAL_TIMEx_HallSensor_Init",
            "M1_HALL_TIMER_SELECTION=HALL_TIM2",
            "HAL_GetTick()",
            "uwTickFreq",
            "1KHz",
            "dedicated free-running timer",
            "unsigned delta",
            "Pseudocode only. Not firmware source.",
            "不可声明 timer configuration 已完成",
            "No 24V",
        ):
            self.assertIn(phrase, review)

    def test_timestamp_source_review_is_registered_without_timer_config_claim(self):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        evidence = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "evidence_packet_2026-05-14.md"
        )
        checklist = read_repo_text("deliverables/submission_checklist.md")
        sprint = read_repo_text("workflow/current_learning_sprint.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = (
            status
            + active
            + register
            + readiness
            + evidence
            + checklist
            + sprint
            + readme
        )

        for phrase in (
            "Software Hall Timestamp Source Review Draft Added",
            "TASK-2026-05-27-p2-software-hall-timestamp-source-review",
            "EV-2026-05-27-P2-SOFTWARE-HALL-TIMESTAMP-SOURCE-001",
            "software_hall_timestamp_source_review_2026-05-27.md",
            "Software Hall timestamp-source review draft / no firmware implementation / no timer configuration / no Hall readiness",
            "TIM1",
            "current `TIM2`",
            "HAL_GetTick()",
            "dedicated free-running timer",
            "unsigned delta",
            "not timer configuration",
            "not usable to claim firmware implementation",
        ):
            self.assertIn(phrase, combined)


class SoftwareHallDebugOutputRouteWorkflowTests(unittest.TestCase):
    def test_debug_output_route_review_records_snapshot_boundary_only(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_debug_output_route_review_2026-05-27.md"
        )

        for phrase in (
            "软件 Hall Low-Frequency Debug-Output Route 审查草案",
            "Software Hall low-frequency debug-output route review draft / no firmware implementation / no UART implementation / no Hall readiness",
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
            "PB3 = LIN1，不参与 Hall",
            "current_raw_state",
            "last_accepted_state",
            "edge_count",
            "illegal_state_count",
            "abnormal_jump_count",
            "last_edge_dt_ticks",
            "direction_candidate",
            "speed_candidate",
            "low-frequency",
            "not every EXTI edge",
            "UART text / CSV / JSON",
            "ESP32 / WebSocket display",
            "SWO / ITM",
            "Pseudocode only. Not firmware source.",
            "不可声明 debug-output firmware 已实现",
            "No 24V",
        ):
            self.assertIn(phrase, review)

    def test_debug_output_route_review_is_registered_without_uart_claim(self):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        evidence = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "evidence_packet_2026-05-14.md"
        )
        checklist = read_repo_text("deliverables/submission_checklist.md")
        sprint = read_repo_text("workflow/current_learning_sprint.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = (
            status
            + active
            + register
            + readiness
            + evidence
            + checklist
            + sprint
            + readme
        )

        for phrase in (
            "Software Hall Debug-Output Route Review Draft Added",
            "TASK-2026-05-27-p2-software-hall-debug-output-route-review",
            "EV-2026-05-27-P2-SOFTWARE-HALL-DEBUG-OUTPUT-ROUTE-001",
            "software_hall_debug_output_route_review_2026-05-27.md",
            "Software Hall low-frequency debug-output route review draft / no firmware implementation / no UART implementation / no Hall readiness",
            "low-frequency debug snapshot",
            "UART transmit",
            "ESP32 / WebSocket",
            "every-edge streaming",
            "not UART implementation",
            "not usable to claim firmware implementation",
        ):
            self.assertIn(phrase, combined)


class SoftwareHallMcsdkFirmwareIntegrationBoundaryWorkflowTests(unittest.TestCase):
    def test_mcsdk_firmware_integration_boundary_records_hook_hard_stops(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md"
        )

        for phrase in (
            "软件 Hall MCSDK Firmware-Integration 边界审查草案",
            "Software Hall MCSDK firmware-integration boundary review draft / no firmware implementation / no MCSDK hook / no Hall readiness",
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
            "PB3 = LIN1",
            "direction_candidate",
            "speed_candidate",
            "HALL_M1",
            "SpeednTorqCtrlM1",
            "PIDSpeedHandle_M1",
            "pSTC",
            "MCI_Handle_t",
            "FOCVars",
            "SPD_HALL_TIM_M1_IRQHandler",
            "M1_SPEED_SENSOR=HALL_SENSOR",
            "M1_HALL_TIMER_SELECTION=HALL_TIM2",
            "hall_speed_pos_fdbk.c/.h",
            "speed_torq_ctrl.c/.h",
            "mc_app_hooks.c/.h",
            "Hard stop",
            "Do not edit generated MCSDK files",
            "No firmware implementation is claimed",
            "No MCSDK hook is claimed",
            "No 24V",
        ):
            self.assertIn(phrase, review)

    def test_mcsdk_firmware_integration_boundary_is_registered_without_hook_claim(
        self,
    ):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        snapshot = read_repo_text("workflow/CURRENT_SNAPSHOT.md")
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        evidence = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "evidence_packet_2026-05-14.md"
        )
        checklist = read_repo_text("deliverables/submission_checklist.md")
        sprint = read_repo_text("workflow/current_learning_sprint.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = (
            status
            + active
            + register
            + snapshot
            + readiness
            + evidence
            + checklist
            + sprint
            + readme
        )

        for phrase in (
            "Software Hall MCSDK Firmware-Integration Boundary Review Draft Added",
            "TASK-2026-05-27-p2-software-hall-mcsdk-firmware-integration-boundary",
            "EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-FIRMWARE-INTEGRATION-BOUNDARY-001",
            "software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md",
            "Software Hall MCSDK firmware-integration boundary review draft / no firmware implementation / no MCSDK hook / no Hall readiness",
            "direction_candidate",
            "speed_candidate",
            "HALL_M1",
            "SpeednTorqCtrlM1",
            "not MCSDK hooks",
            "not MCSDK hook evidence",
            "not usable to claim firmware implementation",
        ):
            self.assertIn(phrase, combined)


class SoftwareHallMcsdkHookEvidenceRequestChecklistWorkflowTests(unittest.TestCase):
    def test_mcsdk_hook_evidence_request_checklist_records_required_sources(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md"
        )

        for phrase in (
            "Software Hall MCSDK hook evidence request checklist / no firmware implementation / no MCSDK hook / no Hall readiness",
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
            "PB3 = LIN1",
            "hall_speed_pos_fdbk.c/.h",
            "speed_torq_ctrl.c/.h",
            "mc_tasks.c",
            "mc_tasks_foc.c",
            "mc_interface.c/.h",
            "mc_api.c/.h",
            "mc_app_hooks.c/.h",
            "mc_parameters.c/.h",
            "motorcontrol.c/.h",
            "mc_type.h",
            "interrupt source files",
            "pwm_curr_fdbk.c/.h",
            "register_interface.h",
            "usart_aspep_driver.c",
            "aspep.c/.h",
            "Rejected Evidence Types",
            "log-only generated file names",
            "AI summaries of MCSDK internals",
            "This checklist does not allow",
            "Hall closed-loop claim",
            "Gate PWM output",
        ):
            self.assertIn(phrase, review)

    def test_mcsdk_hook_evidence_request_checklist_is_registered_without_hook_claim(
        self,
    ):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        snapshot = read_repo_text("workflow/CURRENT_SNAPSHOT.md")
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        evidence = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "evidence_packet_2026-05-14.md"
        )
        checklist = read_repo_text("deliverables/submission_checklist.md")
        sprint = read_repo_text("workflow/current_learning_sprint.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = (
            status
            + active
            + register
            + snapshot
            + readiness
            + evidence
            + checklist
            + sprint
            + readme
        )

        for phrase in (
            "Software Hall MCSDK Hook Evidence Request Checklist Added",
            "TASK-2026-05-27-p2-software-hall-mcsdk-hook-evidence-request-checklist",
            "EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-HOOK-EVIDENCE-REQUEST-001",
            "software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md",
            "Software Hall MCSDK hook evidence request checklist / no firmware implementation / no MCSDK hook / no Hall readiness",
            "source-evidence request",
            "hall_speed_pos_fdbk.c/.h",
            "speed_torq_ctrl.c/.h",
            "mc_app_hooks.c/.h",
            "not MCSDK hook evidence",
            "not usable to claim firmware implementation",
        ):
            self.assertIn(phrase, combined)


class FullWorkbenchSrcIncSnapshotWorkflowTests(unittest.TestCase):
    def test_full_workbench_src_inc_snapshot_archives_required_files(self):
        snapshot_dir = (
            ROOT
            / "apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/"
            "2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot"
        )

        self.assertTrue(snapshot_dir.exists())

        for relative_path in (
            "SOURCE_MANIFEST_2026-05-27.md",
            "SHA256SUMS.txt",
            "Src/hall_speed_pos_fdbk.c",
            "Inc/hall_speed_pos_fdbk.h",
            "Src/speed_torq_ctrl.c",
            "Inc/speed_torq_ctrl.h",
            "Src/mc_tasks.c",
            "Inc/mc_tasks.h",
            "Src/mc_tasks_foc.c",
            "Src/mc_interface.c",
            "Inc/mc_interface.h",
            "Src/mc_api.c",
            "Inc/mc_api.h",
            "Src/mc_app_hooks.c",
            "Inc/mc_app_hooks.h",
            "Src/mc_parameters.c",
            "Inc/mc_parameters.h",
            "Src/motorcontrol.c",
            "Inc/motorcontrol.h",
            "Inc/mc_type.h",
            "Src/stm32g4xx_it.c",
            "Inc/stm32g4xx_it.h",
            "Src/stm32g4xx_mc_it.c",
            "Src/pwm_curr_fdbk.c",
            "Inc/pwm_curr_fdbk.h",
            "Inc/register_interface.h",
            "Src/usart_aspep_driver.c",
            "Src/aspep.c",
            "Inc/aspep.h",
            "CMakeLists.txt",
            "CMakePresets.json",
            "QIANSAI_G474_STDRIVE101_FOC_P2.ioc",
            "QIANSAI_G474_STDRIVE101_FOC_P2.log",
        ):
            with self.subTest(relative_path=relative_path):
                self.assertTrue((snapshot_dir / relative_path).exists())

    def test_full_workbench_src_inc_snapshot_review_records_no_power_limits(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "source_packet_review_2026-05-27_001_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot.md"
        )
        manifest = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/"
            "2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/"
            "SOURCE_MANIFEST_2026-05-27.md"
        )
        hashes = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/"
            "2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/"
            "SHA256SUMS.txt"
        )

        for phrase in (
            "Full generated Src/Inc snapshot archived / source interface evidence available for read-only review / no firmware implementation / no MCSDK hook / no Hall readiness",
            "C:\\Users\\gregrg\\.st_workbench\\projects\\QIANSAI_G474_STDRIVE101_FOC_P2",
            "Src/`: 30 files",
            "Inc/`: 28 files",
            "cmake/`: 3 files",
            "SHA256SUMS.txt`: 72 hash entries",
            "hall_speed_pos_fdbk.c/.h",
            "speed_torq_ctrl.c/.h",
            "mc_tasks.c",
            "mc_tasks_foc.c",
            "mc_interface.c/.h",
            "mc_app_hooks.c/.h",
            "Inc/usart_aspep_driver.h` is not present",
            "generated MCSDK Hall remains TIM2",
            "PA15/PB3/PB10",
            "PA0/PA1/PB4",
            "PB3=LIN1",
            "No Gate PWM output",
        ):
            self.assertIn(phrase, review + manifest)

        self.assertIn("Src\\hall_speed_pos_fdbk.c", hashes)
        self.assertIn("Inc\\hall_speed_pos_fdbk.h", hashes)
        self.assertIn("Src\\mc_tasks_foc.c", hashes)

    def test_full_workbench_src_inc_snapshot_is_registered_without_hook_claim(self):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        snapshot = read_repo_text("workflow/CURRENT_SNAPSHOT.md")
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        evidence = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "evidence_packet_2026-05-14.md"
        )
        checklist = read_repo_text("deliverables/submission_checklist.md")
        sprint = read_repo_text("workflow/current_learning_sprint.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = (
            status
            + active
            + register
            + snapshot
            + readiness
            + evidence
            + checklist
            + sprint
            + readme
        )

        for phrase in (
            "Full Workbench Src/Inc Snapshot Archived",
            "TASK-2026-05-27-p2-full-workbench-src-inc-snapshot-review",
            "EV-2026-05-27-P2-FULL-WORKBENCH-SRC-INC-SNAPSHOT-001",
            "source_packet_review_2026-05-27_001_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot.md",
            "2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot",
            "Full generated Src/Inc snapshot archived / source interface evidence available for read-only review / no firmware implementation / no MCSDK hook / no Hall readiness",
            "read-only interface review",
            "not firmware implementation",
            "not MCSDK hook evidence",
            "not Hall readiness",
        ):
            self.assertIn(phrase, combined)


class SoftwareHallMcsdkSpeedPositionInterfaceWorkflowTests(unittest.TestCase):
    def test_speed_position_interface_review_records_mcsdk_feedback_chain(self):
        review = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md"
        )

        for phrase in (
            "Software Hall MCSDK speed/position feedback interface review / no firmware implementation / no MCSDK hook / no Hall readiness",
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
            "PB3 = LIN1",
            "PA15/PB3/PB10",
            "TIM2",
            "HALL_M1",
            "SpeednPosFdbk_Handle_t",
            "SPD_HALL_TIM_M1_IRQHandler",
            "HALL_TIMx_CC_IRQHandler",
            "HALL_CalcAvrgMecSpeedUnit",
            "STC_GetSpeedSensor",
            "SPD_GetAvrgMecSpeedUnit",
            "SPD_GetElAngle",
            "hElAngle",
            "hElSpeedDpp",
            "hAvrMecSpeedUnit",
            "SensorIsReliable",
            "speed_pos_fdbk.h",
            "debug-only",
            "`SpeednPosFdbk`-compatible component",
            "No firmware implementation is claimed",
            "No MCSDK hook is claimed",
            "No Gate PWM output",
        ):
            self.assertIn(phrase, review)

    def test_speed_position_interface_review_is_registered_without_hook_claim(
        self,
    ):
        status = read_repo_text("CURRENT_STATUS.md")
        active = read_repo_text("workflow/ACTIVE_TASK.md")
        register = read_repo_text("workflow/evidence_register.md")
        snapshot = read_repo_text("workflow/CURRENT_SNAPSHOT.md")
        ai_context = read_repo_text("AI_CONTEXT.md")
        readiness = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "p2_readiness_snapshot_2026-05-15.md"
        )
        evidence = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "evidence_packet_2026-05-14.md"
        )
        checklist = read_repo_text("deliverables/submission_checklist.md")
        sprint = read_repo_text("workflow/current_learning_sprint.md")
        readme = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
        )

        combined = (
            status
            + active
            + register
            + snapshot
            + ai_context
            + readiness
            + evidence
            + checklist
            + sprint
            + readme
        )

        for phrase in (
            "Software Hall MCSDK Speed/Position Feedback Interface Review Added",
            "TASK-2026-05-27-p2-software-hall-mcsdk-speed-position-feedback-interface-review",
            "EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-SPEED-POSITION-INTERFACE-001",
            "software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md",
            "Software Hall MCSDK speed/position feedback interface review / no firmware implementation / no MCSDK hook / no Hall readiness",
            "HALL_M1",
            "HALL_CalcAvrgMecSpeedUnit",
            "STC_GetSpeedSensor",
            "SPD_GetAvrgMecSpeedUnit",
            "SPD_GetElAngle",
            "speed_pos_fdbk.h",
            "debug-only",
            "`SpeednPosFdbk`-compatible component",
            "not MCSDK hook evidence",
            "not Hall readiness",
        ):
            self.assertIn(phrase, combined)


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


class SoftwareHallFirmwareEntryPlanTests(unittest.TestCase):
    def test_firmware_entry_plan_records_debug_only_boundary(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "software_hall_firmware_entry_plan_2026-05-28.md"
        )

        for phrase in (
            "Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness",
            "HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4",
            "PB3 = LIN1",
            "PA15/PB3/PB10",
            "debug-only",
            "raw_state + timestamp + event counter",
            "000/111",
            "direction_candidate",
            "speed_candidate",
            "ISR 内禁止",
            "修改 `hall_speed_pos_fdbk.c/.h`",
            "写入或替换 `HALL_M1`",
            "修改 TIM1 PWM",
            "No flash",
            "No Gate PWM output",
            "no Hall closed-loop claim",
            "software Hall adapter 已实现",
            "MCSDK hook 已完成",
        ):
            self.assertIn(phrase, text)

    def test_firmware_entry_plan_is_registered_without_readiness_upgrade(self):
        combined = (
            read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text("workflow/current_learning_sprint.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
                "p2_readiness_snapshot_2026-05-15.md"
            )
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
                "evidence_packet_2026-05-14.md"
            )
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
            + read_repo_text("deliverables/submission_checklist.md")
        )

        for phrase in (
            "Software Hall Firmware-Entry Plan Added",
            "TASK-2026-05-28-p2-software-hall-firmware-entry-plan",
            "EV-2026-05-28-P2-SOFTWARE-HALL-FIRMWARE-ENTRY-PLAN-001",
            "software_hall_firmware_entry_plan_2026-05-28.md",
            "Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness",
            "PA0/PA1/PB4",
            "PB3=LIN1",
            "debug-only",
            "not current PCB2 Hall proof",
            "Not usable to claim software Hall adapter implementation",
            "DMM continuity / short-check evidence is hardware-side deferred, not passed",
            "no firmware implementation",
            "no MCSDK hook",
            "no Hall readiness",
            "No Gate PWM output",
        ):
            self.assertIn(phrase, combined)


class Stdrive101ManualGateTestLinkedImageBoundaryTests(unittest.TestCase):
    def test_linked_image_boundary_plan_records_no_power_boundary(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_manual_gate_test_linked_image_build_boundary_plan_2026-06-20.md"
        )

        for phrase in (
            "STDRIVE101 manual gate-test linked-image build-boundary plan no-power",
            "EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LINKED-IMAGE-BUILD-BOUNDARY-PLAN-001",
            "TASK-2026-06-20-stdrive101-manual-gate-test-linked-image-build-boundary-plan-no-power",
            "No ELF, MAP, HEX, BIN, or other linked lockout image is produced or claimed",
            "stdrive101_gate_lockout_image",
            "ELF and MAP",
            "startup_stm32g474xx.s",
            "STM32G474XX_FLASH.ld",
            "system_stm32g4xx.c",
            "syscalls.c",
            "sysmem.c",
            "MC_StartMotor1",
            "MCI_START",
            "R3_2_TurnOnLowSides",
            "PWMC_SwitchOnPWM",
            "LL_TIM_EnableAllOutputs",
            "no linked image built",
            "flash",
            "Run / Debug",
            "USB runtime execution",
            "24 V",
            "Gate PWM output",
            "Motor Pilot",
            "Motor Profiler",
            "motor connection",
        ):
            self.assertIn(phrase, text)

    def test_linked_image_boundary_plan_is_registered_without_runtime_upgrade(self):
        combined = (
            read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "stdrive101_manual_gate_test_linked_image_build_boundary_plan_2026-06-20.md",
            "EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LINKED-IMAGE-BUILD-BOUNDARY-PLAN-001",
            "TASK-2026-06-20-stdrive101-manual-gate-test-linked-image-build-boundary-plan-no-power",
            "STDRIVE101 manual gate-test linked-image build-boundary plan no-power",
            "boundary plan only",
            "no linked image built",
            "future target",
            "stdrive101_gate_lockout_image",
            "ELF plus MAP",
            "no flash",
            "no runtime",
            "no PWM-output validation",
            "no powered-drive readiness",
            "separate linked-image build-only record",
        ):
            self.assertIn(phrase, combined)

    def test_linked_image_build_only_record_records_artifacts_and_boundary(self):
        record = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_manual_gate_test_linked_image_build_only_record_2026-06-20.md"
        )
        cmake = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "manual_gate_test_lockout_build_only_2026-06-20/CMakeLists.txt"
        )
        text = record + cmake

        for phrase in (
            "STDRIVE101 manual gate-test linked-image build-only record no-power",
            "EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LINKED-IMAGE-BUILD-ONLY-RECORD-001",
            "TASK-2026-06-20-stdrive101-manual-gate-test-linked-image-build-only-record-no-power",
            "add_executable(stdrive101_gate_lockout_image",
            "startup_stm32g474xx.s",
            "STM32G474XX_FLASH.ld",
            "system_stm32g4xx.c",
            "syscalls.c",
            "sysmem.c",
            "CMAKE_SYSTEM_NAME=Generic",
            "CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY",
            "stdrive101_gate_lockout_image.elf",
            "stdrive101_gate_lockout_image.map",
            "87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6",
            "A020546A3D1D56B1C509939161BD80E5A25EC5843C928B9BC13E8D07684FF6C0",
            "1356 0 1568 2924 b6c",
            "RAM:        1568 B",
            "FLASH:        1356 B",
            "no forbidden source matches",
            "no forbidden ELF symbol matches",
            "no forbidden MAP matches",
            "no flash",
            "no Run / Debug",
            "no USB runtime execution",
            "no 24 V",
            "no Gate PWM output",
            "Motor Pilot",
            "Motor Profiler",
            "motor connection",
            "no readiness claim",
        ):
            self.assertIn(phrase, text)

    def test_linked_image_build_only_record_is_registered_without_runtime_upgrade(self):
        combined = (
            read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "stdrive101_manual_gate_test_linked_image_build_only_record_2026-06-20.md",
            "EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LINKED-IMAGE-BUILD-ONLY-RECORD-001",
            "TASK-2026-06-20-stdrive101-manual-gate-test-linked-image-build-only-record-no-power",
            "STDRIVE101 manual gate-test linked-image build-only record no-power",
            "repo-local CMake linked target stdrive101_gate_lockout_image added",
            "Generic bare-metal CMake configure and Ninja build passed",
            "ELF and MAP artifacts produced and hashed",
            "forbidden source ELF MAP screens clean",
            "build-only evidence",
            "stdrive101_gate_lockout_image.elf",
            "stdrive101_gate_lockout_image.map",
            "no flash",
            "no Run Debug",
            "no USB runtime",
            "no 24 V",
            "no PWM-output validation",
            "no powered-drive readiness",
            "separate USB-only runtime lockout phase-gate plan",
        ):
            self.assertIn(phrase, combined)

    def test_usb_only_runtime_phase_gate_plan_records_no_execution_boundary(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_manual_gate_test_usb_only_runtime_lockout_phase_gate_plan_2026-06-20.md"
        )

        for phrase in (
            "STDRIVE101 manual gate-test USB-only runtime lockout phase-gate plan no-power",
            "EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-PHASE-GATE-PLAN-001",
            "TASK-2026-06-20-stdrive101-manual-gate-test-usbonly-runtime-lockout-phase-gate-plan",
            "linked-image build-only record accepted as image-boundary evidence",
            "phase-gate plan only",
            "no flash",
            "no Run Debug",
            "no USB runtime execution",
            "no 24 V",
            "no PWM-output validation",
            "no powered-drive readiness",
            "stdrive101_gate_lockout_image",
            "stdrive101_gate_lockout_image.elf",
            "87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6",
            "stdrive101_gate_lockout_image.map",
            "A020546A3D1D56B1C509939161BD80E5A25EC5843C928B9BC13E8D07684FF6C0",
            "explicitly asks to execute the USB-only lockout runtime check",
            "HSPY / 24 V is OFF",
            "`VS / 24V_FUSED`",
            "below `1 V`",
            "Motor disconnected",
            "wake resistor / LIN1 stimulus is removed",
            "Motor Pilot and Motor Profiler closed / unused",
            "Do not fill this table in this record",
            "stable reading above `0.3 V`",
            "Do not continue by trying one more time",
            "The next engineering checkpoint is not motor power",
        ):
            self.assertIn(phrase, text)

    def test_usb_only_runtime_phase_gate_plan_is_registered_without_runtime_upgrade(self):
        combined = (
            read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "stdrive101_manual_gate_test_usb_only_runtime_lockout_phase_gate_plan_2026-06-20.md",
            "EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-PHASE-GATE-PLAN-001",
            "TASK-2026-06-20-stdrive101-manual-gate-test-usbonly-runtime-lockout-phase-gate-plan",
            "STDRIVE101 manual gate-test USB-only runtime lockout phase-gate plan no-power",
            "linked-image build-only record accepted as image-boundary evidence",
            "candidate USB-only runtime preconditions",
            "measurement table",
            "stop rules named",
            "phase-gate plan only",
            "no flash",
            "no Run Debug",
            "no USB runtime execution",
            "no 24 V",
            "no PWM-output validation",
            "no powered-drive readiness",
            "only a later separate USB-only runtime execution record",
            "explicit user request",
        ):
            self.assertIn(phrase, combined)

    def test_usb_only_runtime_execution_entry_opens_only_lockout_measurement(self):
        text = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_manual_gate_test_usb_only_runtime_lockout_execution_entry_2026-06-20.md"
        )

        for phrase in (
            "STDRIVE101 manual gate-test USB-only runtime lockout execution entry",
            "EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-EXECUTION-ENTRY-001",
            "TASK-2026-06-20-stdrive101-manual-gate-test-usbonly-runtime-lockout-execution-entry",
            "USB-only lockout runtime 检查",
            "HSPY / 24 V `OFF` and physically disconnected",
            "`VS / 24V_FUSED < 1 V`",
            "motor disconnected",
            "wake resistor / `LIN1` stimulus removed",
            "Motor Pilot / Profiler closed",
            "no abnormal heat / smell / sound",
            "87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6",
            "opens exactly one USB-only lockout flash-run measurement pass",
            "Still forbidden",
            "24 V",
            "Gate PWM output or PWM validation",
            "Motor Pilot",
            "Motor Profiler",
            "motor connection",
            "any normal generated MCSDK application run",
            "Do not infer values",
            "Expected safe result for `CN3_1` through `CN3_6`: close to `0 V`",
            "stable above `0.3 V`",
            "does not contain the measured runtime result yet",
            "create a separate runtime result record",
        ):
            self.assertIn(phrase, text)

    def test_usb_only_runtime_execution_entry_is_registered_without_powered_upgrade(self):
        combined = (
            read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "stdrive101_manual_gate_test_usb_only_runtime_lockout_execution_entry_2026-06-20.md",
            "EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-EXECUTION-ENTRY-001",
            "TASK-2026-06-20-stdrive101-manual-gate-test-usbonly-runtime-lockout-execution-entry",
            "STDRIVE101 manual gate-test USB-only runtime lockout execution entry",
            "user confirmed HSPY 24 V OFF and physically disconnected",
            "VS 24V_FUSED below 1 V",
            "linked-image ELF hash matched",
            "opens exactly one USB-only lockout flash-run measurement pass",
            "no 24 V",
            "no PWM-output validation",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "separate runtime result record",
        ):
            self.assertIn(phrase, combined)

    def test_usb_only_runtime_lockout_result_records_measurements_without_powered_upgrade(self):
        result = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_manual_gate_test_usb_only_runtime_lockout_result_2026-06-20.md"
        )
        combined = (
            result
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 manual gate-test USB-only runtime lockout result",
            "EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-RESULT-001",
            "TASK-2026-06-20-stdrive101-manual-gate-test-usbonly-runtime-lockout-result",
            "reviewed lockout ELF converted to BIN and copied through ST-LINK mass storage",
            "no FAIL.TXT after copy",
            "87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6",
            "CBF833C8E9289D8B4A952C32C641CAA94928F1F8119C5DC528EBD779915EA6BE",
            "`CN3_1` driver input | `0 V`",
            "`CN3_2 / LIN1` | `0 V`",
            "`CN3_3` driver input | `0 V`",
            "`CN3_4` driver input | `0 V`",
            "`CN3_5` driver input | `0 V`",
            "`CN3_6` driver input | `0 V`",
            "`CN3_13 / nFAULT` | `3.3 V`",
            "`CN3_14 / 3V3` | `3.3 V`",
            "`REG12` | `0 V`",
            "driver-input stop rule not hit",
            "USB-only runtime evidence only",
            "no 24 V",
            "no PWM-output validation",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "Not usable to claim 24 V behavior",
            "separate dated phase-gate review",
        ):
            self.assertIn(phrase, combined)

    def test_24v_static_lockout_phase_gate_records_planning_without_powered_upgrade(self):
        plan = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_manual_gate_test_24v_static_lockout_phase_gate_plan_2026-06-20.md"
        )
        combined = (
            plan
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 manual gate-test 24V static lockout phase-gate plan",
            "EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-24V-STATIC-LOCKOUT-PHASE-GATE-PLAN-001",
            "TASK-2026-06-20-stdrive101-manual-gate-test-24v-static-lockout-phase-gate-plan",
            "USB-only runtime lockout result accepted as driver-input-low evidence",
            "earlier USB plus 24V static baseline carried forward",
            "candidate 24V static lockout execution preconditions",
            "measurement table",
            "rollback path",
            "stop rules",
            "phase-gate plan only",
            "no 24V execution in this record",
            "no flash",
            "no Run / Debug",
            "no normal generated MCSDK app run",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "Do not fill this table in this record",
            "HSPY is set to `24 V / 0.2 A`",
            "Black lead on board GND",
            "stable reading above `0.3 V`",
            "HSPY output OFF first",
            "Do not continue by trying one more time",
            "The next engineering checkpoint is not motor power",
            "later separate 24 V static lockout execution-entry record",
            "Not usable to claim 24 V runtime behavior",
        ):
            self.assertIn(phrase, combined)

    def test_24v_static_lockout_execution_entry_is_historical_after_carry_forward(self):
        entry = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_manual_gate_test_24v_static_lockout_execution_entry_2026-06-20.md"
        )
        combined = (
            entry
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 manual gate-test 24V static lockout execution entry",
            "EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-24V-STATIC-LOCKOUT-EXECUTION-ENTRY-001",
            "TASK-2026-06-20-stdrive101-manual-gate-test-24v-static-lockout-execution-entry",
            "user confirmed HSPY output OFF",
            "HSPY set to 24 V 0.2 A",
            "VS 24V_FUSED close to 0 V and below 1 V",
            "motor disconnected",
            "wake stimulus removed",
            "Motor Pilot and Motor Profiler closed",
            "no abnormal heat smell sound",
            "USB-only lockout result accepted as driver-input-low evidence",
            "opens exactly one bounded 24 V static lockout measurement pass",
            "historical execution-entry record",
            "later carry-forward result closes",
            "duplicate-measurement branch",
            "no firmware flash",
            "no new Run / Debug",
            "no normal generated MCSDK app run",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "Black lead stays on board GND",
            "stable above `0.3 V`",
            "current is above `0.08 A`",
            "`REG12` rises unexpectedly above `1 V`",
            "Do not continue by trying one more time",
            "superseded by the carry-forward result",
            "do not repeat the 24 V static table",
            "Not usable to claim PWM validation",
        ):
            self.assertIn(phrase, combined)

    def test_24v_static_lockout_carry_forward_result_records_no_repeat_boundary(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_manual_gate_test_24v_static_lockout_carry_forward_result_2026-06-20.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        result = read_repo_text(artifact)
        combined = (
            result
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 manual gate-test 24V static lockout carry-forward result",
            "EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-24V-STATIC-LOCKOUT-CARRY-FORWARD-RESULT-001",
            "TASK-2026-06-20-stdrive101-manual-gate-test-24v-static-lockout-carry-forward-result",
            "stdrive101_manual_gate_test_24v_static_lockout_carry_forward_result_2026-06-20.md",
            "no repeated measurement",
            "stdrive101_usb24_static_recheck_result_2026-06-20.md",
            "HSPY CV about 0.045 A",
            "CN3_1 through CN3_6 all close to 0 V",
            "nFAULT 3.3 V",
            "CN3_14 3.3 V",
            "REG12 0.3 V",
            "stdrive101_manual_gate_test_usb_only_runtime_lockout_result_2026-06-20.md",
            "87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6",
            "CBF833C8E9289D8B4A952C32C641CAA94928F1F8119C5DC528EBD779915EA6BE",
            "driver-input stop rule not hit",
            "no claim of new 24V lockout measurement under lockout image",
            "static baseline accepted for no-repeat gating only",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "no-power phase-gate plan",
            "gate-waveform / PWM-output planning",
            "Not usable to claim 24 V runtime behavior",
            "power-stage readiness",
            "motor readiness",
        ):
            self.assertIn(phrase, combined)

    def test_gate_waveform_pwm_output_phase_gate_records_no_execution_boundary(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_pwm_output_no_power_phase_gate_plan_2026-06-20.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        plan = read_repo_text(artifact)
        combined = (
            plan
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 gate-waveform PWM-output no-power phase-gate plan",
            "EV-2026-06-20-STDRIVE101-GATE-WAVEFORM-PWM-OUTPUT-NO-POWER-PHASE-GATE-PLAN-001",
            "TASK-2026-06-20-stdrive101-gate-waveform-pwm-output-no-power-phase-gate-plan",
            "stdrive101_gate_waveform_pwm_output_no_power_phase_gate_plan_2026-06-20.md",
            "24V static lockout carry-forward result accepted as static boundary evidence",
            "linked lockout image and USB-only runtime lockout result carried forward as driver-input-low evidence",
            "normal generated MCSDK PWM path remains blocked",
            "future gate-waveform execution gates",
            "instrumentation requirements",
            "rollback path",
            "stop rules named as future-only items",
            "phase-gate plan only",
            "no flash",
            "no Run Debug",
            "no 24 V",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "Gate E0",
            "Gate E1",
            "Gate E2",
            "Gate E3",
            "Gate E4",
            "Gate E5",
            "USB-only neutral-state check",
            "scope-only no-motor execution-entry",
            "oscilloscope probing on live gate or phase nodes",
            "Next checkpoint is Gate E0 only",
            "Not usable to claim PWM validation",
            "power-stage readiness",
            "motor readiness",
        ):
            self.assertIn(phrase, combined)

    def test_gate_waveform_image_design_plan_records_gate_e0_boundary(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_image_design_plan_no_power_2026-06-20.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        plan = read_repo_text(artifact)
        combined = (
            plan
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 gate-waveform image design plan no-power",
            "EV-2026-06-20-STDRIVE101-GATE-WAVEFORM-IMAGE-DESIGN-PLAN-NO-POWER-001",
            "TASK-2026-06-20-stdrive101-gate-waveform-image-design-plan-no-power",
            "stdrive101_gate_waveform_image_design_plan_no_power_2026-06-20.md",
            "Gate E0 only",
            "separate isolated waveform candidate required",
            "normal generated MCSDK app and command ingress remain blocked",
            "six candidate driver inputs fixed as PA8 PA9 PA10 PB13 PB14 PB15",
            "idle state must force all six low before and after any future candidate window",
            "future TIM1 MOE CCER break AOE dead-time and complementary-overlap policy required before source or build",
            "design plan only",
            "no source package",
            "no CMake edit",
            "no build",
            "no flash",
            "no Run Debug",
            "no Run / Debug",
            "no USB runtime execution",
            "no 24 V",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "`PA8`",
            "`PA9`",
            "`PA10`",
            "`PB13`",
            "`PB14`",
            "`PB15`",
            "`MOE`",
            "`CCER`",
            "complementary-overlap",
            "`MC_StartMotor1`",
            "`MCI_START`",
            "PC13 start / stop",
            "MCP / ASPEP command ingress",
            "Motor Pilot",
            "Motor Profiler",
            "Gate E1 isolated waveform source-package planning/review",
            "Not usable to claim PWM validation",
            "power-stage readiness",
            "motor readiness",
        ):
            self.assertIn(phrase, combined)

    def test_gate_waveform_isolated_source_package_review_records_gate_e1_boundary(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_isolated_source_package_review_no_power_2026-06-21.md"
        )
        package = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "manual_gate_waveform_source_package_2026-06-21"
        )
        self.assertTrue((ROOT / artifact).exists())
        self.assertTrue((ROOT / package / "README.md").exists())
        self.assertTrue((ROOT / package / "Inc" / "gate_waveform_candidate.h").exists())
        self.assertTrue((ROOT / package / "Src" / "gate_waveform_candidate.c").exists())
        self.assertTrue((ROOT / package / "Src" / "main_waveform_candidate.c").exists())
        self.assertFalse((ROOT / package / "CMakeLists.txt").exists())

        review = read_repo_text(artifact)
        source = (
            read_repo_text(package + "/Inc/gate_waveform_candidate.h")
            + read_repo_text(package + "/Src/gate_waveform_candidate.c")
            + read_repo_text(package + "/Src/main_waveform_candidate.c")
        )
        combined = (
            review
            + source
            + read_repo_text(package + "/README.md")
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 gate-waveform isolated source package review no-power",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-ISOLATED-SOURCE-PACKAGE-REVIEW-NO-POWER-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-isolated-source-package-review-no-power",
            "stdrive101_gate_waveform_isolated_source_package_review_no_power_2026-06-21.md",
            "manual_gate_waveform_source_package_2026-06-21",
            "Gate E1 source package created for review only",
            "package has no CMakeLists",
            "Gate E2 compile-acknowledgement #error guard",
            "GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK",
            "Gate E1 source package only: open and record a dated Gate E2 build-only boundary before compiling.",
            "future isolated waveform image remains separate from normal generated MCSDK app and lockout image",
            "candidate driver inputs fixed as PA8 PA9 PA10 PB13 PB14 PB15",
            "startup and shutdown force all six low",
            "1 kHz",
            "100 permille duty",
            "16 period window",
            "8 pre-idle periods",
            "32 post-idle periods",
            "DTG 0x90",
            "TIM1 MOE CCER break AOE and dead-time policy visible in source",
            "nFAULT stop path disables TIM1 outputs and forces all six low",
            "source review only",
            "no build",
            "no flash",
            "no Run Debug",
            "no Run / Debug",
            "no USB runtime",
            "no 24 V",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "`PA8`",
            "`PA9`",
            "`PA10`",
            "`PB13`",
            "`PB14`",
            "`PB15`",
            "gate_waveform_candidate_force_idle_low",
            "wait_for_pwm_periods_or_fault",
            "disable_tim1_outputs_keep_counter",
            "command_ingress_present = false",
            "No `CMakeLists.txt`",
            "no forbidden source matches",
            "Next checkpoint is Gate E2 only",
            "object-only and linked-image build-only boundary plan",
            "Not usable to claim compiled firmware",
            "power-stage readiness",
            "motor readiness",
        ):
            self.assertIn(phrase, combined)

        forbidden_source_terms = (
            "MC_StartMotor1",
            "MCI_START",
            "PC13",
            "MCP",
            "ASPEP",
            "Motor Pilot",
            "Motor Profiler",
            "R3_2_TurnOnLowSides",
            "PWMC_SwitchOnPWM",
            "LL_TIM_EnableAllOutputs",
            "HALL_M1",
            "PID_",
            "STC_",
            "HAL_Delay",
            "printf",
            "malloc",
            "free",
        )
        for phrase in forbidden_source_terms:
            self.assertNotIn(phrase, source)

    def test_gate_waveform_build_only_record_records_gate_e2_boundary(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_build_only_record_no_power_2026-06-21.md"
        )
        source_package = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "manual_gate_waveform_source_package_2026-06-21"
        )
        build_package = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "manual_gate_waveform_build_only_2026-06-21"
        )
        self.assertTrue((ROOT / artifact).exists())
        self.assertTrue((ROOT / build_package / "README.md").exists())
        self.assertTrue((ROOT / build_package / "CMakeLists.txt").exists())
        self.assertTrue((ROOT / build_package / "Src" / "minimal_runtime.c").exists())
        self.assertFalse((ROOT / source_package / "CMakeLists.txt").exists())

        record = read_repo_text(artifact)
        cmake = read_repo_text(build_package + "/CMakeLists.txt")
        runtime = read_repo_text(build_package + "/Src/minimal_runtime.c")
        combined = (
            record
            + cmake
            + runtime
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 gate-waveform build-only record no-power",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-BUILD-ONLY-RECORD-NO-POWER-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-build-only-record-no-power",
            "manual_gate_waveform_build_only_2026-06-21",
            "manual_gate_waveform_source_package_2026-06-21",
            "Gate E2 object-only and linked-image build-only evidence",
            "GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK",
            "Gate E1 source package remains source-review only and has no CMakeLists",
            "CMAKE_SYSTEM_NAME=Generic",
            "CMAKE_SYSTEM_PROCESSOR=arm",
            "CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY",
            "GNU Tools for STM32",
            "14.3.1",
            "ninja 1.13.2",
            "stdrive101_gate_waveform_candidate_objects",
            "stdrive101_gate_waveform_candidate_image",
            "stdrive101_gate_waveform_candidate_image.elf",
            "stdrive101_gate_waveform_candidate_image.map",
            "10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C",
            "170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C",
            "text=1852",
            "data=0",
            "bss=1544",
            "dec=3396",
            "hex=d44",
            "RAM",
            "1.18%",
            "FLASH",
            "0.35%",
            "08000000 R g_pfnVectors",
            "08000420 t disable_tim1_outputs_keep_counter",
            "0800051c t wait_for_pwm_periods_or_fault",
            "080005a4 T gate_waveform_candidate_force_idle_low",
            "080005bc T gate_waveform_candidate_run_once",
            "080006a4 T main",
            "080006b8 T __libc_init_array",
            "080006c4 T _init",
            "080006d0 T _fini",
            "080006dc W Reset_Handler",
            "0800072e T SystemInit",
            "20020000 R _estack",
            "-nostdlib",
            "minimal runtime",
            "no forbidden source or CMake path matches",
            "no forbidden ELF symbol matches",
            "no forbidden MAP matches",
            "no flash",
            "no Run Debug",
            "no Run / Debug",
            "no USB runtime",
            "no USB runtime execution",
            "no 24 V",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "Gate E3 only",
            "USB-only neutral-state phase-gate plan",
            "not runtime execution",
            "Not usable to claim flashability",
            "power-stage readiness",
            "motor readiness",
        ):
            self.assertIn(phrase, combined)

    def test_gate_waveform_build_only_record_does_not_create_runtime_artifacts(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_build_only_record_no_power_2026-06-21.md"
        )
        build_package = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "manual_gate_waveform_build_only_2026-06-21"
        )
        cmake = read_repo_text(build_package + "/CMakeLists.txt")
        record = read_repo_text(artifact)

        for phrase in (
            "add_library(stdrive101_gate_waveform_candidate_objects OBJECT",
            "add_executable(stdrive101_gate_waveform_candidate_image",
            "Src/minimal_runtime.c",
            "startup_stm32g474xx.s",
            "system_stm32g4xx.c",
            "STM32G474XX_FLASH.ld",
            "GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK",
            "-nostdlib",
        ):
            self.assertIn(phrase, cmake)

        for forbidden in (
            "add_custom_command",
            ".hex",
            ".bin",
            "objcopy",
            "FLASH_RUN",
        ):
            self.assertNotIn(forbidden, cmake)

        for phrase in (
            "No HEX or BIN target is defined here.",
            "No HEX / BIN target",
            "Gate E3 must be a plan or review unless a later separate dated execution-entry explicitly opens USB-only runtime",
            "Still forbidden after this Gate E2 record",
            "USB runtime execution",
            "24 V",
            "Gate PWM output",
        ):
            self.assertIn(phrase, record)

    def test_gate_waveform_usb_only_neutral_state_plan_records_gate_e3_boundary(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_usb_only_neutral_state_phase_gate_plan_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        plan = read_repo_text(artifact)
        main_source = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "manual_gate_waveform_source_package_2026-06-21/Src/main_waveform_candidate.c"
        )
        combined = (
            plan
            + main_source
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 gate-waveform USB-only neutral-state phase-gate plan",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-USBONLY-NEUTRAL-STATE-PHASE-GATE-PLAN-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-usbonly-neutral-state-phase-gate-plan",
            "stdrive101_gate_waveform_usb_only_neutral_state_phase_gate_plan_2026-06-21.md",
            "Gate E3 plan only",
            "Gate E2 linked-image build-only record accepted as image-boundary evidence",
            "candidate ELF and MAP hashes carried forward",
            "10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C",
            "170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C",
            "gate_waveform_candidate_run_once",
            "gate_waveform_candidate_force_idle_low",
            "current waveform candidate main calls gate_waveform_candidate_run_once once and then loops forcing idle low",
            "DMM-only future check can prove only post-window steady idle and cannot prove absence of a reset-time or boot-time transient",
            "later USB-only execution-entry must separately name flash or transfer method",
            "measurement instrument",
            "pre/post measurement table",
            "rollback path",
            "stop rules",
            "phase-gate plan only",
            "no flash",
            "no Run Debug",
            "no Run / Debug",
            "no USB runtime execution",
            "no 24 V",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "future DMM-only USB check can record only steady post-window idle state",
            "cannot prove there was no reset-time or boot-time transient",
            "Do not fill this table in this record",
            "explicit user request",
            "freshly confirmed preconditions",
            "source-side neutral-wrapper review",
            "Gate E4 remains closed",
            "Not usable to claim flashability",
            "power-stage readiness",
            "motor readiness",
        ):
            self.assertIn(phrase, combined)

    def test_gate_waveform_usb_only_neutral_state_plan_is_not_execution(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_usb_only_neutral_state_phase_gate_plan_2026-06-21.md"
        )
        plan = read_repo_text(artifact)

        for phrase in (
            "This record is planning only",
            "Firmware runtime action:",
            "none in this record",
            "No flash, no Run / Debug, no USB runtime execution",
            "Do not use this table to execute now",
            "This record does not open Gate E4",
            "Still forbidden after this Gate E3 plan",
            "USB runtime execution",
            "24 V",
            "Gate PWM output",
            "oscilloscope probing on live gate or phase nodes",
            "Motor Pilot / Profiler",
            "motor connection",
        ):
            self.assertIn(phrase, plan)

    def test_gate_waveform_neutral_wrapper_source_review_records_boundary(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_source_review_no_power_2026-06-21.md"
        )
        package = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "manual_gate_waveform_neutral_wrapper_source_package_2026-06-21"
        )
        self.assertTrue((ROOT / artifact).exists())
        self.assertTrue((ROOT / package / "README.md").exists())
        self.assertTrue((ROOT / package / "Inc" / "gate_waveform_neutral_wrapper.h").exists())
        self.assertTrue((ROOT / package / "Src" / "main_neutral_wrapper.c").exists())
        self.assertFalse((ROOT / package / "CMakeLists.txt").exists())

        review = read_repo_text(artifact)
        package_readme = read_repo_text(package + "/README.md")
        header = read_repo_text(package + "/Inc/gate_waveform_neutral_wrapper.h")
        source = read_repo_text(package + "/Src/main_neutral_wrapper.c")
        combined = (
            review
            + package_readme
            + header
            + source
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 gate-waveform neutral-wrapper source review no-power",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-SOURCE-REVIEW-NO-POWER-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-source-review-no-power",
            "stdrive101_gate_waveform_neutral_wrapper_source_review_no_power_2026-06-21.md",
            "manual_gate_waveform_neutral_wrapper_source_package_2026-06-21",
            "source-side wrapper package created for review only",
            "package has no CMakeLists",
            "GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK",
            "Neutral-wrapper source package only: open and record a dated build-only boundary before compiling.",
            "wrapper replaces future candidate entry point only",
            "gate_waveform_candidate_force_idle_low before the forever loop and inside the forever loop",
            "wrapper source contains no gate_waveform_candidate_run_once call",
            "no TIM1 waveform-window or output-enable path in wrapper source",
            "current Gate E2 run_once image remains unsuitable for proving no boot transient with DMM-only evidence",
            "source review only",
            "no build",
            "no flash",
            "no Run Debug",
            "no Run / Debug",
            "no USB runtime execution",
            "no 24 V",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "AE04E5D1FE022F0B730F968E1CD82131A37CA6DC75E66EC9B51C87F26450C25D",
            "4E541FF0E4D64AAA8CADFA3182A257843C94B10A7F2EA4E954A55346751B363B",
            "265587CDBE9CB63E2A95D5D06C4F7BBEEE967BDAECE88383782C794DF9A76310",
            "gate_waveform_neutral_wrapper_hold_idle_forever",
            "future build-only package must include reviewed `gate_waveform_candidate.c`, exclude old `main_waveform_candidate.c`, and use this wrapper `main_neutral_wrapper.c` as the only entry point",
            "no forbidden source matches in wrapper `Inc/` or `Src/`",
            "neutral-wrapper build-only boundary plan or build-only record",
            "Not usable to claim compiled firmware",
            "power-stage readiness",
            "motor readiness",
        ):
            self.assertIn(phrase, combined)

        for phrase in (
            "GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK",
            "#error",
        ):
            self.assertIn(phrase, header)

        for phrase in (
            "gate_waveform_candidate_force_idle_low",
            "gate_waveform_neutral_wrapper_hold_idle_forever",
            "int main(void)",
            "for (;;)",
        ):
            self.assertIn(phrase, source)

        for forbidden in (
            "gate_waveform_candidate_run_once",
            "configure_tim1_for_candidate_window",
            "arm_candidate_outputs",
            "TIM_BDTR_MOE",
            "TIM_CCER",
            "MC_StartMotor1",
            "MCI_START",
            "PC13",
            "MCP",
            "ASPEP",
            "Motor Pilot",
            "Motor Profiler",
            "R3_2_TurnOnLowSides",
            "PWMC_SwitchOnPWM",
            "LL_TIM_EnableAllOutputs",
            "HALL_M1",
            "PID_",
            "STC_",
            "HAL_Delay",
            "printf",
            "malloc",
            "free",
        ):
            self.assertNotIn(forbidden, header + source)

    def test_gate_waveform_neutral_wrapper_source_review_is_not_runtime(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_source_review_no_power_2026-06-21.md"
        )
        package = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "manual_gate_waveform_neutral_wrapper_source_package_2026-06-21"
        )
        review = read_repo_text(artifact)
        combined = (
            review
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        self.assertFalse((ROOT / package / "CMakeLists.txt").exists())

        for phrase in (
            "This record is source-review evidence only",
            "none in this record",
            "No object build, linked-image build, flash, Run /",
            "No object file, ELF, MAP, HEX, or BIN is produced by this package",
            "The package is readable source review evidence, not a build target",
            "This source review does not prove runtime behavior",
            "This record still does not prove",
            "that the wrapper compiles",
            "that a linked neutral-wrapper image exists",
            "that USB-only DMM readings will be idle-low",
            "Still forbidden after this neutral-wrapper source review",
            "USB runtime execution",
            "24 V",
            "Gate PWM output",
            "oscilloscope probing on live gate or phase nodes",
            "Motor Pilot / Profiler",
            "motor connection",
            "neutral-wrapper build-only boundary plan or build-only record",
            "not USB runtime",
            "still with no flash, Run / Debug, USB runtime execution, 24 V, Gate PWM output",
        ):
            self.assertIn(phrase, combined)

    def test_gate_waveform_neutral_wrapper_build_only_package_records_sources(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_build_only_record_no_power_2026-06-21.md"
        )
        waveform_source_package = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "manual_gate_waveform_source_package_2026-06-21"
        )
        wrapper_source_package = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "manual_gate_waveform_neutral_wrapper_source_package_2026-06-21"
        )
        build_package = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "manual_gate_waveform_neutral_wrapper_build_only_2026-06-21"
        )

        self.assertTrue((ROOT / artifact).exists())
        self.assertTrue((ROOT / build_package / "README.md").exists())
        self.assertTrue((ROOT / build_package / "CMakeLists.txt").exists())
        self.assertTrue((ROOT / build_package / "Src" / "minimal_runtime.c").exists())
        self.assertFalse((ROOT / waveform_source_package / "CMakeLists.txt").exists())
        self.assertFalse((ROOT / wrapper_source_package / "CMakeLists.txt").exists())

        cmake = read_repo_text(build_package + "/CMakeLists.txt")
        readme = read_repo_text(build_package + "/README.md")
        runtime = read_repo_text(build_package + "/Src/minimal_runtime.c")
        record = read_repo_text(artifact)

        for phrase in (
            "add_library(stdrive101_gate_waveform_neutral_wrapper_objects OBJECT",
            "add_executable(stdrive101_gate_waveform_neutral_wrapper_image",
            "GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK",
            "GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK",
            "manual_gate_waveform_source_package_2026-06-21",
            "manual_gate_waveform_neutral_wrapper_source_package_2026-06-21",
            "Src/gate_waveform_candidate.c",
            "Src/main_neutral_wrapper.c",
            "Src/minimal_runtime.c",
            "startup_stm32g474xx.s",
            "system_stm32g4xx.c",
            "STM32G474XX_FLASH.ld",
            "-nostdlib",
            "No HEX or BIN target is defined here.",
            "__libc_init_array",
            "_init",
            "_fini",
        ):
            self.assertIn(phrase, cmake + readme + runtime + record)

        for forbidden in (
            "main_waveform_candidate.c",
            "add_custom_command",
            ".hex",
            ".bin",
            "objcopy",
            "FLASH_RUN",
        ):
            self.assertNotIn(forbidden, cmake)

        build_ninja = ROOT / ".tmp/gwnw_build_2026-06-21_clean/build.ninja"
        if build_ninja.exists():
            ninja_text = build_ninja.read_text(encoding="utf-8")
            self.assertIn("gate_waveform_candidate.c", ninja_text)
            self.assertIn("main_neutral_wrapper.c", ninja_text)
            self.assertNotIn("main_waveform_candidate", ninja_text)
            for forbidden in (
                "add_custom_command",
                ".hex",
                ".bin",
                "objcopy",
                "FLASH_RUN",
                "ST-LINK",
                "NOD_G474RE",
            ):
                self.assertNotIn(forbidden, ninja_text)

    def test_gate_waveform_neutral_wrapper_build_only_record_keeps_boundary(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_build_only_record_no_power_2026-06-21.md"
        )
        build_package = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "manual_gate_waveform_neutral_wrapper_build_only_2026-06-21"
        )
        record = read_repo_text(artifact)
        cmake = read_repo_text(build_package + "/CMakeLists.txt")
        combined = (
            record
            + cmake
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 gate-waveform neutral-wrapper build-only record no-power",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-BUILD-ONLY-RECORD-NO-POWER-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-build-only-record-no-power",
            "manual_gate_waveform_neutral_wrapper_build_only_2026-06-21",
            "object-only and linked-image build-only evidence for the neutral-wrapper source review",
            "source-review packages remain source-review only and have no CMakeLists",
            "build inputs include reviewed",
            "gate_waveform_candidate.c",
            "main_neutral_wrapper.c",
            "old main_waveform_candidate.c excluded",
            "CMAKE_SYSTEM_NAME=Generic",
            "CMAKE_SYSTEM_PROCESSOR=arm",
            "CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY",
            "GNU Tools for STM32",
            "14.3.1",
            "ninja 1.13.2",
            "stdrive101_gate_waveform_neutral_wrapper_objects",
            "stdrive101_gate_waveform_neutral_wrapper_image",
            "stdrive101_gate_waveform_neutral_wrapper_image.elf",
            "stdrive101_gate_waveform_neutral_wrapper_image.map",
            "C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591",
            "5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83",
            "text=1044",
            "data=0",
            "bss=1536",
            "dec=2580",
            "hex=a14",
            "1.17%",
            "0.20%",
            "08000000 R g_pfnVectors",
            "0800035c T gate_waveform_candidate_force_idle_low",
            "08000374 T gate_waveform_neutral_wrapper_hold_idle_forever",
            "08000382 T main",
            "080003b4 W Reset_Handler",
            "08000406 T SystemInit",
            "20020000 R _estack",
            "retained ELF symbol table has no `gate_waveform_candidate_run_once`",
            "`main_waveform_candidate` symbol",
            ".text.gate_waveform_candidate_run_once",
            "discarded-input-section area",
            "0x00000000",
            "-ffunction-sections",
            "--gc-sections",
            "No HEX or BIN target is defined here.",
            "no forbidden retained ELF symbol matches",
            "no forbidden MAP matches",
            "build-only evidence",
            "no flash",
            "no Run Debug",
            "no Run / Debug",
            "no USB runtime execution",
            "no 24 V",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "neutral-wrapper USB-only neutral-state phase-gate plan or review",
            "not runtime execution",
            "Not usable to claim flashability",
            "absence of real reset-time transient on hardware",
            "power-stage readiness",
            "motor readiness",
        ):
            self.assertIn(phrase, combined)

    def test_gate_waveform_neutral_wrapper_build_only_record_is_not_runtime(self):
        record = read_repo_text(
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_build_only_record_no_power_2026-06-21.md"
        )

        for phrase in (
            "This record is build-only evidence",
            "It does not authorize:",
            "firmware flash",
            "Run / Debug",
            "USB runtime execution",
            "applying 24 V",
            "Gate PWM output on hardware",
            "oscilloscope probing on live gate or phase nodes",
            "normal generated MCSDK application execution",
            "Motor Pilot",
            "Motor Profiler",
            "motor connection",
            "Hall closed loop",
            "sensorless operation",
            "power-stage readiness or motor readiness claims",
            "This build-only record still does not prove",
            "that this ELF should be flashed",
            "reset-time or runtime pin behavior on real hardware",
            "that USB-only DMM readings would be idle-low",
            "Still forbidden after this neutral-wrapper build-only record",
        ):
            self.assertIn(phrase, record)

        for forbidden in (
            "opens exactly one USB-only",
            "opens one bounded",
            "HSPY is set to",
            "Do not fill this table",
            "copy through ST-LINK",
            "FAIL.TXT",
        ):
            self.assertNotIn(forbidden, record)

    def test_gate_waveform_neutral_wrapper_usb_only_plan_records_boundary(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_usb_only_neutral_state_phase_gate_plan_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        plan = read_repo_text(artifact)
        for phrase in (
            "STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only Neutral-State Phase-Gate Plan",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-NEUTRAL-STATE-PHASE-GATE-PLAN-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-neutral-state-phase-gate-plan",
            "neutral-wrapper build-only record accepted as",
            "image-boundary evidence",
            "C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591",
            "5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83",
            "main_neutral_wrapper.c",
            "main_waveform_candidate.c",
            "gate_waveform_neutral_wrapper_hold_idle_forever",
            "has no `gate_waveform_candidate_run_once`",
            ".text.gate_waveform_candidate_run_once",
            "discarded input-section area",
            "0x00000000",
            "This record is planning only",
            "future USB-only execution-entry must separately name transfer method",
            "optional BIN hash if generated",
            "measurement instrument",
            "pre/post measurement table",
            "rollback path",
            "stop rules",
            "Do not use this table to execute now",
            "User explicitly asks to execute the neutral-wrapper USB-only neutral-state check",
            "DMM can show steady neutral state after firmware reaches the wrapper loop",
            "DMM cannot prove reset-time pin state before firmware control",
            "Do not fill this table in this record",
            "disconnect USB if needed",
            "do not retry",
            "This record does not open Gate E4",
            "Gate E4 remains future-only",
            "Still forbidden after this neutral-wrapper USB-only neutral-state plan",
            "flash",
            "Run / Debug",
            "USB runtime execution",
            "24 V",
            "Gate PWM output",
            "Motor Pilot / Profiler",
            "motor connection",
            "power-stage readiness or motor readiness claims",
        ):
            self.assertIn(phrase, plan)

    def test_gate_waveform_neutral_wrapper_usb_only_plan_is_registered_as_plan_only(self):
        combined = (
            read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "stdrive101_gate_waveform_neutral_wrapper_usb_only_neutral_state_phase_gate_plan_2026-06-21.md",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-NEUTRAL-STATE-PHASE-GATE-PLAN-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-neutral-state-phase-gate-plan",
            "STDRIVE101 gate-waveform neutral-wrapper USB-only neutral-state phase-gate plan",
            "neutral-wrapper build-only record accepted as image-boundary evidence",
            "neutral-wrapper ELF and MAP hashes carried forward",
            "source-review packages remain source-review only and have no CMakeLists",
            "build-only image uses main_neutral_wrapper.c and excludes old",
            "retained ELF symbol table has",
            "gate_waveform_neutral_wrapper_hold_idle_forever",
            "has no gate_waveform_candidate_run_once",
            "discarded zero-address input section",
            "phase-gate planning only",
            "no flash",
            "no Run Debug",
            "no Run / Debug",
            "no USB runtime execution",
            "no 24 V",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "only a separate neutral-wrapper USB-only neutral-state execution-entry",
            "explicit user request",
            "freshly confirmed preconditions",
            "Gate E4 remains closed",
            "Not usable to claim flashability",
            "reset-time pin behavior",
            "absence of real transient on hardware",
            "power-stage readiness",
            "motor readiness",
        ):
            self.assertIn(phrase, combined)

    def test_gate_waveform_neutral_wrapper_bin_artifact_record_has_downloadable_identity_only(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_bin_artifact_record_no_power_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        record = read_repo_text(artifact)
        combined = (
            record
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 gate-waveform neutral-wrapper BIN artifact record no-power",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-BIN-ARTIFACT-RECORD-NO-POWER-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-bin-artifact-record-no-power",
            "stdrive101_gate_waveform_neutral_wrapper_bin_artifact_record_no_power_2026-06-21.md",
            "neutral-wrapper ELF converted to BIN with STM32Cube GNU Arm objcopy",
            "C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591",
            "5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83",
            "CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71",
            "BIN size",
            "1044",
            "arm-none-eabi-objcopy",
            "gate_waveform_neutral_wrapper_hold_idle_forever",
            "has no retained gate_waveform_candidate_run_once",
            "D: NOD_G474RE",
            "no FAIL.TXT before copy",
            "No BIN copy was attempted in this record",
            "artifact preparation only",
            "no flash",
            "no Run Debug",
            "no USB runtime execution",
            "no 24 V",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
        ):
            self.assertIn(phrase, combined)

        for forbidden in (
            "neutral-wrapper BIN copied once to D:",
            "no FAIL.TXT after copy",
            "target BIN not retained on D: after copy",
            "Copy Result",
            "direct DMM readings",
        ):
            self.assertNotIn(forbidden, record)

    def test_gate_waveform_neutral_wrapper_usb_only_download_entry_opens_one_copy_only(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_usb_only_download_execution_entry_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        entry = read_repo_text(artifact)
        combined = (
            entry
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 gate-waveform neutral-wrapper USB-only download execution entry",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DOWNLOAD-EXECUTION-ENTRY-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-download-execution-entry",
            "user confirmed USB-only, 24V disconnected, motor disconnected",
            "allowed copying neutral-wrapper BIN to D:",
            "C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591",
            "5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83",
            "CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71",
            "D: volume label NOD_G474RE detected and FAIL.TXT absent before copy",
            "opens exactly one USB-only mass-storage BIN copy",
            "Transfer target",
            "D:\\stdrive101_gate_waveform_neutral_wrapper_image.bin",
            "Power",
            "USB / ST-LINK only",
            "HSPY / 24 V",
            "disconnected",
            "Motor",
            "disconnected",
            "Do not use Motor Pilot",
            "Motor Profiler",
            "Run / Debug",
            "24 V",
            "Gate PWM output",
            "motor connection",
            "no powered-drive readiness",
            "does not contain the copy",
            "measured neutral-state result yet",
        ):
            self.assertIn(phrase, combined)

        self.assertNotIn("no FAIL.TXT after copy", entry)
        self.assertNotIn("target BIN not retained on D: after copy", entry)

    def test_gate_waveform_neutral_wrapper_usb_only_download_result_is_not_dmm_pass(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_usb_only_download_result_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        result = read_repo_text(artifact)
        combined = (
            result
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 gate-waveform neutral-wrapper USB-only download result",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DOWNLOAD-RESULT-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-download-result",
            "neutral-wrapper BIN copied once to D: NOD_G474RE by ST-LINK mass storage",
            "source BIN SHA256 CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71",
            "no FAIL.TXT before copy",
            "no FAIL.TXT after copy",
            "target BIN not retained on D: after copy",
            "consistent with ST-LINK mass-storage consumption",
            "download result only",
            "no DMM neutral-state measurement result yet",
            "Version: V3J17M10",
            "Build:   Oct 17 2025 15:12:06",
            "Copy-Item",
            "Next Measurement Table",
            "`VS / 24V_FUSED`",
            "`CN3_1` driver input",
            "`CN3_2 / LIN1`",
            "`CN3_6` driver input",
            "`CN3_13 / nFAULT`",
            "`CN3_14 / 3V3`",
            "`REG12`",
            "stop-rule hit",
            "stably above `0.3 V`",
            "direct USB-only DMM table",
            "no Run Debug",
            "no 24 V",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
        ):
            self.assertIn(phrase, combined)

        for forbidden in (
            "DMM neutral-state pass",
            "power-stage readiness validated",
            "motor readiness validated",
            "Hall closed loop validated",
            "sensorless operation validated",
        ):
            self.assertNotIn(forbidden, result)

    def test_gate_waveform_neutral_wrapper_download_status_is_superseded_after_residual_result(self):
        active_task = read_repo_text("workflow/ACTIVE_TASK.md")
        combined = (
            read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + active_task
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only Download Result Recorded",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DOWNLOAD-RESULT-001",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DOWNLOAD-EXECUTION-ENTRY-001",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-BIN-ARTIFACT-RECORD-NO-POWER-001",
            "stdrive101_gate_waveform_neutral_wrapper_usb_only_download_result_2026-06-21.md",
            "stdrive101_gate_waveform_neutral_wrapper_usb_only_download_execution_entry_2026-06-21.md",
            "stdrive101_gate_waveform_neutral_wrapper_bin_artifact_record_no_power_2026-06-21.md",
            "direct USB-only DMM",
            "later USB-only DMM partial, DMM completion, and residual-voltage isolation\n"
            "  results supersede this download record's live checkpoint",
            "the newest live\n  checkpoint is a separate dated next-stage phase-gate decision",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-RESIDUAL-VOLTAGE-ISOLATION-RESULT-001",
            "stdrive101_gate_waveform_neutral_wrapper_residual_voltage_isolation_result_2026-06-21.md",
            "no 24 V execution",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
        ):
            self.assertIn(phrase, combined)

        self.assertNotIn(
            "The current repo-side checkpoint is complete through the neutral-wrapper\n"
            "USB-only neutral-state phase-gate plan",
            active_task,
        )

    def test_gate_waveform_neutral_wrapper_usbonly_dmm_partial_result_records_reported_rows(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_partial_result_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        record = read_repo_text(artifact)
        combined = (
            record
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only DMM Partial Result - 2026-06-21",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DMM-PARTIAL-RESULT-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-dmm-partial-result",
            "partial user-reported DMM readings",
            "user-reported CN3_1 through CN3_6 all 0 V",
            "P13 = 3.3 V",
            "P14 = 3.3 V",
            "`CN3_1` driver input | `0 V` | reported",
            "`CN3_2 / LIN1` | `0 V` | reported",
            "`CN3_6` driver input | `0 V` | reported",
            "`CN3_13 / nFAULT` | `3.3 V` | reported as `P13`",
            "`CN3_14 / 3V3` | `3.3 V` | reported as `P14`",
            "`VS / 24V_FUSED` | not reported in this partial record",
            "`REG12` | not reported in this partial record",
            "board heat / smell / sound / reset loop | not reported in this partial record",
            "six driver-input stop-rule not hit",
            "driver-input reading was stably above `0.3 V`",
            "no full DMM neutral-state pass",
            "no Run Debug",
            "no 24 V",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
        ):
            self.assertIn(phrase, combined)

        for forbidden in (
            "full DMM neutral-state result is complete",
            "24 V behavior validated",
            "Gate PWM output validated",
            "power-stage readiness validated",
            "motor readiness validated",
            "Hall closed loop validated",
            "sensorless operation validated",
        ):
            self.assertNotIn(forbidden, record)

    def test_gate_waveform_neutral_wrapper_usbonly_dmm_completion_result_records_vs_boundary(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_completion_result_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        record = read_repo_text(artifact)
        combined = (
            record
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only DMM Completion Result - 2026-06-21",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DMM-COMPLETION-RESULT-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-dmm-completion-result",
            "completed user-reported USB-only DMM table",
            "user-reported CN3_1 through CN3_6 all 0 V",
            "P13 = 3.3 V",
            "P14 = 3.3 V",
            "VS / 24V_FUSED = 2 V",
            "REG12 = 0.5 V",
            "board heat / smell / sound / reset loop = none",
            "`VS / 24V_FUSED` | `2 V` | reported; above prior `< 1 V` USB-only boundary",
            "`REG12` | `0.5 V` | reported",
            "six driver-input stop-rule not hit",
            "The voltage-boundary stop condition is active for upward progression",
            "not a pass for upward hardware progression",
            "superseded by the later residual-voltage isolation result",
            "VS / 24V_FUSED = 0 V",
            "REG12 = 0 V",
            "no Run Debug",
            "no 24 V",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
        ):
            self.assertIn(phrase, combined)

        for forbidden in (
            "power-stage readiness validated",
            "motor readiness validated",
            "Hall closed loop validated",
            "sensorless operation validated",
        ):
            self.assertNotIn(forbidden, record)

    def test_gate_waveform_neutral_wrapper_24v_static_no_motor_result_records_clean_static_table_only(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_24v_static_no_motor_result_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        result = read_repo_text(artifact)
        active_task = read_repo_text("workflow/ACTIVE_TASK.md")
        combined = (
            result
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + active_task
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )
        checkpoint = active_task.split("## Next User Checkpoint", 1)[1].split(
            "## Verification", 1
        )[0]

        for phrase in (
            "STDRIVE101 Gate-Waveform Neutral-Wrapper 24V Static No-Motor Result - 2026-06-21",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-24V-STATIC-NO-MOTOR-RESULT-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-24v-static-no-motor-result",
            "bounded 24 V static check",
            "HSPY CV 0.036 A",
            "VS 24V_FUSED = 24 V",
            "CN3_1 through CN3_6 all 0 V",
            "CN3_13 nFAULT = 3.3 V",
            "CN3_14 3V3 = 3.3 V",
            "REG12 = 0.2 V",
            "no board heat smell sound reset-loop reported",
            "six driver-input stop-rule not hit",
            "nFAULT high in static no-motor state",
            "bounded 24 V static no-motor check\n  clean for this table only",
            "superseded for the live checkpoint by the later 24V static scope baseline",
            "Keep HSPY / 24 V OFF and the\n  motor disconnected until then",
            "no Run Debug",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
        ):
            self.assertIn(phrase, combined)

        for forbidden in (
            "Gate PWM output validated",
            "power-stage readiness validated",
            "motor readiness validated",
            "Hall closed loop validated",
            "sensorless operation validated",
        ):
            self.assertNotIn(forbidden, result)

        assert_current_nfault_fault_tree_checkpoint(self, checkpoint)

    def test_gate_waveform_candidate_bin_artifact_record_has_downloadable_identity_only(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_candidate_bin_artifact_record_no_power_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        record = read_repo_text(artifact)
        active_task = read_repo_text("workflow/ACTIVE_TASK.md")
        combined = (
            record
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + active_task
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )
        checkpoint = active_task.split("## Next User Checkpoint", 1)[1].split(
            "## Verification", 1
        )[0]

        for phrase in (
            "STDRIVE101 Gate-Waveform Candidate BIN Artifact Record No-Power - 2026-06-21",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-BIN-ARTIFACT-RECORD-NO-POWER-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-candidate-bin-artifact-record-no-power",
            "stdrive101_gate_waveform_candidate_bin_artifact_record_no_power_2026-06-21.md",
            "Gate E2 waveform candidate linked ELF converted to downloadable BIN",
            "converter output validated against the prior neutral-wrapper objcopy BIN",
            "10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C",
            "170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C",
            "362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31",
            "candidate BIN size 1852 bytes",
            "CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71",
            "Load base | `0x08000000`",
            "Load end | `0x0800073c`",
            "retained MAP symbol\n  gate_waveform_candidate_run_once at 0x080005bc",
            "0x080005bc gate_waveform_candidate_run_once",
            "no forbidden normal-MCSDK\n  MAP symbols found in the checked screen",
            "BIN artifact only",
            "no USB copy",
            "no board image change",
            "no flash",
            "no Run Debug",
            "no 24 V execution",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "waveform-candidate USB-only download execution entry",
            "explicit user confirmation and authorization",
            "HSPY / 24 V is OFF and physically disconnected",
            "motor is disconnected",
        ):
            self.assertIn(phrase, combined)

        for forbidden in (
            "USB copy result",
            "copied once to D:",
            "no FAIL.TXT after copy",
            "Gate PWM output validated",
            "waveform correctness validated",
            "power-stage readiness validated",
            "motor readiness validated",
            "Hall closed loop validated",
            "sensorless operation validated",
        ):
            self.assertNotIn(forbidden, record)

        assert_current_nfault_fault_tree_checkpoint(self, checkpoint)

    def test_gate_waveform_candidate_usb_only_dmm_result_blocks_upward_progression_on_vs_residual(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_candidate_usb_only_dmm_result_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        result = read_repo_text(artifact)
        active_task = read_repo_text("workflow/ACTIVE_TASK.md")
        combined = (
            result
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + active_task
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )
        checkpoint = active_task.split("## Next User Checkpoint", 1)[1].split(
            "## Verification", 1
        )[0]

        for phrase in (
            "STDRIVE101 Gate-Waveform Candidate USB-Only DMM Result - 2026-06-21",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-USBONLY-DMM-RESULT-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-candidate-usbonly-dmm-result",
            "stdrive101_gate_waveform_candidate_usb_only_dmm_result_2026-06-21.md",
            "CN3_1 through CN3_6 all 0 V",
            "CN3_13 = 3 V",
            "CN3_14 = 3 V",
            "VS / 24V_FUSED = 2 V",
            "REG12 = 0.3 V",
            "board heat smell sound reset-loop status not reported in\n  this latest row",
            "six driver-input stop-rule not hit",
            "VS residual-voltage\n  boundary is active",
            "not a pass for upward hardware progression",
            "residual-voltage isolation check only",
            "USB / ST-LINK disconnected",
            "black probe on GND",
            "remeasure only:",
            "Do not repeat the full CN3 table",
            "no Run Debug",
            "no 24 V command",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
        ):
            self.assertIn(phrase, combined)

        assert_current_nfault_fault_tree_checkpoint(self, checkpoint)
        self.assertNotIn("- `VS / 24V_FUSED`;", checkpoint)
        self.assertNotIn("- `REG12`.", checkpoint)

        for forbidden in (
            "24 V behavior validated",
            "Gate PWM output validated",
            "power-stage readiness validated",
            "motor readiness validated",
            "Hall closed loop validated",
            "sensorless operation validated",
        ):
            self.assertNotIn(forbidden, result)

    def test_gate_waveform_candidate_residual_voltage_isolation_result_clears_residual_only(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_candidate_residual_voltage_isolation_result_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        result = read_repo_text(artifact)
        active_task = read_repo_text("workflow/ACTIVE_TASK.md")
        combined = (
            result
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + active_task
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )
        checkpoint = active_task.split("## Next User Checkpoint", 1)[1].split(
            "## Verification", 1
        )[0]

        for phrase in (
            "STDRIVE101 Gate-Waveform Candidate Residual-Voltage Isolation Result - 2026-06-21",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-RESIDUAL-VOLTAGE-ISOLATION-RESULT-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-candidate-residual-voltage-isolation-result",
            "bounded residual-voltage isolation check",
            "USB / ST-LINK disconnected",
            "HSPY / 24 V OFF and physically disconnected",
            "motor disconnected",
            "no `10 kohm` wake resistor or LIN1 stimulus installed",
            "DMM black probe on GND",
            "VS / 24V_FUSED = 0 V",
            "REG12 = 0 V",
            "earlier candidate USB-only VS / 24V_FUSED = 2 V cleared after USB disconnect",
            "persistent VS backfeed not indicated in this candidate isolation check",
            "residual-voltage blocker cleared only",
            "separate candidate 24 V static no-motor phase-gate or execution entry",
            "fresh preconditions",
            "no Run Debug",
            "no 24 V command from this record",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
        ):
            self.assertIn(phrase, combined)

        assert_current_nfault_fault_tree_checkpoint(self, checkpoint)

        for forbidden in (
            "24 V behavior validated",
            "Gate PWM output validated",
            "power-stage readiness validated",
            "motor readiness validated",
            "Hall closed loop validated",
            "sensorless operation validated",
        ):
            self.assertNotIn(forbidden, result)

    def test_gate_waveform_candidate_usb_only_download_entry_opens_one_copy_only(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_candidate_usb_only_download_execution_entry_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        entry = read_repo_text(artifact)
        combined = (
            entry
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/ACTIVE_TASK.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            "STDRIVE101 Gate-Waveform Candidate USB-Only Download Execution Entry - 2026-06-21",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-USBONLY-DOWNLOAD-EXECUTION-ENTRY-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-candidate-usbonly-download-execution-entry",
            "user explicitly authorized copying candidate BIN to D:",
            "362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31",
            "D: volume label NOD_G474RE detected",
            "FAIL.TXT absent before copy",
            "opens exactly one USB-only ST-LINK\n  mass-storage candidate BIN copy",
            "Transfer target",
            "D:\\stdrive101_gate_waveform_candidate_image.bin",
            "USB / ST-LINK mass storage only",
            "Motor Pilot / Motor Profiler not used",
            "candidate image is a `run_once()` image",
            "must not\nclaim that no MCU output transition occurred",
            "no measured\nwaveform validation",
            "no Run Debug",
            "no 24 V command",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "does not contain the copy\nresult",
        ):
            self.assertIn(phrase, combined)

        self.assertNotIn("no FAIL.TXT after copy", entry)
        self.assertNotIn("target BIN not retained on D: after copy", entry)

    def test_gate_waveform_candidate_usb_only_download_result_is_not_measurement_pass(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_candidate_usb_only_download_result_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        result = read_repo_text(artifact)
        active_task = read_repo_text("workflow/ACTIVE_TASK.md")
        combined = (
            result
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + active_task
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )
        checkpoint = active_task.split("## Next User Checkpoint", 1)[1].split(
            "## Verification", 1
        )[0]

        for phrase in (
            "STDRIVE101 Gate-Waveform Candidate USB-Only Download Result - 2026-06-21",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-USBONLY-DOWNLOAD-RESULT-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-candidate-usbonly-download-result",
            "candidate BIN copied once to D: NOD_G474RE by ST-LINK mass storage",
            "source BIN SHA256\n  362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31",
            "no FAIL.TXT before copy",
            "no FAIL.TXT after copy",
            "target BIN not retained\n  on D: after copy",
            "consistent with ST-LINK mass-storage consumption",
            "candidate board image download result only",
            "no CN3 DMM post-download result\n  yet",
            "no measured waveform result yet",
            "board image is now treated as the waveform candidate image",
            "does not prove absence of a boot-time output transition",
            "`gate_waveform_candidate_run_once()` once after reset",
            "Version: V3J17M10",
            "Build:   Oct 17 2025 15:12:06",
            "Copy-Item",
            "Runtime Interpretation Limit",
            "No probe was used in this record",
            "Next USB-Only Measurement Table",
            "`VS / 24V_FUSED`",
            "`CN3_1` driver input",
            "`CN3_2 / LIN1`",
            "`CN3_6` driver input",
            "`CN3_13 / nFAULT`",
            "`CN3_14 / 3V3`",
            "`REG12`",
            "stably above `0.3 V`",
            "superseded by the later waveform candidate residual-voltage isolation result",
            "clears the immediate residual-voltage blocker only",
            "separate candidate 24 V static no-motor phase-gate",
            "no Run Debug",
            "no 24 V command",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
        ):
            self.assertIn(phrase, combined)

        for forbidden in (
            "CN3 state validated",
            "waveform correctness validated",
            "no MCU output transition occurred",
            "power-stage readiness validated",
            "motor readiness validated",
            "Hall closed loop validated",
            "sensorless operation validated",
        ):
            self.assertNotIn(forbidden, result)

        assert_current_nfault_fault_tree_checkpoint(self, checkpoint)

    def test_gate_waveform_neutral_wrapper_24v_static_scope_baseline_result_records_all_six_inputs_only(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_24v_static_scope_baseline_result_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        result = read_repo_text(artifact)
        active_task = read_repo_text("workflow/ACTIVE_TASK.md")
        combined = (
            result
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + active_task
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )
        checkpoint = active_task.split("## Next User Checkpoint", 1)[1].split(
            "## Verification", 1
        )[0]

        for phrase in (
            "STDRIVE101 Gate-Waveform Neutral-Wrapper 24V Static Scope Baseline Result - 2026-06-21",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-24V-STATIC-SCOPE-BASELINE-RESULT-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-24v-static-scope-baseline-result",
            "oscilloscope static baseline on the six STDRIVE101 MCU-facing driver inputs",
            "oscilloscope ground on CN3_15 GND",
            "HSPY CV about 0.036 A",
            "CN3_1 and CN3_2\n  0 V straight lines",
            "CN3_3 and CN3_4 same 0 V straight lines",
            "CN3_5 and\n  CN3_6 same 0 V straight lines",
            "nFAULT remains 3.3 V",
            "no board heat smell\n  sound reset-loop reported",
            "all six MCU-facing driver inputs static-low in\n  this no-motor no-PWM baseline",
            "no waveform output executed",
            "no Run Debug",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
            "Oscilloscope ground | `CN3_15 / GND`",
            "CH1 first pair | `CN3_1`",
            "CH2 first pair | `CN3_2 / LIN1`",
            "CH1 second pair | `CN3_3`",
            "CH2 second pair | `CN3_4`",
            "CH1 third pair | `CN3_5`",
            "CH2 third pair | `CN3_6`",
            "`CN3_1`, `CN3_2 / LIN1`",
            "`CN3_3`, `CN3_4`",
            "`CN3_5`, `CN3_6`",
            "Turn HSPY output OFF after this baseline",
            "separate no-motor, short-window,\ninstrumented waveform execution entry",
            "exact probe points, stop rules, and rollback",
        ):
            self.assertIn(phrase, combined)

        for forbidden in (
            "Gate PWM output validated",
            "waveform correctness validated",
            "power-stage readiness validated",
            "motor readiness validated",
            "Hall closed loop validated",
            "sensorless operation validated",
        ):
            self.assertNotIn(forbidden, result)

        self.assertIn(
            "Superseded for the live checkpoint by `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-BIN-ARTIFACT-RECORD-NO-POWER-001`",
            combined,
        )
        assert_current_nfault_fault_tree_checkpoint(self, checkpoint)

    def test_gate_waveform_neutral_wrapper_residual_voltage_isolation_result_clears_residual_only(self):
        artifact = (
            "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
            "stdrive101_gate_waveform_neutral_wrapper_residual_voltage_isolation_result_2026-06-21.md"
        )
        self.assertTrue((ROOT / artifact).exists())

        result = read_repo_text(artifact)
        active_task = read_repo_text("workflow/ACTIVE_TASK.md")
        combined = (
            result
            + read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + active_task
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )
        checkpoint = active_task.split("## Next User Checkpoint", 1)[1].split(
            "## Verification", 1
        )[0]

        for phrase in (
            "STDRIVE101 Gate-Waveform Neutral-Wrapper Residual-Voltage Isolation Result - 2026-06-21",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-RESIDUAL-VOLTAGE-ISOLATION-RESULT-001",
            "TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-residual-voltage-isolation-result",
            "bounded residual-voltage isolation check",
            "USB / ST-LINK disconnected",
            "HSPY / 24 V OFF and physically disconnected",
            "motor disconnected",
            "no `10 kohm` wake resistor or LIN1 stimulus installed",
            "VS / 24V_FUSED = 0 V",
            "REG12 = 0 V",
            "earlier USB-only VS / 24V_FUSED = 2 V cleared after USB disconnect",
            "persistent VS backfeed not indicated in this isolation check",
            "residual-voltage isolation blocker cleared only",
            "superseded for the live checkpoint by the later 24V static no-motor result",
            "no Run Debug",
            "no 24 V execution",
            "no Gate PWM output",
            "no Motor Pilot",
            "no Motor Profiler",
            "no motor connection",
            "no powered-drive readiness",
        ):
            self.assertIn(phrase, combined)

        assert_current_nfault_fault_tree_checkpoint(self, checkpoint)

        for forbidden in (
            "24 V behavior validated",
            "Gate PWM output validated",
            "power-stage readiness validated",
            "motor readiness validated",
            "Hall closed loop validated",
            "sensorless operation validated",
        ):
            self.assertNotIn(forbidden, result)

    def test_gate_waveform_neutral_wrapper_usbonly_dmm_partial_result_is_superseded_by_later_results(self):
        active_task = read_repo_text("workflow/ACTIVE_TASK.md")
        combined = (
            read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + active_task
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )
        checkpoint = active_task.split("## Next User Checkpoint", 1)[1].split(
            "## Verification", 1
        )[0]

        for phrase in (
            "newest hardware-adjacent record is\n"
            "the STDRIVE101 PA7 LIN1 wake nFAULT 1.3V fault-isolation result",
            "stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_partial_result_2026-06-21.md",
            "EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DMM-PARTIAL-RESULT-001",
            "STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only DMM Partial Result Recorded",
            "`CN3_1` through `CN3_6` are all `0 V`",
            "`P13 = 3.3 V`",
            "`P14 = 3.3 V`",
            "The current repo-side checkpoint is complete through the STDRIVE101 nFAULT 1.3V\n"
            "fault-tree no-power plan",
            "neutral-wrapper 24V static scope baseline",
            "24V static no-motor result",
            "residual-voltage isolation result",
            "candidate USB-only download execution entry",
        ):
            self.assertIn(phrase, combined)

        assert_current_nfault_fault_tree_checkpoint(self, checkpoint)

        for superseded_row in (
            "- `VS / 24V_FUSED`;",
            "- `REG12`.",
            "- `CN3_1`;",
            "- `CN3_2 / LIN1`;",
            "- `CN3_3`;",
            "- `CN3_4`;",
            "- `CN3_5`;",
            "- `CN3_6`;",
            "- `CN3_13 / nFAULT`;",
            "- `CN3_14 / 3V3`;",
        ):
            self.assertNotIn(superseded_row, checkpoint)


class Stdrive101NfaultFaultTreeNoPowerPlanTests(unittest.TestCase):
    ARTIFACT = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "stdrive101_nfault_1v3_fault_tree_no_power_plan_2026-06-22.md"
    )
    EVIDENCE_ID = (
        "EV-2026-06-22-STDRIVE101-NFAULT-1V3-FAULT-TREE-NO-POWER-PLAN-001"
    )
    TASK_ID = "TASK-2026-06-22-stdrive101-nfault-1v3-fault-tree-no-power-plan"
    DECISION = (
        "STDRIVE101 nFAULT 1.3V fault-tree no-power plan / power-board-side "
        "fault localized / no-power source and photo evidence only / HIN1 "
        "comparison remains future teacher-reviewed phase gate / no repeat "
        "powered wake / no PWM output / no motor readiness"
    )

    def test_fault_tree_plan_exists_and_locks_no_power_scope(self):
        self.assertTrue((ROOT / self.ARTIFACT).exists())

        text = read_repo_text(self.ARTIFACT)

        for phrase in (
            "STDRIVE101 nFAULT 1.3V Fault-Tree No-Power Plan - 2026-06-22",
            self.EVIDENCE_ID,
            self.TASK_ID,
            self.DECISION,
            "power-board / STDRIVE101-side `nFAULT = 1.3 V` condition",
            "planning and source-review artifact only",
            "stdrive101_pa7_lin1_wake_nfault_1v3_fault_isolation_result_2026-06-21.md",
            "stdrive101_single_input_wake_nfault_cause_review_2026-06-20.md",
            "stdrive101_fault_review_schematic_marking_2026-06-20.md",
            "stdrive101_protection_nodes_no_power_dmm_result_2026-06-20.md",
            "nFAULT remains 1.3 V on CN8 P13 after PB12 is disconnected",
            "This localizes the latest symptom away from PA7",
            "`LIN1 / GLS1 / Q2 / OUT1` low-side phase-U path",
            "common STDRIVE101 protection / soldering / chip fault",
            "HIN1 comparison idea remains a future teacher-reviewed phase gate",
            "must not be executed from this plan",
            "- flash;",
            "- Run / Debug;",
            "- repeat 24 V wake;",
            "- any `HIN1` comparison execution;",
            "- motor connection;",
            "- Gate PWM output;",
            "- Motor Pilot;",
            "- Motor Profiler;",
            "- Hall closed-loop claim;",
            "- sensorless / SMO claim;",
            "- power-stage readiness;",
            "- motor readiness;",
            "- safe drive operation.",
        ):
            self.assertIn(phrase, text)

        for forbidden in (
            "HIN1 comparison authorized",
            "Gate PWM output validated",
            "power-stage readiness validated",
            "motor readiness validated",
            "Hall closed loop validated",
            "sensorless operation validated",
            "safe drive operation validated",
        ):
            self.assertNotIn(forbidden, text)

    def test_status_register_and_checkpoint_point_to_fault_tree_plan(self):
        active_task = read_repo_text("workflow/ACTIVE_TASK.md")
        checkpoint = active_task.split("## Next User Checkpoint", 1)[1].split(
            "## Verification", 1
        )[0]
        combined = (
            read_repo_text("CURRENT_STATUS.md")
            + read_repo_text("AI_CONTEXT.md")
            + read_repo_text("workflow/CURRENT_SNAPSHOT.md")
            + active_task
            + read_repo_text("workflow/evidence_register.md")
            + read_repo_text(
                "apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md"
            )
        )

        for phrase in (
            self.ARTIFACT,
            self.EVIDENCE_ID,
            self.TASK_ID,
            self.DECISION,
            "STDRIVE101 nFAULT 1.3V Fault-Tree No-Power Plan Added",
            "no-power source and photo evidence only",
            "HIN1 comparison remains future teacher-reviewed phase gate",
            "no repeat powered wake",
            "power-board-side fault localized",
            "`LIN1 / GLS1 / Q2 / OUT1`",
            "common STDRIVE101 protection / CP / SCREF / soldering / chip",
        ):
            self.assertIn(phrase, combined)

        for phrase in (
            "The current repo-side checkpoint is complete through the STDRIVE101 nFAULT 1.3V\n"
            "fault-tree no-power plan",
            "Board photo or EDA crop showing U1 STDRIVE101",
            "Confirm HSPY OFF, VS / 24V_FUSED near 0 V, motor disconnected",
            "Q2 gate-source = ___",
            "OUT1 / Q2 drain to Q2 source diode mode = ___",
            "nFAULT to 3V3 = ___",
            "nFAULT to GND = ___",
            "Do not repeat residual-voltage isolation",
            "the `LIN1` powered wake",
            "or any\n`HIN1` comparison unless",
            "separate dated teacher-\nreviewed phase gate opens the action",
        ):
            self.assertIn(phrase, checkpoint)

        for forbidden in (
            "HIN1 comparison authorized",
            "24 V behavior validated",
            "Gate PWM output validated",
            "power-stage readiness validated",
            "motor readiness validated",
            "Hall closed loop validated",
            "sensorless operation validated",
        ):
            self.assertNotIn(forbidden, combined)


if __name__ == "__main__":
    unittest.main()
