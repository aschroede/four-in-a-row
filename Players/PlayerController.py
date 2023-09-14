#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:14:58 2023

@author: kateryna
"""
#class defining Player
class PlayerController:
    def __init__(self, playerID, gameN, heuristic):
        self.playerID = playerID
        self.gameN = gameN
        self.heuristic = heuristic
#amount of times heuristic was used to evaluate boardstate        
    def getEvalCount(self):
        return self.heuristic.getEvalCount()
#get string representation for displaying the board   
    def toString(self):
        if self.playerID == 2:
            return "O"
        else:
            return "X"
        
    def makeMove(self, board):
        return board #??