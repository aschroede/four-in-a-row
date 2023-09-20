#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 15:45:02 2023

@author: kateryna
"""

from . import PlayerController
from . import Node
import sys
from Game import Game

class MinMaxPlayer(PlayerController.PlayerController):
    depth = 0
    def __init__(self, playerID, depth, gameN, heuristic):
        self.playerID = playerID
        self.depth = depth
        self.gameN = gameN
        self.heuristic = heuristic
        
    def makeMove(self, board): 

        # TODO: implement minmax player!
        # HINT: use the functions on the 'board' object to produce a new board given a specific move
        # HINT: use the functions on the 'heuristic' object to produce evaluations for the different board states!

        # # Example
        # maxValue = float('-inf')
        # maxMove = 0
        # for i in range(board.columns): # For each of the possible moves
        #     if board.isValid(i): # Check if the move is valid
        #         new_board = board.getNewBoard(i, self.playerID) # Get a new board resultign from that move
        #         value = self.heuristic.evaluateBoard(self.playerID, new_board) #evaluate that new board to get heuristic value from it
        #         if value > maxValue:
        #             maxMove = i
        
        # # This returns the same as:
        # self.heuristic.getBestAction(self.playerId, board) # Very userful helper function!

        # This is obviously not enough (this is depth 1)
        # Your assignment is to create a data structure (tree) to store the gameboards such that you can evaluate a higher depths.
        # Then, use the minmax algorithm to search through this tree to find the best move/action to take!

        maxValue = sys.maxsize
        maxMove = 0

        startNode = Node.Node(board)
        self.createTree(startNode, self.depth, self.playerID )
        self.minMax(startNode, self.depth, self.playerID)

        for child in startNode.children:
            if child.value > maxValue:
                maxValue = child.value
                maxMove = child.column           

        return maxMove
    
    def createTree(self, node, depth, playerID):

        # 1) Depth = 0
        if(depth == 0):
            for i in range(node.board.columns):

                if node.board.isValid(i):
                    new_Node = Node.Node(node.board.getNewBoard(i, playerID))
                    new_Node.column = i
                    node.addChild(new_Node)
            return

        # 2) Game over - no more children needed for this one
        winner = Game.winning(node.board.boardState, self.gameN)
        if(winner != 0):
            return

        for i in range(node.board.columns):
            if node.board.isValid(i):
                new_Node = Node.Node(node.board.getNewBoard(i, playerID))
                new_Node.column = i
                node.addChild(new_Node)
                self.createTree(new_Node, depth-1, 1 if playerID==2 else 2)
        


    # Node is a class with a boardState, a variable for storing the static evaluation of the boardstate,
    # a single parent node, and child nodes, as well as the associated column that leads to this boardstate
    # If player is true we are the maximiser, if false we are the minimizer
    def minMax(self, node, depth, player):
            
            # Base case to bottom out the recursion. 
            
            # 1) Reach depth 0
            if(depth == 0):
                 node.value = self.heuristic.evaluateBoard(player, node.board)
                 return node.value
            
            # 2) Game over
            winner = Game.winning(node.board.boardState, self.gameN)
            if(winner != 0):
                if(winner == self.playerID):
                    node.value = sys.maxsize
                else:
                     node.value = -sys.maxsize
                return node.value

            
            if(player == self.playerID): # We are the maximiser
                currentMax = -sys.maxsize

                for child in node.children:
                    evalResult = self.minMax(child, depth-1, 1 if player==2 else 2)   # Recursion step
                    currentMax = max(currentMax, evalResult)
                
                node.value = currentMax
                return currentMax
                 

            else: # We are the minimizer
                currentMin = sys.maxsize

                for child in node.children:
                    evalResult = self.minMax(child, depth-1, 1 if player==2 else 2)    # Recursion step
                    currentMin = min(currentMin, evalResult)
                
                node.value = currentMin
                return currentMin
                    
                 
        