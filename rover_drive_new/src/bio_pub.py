#!/usr/bin/env python3
# license removed for brevity
import sys
import os
import rospy
from std_msgs.msg import Int32



class config_publisher():
    
    def __init__(self):

        self.pub = rospy.Publisher('/rover/bio_config',Int32, queue_size=10)
        
    def command_generator(self):
        config=Int32()
        while not rospy.is_shutdown():
            config.data=int(input("Enter a config[0:home,1:soil_collection,2:right_bio_box_front,3:right_bio_box_back,4:left_bio_box,5:uncontaminated_sample]:"))

            self.pub.publish(config)
        
           
            



            



    
if __name__ == '__main__':
    rospy.init_node('bio_pub',anonymous=True)
    device=config_publisher()
    while True:
        device.command_generator()
        rospy.spin()