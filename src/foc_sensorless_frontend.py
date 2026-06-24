from __future__ import annotations

import math
from collections.abc import Iterable
from dataclasses import dataclass

from src.foc_core_model import (
    AlphaBeta,
    CurrentLoopGains,
    CurrentLoopInputs,
    CurrentLoopResult,
    CurrentLoopState,
    PIConfig,
    PIResult,
    PIState,
    clarke_abc,
    current_control_step,
    pi_step,
)


MODE_STARTUP = "startup"
MODE_TRACKING = "tracking"


def normalize_angle_rad(theta_rad: float) -> float:
    wrapped = math.fmod(theta_rad, 2.0 * math.pi)
    if wrapped < 0.0:
        wrapped += 2.0 * math.pi
    return wrapped


@dataclass(frozen=True)
class SensorlessFrontendConfig:
    startup_accel_e_rad_s2: float
    startup_target_omega_e_rad_s: float
    lock_blend_factor: float
    observer_min_confidence_for_lock: float = 0.8
    observer_max_angle_step_rad: float = math.pi / 2.0


@dataclass(frozen=True)
class SensorlessObserverConfig:
    stator_resistance_ohm: float
    bemf_confidence_full_scale_v: float
    bemf_to_theta_offset_rad: float = -math.pi / 2.0
    max_angle_step_rad: float = math.pi / 2.0
    confidence_rise_filter: float = 1.0
    confidence_decay_filter: float = 1.0
    omega_filter: float = 1.0


@dataclass(frozen=True)
class SensorlessStartupPolicyConfig:
    lock_confidence_threshold: float
    unlock_confidence_threshold: float
    lock_count_required: int = 1
    unlock_count_required: int = 1


@dataclass(frozen=True)
class SensorlessSpeedLoopConfig:
    speed_pi: PIConfig
    target_omega_rate_limit_e_rad_s2: float | None = None
    hold_when_unlocked: bool = False


@dataclass(frozen=True)
class SensorlessCurrentCommandPolicyConfig:
    unlocked_iq_limit: float = 0.0
    locked_iq_limit: float | None = None


@dataclass(frozen=True)
class SensorlessFrontendInputs:
    i_alpha: float
    i_beta: float
    v_alpha: float
    v_beta: float
    dt_s: float
    observer_theta_e_rad: float | None = None
    observer_omega_e_rad_s: float | None = None
    observer_confidence: float = 0.0
    observer_lock_override: bool | None = None


@dataclass(frozen=True)
class SensorlessFrontendState:
    theta_e_rad: float = 0.0
    omega_e_rad_s: float = 0.0
    mode: str = MODE_STARTUP
    locked: bool = False
    confidence: float = 0.0


@dataclass(frozen=True)
class SensorlessObserverState:
    theta_e_rad: float = 0.0
    omega_e_rad_s: float = 0.0
    confidence: float = 0.0


@dataclass(frozen=True)
class SensorlessStartupPolicyState:
    tracking_enabled: bool = False
    lock_candidate_count: int = 0
    loss_candidate_count: int = 0


@dataclass(frozen=True)
class SensorlessSpeedLoopState:
    speed_pi: PIState = PIState()
    target_omega_e_rad_s: float = 0.0


@dataclass(frozen=True)
class SensorlessFrontendResult:
    theta_e_rad: float
    omega_e_rad_s: float
    mode: str
    locked: bool
    confidence: float


@dataclass(frozen=True)
class SensorlessObserverResult:
    theta_e_rad: float
    omega_e_rad_s: float
    confidence: float
    back_emf_ab: AlphaBeta
    back_emf_magnitude: float
    state: SensorlessObserverState


@dataclass(frozen=True)
class SensorlessStartupPolicyResult:
    tracking_enabled: bool
    lock_candidate: bool
    loss_candidate: bool
    lock_candidate_count: int
    loss_candidate_count: int
    frontend_lock_override: bool
    state: SensorlessStartupPolicyState


