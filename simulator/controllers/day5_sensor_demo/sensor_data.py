"""Validation and directional grouping for the e-puck's eight IR sensors."""

import math
from collections.abc import Sequence


SENSOR_COUNT = 8
MAX_PROXIMITY_VALUE = 4095.0

# The e-puck front points along +x in its local frame. The front pair is also
# part of the left/right arcs, as in Cyberbotics' e-puck avoidance example.
SENSOR_GROUPS = {
    "front": (0, 7),
    "right": (0, 1, 2),
    "left": (5, 6, 7),
    "rear": (3, 4),
}


def validate_proximity_values(values: Sequence[object]) -> tuple[float, ...] | None:
    """Return eight finite in-range readings, or None when any value is bad."""
    if isinstance(values, (str, bytes)):
        return None

    try:
        if len(values) != SENSOR_COUNT:
            return None
        converted = tuple(float(value) for value in values)
    except (TypeError, ValueError, OverflowError):
        return None

    if any(
        not math.isfinite(value)
        or value < 0.0
        or value > MAX_PROXIMITY_VALUE
        for value in converted
    ):
        return None

    return converted


def group_proximity_values(values: Sequence[object]) -> dict[str, float] | None:
    """Summarize each direction by its strongest raw signal; invalid -> None."""
    readings = validate_proximity_values(values)
    if readings is None:
        return None
    return {
        direction: max(readings[index] for index in indices)
        for direction, indices in SENSOR_GROUPS.items()
    }
