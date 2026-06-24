import json
import unittest
from pathlib import Path

from src.foc_core_model import (
    CurrentLoopGains,
    CurrentLoopInputs,
    CurrentLoopState,
    DQ,
    PIConfig,
    PIState,
    current_control_step,
)
from src.foc_mcsdk_bridge import (
    current_loop_result_to_mcsdk_state,
    dq_to_mcsdk_qd,
    duty_to_counts,
    radians_to_q15,
    sensorless_replay_to_mcsdk_observer_snapshots,
    sensorless_replay_to_mcsdk_speed_command_snapshots,
    sensorless_result_to_mcsdk_observer_snapshot,
    sensorless_result_to_mcsdk_speed_command_snapshot,
    speed_command_to_mcsdk_snapshot,
)
from src.foc_sensorless_frontend import (
    SensorlessCurrentCommandPolicyConfig,
    SensorlessCurrentLoopInputs,
    SensorlessFrontendConfig,
    SensorlessFrontendState,
    SensorlessObserverConfig,
    SensorlessObserverState,
    SensorlessSpeedLoopConfig,
    SensorlessSpeedLoopState,
    SensorlessStartupPolicyConfig,
    SensorlessStartupPolicyState,
    sensorless_current_control_replay_sequence,
)


ROOT = Path(__file__).resolve().parents[1]
VECTOR_PATH = ROOT / "tests" / "fixtures" / "foc_mcsdk_bridge_vectors.json"


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


def _sensorless_frontend_config(data):
    return SensorlessFrontendConfig(
        startup_accel_e_rad_s2=data["startup_accel_e_rad_s2"],
        startup_target_omega_e_rad_s=data["startup_target_omega_e_rad_s"],
        lock_blend_factor=data["lock_blend_factor"],
        observer_min_confidence_for_lock=data.get("observer_min_confidence_for_lock", 0.8),
        observer_max_angle_step_rad=data.get("observer_max_angle_step_rad", 1.5707963267948966),
    )


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


class McsdkFocBridgeVectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vectors = json.loads(VECTOR_PATH.read_text(encoding="utf-8"))

    def test_metadata_keeps_translation_only_boundary(self):
        metadata = self.vectors["metadata"]

        self.assertEqual(
            metadata["decision"],
            "MCSDK host-side FOC and sensorless comparison bridge / host-side no-power semantic translation only / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no PWM output / no motor readiness",
        )
        self.assertEqual(
            metadata["scope"],
            "host-side no-power comparison bridge fixture only",
        )
        self.assertIn("MCSDK convention proof", metadata["not_evidence_for"])
        self.assertIn("MCSDK observer equivalence", metadata["not_evidence_for"])
        self.assertIn("host-side / MCSDK numerical equivalence evidence", metadata["not_evidence_for"])
        self.assertIn("compare-register evidence", metadata["not_evidence_for"])
        self.assertIn("Gate PWM output validation", metadata["not_evidence_for"])
        self.assertIn("comparison-ready translation rules", metadata["assumption_note"])
        self.assertIn("sensorless observer-output snapshots", metadata["assumption_note"])
        self.assertIn("lock-aware speed/current command snapshots", metadata["assumption_note"])
        self.assertIn("signed reverse speed/current command snapshots", metadata["assumption_note"])
        self.assertIn(
            "signed reverse target-omega rate-limit command-ramp snapshots",
            metadata["assumption_note"],
        )
        self.assertIn(
            "positive-to-reverse target-omega crossing snapshots",
            metadata["assumption_note"],
        )
        self.assertIn(
            "positive-to-reverse target-omega loss/relock speed/current snapshots",
            metadata["assumption_note"],
        )
        self.assertIn(
            "reverse target-omega lock-threshold handoff snapshots",
            metadata["assumption_note"],
        )

    def test_angle_vectors_replay_against_bridge(self):
        for case in self.vectors["angle_cases"]:
            with self.subTest(case=case["name"]):
                self.assertEqual(
                    radians_to_q15(case["theta_e_rad"]),
                    case["expected_theta_q15"],
                )

    def test_qd_vectors_replay_against_bridge(self):
        for case in self.vectors["qd_cases"]:
            with self.subTest(case=case["name"]):
                actual = dq_to_mcsdk_qd(DQ(**case["host_dq"]))
                self.assertEqual(actual.q, case["expected_qd"]["q"])
                self.assertEqual(actual.d, case["expected_qd"]["d"])

    def test_qd_mapping_clamps_out_of_range_values(self):
        actual = dq_to_mcsdk_qd(DQ(d=2.0, q=-2.0))

        self.assertEqual(actual.q, -32768)
        self.assertEqual(actual.d, 32767)

    def test_duty_count_vectors_replay_against_bridge(self):
        from src.foc_core_model import PhaseDuty, SVPWMResult

        for case in self.vectors["duty_count_cases"]:
            with self.subTest(case=case["name"]):
                host = case["host_svpwm"]
                result = SVPWMResult(
                    duty=PhaseDuty(a=host["a"], b=host["b"], c=host["c"]),
                    saturated=host["saturated"],
                    scale=host["scale"],
                )
                counts = duty_to_counts(result, case["pwm_period_cycles"])
                self.assertEqual(counts.a, case["expected_counts"]["a"])
                self.assertEqual(counts.b, case["expected_counts"]["b"])
                self.assertEqual(counts.c, case["expected_counts"]["c"])

    def test_current_loop_bridge_vectors_replay_against_reference_model(self):
        for case in self.vectors["current_loop_bridge_cases"]:
            with self.subTest(case=case["name"]):
                inputs = _loop_inputs(case["inputs"])
                result = current_control_step(
                    inputs,
                    _loop_gains(case["gains"]),
                    CurrentLoopState(),
                )
                bridge = current_loop_result_to_mcsdk_state(
                    result=result,
                    target_dq=DQ(d=inputs.target_id, q=inputs.target_iq),
                    theta_e_rad=inputs.theta_e_rad,
                    pwm_period_cycles=case["pwm_period_cycles"],
                )
                expected = case["expected"]

                self.assertEqual(bridge.iqd.q, expected["iqd"]["q"])
                self.assertEqual(bridge.iqd.d, expected["iqd"]["d"])
                self.assertEqual(bridge.iqdref.q, expected["iqdref"]["q"])
                self.assertEqual(bridge.iqdref.d, expected["iqdref"]["d"])
                self.assertEqual(bridge.vqd.q, expected["vqd"]["q"])
                self.assertEqual(bridge.vqd.d, expected["vqd"]["d"])
                self.assertEqual(bridge.theta_q15, expected["theta_q15"])
                self.assertEqual(bridge.duty_counts.a, expected["duty_counts"]["a"])
                self.assertEqual(bridge.duty_counts.b, expected["duty_counts"]["b"])
                self.assertEqual(bridge.duty_counts.c, expected["duty_counts"]["c"])
                self.assertEqual(bridge.host_pwm_saturated, expected["host_pwm_saturated"])
                self.assertAlmostEqual(bridge.host_pwm_scale, expected["host_pwm_scale"], places=12)

    def test_sensorless_observer_snapshot_vectors_replay_against_bridge(self):
        for case in self.vectors["sensorless_observer_snapshot_cases"]:
            with self.subTest(case=case["name"]):
                snapshot = sensorless_result_to_mcsdk_observer_snapshot(
                    theta_e_rad=case["sensorless"]["theta_e_rad"],
                    omega_e_rad_s=case["sensorless"]["omega_e_rad_s"],
                    confidence=case["sensorless"]["confidence"],
                    mode=case["sensorless"]["mode"],
                    locked=case["sensorless"]["locked"],
                    omega_full_scale_rad_s=case["omega_full_scale_rad_s"],
                )
                expected = case["expected"]

                self.assertEqual(snapshot.theta_q15, expected["theta_q15"])
                self.assertEqual(snapshot.omega_q15, expected["omega_q15"])
                self.assertEqual(snapshot.confidence_q15, expected["confidence_q15"])
                self.assertEqual(snapshot.mode, expected["mode"])
                self.assertEqual(snapshot.locked, expected["locked"])

    def test_sensorless_observer_snapshot_rejects_non_positive_omega_scale(self):
        with self.assertRaisesRegex(ValueError, "omega_full_scale_rad_s must be positive"):
            sensorless_result_to_mcsdk_observer_snapshot(
                theta_e_rad=0.0,
                omega_e_rad_s=0.0,
                confidence=0.0,
                mode="startup",
                locked=False,
                omega_full_scale_rad_s=0.0,
            )

    def test_speed_command_snapshot_vectors_replay_against_bridge(self):
        for case in self.vectors["sensorless_speed_command_snapshot_cases"]:
            with self.subTest(case=case["name"]):
                snapshot = speed_command_to_mcsdk_snapshot(
                    **case["speed_command"],
                    omega_full_scale_rad_s=case["omega_full_scale_rad_s"],
                    iq_full_scale_a=case["iq_full_scale_a"],
                )
                expected = case["expected"]

                self.assertEqual(snapshot.target_omega_q15, expected["target_omega_q15"])
                self.assertEqual(snapshot.measured_omega_q15, expected["measured_omega_q15"])
                self.assertEqual(snapshot.requested_iq_q15, expected["requested_iq_q15"])
                self.assertEqual(snapshot.effective_iq_q15, expected["effective_iq_q15"])
                self.assertEqual(snapshot.locked, expected["locked"])
                self.assertEqual(snapshot.limited, expected["limited"])
                self.assertEqual(snapshot.reason, expected["reason"])

    def test_speed_command_snapshot_rejects_missing_policy_inputs(self):
        frontend_config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=0.0,
            startup_target_omega_e_rad_s=0.0,
            lock_blend_factor=1.0,
        )
        gains = _loop_gains(
            {
                "d": {"kp": 0.0, "ki": 0.0, "output_limit": 6.0},
                "q": {"kp": 0.0, "ki": 0.0, "output_limit": 6.0},
            }
        )
        replay = sensorless_current_control_replay_sequence(
            [
                SensorlessCurrentLoopInputs(
                    i_a=0.0,
                    i_b=0.0,
                    i_c=0.0,
                    target_id=0.0,
                    target_iq=0.0,
                    vbus=24.0,
                    dt_s=0.1,
                    observer_theta_e_rad=0.0,
                    observer_omega_e_rad_s=0.0,
                    observer_confidence=0.0,
                )
            ],
            SensorlessFrontendState(),
            frontend_config,
            gains,
            CurrentLoopState(),
        )

        with self.assertRaisesRegex(ValueError, "result.speed_loop is required"):
            sensorless_result_to_mcsdk_speed_command_snapshot(
                replay.steps[0],
                omega_full_scale_rad_s=20.0,
                iq_full_scale_a=2.0,
            )

    def test_replay_final_sensorless_step_can_be_snapshotted_for_comparison(self):
        frontend_config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=0.0,
            startup_target_omega_e_rad_s=0.0,
            lock_blend_factor=1.0,
            observer_max_angle_step_rad=0.5,
        )
        observer_config = SensorlessObserverConfig(
            stator_resistance_ohm=0.0,
            bemf_confidence_full_scale_v=2.0,
            max_angle_step_rad=0.4,
        )
        gains = _loop_gains(
            {
                "d": {"kp": 0.0, "ki": 0.0, "output_limit": 6.0},
                "q": {"kp": 0.0, "ki": 10.0, "output_limit": 6.0},
            }
        )
        common = {
            "i_a": 0.0,
            "i_b": 0.0,
            "i_c": 0.0,
            "target_id": 0.0,
            "target_iq": 1.0,
            "vbus": 24.0,
            "dt_s": 0.1,
        }
        replay = sensorless_current_control_replay_sequence(
            [
                SensorlessCurrentLoopInputs(**common, v_alpha=0.1, v_beta=0.0),
                SensorlessCurrentLoopInputs(**common, v_alpha=0.0, v_beta=3.0),
            ],
            SensorlessFrontendState(),
            frontend_config,
            gains,
            CurrentLoopState(),
            observer_config,
            SensorlessObserverState(),
        )

        snapshot = sensorless_result_to_mcsdk_observer_snapshot(
            theta_e_rad=replay.steps[-1].sensorless.theta_e_rad,
            omega_e_rad_s=replay.steps[-1].sensorless.omega_e_rad_s,
            confidence=replay.steps[-1].sensorless.confidence,
            mode=replay.steps[-1].sensorless.mode,
            locked=replay.steps[-1].sensorless.locked,
            omega_full_scale_rad_s=8.0,
        )

        self.assertEqual(snapshot.theta_q15, 0)
        self.assertEqual(snapshot.omega_q15, 16384)
        self.assertEqual(snapshot.confidence_q15, 32767)
        self.assertEqual(snapshot.mode, "tracking")
        self.assertTrue(snapshot.locked)

    def test_replay_sequence_steps_can_be_snapshotted_for_comparison(self):
        for case in self.vectors["sensorless_replay_observer_snapshot_sequence_cases"]:
            with self.subTest(case=case["name"]):
                replay = sensorless_current_control_replay_sequence(
                    [SensorlessCurrentLoopInputs(**step) for step in case["inputs"]],
                    SensorlessFrontendState(**case["sensorless_state"]),
                    _sensorless_frontend_config(case["config"]),
                    _loop_gains(case["gains"]),
                    CurrentLoopState(),
                    startup_policy_config=SensorlessStartupPolicyConfig(
                        **case["startup_policy_config"]
                    ),
                    startup_policy_state=SensorlessStartupPolicyState(
                        **case["startup_policy_state"]
                    ),
                )
                snapshots = sensorless_replay_to_mcsdk_observer_snapshots(
                    replay,
                    omega_full_scale_rad_s=case["omega_full_scale_rad_s"],
                )

                self.assertEqual(len(snapshots), len(case["expected_snapshots"]))
                for snapshot, expected in zip(snapshots, case["expected_snapshots"]):
                    self.assertEqual(snapshot.theta_q15, expected["theta_q15"])
                    self.assertEqual(snapshot.omega_q15, expected["omega_q15"])
                    self.assertEqual(snapshot.confidence_q15, expected["confidence_q15"])
                    self.assertEqual(snapshot.mode, expected["mode"])
                    self.assertEqual(snapshot.locked, expected["locked"])

    def test_speed_command_replay_steps_can_be_snapshotted_for_comparison(self):
        for case in self.vectors["sensorless_replay_speed_command_snapshot_sequence_cases"]:
            with self.subTest(case=case["name"]):
                replay = sensorless_current_control_replay_sequence(
                    [SensorlessCurrentLoopInputs(**step) for step in case["inputs"]],
                    SensorlessFrontendState(**case["sensorless_state"]),
                    _sensorless_frontend_config(case["config"]),
                    _loop_gains(case["gains"]),
                    CurrentLoopState(),
                    startup_policy_config=SensorlessStartupPolicyConfig(
                        **case["startup_policy_config"]
                    ),
                    startup_policy_state=SensorlessStartupPolicyState(
                        **case["startup_policy_state"]
                    ),
                    speed_loop_config=_speed_loop_config(case["speed_loop_config"]),
                    speed_loop_state=_speed_loop_state(case["speed_loop_state"]),
                    current_command_policy_config=SensorlessCurrentCommandPolicyConfig(
                        **case["current_command_policy_config"]
                    ),
                )
                snapshots = sensorless_replay_to_mcsdk_speed_command_snapshots(
                    replay,
                    omega_full_scale_rad_s=case["omega_full_scale_rad_s"],
                    iq_full_scale_a=case["iq_full_scale_a"],
                )

                self.assertEqual(len(snapshots), len(case["expected_snapshots"]))
                for snapshot, expected in zip(
                    snapshots, case["expected_snapshots"], strict=True
                ):
                    self.assertEqual(snapshot.target_omega_q15, expected["target_omega_q15"])
                    self.assertEqual(
                        snapshot.measured_omega_q15, expected["measured_omega_q15"]
                    )
                    self.assertEqual(snapshot.requested_iq_q15, expected["requested_iq_q15"])
                    self.assertEqual(snapshot.effective_iq_q15, expected["effective_iq_q15"])
                    self.assertEqual(snapshot.locked, expected["locked"])
                    self.assertEqual(snapshot.limited, expected["limited"])
                    self.assertEqual(snapshot.reason, expected["reason"])


if __name__ == "__main__":
    unittest.main()
