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
IOC = SNAPSHOT / "QIANSAI_G474_STDRIVE101_FOC_P2.ioc"
MC_CONFIG = SNAPSHOT / "Src" / "mc_config.c"
MC_TASKS_FOC = SNAPSHOT / "Src" / "mc_tasks_foc.c"
MC_MATH_H = SNAPSHOT / "Inc" / "mc_math.h"
MC_STM_TYPES = SNAPSHOT / "Inc" / "mc_stm_types.h"
REGISTER_INTERFACE = SNAPSHOT / "Inc" / "register_interface.h"
STWB6 = (
    ROOT
    / "apps"
    / "stm32_g474_foc"
    / "mcsdk_no_power_precheck"
    / "packet_a_sources"
    / "2026-05-16_custom_nucleo_stdrive101"
    / "QIANSAI_G474_STDRIVE101_FOC_P2_2026-05-21.stwb6"
)
REVIEW = (
    ROOT
    / "apps"
    / "stm32_g474_foc"
    / "mcsdk_no_power_precheck"
    / "mcsdk_sensorless_observer_generated_source_boundary_review_2026-06-22.md"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class McsdkSensorlessObserverBoundaryStaticTests(unittest.TestCase):
    def test_archived_generated_source_uses_hall_speed_sensor_not_sto_instance(self):
        ioc_text = _read(IOC)
        config_text = _read(MC_CONFIG)
        tasks_text = _read(MC_TASKS_FOC)

        for phrase in (
            "MotorControl.HALL_SENSORS=true",
            "MotorControl.M1_SPEED_SENSOR=HALL_SENSOR",
            "MotorControl.SPEED_SENSOR_SELECTION=HALL_SENSORS",
            "Mcu.IP2=CORDIC",
        ):
            self.assertIn(phrase, ioc_text)

        for phrase in (
            "SpeedNPosition sensor parameters Motor 1 - HALL.",
            "HALL_Handle_t HALL_M1 =",
            ".SensorPlacement             = HALL_SENSORS_PLACEMENT,",
            ".TIMx                        = TIM2,",
        ):
            self.assertIn(phrase, config_text)

        for phrase in (
            "HALL_Init (&HALL_M1);",
            "STC_Init(pSTC[M1],&PIDSpeedHandle_M1, &HALL_M1._Super);",
            "(void)HALL_CalcAvrgMecSpeedUnit(&HALL_M1, &wAux);",
            "(void)HALL_CalcElAngle(&HALL_M1);",
            "speedHandle = STC_GetSpeedSensor(pSTC[M1]);",
            "hElAngle = SPD_GetElAngle(speedHandle);",
        ):
            self.assertIn(phrase, tasks_text)

        for forbidden in (
            "MotorControl.M1_SPEED_SENSOR=STO_PLL",
            "MotorControl.M1_SPEED_SENSOR=STO_CORDIC",
            "MotorControl.SPEED_SENSOR_SELECTION=SENSORLESS",
        ):
            self.assertNotIn(forbidden, ioc_text)

    def test_generic_observer_symbols_do_not_imply_active_sensorless_sources(self):
        source_names = {path.name.lower() for path in (SNAPSHOT / "Src").iterdir()}
        include_names = {path.name.lower() for path in (SNAPSHOT / "Inc").iterdir()}

        self.assertIn("hall_speed_pos_fdbk.c", source_names)
        self.assertIn("hall_speed_pos_fdbk.h", include_names)

        for absent_file in (
            "sto_pll_speed_pos_fdbk.c",
            "sto_pll_speed_pos_fdbk.h",
            "sto_cordic_speed_pos_fdbk.c",
            "sto_cordic_speed_pos_fdbk.h",
            "revup_ctrl.c",
            "revup_ctrl.h",
            "virtual_speed_sensor.c",
            "virtual_speed_sensor.h",
        ):
            self.assertNotIn(absent_file, source_names | include_names)

        math_text = _read(MC_MATH_H)
        register_text = _read(REGISTER_INTERFACE)
        stm_types_text = _read(MC_STM_TYPES)

        for phrase in (
            "CORDIC_CONFIG_PHASE",
            "MCM_PhaseComputation",
            "rotor position extraction from B-emf alpha and beta",
        ):
            self.assertIn(phrase, math_text)

        for phrase in (
            "MC_REG_STOPLL_EL_ANGLE",
            "MC_REG_STOCORDIC_EL_ANGLE",
            "MC_REG_STOPLL_BEMF_ALPHA",
            "MC_REG_STOCORDIC_BEMF_ALPHA",
        ):
            self.assertIn(phrase, register_text)

        for phrase in (
            "FULL_MISRA_C_COMPLIANCY_STO_CORDIC",
            "FULL_MISRA_C_COMPLIANCY_STO_PLL",
            "NULL_PTR_CHECK_STO_COR_SPD_POS_FDB",
            "NULL_PTR_CHECK_STO_PLL_SPD_POS_FDB",
        ):
            self.assertIn(phrase, stm_types_text)

    def test_workbench_revup_flag_does_not_override_generated_hall_boundary(self):
        stwb_text = _read(STWB6)
        ioc_text = _read(IOC)

        self.assertIn('"revupToFocSwitchOverEnabled": true', stwb_text)
        self.assertIn("MotorControl.M1_SPEED_SENSOR=HALL_SENSOR", ioc_text)
        self.assertIn("MotorControl.SPEED_SENSOR_SELECTION=HALL_SENSORS", ioc_text)
        self.assertNotIn("MotorControl.M1_SPEED_SENSOR=STO_PLL", ioc_text)

    def test_review_records_source_boundary_without_sensorless_claim(self):
        review = _read(REVIEW)

        for phrase in (
            "MCSDK Sensorless Observer Generated-Source Boundary Review",
            "MCSDK sensorless observer generated-source boundary / Hall generated-source boundary confirmed / generic CORDIC and STO register symbols noted / no active MCSDK observer instance / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness",
            "QIANSAI_G474_STDRIVE101_FOC_P2.ioc",
            "MotorControl.M1_SPEED_SENSOR=HALL_SENSOR",
            "MotorControl.SPEED_SENSOR_SELECTION=HALL_SENSORS",
            "HALL_Init (&HALL_M1);",
            "STC_Init(pSTC[M1],&PIDSpeedHandle_M1, &HALL_M1._Super);",
            "MCM_PhaseComputation",
            "MC_REG_STOPLL_EL_ANGLE",
            "MC_REG_STOCORDIC_EL_ANGLE",
            "revupToFocSwitchOverEnabled",
            "no active MCSDK observer instance",
            "not MCSDK Observer PLL equivalence",
            "not MCSDK Observer CORDIC equivalence",
            "not SMO implementation or validation",
            "No 24 V",
            "No Gate PWM output",
            "No sensorless / SMO claim",
        ):
            self.assertIn(phrase, review)

        for forbidden in (
            "sensorless operation validated",
            "SMO validation passed",
            "MCSDK observer equivalence proved",
            "Gate PWM output validated",
            "motor readiness validated",
        ):
            self.assertNotIn(forbidden, review)


if __name__ == "__main__":
    unittest.main()
