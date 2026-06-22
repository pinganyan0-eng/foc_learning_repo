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
MC_MATH = SNAPSHOT / "Src" / "mc_math.c"
MC_TASKS_FOC = SNAPSHOT / "Src" / "mc_tasks_foc.c"
MC_CONFIG = SNAPSHOT / "Src" / "mc_config.c"
PWM_CURR_FDBK = SNAPSHOT / "Src" / "pwm_curr_fdbk.c"
MC_TYPE = SNAPSHOT / "Inc" / "mc_type.h"
DRIVE_PARAMETERS = SNAPSHOT / "Inc" / "drive_parameters.h"
PARAMETERS_CONVERSION = SNAPSHOT / "Inc" / "parameters_conversion.h"
PROBE_REVIEW = (
    ROOT
    / "apps"
    / "stm32_g474_foc"
    / "mcsdk_no_power_precheck"
    / "mcsdk_foc_convention_probe_translation_table_2026-06-22.md"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class McsdkFocConventionProbeTests(unittest.TestCase):
    def test_archived_sources_contain_expected_convention_clues(self):
        math_text = _read(MC_MATH)
        tasks_text = _read(MC_TASKS_FOC)
        config_text = _read(MC_CONFIG)
        pwm_text = _read(PWM_CURR_FDBK)
        type_text = _read(MC_TYPE)
        drive_text = _read(DRIVE_PARAMETERS)
        conversion_text = _read(PARAMETERS_CONVERSION)

        for phrase in (
            "Output.alpha = Input.a;",
            "Output.q = hqd_tmp;",
            "Output.d = hqd_tmp;",
            "__weak qd_t MCM_Park(alphabeta_t Input, int16_t Theta)",
            "__weak alphabeta_t MCM_Rev_Park(qd_t Input, int16_t Theta)",
        ):
            self.assertIn(phrase, math_text)

        for phrase in (
            "Vqd.q = PI_Controller",
            "Iqdref.q) - Iqd.q",
            "Vqd.d = PI_Controller",
            "Iqdref.d) - Iqd.d",
            "Circle_Limitation(&CircleLimitationM1, Vqd)",
        ):
            self.assertIn(phrase, tasks_text)

        for phrase in (
            "int16_t q;",
            "int16_t d;",
            "alphabeta_t Ialphabeta",
            "qd_t Iqd",
            "qd_t Iqdref",
            "qd_t Vqd",
            "alphabeta_t Valphabeta",
        ):
            self.assertIn(phrase, type_text)

        for phrase in (
            ".MaxModule = MAX_MODULE",
            ".MaxVd     = (uint16_t)((MAX_MODULE * 950) / 1000)",
            ".CntPhA                     = 0,",
            ".CntPhB                     = 0,",
            ".CntPhC                     = 0,",
            ".PWMperiod                  = PWM_PERIOD_CYCLES,",
        ):
            self.assertIn(phrase, config_text)

        for phrase in (
            "wUAlpha = Valfa_beta.alpha * (int32_t)pHandle->hT_Sqrt3;",
            "wUBeta = -(Valfa_beta.beta * ((int32_t)pHandle->PWMperiod)) * 2;",
            "pHandle->CntPhA = (uint16_t)(MAX(wTimePhA, 0));",
            "pHandle->CntPhB = (uint16_t)(MAX(wTimePhB, 0));",
            "pHandle->CntPhC = (uint16_t)(MAX(wTimePhC, 0));",
            "SECTOR_1",
            "SECTOR_6",
        ):
            self.assertIn(phrase, pwm_text)

        for phrase in (
            "#define PID_TORQUE_KP_DEFAULT               2071",
            "#define PID_FLUX_KP_DEFAULT                 2071",
            "#define TF_KPDIV                            128",
            "#define TF_KIDIV                            4096",
        ):
            self.assertIn(phrase, drive_text)

        for phrase in (
            "#define PWM_PERIOD_CYCLES",
            "#define MAX_MODULE",
        ):
            self.assertIn(phrase, conversion_text)

    def test_convention_probe_review_locks_translation_rows_and_boundaries(self):
        review = _read(PROBE_REVIEW)

        for phrase in (
            "MCSDK FOC Convention Probe Translation Table - 2026-06-22",
            "MCSDK FOC convention probe / translation table / host-side no-power generated-source convention mapping only / no firmware implementation / no generated-code edit / no MCSDK integration / no PWM output / no motor readiness",
            "This artifact is the next no-power increment after the host-side FOC model,",
            "MCSDK remains the intended motor-control framework generation path",
            "MCSDK `qd_t` stores fields as `q` then `d`",
            "Host `clarke_abc`",
            "MCSDK `MCM_Clarke`: `Output.alpha = Input.a;`",
            "Host `DQ(d, q)` dataclass",
            "MCSDK `MCM_Park` writes `Output.q` before `Output.d`",
            "Host `svpwm` returns duty floats in `[0,1]`",
            "MCSDK uses `PID_TORQUE_*`, `PID_FLUX_*`, `TF_KPDIV`, `TF_KIDIV`",
            "MCSDK `PWMC_SetPhaseVoltage` computes sector plus `CntPhA`, `CntPhB`, `CntPhC` timer counts",
            "not MCSDK convention proof beyond explicitly source-backed rows",
            "not host-side / MCSDK numerical equivalence evidence",
            "not compare-register evidence",
            "not Gate PWM validation",
            "not MCSDK hook readiness",
            "not hardware validation",
            "No 24V.",
            "No Gate PWM output.",
            "No motor readiness claim.",
        ):
            self.assertIn(phrase, review)


if __name__ == "__main__":
    unittest.main()
