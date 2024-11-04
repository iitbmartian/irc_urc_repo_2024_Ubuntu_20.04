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
from aruco import identifier
msg=Pose
msg.position.x=0
msg.position.y=0
msg.position.z=0
msg.orientation.x=0
msg.orientation.y=0
msg.orientation.z=0
msg.orientation.w=0


def calculate_distance(req):




if __name__ == '__main__':
    rospy.init_node('direction', anonymous=True)
    service=rospy.Service('direction', direction, calculate_distance )