@dataclass(frozen=True)
class SensorlessSpeedLoopResult:
    target_omega_e_rad_s: float
    measured_omega_e_rad_s: float
    target_iq: float
    speed_error_e_rad_s: float
    saturated: bool
    state: SensorlessSpeedLoopState
    pi: PIResult


@dataclass(frozen=True)
class SensorlessCurrentCommandPolicyResult:
    requested_target_iq: float
    effective_target_iq: float
    locked: bool
    limited: bool
    reason: str


@dataclass(frozen=True)
class SensorlessCurrentLoopInputs:
    i_a: float
    i_b: float
    i_c: float
    target_id: float
    target_iq: float
    vbus: float
    dt_s: float
    v_alpha: float = 0.0
    v_beta: float = 0.0
    observer_theta_e_rad: float | None = None
    observer_omega_e_rad_s: float | None = None
    observer_confidence: float = 0.0
    observer_lock_override: bool | None = None
    target_omega_e_rad_s: float | None = None


@dataclass(frozen=True)
class SensorlessCurrentLoopResult:
    sensorless: SensorlessFrontendResult
    current_loop: CurrentLoopResult
    state: SensorlessFrontendState
    current_loop_state: CurrentLoopState
    observer: SensorlessObserverResult | None = None
    startup_policy: SensorlessStartupPolicyResult | None = None
    speed_loop: SensorlessSpeedLoopResult | None = None
    current_command_policy: SensorlessCurrentCommandPolicyResult | None = None


@dataclass(frozen=True)
class SensorlessReplayResult:
    steps: tuple[SensorlessCurrentLoopResult, ...]
    state: SensorlessFrontendState
    current_loop_state: CurrentLoopState
    observer_state: SensorlessObserverState | None = None
    startup_policy_state: SensorlessStartupPolicyState | None = None
    speed_loop_state: SensorlessSpeedLoopState | None = None


def _shortest_angle_delta_rad(target_rad: float, current_rad: float) -> float:
    delta = normalize_angle_rad(target_rad - current_rad)
    if delta > math.pi:
        delta -= 2.0 * math.pi
    return delta


def _validate_config(config: SensorlessFrontendConfig) -> None:
    if config.startup_accel_e_rad_s2 < 0.0:
        raise ValueError("startup_accel_e_rad_s2 must be non-negative")
    if config.startup_target_omega_e_rad_s < 0.0:
        raise ValueError("startup_target_omega_e_rad_s must be non-negative")
    if not 0.0 <= config.lock_blend_factor <= 1.0:
        raise ValueError("lock_blend_factor must be within [0, 1]")
    if not 0.0 <= config.observer_min_confidence_for_lock <= 1.0:
        raise ValueError("observer_min_confidence_for_lock must be within [0, 1]")
    if config.observer_max_angle_step_rad <= 0.0:
        raise ValueError("observer_max_angle_step_rad must be positive")


def _validate_inputs(inputs: SensorlessFrontendInputs) -> None:
    if inputs.dt_s < 0.0:
        raise ValueError("dt_s must be non-negative")
    if not 0.0 <= inputs.observer_confidence <= 1.0:
        raise ValueError("observer_confidence must be within [0, 1]")


def _validate_observer_config(config: SensorlessObserverConfig) -> None:
    if config.stator_resistance_ohm < 0.0:
        raise ValueError("stator_resistance_ohm must be non-negative")
    if config.bemf_confidence_full_scale_v <= 0.0:
        raise ValueError("bemf_confidence_full_scale_v must be positive")
    if config.max_angle_step_rad <= 0.0:
        raise ValueError("max_angle_step_rad must be positive")
    if not 0.0 <= config.confidence_rise_filter <= 1.0:
        raise ValueError("confidence_rise_filter must be within [0, 1]")
    if not 0.0 <= config.confidence_decay_filter <= 1.0:
        raise ValueError("confidence_decay_filter must be within [0, 1]")
    if not 0.0 <= config.omega_filter <= 1.0:
        raise ValueError("omega_filter must be within [0, 1]")


