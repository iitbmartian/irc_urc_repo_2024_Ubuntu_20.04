#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float32
import RPi.GPIO as gp  
from time import sleep
gp.setmode(gp.BOARD)  
gp.setup(12,gp.OUT)  
pwm=gp.PWM(12,50)  
pwm.start(0)


class servo():
    def __init__(self):
        self.sub = rospy.Subscriber("angle",Float32,self.angle_to_turn)

    
    def angle_to_turn(self,data):
        sig=(data/36)+5
        pwm.ChangeDutyCycle(sig)



        


        
















if __name__ == '__main__':
    rospy.init_node("subscriber",anonymous=True)
    servo1=servo()
    rospy.spin()