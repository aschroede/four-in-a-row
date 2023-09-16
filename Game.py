import Players.PlayerController
from Board import Board

class Game:
    gameN = 0
    players = 0
    gameBoard = 0 
    winner = 0


    # Create a new game
    # gameN - N in a row required to win
    def __init__(self, gameN, rows, columns, players):
        assert(columns % 2 != 0), "Board width must be odd!"
        self.gameN = gameN
        self.players = players
        self.gameBoard = Board(rows, columns)

    
    # Start game
    def startGame(self):
        print("Start game!")
        currentPlayer = 0

        while (not(self.isOver)):
            # turn player can make a move
            self.gameBoard.play(self.players[currentPlayer].makeMove(self.gameBoard), self.players[currentPlayer].playerId)

            # other player gets to make a move
            currentPlayer = 1 if currentPlayer == 0 else 0
        
        print(self.gameBoard)
        if(self.winner < 0):
            print("Game is a draw!")
        else:
            print("Player " + self.players[self.winner -1] + " won!")
        print("Player " + self.players[0] + " evaluated a boardsate " + self.players[0].getEvalCount() + " times.")
        print("Player " + self.players[1] + " evaluated a boardsate " + self.players[1].getEvalCount() + " times.")
        return self.winner
    
    # Determine if the game is over
    def isOver(self):
        self.winner = self.winning(self.gameBoard.getBoardState(), self.gameN)
        return self.winner != 0
    

    @staticmethod
    def winning (self, board, gameN):
        player = 0

        # Vertical Check 
        for row in range (len(board)):
            for column in range (len(board[row]) - gameN):
                if(board[row][column] != 0):
                    player = board[row][column]
                    for x in range(gameN):
                        if(board[row][column + x] != player):
                            player = 0
                            break
                    if (player != 0):
                        return player
                    

        # Horizontal Check 
        for row in range (len(board) - gameN):
            for column in range (len(board[row])):
                if(board[row][column] != 0):
                    player = board[row][column]
                    for x in range(gameN):
                        if(board[row + x][column] != player):
                            player = 0
                            break
                    if (player != 0):
                        return player
                    

        # Ascending Diagonal Check 
        for row in reversed(range(len(board) - gameN)):
            for column in range(len(board[0] - gameN)):
                if(board[row][column] != 0):
                    player = board[row][column]
                    for x in range(gameN):
                        if(board[row-x][column+x] != player):
                            player = 0
                            break
                    if(player != 0):
                        return player
                    
        # Descending Diagonal Check
        for row in (range(len(board) - gameN)):
            for column in range(len(board[0] - gameN)):
                if(board[row][column] != 0):
                    player = board[row][column]
                    for x in range(gameN):
                        if(board[row+x][column+x] != player):
                            player = 0
                            break
                    if(player != 0):
                        return player
                    
        # Check if draw (full board)
        for x in range(len(board)):
            if(board[0][x] == 0):
                return 0
            
        return -1 # Game is a draw
                    

        

    