def _validate_startup_policy_config(config: SensorlessStartupPolicyConfig) -> None:
    if not 0.0 <= config.lock_confidence_threshold <= 1.0:
        raise ValueError("lock_confidence_threshold must be within [0, 1]")
    if not 0.0 <= config.unlock_confidence_threshold <= 1.0:
        raise ValueError("unlock_confidence_threshold must be within [0, 1]")
    if config.unlock_confidence_threshold > config.lock_confidence_threshold:
        raise ValueError("unlock_confidence_threshold must be <= lock_confidence_threshold")
    if config.lock_count_required <= 0:
        raise ValueError("lock_count_required must be positive")
    if config.unlock_count_required <= 0:
        raise ValueError("unlock_count_required must be positive")


def _validate_speed_loop_config(config: SensorlessSpeedLoopConfig) -> None:
    if (
        config.target_omega_rate_limit_e_rad_s2 is not None
        and config.target_omega_rate_limit_e_rad_s2 <= 0.0
    ):
        raise ValueError("target_omega_rate_limit_e_rad_s2 must be positive")


def _validate_current_command_policy_config(
    config: SensorlessCurrentCommandPolicyConfig,
) -> None:
    if config.unlocked_iq_limit < 0.0:
        raise ValueError("unlocked_iq_limit must be non-negative")
    if config.locked_iq_limit is not None and config.locked_iq_limit < 0.0:
        raise ValueError("locked_iq_limit must be non-negative")


def _ramp_target_omega(
    *,
    requested_target_omega_e_rad_s: float,
    current_target_omega_e_rad_s: float,
    dt_s: float,
    rate_limit_e_rad_s2: float | None,
) -> float:
    if dt_s < 0.0:
        raise ValueError("dt_s must be non-negative")
    if rate_limit_e_rad_s2 is None:
        return requested_target_omega_e_rad_s

    max_delta = rate_limit_e_rad_s2 * dt_s
    delta = max(
        -max_delta,
        min(max_delta, requested_target_omega_e_rad_s - current_target_omega_e_rad_s),
    )
    return current_target_omega_e_rad_s + delta


def back_emf_observer_step(
    inputs: SensorlessFrontendInputs,
    state: SensorlessObserverState,
    config: SensorlessObserverConfig,
) -> SensorlessObserverResult:
    """Host-side back-EMF angle stub; not an MCSDK SMO/PLL implementation."""

    _validate_inputs(inputs)
    _validate_observer_config(config)

    bemf_alpha = inputs.v_alpha - config.stator_resistance_ohm * inputs.i_alpha
    bemf_beta = inputs.v_beta - config.stator_resistance_ohm * inputs.i_beta
    magnitude = math.hypot(bemf_alpha, bemf_beta)
    raw_confidence = min(1.0, magnitude / config.bemf_confidence_full_scale_v)

    confidence_filter = (
        config.confidence_rise_filter
        if raw_confidence >= state.confidence
        else config.confidence_decay_filter
    )
    confidence = state.confidence + (raw_confidence - state.confidence) * confidence_filter

    if magnitude > 0.0:
        candidate_theta = normalize_angle_rad(
            math.atan2(bemf_beta, bemf_alpha) + config.bemf_to_theta_offset_rad
        )
        delta = _shortest_angle_delta_rad(candidate_theta, state.theta_e_rad)
        limited_delta = max(
            -config.max_angle_step_rad,
            min(config.max_angle_step_rad, delta),
        )
        theta = normalize_angle_rad(state.theta_e_rad + limited_delta)
        raw_omega = (
            state.omega_e_rad_s
            if inputs.dt_s == 0.0
            else limited_delta / inputs.dt_s
        )
    else:
        theta = normalize_angle_rad(state.theta_e_rad)
        raw_omega = state.omega_e_rad_s

    omega = (
        (1.0 - config.omega_filter) * state.omega_e_rad_s
        + config.omega_filter * raw_omega
    )
    next_state = SensorlessObserverState(
        theta_e_rad=theta,
        omega_e_rad_s=omega,
        confidence=confidence,
    )

    return SensorlessObserverResult(
        theta_e_rad=theta,
        omega_e_rad_s=omega,
        confidence=confidence,
        back_emf_ab=AlphaBeta(alpha=bemf_alpha, beta=bemf_beta),
        back_emf_magnitude=magnitude,
        state=next_state,
    )


