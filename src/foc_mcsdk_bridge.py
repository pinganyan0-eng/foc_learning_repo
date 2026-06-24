from __future__ import annotations

import math
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.foc_core_model import CurrentLoopResult, DQ, SVPWMResult

if TYPE_CHECKING:
    from src.foc_sensorless_frontend import (
        SensorlessCurrentLoopResult,
        SensorlessReplayResult,
    )


Q15_SCALE = 32768
S16_ANGLE_SCALE = 65536
INT16_MIN = -32768
INT16_MAX = 32767


@dataclass(frozen=True)
class McsdkQd:
    q: int
    d: int


@dataclass(frozen=True)
class McsdkDutyCounts:
    a: int
    b: int
    c: int
    pwm_period_cycles: int


@dataclass(frozen=True)
class McsdkComparisonState:
    iqd: McsdkQd
    iqdref: McsdkQd
    vqd: McsdkQd
    theta_q15: int
    duty_counts: McsdkDutyCounts
    host_pwm_saturated: bool
    host_pwm_scale: float


@dataclass(frozen=True)
class McsdkObserverSnapshot:
    theta_q15: int
    omega_q15: int
    confidence_q15: int
    mode: str
    locked: bool


@dataclass(frozen=True)
class McsdkSpeedCommandSnapshot:
    target_omega_q15: int
    measured_omega_q15: int
    requested_iq_q15: int
    effective_iq_q15: int
    locked: bool
    limited: bool
    reason: str


def clamp_int16(value: int) -> int:
    if value > INT16_MAX:
        return INT16_MAX
    if value < INT16_MIN:
        return INT16_MIN
    return value


def radians_to_q15(theta_e_rad: float) -> int:
    """Map host radians into the MCSDK q1.15 electrical-angle domain."""

    wrapped = math.fmod(theta_e_rad, 2.0 * math.pi)
    if wrapped < 0.0:
        wrapped += 2.0 * math.pi
    raw = int(round((wrapped / (2.0 * math.pi)) * S16_ANGLE_SCALE))
    return clamp_int16(raw if raw < 32768 else raw - S16_ANGLE_SCALE)


def float_to_q15(value: float) -> int:
    """Map host floating-point quantities into comparison-only q1.15 digits."""

    return clamp_int16(int(round(value * Q15_SCALE)))


def dq_to_mcsdk_qd(dq: DQ) -> McsdkQd:
    return McsdkQd(q=float_to_q15(dq.q), d=float_to_q15(dq.d))


def duty_to_counts(result: SVPWMResult, pwm_period_cycles: int) -> McsdkDutyCounts:
    if pwm_period_cycles <= 0:
        raise ValueError("pwm_period_cycles must be positive")

    return McsdkDutyCounts(
        a=int(round(result.duty.a * pwm_period_cycles)),
        b=int(round(result.duty.b * pwm_period_cycles)),
        c=int(round(result.duty.c * pwm_period_cycles)),
        pwm_period_cycles=pwm_period_cycles,
    )


def current_loop_result_to_mcsdk_state(
    *,
    result: CurrentLoopResult,
    target_dq: DQ,
    theta_e_rad: float,
    pwm_period_cycles: int,
) -> McsdkComparisonState:
    """Build a comparison-only MCSDK-shaped snapshot from host-side results."""

    return McsdkComparisonState(
        iqd=dq_to_mcsdk_qd(result.current_dq),
        iqdref=dq_to_mcsdk_qd(target_dq),
        vqd=dq_to_mcsdk_qd(result.voltage_dq),
        theta_q15=radians_to_q15(theta_e_rad),
        duty_counts=duty_to_counts(result.svpwm, pwm_period_cycles),
        host_pwm_saturated=result.svpwm.saturated,
        host_pwm_scale=result.svpwm.scale,
    )


