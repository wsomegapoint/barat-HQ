import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library
import random

robot = CamJamKitRobot()
sleepTimeForward = 1
sleepTimeSideways = 0.5

for x in range(10):
    op = random.randint(1, 4)

    if op == 1:
        robot.forward()
        time.sleep(sleepTimeForward)

    if op == 2:
        robot.backward()
        time.sleep(sleepTimeForward)

    if op == 3:
        robot.left()
        time.sleep(sleepTimeSideways)

    if op == 4:
        robot.right()
        time.sleep(sleepTimeSideways)
        

robot.stop()