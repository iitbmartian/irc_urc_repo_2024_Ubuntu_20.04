#!/usr/bin/env python

from arm_command_new import Arm
from roboclaw_3 import Roboclaw
from arduino_rot import Arduino_Rot
import rospy
from std_msgs.msg import Float64MultiArray
from rover_msgs.msg import arm_msg
from serial.serialutil import SerialException as SerialException
import signal
import sys
import os


# SIGINT handler
def sigint_handler_arm(signal, frame):
    Arm.arm_stop()
    sys.exit(0)


def enable_actuators_motors():
    print()
    enb_all = "y"
    #enb_all = input("Enable all Actuators/Motors? ")
    if enb_all == "y" or enb_all == "Y" or enb_all == "yes" or enb_all == "Yes":
        enable_shoulder_elbow_actuators = True
        enable_base_elbow_rot_motors = True
        enable_wrist_motor = True
    else:
        enb_shoulder_elbow_actuators = input("Enable Shoulder Elbow Actuators? ")
        if enb_shoulder_elbow_actuators == "y" or enb_shoulder_elbow_actuators == "Y" or \
                enb_shoulder_elbow_actuators == "yes" or enb_shoulder_elbow_actuators == "Yes":
            enable_shoulder_elbow_actuators = True
        else:
            enable_shoulder_elbow_actuators = False

        enb_base_elbow_rot_motors = input("Enable Base Elbow Motors? ")
        if enb_base_elbow_rot_motors == "y" or enb_base_elbow_rot_motors == "Y" or \
                enb_base_elbow_rot_motors == "yes" or enb_base_elbow_rot_motors == "Yes":
            enable_base_elbow_rot_motors = True
        else:
            enable_base_elbow_rot_motors = False

        enb_wrist_motor = input("Enable Wrist Motor? ")
        if enb_wrist_motor == "y" or enb_wrist_motor == "Y" or \
                enb_wrist_motor == "yes" or enb_wrist_motor == "Yes":
            enable_wrist_motor = True
        else:
            enable_wrist_motor= False

    return enable_shoulder_elbow_actuators, enable_base_elbow_rot_motors, enable_wrist_motor


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler_arm)

    rospy.init_node("Arm_Node")
    rospy.loginfo("Starting Arm_Node")
    iter_time = rospy.Rate(1)
    enable_shoulder_elbow_actuators, enable_base_elbow_rot_motors, enable_wrist_motor = enable_actuators_motors()

    if enable_shoulder_elbow_actuators:
        while True:
            try:
                shoulder_elbow_actuators = Roboclaw("/dev/shoulder_elbow_actuators", 9600)
                break
            except SerialException:
                rospy.logwarn("Could not connect to Shoulder and Elbow Claw, retrying...")
                iter_time.sleep()
        rospy.loginfo("Connected to Shoulder and Elbow Claw")
    else:
        shoulder_elbow_actuators = None

    if enable_base_elbow_rot_motors:
        while True:
            try:
                base_elbow_rot_motors = Roboclaw("/dev/base_elbow_rot_motors", 9600)
                break
            except SerialException:
                rospy.logwarn("Could not connect to Base and Elbow(Motor) Claw, retrying...")
                iter_time.sleep()
        rospy.loginfo("Connected to Base and Elbow Claw")
    else:
        base_elbow_rot_motors = None

    if enable_wrist_motor:
        while True:
            try:
                wrist_motor = Roboclaw("/dev/wrist_motor", 9600)
                break
            except SerialException:
                rospy.logwarn("Could not connect to Wrist Claw, retrying...")
                iter_time.sleep()
        rospy.loginfo("Connected to Wrist Claw")
    else:
        wrist_motor = None

    # initialising Arm Object-------------------
    Arm = Arm(shoulder_elbow_actuators, base_elbow_rot_motors, wrist_motor)
    Arm.init_enc_vals()

    rospy.loginfo("Subscribing to /rover/arm_directives...")
    rospy.Subscriber("/rover/arm_directives", arm_msg, Arm.arm_callback)
    rospy.loginfo("Subscribed to /rover/arm_directives")
    run_time = rospy.Rate(10)

    while not rospy.is_shutdown():
        Arm.current_limiter()
        if not Arm.current_exceeded:
            Arm.update_arm_steer()
        else:
            rospy.logwarn("Arm stopped due to excess current")
            rospy.loginfo(Arm.currents)
        run_time.sleep()