def sensorless_result_to_mcsdk_observer_snapshot(
    *,
    theta_e_rad: float,
    omega_e_rad_s: float,
    confidence: float,
    mode: str,
    locked: bool,
    omega_full_scale_rad_s: float,
) -> McsdkObserverSnapshot:
    """Build a comparison-only MCSDK-shaped sensorless-output snapshot."""

    if omega_full_scale_rad_s <= 0.0:
        raise ValueError("omega_full_scale_rad_s must be positive")

    normalized_omega = omega_e_rad_s / omega_full_scale_rad_s
    bounded_confidence = max(0.0, min(1.0, confidence))

    return McsdkObserverSnapshot(
        theta_q15=radians_to_q15(theta_e_rad),
        omega_q15=float_to_q15(normalized_omega),
        confidence_q15=float_to_q15(bounded_confidence),
        mode=mode,
        locked=locked,
    )


def sensorless_replay_to_mcsdk_observer_snapshots(
    replay: SensorlessReplayResult,
    *,
    omega_full_scale_rad_s: float,
) -> tuple[McsdkObserverSnapshot, ...]:
    """Translate each host-side replay step into comparison-only snapshots."""

    return tuple(
        sensorless_result_to_mcsdk_observer_snapshot(
            theta_e_rad=step.sensorless.theta_e_rad,
            omega_e_rad_s=step.sensorless.omega_e_rad_s,
            confidence=step.sensorless.confidence,
            mode=step.sensorless.mode,
            locked=step.sensorless.locked,
            omega_full_scale_rad_s=omega_full_scale_rad_s,
        )
        for step in replay.steps
    )


def speed_command_to_mcsdk_snapshot(
    *,
    target_omega_e_rad_s: float,
    measured_omega_e_rad_s: float,
    requested_target_iq: float,
    effective_target_iq: float,
    locked: bool,
    limited: bool,
    reason: str,
    omega_full_scale_rad_s: float,
    iq_full_scale_a: float,
) -> McsdkSpeedCommandSnapshot:
    """Build a comparison-only speed/current command snapshot."""

    if omega_full_scale_rad_s <= 0.0:
        raise ValueError("omega_full_scale_rad_s must be positive")
    if iq_full_scale_a <= 0.0:
        raise ValueError("iq_full_scale_a must be positive")

    return McsdkSpeedCommandSnapshot(
        target_omega_q15=float_to_q15(target_omega_e_rad_s / omega_full_scale_rad_s),
        measured_omega_q15=float_to_q15(measured_omega_e_rad_s / omega_full_scale_rad_s),
        requested_iq_q15=float_to_q15(requested_target_iq / iq_full_scale_a),
        effective_iq_q15=float_to_q15(effective_target_iq / iq_full_scale_a),
        locked=locked,
        limited=limited,
        reason=reason,
    )


def sensorless_result_to_mcsdk_speed_command_snapshot(
    result: SensorlessCurrentLoopResult,
    *,
    omega_full_scale_rad_s: float,
    iq_full_scale_a: float,
) -> McsdkSpeedCommandSnapshot:
    """Translate one host-side lock-aware speed/current result."""

    if result.speed_loop is None:
        raise ValueError("result.speed_loop is required")
    if result.current_command_policy is None:
        raise ValueError("result.current_command_policy is required")

    return speed_command_to_mcsdk_snapshot(
        target_omega_e_rad_s=result.speed_loop.target_omega_e_rad_s,
        measured_omega_e_rad_s=result.speed_loop.measured_omega_e_rad_s,
        requested_target_iq=result.current_command_policy.requested_target_iq,
        effective_target_iq=result.current_command_policy.effective_target_iq,
        locked=result.current_command_policy.locked,
        limited=result.current_command_policy.limited,
        reason=result.current_command_policy.reason,
        omega_full_scale_rad_s=omega_full_scale_rad_s,
        iq_full_scale_a=iq_full_scale_a,
    )


def sensorless_replay_to_mcsdk_speed_command_snapshots(
    replay: SensorlessReplayResult,
    *,
    omega_full_scale_rad_s: float,
    iq_full_scale_a: float,
) -> tuple[McsdkSpeedCommandSnapshot, ...]:
    """Translate each host-side speed/current policy step for comparison."""

    return tuple(
        sensorless_result_to_mcsdk_speed_command_snapshot(
            step,
            omega_full_scale_rad_s=omega_full_scale_rad_s,
            iq_full_scale_a=iq_full_scale_a,
        )
        for step in replay.steps
    )
