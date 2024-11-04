#!/usr/bin/env python3
import sys
import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class ImagePublisher:
    def __init__(self, video_path, topic_name):
        self.cap = cv2.VideoCapture(video_path)
        self.bridge = CvBridge()
        self.publisher = rospy.Publisher(topic_name, Image, queue_size=10)

    def publish(self):
        rate = rospy.Rate(30) # 30hz
        while not rospy.is_shutdown():
            ret, frame = self.cap.read()
            if ret:
                try:
                    image_msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
                    self.publisher.publish(image_msg)
                except Exception as e:
                    rospy.logerr("Error converting image: {}".format(e))
            else:
                break
            rate.sleep()

        self.cap.release()

if __name__ == '__main__':
    rospy.init_node('image_publisher')
    video_path = "/home/arinweling/catkin_ws/src/assignment_1/my_video.mp4"
    topic_name = "video"
    publisher = ImagePublisher(video_path, topic_name)
    publisher.publish() 
