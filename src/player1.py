#!/usr/bin/env python

import random
import rospy
import os
import sys
from complex_communication_messages.msg import game
from class_player import Player

if __name__ == '__main__':
	player1= Player(1, "X")
	rospy.init_node('player1', anonymous=True)
	player1.listener()
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            rate.sleep()


