import math
import unittest

from src.foc_core_model import CurrentLoopGains, CurrentLoopState, DQ, PIConfig, PIState
from src.foc_mcsdk_bridge import current_loop_result_to_mcsdk_state
from src.foc_sensorless_frontend import (
    MODE_STARTUP,
    MODE_TRACKING,
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
    normalize_angle_rad,
    sensorless_current_command_policy_step,
    sensorless_current_control_step,
    sensorless_current_control_replay_sequence,
    sensorless_frontend_step,
    sensorless_speed_loop_step,
    sensorless_startup_policy_step,
)


class SensorlessFrontendRuleTests(unittest.TestCase):
    def test_normalize_angle_wraps_negative_and_large_angles(self):
        self.assertAlmostEqual(
            normalize_angle_rad(-math.pi / 2.0),
            1.5 * math.pi,
        )
        self.assertAlmostEqual(
            normalize_angle_rad(5.0 * math.pi),
            math.pi,
        )

    def test_startup_mode_advances_theta_with_ramp_until_lock(self):
        config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=100.0,
            startup_target_omega_e_rad_s=20.0,
            lock_blend_factor=0.5,
        )
        result = sensorless_frontend_step(
            SensorlessFrontendInputs(
                i_alpha=0.0,
                i_beta=0.0,
                v_alpha=0.0,
                v_beta=0.0,
                dt_s=0.1,
                observer_confidence=0.2,
            ),
            SensorlessFrontendState(),
            config,
        )

        self.assertEqual(result.mode, MODE_STARTUP)
        self.assertFalse(result.locked)
        self.assertAlmostEqual(result.omega_e_rad_s, 10.0)
        self.assertAlmostEqual(result.theta_e_rad, 1.0)

    def test_tracking_mode_blends_observer_theta_after_lock(self):
        config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=0.0,
            startup_target_omega_e_rad_s=0.0,
            lock_blend_factor=0.5,
        )
        result = sensorless_frontend_step(
            SensorlessFrontendInputs(
                i_alpha=0.0,
                i_beta=0.0,
                v_alpha=0.0,
                v_beta=0.0,
                dt_s=0.1,
                observer_theta_e_rad=1.0,
                observer_omega_e_rad_s=30.0,
                observer_confidence=0.95,
            ),
            SensorlessFrontendState(theta_e_rad=0.2, omega_e_rad_s=10.0),
            config,
        )

        self.assertEqual(result.mode, MODE_TRACKING)
        self.assertTrue(result.locked)
        self.assertAlmostEqual(result.theta_e_rad, 0.6)
        self.assertAlmostEqual(result.omega_e_rad_s, 20.0)
        self.assertAlmostEqual(result.confidence, 0.95)

    def test_tracking_mode_blends_theta_across_wrap_by_shortest_path(self):
        config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=0.0,
            startup_target_omega_e_rad_s=0.0,
            lock_blend_factor=0.5,
        )
        result = sensorless_frontend_step(
            SensorlessFrontendInputs(
                i_alpha=0.0,
                i_beta=0.0,
                v_alpha=0.0,
                v_beta=0.0,
                dt_s=0.1,
                observer_theta_e_rad=0.1,
                observer_omega_e_rad_s=9.0,
                observer_confidence=0.95,
            ),
            SensorlessFrontendState(theta_e_rad=6.1, omega_e_rad_s=5.0),
            config,
        )

        self.assertEqual(result.mode, MODE_TRACKING)
        self.assertTrue(result.locked)
        self.assertAlmostEqual(result.theta_e_rad, 6.241592653589793)
        self.assertAlmostEqual(result.omega_e_rad_s, 7.0)
        self.assertLess(result.theta_e_rad, 2.0 * math.pi)

    def test_observer_angle_step_is_limited_before_lock(self):
        config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=0.0,
            startup_target_omega_e_rad_s=0.0,
            lock_blend_factor=1.0,
            observer_max_angle_step_rad=0.25,
        )
        result = sensorless_frontend_step(
            SensorlessFrontendInputs(
                i_alpha=0.0,
                i_beta=0.0,
                v_alpha=0.0,
                v_beta=0.0,
                dt_s=0.1,
                observer_theta_e_rad=2.0,
                observer_confidence=0.95,
            ),
            SensorlessFrontendState(theta_e_rad=0.0, omega_e_rad_s=0.0),
            config,
        )

        self.assertAlmostEqual(result.theta_e_rad, 0.25)

    def test_back_emf_observer_uses_alpha_beta_voltage_and_current(self):
        config = SensorlessObserverConfig(
            stator_resistance_ohm=0.5,
            bemf_confidence_full_scale_v=4.0,
            max_angle_step_rad=0.5,
        )
        result = back_emf_observer_step(
            SensorlessFrontendInputs(
                i_alpha=1.0,
                i_beta=-2.0,
                v_alpha=0.5,
                v_beta=5.0,
                dt_s=0.001,
            ),
            SensorlessObserverState(),
            config,
        )

        self.assertAlmostEqual(result.back_emf_ab.alpha, 0.0)
        self.assertAlmostEqual(result.back_emf_ab.beta, 6.0)
        self.assertAlmostEqual(result.back_emf_magnitude, 6.0)
        self.assertAlmostEqual(result.theta_e_rad, 0.0)
        self.assertAlmostEqual(result.omega_e_rad_s, 0.0)
        self.assertAlmostEqual(result.confidence, 1.0)

    def test_back_emf_observer_limits_angle_step_and_decays_confidence(self):
        config = SensorlessObserverConfig(
            stator_resistance_ohm=0.0,
            bemf_confidence_full_scale_v=1.0,
            max_angle_step_rad=1.0,
            confidence_decay_filter=0.25,
            omega_filter=0.5,
        )
        result = back_emf_observer_step(
            SensorlessFrontendInputs(
                i_alpha=0.0,
                i_beta=0.0,
                v_alpha=0.1,
                v_beta=0.0,
                dt_s=0.001,
            ),
            SensorlessObserverState(
                theta_e_rad=1.0,
                omega_e_rad_s=20.0,
                confidence=0.8,
            ),
            config,
        )

        self.assertAlmostEqual(result.theta_e_rad, 0.0)
        self.assertAlmostEqual(result.omega_e_rad_s, -490.0)
        self.assertAlmostEqual(result.confidence, 0.625)
        self.assertAlmostEqual(result.back_emf_magnitude, 0.1)

    def test_current_control_step_uses_frontend_theta(self):
        config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=0.0,
            startup_target_omega_e_rad_s=0.0,
            lock_blend_factor=1.0,
        )
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=1.0, ki=0.0, output_limit=6.0),
            q_axis=PIConfig(kp=1.0, ki=0.0, output_limit=6.0),
        )

        result = sensorless_current_control_step(
            SensorlessCurrentLoopInputs(
                i_a=1.0,
                i_b=-0.5,
                i_c=-0.5,
                target_id=0.0,
                target_iq=0.0,
                vbus=24.0,
                dt_s=0.0001,
                observer_theta_e_rad=math.pi / 2.0,
                observer_omega_e_rad_s=5.0,
                observer_confidence=1.0,
            ),
            SensorlessFrontendState(),
            config,
            gains,
            CurrentLoopState(),
        )

        self.assertTrue(result.sensorless.locked)
        self.assertAlmostEqual(result.sensorless.theta_e_rad, math.pi / 2.0)
        self.assertAlmostEqual(result.current_loop.current_dq.q, -1.0, places=12)
        self.assertAlmostEqual(result.current_loop.svpwm.duty.a, 0.46875, places=12)
        self.assertAlmostEqual(result.current_loop.svpwm.duty.b, 0.53125, places=12)
        self.assertAlmostEqual(result.current_loop.svpwm.duty.c, 0.53125, places=12)

    def test_current_control_step_can_use_back_emf_observer_stub(self):
        frontend_config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=0.0,
            startup_target_omega_e_rad_s=0.0,
            lock_blend_factor=1.0,
            observer_max_angle_step_rad=0.5,
        )
        observer_config = SensorlessObserverConfig(
            stator_resistance_ohm=0.5,
            bemf_confidence_full_scale_v=4.0,
            max_angle_step_rad=0.5,
        )
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=1.0, ki=0.0, output_limit=6.0),
            q_axis=PIConfig(kp=1.0, ki=0.0, output_limit=6.0),
        )

        result = sensorless_current_control_step(
            SensorlessCurrentLoopInputs(
                i_a=1.0,
                i_b=-0.5,
                i_c=-0.5,
                target_id=0.0,
                target_iq=0.0,
                vbus=24.0,
                dt_s=0.001,
                v_alpha=0.5,
                v_beta=5.0,
            ),
            SensorlessFrontendState(),
            frontend_config,
            gains,
            CurrentLoopState(),
            observer_config,
            SensorlessObserverState(),
        )
        bridge = current_loop_result_to_mcsdk_state(
            result=result.current_loop,
            target_dq=DQ(d=0.0, q=0.0),
            theta_e_rad=result.sensorless.theta_e_rad,
            pwm_period_cycles=1000,
        )

        self.assertIsNotNone(result.observer)
        self.assertTrue(result.sensorless.locked)
        self.assertEqual(result.sensorless.mode, MODE_TRACKING)
        self.assertAlmostEqual(result.sensorless.theta_e_rad, 0.0)
        self.assertAlmostEqual(result.current_loop.current_dq.d, 1.0)
        self.assertAlmostEqual(result.current_loop.svpwm.duty.a, 0.46875, places=12)
        self.assertEqual(bridge.theta_q15, 0)
        self.assertEqual(bridge.duty_counts.a, 469)
        self.assertEqual(bridge.host_pwm_saturated, False)

    def test_startup_policy_requires_consecutive_lock_and_loss_candidates(self):
        config = SensorlessStartupPolicyConfig(
            lock_confidence_threshold=0.8,
            unlock_confidence_threshold=0.2,
            lock_count_required=2,
            unlock_count_required=2,
        )
        state = SensorlessStartupPolicyState()

        first_lock = sensorless_startup_policy_step(0.85, state, config)
        second_lock = sensorless_startup_policy_step(0.9, first_lock.state, config)
        reset_loss = sensorless_startup_policy_step(0.3, second_lock.state, config)
        first_loss = sensorless_startup_policy_step(0.1, reset_loss.state, config)
        second_loss = sensorless_startup_policy_step(0.1, first_loss.state, config)

        self.assertFalse(first_lock.tracking_enabled)
        self.assertEqual(first_lock.lock_candidate_count, 1)
        self.assertTrue(second_lock.tracking_enabled)
        self.assertEqual(second_lock.lock_candidate_count, 2)
        self.assertTrue(reset_loss.tracking_enabled)
        self.assertEqual(reset_loss.loss_candidate_count, 0)
        self.assertTrue(first_loss.tracking_enabled)
        self.assertEqual(first_loss.loss_candidate_count, 1)
        self.assertFalse(second_loss.tracking_enabled)
        self.assertFalse(second_loss.frontend_lock_override)
        self.assertEqual(second_loss.loss_candidate_count, 2)

    def test_speed_loop_rate_limits_target_and_saturates_iq_reference(self):
        config = SensorlessSpeedLoopConfig(
            speed_pi=PIConfig(kp=0.2, ki=1.0, output_limit=2.0),
            target_omega_rate_limit_e_rad_s2=50.0,
        )

        first = sensorless_speed_loop_step(
            target_omega_e_rad_s=20.0,
            measured_omega_e_rad_s=2.0,
            dt_s=0.1,
            state=SensorlessSpeedLoopState(),
            config=config,
        )
        second = sensorless_speed_loop_step(
            target_omega_e_rad_s=20.0,
            measured_omega_e_rad_s=4.0,
            dt_s=0.1,
            state=first.state,
            config=config,
        )

        self.assertAlmostEqual(first.target_omega_e_rad_s, 5.0)
        self.assertAlmostEqual(first.speed_error_e_rad_s, 3.0)
        self.assertAlmostEqual(first.target_iq, 0.9)
        self.assertFalse(first.saturated)
        self.assertAlmostEqual(first.state.speed_pi.integrator, 0.3)
        self.assertAlmostEqual(second.target_omega_e_rad_s, 10.0)
        self.assertAlmostEqual(second.speed_error_e_rad_s, 6.0)
        self.assertAlmostEqual(second.target_iq, 1.5)
        self.assertFalse(second.saturated)

    def test_speed_loop_supports_signed_reverse_target_and_integrator(self):
        config = SensorlessSpeedLoopConfig(
            speed_pi=PIConfig(kp=0.2, ki=1.0, output_limit=3.0),
            target_omega_rate_limit_e_rad_s2=50.0,
        )

        first = sensorless_speed_loop_step(
            target_omega_e_rad_s=-20.0,
            measured_omega_e_rad_s=-2.0,
            dt_s=0.1,
            state=SensorlessSpeedLoopState(),
            config=config,
        )
        second = sensorless_speed_loop_step(
            target_omega_e_rad_s=-20.0,
            measured_omega_e_rad_s=-4.0,
            dt_s=0.1,
            state=first.state,
            config=config,
        )

        self.assertAlmostEqual(first.target_omega_e_rad_s, -5.0)
        self.assertAlmostEqual(first.speed_error_e_rad_s, -3.0)
        self.assertAlmostEqual(first.target_iq, -0.9)
        self.assertAlmostEqual(first.state.speed_pi.integrator, -0.3)
        self.assertAlmostEqual(second.target_omega_e_rad_s, -10.0)
        self.assertAlmostEqual(second.speed_error_e_rad_s, -6.0)
        self.assertAlmostEqual(second.target_iq, -2.1)
        self.assertAlmostEqual(second.state.speed_pi.integrator, -0.9)
        self.assertFalse(second.saturated)

    def test_speed_loop_can_hold_pi_state_while_unlocked(self):
        config = SensorlessSpeedLoopConfig(
            speed_pi=PIConfig(kp=0.1, ki=0.5, output_limit=2.0),
            hold_when_unlocked=True,
        )
        state = SensorlessSpeedLoopState(
            speed_pi=PIState(integrator=0.75),
            target_omega_e_rad_s=12.0,
        )

        held = sensorless_speed_loop_step(
            target_omega_e_rad_s=20.0,
            measured_omega_e_rad_s=0.0,
            dt_s=0.1,
            state=state,
            config=config,
            enabled=False,
        )
        resumed = sensorless_speed_loop_step(
            target_omega_e_rad_s=20.0,
            measured_omega_e_rad_s=10.0,
            dt_s=0.1,
            state=held.state,
            config=config,
            enabled=True,
        )

        self.assertAlmostEqual(held.target_omega_e_rad_s, 12.0)
        self.assertAlmostEqual(held.target_iq, 0.0)
        self.assertAlmostEqual(held.state.speed_pi.integrator, 0.75)
        self.assertIs(held.state, state)
        self.assertAlmostEqual(resumed.target_omega_e_rad_s, 20.0)
        self.assertAlmostEqual(resumed.target_iq, 1.75)
        self.assertAlmostEqual(resumed.state.speed_pi.integrator, 0.75)

    def test_current_command_policy_limits_unlocked_and_tracking_commands(self):
        config = SensorlessCurrentCommandPolicyConfig(
            unlocked_iq_limit=0.0,
            locked_iq_limit=1.5,
        )

        unlocked = sensorless_current_command_policy_step(
            requested_target_iq=1.0,
            locked=False,
            config=config,
        )
        locked = sensorless_current_command_policy_step(
            requested_target_iq=2.0,
            locked=True,
            config=config,
        )
        reverse_locked = sensorless_current_command_policy_step(
            requested_target_iq=-2.0,
            locked=True,
            config=config,
        )

        self.assertEqual(unlocked.effective_target_iq, 0.0)
        self.assertTrue(unlocked.limited)
        self.assertEqual(unlocked.reason, "unlocked_current_limit")
        self.assertEqual(locked.effective_target_iq, 1.5)
        self.assertTrue(locked.limited)
        self.assertEqual(locked.reason, "tracking_command")
        self.assertEqual(reverse_locked.effective_target_iq, -1.5)
        self.assertTrue(reverse_locked.limited)
        self.assertEqual(reverse_locked.reason, "tracking_command")

    def test_replay_sequence_preserves_empty_initial_state(self):
        frontend_config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=10.0,
            startup_target_omega_e_rad_s=5.0,
            lock_blend_factor=1.0,
        )
        observer_config = SensorlessObserverConfig(
            stator_resistance_ohm=0.0,
            bemf_confidence_full_scale_v=2.0,
        )
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=0.0, ki=0.0, output_limit=6.0),
            q_axis=PIConfig(kp=0.0, ki=1.0, output_limit=6.0),
        )
        sensorless_state = SensorlessFrontendState(theta_e_rad=0.3, omega_e_rad_s=2.0)
        current_loop_state = CurrentLoopState()
        observer_state = SensorlessObserverState(theta_e_rad=0.4, confidence=0.2)

        result = sensorless_current_control_replay_sequence(
            [],
            sensorless_state,
            frontend_config,
            gains,
            current_loop_state,
            observer_config,
            observer_state,
        )

        self.assertEqual(result.steps, ())
        self.assertEqual(result.state, sensorless_state)
        self.assertEqual(result.current_loop_state, current_loop_state)
        self.assertEqual(result.observer_state, observer_state)

    def test_replay_sequence_carries_observer_frontend_and_pi_state(self):
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
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=0.0, ki=0.0, output_limit=6.0),
            q_axis=PIConfig(kp=0.0, ki=10.0, output_limit=6.0),
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

        result = sensorless_current_control_replay_sequence(
            [
                SensorlessCurrentLoopInputs(**common, v_alpha=0.1, v_beta=0.0),
                SensorlessCurrentLoopInputs(**common, v_alpha=0.0, v_beta=3.0),
                SensorlessCurrentLoopInputs(**common, v_alpha=0.0, v_beta=3.0),
            ],
            SensorlessFrontendState(),
            frontend_config,
            gains,
            CurrentLoopState(),
            observer_config,
            SensorlessObserverState(),
        )

        self.assertEqual(len(result.steps), 3)
        self.assertFalse(result.steps[0].sensorless.locked)
        self.assertTrue(result.steps[1].sensorless.locked)
        self.assertTrue(result.steps[2].sensorless.locked)
        self.assertAlmostEqual(result.steps[0].observer.confidence, 0.05)
        self.assertAlmostEqual(result.steps[1].observer.theta_e_rad, 0.0)
        self.assertAlmostEqual(result.steps[1].observer.omega_e_rad_s, 4.0)
        self.assertAlmostEqual(result.steps[2].observer.omega_e_rad_s, 0.0)
        self.assertAlmostEqual(result.current_loop_state.q_axis.integrator, 3.0)
        self.assertAlmostEqual(result.steps[0].current_loop_state.q_axis.integrator, 1.0)
        self.assertAlmostEqual(result.steps[1].current_loop_state.q_axis.integrator, 2.0)
        self.assertAlmostEqual(result.steps[2].current_loop_state.q_axis.integrator, 3.0)
        self.assertIsNotNone(result.observer_state)
        assert result.observer_state is not None
        self.assertAlmostEqual(result.observer_state.theta_e_rad, 0.0)
        self.assertAlmostEqual(result.observer_state.confidence, 1.0)

    def test_replay_sequence_can_use_startup_policy_lock_loss_and_relock(self):
        frontend_config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=10.0,
            startup_target_omega_e_rad_s=20.0,
            lock_blend_factor=1.0,
            observer_max_angle_step_rad=1.0,
        )
        policy_config = SensorlessStartupPolicyConfig(
            lock_confidence_threshold=0.8,
            unlock_confidence_threshold=0.2,
            lock_count_required=2,
            unlock_count_required=2,
        )
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=0.0, ki=0.0, output_limit=20.0),
            q_axis=PIConfig(kp=0.0, ki=10.0, output_limit=20.0),
        )
        common = {
            "i_a": 0.0,
            "i_b": 0.0,
            "i_c": 0.0,
            "target_id": 0.0,
            "target_iq": 1.0,
            "vbus": 24.0,
            "dt_s": 0.1,
            "observer_omega_e_rad_s": 10.0,
        }

        result = sensorless_current_control_replay_sequence(
            [
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.4,
                    observer_confidence=0.2,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.7,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.0,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.2,
                    observer_confidence=0.4,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.4,
                    observer_confidence=0.1,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.6,
                    observer_confidence=0.1,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=3.0,
                    observer_confidence=0.95,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=4.0,
                    observer_confidence=0.95,
                ),
            ],
            SensorlessFrontendState(),
            frontend_config,
            gains,
            CurrentLoopState(),
            startup_policy_config=policy_config,
            startup_policy_state=SensorlessStartupPolicyState(),
        )

        modes = [step.sensorless.mode for step in result.steps]
        locks = [step.sensorless.locked for step in result.steps]
        policy_enabled = [
            step.startup_policy.tracking_enabled for step in result.steps
        ]
        policy_lock_counts = [
            step.startup_policy.lock_candidate_count for step in result.steps
        ]
        policy_loss_counts = [
            step.startup_policy.loss_candidate_count for step in result.steps
        ]

        self.assertEqual(
            modes,
            [
                MODE_STARTUP,
                MODE_STARTUP,
                MODE_TRACKING,
                MODE_TRACKING,
                MODE_TRACKING,
                MODE_STARTUP,
                MODE_STARTUP,
                MODE_TRACKING,
            ],
        )
        self.assertEqual(
            locks,
            [False, False, True, True, True, False, False, True],
        )
        self.assertEqual(
            policy_enabled,
            [False, False, True, True, True, False, False, True],
        )
        self.assertEqual(policy_lock_counts, [0, 1, 2, 2, 2, 0, 1, 2])
        self.assertEqual(policy_loss_counts, [0, 0, 0, 0, 1, 2, 0, 0])
        self.assertAlmostEqual(result.steps[0].sensorless.theta_e_rad, 0.1)
        self.assertAlmostEqual(result.steps[1].sensorless.theta_e_rad, 0.3)
        self.assertAlmostEqual(result.steps[2].sensorless.theta_e_rad, 1.0)
        self.assertAlmostEqual(result.steps[5].sensorless.theta_e_rad, 2.5)
        self.assertAlmostEqual(result.steps[7].sensorless.theta_e_rad, 4.0)
        self.assertAlmostEqual(result.current_loop_state.q_axis.integrator, 8.0)
        self.assertIsNotNone(result.startup_policy_state)
        assert result.startup_policy_state is not None
        self.assertTrue(result.startup_policy_state.tracking_enabled)

    def test_replay_sequence_can_gate_speed_loop_iq_until_lock_and_after_loss(self):
        frontend_config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=10.0,
            startup_target_omega_e_rad_s=20.0,
            lock_blend_factor=1.0,
            observer_max_angle_step_rad=1.0,
        )
        policy_config = SensorlessStartupPolicyConfig(
            lock_confidence_threshold=0.8,
            unlock_confidence_threshold=0.2,
            lock_count_required=2,
            unlock_count_required=2,
        )
        speed_loop_config = SensorlessSpeedLoopConfig(
            speed_pi=PIConfig(kp=0.1, ki=0.0, output_limit=2.0),
        )
        command_policy_config = SensorlessCurrentCommandPolicyConfig(
            unlocked_iq_limit=0.0,
            locked_iq_limit=1.5,
        )
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=0.0, ki=0.0, output_limit=20.0),
            q_axis=PIConfig(kp=0.0, ki=10.0, output_limit=20.0),
        )
        common = {
            "i_a": 0.0,
            "i_b": 0.0,
            "i_c": 0.0,
            "target_id": 0.0,
            "target_iq": 9.0,
            "target_omega_e_rad_s": 20.0,
            "vbus": 24.0,
            "dt_s": 0.1,
            "observer_omega_e_rad_s": 10.0,
        }

        result = sensorless_current_control_replay_sequence(
            [
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.4,
                    observer_confidence=0.2,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.7,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.0,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.2,
                    observer_confidence=0.4,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.4,
                    observer_confidence=0.1,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.6,
                    observer_confidence=0.1,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=3.0,
                    observer_confidence=0.95,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=4.0,
                    observer_confidence=0.95,
                ),
            ],
            SensorlessFrontendState(),
            frontend_config,
            gains,
            CurrentLoopState(),
            startup_policy_config=policy_config,
            startup_policy_state=SensorlessStartupPolicyState(),
            speed_loop_config=speed_loop_config,
            speed_loop_state=SensorlessSpeedLoopState(),
            current_command_policy_config=command_policy_config,
        )

        speed_iq = [step.speed_loop.target_iq for step in result.steps]
        effective_iq = [
            step.current_command_policy.effective_target_iq for step in result.steps
        ]
        reasons = [step.current_command_policy.reason for step in result.steps]

        self.assertEqual(len(result.steps), 8)
        self.assertEqual(
            effective_iq,
            [0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0],
        )
        self.assertEqual(
            reasons,
            [
                "unlocked_current_limit",
                "unlocked_current_limit",
                "tracking_command",
                "tracking_command",
                "tracking_command",
                "unlocked_current_limit",
                "unlocked_current_limit",
                "tracking_command",
            ],
        )
        self.assertAlmostEqual(speed_iq[0], 1.9)
        self.assertAlmostEqual(speed_iq[5], 0.9)
        self.assertAlmostEqual(result.steps[2].current_loop_state.q_axis.integrator, 1.0)
        self.assertAlmostEqual(result.steps[4].current_loop_state.q_axis.integrator, 3.0)
        self.assertAlmostEqual(result.steps[5].current_loop_state.q_axis.integrator, 3.0)
        self.assertAlmostEqual(result.current_loop_state.q_axis.integrator, 4.0)
        self.assertIsNotNone(result.speed_loop_state)
        assert result.speed_loop_state is not None
        self.assertAlmostEqual(result.speed_loop_state.target_omega_e_rad_s, 20.0)

    def test_replay_sequence_can_hold_speed_loop_pi_until_lock_and_after_loss(self):
        frontend_config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=10.0,
            startup_target_omega_e_rad_s=20.0,
            lock_blend_factor=1.0,
            observer_max_angle_step_rad=1.0,
        )
        policy_config = SensorlessStartupPolicyConfig(
            lock_confidence_threshold=0.8,
            unlock_confidence_threshold=0.2,
            lock_count_required=2,
            unlock_count_required=2,
        )
        speed_loop_config = SensorlessSpeedLoopConfig(
            speed_pi=PIConfig(kp=0.1, ki=0.5, output_limit=2.0),
            hold_when_unlocked=True,
        )
        command_policy_config = SensorlessCurrentCommandPolicyConfig(
            unlocked_iq_limit=0.0,
            locked_iq_limit=1.5,
        )
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=0.0, ki=0.0, output_limit=20.0),
            q_axis=PIConfig(kp=0.0, ki=10.0, output_limit=20.0),
        )
        common = {
            "i_a": 0.0,
            "i_b": 0.0,
            "i_c": 0.0,
            "target_id": 0.0,
            "target_iq": 9.0,
            "target_omega_e_rad_s": 20.0,
            "vbus": 24.0,
            "dt_s": 0.1,
            "observer_omega_e_rad_s": 10.0,
        }

        result = sensorless_current_control_replay_sequence(
            [
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.4,
                    observer_confidence=0.2,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.7,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.0,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.2,
                    observer_confidence=0.4,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.4,
                    observer_confidence=0.1,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.6,
                    observer_confidence=0.1,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=3.0,
                    observer_confidence=0.95,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=4.0,
                    observer_confidence=0.95,
                ),
            ],
            SensorlessFrontendState(),
            frontend_config,
            gains,
            CurrentLoopState(),
            startup_policy_config=policy_config,
            startup_policy_state=SensorlessStartupPolicyState(),
            speed_loop_config=speed_loop_config,
            speed_loop_state=SensorlessSpeedLoopState(),
            current_command_policy_config=command_policy_config,
        )

        speed_iq = [step.speed_loop.target_iq for step in result.steps]
        speed_integrators = [
            step.speed_loop.state.speed_pi.integrator for step in result.steps
        ]
        speed_targets = [
            step.speed_loop.state.target_omega_e_rad_s for step in result.steps
        ]
        effective_iq = [
            step.current_command_policy.effective_target_iq for step in result.steps
        ]

        self.assertEqual(
            speed_iq,
            [0.0, 0.0, 1.5, 2.0, 2.0, 0.0, 0.0, 2.0],
        )
        self.assertEqual(
            speed_targets,
            [0.0, 0.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0],
        )
        self.assertEqual(
            speed_integrators,
            [0.0, 0.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0],
        )
        self.assertEqual(
            effective_iq,
            [0.0, 0.0, 1.5, 1.5, 1.5, 0.0, 0.0, 1.5],
        )
        self.assertAlmostEqual(result.current_loop_state.q_axis.integrator, 6.0)

    def test_replay_sequence_preserves_signed_reverse_speed_current_command(self):
        frontend_config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=10.0,
            startup_target_omega_e_rad_s=20.0,
            lock_blend_factor=1.0,
            observer_max_angle_step_rad=1.0,
        )
        policy_config = SensorlessStartupPolicyConfig(
            lock_confidence_threshold=0.8,
            unlock_confidence_threshold=0.2,
            lock_count_required=2,
            unlock_count_required=2,
        )
        speed_loop_config = SensorlessSpeedLoopConfig(
            speed_pi=PIConfig(kp=0.1, ki=0.5, output_limit=2.0),
            hold_when_unlocked=True,
        )
        command_policy_config = SensorlessCurrentCommandPolicyConfig(
            unlocked_iq_limit=0.0,
            locked_iq_limit=1.5,
        )
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=0.0, ki=0.0, output_limit=20.0),
            q_axis=PIConfig(kp=0.0, ki=10.0, output_limit=20.0),
        )
        common = {
            "i_a": 0.0,
            "i_b": 0.0,
            "i_c": 0.0,
            "target_id": 0.0,
            "target_iq": 9.0,
            "target_omega_e_rad_s": -20.0,
            "vbus": 24.0,
            "dt_s": 0.1,
            "observer_omega_e_rad_s": -10.0,
        }

        result = sensorless_current_control_replay_sequence(
            [
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=5.8,
                    observer_confidence=0.2,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=5.5,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=5.2,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=5.0,
                    observer_confidence=0.4,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=4.8,
                    observer_confidence=0.1,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=4.6,
                    observer_confidence=0.1,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=3.8,
                    observer_confidence=0.95,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=3.5,
                    observer_confidence=0.95,
                ),
            ],
            SensorlessFrontendState(),
            frontend_config,
            gains,
            CurrentLoopState(),
            startup_policy_config=policy_config,
            startup_policy_state=SensorlessStartupPolicyState(),
            speed_loop_config=speed_loop_config,
            speed_loop_state=SensorlessSpeedLoopState(),
            current_command_policy_config=command_policy_config,
        )

        speed_iq = [step.speed_loop.target_iq for step in result.steps]
        speed_integrators = [
            step.speed_loop.state.speed_pi.integrator for step in result.steps
        ]
        speed_targets = [
            step.speed_loop.state.target_omega_e_rad_s for step in result.steps
        ]
        effective_iq = [
            step.current_command_policy.effective_target_iq for step in result.steps
        ]
        q_integrators = [
            step.current_loop_state.q_axis.integrator for step in result.steps
        ]

        self.assertEqual(
            speed_iq,
            [0.0, 0.0, -1.5, -2.0, -2.0, 0.0, 0.0, -2.0],
        )
        self.assertEqual(
            speed_targets,
            [0.0, 0.0, -20.0, -20.0, -20.0, -20.0, -20.0, -20.0],
        )
        self.assertEqual(
            speed_integrators,
            [0.0, 0.0, -0.5, -1.0, -1.0, -1.0, -1.0, -1.0],
        )
        self.assertEqual(
            effective_iq,
            [0.0, 0.0, -1.5, -1.5, -1.5, 0.0, 0.0, -1.5],
        )
        self.assertEqual(
            q_integrators,
            [0.0, 0.0, -1.5, -3.0, -4.5, -4.5, -4.5, -6.0],
        )
        self.assertIsNotNone(result.speed_loop_state)
        assert result.speed_loop_state is not None
        self.assertAlmostEqual(result.speed_loop_state.target_omega_e_rad_s, -20.0)
        self.assertAlmostEqual(result.speed_loop_state.speed_pi.integrator, -1.0)
        self.assertAlmostEqual(result.current_loop_state.q_axis.integrator, -6.0)

    def test_replay_sequence_rate_limits_signed_reverse_target_command(self):
        frontend_config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=10.0,
            startup_target_omega_e_rad_s=20.0,
            lock_blend_factor=1.0,
            observer_max_angle_step_rad=1.0,
        )
        policy_config = SensorlessStartupPolicyConfig(
            lock_confidence_threshold=0.8,
            unlock_confidence_threshold=0.2,
            lock_count_required=2,
            unlock_count_required=2,
        )
        speed_loop_config = SensorlessSpeedLoopConfig(
            speed_pi=PIConfig(kp=0.1, ki=0.5, output_limit=2.0),
            target_omega_rate_limit_e_rad_s2=50.0,
            hold_when_unlocked=True,
        )
        command_policy_config = SensorlessCurrentCommandPolicyConfig(
            unlocked_iq_limit=0.0,
            locked_iq_limit=1.5,
        )
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=0.0, ki=0.0, output_limit=20.0),
            q_axis=PIConfig(kp=0.0, ki=10.0, output_limit=20.0),
        )
        common = {
            "i_a": 0.0,
            "i_b": 0.0,
            "i_c": 0.0,
            "target_id": 0.0,
            "target_iq": 9.0,
            "target_omega_e_rad_s": -20.0,
            "vbus": 24.0,
            "dt_s": 0.1,
            "observer_omega_e_rad_s": -10.0,
        }

        result = sensorless_current_control_replay_sequence(
            [
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=5.8,
                    observer_confidence=0.2,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=5.5,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=5.2,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=5.0,
                    observer_confidence=0.4,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=4.8,
                    observer_confidence=0.1,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=4.6,
                    observer_confidence=0.1,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=3.8,
                    observer_confidence=0.95,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=3.5,
                    observer_confidence=0.95,
                ),
            ],
            SensorlessFrontendState(),
            frontend_config,
            gains,
            CurrentLoopState(),
            startup_policy_config=policy_config,
            startup_policy_state=SensorlessStartupPolicyState(),
            speed_loop_config=speed_loop_config,
            speed_loop_state=SensorlessSpeedLoopState(),
            current_command_policy_config=command_policy_config,
        )

        speed_iq = [step.speed_loop.target_iq for step in result.steps]
        speed_integrators = [
            step.speed_loop.state.speed_pi.integrator for step in result.steps
        ]
        speed_targets = [
            step.speed_loop.state.target_omega_e_rad_s for step in result.steps
        ]
        effective_iq = [
            step.current_command_policy.effective_target_iq for step in result.steps
        ]
        q_integrators = [
            step.current_loop_state.q_axis.integrator for step in result.steps
        ]

        self.assertEqual(
            speed_iq,
            [0.0, 0.0, 0.75, 0.25, -0.5, 0.0, 0.0, -1.5],
        )
        self.assertEqual(
            speed_targets,
            [0.0, 0.0, -5.0, -10.0, -15.0, -15.0, -15.0, -20.0],
        )
        self.assertEqual(
            speed_integrators,
            [0.0, 0.0, 0.25, 0.25, 0.0, 0.0, 0.0, -0.5],
        )
        self.assertEqual(
            effective_iq,
            [0.0, 0.0, 0.75, 0.25, -0.5, 0.0, 0.0, -1.5],
        )
        self.assertEqual(
            q_integrators,
            [0.0, 0.0, 0.75, 1.0, 0.5, 0.5, 0.5, -1.0],
        )
        self.assertIsNotNone(result.speed_loop_state)
        assert result.speed_loop_state is not None
        self.assertAlmostEqual(result.speed_loop_state.target_omega_e_rad_s, -20.0)
        self.assertAlmostEqual(result.speed_loop_state.speed_pi.integrator, -0.5)
        self.assertAlmostEqual(result.current_loop_state.q_axis.integrator, -1.0)

    def test_replay_sequence_freezes_reverse_target_until_lock_not_startup_strategy(self):
        frontend_config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=10.0,
            startup_target_omega_e_rad_s=20.0,
            lock_blend_factor=1.0,
            observer_max_angle_step_rad=1.0,
        )
        policy_config = SensorlessStartupPolicyConfig(
            lock_confidence_threshold=0.8,
            unlock_confidence_threshold=0.2,
            lock_count_required=2,
            unlock_count_required=2,
        )
        speed_loop_config = SensorlessSpeedLoopConfig(
            speed_pi=PIConfig(kp=0.1, ki=0.5, output_limit=2.0),
            target_omega_rate_limit_e_rad_s2=50.0,
            hold_when_unlocked=True,
        )
        command_policy_config = SensorlessCurrentCommandPolicyConfig(
            unlocked_iq_limit=0.0,
            locked_iq_limit=1.5,
        )
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=0.0, ki=0.0, output_limit=20.0),
            q_axis=PIConfig(kp=0.0, ki=10.0, output_limit=20.0),
        )
        common = {
            "i_a": 0.0,
            "i_b": 0.0,
            "i_c": 0.0,
            "target_id": 0.0,
            "target_iq": 9.0,
            "target_omega_e_rad_s": -20.0,
            "vbus": 24.0,
            "dt_s": 0.1,
            "observer_omega_e_rad_s": -10.0,
        }

        result = sensorless_current_control_replay_sequence(
            [
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.2,
                    observer_confidence=0.2,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.4,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.6,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.8,
                    observer_confidence=0.95,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.0,
                    observer_confidence=0.95,
                ),
            ],
            SensorlessFrontendState(
                theta_e_rad=0.0,
                omega_e_rad_s=0.0,
                mode=MODE_STARTUP,
                locked=False,
                confidence=0.0,
            ),
            frontend_config,
            gains,
            CurrentLoopState(),
            startup_policy_config=policy_config,
            startup_policy_state=SensorlessStartupPolicyState(),
            speed_loop_config=speed_loop_config,
            speed_loop_state=SensorlessSpeedLoopState(
                speed_pi=PIState(integrator=0.5),
                target_omega_e_rad_s=20.0,
            ),
            current_command_policy_config=command_policy_config,
        )

        speed_iq = [step.speed_loop.target_iq for step in result.steps]
        speed_integrators = [
            step.speed_loop.state.speed_pi.integrator for step in result.steps
        ]
        speed_targets = [
            step.speed_loop.state.target_omega_e_rad_s for step in result.steps
        ]
        effective_iq = [
            step.current_command_policy.effective_target_iq for step in result.steps
        ]
        command_reasons = [
            step.current_command_policy.reason for step in result.steps
        ]
        q_integrators = [
            step.current_loop_state.q_axis.integrator for step in result.steps
        ]
        locked = [step.sensorless.locked for step in result.steps]
        lock_counts = [
            step.startup_policy.lock_candidate_count for step in result.steps
        ]

        self.assertEqual(speed_targets, [20.0, 20.0, 15.0, 10.0, 5.0])
        self.assertEqual(speed_iq, [0.0, 0.0, 2.0, 2.0, 2.0])
        self.assertEqual(speed_integrators, [0.5, 0.5, 0.5, 0.5, 0.5])
        self.assertEqual(effective_iq, [0.0, 0.0, 1.5, 1.5, 1.5])
        self.assertEqual(
            command_reasons,
            [
                "unlocked_current_limit",
                "unlocked_current_limit",
                "tracking_command",
                "tracking_command",
                "tracking_command",
            ],
        )
        self.assertEqual(q_integrators, [0.0, 0.0, 1.5, 3.0, 4.5])
        self.assertEqual(locked, [False, False, True, True, True])
        self.assertEqual(lock_counts, [0, 1, 2, 2, 2])
        self.assertIsNotNone(result.speed_loop_state)
        assert result.speed_loop_state is not None
        self.assertAlmostEqual(result.speed_loop_state.target_omega_e_rad_s, 5.0)
        self.assertAlmostEqual(result.speed_loop_state.speed_pi.integrator, 0.5)
        self.assertAlmostEqual(result.current_loop_state.q_axis.integrator, 4.5)

    def test_replay_sequence_starts_reverse_target_ramp_at_lock_threshold(self):
        frontend_config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=10.0,
            startup_target_omega_e_rad_s=20.0,
            lock_blend_factor=1.0,
            observer_max_angle_step_rad=1.0,
        )
        policy_config = SensorlessStartupPolicyConfig(
            lock_confidence_threshold=0.8,
            unlock_confidence_threshold=0.2,
            lock_count_required=3,
            unlock_count_required=2,
        )
        speed_loop_config = SensorlessSpeedLoopConfig(
            speed_pi=PIConfig(kp=0.1, ki=0.5, output_limit=2.0),
            target_omega_rate_limit_e_rad_s2=50.0,
            hold_when_unlocked=True,
        )
        command_policy_config = SensorlessCurrentCommandPolicyConfig(
            unlocked_iq_limit=0.0,
            locked_iq_limit=1.5,
        )
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=0.0, ki=0.0, output_limit=20.0),
            q_axis=PIConfig(kp=0.0, ki=10.0, output_limit=20.0),
        )
        common = {
            "i_a": 0.0,
            "i_b": 0.0,
            "i_c": 0.0,
            "target_id": 0.0,
            "target_iq": 9.0,
            "target_omega_e_rad_s": -20.0,
            "vbus": 24.0,
            "dt_s": 0.1,
            "observer_omega_e_rad_s": -10.0,
        }

        result = sensorless_current_control_replay_sequence(
            [
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.2,
                    observer_confidence=0.2,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.4,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.6,
                    observer_confidence=0.9,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=0.8,
                    observer_confidence=0.95,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.0,
                    observer_confidence=0.95,
                ),
            ],
            SensorlessFrontendState(
                theta_e_rad=0.0,
                omega_e_rad_s=0.0,
                mode=MODE_STARTUP,
                locked=False,
                confidence=0.0,
            ),
            frontend_config,
            gains,
            CurrentLoopState(),
            startup_policy_config=policy_config,
            startup_policy_state=SensorlessStartupPolicyState(),
            speed_loop_config=speed_loop_config,
            speed_loop_state=SensorlessSpeedLoopState(
                speed_pi=PIState(integrator=0.5),
                target_omega_e_rad_s=20.0,
            ),
            current_command_policy_config=command_policy_config,
        )

        speed_iq = [step.speed_loop.target_iq for step in result.steps]
        speed_targets = [
            step.speed_loop.state.target_omega_e_rad_s for step in result.steps
        ]
        effective_iq = [
            step.current_command_policy.effective_target_iq for step in result.steps
        ]
        command_reasons = [
            step.current_command_policy.reason for step in result.steps
        ]
        q_integrators = [
            step.current_loop_state.q_axis.integrator for step in result.steps
        ]
        locked = [step.sensorless.locked for step in result.steps]
        lock_counts = [
            step.startup_policy.lock_candidate_count for step in result.steps
        ]

        self.assertEqual(speed_targets, [20.0, 20.0, 20.0, 15.0, 10.0])
        self.assertEqual(speed_iq, [0.0, 0.0, 0.0, 2.0, 2.0])
        self.assertEqual(effective_iq, [0.0, 0.0, 0.0, 1.5, 1.5])
        self.assertEqual(
            command_reasons,
            [
                "unlocked_current_limit",
                "unlocked_current_limit",
                "unlocked_current_limit",
                "tracking_command",
                "tracking_command",
            ],
        )
        self.assertEqual(q_integrators, [0.0, 0.0, 0.0, 1.5, 3.0])
        self.assertEqual(locked, [False, False, False, True, True])
        self.assertEqual(lock_counts, [0, 1, 2, 3, 3])
        self.assertIsNotNone(result.speed_loop_state)
        assert result.speed_loop_state is not None
        self.assertAlmostEqual(result.speed_loop_state.target_omega_e_rad_s, 10.0)
        self.assertAlmostEqual(result.speed_loop_state.speed_pi.integrator, 0.5)
        self.assertAlmostEqual(result.current_loop_state.q_axis.integrator, 3.0)

    def test_replay_sequence_rate_limits_positive_target_across_zero_to_reverse(self):
        frontend_config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=10.0,
            startup_target_omega_e_rad_s=20.0,
            lock_blend_factor=1.0,
            observer_max_angle_step_rad=1.0,
        )
        policy_config = SensorlessStartupPolicyConfig(
            lock_confidence_threshold=0.8,
            unlock_confidence_threshold=0.2,
            lock_count_required=2,
            unlock_count_required=2,
        )
        speed_loop_config = SensorlessSpeedLoopConfig(
            speed_pi=PIConfig(kp=0.1, ki=0.5, output_limit=2.0),
            target_omega_rate_limit_e_rad_s2=50.0,
            hold_when_unlocked=True,
        )
        command_policy_config = SensorlessCurrentCommandPolicyConfig(
            unlocked_iq_limit=0.0,
            locked_iq_limit=1.5,
        )
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=0.0, ki=0.0, output_limit=20.0),
            q_axis=PIConfig(kp=0.0, ki=10.0, output_limit=20.0),
        )
        common = {
            "i_a": 0.0,
            "i_b": 0.0,
            "i_c": 0.0,
            "target_id": 0.0,
            "target_iq": 9.0,
            "target_omega_e_rad_s": -20.0,
            "vbus": 24.0,
            "dt_s": 0.1,
            "observer_omega_e_rad_s": 10.0,
            "observer_confidence": 0.95,
        }

        result = sensorless_current_control_replay_sequence(
            [
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.0,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.1,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.2,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.3,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.4,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.5,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.6,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.7,
                ),
            ],
            SensorlessFrontendState(
                theta_e_rad=1.0,
                omega_e_rad_s=10.0,
                mode=MODE_TRACKING,
                locked=True,
                confidence=0.95,
            ),
            frontend_config,
            gains,
            CurrentLoopState(),
            startup_policy_config=policy_config,
            startup_policy_state=SensorlessStartupPolicyState(
                tracking_enabled=True,
                lock_candidate_count=2,
                loss_candidate_count=0,
            ),
            speed_loop_config=speed_loop_config,
            speed_loop_state=SensorlessSpeedLoopState(
                speed_pi=PIState(integrator=0.5),
                target_omega_e_rad_s=20.0,
            ),
            current_command_policy_config=command_policy_config,
        )

        speed_iq = [step.speed_loop.target_iq for step in result.steps]
        speed_integrators = [
            step.speed_loop.state.speed_pi.integrator for step in result.steps
        ]
        speed_targets = [
            step.speed_loop.state.target_omega_e_rad_s for step in result.steps
        ]
        effective_iq = [
            step.current_command_policy.effective_target_iq for step in result.steps
        ]
        q_integrators = [
            step.current_loop_state.q_axis.integrator for step in result.steps
        ]

        self.assertEqual(
            speed_targets,
            [15.0, 10.0, 5.0, 0.0, -5.0, -10.0, -15.0, -20.0],
        )
        self.assertEqual(
            speed_iq,
            [1.25, 0.75, 0.0, -1.0, -1.5, -2.0, -2.0, -2.0],
        )
        self.assertEqual(
            speed_integrators,
            [0.75, 0.75, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0],
        )
        self.assertEqual(
            effective_iq,
            [1.25, 0.75, 0.0, -1.0, -1.5, -1.5, -1.5, -1.5],
        )
        self.assertEqual(
            q_integrators,
            [1.25, 2.0, 2.0, 1.0, -0.5, -2.0, -3.5, -5.0],
        )
        self.assertIsNotNone(result.speed_loop_state)
        assert result.speed_loop_state is not None
        self.assertAlmostEqual(result.speed_loop_state.target_omega_e_rad_s, -20.0)
        self.assertAlmostEqual(result.speed_loop_state.speed_pi.integrator, 0.0)
        self.assertAlmostEqual(result.current_loop_state.q_axis.integrator, -5.0)

    def test_replay_sequence_holds_positive_to_reverse_ramp_during_loss_and_relock(self):
        frontend_config = SensorlessFrontendConfig(
            startup_accel_e_rad_s2=10.0,
            startup_target_omega_e_rad_s=20.0,
            lock_blend_factor=1.0,
            observer_max_angle_step_rad=1.0,
        )
        policy_config = SensorlessStartupPolicyConfig(
            lock_confidence_threshold=0.8,
            unlock_confidence_threshold=0.2,
            lock_count_required=2,
            unlock_count_required=2,
        )
        speed_loop_config = SensorlessSpeedLoopConfig(
            speed_pi=PIConfig(kp=0.1, ki=0.5, output_limit=2.0),
            target_omega_rate_limit_e_rad_s2=50.0,
            hold_when_unlocked=True,
        )
        command_policy_config = SensorlessCurrentCommandPolicyConfig(
            unlocked_iq_limit=0.0,
            locked_iq_limit=1.5,
        )
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=0.0, ki=0.0, output_limit=20.0),
            q_axis=PIConfig(kp=0.0, ki=10.0, output_limit=20.0),
        )
        common = {
            "i_a": 0.0,
            "i_b": 0.0,
            "i_c": 0.0,
            "target_id": 0.0,
            "target_iq": 9.0,
            "target_omega_e_rad_s": -20.0,
            "vbus": 24.0,
            "dt_s": 0.1,
            "observer_omega_e_rad_s": 10.0,
        }

        result = sensorless_current_control_replay_sequence(
            [
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.0,
                    observer_confidence=0.95,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.1,
                    observer_confidence=0.95,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.2,
                    observer_confidence=0.95,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.3,
                    observer_confidence=0.1,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.4,
                    observer_confidence=0.1,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.5,
                    observer_confidence=0.95,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.6,
                    observer_confidence=0.95,
                ),
                SensorlessCurrentLoopInputs(
                    **common,
                    observer_theta_e_rad=1.7,
                    observer_confidence=0.95,
                ),
            ],
            SensorlessFrontendState(
                theta_e_rad=1.0,
                omega_e_rad_s=10.0,
                mode=MODE_TRACKING,
                locked=True,
                confidence=0.95,
            ),
            frontend_config,
            gains,
            CurrentLoopState(),
            startup_policy_config=policy_config,
            startup_policy_state=SensorlessStartupPolicyState(
                tracking_enabled=True,
                lock_candidate_count=2,
                loss_candidate_count=0,
            ),
            speed_loop_config=speed_loop_config,
            speed_loop_state=SensorlessSpeedLoopState(
                speed_pi=PIState(integrator=0.5),
                target_omega_e_rad_s=20.0,
            ),
            current_command_policy_config=command_policy_config,
        )

        speed_iq = [step.speed_loop.target_iq for step in result.steps]
        speed_integrators = [
            step.speed_loop.state.speed_pi.integrator for step in result.steps
        ]
        speed_targets = [
            step.speed_loop.state.target_omega_e_rad_s for step in result.steps
        ]
        effective_iq = [
            step.current_command_policy.effective_target_iq for step in result.steps
        ]
        q_integrators = [
            step.current_loop_state.q_axis.integrator for step in result.steps
        ]
        locked = [step.sensorless.locked for step in result.steps]
        loss_counts = [
            step.startup_policy.loss_candidate_count for step in result.steps
        ]

        self.assertEqual(
            speed_targets,
            [15.0, 10.0, 5.0, 0.0, 0.0, 0.0, -5.0, -10.0],
        )
        self.assertEqual(
            speed_iq,
            [1.25, 0.75, 0.0, -1.0, 0.0, 0.0, -1.5, -2.0],
        )
        self.assertEqual(
            speed_integrators,
            [0.75, 0.75, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0],
        )
        self.assertEqual(
            effective_iq,
            [1.25, 0.75, 0.0, -1.0, 0.0, 0.0, -1.5, -1.5],
        )
        self.assertEqual(
            q_integrators,
            [1.25, 2.0, 2.0, 1.0, 1.0, 1.0, -0.5, -2.0],
        )
        self.assertEqual(locked, [True, True, True, True, False, False, True, True])
        self.assertEqual(loss_counts, [0, 0, 0, 1, 2, 0, 0, 0])
        self.assertIsNotNone(result.speed_loop_state)
        assert result.speed_loop_state is not None
        self.assertAlmostEqual(result.speed_loop_state.target_omega_e_rad_s, -10.0)
        self.assertAlmostEqual(result.speed_loop_state.speed_pi.integrator, 0.0)
        self.assertAlmostEqual(result.current_loop_state.q_axis.integrator, -2.0)


if __name__ == "__main__":
    unittest.main()
