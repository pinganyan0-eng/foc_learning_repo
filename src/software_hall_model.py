from __future__ import annotations

from dataclasses import dataclass


VALID_HALL_STATES = (0b001, 0b010, 0b011, 0b100, 0b101, 0b110)
FORWARD_SEQUENCE = (0b001, 0b101, 0b100, 0b110, 0b010, 0b011)
REVERSE_SEQUENCE = tuple(reversed(FORWARD_SEQUENCE))

DIRECTION_UNKNOWN = "unknown"
DIRECTION_FORWARD = "forward"
DIRECTION_REVERSE = "reverse"

DECISION_ILLEGAL_STATE = "illegal_state"
DECISION_FIRST_VALID = "first_valid"
DECISION_REPEAT_STATE = "repeat_state"
DECISION_BOUNCE_CANDIDATE = "bounce_candidate"
DECISION_FORWARD_STEP = "forward_step"
DECISION_REVERSE_STEP = "reverse_step"
DECISION_ABNORMAL_JUMP = "abnormal_jump"


@dataclass(frozen=True)
class HallDecision:
    decision: str
    raw_state: int
    accepted_state: int | None
    previous_state: int | None
    direction_candidate: str
    counted_edge: bool
    abnormal: bool
    dt_ticks: int | None = None


def format_hall_state(state: int | None) -> str:
    if state is None:
        return "---"
    return f"{state:03b}"


def is_valid_state(state: int) -> bool:
    return state in VALID_HALL_STATES


def _is_adjacent(sequence: tuple[int, ...], previous: int, current: int) -> bool:
    index = sequence.index(previous)
    return sequence[(index + 1) % len(sequence)] == current


def is_forward_adjacent(previous: int, current: int) -> bool:
    if previous not in FORWARD_SEQUENCE or current not in FORWARD_SEQUENCE:
        return False
    return _is_adjacent(FORWARD_SEQUENCE, previous, current)


def is_reverse_adjacent(previous: int, current: int) -> bool:
    if previous not in REVERSE_SEQUENCE or current not in REVERSE_SEQUENCE:
        return False
    return _is_adjacent(REVERSE_SEQUENCE, previous, current)


class SoftwareHallStateMachine:
    """Host-side software Hall reference model; not STM32 firmware."""

    def __init__(self, min_edge_ticks: int | None = None) -> None:
        if min_edge_ticks is not None and min_edge_ticks < 0:
            raise ValueError("min_edge_ticks must be non-negative")

        self.min_edge_ticks = min_edge_ticks
        self.last_accepted_state: int | None = None
        self.last_edge_ticks: int | None = None
        self.direction_candidate = DIRECTION_UNKNOWN
        self.edge_count = 0
        self.illegal_state_count = 0
        self.repeat_count = 0
        self.bounce_candidate_count = 0
        self.abnormal_jump_count = 0
        self.last_edge_dt_ticks: int | None = None

    def process(self, raw_state: int, timestamp_ticks: int) -> HallDecision:
        if not is_valid_state(raw_state):
            self.illegal_state_count += 1
            return HallDecision(
                decision=DECISION_ILLEGAL_STATE,
                raw_state=raw_state,
                accepted_state=self.last_accepted_state,
                previous_state=self.last_accepted_state,
                direction_candidate=self.direction_candidate,
                counted_edge=False,
                abnormal=True,
            )

        previous = self.last_accepted_state
        if previous is None:
            self.last_accepted_state = raw_state
            self.last_edge_ticks = timestamp_ticks
            return HallDecision(
                decision=DECISION_FIRST_VALID,
                raw_state=raw_state,
                accepted_state=raw_state,
                previous_state=None,
                direction_candidate=DIRECTION_UNKNOWN,
                counted_edge=False,
                abnormal=False,
            )

        if raw_state == previous:
            self.repeat_count += 1
            return HallDecision(
                decision=DECISION_REPEAT_STATE,
                raw_state=raw_state,
                accepted_state=previous,
                previous_state=previous,
                direction_candidate=self.direction_candidate,
                counted_edge=False,
                abnormal=False,
            )

        dt_ticks = (
            None
            if self.last_edge_ticks is None
            else timestamp_ticks - self.last_edge_ticks
        )

        if (
            self.min_edge_ticks is not None
            and dt_ticks is not None
            and dt_ticks < self.min_edge_ticks
        ):
            self.bounce_candidate_count += 1
            return HallDecision(
                decision=DECISION_BOUNCE_CANDIDATE,
                raw_state=raw_state,
                accepted_state=previous,
                previous_state=previous,
                direction_candidate=self.direction_candidate,
                counted_edge=False,
                abnormal=False,
                dt_ticks=dt_ticks,
            )

        if is_forward_adjacent(previous, raw_state):
            return self._accept_edge(
                raw_state=raw_state,
                previous=previous,
                timestamp_ticks=timestamp_ticks,
                dt_ticks=dt_ticks,
                direction=DIRECTION_FORWARD,
                decision=DECISION_FORWARD_STEP,
            )

        if is_reverse_adjacent(previous, raw_state):
            return self._accept_edge(
                raw_state=raw_state,
                previous=previous,
                timestamp_ticks=timestamp_ticks,
                dt_ticks=dt_ticks,
                direction=DIRECTION_REVERSE,
                decision=DECISION_REVERSE_STEP,
            )

        self.abnormal_jump_count += 1
        return HallDecision(
            decision=DECISION_ABNORMAL_JUMP,
            raw_state=raw_state,
            accepted_state=previous,
            previous_state=previous,
            direction_candidate=self.direction_candidate,
            counted_edge=False,
            abnormal=True,
            dt_ticks=dt_ticks,
        )

    def _accept_edge(
        self,
        *,
        raw_state: int,
        previous: int,
        timestamp_ticks: int,
        dt_ticks: int | None,
        direction: str,
        decision: str,
    ) -> HallDecision:
        self.last_accepted_state = raw_state
        self.last_edge_ticks = timestamp_ticks
        self.last_edge_dt_ticks = dt_ticks
        self.direction_candidate = direction
        self.edge_count += 1
        return HallDecision(
            decision=decision,
            raw_state=raw_state,
            accepted_state=raw_state,
            previous_state=previous,
            direction_candidate=direction,
            counted_edge=True,
            abnormal=False,
            dt_ticks=dt_ticks,
        )
