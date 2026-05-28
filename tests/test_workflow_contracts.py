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


if __name__ == "__main__":
    unittest.main()
