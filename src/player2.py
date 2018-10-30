#!/usr/bin/env python

import rospy
from complex_communication.srv import *
from player_class import Player

def player2():
	rospy.init_node('player2_server')
	s=rospy.Service('player2', movement, p2.handle_player)
	rospy.spin()#just waits for the node to shutdown

if __name__ == "__main__":
	p2 = Player()
	player2()
