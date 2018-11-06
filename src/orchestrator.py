#!/usr/bin/env python

import random
import rospy
import os
import sys
from complex_communication_messages.msg import game
from class_board import Board, BoardNode

 		  	
if __name__ == '__main__':
    brdNode = BoardNode("TicTacToeOrchestrator")
    brdNode.start()

