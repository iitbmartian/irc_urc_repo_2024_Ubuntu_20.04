#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
from robotclaw import Roboclaw


class control():
    def __init__(self):
        self.control_sub = rospy.Subscriber("drive-directives",String,self.direction)
    
    def direction(self,data):
        
        if("Forward" in data):
            robot.ForwardM1(0x80,127)
            robot.ForwardM2(0x80,127)
        elif("Backward" in data):
            robot.BackwardM1(0x80,127)
            robot.BackwardM2(0x80,127)
        if("Left" in data):
            robot.BackwardM2(0x80,127)
            robot.ForwardM1(0x80,127)
        elif("Right" in data):
            robot.ForwardM2(0x80,127)
            robot.BackwardM2(0x80,127)


        









if __name__ == '__main__':
    rospy.init_node("controller",anonymous=True)
    joystick=control()
    robot=Roboclaw()
    rospy.spin()