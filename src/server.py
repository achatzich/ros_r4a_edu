#!/usr/bin/env python
# Tic Tac Toe server
from __future__ import print_function
import random
import rospy
import random
import os
import sys
from complex_communication.srv import *
from board_class import Board

def player1_client(b, won):
	rospy.wait_for_service('player1')
	try:
		player1 = rospy.ServiceProxy('player1', movement)
		resp1 = player1(b, won)		
		return resp1.move
	except rospy.ServiceException, e:
		rospy.logerr("Service call failed: %s" % (e,))

def player2_client(b, won):
	rospy.wait_for_service('player2')
	try:
		player2 = rospy.ServiceProxy('player2', movement)
		resp2 = player2(b, won)
		return resp2.move
	except rospy.ServiceException, e:
		rospy.logerr("Service call failed: %s" % (e,))
		

if __name__ == "__main__":
	# Reset the board
	theBoard = Board()
	turn = theBoard.choose_first()
	print(turn + ' will go first.')
	game_on = True
	
	while game_on:
		if turn == 'Player 1':
			position = player1_client(theBoard.board, False)
			print(position)
			theBoard.place_marker('X', position)
			if theBoard.win_check('X'):
				print('Player 1 has won the game!')
				player1_client(theBoard.board, True)
				game_on = False
			else:
				if theBoard.full_board_check():
					break
				else:
					turn = 'Player 2'
		else: 
			position = player2_client(theBoard.board, False)
			print(position)
			theBoard.place_marker('O', position)
			
			if theBoard.win_check('O'):
				print('Player 2 has won the game!')
				player2_client(theBoard.board, True)
				game_on = False
			else:
				if theBoard.full_board_check():
					break
				else:
					turn = 'Player 1'
	print('Game over')
	rospy.is_shutdown()
	sys.exit(0)
                    		                    				
