#!/usr/bin/env python
from __future__ import print_function
import random
import rospy
import os
import sys

class Player:
	
	#clear = lambda : os.system('clear')			
	
	def display_board(self,board):
		#clear()
		print('   |   |')
		print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
		print('   |   |')
		print('-----------')
		print('   |   |')
		print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
		print('   |   |')
		print('-----------')
		print('   |   |')
		print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
		print('   |   |')
		
	def handle_player(self, req):
		self.display_board(req.brd)
		if req.won:
			print('You have won!')
			return -1
		else:
			position = ' '
			while position not in '1 2 3 4 5 6 7 8 9'.split() or ' ' not in req.brd[int(position)]:
		    		position = raw_input('Choose number input 1-9')
			return int(position)
		
	
	

