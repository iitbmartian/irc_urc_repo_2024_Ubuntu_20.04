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
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from project.srv import *
import math
import numpy
import signal
# def SignalHandler_SIGINT(SignalNumber,Frame):
#      print('End')



# #register the signal with Signal handler
# signal.signal(signal.SIGINT,SignalHandler_SIGINT)
# distance_to_marker=0
# angle=0
# aruco_detectionResponse(distance_to_marker,angle)

m=51
class identifier():

  def __init__(self):
    self.bridge = CvBridge()
    self.origin=Pose()
    self.orient=String()
    service1=rospy.Service('aruco_detection', aruco_detection, self.findAruco )

    
    rospy.spin()

  def findAruco(self,req):
        global m
        img=self.bridge.imgmsg_to_cv2(req.detected_image, 'bgr8')
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        arucoDict=aruco.Dictionary_get(aruco.DICT_4X4_100)
        arucoParams=aruco.DetectorParameters_create()
        bbox,ids,_=aruco.detectMarkers(gray,arucoDict,parameters=arucoParams)
    
    
        # aruco.drawDetectedMarkers(img,bbox)
        # cv2.imshow('images', img)
          

          
        if ids is None:
         print("e")
        else:

            
            
            
            if(m<=53):
              print(m)
              ids=ids.flatten().tolist()
              bbox_array=numpy.array(bbox)
              bbox_array=bbox_array.flatten().tolist()
              print(ids)
      
              k=ids.index(50)
              print(k)
              try:
                  l=ids.index(m)
              except:
                  m=m+1
                  rospy.sleep(0.8)
                  self.orient.data="2"
                  distance_to_marker=0
                  angle=0
                  
                  return aruco_detectionResponse(distance_to_marker,angle,self.orient,self.origin)
              l=ids.index(m)    

                  
                  
              print(l)
        
          
      
              robot=numpy.array(bbox[k]).flatten()
              destination=numpy.array(bbox[l]).flatten()


          

              lt_x=destination[0]
              lt_y=destination[1]
              rd_x=destination[4]
              rd_y=destination[5]
              centre_x_destination= (lt_x+rd_x)/2
              centre_y_destination=(lt_y+rd_y)/2
              lt_x=robot[0]
              lt_y=robot[1]
              rt_x=robot[2]
              rt_y=robot[3]
              rd_x=robot[4]
              rd_y=robot[5]
              ld_x=robot[6]
              ld_y=robot[7]
              ct_x=(lt_x+rt_x)/2.00
              ct_y=(lt_y+rt_y)/2.00
              cd_x=(ld_x+rd_x)/2.00
              cd_y=(ld_y+rd_y)/2.00
              centre_x_robot= (lt_x+rd_x)/2
              centre_y_robot=(lt_y+rd_y)/2
              distance_to_marker=math.sqrt(pow(centre_x_robot-centre_x_destination,2)+pow(centre_y_robot-centre_y_destination,2))
              dist=math.sqrt(pow(lt_y-ld_y,2)+pow(lt_x-ld_x,2))
              front_dist=math.sqrt(pow(ct_x-centre_x_destination,2)+pow(ct_y-centre_y_destination,2))
              back_dist=math.sqrt(pow(cd_x-centre_x_destination,2)+pow(cd_y-centre_y_destination,2))
              left_dist=math.sqrt(pow(lt_x-centre_x_destination,2)+pow(lt_y-centre_y_destination,2))
              right_dist=math.sqrt(pow(rt_x-centre_x_destination,2)+pow(rt_y-centre_y_destination,2))
              if(front_dist>=back_dist):
                 self.orient.data="1"
              else:
                 self.orient.data="3"
                 
              slope1=math.atan((lt_y-ld_y)/(lt_x-ld_x))
              slope2=math.atan((centre_y_destination-centre_y_robot)/(centre_x_destination-centre_x_robot))
              angle=slope2-slope1
              print(angle*180/(numpy.pi))
              self.origin.position.x=centre_x_robot
              self.origin.position.y=centre_y_robot
              self.origin.orientation.z=slope1
            #   if(distance_to_marker<=(dist)):
            #      m=m+1
              return aruco_detectionResponse(distance_to_marker,angle,self.orient,self.origin)
            distance_to_marker=0
            angle=0
            self.orient.data="3"
            

            
            return aruco_detectionResponse(distance_to_marker,angle,self.orient,self.origin)



if __name__ == '__main__':
    rospy.init_node('identifier', anonymous=True)

    aruco_b=identifier()


       
            




     