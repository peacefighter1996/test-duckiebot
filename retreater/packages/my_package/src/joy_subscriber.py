#!/usr/bin/env python3

import os
import rospy
import json
from duckietown.dtros import DTROS, NodeType
from std_msgs.msg import String
from sensor_msgs.msg import Joy

class joy_subscriber(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(joy_subscriber, self).__init__(node_name=node_name, node_type=NodeType.GENERIC)
        # construct publisher
        self.sub = rospy.Subscriber('~sub_endpoint', Joy, self.callback)

    def callback(self, data):
        rospy.loginfo("I heard %s", data)

if __name__ == '__main__':
    # create the node
    node = joy_subscriber(node_name='my_subscriber_node')
    # keep spinning
    rospy.spin()