def sensorless_startup_policy_step(
    observer_confidence: float,
    state: SensorlessStartupPolicyState,
    config: SensorlessStartupPolicyConfig,
) -> SensorlessStartupPolicyResult:
    """Host-side lock/loss hysteresis policy; not firmware startup logic."""

    if not 0.0 <= observer_confidence <= 1.0:
        raise ValueError("observer_confidence must be within [0, 1]")
    _validate_startup_policy_config(config)

    lock_candidate = observer_confidence >= config.lock_confidence_threshold
    loss_candidate = observer_confidence <= config.unlock_confidence_threshold

    if state.tracking_enabled:
        loss_count = state.loss_candidate_count + 1 if loss_candidate else 0
        tracking_enabled = loss_count < config.unlock_count_required
        lock_count = config.lock_count_required if tracking_enabled else 0
    else:
        loss_count = 0
        lock_count = state.lock_candidate_count + 1 if lock_candidate else 0
        tracking_enabled = lock_count >= config.lock_count_required
        if tracking_enabled:
            lock_count = config.lock_count_required

    next_state = SensorlessStartupPolicyState(
        tracking_enabled=tracking_enabled,
        lock_candidate_count=lock_count,
        loss_candidate_count=loss_count,
    )

    return SensorlessStartupPolicyResult(
        tracking_enabled=tracking_enabled,
        lock_candidate=lock_candidate,
        loss_candidate=loss_candidate,
        lock_candidate_count=lock_count,
        loss_candidate_count=loss_count,
        frontend_lock_override=tracking_enabled,
        state=next_state,
    )


def sensorless_speed_loop_step(
    *,
    target_omega_e_rad_s: float,
    measured_omega_e_rad_s: float,
    dt_s: float,
    state: SensorlessSpeedLoopState,
    config: SensorlessSpeedLoopConfig,
    enabled: bool = True,
) -> SensorlessSpeedLoopResult:
    """Host-side speed outer loop; not MCSDK speed-loop firmware."""

    _validate_speed_loop_config(config)

    if not enabled and config.hold_when_unlocked:
        pi_result = PIResult(
            output=0.0,
            state=state.speed_pi,
            saturated=False,
        )
        return SensorlessSpeedLoopResult(
            target_omega_e_rad_s=state.target_omega_e_rad_s,
            measured_omega_e_rad_s=measured_omega_e_rad_s,
            target_iq=0.0,
            speed_error_e_rad_s=0.0,
            saturated=False,
            state=state,
            pi=pi_result,
        )

    ramped_target = _ramp_target_omega(
        requested_target_omega_e_rad_s=target_omega_e_rad_s,
        current_target_omega_e_rad_s=state.target_omega_e_rad_s,
        dt_s=dt_s,
        rate_limit_e_rad_s2=config.target_omega_rate_limit_e_rad_s2,
    )
    error = ramped_target - measured_omega_e_rad_s
    pi_result = pi_step(
        error=error,
        dt_s=dt_s,
        state=state.speed_pi,
        config=config.speed_pi,
    )
    next_state = SensorlessSpeedLoopState(
        speed_pi=pi_result.state,
        target_omega_e_rad_s=ramped_target,
    )

    return SensorlessSpeedLoopResult(
        target_omega_e_rad_s=ramped_target,
        measured_omega_e_rad_s=measured_omega_e_rad_s,
        target_iq=pi_result.output,
        speed_error_e_rad_s=error,
        saturated=pi_result.saturated,
        state=next_state,
        pi=pi_result,
    )


