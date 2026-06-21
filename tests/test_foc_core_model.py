import math
import unittest

from src.foc_core_model import (
    CurrentLoopGains,
    CurrentLoopInputs,
    CurrentLoopState,
    PIConfig,
    PIState,
    clarke_abc,
    current_control_step,
    inverse_clarke,
    inverse_park,
    park,
    pi_step,
    svpwm,
)


class FocTransformTests(unittest.TestCase):
    def assertAlmostTuple(self, actual, expected, places=12):
        for left, right in zip(actual, expected):
            self.assertAlmostEqual(left, right, places=places)

    def test_clarke_maps_balanced_a_axis_current_to_alpha(self):
        ab = clarke_abc(1.0, -0.5, -0.5)

        self.assertAlmostEqual(ab.alpha, 1.0)
        self.assertAlmostEqual(ab.beta, 0.0)

    def test_inverse_clarke_round_trips_alpha_beta_when_sum_is_zero(self):
        alpha = 0.8
        beta = -0.3

        phase = inverse_clarke(alpha, beta)
        ab = clarke_abc(*phase)

        self.assertAlmostEqual(sum(phase), 0.0)
        self.assertAlmostEqual(ab.alpha, alpha)
        self.assertAlmostEqual(ab.beta, beta)

    def test_park_and_inverse_park_are_inverse_operations(self):
        theta = 1.2
        ab = inverse_park(d_axis=0.4, q_axis=-0.7, theta_e_rad=theta)
        dq = park(ab.alpha, ab.beta, theta)

        self.assertAlmostEqual(dq.d, 0.4)
        self.assertAlmostEqual(dq.q, -0.7)

    def test_park_sign_convention_for_positive_quarter_turn(self):
        dq = park(alpha=1.0, beta=0.0, theta_e_rad=math.pi / 2.0)

        self.assertAlmostEqual(dq.d, 0.0, places=12)
        self.assertAlmostEqual(dq.q, -1.0, places=12)


class SvpwmTests(unittest.TestCase):
    def test_zero_vector_centers_all_duties(self):
        result = svpwm(alpha=0.0, beta=0.0, vbus=24.0)

        self.assertFalse(result.saturated)
        self.assertEqual(result.scale, 1.0)
        self.assertAlmostEqual(result.duty.a, 0.5)
        self.assertAlmostEqual(result.duty.b, 0.5)
        self.assertAlmostEqual(result.duty.c, 0.5)

    def test_zero_sequence_keeps_duties_inside_range(self):
        result = svpwm(alpha=6.0, beta=0.0, vbus=24.0)

        self.assertFalse(result.saturated)
        self.assertAlmostEqual(result.duty.a, 0.6875)
        self.assertAlmostEqual(result.duty.b, 0.3125)
        self.assertAlmostEqual(result.duty.c, 0.3125)

    def test_large_vector_is_scaled_instead_of_exceeding_duty_limits(self):
        result = svpwm(alpha=30.0, beta=0.0, vbus=24.0)

        self.assertTrue(result.saturated)
        self.assertLess(result.scale, 1.0)
        for duty in (result.duty.a, result.duty.b, result.duty.c):
            self.assertGreaterEqual(duty, 0.0)
            self.assertLessEqual(duty, 1.0)

    def test_vbus_must_be_positive(self):
        with self.assertRaises(ValueError):
            svpwm(alpha=0.0, beta=0.0, vbus=0.0)


