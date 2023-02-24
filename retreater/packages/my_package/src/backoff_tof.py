#!/usr/bin/env python3

import os
import rospy
import json
from datetime import datetime, timedelta
from duckietown.dtros import DTROS, NodeType
from sensor_msgs.msg import Range, Joy


def init_joy():
    cmd = Joy()
    cmd.axes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    cmd.buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return cmd

class BackoffTof(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(BackoffTof, self).__init__(node_name=node_name, node_type=NodeType.GENERIC)
        # construct publisher
        self.sub = rospy.Subscriber('~sub_endpoint', Range, self.callback)
        self.pub = rospy.Publisher('~pub_endpoint',Joy)
        self.record_start:datetime = datetime.now()
        self.recording = False
        self.drive = False
    def callback(self, range:Range):
        if (range.range <0.10 and not self.recording):
           self.record_start = datetime.now()
           self.recording = True
           rospy.loginfo("backoff waiting for retreat")
        if (not self.recording):
            elapsed:timedelta =(datetime.now() - self.record_start)
            if (elapsed.total_seconds() > 0.25):
                rospy.loginfo("I heard %s", range.range)
            return
        
        elapsed = (datetime.now() - self.record_start ).total_seconds() 
        if (range.range <0.10 and elapsed > 1.0):
            self.record_start = datetime.now()
            self.drive = True
            cmd = init_joy()
            cmd.axes[1] = -1.0
            self.pub.publish(cmd)
            rospy.loginfo("Retreat!")
        elif (range.range >0.10 ):
            
            self.recording = False
            if (self.drive):
                self.drive = False
                self.pub.publish(init_joy())
                rospy.loginfo("Retreated. waiting for orders.")
            else:
                rospy.loginfo("Apperently was a glitch")
    
        

if __name__ == '__main__':
    # create the node
    node = BackoffTof(node_name='my_subscriber_node')
    # keep spinning
    rospy.spin()