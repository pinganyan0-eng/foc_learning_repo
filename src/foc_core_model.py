from __future__ import annotations

import math
from dataclasses import dataclass


SQRT3 = math.sqrt(3.0)


@dataclass(frozen=True)
class AlphaBeta:
    alpha: float
    beta: float


@dataclass(frozen=True)
class DQ:
    d: float
    q: float


@dataclass(frozen=True)
class PhaseDuty:
    a: float
    b: float
    c: float


@dataclass(frozen=True)
class SVPWMResult:
    duty: PhaseDuty
    saturated: bool
    scale: float


@dataclass(frozen=True)
class PIConfig:
    kp: float
    ki: float
    output_limit: float
    integrator_limit: float | None = None


@dataclass(frozen=True)
class PIState:
    integrator: float = 0.0


@dataclass(frozen=True)
class PIResult:
    output: float
    state: PIState
    saturated: bool


@dataclass(frozen=True)
class CurrentLoopGains:
    d_axis: PIConfig
    q_axis: PIConfig


@dataclass(frozen=True)
class CurrentLoopState:
    d_axis: PIState = PIState()
    q_axis: PIState = PIState()


@dataclass(frozen=True)
class CurrentLoopInputs:
    i_a: float
    i_b: float
    i_c: float
    theta_e_rad: float
    target_id: float
    target_iq: float
    vbus: float
    dt_s: float


@dataclass(frozen=True)
class CurrentLoopResult:
    current_ab: AlphaBeta
    current_dq: DQ
    voltage_dq: DQ
    voltage_ab: AlphaBeta
    svpwm: SVPWMResult
    state: CurrentLoopState


def clamp(value: float, lower: float, upper: float) -> float:
    if lower > upper:
        raise ValueError("lower must be <= upper")
    return max(lower, min(upper, value))


def clarke_abc(i_a: float, i_b: float, i_c: float) -> AlphaBeta:
    """Amplitude-invariant Clarke transform for a three-shunt current set."""

    alpha = (2.0 * i_a - i_b - i_c) / 3.0
    beta = (i_b - i_c) / SQRT3
    return AlphaBeta(alpha=alpha, beta=beta)


def inverse_clarke(alpha: float, beta: float) -> tuple[float, float, float]:
    a = alpha
    b = -0.5 * alpha + (SQRT3 / 2.0) * beta
    c = -0.5 * alpha - (SQRT3 / 2.0) * beta
    return a, b, c


def park(alpha: float, beta: float, theta_e_rad: float) -> DQ:
    cos_t = math.cos(theta_e_rad)
    sin_t = math.sin(theta_e_rad)
    return DQ(
        d=alpha * cos_t + beta * sin_t,
        q=-alpha * sin_t + beta * cos_t,
    )


def inverse_park(d_axis: float, q_axis: float, theta_e_rad: float) -> AlphaBeta:
    cos_t = math.cos(theta_e_rad)
    sin_t = math.sin(theta_e_rad)
    return AlphaBeta(
        alpha=d_axis * cos_t - q_axis * sin_t,
        beta=d_axis * sin_t + q_axis * cos_t,
    )


def svpwm(alpha: float, beta: float, vbus: float) -> SVPWMResult:
    """Host-side SVPWM-style zero-sequence injection; not a timer driver."""

    if vbus <= 0.0:
        raise ValueError("vbus must be positive")

    a, b, c = inverse_clarke(alpha, beta)
    phase_span = max(a, b, c) - min(a, b, c)
    saturated = phase_span > vbus
    scale = 1.0

    if saturated:
        scale = vbus / phase_span
        a *= scale
        b *= scale
        c *= scale

    offset = -0.5 * (max(a, b, c) + min(a, b, c))
    duty_a = clamp(0.5 + (a + offset) / vbus, 0.0, 1.0)
    duty_b = clamp(0.5 + (b + offset) / vbus, 0.0, 1.0)
    duty_c = clamp(0.5 + (c + offset) / vbus, 0.0, 1.0)

    return SVPWMResult(
        duty=PhaseDuty(a=duty_a, b=duty_b, c=duty_c),
        saturated=saturated,
        scale=scale,
    )


def _validate_pi(config: PIConfig, dt_s: float) -> None:
    if dt_s < 0.0:
        raise ValueError("dt_s must be non-negative")
    if config.output_limit <= 0.0:
        raise ValueError("output_limit must be positive")
    if config.integrator_limit is not None and config.integrator_limit <= 0.0:
        raise ValueError("integrator_limit must be positive")


def pi_step(error: float, dt_s: float, state: PIState, config: PIConfig) -> PIResult:
    _validate_pi(config, dt_s)

    integrator_limit = (
        config.output_limit
        if config.integrator_limit is None
        else config.integrator_limit
    )
    previous_integrator = clamp(
        state.integrator,
        -integrator_limit,
        integrator_limit,
    )
    candidate_integrator = clamp(
        previous_integrator + config.ki * error * dt_s,
        -integrator_limit,
        integrator_limit,
    )

    unsaturated = config.kp * error + candidate_integrator
    output = clamp(unsaturated, -config.output_limit, config.output_limit)
    saturated = output != unsaturated

    if saturated and (
        (unsaturated > config.output_limit and error > 0.0)
        or (unsaturated < -config.output_limit and error < 0.0)
    ):
        candidate_integrator = previous_integrator
        unsaturated = config.kp * error + candidate_integrator
        output = clamp(unsaturated, -config.output_limit, config.output_limit)

    return PIResult(
        output=output,
        state=PIState(integrator=candidate_integrator),
        saturated=output != unsaturated,
    )


def current_control_step(
    inputs: CurrentLoopInputs,
    gains: CurrentLoopGains,
    state: CurrentLoopState,
) -> CurrentLoopResult:
    current_ab = clarke_abc(inputs.i_a, inputs.i_b, inputs.i_c)
    current_dq = park(current_ab.alpha, current_ab.beta, inputs.theta_e_rad)

    d_result = pi_step(
        error=inputs.target_id - current_dq.d,
        dt_s=inputs.dt_s,
        state=state.d_axis,
        config=gains.d_axis,
    )
    q_result = pi_step(
        error=inputs.target_iq - current_dq.q,
        dt_s=inputs.dt_s,
        state=state.q_axis,
        config=gains.q_axis,
    )

    voltage_dq = DQ(d=d_result.output, q=q_result.output)
    voltage_ab = inverse_park(voltage_dq.d, voltage_dq.q, inputs.theta_e_rad)
    pwm = svpwm(voltage_ab.alpha, voltage_ab.beta, inputs.vbus)

    return CurrentLoopResult(
        current_ab=current_ab,
        current_dq=current_dq,
        voltage_dq=voltage_dq,
        voltage_ab=voltage_ab,
        svpwm=pwm,
        state=CurrentLoopState(d_axis=d_result.state, q_axis=q_result.state),
    )