def sensorless_current_command_policy_step(
    *,
    requested_target_iq: float,
    locked: bool,
    config: SensorlessCurrentCommandPolicyConfig,
) -> SensorlessCurrentCommandPolicyResult:
    """Host-side lock-aware current command policy; not firmware protection."""

    _validate_current_command_policy_config(config)

    limit = config.locked_iq_limit if locked else config.unlocked_iq_limit
    reason = "tracking_command" if locked else "unlocked_current_limit"

    if limit is None:
        effective_target_iq = requested_target_iq
    else:
        effective_target_iq = max(-limit, min(limit, requested_target_iq))

    return SensorlessCurrentCommandPolicyResult(
        requested_target_iq=requested_target_iq,
        effective_target_iq=effective_target_iq,
        locked=locked,
        limited=effective_target_iq != requested_target_iq,
        reason=reason,
    )


def sensorless_startup_step(
    inputs: SensorlessFrontendInputs,
    state: SensorlessFrontendState,
    config: SensorlessFrontendConfig,
) -> SensorlessFrontendResult:
    next_omega = min(
        config.startup_target_omega_e_rad_s,
        state.omega_e_rad_s + config.startup_accel_e_rad_s2 * inputs.dt_s,
    )
    next_theta = normalize_angle_rad(state.theta_e_rad + next_omega * inputs.dt_s)
    return SensorlessFrontendResult(
        theta_e_rad=next_theta,
        omega_e_rad_s=next_omega,
        mode=MODE_STARTUP,
        locked=False,
        confidence=0.0,
    )


def sensorless_observer_contract_step(
    inputs: SensorlessFrontendInputs,
    state: SensorlessFrontendState,
    config: SensorlessFrontendConfig,
) -> SensorlessFrontendResult:
    observer_theta = state.theta_e_rad
    if inputs.observer_theta_e_rad is not None:
        delta = _shortest_angle_delta_rad(inputs.observer_theta_e_rad, state.theta_e_rad)
        delta = max(
            -config.observer_max_angle_step_rad,
            min(config.observer_max_angle_step_rad, delta),
        )
        observer_theta = normalize_angle_rad(state.theta_e_rad + delta)

    observer_omega = (
        state.omega_e_rad_s
        if inputs.observer_omega_e_rad_s is None
        else inputs.observer_omega_e_rad_s
    )
    confidence = inputs.observer_confidence
    locked = (
        confidence >= config.observer_min_confidence_for_lock
        if inputs.observer_lock_override is None
        else inputs.observer_lock_override
    )
    mode = MODE_TRACKING if locked else MODE_STARTUP

    if locked:
        delta = _shortest_angle_delta_rad(observer_theta, state.theta_e_rad)
        theta = normalize_angle_rad(state.theta_e_rad + config.lock_blend_factor * delta)
        omega = (
            (1.0 - config.lock_blend_factor) * state.omega_e_rad_s
            + config.lock_blend_factor * observer_omega
        )
    else:
        theta = observer_theta
        omega = observer_omega

    return SensorlessFrontendResult(
        theta_e_rad=theta,
        omega_e_rad_s=omega,
        mode=mode,
        locked=locked,
        confidence=confidence,
    )


def sensorless_frontend_step(
    inputs: SensorlessFrontendInputs,
    state: SensorlessFrontendState,
    config: SensorlessFrontendConfig,
) -> SensorlessFrontendResult:
    _validate_config(config)
    _validate_inputs(inputs)

    observer = sensorless_observer_contract_step(inputs, state, config)
    if observer.locked:
        return observer

    return sensorless_startup_step(inputs, state, config)


