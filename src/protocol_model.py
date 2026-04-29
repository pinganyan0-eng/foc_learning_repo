from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any


MAX_FRAME_BYTES = 256
MAX_SPEED_RPM = 4000

OK = 0
ERR_BAD_JSON = 100
ERR_BAD_FRAME = 101
ERR_UNKNOWN_CMD = 102
ERR_BAD_VALUE = 103
ERR_STATE = 104
ERR_FAULT = 105

KNOWN_COMMANDS = {"heartbeat", "arm", "set_speed", "stop", "clear_fault"}


@dataclass(frozen=True)
class Command:
    name: str
    payload: dict[str, Any]
    seq: int | None = None


@dataclass(frozen=True)
class Result:
    code: int
    message: str
    state: str
    target_rpm: int

    @property
    def ok(self) -> bool:
        return self.code == OK


def clamp_rpm(value: int) -> int:
    return max(-MAX_SPEED_RPM, min(MAX_SPEED_RPM, value))


def parse_frame(raw: bytes | str) -> tuple[Command | None, int]:
    if isinstance(raw, bytes):
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            return None, ERR_BAD_FRAME
    else:
        text = raw

    if len(text.encode("utf-8")) > MAX_FRAME_BYTES:
        return None, ERR_BAD_FRAME

    text = text.strip()
    if not text:
        return None, ERR_BAD_FRAME

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None, ERR_BAD_JSON

    if not isinstance(data, dict) or not isinstance(data.get("cmd"), str):
        return None, ERR_BAD_FRAME

    cmd = data["cmd"]
    if cmd not in KNOWN_COMMANDS:
        return None, ERR_UNKNOWN_CMD

    seq = data.get("seq")
    if seq is not None and not isinstance(seq, int):
        return None, ERR_BAD_VALUE

    if cmd == "set_speed":
        rpm = data.get("rpm")
        if not isinstance(rpm, int):
            return None, ERR_BAD_VALUE

    return Command(name=cmd, payload=data, seq=seq), OK


class MotorStateMachine:
    def __init__(self) -> None:
        self.state = "IDLE"
        self.target_rpm = 0
        self.last_error = OK

    def fault(self, code: int = ERR_FAULT) -> Result:
        self.state = "FAULT"
        self.target_rpm = 0
        self.last_error = code
        return Result(code, "fault latched", self.state, self.target_rpm)

    def apply(self, command: Command) -> Result:
        if self.state == "FAULT" and command.name != "clear_fault":
            return Result(ERR_FAULT, "fault must be cleared first", self.state, self.target_rpm)

        if command.name == "heartbeat":
            return Result(OK, "alive", self.state, self.target_rpm)

        if command.name == "arm":
            if self.state != "IDLE":
                return Result(ERR_STATE, "arm is only allowed from IDLE", self.state, self.target_rpm)
            self.state = "ARMED"
            return Result(OK, "armed", self.state, self.target_rpm)

        if command.name == "set_speed":
            if self.state not in {"ARMED", "RUNNING"}:
                return Result(ERR_STATE, "speed command requires ARMED or RUNNING", self.state, self.target_rpm)
            self.target_rpm = clamp_rpm(command.payload["rpm"])
            self.state = "RUNNING" if self.target_rpm != 0 else "ARMED"
            return Result(OK, "speed accepted", self.state, self.target_rpm)

        if command.name == "stop":
            if self.state not in {"ARMED", "RUNNING"}:
                return Result(ERR_STATE, "stop requires ARMED or RUNNING", self.state, self.target_rpm)
            self.target_rpm = 0
            self.state = "IDLE"
            return Result(OK, "stopped", self.state, self.target_rpm)

        if command.name == "clear_fault":
            if self.state != "FAULT":
                return Result(ERR_STATE, "clear_fault is only allowed from FAULT", self.state, self.target_rpm)
            self.state = "IDLE"
            self.last_error = OK
            return Result(OK, "fault cleared", self.state, self.target_rpm)

        return Result(ERR_UNKNOWN_CMD, "unknown command", self.state, self.target_rpm)
