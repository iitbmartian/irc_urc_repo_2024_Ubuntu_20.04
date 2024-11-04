#!/usr/bin/env python3
# license removed for brevity
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import *
from geometry_msgs.msg import Twist

class Subscriber():
    def __init__(self):
        self.joy_sub = rospy.Subscriber("joy",Joy,self.callback)
        self.joy_pub= rospy.Publisher("drive-directives",String,queue_size=10)
        self.joy_pub= rospy.Publisher("cmd_vel",Twist,queue_size=10)
        self.sentence=String()
        self.control=Twist()
    
    def callback(self,Joy):
        arr=Joy.axes
        if(arr[7]==1):
            direction="Forward"
        elif(arr[7]==0):
            direction="Stop"
        elif(arr[7]==-1):
            direction="Backward"
        if(arr[6]==1):
            direction1="Left"
        elif(arr[6]==0):
            direction1="Stop"
        elif(arr[6]==-1):
            direction1="Right"

        self.sentence.data=f"{direction} and {direction1}"
        self.joy_pub.publish(self.sentence)
        print(self.sentence)










if __name__ == '__main__':
    rospy.init_node("sachin",anonymous=True)
    joystick=Subscriber()
    rospy.spin()