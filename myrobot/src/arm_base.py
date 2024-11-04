from roboclaw_3 import Roboclaw
import rospy
from std_msgs.msg import Int32
import signal
import sys
import os
from serial.serialutil import SerialException as SerialException

class Arm:
    def __init__(self, claw2):
        self.base_elbow_motors = claw2
        self.base_motor = {'name': "Base Rotation", 'speed': 0,
                           'direction': "stop"}  # Claw3M1; Stop: 0, Clockwise: 1, Anticlockwise: -1
        self.config = 0
        self.isconfig = False
        self.configComplete = False
        self.runtimer = rospy.Rate(10)
    
    def init_enc_vals(self):
        if self.base_elbow_motors is not None:
            self.base_elbow_motors.ForwardM1(0x80, 0)
            
            self.base_elbow_motors.ResetEncoders(0x80)
            self.base_elbow_motors.SetEncM1(0x80, 0)


    

    def update_arm_steer(self):

        if self.base_elbow_motors is not None:
            _, enc3, _ = self.base_elbow_motors.ReadEncM1(0x80)
            if (self.encoder_value)>=(enc3+10):
                self.base_motor['direction'] == 'forward'
            elif (self.encoder_value)<=(enc3-10):
                self.base_motor['direction'] == 'backward'
            else:
                self.base_motor['direction'] == 'stop'




            if -3240 < enc3 < -3200:
                if self.base_motor['direction'] == 'forward':
                    self.runclawM1(self.base_elbow_motors, self.base_motor)
                else:
                    self.base_elbow_motors.ForwardM1(0x80, 0)
            elif -3200 <= enc3 < 3200:
                self.runclawM1(self.base_elbow_motors, self.base_motor)
            else:
                if self.base_motor['direction'] == 'backward':
                    self.runclawM1(self.base_elbow_motors, self.base_motor)
                else:
                    self.base_elbow_motors.ForwardM1(0x80, 0)
    def arm_callback(self, inp):
        self.config = 0
        self.isconfig = False
        angle=inp.data
        self.encoder_value=angle*36

        # self.base_motor['speed'], self.base_motor['direction'] = int(inp.base_motor.speed), inp.base_motor.direction
    def arm_stop(self):
        if self.base_elbow_motors is not None:
            while True:
                _, enc3, _ = self.base_elbow_motors.ReadEncM1(0x80)
                if (enc3)>=10:
                    self.base_motor['direction'] == 'backward'
                elif (enc3)<=(-10):
                    self.base_motor['direction'] == 'forward'
                else:
                    self.base_motor['direction'] == 'stop'
                    break
                



    def arm_break(self):
        rospy.loginfo('Arm: ' + "Arm commanded to break")

        if self.base_elbow_motors is not None:
            self.base_elbow_motors.ForwardM1(0x80, 0)
            self.base_elbow_motors.ForwardM2(0x80, 0)

    def runclawM1(self, claw, cmd_dict):
        if cmd_dict['direction'] == "stop":
            claw.ForwardM1(0x80, 0)
            # rospy.loginfo('Arm: '+ cmd_dict['name'] + ' commanded to stop')
        if cmd_dict['direction'] == "forward":
            claw.ForwardM1(0x80, 60)
            # rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = 1')
        if cmd_dict['direction'] == "backward":
            claw.BackwardM1(0x80, 60)
            # rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = -1')








def sigint_handler_arm(signal, frame):
    Arm.arm_stop()
    sys.exit(0)


def enable_actuators_motors():
    print()
    enb_base = "y"
    #enb_all = input("Enable all Actuators/Motors? ")
    if enb_base == "y" or enb_base == "Y" or enb_base == "yes" or enb_base == "Yes":
        enable_base_elbow_rot_motors = True

    else:
        enable_base_elbow_rot_motors = False


    return  enable_base_elbow_rot_motors










if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler_arm)

    rospy.init_node("Arm_Node")
    rospy.loginfo("Starting Arm_Node")
    iter_time = rospy.Rate(1)
    enable_base_elbow_rot_motors = enable_actuators_motors()
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
    Arm = Arm(base_elbow_rot_motors)
    Arm.init_enc_vals()

    rospy.loginfo("Subscribing to /rover/auto_cam_angle...")
    rospy.Subscriber("/rover/auto_cam_angle", Int32, Arm.arm_callback)
    rospy.loginfo("Subscribed to /rover/auto_cam_angle")
    run_time = rospy.Rate(10)
    while not rospy.is_shutdown():
        Arm.update_arm_steer()
        run_time.sleep()