#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:58:10 2023

@author: kateryna
"""

from . import PlayerController

class HumanPlayer(PlayerController.PlayerController):


    # Create human player
    def __init__(self, playerID, gameN, heuristic=None):
        self.playerID = playerID
        self.gameN = gameN
        self.heuristic = heuristic
    
    # Show the human player the current board and ask them for the next move       
    def makeMove(self, board):
        print(board)

        if self.heuristic != None:
            print(f"Heuristic: {self.heuristic} calculated the best move is: {self.heuristic.getBestSction(self.playerID, board)+1}")        
        
        column = int(input("Player " + self + "\nWhich column would you like to play in?"))
        
        print(f"Selected Column: {column}")
        
        return column - 1 


    
    
    
    
    