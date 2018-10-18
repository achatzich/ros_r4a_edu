#!/usr/bin/env python

from __future__ import print_function
import random
import rospy
import random
import os
import sys
from complex_communication.srv import *

clear = lambda : os.system('clear')
def handle_player2(req):
	display_board(req.brd)
	position = ' '
	while position not in '1 2 3 4 5 6 7 8 9'.split() or not check_space(req.brd, int(position)):
        	position = raw_input('Choose number input 1-9')
	return int(position)

def player2():
	rospy.init_node('player2_server')
	s=rospy.Service('player2', movement, handle_player2)
	rospy.spin()

# checking space is free or not
def check_space(board,position):
	return board[position] == ' '

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

if __name__ == "__main__":
	player2()
