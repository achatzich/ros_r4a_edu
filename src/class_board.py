#!/usr/bin/env python
from __future__ import print_function
import random
import rospy
import os
import sys
from complex_communication_messages.msg import game

class Board:

 	def __init__(self):
 		self.board = [' '] * 10
 		self.game_on = True
 		self.pub_node = 0
 		self.sub_node = random.randint(1,2)
 		
	def display_board(self):
		print('   |   |')
		print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
		print('   |   |')
		print('-----------')
		print('   |   |')
		print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
		print('   |   |')
		print('-----------')
		print('   |   |')
		print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
		print('   |   |')
		                                                                                                                                                       
		
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

	def talker_beginning(self):
		self.pub = rospy.Publisher('tic_tac_toe', game, queue_size=10)
		#rospy.init_node('orchestrator', anonymous=True)
		msg = game()
		msg.from_node = self.pub_node
		msg.to_node = self.sub_node
		msg.brd=self.board
		rospy.loginfo(msg)
		print('Player', self.sub_node, ' will go first.')
		self.display_board()
		self.pub.publish(msg)
		print('kfjghdsjfg')

	def callback(self,data):
		rospy.loginfo((data.from_node, data.to_node))
		if data.to_node == 0:
			self.board = data.brd
			self.pub_node = data.from_node
			self.sub_node = data.to_node
			self.end_game()
			if self.game_on:
				self.diplay_board()
				self.next_move()
				
	def next_move(self):
		msg = game()
		msg.from_node = 0
		msg.brd=self.board
		if self.pub_node == 1:
			msg.to_node = 2
		else:
			msg.to_node = 1
		self.pub.publish(msg)
		
	def end_game(self):
		if self.pub_node == 1:
			if self.win_check('X'):
				self.display_board()
				print('Player 1 has won the game!')
				self.game_on = False
		else:
			if self.win_check('O'):
				self.display_board()
				print('Player 2 has won the game!')
				self.game_on = False
			
		if self.full_board_check():
				self.display_board()
				print('The game is a draw!')
				self.game_on = False
			

	def listener(self):
		#rospy.init_node('orchestrator', anonymous=True)
		print("e")
		rospy.Subscriber("tic_tac_toe", game, self.callback)
		print("ea")
		# spin() simply keeps python from exiting until this node is stopped
		rospy.spin()
		print("eb")
		
		
		
		
