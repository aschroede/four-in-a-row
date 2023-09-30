
from copy import deepcopy

class Board:
    
    # Constructor for new empty board
    def __init__(self, *args):

        # Default constructor
        if len(args) == 2:
            self.rows = args[0]
            self.columns = args[1]
            self.boardState = [[0 for i in range(self.columns)] for j in range(self.rows)]

        else:
            # Make Board from Board
            if(isinstance(args[0], Board)):
                self.rows = args[0].rows
                self.columns = args[0].columns
                self.boardState = args[0]
            
            # Make Board from State
            elif(isinstance(args[0], list)):
                self.rows = len(args[0])
                self.columns = len(args[0][0])
                self.boardState = args[0]

    # Get the value of a certain coordinate on the board
    def getValue(self, x, y):
        return self.boardState[x][y]
    
    # Get cloned int array of the board state
    def getBoardState(self):
        return deepcopy(self.boardState)

    # let player PlayerId make a move in column x
    def play(self, col, playerId):
        # Iterate through each row in reverse order
        for row, value in reversed(list(enumerate(self.boardState))):
            if(self.boardState[row][col] == 0):
                self.boardState[row][col] = playerId
                return True
        
        return False
    
    # Returns if a move is valid by checking if the first row of the specified column (x) is occupied
    def isValid(self, x):
        return self.boardState[0][x] == 0

    # Gets a new board given a player and their action 
    def getNewBoard(self, col, playerId):
        newBoardState = self.getBoardState()
        # Iterate through each row in reverse order
        for row, value in reversed(list(enumerate(self.boardState))):
            if(newBoardState[row][col] == 0):
                newBoardState[row][col] = playerId
                return Board(newBoardState)
        
        return  Board(newBoardState)

    def __str__(self):
        divider = " "
        divider2 = " "
        numberColumn = "|"

        for index, value in enumerate(self.boardState[0]):
            divider += "--- "
            divider2 += "=== "
            numberColumn += " " + str(index+1) + " |"

        output = ""

        for row, value in enumerate(self.boardState):
            output += "\n" + divider + "\n"
            for column, value in enumerate(self.boardState[0]):
                node = " "
                if(self.boardState[row][column] == 1):
                    node = "X"
                elif(self.boardState[row][column] == 2):
                    node = "O"
                output += "| " + node + " "
            output += "|"

        output += "\n" + divider2 + "\n" + numberColumn + "\n"
        return output


    

    
    