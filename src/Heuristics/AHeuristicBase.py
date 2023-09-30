from Board import Board
import sys
from abc import ABC, abstractmethod

#### THIS IS NOT WORKING AND IS NOT USED ####

class AHeuristicBase(ABC):
    
    evalCount = 0
    
    def __init__(self, gameN):
        self.gameN = gameN
        
   #amount of times broadstate was evaluated
    def getEvalCount(self):
        return self.evalCount
         
   #determines best column for the next move 
    def getBestAction(self, player, board):
        myUtilities = self.evalActions(player, board)
        enemyUtilities = self.evalActions(1 if player==2 else 2, board)
        bestAction = 0
        
        # Check for winning moves on our side
        for i in range(len(myUtilities)):
            if(myUtilities[i] == sys.maxsize):
                return i

        # Check for winning moves on enemy side and deny them
        for i in range(len(myUtilities)):
            if(enemyUtilities[i] == sys.maxsize):
                return i
        
        # If no winning moves just get best utility
        for i in range(len(myUtilities)):
            if myUtilities[i] > myUtilities[bestAction]:
                bestAction = i
        
        return bestAction
    
    #helper function that determines utility for each column    
    def evalActions(self, player, board):
        utilities = [0]*board.columns
        for i in range(board.columns):
            utilities[i] = self.evaluateAction(player, i, board)
        return utilities

    #helper function to assign value to an action
    def evaluateAction(self, player, action, board):
        if board.isValid(action):
            self.evalCount += 1
            value = self.evaluateBoard(player, board.getNewBoard(action, player))
            return value
        else:
            return -sys.maxsize 

    #helper function to assign utility to a board
    def evaluateBoard(self, player, board):
        self.evalCount +=1
        return self.evaluate(player, board)
    
    def __str__(self):
        return self.name()
    
    @abstractmethod
    def name(self):
        pass
    
    #return heuristic value for board state
    @abstractmethod
    def evaluate(self, player, board):
        pass

    
                