from controller import Robot
import math

robot = Robot()
timestep = int(robot.getBasicTimeStep())
print("Time step:", timestep)

# Get motors
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

# Velocity control mode
left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))

# e-puck parameters
WHEEL_RADIUS = 0.0205
AXLE_LENGTH = 0.052

SPEED = 2.0  # rad/s

def move(left_speed, right_speed, duration):
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)

    start = robot.getTime()

    while robot.step(timestep) != -1:
        if robot.getTime() - start >= duration:
            break

    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    return robot.step(timestep) != -1


def go_straight(distance):
    velocity = WHEEL_RADIUS * SPEED
    duration = distance / velocity
    return move(SPEED, SPEED, duration)


def turn_left_90():
    angular_velocity = 2 * WHEEL_RADIUS * SPEED / AXLE_LENGTH
    duration = (math.pi / 2) / angular_velocity
    return move(-SPEED, SPEED, duration)


# Rectangle: 1 m x 0.5 m
for i in range(4):
    if i % 2 == 0:
        distance = 1.0
    else:
        distance = 0.5

    if not go_straight(distance):
        break

    if not turn_left_90():
        break