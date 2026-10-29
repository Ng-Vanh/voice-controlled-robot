"""Hardware/simulator boundary, independent of any robot SDK."""

from abc import ABC, abstractmethod
from typing import Sequence


class RobotInterface(ABC):
    """Operations required by higher-level robot logic."""

    @abstractmethod
    def set_wheel_speeds(self, left: float, right: float) -> None:
        """Set left and right wheel angular speeds in rad/s."""

    @abstractmethod
    def read_distances(self) -> Sequence[float]:
        """Return raw distance-sensor readings without assuming units."""

    @abstractmethod
    def stop(self) -> None:
        """Stop all driven wheels."""
