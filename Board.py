
# ---- Indexing a 2D Array ------------
# input = ([[1, 2], [3, 4], [5, 6]])
# input[0][1] = 2
# First number is for the row, second number is for the column. This is the same as in Java

# ---- Dimensions of 2D Array ---------
# numrows = len(input)
# numcols = len(input[0])
# 


#          -------------Columns-------------
#              1   2   3   4   5   6   7  
#----Row 0   |   |   |   |   |   |   |   |
#----Row 1   |   |   |   |   |   |   |   |
#----Row 2   |   |   |   |   |   |   |   |
#----Row 3   |   | o |   | x |   |   |   |
#----Row 4   |   | o |   | x |   |   |   |
#----Row 5   |   | o | 0 | x |   |   |   |


class Board:
    
    width = 0
    height = 0
    boardState = [[]] # 2D integer array cntaining 0's, or else playerId's in case a spot has been claimed 


    # Constructor for new empty board
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.boardState = [self.width][self.height]

    # Method for cloning a board based on another board class
    def makeBoardFromBoard(self, board):
        self.height = board.height
        self.width = board.width
        self.boardState = board

    # Constructor for cloning a board using a boardstate
    def makeBoardFromState(self, state):
        self.height = len(state)
        self.width = len(state[0])
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
        # Iterate through each row
        for row, value in reversed(list(enumerate(self.boardState))):
            if(self.boardState[row][col] == 0):
                self.boardState[row][col] = playerId
                return True
        
        return False
    
    # Returns if a move is valid by checking if the first row of the specified column is occupied
    def isValid(self, x):
        return self.boardState[0][x] == 0




    

    
    