#!/usr/bin/env python3
# license removed for brevity
import sys
import roslib
import cv2
import os
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

class image_converter:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("video",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      # Setting parameter values
      t_lower = 100  # Lower Threshold
      t_upper = 200  # Upper threshold
  
      # Applying the Canny Edge filter
      edge = cv2.Canny(cv_image, t_lower, t_upper)
      edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

      # Concatenating the original and edge images horizontally
      stacked_image = cv2.hconcat([cv_image, edge])
      resized_image = cv2.resize(stacked_image, (0,0), fx=0.5, fy=0.5)
      cv2.imshow('Video Feed', resized_image)
  
      
      cv2.waitKey(1)
    except CvBridgeError as e:
      print(e)

if __name__ == '__main__':
    rospy.init_node('image_converter', anonymous=True)
    ic = image_converter()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()