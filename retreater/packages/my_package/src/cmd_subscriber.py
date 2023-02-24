#!/usr/bin/env python3

import os
import rospy
import json
from duckietown.dtros import DTROS, NodeType
from std_msgs.msg import String
from duckietown_msgs.msg import WheelsCmdStamped

class MyNode(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(MyNode, self).__init__(node_name=node_name, node_type=NodeType.GENERIC)
        # construct publisher
        self.sub = rospy.Subscriber('~sub_endpoint', WheelsCmdStamped, self.callback, queue_size=2)

    def callback(self, data):
        rospy.loginfo("I heard %s", data)

if __name__ == '__main__':
    # create the node
    node = MyNode(node_name='my_subscriber_node')
    # keep spinning
    rospy.spin()