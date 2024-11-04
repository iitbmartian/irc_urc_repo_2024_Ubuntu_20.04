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
from project.srv import *
import numpy

class image_receiver():
    
    def __init__(self):
        self.pub=rospy.Publisher('drive-directives',String, queue_size=10)
        self.aruco_detect=rospy.ServiceProxy("/aruco_detection",aruco_detection)
        self.sentence=String()
        self.sub=rospy.Subscriber("camera", Image, self.client)
        
    
        

        
    def client(self,sachin):
        rospy.wait_for_service("/aruco_detection")
        
        try:
            response=self.aruco_detect(aruco_detectionRequest(sachin))
            if(response.orient.data=="1"):
                 self.sentence.data="Stop and Right"
                 self.pub.publish(self.sentence)
            elif(response.orient.data=="2"):
                 self.sentence.data="Blink"
                 self.pub.publish(self.sentence)
                 rospy.sleep(3)
                 
            else:
                if(response.angle>=(numpy.pi/10)):
                        self.sentence.data="Stop and Right"
                        self.pub.publish(self.sentence)
                elif(response.angle<=(-(numpy.pi/10))):
                        self.sentence.data="Stop and Left" 
                        self.pub.publish(self.sentence)
                elif(response.distance_to_marker>=20):
                    self.sentence.data="Forward and Stop"
                    self.pub.publish(self.sentence)
                else:
                     self.sentence.data="Stop and Stop"
                     self.pub.publish(self.sentence)
        except:
              print("e")
              self.sentence.data="Stop and Stop"
              self.pub.publish(self.sentence)


        

             
                 
                 
                     
             
            



            



    
if __name__ == '__main__':
    rospy.init_node('client',anonymous=True)
    ic=image_receiver()
    rospy.spin()
   