from abc import ABC, abstractmethod

# Abstract class defining Player
class PlayerController(ABC):
    def __init__(self, playerID, gameN, heuristic):
        self.playerID = playerID
        self.gameN = gameN
        self.heuristic = heuristic
        self.history = []

#amount of times heuristic was used to evaluate boardstate        
    def getEvalCount(self):
        return self.heuristic.getEvalCount()
    
#get string representation for displaying the board   
    def __str__(self):
        if self.playerID == 2:
            return "O"
        else:
            return "X"
    
    @abstractmethod
    def makeMove(self, board):
        pass

    def printHistory(self):
        print("Player "+ str(self) + " made these moves: " + str(self.history))