#!/usr/bin/env python

import rospy


class Arm:

    def __init__(self, claw1, claw2, claw3):
        self.shoulder_elbow_actuators = claw1
        self.base_elbow_motors = claw2
        self.wrist_motor = claw3
        self.current_exceeded = False
        self.currents = [0, 0, 0, 0, 0, 0]
        self.current_threshold = 1000
        self.shoulder_actuator = {'name': "Shoulder Actuator", 'speed': 0,
                                  'direction': "stop"}  # Claw1M1; Stop: 0, Up: 1, Down: -1
        self.elbow_actuator = {'name': "Elbow Actuator", 'speed': 0,
                               'direction': "stop"}  # Claw1M2; Stop: 0, Extend: 1, Contract: -1\
        self.base_motor = {'name': "Base Rotation", 'speed': 0,
                           'direction': "stop"}  # Claw3M1; Stop: 0, Clockwise: 1, Anticlockwise: -1
        self.wrist_actuator = {'name': "Wrist Actuator", 'speed': 0,
                               'direction': "stop"}  # Claw2M2; Stop: 0, .: 1, .: -1
        self.elbow_motor = {'name': "Elbow Rotation", 'speed': 0,
                            'direction': "stop"}  #
        self.config = 0
        self.isconfig = False
        self.configComplete = False
        self.runtimer = rospy.Rate(10)

    def init_enc_vals(self):
        if self.shoulder_elbow_actuators is not None:
            self.shoulder_elbow_actuators.ForwardM1(0x80, 0)
            self.shoulder_elbow_actuators.ForwardM2(0x80, 0)
            self.shoulder_elbow_actuators.ResetEncoders(0x80)
            self.shoulder_elbow_actuators.SetM1EncoderMode(0x80, 1)
            self.shoulder_elbow_actuators.SetM2EncoderMode(0x80, 1)
            self.shoulder_elbow_actuators.SetM1VelocityPID(0x80, 0, 0, 0, 65)
            self.shoulder_elbow_actuators.SetM2VelocityPID(0x80, 0, 0, 0, 85)
            self.shoulder_elbow_actuators.SetM1PositionPID(0x80, 2750, 2000, 27500, 0, 20, 210, 1050)
            self.shoulder_elbow_actuators.SetM2PositionPID(0x80, 2400, 2000, 24000, 0, 20, 52, 950)
        if self.base_elbow_motors is not None:
            self.base_elbow_motors.ForwardM1(0x80, 0)
            self.base_elbow_motors.ForwardM2(0x80, 0)
            self.base_elbow_motors.ResetEncoders(0x80)
            self.base_elbow_motors.SetEncM1(0x80, 0)
            self.base_elbow_motors.SetEncM2(0x80, 0)
            self.base_elbow_motors.SetM1VelocityPID(0x80, 8, 1, 0, 2450)
            self.base_elbow_motors.SetM2VelocityPID(0x80, 8, 1, 0, 2700)
        if self.wrist_motor is not None:
            self.wrist_motor.ForwardM1(0x80, 0)
            self.wrist_motor.ResetEncoders(0x80)
            self.wrist_motor.SetM1EncoderMode(0x80, 1)
            self.wrist_motor.SetM1VelocityPID(0x80, 0, 0, 0, 40)
            self.wrist_motor.SetM1PositionPID(0x80, 2300, 2000, 23000, 0, 20, 229, 1296)

    def home(self):
        print("Setting up Arm Home Position...")
        print("...Setting up Base")
        while True:
            _, enc3, _ = self.base_elbow_motors.ReadEncM1(0x80)
            if -250 < enc3 < 250:
                self.base_elbow_motors.ForwardM1(0x80, 0)
                break
            else:
                self.base_elbow_motors.SpeedM1(0x80, -int((enc3) * 2450 / abs((enc3))))
            self.runtimer.sleep()
        print("...Base Config Done")

        print("...Setting up Shoulder")
        while True:
            _, enc1, _ = self.shoulder_elbow_actuators.ReadEncM1(0x80)
            if 210 < enc1 < 230:
                self.shoulder_elbow_actuators.ForwardM1(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM1(0x80, -int((enc1 - 220) * 65 / abs(enc1 - 220)))
            self.runtimer.sleep()
        print("...Shoulder Config Done")

        print("...Setting up Elbow")
        while True:
            _, enc2, _ = self.shoulder_elbow_actuators.ReadEncM2(0x80)
            if 970 < enc2 < 980:
                self.shoulder_elbow_actuators.ForwardM2(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM2(0x80, -int((enc2 - 975) * 85 / abs(enc2 - 975)))
            self.runtimer.sleep()
        print("...Elbow Config Done")

    def soil_config(self):
        print("Setting up Arm Bio Soil Collection Config...")

        print("...Setting up Elbow")
        while True:
            _, enc2, _ = self.shoulder_elbow_actuators.ReadEncM2(0x80)
            if 344 < enc2 < 364:
                self.shoulder_elbow_actuators.ForwardM2(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM2(0x80, -int((enc2 - 354) * 85 / abs(enc2 - 354)))
            self.runtimer.sleep()
        print("...Elbow Config Done")

        print("...Setting up Wrist")
        while True:
            _, enc5, _ = self.wrist_motor.ReadEncM1(0x80)
            if 931 < enc5 < 951:
                self.wrist_motor.ForwardM1(0x80, 0)
                break
            else:
                self.wrist_motor.SpeedM1(0x80, -int((enc5 - 941) * 40 / abs(enc5 - 941)))
            self.runtimer.sleep()
        print("..Wrist Config Done")

        print("...Setting up Base")
        while True:
            _, enc3, _ = self.base_elbow_motors.ReadEncM1(0x80)
            if -250 < enc3 < 250:
                self.base_elbow_motors.ForwardM1(0x80, 0)
                break
            else:
                self.base_elbow_motors.SpeedM1(0x80, -int((enc3) * 2450 / abs((enc3))))
            self.runtimer.sleep()
        print("...Base Config Done")

        print("...Setting up Shoulder")
        while True:
            _, enc1, _ = self.shoulder_elbow_actuators.ReadEncM1(0x80)
            if 1050 < enc1 < 1127:
                self.shoulder_elbow_actuators.ForwardM1(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM1(0x80, -int((enc1 - 1102) * 65 / abs(enc1 - 1102)))
            self.runtimer.sleep()
        print("...Shoulder Config Done")

    def arm_bio1(self):
        print("Setting up Arm Bio Position 1...")

        print("...Setting up Shoulder")
        while True:
            _, enc1, _ = self.shoulder_elbow_actuators.ReadEncM1(0x80)
            if 257 < enc1 < 287:
                self.shoulder_elbow_actuators.ForwardM1(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM1(0x80, -int((enc1 - 267) * 65 / abs(enc1 - 267)))
            self.runtimer.sleep()
        print("...Shoulder Config Done")

        print("...Setting up Base")
        while True:
            _, enc3, _ = self.base_elbow_motors.ReadEncM1(0x80)
            if -27957 < enc3 < -27057:
                self.base_elbow_motors.ForwardM1(0x80, 0)
                break
            else:
                self.base_elbow_motors.SpeedM1(0x80, -int((enc3 + 27457) * 2450 / abs((enc3 + 27457))))
            self.runtimer.sleep()
        print("...Base Config Done")

        print("...Setting up Elbow")
        while True:
            _, enc2, _ = self.shoulder_elbow_actuators.ReadEncM2(0x80)
            if 962 < enc2 < 980:
                self.shoulder_elbow_actuators.ForwardM2(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM2(0x80, -int((enc2 - 972) * 85 / abs(enc2 - 972)))
            self.runtimer.sleep()
        print("...Elbow Config Done")

        print("...Setting up Wrist")
        while True:
            _, enc5, _ = self.wrist_motor.ReadEncM1(0x80)
            if 568 < enc5 < 588:
                self.wrist_motor.ForwardM1(0x80, 0)
                break
            else:
                self.wrist_motor.SpeedM1(0x80, -int((enc5 - 578) * 40 / abs(enc5 - 578)))
            self.runtimer.sleep()
        print("...Wrist Config Done")

    def arm_bio2(self):
        print("Setting up Arm Bio Position 2...")
        print("...Setting up Shoulder")
        while True:
            _, enc1, _ = self.shoulder_elbow_actuators.ReadEncM1(0x80)
            if 257 < enc1 < 287:
                self.shoulder_elbow_actuators.ForwardM1(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM1(0x80, -int((enc1 - 267) * 65 / abs(enc1 - 267)))
            self.runtimer.sleep()
        print("...Shoulder Config Done")

        print("...Setting up Base")
        while True:
            _, enc3, _ = self.base_elbow_motors.ReadEncM1(0x80)
            if -27957 < enc3 < -27057:
                self.base_elbow_motors.ForwardM1(0x80, 0)
                break
            else:
                self.base_elbow_motors.SpeedM1(0x80, -int((enc3 + 27457) * 2450 / abs((enc3 + 27457))))
            self.runtimer.sleep()
        print("...Base Config Done")

        print("...Setting up Elbow")
        while True:
            _, enc2, _ = self.shoulder_elbow_actuators.ReadEncM2(0x80)
            if 962 < enc2 < 980:
                self.shoulder_elbow_actuators.ForwardM2(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM2(0x80, -int((enc2 - 972) * 85 / abs(enc2 - 972)))
            self.runtimer.sleep()
        print("...Elbow Config Done")

        print("...Setting up Wrist")
        while True:
            _, enc5, _ = self.wrist_motor.ReadEncM1(0x80)
            if 440 < enc5 < 460:
                self.wrist_motor.ForwardM1(0x80, 0)
                break
            else:
                self.wrist_motor.SpeedM1(0x80, -int((enc5 - 450) * 40 / abs(enc5 - 450)))
            self.runtimer.sleep()
        print("...Wrist Config Done")

    def arm_bio3(self):
        print("Setting up Arm Bio Position 3...")

        print("...Setting up Shoulder")
        while True:
            _, enc1, _ = self.shoulder_elbow_actuators.ReadEncM1(0x80)
            if 257 < enc1 < 287:
                self.shoulder_elbow_actuators.ForwardM1(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM1(0x80, -int((enc1 - 267) * 65 / abs(enc1 - 267)))
            self.runtimer.sleep()
        print("...Shoulder Config Done")

        print("...Setting up Base")
        while True:
            _, enc3, _ = self.base_elbow_motors.ReadEncM1(0x80)
            if 27057 < enc3 < 27957:
                self.base_elbow_motors.ForwardM1(0x80, 0)
                break
            else:
                self.base_elbow_motors.SpeedM1(0x80, -int((enc3 - 27457) * 2450 / abs((enc3 - 27457))))
            self.runtimer.sleep()
        print("...Base Config Done")

        print("...Setting up Elbow")
        while True:
            _, enc2, _ = self.shoulder_elbow_actuators.ReadEncM2(0x80)
            if 962 < enc2 < 980:
                self.shoulder_elbow_actuators.ForwardM2(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM2(0x80, -int((enc2 - 972) * 85 / abs(enc2 - 972)))
            self.runtimer.sleep()
        print("...Elbow Config Done")

        print("...Setting up Wrist")
        while True:
            _, enc5, _ = self.wrist_motor.ReadEncM1(0x80)
            if 568 < enc5 < 588:
                self.wrist_motor.ForwardM1(0x80, 0)
                break
            else:
                self.wrist_motor.SpeedM1(0x80, -int((enc5 - 578) * 40 / abs(enc5 - 578)))
            self.runtimer.sleep()
        print("...Wrist Config Done")

    def arm_bio4(self):
        print("Setting up Arm Bio Position 4...")
        print("...Setting up Shoulder")
        while True:
            _, enc1, _ = self.shoulder_elbow_actuators.ReadEncM1(0x80)
            if 257 < enc1 < 287:
                self.shoulder_elbow_actuators.ForwardM1(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM1(0x80, -int((enc1 - 267) * 65 / abs(enc1 - 267)))
            self.runtimer.sleep()
        print("...Shoulder Config Done")

        print("...Setting up Base")
        while True:
            _, enc3, _ = self.base_elbow_motors.ReadEncM1(0x80)
            if 27057 < enc3 < 27957:
                self.base_elbow_motors.ForwardM1(0x80, 0)
                break
            else:
                self.base_elbow_motors.SpeedM1(0x80, -int((enc3 - 27457) * 2450 / abs((enc3 - 27457))))
            self.runtimer.sleep()
        print("...Base Config Done")

        print("...Setting up Elbow")
        while True:
            _, enc2, _ = self.shoulder_elbow_actuators.ReadEncM2(0x80)
            if 962 < enc2 < 980:
                self.shoulder_elbow_actuators.ForwardM2(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM2(0x80, -int((enc2 - 972) * 85 / abs(enc2 - 972)))
            self.runtimer.sleep()
        print("...Elbow Config Done")

        print("...Setting up Wrist")
        while True:
            _, enc5, _ = self.wrist_motor.ReadEncM1(0x80)
            if 440 < enc5 < 460:
                self.wrist_motor.ForwardM1(0x80, 0)
                break
            else:
                self.wrist_motor.SpeedM1(0x80, -int((enc5 - 450) * 40 / abs(enc5 - 450)))
            self.runtimer.sleep()
        print("...Wrist Config Done")

    def arm_bio_uncontaminated(self):
        print("Setting up Arm Bio Uncontaminated Position...")
        print("...Setting up Shoulder")
        while True:
            _, enc1, _ = self.shoulder_elbow_actuators.ReadEncM1(0x80)
            if 343 < enc1 < 383:
                self.shoulder_elbow_actuators.ForwardM1(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM1(0x80, -int((enc1 - 363) * 65 / abs(enc1 - 363)))
            self.runtimer.sleep()
        print("...Shoulder Config Done")

        print("...Setting up Elbow")
        while True:
            _, enc2, _ = self.shoulder_elbow_actuators.ReadEncM2(0x80)
            if 761 < enc2 < 801:
                self.shoulder_elbow_actuators.ForwardM2(0x80, 0)
                break
            else:
                self.shoulder_elbow_actuators.SpeedM2(0x80, -int((enc2 - 781) * 85 / abs(enc2 - 781)))
            self.runtimer.sleep()
        print("...Elbow Config Done")

        print("...Setting up Wrist")
        while True:
            _, enc5, _ = self.wrist_motor.ReadEncM1(0x80)
            if 544 < enc5 < 564:
                self.wrist_motor.ForwardM1(0x80, 0)
                break
            else:
                self.wrist_motor.SpeedM1(0x80, -int((enc5 - 554) * 40 / abs(enc5 - 554)))
            self.runtimer.sleep()
        print("...Wrist Config Done")

        print("...Setting up Base")
        while True:
            _, enc3, _ = self.base_elbow_motors.ReadEncM1(0x80)
            if 56572 < enc3 < 57172:
                self.base_elbow_motors.ForwardM1(0x80, 0)
                break
            else:
                self.base_elbow_motors.SpeedM1(0x80, -int((enc3 - 56872) * 2450 / abs((enc3 - 56872))))
            self.runtimer.sleep()
        print("...Base Config Done")

    def update_arm_steer(self):
        if (self.isconfig == True):
            if self.config == 1:
                self.arm_bio1()
                self.configComplete = True
                self.isconfig = False
            elif self.config == 2:
                self.arm_bio2()
                self.configComplete = True
                self.isconfig = False
            elif self.config == 3:
                self.arm_bio3()
                self.configComplete = True
                self.isconfig = False
            elif self.config == 4:
                self.arm_bio4()
                self.configComplete = True
                self.isconfig = False
            elif self.config == 5:
                self.arm_bio_uncontaminated()
                self.configComplete = True
                self.isconfig = False
            elif self.config == 6:
                self.soil_config()
                self.configComplete = True
                self.isconfig = False
            elif self.config == 0:
                self.home()
                self.configComplete = True
                self.isconfig = False
        else:
            if self.shoulder_elbow_actuators is not None:
                _, enc1, _ = self.shoulder_elbow_actuators.ReadEncM1(0x80)
                _, enc2, _ = self.shoulder_elbow_actuators.ReadEncM2(0x80)
                if 210 < enc1 < 230:
                    if self.shoulder_actuator['direction'] == 'forward':
                        self.runclawM1(self.shoulder_elbow_actuators, self.shoulder_actuator)
                    else:
                        self.shoulder_elbow_actuators.ForwardM1(0x80, 0)
                elif 250 <= enc1 < 1100:
                    self.runclawM1(self.shoulder_elbow_actuators, self.shoulder_actuator)
                else:
                    if self.shoulder_actuator['direction'] == 'backward':
                        self.runclawM1(self.shoulder_elbow_actuators, self.shoulder_actuator)
                    else:
                        self.shoulder_elbow_actuators.ForwardM1(0x80, 0)

                if 52 < enc2 < 62:
                    if self.elbow_actuator['direction'] == 'forward':
                        self.runclawM2(self.shoulder_elbow_actuators, self.elbow_actuator)
                    else:
                        self.shoulder_elbow_actuators.ForwardM2(0x80, 0)
                elif 62 <= enc2 < 970:
                    self.runclawM2(self.shoulder_elbow_actuators, self.elbow_actuator)
                else:
                    if self.elbow_actuator['direction'] == 'backward':
                        self.runclawM2(self.shoulder_elbow_actuators, self.elbow_actuator)
                    else:
                        self.shoulder_elbow_actuators.ForwardM2(0x80, 0)

            if self.base_elbow_motors is not None:
                _, enc3, _ = self.base_elbow_motors.ReadEncM1(0x80)
                _, enc4, _ = self.base_elbow_motors.ReadEncM2(0x80)
                self.runclawM1(self.base_elbow_motors, self.base_motor)
                if -28090 < enc4 < -28190:
                    if self.elbow_motor['direction'] == 'forward':
                        self.runclawM2(self.base_elbow_motors, self.elbow_motor)
                    else:
                        self.base_elbow_motors.ForwardM2(0x80, 0)
                elif -28090 <= enc4 < 28090:
                    self.runclawM2(self.base_elbow_motors, self.elbow_motor)
                else:
                    if self.elbow_motor['direction'] == 'backward':
                        self.runclawM2(self.base_elbow_motors, self.elbow_motor)
                    else:
                        self.base_elbow_motors.ForwardM2(0x80, 0)

            if self.wrist_motor is not None:
                _, enc5, _ = self.wrist_motor.ReadEncM1(0x80)
                if 229 < enc5 < 239:
                    if self.wrist_actuator['direction'] == 'forward':
                        self.runclawM1(self.wrist_motor, self.wrist_actuator)
                    else:
                        self.wrist_motor.ForwardM1(0x80, 0)
                elif 239 <= enc5 < 1286:
                    self.runclawM1(self.wrist_motor, self.wrist_actuator)
                else:
                    if self.wrist_actuator['direction'] == 'backward':
                        self.runclawM1(self.wrist_motor, self.wrist_actuator)
                    else:
                        self.wrist_motor.ForwardM1(0x80, 0)

    def arm_callback(self, inp):
        if inp.bio == 'y':
            self.config = int(input('Enter Configuration: '))
            self.isconfig = True
            self.configComplete = False
        elif self.configComplete:
            self.config = 0
            self.isconfig = False
        self.shoulder_actuator['speed'], self.shoulder_actuator['direction'] = int(
            inp.shoulder_actuator.speed), inp.shoulder_actuator.direction
        self.elbow_actuator['speed'], self.elbow_actuator['direction'] = int(
            inp.elbow_actuator.speed), inp.elbow_actuator.direction
        self.base_motor['speed'], self.base_motor['direction'] = int(inp.base_motor.speed), inp.base_motor.direction
        self.wrist_actuator['speed'], self.wrist_actuator['direction'] = int(
            inp.wrist_actuator.speed), inp.wrist_actuator.direction
        self.elbow_motor['speed'], self.elbow_motor['direction'] = int(inp.elbow_motor.speed), inp.elbow_motor.direction

    def arm_stop(self):
        if self.shoulder_elbow_actuators is not None:
            self.shoulder_elbow_actuators.ForwardM1(0x80, 0)
            self.shoulder_elbow_actuators.ForwardM2(0x80, 0)
        if self.base_elbow_motors is not None:
            while True:
                _, enc3, _ = self.base_elbow_motors.ReadEncM1(0x80)
                if enc3 > 250 or enc3 < -250:
                    self.base_elbow_motors.SpeedM1(0x80, -int(2450 * enc3 / abs(enc3)))
                else:
                    self.base_elbow_motors.ForwardM1(0x80, 0)
                    break
            while True:
                _, enc4, _ = self.base_elbow_motors.ReadEncM2(0x80)
                if enc4 < -100 or enc4 > 100:
                    self.base_elbow_motors.SpeedM2(0x80, -int(2700 * enc4 / abs(enc4)))
                else:
                    self.base_elbow_motors.ForwardM2(0x80, 0)
                    break
        if self.wrist_motor is not None:
            self.wrist_motor.ForwardM1(0x80, 0)
            self.wrist_motor.ForwardM2(0x80, 0)

    def arm_break(self):
        rospy.loginfo('Arm: ' + "Arm commanded to break")
        if self.shoulder_elbow_actuators is not None:
            self.shoulder_elbow_actuators.ForwardM1(0x80, 0)
            self.shoulder_elbow_actuators.ForwardM2(0x80, 0)
        if self.base_elbow_motors is not None:
            self.base_elbow_motors.ForwardM1(0x80, 0)
            self.base_elbow_motors.ForwardM2(0x80, 0)
        if self.wrist_motor is not None:
            self.wrist_motor.ForwardM1(0x80, 0)
            self.wrist_motor.ForwardM2(0x80, 0)

    def runclawM1(self, claw, cmd_dict):
        if cmd_dict['direction'] == "stop":
            claw.ForwardM1(0x80, 0)
            # rospy.loginfo('Arm: '+ cmd_dict['name'] + ' commanded to stop')
        if cmd_dict['direction'] == "forward":
            claw.ForwardM1(0x80, cmd_dict['speed'])
            rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = 1')
        if cmd_dict['direction'] == "backward":
            claw.BackwardM1(0x80, cmd_dict['speed'])
            rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = -1')

    def runclawM2(self, claw, cmd_dict):
        if cmd_dict['direction'] == "stop":
            claw.ForwardM2(0x80, 0)
            # rospy.loginfo('Arm: '+ cmd_dict['name'] + ' commanded to stop')
        if cmd_dict['direction'] == "forward":
            claw.ForwardM2(0x80, cmd_dict['speed'])
            rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = 1')
        if cmd_dict['direction'] == "backward":
            claw.BackwardM2(0x80, cmd_dict['speed'])
            rospy.loginfo('Arm: ' + cmd_dict['name'] + ' commanded to move in Direction = -1')

    def current_limiter(self):
        if self.shoulder_elbow_actuators is not None:
            i, self.currents[0], self.currents[1] = self.shoulder_elbow_actuators.ReadCurrents(0x80)
        if self.base_elbow_motors is not None:
            i, self.currents[2], self.currents[3] = self.base_elbow_motors.ReadCurrents(0x80)
        if self.wrist_motor is not None:
            i, self.currents[4], self.currents[5] = self.wrist_motor.ReadCurrents(0x80)
        for i in range(6):
            if self.currents[i] > self.current_threshold:
                self.arm_break()
                self.current_exceeded = True
                return
        self.current_exceeded = False

    def update_current(self):
        if self.shoulder_elbow_actuators is not None:
            i, self.currents[0], self.currents[1] = self.shoulder_elbow_actuators.ReadCurrents(0x80)
        if self.base_elbow_motors is not None:
            i, self.currents[2], self.currents[3] = self.base_elbow_motors.ReadCurrents(0x80)
        if self.wrist_motor is not None:
            i, self.currents[4], self.currents[5] = self.wrist_motor.ReadCurrents(0x80)