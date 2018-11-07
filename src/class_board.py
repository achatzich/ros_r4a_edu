#!/usr/bin/env python
from __future__ import print_function
import random
import rospy
import os
import sys
from complex_communication_messages.msg import game


class BoardNode(object):
    def __init__(self, node_name="orchestrator"):
	theBoard = Board()
        rospy.init_node('orchestrator', anonymous=True)
        self.rate = rospy.Rate(10) # 10hz
	theBoard.start_game()

    def start(self):
        self.rate.sleep()
        while not rospy.is_shutdown():
            self.rate.sleep()


class Board:
 	def __init__(self):
            self.board = [' '] * 10
            self.game_on = True
            self.pub_node = 0
            self.sub_node = random.randint(1,2)
            self.pub = rospy.Publisher('/tic_tac_toe', game, queue_size=10, latch=True)
            self.sub = rospy.Subscriber('/tic_tac_toe', game, self.callback)
 		
	def display_board(self):
            print('\033[95m\r\nTicTacToe Board: \033[0m')
            print('\033[92m-------------\033[0m')
            print('\033[92m| \033[93m' + self.board[7] + '\033[92m | \033[93m' + self.board[8] + '\033[92m | \033[93m' + self.board[9] + '\033[92m |\033[0m')
            print('\033[92m-------------\033[0m')
            print('\033[92m| \033[93m' + self.board[4] + '\033[92m | \033[93m' + self.board[5] + '\033[92m | \033[93m' + self.board[6] + '\033[92m |\033[0m')
            print('\033[92m-------------\033[0m')
            print('\033[92m| \033[93m' + self.board[1] + '\033[92m | \033[93m' + self.board[2] + '\033[92m | \033[93m' + self.board[3] + '\033[92m |\033[0m')
            print('\033[92m-------------\033[0m')
		
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

	def start_game(self):
            self.msg = game()
            self.msg.from_node = self.pub_node
            self.msg.to_node = self.sub_node
            self.msg.brd=self.board
            print('Player', self.sub_node, ' will go first.')
            self.display_board()
            self.pub.publish(self.msg)

	def callback(self,data):
            if data.to_node == 0:
                self.board = data.brd
                self.pub_node = data.from_node
                self.sub_node = data.to_node
                self.end_game()
                if self.game_on:
                    self.display_board()
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
