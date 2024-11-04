#!/usr/bin/env python
import rospy
from time import sleep
import serial
import serial.tools.list_ports as ports
shoulder_elbow_rot_addr=0x83
base_elbow_addr=0x84
wrist_rot_addr=0x85
PORT='/dev/UART_Servo'
class Arm:

    def __init__(self, claw1):
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.port = PORT
        self.ser.open()
        self.shoulder_elbow_rot_actuators = claw1
        self.base_elbow_motors = claw1
        self.wrist_motors = claw1

        self.current_exceeded = False
        self.currents = [0, 0, 0, 0, 0, 0, 0, 0]
        self.current_threshold = 1000
        self.shoulder_actuator = {'name': "Shoulder Actuator", 'speed': 0,
                                  'direction': "stop"}  # Claw1M1; Stop: 0, Up: 1, Down: -1
        self.elbow_actuator = {'name': "Elbow Actuator", 'speed': 0,
                               'direction': "stop"}  # Claw1M2; Stop: 0, Extend: 1, Contract: -1\
        self.base_motor = {'name': "Base Rotation", 'speed': 0,
                           'direction': "stop"}  # Claw3M1; Stop: 0, Clockwise: 1, Anticlockwise: -1
        # self.finger_motor = {'name': "Finger Actuator", 'speed': 0,
        #                      'direction': "stop"}  # Claw2M1; Stop: 0, Clockwise: 1, Anticlockwise: -1
        self.wrist_actuator = {'name': "Wrist Actuator", 'speed': 0, 'direction': "stop"}  # Claw2M2; Stop: 0, .: 1, .: -1
        # self.rotation_motor = {'name': "Gripper Motor", 'speed': 0,
        #                        'direction': "stop"}  # Arduino - Pin 9
        self.elbow_rotation = {'name': "Elbow Rotation", 'speed': 0,
                               'direction': "stop"}  # Arduino - Pin 10
        self.gripper={'name': "Gripper", 'speed': 0,
                               'direction': "stop"}
        self.gripper_rot={'name': "Gripper rotation", 'speed': 0,
                               'direction': "stop"}
    def update_arm_steer(self):
        print(self.gripper_rot['direction'])
        if self.shoulder_elbow_rot_actuators is not None:
            self.runclawM1(self.shoulder_elbow_rot_actuators, self.shoulder_actuator,shoulder_elbow_rot_addr)
            self.runclawM2(self.shoulder_elbow_rot_actuators, self.elbow_rotation,base_elbow_addr)
        if self.base_elbow_motors is not None:
            self.runclawM2(self.base_elbow_motors, self.base_motor,shoulder_elbow_rot_addr)
            self.runclawM1(self.base_elbow_motors, self.elbow_actuator,base_elbow_addr)
        if self.wrist_motors is not None:
            self.runclawM1(self.wrist_motors, self.wrist_actuator,wrist_rot_addr)
            self.runclawM2(self.wrist_motors, self.gripper,wrist_rot_addr)
        if (self.gripper['direction'] == "forward") and (self.gripper_rot['direction']=="forward"):
            self.serial_send(22)
        elif (self.gripper['direction'] == "forward") and (self.gripper_rot['direction']=="backward"):
            self.serial_send(21)
        elif (self.gripper['direction'] == "backward") and (self.gripper_rot['direction']=="forward"):
            self.serial_send(12)
        elif (self.gripper['direction'] == "backward") and (self.gripper_rot['direction']=="backward"):
            self.serial_send(11)
        elif (self.gripper['direction'] == "backward") and (self.gripper_rot['direction']=="stop"):
            self.serial_send(10)
        elif (self.gripper['direction'] == "stop") and (self.gripper_rot['direction']=="backward"):
            self.serial_send(1)
        elif (self.gripper['direction'] == "forward") and (self.gripper_rot['direction']=="stop"):
            self.serial_send(20)
        elif (self.gripper['direction'] == "stop") and (self.gripper_rot['direction']=="forward"):
            self.serial_send(2)
        elif (self.gripper['direction'] == "stop") and (self.gripper_rot['direction']=="stop"):
            self.serial_send(0)

       
        # if self.elbow_rotation is not None:
        #     self.runclawM1(self.rotation_servo, self.elbow_rotation)
        #     self.runclawM1(self.rotation_servo, self.rotation_motor)
    def serial_send(self,a):
       
        command=str(a)
        command=command+'\n'
        self.ser.write(command.encode())
        print("Sent "+command)

    def arm_callback(self, inp):
        self.shoulder_actuator['speed'], self.shoulder_actuator['direction'] = int(inp.shoulder_actuator.speed), inp.shoulder_actuator.direction
        self.elbow_actuator['speed'], self.elbow_actuator['direction'] = int(inp.elbow_actuator.speed), inp.elbow_actuator.direction
        self.base_motor['speed'], self.base_motor['direction'] = int(inp.base_motor.speed), inp.base_motor.direction
        self.gripper['speed'], self.gripper['direction'] = int(inp.gripper.speed), inp.gripper.direction
        self.wrist_actuator['speed'], self.wrist_actuator['direction'] = int(inp.wrist_actuator.speed), inp.wrist_actuator.direction
        self.gripper_rot['speed'], self.gripper_rot['direction'] = int(inp.gripper_rot.speed), inp.gripper_rot.direction
        self.elbow_rotation['speed'], self.elbow_rotation['direction'] = int(inp.elbow_motor.speed), inp.elbow_motor.direction

    def arm_stop(self):
        rospy.loginfo('Arm: ' + "Arm commanded to stop")
        if self.shoulder_elbow_rot_actuators is not None:
            self.shoulder_elbow_rot_actuators.ForwardM1(shoulder_elbow_rot_addr, 0)
            self.shoulder_elbow_rot_actuators.ForwardM2(shoulder_elbow_rot_addr, 0)
        if self.base_elbow_motors is not None:
            self.base_elbow_motors.ForwardM1(base_elbow_addr, 0)
            self.base_elbow_motors.ForwardM2(base_elbow_addr, 0)
        if self.wrist_motors is not None:
            self.wrist_motors.ForwardM1(wrist_rot_addr,0)
        # if self.wrist_rotation_motors is not None:
        #     self.wrist_rotation_motors.ForwardM1(wrist_rot_addr, 0)
        #     self.wrist_rotation_motors.ForwardM2(wrist_rot_addr, 0)
        # if self.rotation_servo is not None:
        #     self.rotation_motor.ForwardM1(0x80, 0)
        #     self.elbow_rotation.ForwardM2(0x80, 0)

    def runclawM1(self, claw, cmd_dict,address):
        if cmd_dict['direction'] == "stop":
            claw.ForwardM1(address, 0)
        if cmd_dict['direction'] == "forward":
            claw.ForwardM1(address, cmd_dict['speed'])
            rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = 1')
        if cmd_dict['direction'] == "backward":
            claw.BackwardM1(address, cmd_dict['speed'])
            rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = -1')

    def runclawM2(self, claw, cmd_dict,address):
        if cmd_dict['direction'] == "stop":
            claw.ForwardM2(address, 0)
        if cmd_dict['direction'] == "forward":
            claw.ForwardM2(address, cmd_dict['speed'])
            rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = 1')
        if cmd_dict['direction'] == "backward":
            claw.BackwardM2(address, cmd_dict['speed'])
            rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = -1')
    def init_enc_vals(self):
        if self.shoulder_elbow_rot_actuators is not None:
            self.shoulder_elbow_rot_actuators.ForwardM1(shoulder_elbow_rot_addr, 0)
            self.shoulder_elbow_rot_actuators.ForwardM1(base_elbow_addr, 0)
            self.shoulder_elbow_rot_actuators.ResetEncoders(shoulder_elbow_rot_addr)
            self.shoulder_elbow_rot_actuators.ResetEncoders(base_elbow_addr)
            # self.shoulder_elbow_rot_actuators.SetM1EncoderMode(0x80, 1)
            # self.shoulder_elbow_rot_actuators.SetM2EncoderMode(0x80, 1)
            self.shoulder_elbow_rot_actuators.SetM1VelocityPID(shoulder_elbow_rot_addr, 0, 0, 0, 65)
            self.shoulder_elbow_rot_actuators.SetM1VelocityPID(base_elbow_addr, 0, 0, 0, 85)
            self.shoulder_elbow_rot_actuators.SetM1PositionPID(shoulder_elbow_rot_addr, 2750, 2000, 27500, 0, 20, 210, 1050)
            self.shoulder_elbow_rot_actuators.SetM1PositionPID(base_elbow_addr, 2400, 2000, 24000, 0, 20, 52, 950)
        if self.base_elbow_motors is not None:
            self.base_elbow_motors.ForwardM2(shoulder_elbow_rot_addr, 0)
            self.base_elbow_motors.ForwardM2(base_elbow_addr, 0)
            # self.base_elbow_motors.ResetEncoders(base_elbow_addr)
            self.base_elbow_motors.SetEncM2(shoulder_elbow_rot_addr, 0)
            self.base_elbow_motors.SetEncM2(base_elbow_addr, 0)
            self.base_elbow_motors.SetM2VelocityPID(shoulder_elbow_rot_addr, 8, 1, 0, 2450)
            self.base_elbow_motors.SetM2VelocityPID(base_elbow_addr, 8, 1, 0, 2700)
        if self.wrist_motors is not None:
            self.wrist_motors.ForwardM1(wrist_rot_addr, 0)
            self.wrist_motors.ResetEncoders(wrist_rot_addr)
            # self.wrist_motors.SetM1EncoderMode(wrist_rot_addr, 1)
            self.wrist_motors.SetM1VelocityPID(wrist_rot_addr, 0, 0, 0, 40)
            self.wrist_motors.SetM1PositionPID(wrist_rot_addr, 2300, 2000, 23000, 0, 20, 229, 1296)
    def home(self):
        print("Setting up Arm Home Position...")
        print("...Setting up Base")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM2(shoulder_elbow_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc3=enc_ret[1]
            print(enc3)
            rospy.sleep(0.01)
            if -250 < enc3 < 250:
                self.base_elbow_motors.ForwardM2(shoulder_elbow_rot_addr, 0)
                rospy.sleep(0.01)
                break
            elif enc3>=250:
                self.base_elbow_motors.BackwardM2(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM2(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)

            rospy.sleep(0.01)
        print("...Base Config Done")

        print("...Setting up Shoulder")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(shoulder_elbow_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc1=enc_ret[1]
            print(enc1)
            if 210 < enc1 < 230:
                self.shoulder_elbow_rot_actuators.ForwardM1(shoulder_elbow_rot_addr, 0)
                rospy.sleep(0.01)

                break
            elif enc1>=230:
                self.base_elbow_motors.BackwardM1(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(shoulder_elbow_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Shoulder Config Done")

        print("...Setting up Elbow")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(base_elbow_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc1=enc_ret[1]
            print(enc1)
            if 970 < enc1 < 980:
                self.shoulder_elbow_rot_actuators.ForwardM1(base_elbow_addr, 0)
                rospy.sleep(0.01)

                break
            elif enc1>=980:
                self.base_elbow_motors.BackwardM1(base_elbow_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(base_elbow_addr, 60)
            rospy.sleep(0.01)
        print("...Elbow Config Done")

    def soil_config(self):
        print("Setting up Arm Bio Soil Collection Config...")

        print("...Setting up Elbow")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(base_elbow_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc1=enc_ret[1]
            if 344 < enc1 < 364:
                self.shoulder_elbow_rot_actuators.ForwardM1(base_elbow_addr, 0)
                rospy.sleep(0.01)

                break
            elif enc1>=364:
                self.base_elbow_motors.BackwardM1(base_elbow_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(base_elbow_addr, 60)
            rospy.sleep(0.01)
        print("...Elbow Config Done")

        print("...Setting up Wrist")
        while True:
            enc_ret=self.wrist_motors.ReadEncM1(wrist_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc1=enc_ret[1]
            if 931 < enc1 < 951:
                self.shoulder_elbow_rot_actuators.ForwardM1(wrist_rot_addr, 0)
                rospy.sleep(0.01)

                break
            elif enc1>=951:
                self.base_elbow_motors.BackwardM1(wrist_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(wrist_rot_addr, 60)
            rospy.sleep(0.01)
        print("..Wrist Config Done")

        print("...Setting up Base")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM2(shoulder_elbow_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc3=enc_ret[1]
            rospy.sleep(0.01)
            if -250 < enc3 < 250:
                self.base_elbow_motors.ForwardM2(shoulder_elbow_rot_addr, 0)
                rospy.sleep(0.01)
                break
            elif enc3>=250:
                self.base_elbow_motors.BackwardM2(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM2(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)

        print("...Base Config Done")

        print("...Setting up Shoulder")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(shoulder_elbow_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc1=enc_ret[1]
            if 1000 < enc1 < 1100:
                self.shoulder_elbow_rot_actuators.ForwardM1(shoulder_elbow_rot_addr, 0)
                rospy.sleep(0.01)

                break
            elif enc1>=1100:
                self.base_elbow_motors.BackwardM1(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(shoulder_elbow_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Shoulder Config Done")

    def arm_bio1(self):
        print("Setting up Arm Bio Position 1...")

        print("...Extending Wrist")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(wrist_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc5=enc_ret[1]
            print(enc5)
            rospy.sleep(0.01)
            if 940 < enc5 < 960:
                self.wrist_motors.ForwardM1(wrist_rot_addr, 0)
                break
            elif enc5>=960:
                self.base_elbow_motors.BackwardM1(wrist_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(wrist_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Wrist Extended")

        print("...Setting up Shoulder")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(shoulder_elbow_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc1=enc_ret[1]
            print(enc1)
            rospy.sleep(0.01)
            if 232 < enc1 < 252:
                self.shoulder_elbow_rot_actuators.ForwardM1(shoulder_elbow_rot_addr, 0)
                break
            elif enc1>=252:
                self.base_elbow_motors.BackwardM1(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(shoulder_elbow_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Shoulder Config Done")

        print("...Setting up Base")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM2(shoulder_elbow_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc3=enc_ret[1]
            print(enc3)
            rospy.sleep(0.01)
            if -28950 < enc3 < -28450:
                self.base_elbow_motors.ForwardM2(shoulder_elbow_rot_addr, 0)
                break
            elif enc3>=-28450:
                self.base_elbow_motors.BackwardM2(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM2(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)

        print("...Base Config Done")

        print("...Setting up Elbow")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(base_elbow_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc2=enc_ret[1]
            print(enc2)
            rospy.sleep(0.01)
            if 973 < enc2 < 993:
                self.shoulder_elbow_rot_actuators.ForwardM1(base_elbow_addr, 0)
                break
            elif enc2>=993:
                self.base_elbow_motors.BackwardM1(base_elbow_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(base_elbow_addr, 60)
            rospy.sleep(0.01)
        print("...Elbow Config Done")

        print("...Extending Wrist")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(wrist_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc5=enc_ret[1]
            print(enc5)
            rospy.sleep(0.01)
            if 604 < enc5 < 624:
                self.wrist_motors.ForwardM1(wrist_rot_addr, 0)
                break
            elif enc5>=624:
                self.base_elbow_motors.BackwardM1(wrist_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(wrist_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Wrist Extended")

    def arm_bio2(self):
        print("Setting up Arm Bio Position 2...")
        print("...Extending Wrist")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(wrist_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc5=enc_ret[1]
            print(enc5)
            rospy.sleep(0.01)
            if 940 < enc5 < 960:
                self.wrist_motors.ForwardM1(wrist_rot_addr, 0)
                break
            elif enc5>=960:
                self.base_elbow_motors.BackwardM1(wrist_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(wrist_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Wrist Extended")

        print("...Setting up Shoulder")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(shoulder_elbow_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc1=enc_ret[1]
            print(enc1)
            rospy.sleep(0.01)
            if 197 < enc1 < 217:
                self.shoulder_elbow_rot_actuators.ForwardM1(shoulder_elbow_rot_addr, 0)
                break
            elif enc1>=217:
                self.base_elbow_motors.BackwardM1(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(shoulder_elbow_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Shoulder Config Done")

        print("...Setting up Base")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM2(shoulder_elbow_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc3=enc_ret[1]
            print(enc3)
            rospy.sleep(0.01)
            if -44831 < enc3 < -44331:
                self.base_elbow_motors.ForwardM2(shoulder_elbow_rot_addr, 0)
                break
            elif enc3>=-44331:
                self.base_elbow_motors.BackwardM2(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM2(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)

        print("...Base Config Done")

        print("...Setting up Elbow")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(base_elbow_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc2=enc_ret[1]
            print(enc2)
            rospy.sleep(0.01)
            if 967 < enc2 < 987:
                self.shoulder_elbow_rot_actuators.ForwardM1(base_elbow_addr, 0)
                break
            elif enc2>=987:
                self.base_elbow_motors.BackwardM1(base_elbow_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(base_elbow_addr, 60)
            rospy.sleep(0.01)
        print("...Elbow Config Done")

        print("...Setting up Wrist")
        print("...Extending Wrist")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(wrist_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc5=enc_ret[1]
            print(enc5)
            rospy.sleep(0.01)
            if 436 < enc5 < 456:
                self.wrist_motors.ForwardM1(wrist_rot_addr, 0)
                break
            elif enc5>=456:
                self.base_elbow_motors.BackwardM1(wrist_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(wrist_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Wrist Extended")

    def arm_bio3(self):
        print("Setting up Arm Bio Position 3...")

        print("...Extending Wrist")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(wrist_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc5=enc_ret[1]
            print(enc5)
            rospy.sleep(0.01)
            if 940 < enc5 < 960:
                self.wrist_motors.ForwardM1(wrist_rot_addr, 0)
                break
            elif enc5>=960:
                self.base_elbow_motors.BackwardM1(wrist_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(wrist_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Wrist Extended")
        print("...Setting up Shoulder")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(shoulder_elbow_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc1=enc_ret[1]
            print(enc1)
            rospy.sleep(0.01)
            if 195 < enc1 < 225:
                self.shoulder_elbow_rot_actuators.ForwardM1(shoulder_elbow_rot_addr, 0)
                break
            elif enc1>=225:
                self.base_elbow_motors.BackwardM1(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(shoulder_elbow_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Shoulder Config Done")

        print("...Setting up Base")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM2(shoulder_elbow_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc3=enc_ret[1]
            print(enc3)
            rospy.sleep(0.01)
            if 24511 < enc3 < 25011:
                self.base_elbow_motors.ForwardM2(shoulder_elbow_rot_addr, 0)
                break
            elif enc3>=25011:
                self.base_elbow_motors.BackwardM2(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM2(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)

        print("...Base Config Done")

        print("...Setting up Elbow")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(base_elbow_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc2=enc_ret[1]
            print(enc2)
            rospy.sleep(0.01)
            if 950 < enc2 < 975:
                self.shoulder_elbow_rot_actuators.ForwardM1(base_elbow_addr, 0)
                break
            elif enc2>=975:
                self.base_elbow_motors.BackwardM1(base_elbow_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(base_elbow_addr, 60)
            rospy.sleep(0.01)
        print("...Elbow Config Done")

        print("...Extending Wrist")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(wrist_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc5=enc_ret[1]
            print(enc5)
            rospy.sleep(0.01)
            if 477 < enc5 < 517:
                self.wrist_motors.ForwardM1(wrist_rot_addr, 0)
                break
            elif enc5>=517:
                self.base_elbow_motors.BackwardM1(wrist_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(wrist_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Wrist Extended")

    def arm_bio4(self):
        print("Setting up Arm Bio Position 4...")

        print("...Extending Wrist")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(wrist_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc5=enc_ret[1]
            print(enc5)
            rospy.sleep(0.01)
            if 940 < enc5 < 960:
                self.wrist_motors.ForwardM1(wrist_rot_addr, 0)
                break
            elif enc5>=960:
                self.base_elbow_motors.BackwardM1(wrist_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(wrist_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Wrist Extended")
        print("...Setting up Shoulder")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(shoulder_elbow_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc1=enc_ret[1]
            print(enc1)
            rospy.sleep(0.01)
            if 195 < enc1 < 225:
                self.shoulder_elbow_rot_actuators.ForwardM1(shoulder_elbow_rot_addr, 0)
                break
            elif enc1>=225:
                self.base_elbow_motors.BackwardM1(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(shoulder_elbow_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Shoulder Config Done")

        print("...Setting up Base")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM2(shoulder_elbow_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc3=enc_ret[1]
            print(enc3)
            rospy.sleep(0.01)
            if 42116 < enc3 < 42916:
                self.base_elbow_motors.ForwardM2(shoulder_elbow_rot_addr, 0)
                break
            elif enc3>=42916:
                self.base_elbow_motors.BackwardM2(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM2(shoulder_elbow_rot_addr, 60)
                rospy.sleep(0.01)

        print("...Base Config Done")

        print("...Setting up Elbow")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(base_elbow_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc2=enc_ret[1]
            print(enc2)
            rospy.sleep(0.01)
            if 965 < enc2 < 990:
                self.shoulder_elbow_rot_actuators.ForwardM1(base_elbow_addr, 0)
                break
            elif enc2>=990:
                self.base_elbow_motors.BackwardM1(base_elbow_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(base_elbow_addr, 60)
            rospy.sleep(0.01)
        print("...Elbow Config Done")

        print("...Extending Wrist")
        while True:
            enc_ret=self.base_elbow_motors.ReadEncM1(wrist_rot_addr)
            rospy.sleep(0.01)
            if(len(enc_ret)!=3):
                continue
            enc5=enc_ret[1]
            print(enc5)
            rospy.sleep(0.01)
            if 488 < enc5 < 508:
                self.wrist_motors.ForwardM1(wrist_rot_addr, 0)
                break
            elif enc5>=508:
                self.base_elbow_motors.BackwardM1(wrist_rot_addr, 60)
                rospy.sleep(0.01)
            else:
                self.base_elbow_motors.ForwardM1(wrist_rot_addr, 60)
            rospy.sleep(0.01)
        print("...Wrist Extended")

    # def arm_bio_uncontaminated(self):
    #     print("Setting up Arm Bio Uncontaminated Position...")
    #     print("...Setting up Shoulder")
    #     while True:
    #         _, enc1, _ = self.shoulder_elbow_rot_actuators.ReadEncM1(0x80)
    #         if 440 < enc1 < 470:
    #             self.shoulder_elbow_rot_actuators.ForwardM1(0x80, 0)
    #             break
    #         else:
    #             self.shoulder_elbow_rot_actuators.SpeedM1(0x80, -int((enc1 - 455) * 65 / abs(enc1 - 455)))
    #         rospy.sleep(0.01)
    #     print("...Shoulder Config Done")

    #     print("...Setting up Intermediate Base")
    #     while True:
    #         _, enc3, _ = self.base_elbow_motors.ReadEncM1(0x80)
    #         if -68094 < enc3 < -67894:
    #             self.base_elbow_motors.ForwardM1(0x80, 0)
    #             break
    #         else:
    #             self.base_elbow_motors.SpeedM1(0x80, -int((enc3 + 67994) * 2450 / abs((enc3 + 67994))))
    #         rospy.sleep(0.01)
    #     print("...Intermediate Base Config Done")

    #     print("...Setting up Intermediate Elbow")
    #     while True:
    #         _, enc2, _ = self.shoulder_elbow_rot_actuators.ReadEncM2(0x80)
    #         if 723 < enc2 < 743:
    #             self.shoulder_elbow_rot_actuators.ForwardM2(0x80, 0)
    #             break
    #         else:
    #             self.shoulder_elbow_rot_actuators.SpeedM2(0x80, -int((enc2 - 733) * 85 / abs(enc2 - 733)))
    #         rospy.sleep(0.01)
    #     print("...Intermediate Elbow Config Done")

    #     print("...Setting up Intermediate Wrist")
    #     while True:
    #         _, enc5, _ = self.wrist_motors.ReadEncM1(0x80)
    #         if 630 < enc5 < 650:
    #             self.wrist_motors.ForwardM1(0x80, 0)
    #             break
    #         else:
    #             self.wrist_motors.SpeedM1(0x80, -int((enc5 - 640) * 40 / abs(enc5 - 640)))
    #         rospy.sleep(0.01)
    #     print("...Intermediate Wrist Config Done")

    #     print("...Setting up Base")
    #     while True:
    #         _, enc3, _ = self.base_elbow_motors.ReadEncM1(0x80)
    #         if -90568 < enc3 < -90068:
    #             self.base_elbow_motors.ForwardM1(0x80, 0)
    #             break
    #         else:
    #             self.base_elbow_motors.SpeedM1(0x80, -int((enc3 + 90318) * 2450 / abs((enc3 + 90318))))
    #         rospy.sleep(0.01)
    #     print("...Base Config Done")

    #     print("...Setting up Elbow")
    #     while True:
    #         _, enc2, _ = self.shoulder_elbow_rot_actuators.ReadEncM2(0x80)
    #         if 785 < enc2 < 805:
    #             self.shoulder_elbow_rot_actuators.ForwardM2(0x80, 0)
    #             break
    #         else:
    #             self.shoulder_elbow_rot_actuators.SpeedM2(0x80, -int((enc2 - 795) * 85 / abs(enc2 - 795)))
    #         rospy.sleep(0.01)
    #     print("...Elbow Config Done")

    #     print("...Setting up Wrist")
    #     while True:
    #         _, enc5, _ = self.wrist_motors.ReadEncM1(0x80)
    #         if 670 < enc5 < 710:
    #             self.wrist_motors.ForwardM1(0x80, 0)
    #             break
    #         else:
    #             self.wrist_motors.SpeedM1(0x80, -int((enc5 - 700) * 40 / abs(enc5 - 700)))
    #         rospy.sleep(0.01)
    #     print("...Wrist Config Done")
    # def current_limiter(self):
    #     if self.shoulder_elbow_rot_actuators is not None:
    #         i, self.currents[0], self.currents[1] = self.shoulder_elbow_rot_actuators.ReadCurrents(0x80)
    #     if self.base_finger_motors is not None:
    #         i, self.currents[2], self.currents[3] = self.base_finger_motors.ReadCurrents(0x80)
    #     if self.wrist_rotation_motors is not None:
    #         i, self.currents[4], self.currents[5] = self.wrist_rotation_motors.ReadCurrents(0x80)
    #     # No current measurement in arduino
    #     # if self.carriage_motors is not None:
    #     #     i, self.currents[6], self.currents[7] = self.carriage_motors.ReadCurrents(0x80)
    #     for i in range(8):
    #         if self.currents[i] > self.current_threshold:
    #             self.arm_stop()
    #             self.current_exceeded = True
    #             return
    #     self.current_exceeded = False

    # def update_current(self):
    #     if self.shoulder_elbow_rot_actuators is not None:
    #         i, self.currents[0], self.currents[1] = self.shoulder_elbow_rot_actuators.ReadCurrents(0x80)
    #     if self.base_finger_motors is not None:
    #         i, self.currents[2], self.currents[3] = self.base_finger_motors.ReadCurrents(0x80)
    #     if self.wrist_rotation_motors is not None:
    #         i, self.currents[4], self.currents[5] = self.wrist_rotation_motors.ReadCurrents(0x80)
    #     # No current measurement in arduino
    #     # if self.carriage_motors is not None:
    #     #     i, self.currents[6], self.currents[7] = self.carriage_motors.ReadCurrents(0x80)
