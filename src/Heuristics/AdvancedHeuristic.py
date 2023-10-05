from Board import Board
import sys
from Game import Game

class AdvancedHeuristic():
    
    evalCount = 0
    
    def __init__(self, gameN):
        self.gameN = gameN
        
    #amount of times broadstate was evaluated
    def getEvalCount(self):
        return self.evalCount
    
    #return heuristic value for board state
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
    
    def evaluate_opponent(self, player, board):
        utilities_opponent = [0]*board.columns
        if player == 1:     
            opponent = 2
        else:
            opponent = 1
        max_opponent = 100
        boardState = board.getBoardState()
        for row in range(len(boardState)):
            for col in range (len(boardState[row])):
                if boardState[row][col] == opponent:
                    if row < len(boardState)-2:  
                        if boardState[row+1][col] == opponent and boardState[row+2][col] == opponent:
                            if row > 0 and boardState[row-1][col] == 0:
                               utilities_opponent[col] = max_opponent
                    elif col < len(boardState[row])-3: 
                       if boardState[row][col+1] == opponent and boardState[row][col+2] == opponent:
                          if boardState[row][col+3] == 0:
                             utilities_opponent[col+3] = max_opponent
                          elif col-1 >= 0 and boardState[row][col-1] == 0:
                             utilities_opponent[col-1] = max_opponent
                       elif boardState[row][col+2] == opponent and boardState[row][col+3] == opponent:
                          if boardState[row][col+1] == 0:
                             utilities_opponent[col+1] = max_opponent
                       elif boardState[row][col+1] == opponent and boardState[row][col+3] == opponent:
                          if boardState[row][col+1] == 0:
                             utilities_opponent[col+1] = max_opponent  
        return utilities_opponent 

    
    
    # helper Function that determines utility for each column    
    def evalActions(self, player, board):
        utilities = [0]*board.columns
        for i in range(board.columns):
            utilities[i] = self.evaluateAction(player, i, board)
        return utilities
        
         
   # determines best column for the next move 
    def getBestAction(self, player, board):
        utilities = self.evalActions(player, board)
        utilities_opponent = self.evaluate_opponent(player, board)
        max_opponent = 100
        if max_opponent in utilities_opponent:
            utilities[utilities_opponent.index(max_opponent)] = max_opponent
        bestAction = 0
        for i in range(len(utilities)):
            if utilities[i] > utilities[bestAction]:
                bestAction = i
        return bestAction
        
           
    def name(self):
        return "Advanced"
    
    def __str__(self):
        return self.name()
    
                