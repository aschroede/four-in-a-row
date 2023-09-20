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

        winning = Game.winning(boardState, self.gameN)
        if winning == player:
            return sys.maxsize
        elif winning != 0:
            return -sys.maxsize
        
        #if not winning or losing return highest number of claimed squares in a row
        maxInRow = 0
        for row in range(len(boardState)):
            for col in range(len(boardState[row])):
                if boardState[row][col] == player:
                    maxInRow = max(maxInRow, 1)

                    # Vertical check
                    for x in range(1,len(boardState)-row):
                        if boardState[row+x][col]==player:
                            maxInRow=max(maxInRow, x+1)
                        else:
                            break
                    
                    # Horizontal check
                    for y in range(1,len(boardState[0])-col):
                        if boardState[row][col+y] == player:
                            maxInRow = max(maxInRow, y+1)
                        else:
                            break
                    
                    # Descending diagonal check
                    for d in range(1,min(len(boardState)-row, len(boardState[0])-col)):
                        if boardState[row+d][col+d] == player:
                            maxInRow = max(maxInRow, d+1)
                        else:
                            break
                    
                    # Ascending diagonal check
                    for a in range(1,min(len(boardState)-row,col)):
                        if boardState[row+a][col-a] == player:
                            maxInRow = max(maxInRow, a+1)
                        else:
                            break

        return maxInRow
            
            