#!/usr/bin/env python
from __future__ import print_function
import random
import rospy
import os
import sys

class Board:

	#clear = lambda : os.system('clear')
 
 	def __init__(self):
		self.board=[' '] * 10                                                                                                                                                               
		
	def win_check (self,mark):
		return ((self.board[7] == mark and self.board[8] == mark and self.board[9] == mark) or # across the top
		(self.board[4] == mark and self.board[5] == mark and self.board[6] == mark) or # across the middle
		(self.board[1] == mark and self.board[2] == mark and self.board[3] == mark) or # across the bottom
		(self.board[7] == mark and self.board[4] == mark and self.board[1] == mark) or # down the middle
		(self.board[8] == mark and self.board[5] == mark and self.board[2] == mark) or # down the middle
		(self.board[9] == mark and self.board[6] == mark and self.board[3] == mark) or # down the right side
		(self.board[7] == mark and self.board[5] == mark and self.board[3] == mark) or # diagonal
		(self.board[9] == mark and self.board[5] == mark and self.board[1] == mark)) # diagonal
    
	def check_space(self,position):
		return self.board[position] == ' '
		
	def full_board_check (self):
		for i in range (1,10):
			if self.check_space(i):
				return False
		return True
 #place marker on board
	def place_marker(self,marker,position):
		self.board[position] = marker
	
	#@staticmethod	
	def choose_first(self):
		if random.randint(0,1) == 0:
			return 'Player 1'
		else:
			return 'Player 2'
