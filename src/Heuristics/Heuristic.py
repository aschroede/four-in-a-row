from Board import Board
import sys
from abc import ABC, abstractmethod
class Heuristic(ABC):
    
    evalCount = 0
    
    def __init__(self, gameN):
        self.gameN = gameN
        
   #amount of times broadstate was evaluated
    def getEvalCount(self):
        return self.evalCount
    
    #return heuristic value for board state
    @abstractmethod
    def evaluate(self, player, board):
        pass

    #helper function to assign utility to a board
    def evaluateBoard(self, player, board):
        self.evalCount +=1
        return self.evaluate(player, board)
    
    #helper function to assign value to an action
    def evaluateAction(self, player, action, board):
        if board.isValid(action):
            self.evalCount += 1
            value = self.evaluateBoard(player, board.getNewBoard(action, player))
            return value
        else:
            return -sys.maxsize 
    
    #helper dunction that determines utility for each column    
    def evalActions(self, player, board):
        utilities = [0]*board.columns
        for i in range(board.columns):
            utilities[i] = self.evaluateAction(player, i, board)
        return utilities
         
   #determines best column for the next move 
    def getBestAction(self, player, board):
        utilities = self.evalActions(player, board)
        bestAction = 0
        for i in range(len(utilities)):
            if utilities[i] > utilities[bestAction]:
                bestAction = i
        return bestAction
           
    @abstractmethod
    def name(self):
        pass
    
    def __str__(self):
        return self.name()
    
                