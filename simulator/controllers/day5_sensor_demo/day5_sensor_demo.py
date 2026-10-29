"""Log e-puck proximity signals while moving slowly toward an obstacle."""

from controller import Robot

from sensor_data import group_proximity_values, validate_proximity_values


SENSOR_NAMES = tuple(f"ps{index}" for index in range(8))
FORWARD_SPEED = 1.0  # rad/s; deliberately slow for this diagnostic exercise
FRONT_STOP_THRESHOLD = 80.0  # raw signal, exploratory threshold (not calibrated)
MAX_DEMO_DURATION = 12.0  # simulation seconds; always bound this exercise
LOG_INTERVAL = 0.25  # simulation seconds


robot = Robot()
timestep = int(robot.getBasicTimeStep())
sensors = []
for sensor_name in SENSOR_NAMES:
    sensor = robot.getDevice(sensor_name)
    sensor.enable(timestep)
    sensors.append(sensor)

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))


def stop_motors():
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)


def finish(reason):
    stop_motors()
    print(reason)
    # Apply the stop command on the next simulation step.
    return robot.step(timestep) != -1


print("Day 5 sensor demo: raw proximity signals are not meters or centimeters.")
start_time = robot.getTime()
last_log_time = start_time - LOG_INTERVAL

while robot.step(timestep) != -1:
    now = robot.getTime()
    raw_values = [sensor.getValue() for sensor in sensors]
    readings = validate_proximity_values(raw_values)

    if readings is None:
        finish(f"Invalid proximity data {raw_values!r}; stopping safely.")
        break

    groups = group_proximity_values(readings)
    if now - last_log_time >= LOG_INTERVAL:
        raw_log = " ".join(
            f"ps{index}={value:.0f}" for index, value in enumerate(readings)
        )
        group_log = " ".join(f"{name}={value:.0f}" for name, value in groups.items())
        print(f"{raw_log} | {group_log}")
        last_log_time = now

    if groups["front"] >= FRONT_STOP_THRESHOLD:
        finish(
            "Front signal reached the exploratory threshold "
            f"({FRONT_STOP_THRESHOLD:.0f}); stopping."
        )
        break

    if now - start_time >= MAX_DEMO_DURATION:
        finish("Diagnostic duration reached; stopping.")
        break

    left_motor.setVelocity(FORWARD_SPEED)
    right_motor.setVelocity(FORWARD_SPEED)

stop_motors()
