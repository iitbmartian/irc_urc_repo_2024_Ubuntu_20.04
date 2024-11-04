#!/usr/bin/env python3
# license removed for brevity
import sys
import os
import rospy
import cv2 
import cv2.aruco as aruco
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import *
from custom_server.srv import *
from geometry_msgs.msg import Pose




class distance_calculator():
    def __init__(self):
        origin=Pose()
        origin.position.x=float(input("Enter x coordinate of rover: \n"))
        origin.position.y=float(input("Enter y coordinate of rover: \n"))
        origin.orientation.z=float(input("Enter angle made by rover with x axis: \n"))
        self.ids=int(input("Enter the aruco id \n"))
        self.origin=origin
        self.direction_detect=rospy.ServiceProxy("direction",direction)
    def client(self):
        rospy.wait_for_service("direction")
        while not rospy.is_shutdown():
            response2=self.direction_detect(directionRequest(self.origin,self.ids))
            answer=[response2.distance_to_marker,response2.angle]
            print(answer)
            
            












if __name__ == '__main__':
    rospy.init_node('client1',anonymous=True)
    ic=distance_calculator()
    ic.client()
    
    