def startup_state_from_result(result: SensorlessFrontendResult) -> SensorlessFrontendState:
    return SensorlessFrontendState(
        theta_e_rad=result.theta_e_rad,
        omega_e_rad_s=result.omega_e_rad_s,
        mode=result.mode,
        locked=result.locked,
        confidence=result.confidence,
    )


def sensorless_current_control_step(
    sensorless_inputs: SensorlessCurrentLoopInputs,
    sensorless_state: SensorlessFrontendState,
    sensorless_config: SensorlessFrontendConfig,
    current_loop_gains: CurrentLoopGains,
    current_loop_state: CurrentLoopState,
    observer_config: SensorlessObserverConfig | None = None,
    observer_state: SensorlessObserverState | None = None,
    startup_policy_config: SensorlessStartupPolicyConfig | None = None,
    startup_policy_state: SensorlessStartupPolicyState | None = None,
    speed_loop_config: SensorlessSpeedLoopConfig | None = None,
    speed_loop_state: SensorlessSpeedLoopState | None = None,
    current_command_policy_config: SensorlessCurrentCommandPolicyConfig | None = None,
) -> SensorlessCurrentLoopResult:
    observer_result = None
    observer_theta = sensorless_inputs.observer_theta_e_rad
    observer_omega = sensorless_inputs.observer_omega_e_rad_s
    observer_confidence = sensorless_inputs.observer_confidence
    observer_lock_override = sensorless_inputs.observer_lock_override

    if observer_config is not None:
        current_ab = clarke_abc(
            sensorless_inputs.i_a,
            sensorless_inputs.i_b,
            sensorless_inputs.i_c,
        )
        observer_result = back_emf_observer_step(
            SensorlessFrontendInputs(
                i_alpha=current_ab.alpha,
                i_beta=current_ab.beta,
                v_alpha=sensorless_inputs.v_alpha,
                v_beta=sensorless_inputs.v_beta,
                dt_s=sensorless_inputs.dt_s,
                observer_confidence=sensorless_inputs.observer_confidence,
            ),
            SensorlessObserverState() if observer_state is None else observer_state,
            observer_config,
        )
        if observer_theta is None:
            observer_theta = observer_result.theta_e_rad
            observer_confidence = max(observer_confidence, observer_result.confidence)
        if observer_omega is None:
            observer_omega = observer_result.omega_e_rad_s
    else:
        current_ab = AlphaBeta(alpha=0.0, beta=0.0)

    startup_policy_result = None
    if startup_policy_config is not None:
        startup_policy_result = sensorless_startup_policy_step(
            observer_confidence,
            (
                SensorlessStartupPolicyState()
                if startup_policy_state is None
                else startup_policy_state
            ),
            startup_policy_config,
        )
        observer_lock_override = startup_policy_result.frontend_lock_override

    frontend = sensorless_frontend_step(
        SensorlessFrontendInputs(
            i_alpha=current_ab.alpha,
            i_beta=current_ab.beta,
            v_alpha=sensorless_inputs.v_alpha,
            v_beta=sensorless_inputs.v_beta,
            dt_s=sensorless_inputs.dt_s,
            observer_theta_e_rad=observer_theta,
            observer_omega_e_rad_s=observer_omega,
            observer_confidence=observer_confidence,
            observer_lock_override=observer_lock_override,
        ),
        sensorless_state,
        sensorless_config,
    )

    speed_loop_result = None
    target_iq = sensorless_inputs.target_iq
    if speed_loop_config is not None:
        if sensorless_inputs.target_omega_e_rad_s is None:
            raise ValueError("target_omega_e_rad_s is required when speed_loop_config is provided")
        speed_loop_result = sensorless_speed_loop_step(
            target_omega_e_rad_s=sensorless_inputs.target_omega_e_rad_s,
            measured_omega_e_rad_s=frontend.omega_e_rad_s,
            dt_s=sensorless_inputs.dt_s,
            state=(
                SensorlessSpeedLoopState()
                if speed_loop_state is None
                else speed_loop_state
            ),
            config=speed_loop_config,
            enabled=frontend.locked,
        )
        target_iq = speed_loop_result.target_iq

    current_command_policy_result = None
    if current_command_policy_config is not None:
        current_command_policy_result = sensorless_current_command_policy_step(
            requested_target_iq=target_iq,
            locked=frontend.locked,
            config=current_command_policy_config,
        )
        target_iq = current_command_policy_result.effective_target_iq

    loop_result = current_control_step(
        CurrentLoopInputs(
            i_a=sensorless_inputs.i_a,
            i_b=sensorless_inputs.i_b,
            i_c=sensorless_inputs.i_c,
            theta_e_rad=frontend.theta_e_rad,
            target_id=sensorless_inputs.target_id,
            target_iq=target_iq,
            vbus=sensorless_inputs.vbus,
            dt_s=sensorless_inputs.dt_s,
        ),
        current_loop_gains,
        current_loop_state,
    )

    return SensorlessCurrentLoopResult(
        sensorless=frontend,
        current_loop=loop_result,
        state=startup_state_from_result(frontend),
        current_loop_state=loop_result.state,
        observer=observer_result,
        startup_policy=startup_policy_result,
        speed_loop=speed_loop_result,
        current_command_policy=current_command_policy_result,
    )


