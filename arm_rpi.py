#!/usr/bin/env python

import rospy
from rover_msgs.msg import arm_msg
from serial.serialutil import SerialException as SerialException
import signal
import sys
import os
import RPi.GPIO as GPIO
from time import sleep


# SIGINT handler
def sigint_handler_arm(signal, frame):
    Arm_RPi.arm_stop()
    sys.exit(0)


class Arm_RPi:

    def __init__(self, pin1, pin2):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        self.gripper = GPIO.PWM(pin1, 50)
        self.gripper_rot = GPIO.PWM(pin2, 50)
        self.gripper.start(11.5)
        self.gripper_rot.start(0)
        self.last_position = 5.5
        sleep(1)
        self.gripper_desc = {'name': "Gripper", 'speed': 0,
                             'direction': "stop", 'duty': 2}  # Claw1M1; Stop: 0, Up: 1, Down: -1
        self.gripper_rot_desc = {'name': "Gripper Rotation", 'speed': 0,
                                 'direction': "stop"}  # Claw1M2; Stop: 0, Extend: 1, Contract: -1

    # def update_arm_steer(self):
    #     self.rungripper(self.gripper_desc)
    #     self.rungripper_rot(self.gripper_rot_desc)

    def arm_callback(self, inp):
        self.gripper_desc['speed'], self.gripper_desc['direction'] = int(inp.gripper.speed), inp.gripper.direction
        self.gripper_rot_desc['speed'], self.gripper_rot_desc['direction'] = int(
            inp.gripper_rot.speed), inp.gripper_rot.direction
        if self.gripper_desc['direction'] == 'forward':
            self.gripper.ChangeDutyCycle(11.5)
            self.last_position = 11.5
        elif self.gripper_desc['direction'] == 'backward':
            self.gripper.ChangeDutyCycle(5.5)
            self.last_position = 5.5
        else:
            self.gripper.ChangeDutyCycle(self.last_position)
        # self.rungripper(self.gripper_desc)
        # self.rungripper_rot(self.gripper_rot_desc)

    def arm_stop(self):
        rospy.loginfo('Arm_RPi: ' + "Arm_RPi commanded to stop")
        self.gripper_rot.ChangeDutyCycle(7)
        self.gripper.ChangeDutyCycle(0)

    def gripper_clock(self):
        self.gripper_desc['duty'] += 1
        if self.gripper_desc['duty'] <= 11.5:
            self.gripper.ChangeDutyCycle(self.gripper_desc['duty'])
            sleep(0.01)
            print(self.gripper_desc['duty'])
        else:
            self.gripper_desc['duty'] = 11.5
            self.gripper.ChangeDutyCycle(self.gripper_desc['duty'])

    def gripper_anticlock(self):
        self.gripper_desc['duty'] -= 1
        if self.gripper_desc['duty'] >= 5.5:
            self.gripper.ChangeDutyCycle(self.gripper_desc['duty'])
            sleep(0.01)
            print(self.gripper_desc['duty'])
        else:
            self.gripper_desc['duty'] = 5.5
            self.gripper.ChangeDutyCycle(self.gripper_desc['duty'])

    def rungripper(self, cmd_dict):
        # if cmd_dict['direction'] == "stop":
        #     self.gripper.ChangeDutyCycle(0)
        if cmd_dict['direction'] == "forward":
            self.gripper_clock()
            rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = 1')
        if cmd_dict['direction'] == "backward":
            self.gripper_anticlock()
            rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = -1')

    def rungripper_rot(self, cmd_dict):
        if cmd_dict['direction'] == "stop":
            self.gripper_rot.ChangeDutyCycle(7)
        if cmd_dict['direction'] == "forward":
            self.gripper_rot.ChangeDutyCycle(6)
            rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = 1')
        if cmd_dict['direction'] == "backward":
            self.gripper_rot.ChangeDutyCycle(8)
            rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = -1')


def enable_motors():
    print()
    enb_all = input("Enable Motors? ")
    if enb_all == "y" or enb_all == "Y" or enb_all == "yes" or enb_all == "Yes":
        enable_gripper = True
        enable_gripper_rotation = True
    else:
        enable_gripper = False
        enable_gripper_rotation = False
    return enable_gripper, enable_gripper_rotation


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler_arm)

    rospy.init_node("Arm_RPi_Node")
    rospy.loginfo("Starting Arm_RPi_Node")
    iter_time = rospy.Rate(1)
    enable_gripper, enable_gripper_rotation = enable_motors()

    if enable_gripper_rotation and enable_gripper:
        rospy.loginfo("Connected to RPi for Gripper and Gripper Rotation")

    # initialising Arm Object-------------------
    Arm_RPi = Arm_RPi(22, 27)
    Arm_RPi.arm_stop()

    rospy.loginfo("Subscribing to /rover/arm_directives...")
    rospy.Subscriber("/rover/arm_directives", arm_msg, Arm_RPi.arm_callback)
    rospy.loginfo("Subscribed to /rover/arm_directives")
    rospy.spin()