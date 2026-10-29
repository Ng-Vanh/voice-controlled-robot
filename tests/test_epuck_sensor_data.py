import math

import pytest

from simulator.controllers.day5_sensor_demo.sensor_data import (
    group_proximity_values,
    validate_proximity_values,
)


def test_groups_e_puck_values_by_sensor_direction():
    readings = [10, 20, 30, 40, 50, 60, 70, 80]

    assert group_proximity_values(readings) == {
        "front": 80.0,
        "right": 30.0,
        "left": 80.0,
        "rear": 50.0,
    }


@pytest.mark.parametrize(
    "readings",
    [
        [0] * 7,
        [0] * 9,
        [-1, 0, 0, 0, 0, 0, 0, 0],
        [4096, 0, 0, 0, 0, 0, 0, 0],
        [math.nan, 0, 0, 0, 0, 0, 0, 0],
        [math.inf, 0, 0, 0, 0, 0, 0, 0],
        ["bad", 0, 0, 0, 0, 0, 0, 0],
        None,
        "00000000",
    ],
)
def test_rejects_invalid_sensor_readings(readings):
    assert validate_proximity_values(readings) is None
    assert group_proximity_values(readings) is None


def test_converts_valid_readings_to_floats():
    assert validate_proximity_values([0, 1, 2, 3, 4, 5, 6, 4095]) == (
        0.0,
        1.0,
        2.0,
        3.0,
        4.0,
        5.0,
        6.0,
        4095.0,
    )
