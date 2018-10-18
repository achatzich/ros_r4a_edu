#!/usr/bin/env python
# Tic Tac Toe server
from __future__ import print_function
import random
import rospy
import random
import os
import sys
from complex_communication.srv import *
#clear output 
clear = lambda : os.system('clear')
# who first to go
def choose_first():
    if random.randint(0,1) == 0:
       return 'Player 1'
    else:
       return 'Player 2'
#creating display board 
def display_board(board):
    clear()
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
#Checking win or not 
def win_check (board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
# checking space is free or not
def check_space(board,position):
	return board[position] == ' '

def full_board_check (board):
    for i in range (1,10):
        if check_space(board,i):
            return False
    return True
#place marker on board
def place_marker(board,marker,position):
    board[position] = marker

def player1_client(board):
	rospy.wait_for_service('player1')
	try:
		player1=rospy.ServiceProxy('player1', movement)
		resp1=player1(board)		
		return resp1.move
	except rospy.ServiceException, e:
		rospy.logerr("Service call failed: %s" % (e,))

def player2_client(board):
	rospy.wait_for_service('player2')
	try:
		player2=rospy.ServiceProxy('player2', movement)
		resp2=player2(board)
		return resp2.move
	except rospy.ServiceException, e:
		rospy.logerr("Service call failed: %s" % (e,))
		

if __name__ == "__main__":
	# Reset the board
	theBoard = [' '] * 10
	turn = choose_first()
	print(turn + ' will go first.')
	game_on = True
	
	while game_on:
        	if turn == 'Player 1':
			position=player1_client(theBoard)
			place_marker(theBoard, 'X', position)
			
			if win_check(theBoard, 'X'):
				display_board(theBoard)
				print('Congratulations! You have won the game!')
				game_on = False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print('The game is a draw!')
					break
				else:
					turn = 'Player 2'
		else: 
			position=player2_client(theBoard)
			place_marker(theBoard, 'O', position)
			
			if win_check(theBoard, 'O'):
				display_board(theBoard)
				print('Congratulations! You have won the game!')
				game_on = False
			else:
				if full_board_check(theBoard):
					display_board(theBoard)
					print('The game is a draw!')
					break
				else:
					turn = 'Player 1'
#	 rospy.signal_shutdown()
                    		                    				
