#!/usr/bin/env python

import random
import rospy
import os
import sys
from complex_communication_messages.msg import game
from class_board import Board

 		  	
if __name__ == '__main__':
	theBoard=Board()
	#pub = rospy.Publisher('tic_tac_toe', game, queue_size=10)
	rospy.init_node('orchestrator', anonymous=True)
	theBoard.talker_beginning()
	while theBoard.game_on:
		theBoard.listener()
		theBoard.next_move()
	rospy.is_shutdown()
	sys.exit(0)
		
