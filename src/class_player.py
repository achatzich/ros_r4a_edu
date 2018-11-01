#!/usr/bin/env python
from __future__ import print_function
import random
import rospy
import os
import sys
from complex_communication_messages.msg import game

class Player:

	def __init__(self, player_id, marker):
		self.player_id = player_id
		self.marker = marker
		
	def talker(self, board):
		pub = rospy.Publisher('tic_tac_toe', game, queue_size=10)
#rospy.init_node('player', anonymous=True)
		msg = game()
		msg.from_node = self.player_id
		msg.to_node = 0
		msg.brd=board
		rospy.loginfo(msg)
		pub.publish()
				
	def callback(self, data):
		rospy.loginfo((data.from_node, data.to_node))
		if data.to_node == self.player_id:
			board = data.brd
			position=self.player_choice(board)
			self.place_marker(board, position)

	def listener(self):
		#rospy.init_node('player', anonymous=True)
		rospy.Subscriber("tic_tac_toe", game, self.callback)
		rospy.spin()
		
#place marker on board
	def place_marker(self,board,position):
		board[position] = self.marker
		
	def player_choice(self, board):
		position = ' '
		while position not in '1 2 3 4 5 6 7 8 9'.split() or ' ' not in board[int(position)]:
			position = raw_input('Choose number input 1-9')
		return int(position)

			
