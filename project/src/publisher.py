#!/usr/bin/env python3
# license removed for brevity
import sys
import os
import rospy
import cv2 
import cv2.aruco as aruco
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image



class image_converter():
    
    def __init__(self):
        self.bridge=CvBridge()
        self.cap=cv2.VideoCapture(2)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,960)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,540)
        self.pub = rospy.Publisher('camera',Image, queue_size=10)
        
    def client(self):
        while not rospy.is_shutdown():
            print("sending")
            _,img=self.cap.read()
            cv2.imshow('wow',img)
            cv2.waitKey(20)
            detected_image=self.bridge.cv2_to_imgmsg(img,encoding="bgr8")
            self.pub.publish(detected_image)
           
            



            



    
if __name__ == '__main__':
    rospy.init_node('camera',anonymous=True)
    ic=image_converter()
    ic.client()