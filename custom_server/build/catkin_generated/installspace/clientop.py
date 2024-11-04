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

class image_converter():
    
    def __init__(self):
        self.bridge=CvBridge()
        self.cap=cv2.VideoCapture(0)
        self.aruco_detect=rospy.ServiceProxy("/aruco_detection",aruco_detection)
        
    def client(self):
        rospy.wait_for_service("/aruco_detection")
        while not rospy.is_shutdown():
            print("sending")
            _,img=self.cap.read()
            cv2.imshow('wow',img)
            cv2.waitKey(20)
            
            detected_image=self.bridge.cv2_to_imgmsg(img,encoding="bgr8")
            response=str(self.aruco_detect(aruco_detectionRequest(detected_image)))
            print(response)
            



            



    
if __name__ == '__main__':
    rospy.init_node('client',anonymous=True)
    ic=image_converter()
    ic.client()
    
    
