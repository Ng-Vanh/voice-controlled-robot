"""Day 3: bounded differential-drive motor control for the Webots e-puck."""

import math

from controller import Robot


robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_encoder = robot.getDevice("left wheel sensor")
right_encoder = robot.getDevice("right wheel sensor")

left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)
left_encoder.enable(timestep)
right_encoder.enable(timestep)

MAX_WHEEL_SPEED = 6.28  # rad/s, e-puck example limit in Webots
TEST_SPEED = 2.0  # keep the lesson demonstration slow
MOTION_DURATION = 0.8  # seconds of simulation time per movement


def set_wheel_speeds(left_requested, right_requested):
    """Set wheel angular speeds, clamping requests to the motor limit."""
    requested = (float(left_requested), float(right_requested))
    applied = tuple(
        max(-MAX_WHEEL_SPEED, min(MAX_WHEEL_SPEED, speed))
        if math.isfinite(speed)
        else 0.0
        for speed in requested
    )

    if requested != applied:
        print(
            "Clamped wheel speed: "
            f"requested=({requested[0]:.2f}, {requested[1]:.2f}) rad/s, "
            f"applied=({applied[0]:.2f}, {applied[1]:.2f}) rad/s"
        )

    left_motor.setVelocity(applied[0])
    right_motor.setVelocity(applied[1])
    print(
        f"Wheel target: left={applied[0]:.2f}, "
        f"right={applied[1]:.2f} rad/s"
    )
    return applied


def run_motion(name, left_speed, right_speed, duration):
    """Run one bounded motion, log encoder-based speed, then stop."""
    print(f"\n--- {name} ---")
    set_wheel_speeds(left_speed, right_speed)

    start_time = robot.getTime()
    last_sample_time = start_time
    last_left_angle = left_encoder.getValue()
    last_right_angle = right_encoder.getValue()
    last_log_time = start_time

    while robot.step(timestep) != -1:
        now = robot.getTime()
        delta_time = now - last_sample_time

        if delta_time > 0:
            left_angle = left_encoder.getValue()
            right_angle = right_encoder.getValue()
            measured_left = (left_angle - last_left_angle) / delta_time
            measured_right = (right_angle - last_right_angle) / delta_time
            last_left_angle = left_angle
            last_right_angle = right_angle
            last_sample_time = now

            if now - last_log_time >= 0.4:
                print(
                    f"Measured wheel speed: left={measured_left:.2f}, "
                    f"right={measured_right:.2f} rad/s"
                )
                last_log_time = now

        if now - start_time >= duration:
            break

    set_wheel_speeds(0.0, 0.0)
    # Advance one step so Webots applies the stop command before the next case.
    return robot.step(timestep) != -1


test_cases = (
    ("Tiến", TEST_SPEED, TEST_SPEED, MOTION_DURATION),
    ("Lùi", -TEST_SPEED, -TEST_SPEED, MOTION_DURATION),
    ("Xoay trái tại chỗ", -TEST_SPEED, TEST_SPEED, MOTION_DURATION),
    ("Xoay phải tại chỗ", TEST_SPEED, -TEST_SPEED, MOTION_DURATION),
    ("Dừng", 0.0, 0.0, 0.4),
)

for case in test_cases:
    if not run_motion(*case):
        break

set_wheel_speeds(0.0, 0.0)
