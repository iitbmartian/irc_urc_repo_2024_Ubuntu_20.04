#!/usr/bin/env python3
from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)
# import adafruit_motor.servo
# servo = adafruit_motor.servo.Servo(servo_channel)
for i in 120,1:

    kit.servo[0].angle = i
    time.sleep(1)

