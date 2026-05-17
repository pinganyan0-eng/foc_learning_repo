import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_repo_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class P2EvidenceContractTests(unittest.TestCase):
    INTAKE = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "source_packet_intake_checklist_2026-05-14.md"
    )
    REQUEST = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "source_packet_request_pack_2026-05-14.md"
    )
    USER_ACTION = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "user_action_queue_2026-05-14.md"
    )
    REVIEW_TEMPLATE = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "source_packet_review_template_2026-05-14.md"
    )
    EVIDENCE_PACKET = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "evidence_packet_2026-05-14.md"
    )
    SCHEMATIC_CANDIDATE_NOTE = (
        "hardware/schematic/"
        "2026-05-15_power_board_cn8_stdrive101_schematic_candidate.md"
    )
    SCHEMATIC_CANDIDATE_REVIEW = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "source_packet_review_2026-05-15_001_cn8_stdrive101_schematic_candidate.md"
    )
    NON_HARDWARE_TRACK = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "non_hardware_parallel_track_2026-05-15.md"
    )
    PACKET_A_LOCAL_PROBE = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "packet_a_local_probe_2026-05-15.md"
    )
    PACKET_A_CAPTURE_CHECKLIST = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "packet_a_capture_checklist_2026-05-15.md"
    )
    STM32_SIGNAL_CONTRACT = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "stm32_side_signal_contract_2026-05-15.md"
    )
    FUTURE_BUILD_ONLY_GATE = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "future_build_only_gate_2026-05-15.md"
    )
    P2_READINESS_SNAPSHOT = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "p2_readiness_snapshot_2026-05-15.md"
    )
    PACKET_A_STWB6_SOURCE = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6"
    )
    PACKET_A_STWB6_NOTE = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "packet_a_sources/2026-05-15_my_first_foc/README.md"
    )
    PACKET_A_STWB6_REVIEW = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "source_packet_review_2026-05-15_002_my_first_foc_stwb6.md"
    )
    PACKET_A_CUSTOM_README = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "packet_a_sources/2026-05-16_custom_nucleo_stdrive101/README.md"
    )
    PACKET_A_CUSTOM_GUIDE = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "packet_a_sources/2026-05-16_custom_nucleo_stdrive101/"
        "workbench_no_power_configuration_guide_2026-05-16.md"
    )
    PACKET_A_CUSTOM_MOTOR_LOG = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "packet_a_sources/2026-05-16_custom_nucleo_stdrive101/"
        "motor_no_power_measurement_log_2026-05-16.md"
    )
    PACKET_A_CUSTOM_PIN_TABLE = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "packet_a_sources/2026-05-16_custom_nucleo_stdrive101/"
        "pin_assignment_table_2026-05-16.md"
    )
    PACKET_A_CUSTOM_REVIEW = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md"
    )
    VENDOR_MOTOR_IMAGE = "hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.jpg"
    VENDOR_MOTOR_NOTE = "hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.md"
    HW_PIN_TABLE_PDF = (
        "hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.pdf"
    )
    HW_PIN_TABLE_NOTE = (
        "hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.md"
    )
    MCU_PIN_COMPATIBILITY_CHECK = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "mcu_pin_compatibility_check_2026-05-17.md"
    )
    VENDOR_MOTOR_PIN_REVIEW = (
        "apps/stm32_g474_foc/mcsdk_no_power_precheck/"
        "source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md"
    )
    PHASE_GATE = "workflow/phase_gate_checklist.md"

    def test_source_packet_intake_defines_accepted_and_rejected_sources(self):
        text = read_repo_text(self.INTAKE)

        for phrase in (
            "Accepted Source Packets",
            "MCSDK / MotorControl Configuration Packet",
            "CN8 / Board Route Packet",
            "STDRIVE101 Protection Path Packet",
            "Rejected Source Types",
            "low-resolution screenshots",
            "oral descriptions",
            "old, draft, or unknown-version",
            "netlist_PADS.net",
        ):
            self.assertIn(phrase, text)

    def test_source_packet_intake_keeps_no_power_boundary(self):
        text = read_repo_text(self.INTAKE)

        for phrase in (
            "No 24V",
            "No power-board connection",
            "No motor connection",
            "No Gate PWM output",
            "No Motor Profiler run",
            "No Hall closed-loop claim",
            "No sensorless / SMO claim",
        ):
            self.assertIn(phrase, text)

    def test_source_packet_request_pack_defines_next_handoff(self):
        text = read_repo_text(self.REQUEST)

        for phrase in (
            "Packet A - MCSDK / MotorControl Configuration",
            "Packet B - CN8 / Board Route Evidence",
            "Packet C - STDRIVE101 Protection Path Evidence",
            "source_packet_intake_checklist_2026-05-14.md",
            "Current Blocking State",
            "No 24V",
            "No Gate PWM output",
            "No Motor Profiler run",
            "netlist_PADS.net",
            "does not add any",
            "new board evidence",
        ):
            self.assertIn(phrase, text)

    def test_user_action_queue_tells_user_exactly_what_to_provide(self):
        text = read_repo_text(self.USER_ACTION)

        for phrase in (
            "你现在要做的事",
            "Task 1 - 先交 Packet B",
            "当前版板级走线源包",
            "Task 2 - 交 Packet A",
            "MCSDK / MotorControl 配置源包",
            "Task 3 - 补 PB3 / SWO 释放证据",
            "你发给 Codex 的最短模板",
            "source_packet_intake_checklist_2026-05-14.md",
            "No 24V",
            "No Gate PWM output",
            "No Motor Profiler run",
            "netlist_PADS.net",
            "仍不授权任何上电或电机动作",
        ):
            self.assertIn(phrase, text)

    def test_source_packet_review_template_requires_accept_partial_or_reject(self):
        text = read_repo_text(self.REVIEW_TEMPLATE)

        for phrase in (
            "P2 Source Packet Review Template",
            "Accept / Partial clue / Reject",
            "Packet A - MCSDK / MotorControl Configuration Review",
            "Packet B - CN8 / Board Route Review",
            "Packet C - STDRIVE101 Protection Path Review",
            "PB3 / SWO Release Review",
            "Required Output After Review",
            "Forbidden Conclusions",
            "source_packet_intake_checklist_2026-05-14.md",
            "user_action_queue_2026-05-14.md",
            "No 24V",
            "No Gate PWM output",
            "No Motor Profiler run",
            "netlist_PADS.net",
            "Do not upgrade evidence",
        ):
            self.assertIn(phrase, text)

    def test_evidence_packet_links_missing_items_to_intake(self):
        text = read_repo_text(self.EVIDENCE_PACKET)

        for phrase in (
            "source_packet_intake_checklist_2026-05-14.md",
            "user_action_queue_2026-05-14.md",
            "source_packet_review_template_2026-05-14.md",
            "下一步证据入口",
            "MCSDK / MotorControl Configuration Packet",
            "CN8 / Board Route Packet",
            "STDRIVE101 Protection Path Packet",
            "Blocked",
            "My_First_FOC.stwb6",
            "Partial clue",
            "仍没有 current-version EDA",
            "仍只有官方器件要求和缺证矩阵",
            "netlist_PADS.net",
        ):
            self.assertIn(phrase, text)

    def test_packet_a_stwb6_candidate_is_preserved_as_partial_clue(self):
        source_path = ROOT / self.PACKET_A_STWB6_SOURCE
        self.assertTrue(source_path.exists())

        data = json.loads(source_path.read_text(encoding="utf-8"))
        self.assertEqual(data["algorithm"], "FOC")
        self.assertEqual(data["workBenchVersion"], "6.4.2")
        self.assertEqual(data["hardwares"]["control"]["id"], "NUCLEO-G474RE")
        self.assertEqual(data["hardwares"]["control"]["mcu"]["id"], "STM32G474RETx")
        self.assertEqual(data["hardwares"]["power"][0]["id"], "EVALSTDRIVE101")

        note = read_repo_text(self.PACKET_A_STWB6_NOTE)
        review = read_repo_text(self.PACKET_A_STWB6_REVIEW)

        for phrase in (
            "Packet A Source Candidate",
            "My_First_FOC.stwb6",
            "STMCWB.exe",
            "6.4.2",
            "Partial clue",
            "does not authorize generated-project trust",
        ):
            self.assertIn(phrase, note + review)

        for phrase in (
            "P2-SOURCE-REVIEW-2026-05-15-002",
            "MCSDK 6 stores Workbench projects as `.stwb6`",
            "Partial clue",
            "NUCLEO-G474RE",
            "STM32G474RETx",
            "EVALSTDRIVE101",
            "generated-project trust",
            "Not allowed",
        ):
            self.assertIn(phrase, review)

    def test_packet_a_custom_capture_package_is_preparation_only(self):
        texts = [
            read_repo_text(self.PACKET_A_CUSTOM_README),
            read_repo_text(self.PACKET_A_CUSTOM_GUIDE),
            read_repo_text(self.PACKET_A_CUSTOM_MOTOR_LOG),
            read_repo_text(self.PACKET_A_CUSTOM_PIN_TABLE),
            read_repo_text(self.PACKET_A_CUSTOM_REVIEW),
        ]
        combined = "\n".join(texts)

        for phrase in (
            "Packet A Capture Package",
            "NUCLEO-G474RE",
            "STM32G474RETx",
            "Custom / Generic STDRIVE101",
            "Do not select `EVALSTDRIVE101`",
            "57BLF01_VENDOR_CANDIDATE",
            "supplier clue",
            "Hall as the main speed feedback",
            "3-shunt",
            "No generated source",
            "No Motor Profiler",
            "Pin Assignment Table",
            "source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md",
            "mcu_pin_compatibility_check_2026-05-17.md",
            "PB3 / TIM2_CH2",
            "PB3.Signal=SYS_JTDO-SWO",
            "Partial clue / Preparation only",
            "Generated-project trust remains `Not allowed`",
        ):
            self.assertIn(phrase, combined)

        for path in (
            self.PACKET_A_CUSTOM_README,
            self.PACKET_A_CUSTOM_GUIDE,
            self.PACKET_A_CUSTOM_MOTOR_LOG,
            self.PACKET_A_CUSTOM_PIN_TABLE,
            self.PACKET_A_CUSTOM_REVIEW,
        ):
            self.assertTrue((ROOT / path).exists())

    def test_vendor_motor_and_g431_pin_table_remain_partial_clues(self):
        for path in (
            self.VENDOR_MOTOR_IMAGE,
            self.VENDOR_MOTOR_NOTE,
            self.HW_PIN_TABLE_PDF,
            self.HW_PIN_TABLE_NOTE,
            self.MCU_PIN_COMPATIBILITY_CHECK,
            self.VENDOR_MOTOR_PIN_REVIEW,
        ):
            self.assertTrue((ROOT / path).exists())

        combined = "\n".join(
            read_repo_text(path)
            for path in (
                self.VENDOR_MOTOR_NOTE,
                self.HW_PIN_TABLE_NOTE,
                self.MCU_PIN_COMPATIBILITY_CHECK,
                self.VENDOR_MOTOR_PIN_REVIEW,
                self.PACKET_A_CAPTURE_CHECKLIST,
                self.P2_READINESS_SNAPSHOT,
            )
        )

        for phrase in (
            "P2-SOURCE-REVIEW-2026-05-17-001",
            "57BLF01",
            "57BLF01_VENDOR_CANDIDATE",
            "supplier clue",
            "Physical measurement by project | No",
            "Motor Profiler result | No",
            "STM32G431RB",
            "STM32G431RBTx",
            "STM32G474RETx",
            "LQFP64",
            "TIM1_CH1N",
            "TIM2_CH2",
            "SYS_JTDO-SWO",
            "J_HALL",
            "PB3",
            "OPAMP2",
            "Partial clue",
            "Not allowed",
            "does not prove CN8",
            "does not confirm CN8 routing",
            "does not release SWO",
            "not measured",
        ):
            self.assertIn(phrase, combined)

        for phrase in (
            "Motor Profiler data exists",
            "the motor has been tested or is ready to run",
            "CN8 routing is accepted",
            "build-only, flash, power, Gate PWM, or motor actions are allowed",
        ):
            self.assertIn(phrase, combined)

    def test_schematic_candidate_is_preserved_as_partial_clue_only(self):
        note = read_repo_text(self.SCHEMATIC_CANDIDATE_NOTE)
        review = read_repo_text(self.SCHEMATIC_CANDIDATE_REVIEW)

        self.assertTrue(
            (ROOT / "hardware/schematic/2026-05-15_power_board_cn8_stdrive101_schematic_candidate.png").exists()
        )

        for phrase in (
            "Partial clue",
            "CN8",
            "STDRIVE101",
            "硬件同学自绘",
            "current physical power board",
            "STM32",
            "DT/MODE",
            "STBY",
            "不能升级为 accepted board-route proof",
        ):
            self.assertIn(phrase, note)

        for phrase in (
            "P2-SOURCE-REVIEW-2026-05-15-001",
            "Partial clue",
            "Packet B blocker status: still `Blocked`",
            "Packet C blocker status: still `Blocked`",
            "current physical power board",
            "hardware teammate",
            "Formal source date/version",
            "STM32 / NUCLEO-side CN8-to-MCU pin mapping",
            "does not upgrade CN8 routing proof",
        ):
            self.assertIn(phrase, review)

    def test_status_and_submission_register_intake_without_upgrading_blockers(self):
        current_status = read_repo_text("CURRENT_STATUS.md")
        submission = read_repo_text("deliverables/submission_checklist.md")
        register = read_repo_text("workflow/evidence_register.md")
        sprint = read_repo_text("workflow/current_learning_sprint.md")

        for text in (current_status, submission, register, sprint):
            self.assertIn("source_packet_intake_checklist_2026-05-14.md", text)
            self.assertIn("source_packet_request_pack_2026-05-14.md", text)
            self.assertIn("user_action_queue_2026-05-14.md", text)
            self.assertIn("source_packet_review_template_2026-05-14.md", text)

        self.assertIn("does not prove MCSDK MotorControl", current_status)
        self.assertIn("does not authorize 24V", current_status)
        self.assertIn("still missing", submission)
        self.assertIn("not usable to claim", register)
        self.assertIn("Packet B", submission)
        self.assertIn("Partial clue", register)
        self.assertIn("2026-05-15_power_board_cn8_stdrive101_schematic_candidate", register)
        self.assertIn("non_hardware_parallel_track_2026-05-15.md", register)
        self.assertIn("p2_readiness_snapshot_2026-05-15.md", current_status)
        self.assertIn("p2_readiness_snapshot_2026-05-15.md", submission)
        self.assertIn("p2_readiness_snapshot_2026-05-15.md", register)
        self.assertIn("p2_readiness_snapshot_2026-05-15.md", sprint)
        self.assertIn("2026-05-16_custom_nucleo_stdrive101", current_status)
        self.assertIn("2026-05-16_custom_nucleo_stdrive101", submission)
        self.assertIn("2026-05-16_custom_nucleo_stdrive101", register)
        self.assertIn("2026-05-16_custom_nucleo_stdrive101", sprint)
        self.assertIn(
            "source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md",
            current_status + submission + register + sprint,
        )
        self.assertIn(
            "source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md",
            current_status + submission + register + sprint,
        )
        self.assertIn(
            "mcu_pin_compatibility_check_2026-05-17.md",
            current_status + submission + register + sprint,
        )
        self.assertIn("57BLF01_VENDOR_CANDIDATE", current_status + submission + register + sprint)
        self.assertIn("G431/G474", current_status + submission + register + sprint)
        self.assertIn("J_HALL", current_status + submission + register + sprint)

    def test_non_hardware_parallel_track_skips_but_does_not_clear_hardware(self):
        text = read_repo_text(self.NON_HARDWARE_TRACK)

        for phrase in (
            "P2 Non-Hardware Parallel Track",
            "Skipped, Not Cleared",
            "Allowed Parallel Work",
            "Packet A - MCSDK / MotorControl evidence",
            "STM32-side signal contract",
            "Future Generated-Project Gate",
            "does not close Packet B",
            "No 24V",
            "No Gate PWM output",
            "No Motor Profiler run",
            "cannot claim CN8 routing proof",
            "cannot claim",
                "sensorless readiness",
        ):
            self.assertIn(phrase, text)

    def test_packet_a_local_probe_keeps_configuration_partial(self):
        probe = read_repo_text(self.PACKET_A_LOCAL_PROBE)
        checklist = read_repo_text(self.PACKET_A_CAPTURE_CHECKLIST)

        for phrase in (
            "Packet A Local Probe",
            "No 24V",
            "No Gate PWM output",
            "No Motor Profiler run",
            "apps/stm32_g474_foc/MotorControl",
            "contains only tracked `.gitkeep`",
            "STMCWB.exe",
            "My_First_FOC.stwb6",
            "Partial clue",
            "No MotorControl / Workbench configuration screenshot",
        ):
            self.assertIn(phrase, probe)

        for phrase in (
            "Packet A Capture Checklist",
            "Real Workbench project file: `.stwb6`",
            "legacy `.stmcx`",
            "MotorControl / Workbench configuration screenshot",
            "Exact reproducible GUI launcher path",
            "Generated MCSDK source without the matching Workbench project file",
            "57BLF01_VENDOR_CANDIDATE",
            "supplier-clue label",
            "G431/G474 pins are the same",
            "does not confirm CN8 routing",
            "`PB3` ownership",
            "No Motor Profiler run",
            "Partial clue",
        ):
            self.assertIn(phrase, checklist)

    def test_signal_contract_and_build_gate_keep_no_power_scope(self):
        contract = read_repo_text(self.STM32_SIGNAL_CONTRACT)
        gate = read_repo_text(self.FUTURE_BUILD_ONLY_GATE)

        for phrase in (
            "STM32-Side Signal Contract",
            "No 24V",
            "No Gate PWM output",
            "TIM1 PWM command outputs",
            "`NFAULT`",
            "`STBY`",
            "`DT/MODE`",
            "`PB3` cannot be claimed for Hall B while SWO owns it",
            "ESP32 does not own FOC timing",
            "It does not prove CN8 routing",
            "It does not prove STDRIVE101 protection-path implementation",
        ):
            self.assertIn(phrase, contract)

        for phrase in (
            "Future Build-Only Gate",
            "No 24V",
            "No Gate PWM output",
            "No flash or board run",
            "`Not allowed`",
            "Current state because Packet A is only `Partial clue`",
            "Allowed Build-Only Actions",
            "Forbidden Actions In This Gate",
            "cannot claim Gate PWM behavior is safe",
                "Build success",
        ):
            self.assertIn(phrase, gate)

    def test_p2_readiness_snapshot_keeps_generated_project_blocked(self):
        text = read_repo_text(self.P2_READINESS_SNAPSHOT)

        for phrase in (
            "P2 Readiness Snapshot",
            "P2 remains in progress",
            "Packet A MCSDK / MotorControl evidence",
            "Partial clue",
            "`Not allowed` because Packet A is only `Partial clue / Preparation only`",
            "2026-05-16 custom NUCLEO + STDRIVE101",
            "2026-05-17 vendor motor / G431 pin-table",
            "57BLF01_VENDOR_CANDIDATE",
            "mcu_pin_compatibility_check_2026-05-17.md",
            "Hardware action is not a P2 state",
            "No 24V",
            "No Gate PWM output",
            "No flash or board run",
            "Generated-project trust",
            "Not allowed",
            "Packet B CN8 / board-route proof",
            "Partial clue",
            "Packet C STDRIVE101 protection proof",
            "PB3 Hall B readiness",
            "`PB3.Signal=SYS_JTDO-SWO`",
            "J_HALL",
            "vendor motor parameters are measured project data",
            "Allowed current claims",
            "Forbidden current claims",
            "Before moving from current P2 planning to build-only generated-project work",
            "Before moving from P2 to any powered or motor stage",
            "P2 cannot currently",
        ):
            self.assertIn(phrase, text)

    def test_phase_gate_requires_p2_no_power_before_profiler_or_build(self):
        text = read_repo_text(self.PHASE_GATE)

        for phrase in (
            "2026-05-15 P2 No-Power Gate Insert",
            "not allowed to jump from NUCLEO basics directly to Motor Profiler",
            "P2-S1 - MCSDK No-Power Precheck",
            "p2_readiness_snapshot_2026-05-15.md",
            "source_packet_intake_checklist_2026-05-14.md",
            "Passing this gate does not authorize generated-project trust",
            "P2-S2 - Build-Only Generated Project Gate",
            "Packet A is accepted",
            "future_build_only_gate_2026-05-15.md",
            "Do not claim CN8 routing proof",
            "Do not flash or run the generated project",
            "P2 To P3 Blocker List",
            "Accepted Packet A",
            "Accepted Packet B",
            "Accepted Packet C",
            "PB3/SWO release or isolation evidence",
            "current-limited bring-up settings",
            "explicitly opens the powered action",
        ):
            self.assertIn(phrase, text)

    def test_p2_documents_do_not_make_positive_power_or_motor_claims(self):
        p2_doc_dir = ROOT / "apps/stm32_g474_foc/mcsdk_no_power_precheck"
        p2_paths = tuple(
            str(path.relative_to(ROOT)) for path in p2_doc_dir.glob("*.md")
        ) + (
            "deliverables/submission_checklist.md",
            "workflow/evidence_register.md",
            "CURRENT_STATUS.md",
        )
        unsafe_patterns = (
            r"可以接\s*24V",
            r"允许接\s*24V",
            r"允许\s*24V\s*上电",
            r"24V\s*已通过",
            r"Gate PWM\s*已验证",
            r"Motor Profiler\s*已运行",
            r"Hall 闭环\s*已验证",
            r"SMO\s*已验证",
            r"无感控制\s*已验证",
            r"功率板\s*已验证",
            r"电机\s*已验证",
            r"Motor Profiler\s+is ready to run",
            r"Gate PWM behavior",
            r"behavior is validated",
        )
        negative_context = (
            "不",
            "No ",
            "no ",
            "not ",
            "cannot",
            "blocked",
            "Blocked",
            "forbidden",
            "禁止",
            "缺失",
            "仍没有",
            "不可",
        )

        for relative_path in p2_paths:
            text = read_repo_text(relative_path)
            for lineno, line in enumerate(text.splitlines(), start=1):
                for pattern in unsafe_patterns:
                    if re.search(pattern, line):
                        with self.subTest(relative_path=relative_path, lineno=lineno):
                            self.assertTrue(
                                any(marker in line for marker in negative_context),
                                f"Unsafe positive P2 claim at {relative_path}:{lineno}: {line}",
                            )


if __name__ == "__main__":
    unittest.main()
