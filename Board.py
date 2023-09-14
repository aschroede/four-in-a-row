


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
        return 


    

    
    