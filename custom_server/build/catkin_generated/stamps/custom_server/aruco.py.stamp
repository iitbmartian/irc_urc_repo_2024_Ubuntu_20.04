#!/usr/bin/env python3
# license removed for brevity
import numpy
import os
import rospy
import cv2 
import cv2.aruco as aruco
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import Int32MultiArray
from custom_server.srv import *
from custom_server.msg import *
import math


class identifier():
  def __init__(self):
    self.bridge = CvBridge()
    service1=rospy.Service('aruco_detection', aruco_detection, self.findAruco )
    service2=rospy.Service('direction', direction, self.calculate )
    rospy.spin()
  def calculate(self,req):
      if self.ids is None:
        print("e")
        return directionResponse(0,0,0)
      else:
        k=self.ids.index(req.ids)
        # l=len(self.ids)
        
          
        sachin=numpy.array(self.bbox[k]).flatten()

        
        lt_x=sachin[0]
        lt_y=sachin[1]
        rd_x=sachin[4]
        rd_y=sachin[5]
        centre_x= (lt_x+rd_x)/2
        centre_y=(lt_y+rd_y)/2
        a=req.origin.position.x
        b=req.origin.position.y
        c=req.origin.orientation.z
        distance_to_marker=math.sqrt(pow(centre_x-a,2)+pow(centre_y-b,2))
        angle=(math.atan((centre_y-b)/(centre_x-a)))-c
        return directionResponse(distance_to_marker,angle)


      



  def findAruco(self,req):
    img=self.bridge.imgmsg_to_cv2(req.detected_image, 'bgr8')
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    arucoDict=aruco.Dictionary_get(aruco.DICT_4X4_100)
    arucoParams=aruco.DetectorParameters_create()
    bbox,ids,_=aruco.detectMarkers(gray,arucoDict,parameters=arucoParams)
    
  
    # aruco.drawDetectedMarkers(img,bbox)
    # cv2.imshow('images', img)
    
    if ids is None:
      cstm_msg = custom()
      cstm_msg.answer.data=[]
      self.ids=None
      self.bbox=None
      
      return aruco_detectionResponse(cstm_msg)
    else:
      # print(ids.flatten())
      # print(numpy.array(bbox).flatten())
     
      self.bbox=bbox
      wow_msg=custom()
      
      ids=ids.flatten().tolist()
      self.ids=ids
      bbox_array=numpy.array(bbox)
      bbox_array=bbox_array.flatten().tolist()
      
      wow_msg.answer.data=ids+bbox_array
      return aruco_detectionResponse(wow_msg)
      

if __name__ == '__main__':
  rospy.init_node('identifier', anonymous=True)
  aruco_b=identifier()

    
    



