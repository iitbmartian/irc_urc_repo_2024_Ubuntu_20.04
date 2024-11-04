#!/usr/bin/env python3

from std_msgs.msg import String
frontClaw_address=0x80
centerClaw_address=0x81
backClaw_address=0x83


class Drive:
    def __init__(self, driver):
        self.DriveClaw = driver
        self.direction = "stop"
        self.speed = 0
        self.current_exceeded = False
        self.currents = [0, 0, 0, 0, 0, 0]
        self.current_threshold = 1000
        self.mode = "manual"

    def fwd(self):
        self.DriveClaw.ForwardM1(frontClaw_address, self.speed)
        self.DriveClaw.ForwardM2(frontClaw_address, self.speed)
        self.DriveClaw.ForwardM1(centerClaw_address, int(self.speed / 1.5))
        self.DriveClaw.ForwardM2(centerClaw_address, self.speed)
        self.DriveClaw.ForwardM1(backClaw_address, self.speed)
        self.DriveClaw.BackwardM2(backClaw_address, self.speed)

    def bwd(self):
        self.DriveClaw.BackwardM1(frontClaw_address, self.speed)
        self.DriveClaw.BackwardM2(frontClaw_address, self.speed)
        self.DriveClaw.BackwardM1(centerClaw_address, int(self.speed / 1.5))
        self.DriveClaw.BackwardM2(centerClaw_address, self.speed)
        self.DriveClaw.BackwardM1(backClaw_address, self.speed)
        self.DriveClaw.ForwardM2(backClaw_address, self.speed)

    def stop(self):
        self.DriveClaw.ForwardM1(frontClaw_address, 0)
        self.DriveClaw.ForwardM1(centerClaw_address, 0)
        self.DriveClaw.ForwardM1(backClaw_address, 0)
        self.DriveClaw.ForwardM2(frontClaw_address, 0)
        self.DriveClaw.ForwardM2(centerClaw_address, 0)
        self.DriveClaw.ForwardM2(backClaw_address, 0)

    def right(self):
        self.DriveClaw.ForwardM1(frontClaw_address, self.speed)
        self.DriveClaw.BackwardM2(frontClaw_address, self.speed)
        self.DriveClaw.ForwardM1(centerClaw_address, int(self.speed / 1.5))
        self.DriveClaw.BackwardM2(centerClaw_address, self.speed)
        self.DriveClaw.ForwardM1(backClaw_address, self.speed)
        self.DriveClaw.ForwardM2(backClaw_address, self.speed)

    def left(self):
        self.DriveClaw.BackwardM1(frontClaw_address, self.speed)
        self.DriveClaw.ForwardM2(frontClaw_address, self.speed)
        self.DriveClaw.BackwardM1(centerClaw_address, int(self.speed / 1.5))
        self.DriveClaw.ForwardM2(centerClaw_address, self.speed)
        self.DriveClaw.BackwardM1(backClaw_address, self.speed)
        self.DriveClaw.BackwardM2(backClaw_address, self.speed)

    def update_steer(self):
        if self.direction == "stop":
            self.stop()
        elif self.direction == "forward":
            self.fwd()
        elif self.direction == "clockwise":
            self.right()
        elif self.direction == "backward":
            self.bwd()
        elif self.direction == "anticlockwise":
            self.left()

    def drive_callback(self, inp):
        self.speed, self.direction, self.mode = int(inp.speed), inp.direction, inp.mode
        if self.direction == "stop":
            pass
        elif self.direction == "forward":
            # rospy.loginfo('Drive: Rover commanded to move Forward')
            print("forward")
        elif self.direction == "clockwise":
            # rospy.loginfo('Drive: Rover commanded to turn Clockwise')
            print("clockwise")
        elif self.direction == "backward":
            # rospy.loginfo('Drive: Rover commanded to move Backward')
            print("backward")
        elif self.direction == "anticlockwise":
            # rospy.loginfo('Drive: Rover commanded to turn Anti-Clockwise')
            print("anticlockwise")

    def current_limiter(self):
        (i, self.currents[0], self.currents[1]) = self.DriveClaw.ReadCurrents(frontClaw_address)
        (i, self.currents[2], self.currents[3]) = self.DriveClaw.ReadCurrents(centerClaw_address)
        (i, self.currents[4], self.currents[5]) = self.DriveClaw.ReadCurrents(backClaw_address)
        for i in range(6):
            if self.currents[i] > self.current_threshold:
                self.stop()
                self.current_exceeded = True
                return
        self.current_exceeded = False

    def update_current(self):
        (i, self.currents[0], self.currents[1]) = self.DriveClaw.ReadCurrents(frontClaw_address)
        (i, self.currents[2], self.currents[3]) = self.DriveClaw.ReadCurrents(centerClaw_address)
        (i, self.currents[4], self.currents[5]) = self.DriveClaw.ReadCurrents(backClaw_address)