def sensorless_current_control_replay_sequence(
    sensorless_inputs: Iterable[SensorlessCurrentLoopInputs],
    sensorless_state: SensorlessFrontendState,
    sensorless_config: SensorlessFrontendConfig,
    current_loop_gains: CurrentLoopGains,
    current_loop_state: CurrentLoopState,
    observer_config: SensorlessObserverConfig | None = None,
    observer_state: SensorlessObserverState | None = None,
    startup_policy_config: SensorlessStartupPolicyConfig | None = None,
    startup_policy_state: SensorlessStartupPolicyState | None = None,
    speed_loop_config: SensorlessSpeedLoopConfig | None = None,
    speed_loop_state: SensorlessSpeedLoopState | None = None,
    current_command_policy_config: SensorlessCurrentCommandPolicyConfig | None = None,
) -> SensorlessReplayResult:
    """Replay host-side sensorless steps with explicit state handoff."""

    next_sensorless_state = sensorless_state
    next_current_loop_state = current_loop_state
    next_observer_state = (
        None
        if observer_config is None
        else SensorlessObserverState() if observer_state is None else observer_state
    )
    next_startup_policy_state = (
        None
        if startup_policy_config is None
        else (
            SensorlessStartupPolicyState()
            if startup_policy_state is None
            else startup_policy_state
        )
    )
    next_speed_loop_state = (
        None
        if speed_loop_config is None
        else SensorlessSpeedLoopState() if speed_loop_state is None else speed_loop_state
    )
    steps: list[SensorlessCurrentLoopResult] = []

    for step_inputs in sensorless_inputs:
        result = sensorless_current_control_step(
            step_inputs,
            next_sensorless_state,
            sensorless_config,
            current_loop_gains,
            next_current_loop_state,
            observer_config,
            next_observer_state,
            startup_policy_config,
            next_startup_policy_state,
            speed_loop_config,
            next_speed_loop_state,
            current_command_policy_config,
        )
        steps.append(result)
        next_sensorless_state = result.state
        next_current_loop_state = result.current_loop_state
        if result.observer is not None:
            next_observer_state = result.observer.state
        if result.startup_policy is not None:
            next_startup_policy_state = result.startup_policy.state
        if result.speed_loop is not None:
            next_speed_loop_state = result.speed_loop.state

    return SensorlessReplayResult(
        steps=tuple(steps),
        state=next_sensorless_state,
        current_loop_state=next_current_loop_state,
        observer_state=next_observer_state,
        startup_policy_state=next_startup_policy_state,
        speed_loop_state=next_speed_loop_state,
    )
