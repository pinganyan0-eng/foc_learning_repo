import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = (
    ROOT
    / "apps"
    / "stm32_g474_foc"
    / "mcsdk_no_power_precheck"
    / "packet_a_sources"
    / "2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot"
)
MC_TASKS_FOC = SNAPSHOT / "Src" / "mc_tasks_foc.c"
MC_MATH = SNAPSHOT / "Src" / "mc_math.c"
MC_CONFIG = SNAPSHOT / "Src" / "mc_config.c"
MC_TYPE = SNAPSHOT / "Inc" / "mc_type.h"
BRIDGE_REVIEW = (
    ROOT
    / "apps"
    / "stm32_g474_foc"
    / "mcsdk_no_power_precheck"
    / "mcsdk_host_side_foc_math_comparison_boundary_plan_2026-06-22.md"
)


def _read(path):
    return path.read_text(encoding="utf-8")


def _assert_order(testcase, text, phrases):
    cursor = -1
    for phrase in phrases:
        index = text.find(phrase, cursor + 1)
        testcase.assertNotEqual(index, -1, f"missing or out-of-order: {phrase}")
        cursor = index


class McsdkFocPipelineStaticTests(unittest.TestCase):
    def test_archived_generated_source_contains_foc_current_loop_pipeline(self):
        text = _read(MC_TASKS_FOC)

        _assert_order(
            self,
            text,
            (
                "PWMC_GetPhaseCurrents",
                "MCM_Clarke",
                "MCM_Park",
                "PI_Controller",
                "Circle_Limitation",
                "MCM_Rev_Park",
                "PWMC_SetPhaseVoltage",
            ),
        )
        self.assertIn("FOC_CurrControllerM1", text)
        self.assertIn("PWMC_GetPWMState", text)

    def test_archived_generated_sources_expose_math_and_state_clues(self):
        math_text = _read(MC_MATH)
        config_text = _read(MC_CONFIG)
        type_text = _read(MC_TYPE)

        for phrase in (
            "alphabeta_t MCM_Clarke",
            "qd_t MCM_Park",
            "alphabeta_t MCM_Rev_Park",
        ):
            self.assertIn(phrase, math_text)

        for phrase in (
            "PIDIqHandle_M1",
            "PIDIdHandle_M1",
            "CircleLimitationM1",
            "FOCVars",
        ):
            self.assertIn(phrase, config_text)

        for phrase in (
            "typedef struct",
            "int16_t q;",
            "int16_t d;",
            "alphabeta_t Ialphabeta",
            "qd_t Iqd",
            "alphabeta_t Valphabeta",
        ):
            self.assertIn(phrase, type_text)

    def test_boundary_plan_keeps_mcsdk_and_host_side_boundaries(self):
        review = _read(BRIDGE_REVIEW)

        for phrase in (
            "MCSDK / Host-Side FOC Math Comparison Boundary Plan",
            "MCSDK host-side FOC math comparison boundary plan / no firmware implementation / no MCSDK integration / no PWM output / no motor readiness",
            "MCSDK remains the intended motor-control framework generation path",
            "read-only generated-source pipeline bridge",
            "PWMC_GetPhaseCurrents -> MCM_Clarke -> MCM_Park -> PI_Controller -> Circle_Limitation -> MCM_Rev_Park -> PWMC_SetPhaseVoltage",
            "compare only sign, scaling, saturation, duty representation, and naming assumptions",
            "not proof that MCSDK generated code matches the Python model",
            "does not modify generated MCSDK source",
            "not compare-register evidence",
            "not Gate PWM validation",
            "No 24V",
            "No Gate PWM output",
            "No Hall closed-loop claim",
            "No motor connection",
        ):
            self.assertIn(phrase, review)


if __name__ == "__main__":
    unittest.main()
