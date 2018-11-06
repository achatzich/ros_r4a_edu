#!/usr/bin/env python

import random
import rospy
import os
import sys
from complex_communication_messages.msg import game
from class_player import Player

if __name__ == '__main__':
	player2= Player(2, "O")
	rospy.init_node('player2', anonymous=True)
	player2.listener()
        rospy.spin()
