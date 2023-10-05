from Heuristics import AHeuristicBase
from Game import Game
import sys

#### THIS IS NOT WORKING AND IS NOT USED ####

class AdvancedHeuristic(AHeuristicBase.AHeuristicBase):
    def __init__(self, gameN):
        self.gameN = gameN
        #super().__init__(gameN)
        
    def name(self):
        return "Advanced"
        
    def evaluate(self, player, board):
        boardState = board.getBoardState()

        winning = Game.winning(boardState, self.gameN)
        if winning == player:
            return sys.maxsize
        elif winning != 0:
            return -sys.maxsize
        
        #if not winning or losing return highest number of claimed squares in a row
        myMaxInRow = 0
        enemyMaxInRow = 0
        for row in range(len(boardState)):
            for col in range(len(boardState[row])):
                
                if boardState[row][col] == player:
                    myMaxInRow = max(myMaxInRow, 1)

                    # Vertical check
                    for x in range(1,len(boardState)-row):
                        if boardState[row+x][col]==player:
                            myMaxInRow=max(myMaxInRow, x+1)
                        else:
                            break

                    if (myMaxInRow != self.gameN):
                        myMaxInRow = 0
                    
                    # Horizontal check
                    for y in range(1,len(boardState[0])-col):
                        if boardState[row][col+y] == player:
                            myMaxInRow = max(myMaxInRow, y+1)
                        else:
                            break
                    
                    # Descending diagonal check
                    for d in range(1,min(len(boardState)-row, len(boardState[0])-col)):
                        if boardState[row+d][col+d] == player:
                            myMaxInRow = max(myMaxInRow, d+1)
                        else:
                            break
                    
                    # Ascending diagonal check
                    for a in range(1,min(len(boardState)-row,col)):
                        if boardState[row+a][col-a] == player:
                            myMaxInRow = max(myMaxInRow, a+1)
                        else:
                            break

                # player = 1 if player==2 else 2
                # if boardState[row][col] == player:
                #     enemyMaxInRow = max(enemyMaxInRow, 1)

                #     # Vertical check
                #     for x in range(1,len(boardState)-row):
                #         if boardState[row+x][col]==player:
                #             enemyMaxInRow=max(enemyMaxInRow, x+1)
                #         else:
                #             break
                    
                #     # Horizontal check
                #     for y in range(1,len(boardState[0])-col):
                #         if boardState[row][col+y] == player:
                #             enemyMaxInRow = max(enemyMaxInRow, y+1)
                #         else:
                #             break
                    
                #     # Descending diagonal check
                #     for d in range(1,min(len(boardState)-row, len(boardState[0])-col)):
                #         if boardState[row+d][col+d] == player:
                #             enemyMaxInRow = max(enemyMaxInRow, d+1)
                #         else:
                #             break
                    
                #     # Ascending diagonal check
                #     for a in range(1,min(len(boardState)-row,col)):
                #         if boardState[row+a][col-a] == player:
                #             enemyMaxInRow = max(enemyMaxInRow, a+1)
                #         else:
                #             break

                # player = 1 if player==2 else 2
            
        # if(enemyMaxInRow == 3 and myMaxInRow < 4):
        #     return enemyMaxInRow
        # else:

        return myMaxInRow
        # if(myMaxInRow == 4):
        #     return sys.maxsize
        # else:
        #     return myMaxInRow