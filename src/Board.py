
# ---- Indexing a 2D Array ------------
# input = ([[1, 2], [3, 4], [5, 6]])
# input[0][1] = 2
# First number is for the row, second number is for the column. This is the same as in Java

# ---- Dimensions of 2D Array ---------
# numrows = len(input)
# numcols = len(input[0])


#          -------------Columns-------------
#              1   2   3   4   5   6   7  
#----Row 0   |   |   |   |   |   |   |   |
#----Row 1   |   |   |   |   |   |   |   |
#----Row 2   |   |   |   |   |   |   |   |
#----Row 3   |   | O |   | X |   |   |   |
#----Row 4   |   | O |   | X |   |   |   |
#----Row 5   |   | O | O | X |   |   |   |


class Board:
    
    rows = 0
    columns = 0
    boardState = 0 # 2D integer array cntaining 0's, or else playerId's in case a spot has been claimed 


    # Constructor for new empty board
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.boardState = [[0]*columns]*rows

    # Method for cloning a board based on another board class
    def makeBoardFromBoard(self, board):
        self.rows = board.rows
        self.columns = board.columns
        self.boardState = board

    # Constructor for cloning a board using a boardstate
    def makeBoardFromState(self, state):
        self.rows = len(state)
        self.columns = len(state[0])
        self.boardState = state

    # Get the value of a certain coordinate on the board
    def getValue(self, x, y):
        return self.boardState[x][y]
    
    # Get cloned int array of the board state
    def getBoardState(self):
        raise NotImplementedError
        #TODO

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
                return self.makeBoardFromState(newBoardState)
        
        return newBoardState


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


    

    
    