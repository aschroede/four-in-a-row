from Heuristics import Heuristic
from Game import Game
import sys

class SimpleHeuristic(Heuristic.Heuristic):
    def __init__(self, gameN):
        self.gameN = gameN
        #super().__init__(gameN)
        
    def name(self):
        return "Simple"
        
    def evaluate(self, player, board):
        boardState = board.getBoardState()
        #some problems here -> board is a NoneType
        winning = Game.winning(boardState, self.gameN)
        if winning == player:
            return sys.maxsize
        elif winning != 0:
            return -sys.maxsize
        
        #if not winning or losing return highest number of claimed squares
        maxInRow = 0
        for i in range(len(boardState)):
            for j in range(len(boardState[i])):
                if boardState[i][j] == player:
                    maxInRow = max(maxInRow, 1)
                    for x in range(1,len(boardState)-i):
                        if boardState[i+x][j]==player:
                            maxInRow=max(maxInRow, x+1)
                        else:
                            break
                        
                    for y in range(1,len(boardState[0])-j):
                        if boardState[i][j+y] == player:
                            maxInRow = max(maxInRow, y+1)
                        else:
                            break
                    
                    for d in range(1,min(len(boardState)-i, len(boardState[0])-j)):
                        if boardState[i+d][j+d] == player:
                            maxInRow = max(maxInRow, d+1)
                        else:
                            break
                    
                    for a in range(1,min(len(boardState)-i,j)):
                        if boardState[i+a][j-a] == player:
                            maxInRow = max(maxInRow, a+1)
                        else:
                            break
            return maxInRow
            
            