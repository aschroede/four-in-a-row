#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 15:45:02 2023

@author: kateryna
"""

from PlayerController import PlayerController

class MinMaxPlayer(PlayerController):
    depth = 0
    def __init__(self, playerID, depth, gameN, heuristic):
        self.playerID = playerID
        self.depth = depth
        self.gameN = gameN
        self.heuristic = heuristic
        
    def makeMove(self, board): 
        maxValue = float('-inf')
        maxMove = 0
        for i in range(board.width):
            if board.isValid(i): 
                new_board = board.getNewBoard(i, self.playerID) #that's how we make new board?
                value = self.heuristic.evaluateBoard(self.playerID, new_board) #evaluate that new board to get heuristic value from it
                if value > maxValue:
                    maxMove = 1
                    
        self.heuristic.getBestAction(self.playerId, board)
        return maxMove
            
#undefined names come with self, right?              
        