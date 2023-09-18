#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:58:10 2023

@author: kateryna
"""

from PlayerController import PlayerController
from Board import Board
from Heuristic import Heuristic


class HumanPlayer(PlayerController):
    

    # Create human player
    def __init__(self, playerID, gameN, heuristic):
        
        super().__init__(playerID)
        super().__init__(gameN)
        super().__init__(heuristic)
    
    # Show the human player the current board and ask them for the next move       
    def makeMove(self, board):
        print(board)

        if self.heuristic != None:
            print(f"Heuristic: {self.heuristic} calculated the best move is: {self.heuristic.getBestAction(self.playerID, board)+1}")        
        #not sure what is referred by this in Java
        print("Player " + self.playerID + "\nWhich column would you like to play in? ")
        column = int(input())
        print(f"Selected Column: {column}")
        
        return column - 1 


    
    
    
    
    