class PiControllerTests(unittest.TestCase):
    def test_pi_step_combines_proportional_and_integral_terms(self):
        result = pi_step(
            error=2.0,
            dt_s=0.1,
            state=PIState(),
            config=PIConfig(kp=1.0, ki=0.5, output_limit=10.0),
        )

        self.assertAlmostEqual(result.output, 2.1)
        self.assertAlmostEqual(result.state.integrator, 0.1)
        self.assertFalse(result.saturated)

    def test_pi_anti_windup_holds_integrator_when_saturated_same_direction(self):
        state = PIState()
        config = PIConfig(kp=10.0, ki=5.0, output_limit=1.0)

        first = pi_step(error=1.0, dt_s=0.1, state=state, config=config)
        second = pi_step(error=1.0, dt_s=0.1, state=first.state, config=config)

        self.assertAlmostEqual(first.output, 1.0)
        self.assertAlmostEqual(second.output, 1.0)
        self.assertAlmostEqual(first.state.integrator, 0.0)
        self.assertAlmostEqual(second.state.integrator, 0.0)

    def test_pi_accepts_integrator_when_error_reduces_existing_saturation(self):
        config = PIConfig(kp=0.0, ki=10.0, output_limit=1.0)
        result = pi_step(
            error=-1.0,
            dt_s=0.05,
            state=PIState(integrator=1.0),
            config=config,
        )

        self.assertAlmostEqual(result.output, 0.5)
        self.assertAlmostEqual(result.state.integrator, 0.5)
        self.assertFalse(result.saturated)

    def test_pi_clamps_externally_supplied_prior_integrator(self):
        config = PIConfig(kp=10.0, ki=5.0, output_limit=1.0)
        result = pi_step(
            error=1.0,
            dt_s=0.1,
            state=PIState(integrator=100.0),
            config=config,
        )

        self.assertAlmostEqual(result.output, 1.0)
        self.assertAlmostEqual(result.state.integrator, 1.0)
        self.assertTrue(result.saturated)


class CurrentLoopTests(unittest.TestCase):
    def test_zero_error_outputs_centered_pwm(self):
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=1.0, ki=0.0, output_limit=6.0),
            q_axis=PIConfig(kp=1.0, ki=0.0, output_limit=6.0),
        )
        inputs = CurrentLoopInputs(
            i_a=0.0,
            i_b=0.0,
            i_c=0.0,
            theta_e_rad=0.0,
            target_id=0.0,
            target_iq=0.0,
            vbus=24.0,
            dt_s=0.0001,
        )

        result = current_control_step(inputs, gains, CurrentLoopState())

        self.assertAlmostEqual(result.voltage_dq.d, 0.0)
        self.assertAlmostEqual(result.voltage_dq.q, 0.0)
        self.assertAlmostEqual(result.svpwm.duty.a, 0.5)
        self.assertAlmostEqual(result.svpwm.duty.b, 0.5)
        self.assertAlmostEqual(result.svpwm.duty.c, 0.5)

    def test_q_axis_current_request_produces_nonzero_voltage_vector(self):
        gains = CurrentLoopGains(
            d_axis=PIConfig(kp=1.0, ki=0.0, output_limit=6.0),
            q_axis=PIConfig(kp=1.0, ki=0.0, output_limit=6.0),
        )
        inputs = CurrentLoopInputs(
            i_a=0.0,
            i_b=0.0,
            i_c=0.0,
            theta_e_rad=0.0,
            target_id=0.0,
            target_iq=2.0,
            vbus=24.0,
            dt_s=0.0001,
        )

        result = current_control_step(inputs, gains, CurrentLoopState())

        self.assertAlmostEqual(result.voltage_dq.d, 0.0)
        self.assertAlmostEqual(result.voltage_dq.q, 2.0)
        self.assertFalse(result.svpwm.saturated)
        self.assertAlmostEqual(result.svpwm.duty.a, 0.5)
        self.assertAlmostEqual(
            result.svpwm.duty.b,
            0.5 + math.sqrt(3.0) / 24.0,
        )
        self.assertAlmostEqual(
            result.svpwm.duty.c,
            0.5 - math.sqrt(3.0) / 24.0,
        )
        self.assertGreater(result.svpwm.duty.b, result.svpwm.duty.a)
        self.assertGreater(result.svpwm.duty.a, result.svpwm.duty.c)


if __name__ == "__main__":
    unittest.main()
