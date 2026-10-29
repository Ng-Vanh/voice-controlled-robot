"""Shared, Webots-independent types used across the robot project."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping


class Command(str, Enum):
    """Recognized high-level robot intents."""

    MOVE_FORWARD = "MOVE_FORWARD"
    MOVE_BACKWARD = "MOVE_BACKWARD"
    TURN_LEFT = "TURN_LEFT"
    TURN_RIGHT = "TURN_RIGHT"
    STOP = "STOP"
    UNKNOWN = "UNKNOWN"


class RobotMode(str, Enum):
    MANUAL = "MANUAL"
    AUTO_AVOID = "AUTO_AVOID"


@dataclass(frozen=True)
class Telemetry:
    """A snapshot of robot status; sensor values retain their raw units."""

    mode: RobotMode = RobotMode.MANUAL
    state: str = "IDLE"
    last_command: Command = Command.UNKNOWN
    sensor_values: Mapping[str, float] = field(default_factory=dict)
