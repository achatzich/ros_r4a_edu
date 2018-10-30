#!/usr/bin/env python

import rospy
from complex_communication.srv import *
from player_class import Player

def player1():
	rospy.init_node('player1_server')
	s=rospy.Service('player1', movement, p1.handle_player)
	rospy.spin()#just waits for the node to shutdown

if __name__ == "__main__":
	p1 = Player()
	player1()
