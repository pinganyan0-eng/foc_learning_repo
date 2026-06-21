import json
import unittest
from pathlib import Path

from src.foc_core_model import (
    CurrentLoopGains,
    CurrentLoopInputs,
    CurrentLoopState,
    PIConfig,
    PIState,
    clarke_abc,
    current_control_step,
    inverse_park,
    park,
    pi_step,
    svpwm,
)


ROOT = Path(__file__).resolve().parents[1]
VECTOR_PATH = ROOT / "tests" / "fixtures" / "foc_core_golden_vectors.json"


def _assert_close(testcase, actual, expected, places=12):
    testcase.assertAlmostEqual(actual, expected, places=places)


def _assert_dict_close(testcase, actual, expected, places=12):
    for key, expected_value in expected.items():
        actual_value = actual[key]
        if isinstance(expected_value, bool):
            testcase.assertEqual(actual_value, expected_value)
        else:
            _assert_close(testcase, actual_value, expected_value, places)


def _svpwm_dict(result):
    return {
        "a": result.duty.a,
        "b": result.duty.b,
        "c": result.duty.c,
        "saturated": result.saturated,
        "scale": result.scale,
    }


def _pi_config(data):
    return PIConfig(
        kp=data["kp"],
        ki=data["ki"],
        output_limit=data["output_limit"],
        integrator_limit=data.get("integrator_limit"),
    )


def _loop_gains(data):
    return CurrentLoopGains(d_axis=_pi_config(data["d"]), q_axis=_pi_config(data["q"]))


def _loop_inputs(data):
    return CurrentLoopInputs(
        i_a=data["i_a"],
        i_b=data["i_b"],
        i_c=data["i_c"],
        theta_e_rad=data["theta_e_rad"],
        target_id=data["target_id"],
        target_iq=data["target_iq"],
        vbus=data["vbus"],
        dt_s=data["dt_s"],
    )


def _loop_result_dict(result):
    return {
        "current_ab": {
            "alpha": result.current_ab.alpha,
            "beta": result.current_ab.beta,
        },
        "current_dq": {
            "d": result.current_dq.d,
            "q": result.current_dq.q,
        },
        "voltage_dq": {
            "d": result.voltage_dq.d,
            "q": result.voltage_dq.q,
        },
        "voltage_ab": {
            "alpha": result.voltage_ab.alpha,
            "beta": result.voltage_ab.beta,
        },
        "svpwm": _svpwm_dict(result.svpwm),
        "state": {
            "d_integrator": result.state.d_axis.integrator,
            "q_integrator": result.state.q_axis.integrator,
        },
    }


class FocCoreGoldenVectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vectors = json.loads(VECTOR_PATH.read_text(encoding="utf-8"))

    def test_metadata_keeps_no_power_boundary(self):
        metadata = self.vectors["metadata"]

        self.assertEqual(
            metadata["decision"],
            "Host-side no-power FOC golden vectors / no firmware implementation / no MCSDK integration / no PWM output / no motor readiness",
        )
        self.assertEqual(
            metadata["scope"],
            "host-side no-power FOC math regression fixture only",
        )
        self.assertIn("firmware implementation", metadata["not_evidence_for"])
        self.assertIn("MCSDK hook readiness", metadata["not_evidence_for"])
        self.assertIn("compare-register values", metadata["not_evidence_for"])
        self.assertIn("Gate PWM output validation", metadata["not_evidence_for"])
        self.assertIn("motor readiness", metadata["not_evidence_for"])
        self.assertIn("not proof that MCSDK generated code", metadata["assumption_note"])

    def test_transform_vectors_replay_against_reference_model(self):
        for case in self.vectors["transform_cases"]:
            with self.subTest(case=case["name"]):
                input_data = case["input"]

                if "clarke" in case:
                    result = clarke_abc(
                        input_data["i_a"],
                        input_data["i_b"],
                        input_data["i_c"],
                    )
                    _assert_dict_close(
                        self,
                        {"alpha": result.alpha, "beta": result.beta},
                        case["clarke"],
                    )

                if "park" in case:
                    park_result = park(
                        input_data["alpha"],
                        input_data["beta"],
                        input_data["theta_e_rad"],
                    )
                    _assert_dict_close(
                        self,
                        {"d": park_result.d, "q": park_result.q},
                        case["park"],
                    )

                    inverse = inverse_park(
                        park_result.d,
                        park_result.q,
                        input_data["theta_e_rad"],
                    )
                    _assert_dict_close(
                        self,
                        {"alpha": inverse.alpha, "beta": inverse.beta},
                        case["inverse_park"],
                    )

    def test_svpwm_vectors_replay_against_reference_model(self):
        for case in self.vectors["svpwm_cases"]:
            with self.subTest(case=case["name"]):
                input_data = case["input"]
                result = svpwm(
                    input_data["alpha"],
                    input_data["beta"],
                    input_data["vbus"],
                )

                _assert_dict_close(self, _svpwm_dict(result), case["expected"])

    def test_pi_vectors_replay_against_reference_model(self):
        for case in self.vectors["pi_cases"]:
            with self.subTest(case=case["name"]):
                input_data = case["input"]
                result = pi_step(
                    error=input_data["error"],
                    dt_s=input_data["dt_s"],
                    state=PIState(integrator=input_data["state_integrator"]),
                    config=_pi_config(input_data),
                )

                _assert_dict_close(
                    self,
                    {
                        "output": result.output,
                        "integrator": result.state.integrator,
                        "saturated": result.saturated,
                    },
                    case["expected"],
                )

    def test_current_loop_vectors_replay_against_reference_model(self):
        for case in self.vectors["current_loop_cases"]:
            with self.subTest(case=case["name"]):
                result = current_control_step(
                    _loop_inputs(case["inputs"]),
                    _loop_gains(case["gains"]),
                    CurrentLoopState(),
                )
                actual = _loop_result_dict(result)

                for section, expected in case["expected"].items():
                    _assert_dict_close(self, actual[section], expected)

    def test_current_loop_sequence_vectors_replay_against_reference_model(self):
        for case in self.vectors["current_loop_sequence_cases"]:
            with self.subTest(case=case["name"]):
                state = CurrentLoopState()

                for expected in case["steps"]:
                    result = current_control_step(
                        _loop_inputs(case["inputs"]),
                        _loop_gains(case["gains"]),
                        state,
                    )
                    state = result.state
                    actual = _loop_result_dict(result)

                    for section in ("voltage_dq", "state", "svpwm"):
                        _assert_dict_close(self, actual[section], expected[section])


if __name__ == "__main__":
    unittest.main()
