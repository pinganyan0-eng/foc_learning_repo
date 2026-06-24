import json
import unittest
from pathlib import Path

from src.foc_core_model import CurrentLoopGains, CurrentLoopState, PIConfig, PIState
from src.foc_sensorless_frontend import (
    SensorlessCurrentCommandPolicyConfig,
    SensorlessCurrentLoopInputs,
    SensorlessFrontendConfig,
    SensorlessFrontendInputs,
    SensorlessFrontendState,
    SensorlessObserverConfig,
    SensorlessObserverState,
    SensorlessSpeedLoopConfig,
    SensorlessSpeedLoopState,
    SensorlessStartupPolicyConfig,
    SensorlessStartupPolicyState,
    back_emf_observer_step,
    sensorless_current_control_step,
    sensorless_current_control_replay_sequence,
    sensorless_frontend_step,
)


ROOT = Path(__file__).resolve().parents[1]
VECTOR_PATH = ROOT / "tests" / "fixtures" / "foc_sensorless_frontend_vectors.json"


def _config(data):
    return SensorlessFrontendConfig(**data)


def _state(data):
    return SensorlessFrontendState(**data)


def _frontend_inputs(data):
    return SensorlessFrontendInputs(**data)


def _loop_inputs(data):
    return SensorlessCurrentLoopInputs(**data)


def _loop_gains(data):
    return CurrentLoopGains(
        d_axis=PIConfig(**data["d"]),
        q_axis=PIConfig(**data["q"]),
    )


def _observer_config(data):
    return SensorlessObserverConfig(**data)


def _observer_state(data):
    return SensorlessObserverState(**data)


def _startup_policy_config(data):
    return SensorlessStartupPolicyConfig(**data)


def _startup_policy_state(data):
    return SensorlessStartupPolicyState(**data)


def _speed_loop_config(data):
    return SensorlessSpeedLoopConfig(
        speed_pi=PIConfig(**data["speed_pi"]),
        target_omega_rate_limit_e_rad_s2=data.get(
            "target_omega_rate_limit_e_rad_s2"
        ),
        hold_when_unlocked=data.get("hold_when_unlocked", False),
    )


def _speed_loop_state(data):
    return SensorlessSpeedLoopState(
        speed_pi=PIState(**data["speed_pi"]),
        target_omega_e_rad_s=data["target_omega_e_rad_s"],
    )


def _current_command_policy_config(data):
    return SensorlessCurrentCommandPolicyConfig(**data)


class SensorlessFrontendGoldenVectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vectors = json.loads(VECTOR_PATH.read_text(encoding="utf-8"))

    def test_metadata_keeps_no_power_boundary(self):
        metadata = self.vectors["metadata"]

        self.assertEqual(
            metadata["decision"],
            "Host-side no-power reverse target-omega lock-threshold handoff / startup-unlocked threshold fixture only / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness",
        )
        self.assertEqual(
            metadata["scope"],
            "host-side no-power sensorless frontend, replay, startup policy, speed-loop hold, signed reverse speed/current command, signed reverse target-omega rate-limit replay, reverse target-omega startup hold, reverse target-omega lock-threshold handoff, positive-to-reverse target-omega crossing replay, current-command policy, and locked-theta shortest-path blend fixture only",
        )
        self.assertIn("firmware implementation", metadata["not_evidence_for"])
        self.assertIn("MCSDK integration", metadata["not_evidence_for"])
        self.assertIn("sensorless / SMO validation", metadata["not_evidence_for"])
        self.assertIn("firmware speed loop", metadata["not_evidence_for"])
        self.assertIn("firmware current limiting strategy", metadata["not_evidence_for"])
        self.assertIn("theta_e_rad producer", metadata["assumption_note"])
        self.assertIn("locked-theta shortest-path wrap blending", metadata["assumption_note"])
        self.assertIn("back-EMF observer stub", metadata["assumption_note"])
        self.assertIn("multi-step state-continuity replay", metadata["assumption_note"])
        self.assertIn("startup policy lock/loss hysteresis", metadata["assumption_note"])
        self.assertIn("lock-aware speed-loop PI hold", metadata["assumption_note"])
        self.assertIn("lock-aware speed/current command gating", metadata["assumption_note"])
        self.assertIn("signed reverse target speed/current command replay", metadata["assumption_note"])
        self.assertIn("signed reverse target-omega rate-limit replay", metadata["assumption_note"])
        self.assertIn("reverse target-omega startup hold", metadata["assumption_note"])
        self.assertIn("reverse target-omega lock-threshold handoff", metadata["assumption_note"])
        self.assertIn("not a reverse open-loop startup strategy", metadata["assumption_note"])
        self.assertIn("positive-to-reverse target-omega crossing replay", metadata["assumption_note"])
        self.assertIn("MCSDK observer equivalence proof", metadata["not_evidence_for"])
        self.assertIn("firmware startup state machine", metadata["not_evidence_for"])

    def test_frontend_cases_replay_against_reference_model(self):
        for case in self.vectors["frontend_cases"]:
            with self.subTest(case=case["name"]):
                result = sensorless_frontend_step(
                    _frontend_inputs(case["inputs"]),
                    _state(case["state"]),
                    _config(case["config"]),
                )
                expected = case["expected"]

                self.assertAlmostEqual(result.theta_e_rad, expected["theta_e_rad"], places=12)
                self.assertAlmostEqual(result.omega_e_rad_s, expected["omega_e_rad_s"], places=12)
                self.assertEqual(result.mode, expected["mode"])
                self.assertEqual(result.locked, expected["locked"])
                self.assertAlmostEqual(result.confidence, expected["confidence"], places=12)

    def test_observer_stub_cases_replay_against_reference_model(self):
        for case in self.vectors["observer_stub_cases"]:
            with self.subTest(case=case["name"]):
                result = back_emf_observer_step(
                    _frontend_inputs(case["inputs"]),
                    _observer_state(case["state"]),
                    _observer_config(case["config"]),
                )
                expected = case["expected"]

                self.assertAlmostEqual(result.theta_e_rad, expected["theta_e_rad"], places=12)
                self.assertAlmostEqual(result.omega_e_rad_s, expected["omega_e_rad_s"], places=12)
                self.assertAlmostEqual(result.confidence, expected["confidence"], places=12)
                self.assertAlmostEqual(result.back_emf_ab.alpha, expected["back_emf_ab"]["alpha"], places=12)
                self.assertAlmostEqual(result.back_emf_ab.beta, expected["back_emf_ab"]["beta"], places=12)
                self.assertAlmostEqual(result.back_emf_magnitude, expected["back_emf_magnitude"], places=12)

    def test_sensorless_current_loop_cases_replay_against_reference_model(self):
        for case in self.vectors["sensorless_current_loop_cases"]:
            with self.subTest(case=case["name"]):
                observer_config = (
                    None
                    if case.get("observer_config") is None
                    else _observer_config(case["observer_config"])
                )
                observer_state = (
                    None
                    if case.get("observer_state") is None
                    else _observer_state(case["observer_state"])
                )
                result = sensorless_current_control_step(
                    _loop_inputs(case["inputs"]),
                    _state(case["sensorless_state"]),
                    _config(case["config"]),
                    _loop_gains(case["gains"]),
                    CurrentLoopState(),
                    observer_config,
                    observer_state,
                )
                expected = case["expected"]

                if "observer" in expected:
                    self.assertIsNotNone(result.observer)
                    assert result.observer is not None
                    self.assertAlmostEqual(result.observer.theta_e_rad, expected["observer"]["theta_e_rad"], places=12)
                    self.assertAlmostEqual(result.observer.omega_e_rad_s, expected["observer"]["omega_e_rad_s"], places=12)
                    self.assertAlmostEqual(result.observer.confidence, expected["observer"]["confidence"], places=12)
                    self.assertAlmostEqual(result.observer.back_emf_ab.alpha, expected["observer"]["back_emf_ab"]["alpha"], places=12)
                    self.assertAlmostEqual(result.observer.back_emf_ab.beta, expected["observer"]["back_emf_ab"]["beta"], places=12)
                    self.assertAlmostEqual(result.observer.back_emf_magnitude, expected["observer"]["back_emf_magnitude"], places=12)

                self.assertAlmostEqual(result.sensorless.theta_e_rad, expected["sensorless"]["theta_e_rad"], places=12)
                self.assertAlmostEqual(result.sensorless.omega_e_rad_s, expected["sensorless"]["omega_e_rad_s"], places=12)
                self.assertEqual(result.sensorless.mode, expected["sensorless"]["mode"])
                self.assertEqual(result.sensorless.locked, expected["sensorless"]["locked"])
                self.assertAlmostEqual(result.current_loop.current_dq.d, expected["current_loop"]["current_dq"]["d"], places=12)
                self.assertAlmostEqual(result.current_loop.current_dq.q, expected["current_loop"]["current_dq"]["q"], places=12)
                if "voltage_dq" in expected["current_loop"]:
                    self.assertAlmostEqual(result.current_loop.voltage_dq.d, expected["current_loop"]["voltage_dq"]["d"], places=12)
                    self.assertAlmostEqual(result.current_loop.voltage_dq.q, expected["current_loop"]["voltage_dq"]["q"], places=12)
                self.assertAlmostEqual(result.current_loop.svpwm.duty.a, expected["current_loop"]["svpwm"]["a"], places=12)
                self.assertAlmostEqual(result.current_loop.svpwm.duty.b, expected["current_loop"]["svpwm"]["b"], places=12)
                self.assertAlmostEqual(result.current_loop.svpwm.duty.c, expected["current_loop"]["svpwm"]["c"], places=12)
                self.assertEqual(result.current_loop.svpwm.saturated, expected["current_loop"]["svpwm"]["saturated"])

    def test_sensorless_replay_sequences_replay_against_reference_model(self):
        for case in self.vectors["sensorless_replay_sequences"]:
            with self.subTest(case=case["name"]):
                observer_config = (
                    None
                    if case.get("observer_config") is None
                    else _observer_config(case["observer_config"])
                )
                observer_state = (
                    None
                    if case.get("observer_state") is None
                    else _observer_state(case["observer_state"])
                )
                result = sensorless_current_control_replay_sequence(
                    [_loop_inputs(step) for step in case["inputs"]],
                    _state(case["sensorless_state"]),
                    _config(case["config"]),
                    _loop_gains(case["gains"]),
                    CurrentLoopState(),
                    observer_config,
                    observer_state,
                )
                expected = case["expected"]

                self.assertEqual(len(result.steps), len(expected["steps"]))
                for index, (actual_step, expected_step) in enumerate(
                    zip(result.steps, expected["steps"], strict=True)
                ):
                    with self.subTest(case=case["name"], step=index):
                        self.assertAlmostEqual(
                            actual_step.sensorless.theta_e_rad,
                            expected_step["sensorless"]["theta_e_rad"],
                            places=12,
                        )
                        self.assertAlmostEqual(
                            actual_step.sensorless.omega_e_rad_s,
                            expected_step["sensorless"]["omega_e_rad_s"],
                            places=12,
                        )
                        self.assertEqual(
                            actual_step.sensorless.mode,
                            expected_step["sensorless"]["mode"],
                        )
                        self.assertEqual(
                            actual_step.sensorless.locked,
                            expected_step["sensorless"]["locked"],
                        )
                        if "observer" in expected_step:
                            self.assertIsNotNone(actual_step.observer)
                            assert actual_step.observer is not None
                            self.assertAlmostEqual(
                                actual_step.observer.theta_e_rad,
                                expected_step["observer"]["theta_e_rad"],
                                places=12,
                            )
                            self.assertAlmostEqual(
                                actual_step.observer.omega_e_rad_s,
                                expected_step["observer"]["omega_e_rad_s"],
                                places=12,
                            )
                            self.assertAlmostEqual(
                                actual_step.observer.confidence,
                                expected_step["observer"]["confidence"],
                                places=12,
                            )
                        self.assertAlmostEqual(
                            actual_step.current_loop_state.q_axis.integrator,
                            expected_step["current_loop_state"]["q_axis_integrator"],
                            places=12,
                        )

                self.assertAlmostEqual(
                    result.state.theta_e_rad,
                    expected["final_state"]["theta_e_rad"],
                    places=12,
                )
                self.assertAlmostEqual(
                    result.current_loop_state.q_axis.integrator,
                    expected["final_current_loop_state"]["q_axis_integrator"],
                    places=12,
                )
                if "final_observer_state" in expected:
                    self.assertIsNotNone(result.observer_state)
                    assert result.observer_state is not None
                    self.assertAlmostEqual(
                        result.observer_state.theta_e_rad,
                        expected["final_observer_state"]["theta_e_rad"],
                        places=12,
                    )
                    self.assertAlmostEqual(
                        result.observer_state.confidence,
                        expected["final_observer_state"]["confidence"],
                        places=12,
                    )

    def test_sensorless_startup_policy_sequences_replay_against_reference_model(self):
        for case in self.vectors["sensorless_startup_policy_sequences"]:
            with self.subTest(case=case["name"]):
                result = sensorless_current_control_replay_sequence(
                    [_loop_inputs(step) for step in case["inputs"]],
                    _state(case["sensorless_state"]),
                    _config(case["config"]),
                    _loop_gains(case["gains"]),
                    CurrentLoopState(),
                    startup_policy_config=_startup_policy_config(
                        case["startup_policy_config"]
                    ),
                    startup_policy_state=_startup_policy_state(
                        case["startup_policy_state"]
                    ),
                )
                expected = case["expected"]

                self.assertEqual(len(result.steps), len(expected["steps"]))
                for index, (actual_step, expected_step) in enumerate(
                    zip(result.steps, expected["steps"], strict=True)
                ):
                    with self.subTest(case=case["name"], step=index):
                        self.assertIsNotNone(actual_step.startup_policy)
                        assert actual_step.startup_policy is not None
                        self.assertAlmostEqual(
                            actual_step.sensorless.theta_e_rad,
                            expected_step["sensorless"]["theta_e_rad"],
                            places=12,
                        )
                        self.assertAlmostEqual(
                            actual_step.sensorless.omega_e_rad_s,
                            expected_step["sensorless"]["omega_e_rad_s"],
                            places=12,
                        )
                        self.assertEqual(
                            actual_step.sensorless.mode,
                            expected_step["sensorless"]["mode"],
                        )
                        self.assertEqual(
                            actual_step.sensorless.locked,
                            expected_step["sensorless"]["locked"],
                        )
                        self.assertEqual(
                            actual_step.startup_policy.tracking_enabled,
                            expected_step["startup_policy"]["tracking_enabled"],
                        )
                        self.assertEqual(
                            actual_step.startup_policy.lock_candidate,
                            expected_step["startup_policy"]["lock_candidate"],
                        )
                        self.assertEqual(
                            actual_step.startup_policy.loss_candidate,
                            expected_step["startup_policy"]["loss_candidate"],
                        )
                        self.assertEqual(
                            actual_step.startup_policy.lock_candidate_count,
                            expected_step["startup_policy"]["lock_candidate_count"],
                        )
                        self.assertEqual(
                            actual_step.startup_policy.loss_candidate_count,
                            expected_step["startup_policy"]["loss_candidate_count"],
                        )
                        self.assertEqual(
                            actual_step.startup_policy.frontend_lock_override,
                            expected_step["startup_policy"]["frontend_lock_override"],
                        )
                        self.assertAlmostEqual(
                            actual_step.current_loop_state.q_axis.integrator,
                            expected_step["current_loop_state"]["q_axis_integrator"],
                            places=12,
                        )

                self.assertAlmostEqual(
                    result.state.theta_e_rad,
                    expected["final_state"]["theta_e_rad"],
                    places=12,
                )
                self.assertEqual(result.state.mode, expected["final_state"]["mode"])
                self.assertEqual(result.state.locked, expected["final_state"]["locked"])
                self.assertAlmostEqual(
                    result.current_loop_state.q_axis.integrator,
                    expected["final_current_loop_state"]["q_axis_integrator"],
                    places=12,
                )
                self.assertIsNotNone(result.startup_policy_state)
                assert result.startup_policy_state is not None
                self.assertEqual(
                    result.startup_policy_state.tracking_enabled,
                    expected["final_startup_policy_state"]["tracking_enabled"],
                )
                self.assertEqual(
                    result.startup_policy_state.lock_candidate_count,
                    expected["final_startup_policy_state"]["lock_candidate_count"],
                )
                self.assertEqual(
                    result.startup_policy_state.loss_candidate_count,
                    expected["final_startup_policy_state"]["loss_candidate_count"],
                )

    def test_sensorless_speed_command_policy_sequences_replay_against_reference_model(self):
        for case in self.vectors["sensorless_speed_command_policy_sequences"]:
            with self.subTest(case=case["name"]):
                result = sensorless_current_control_replay_sequence(
                    [_loop_inputs(step) for step in case["inputs"]],
                    _state(case["sensorless_state"]),
                    _config(case["config"]),
                    _loop_gains(case["gains"]),
                    CurrentLoopState(),
                    startup_policy_config=_startup_policy_config(
                        case["startup_policy_config"]
                    ),
                    startup_policy_state=_startup_policy_state(
                        case["startup_policy_state"]
                    ),
                    speed_loop_config=_speed_loop_config(case["speed_loop_config"]),
                    speed_loop_state=_speed_loop_state(case["speed_loop_state"]),
                    current_command_policy_config=_current_command_policy_config(
                        case["current_command_policy_config"]
                    ),
                )
                expected = case["expected"]

                self.assertEqual(len(result.steps), len(expected["effective_target_iq"]))
                for index, actual_step in enumerate(result.steps):
                    with self.subTest(case=case["name"], step=index):
                        self.assertIsNotNone(actual_step.speed_loop)
                        self.assertIsNotNone(actual_step.current_command_policy)
                        assert actual_step.speed_loop is not None
                        assert actual_step.current_command_policy is not None
                        self.assertAlmostEqual(
                            actual_step.speed_loop.target_iq,
                            expected["speed_loop_target_iq"][index],
                            places=12,
                        )
                        if "speed_loop_target_omega" in expected:
                            self.assertAlmostEqual(
                                actual_step.speed_loop.target_omega_e_rad_s,
                                expected["speed_loop_target_omega"][index],
                                places=12,
                            )
                        if "speed_loop_pi_integrator" in expected:
                            self.assertAlmostEqual(
                                actual_step.speed_loop.state.speed_pi.integrator,
                                expected["speed_loop_pi_integrator"][index],
                                places=12,
                            )
                        self.assertAlmostEqual(
                            actual_step.current_command_policy.effective_target_iq,
                            expected["effective_target_iq"][index],
                            places=12,
                        )
                        self.assertEqual(
                            actual_step.current_command_policy.reason,
                            expected["command_reasons"][index],
                        )
                        if "locked" in expected:
                            self.assertEqual(
                                actual_step.sensorless.locked,
                                expected["locked"][index],
                            )
                        if "loss_candidate_count" in expected:
                            self.assertIsNotNone(actual_step.startup_policy)
                            assert actual_step.startup_policy is not None
                            self.assertEqual(
                                actual_step.startup_policy.loss_candidate_count,
                                expected["loss_candidate_count"][index],
                            )
                        if "lock_candidate_count" in expected:
                            self.assertIsNotNone(actual_step.startup_policy)
                            assert actual_step.startup_policy is not None
                            self.assertEqual(
                                actual_step.startup_policy.lock_candidate_count,
                                expected["lock_candidate_count"][index],
                            )
                        self.assertAlmostEqual(
                            actual_step.current_loop_state.q_axis.integrator,
                            expected["q_axis_integrator"][index],
                            places=12,
                        )

                self.assertIsNotNone(result.speed_loop_state)
                assert result.speed_loop_state is not None
                self.assertAlmostEqual(
                    result.speed_loop_state.target_omega_e_rad_s,
                    expected["final_speed_loop_state"]["target_omega_e_rad_s"],
                    places=12,
                )
                self.assertAlmostEqual(
                    result.speed_loop_state.speed_pi.integrator,
                    expected["final_speed_loop_state"]["speed_pi_integrator"],
                    places=12,
                )


if __name__ == "__main__":
    unittest.main()
