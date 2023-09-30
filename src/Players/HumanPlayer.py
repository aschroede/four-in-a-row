from . import PlayerController

class HumanPlayer(PlayerController.PlayerController):
    

    # Create human player
    def __init__(self, playerID, gameN, heuristic):
        
        self.playerID = playerID
        self.gameN = gameN
        self.heuristic = heuristic
    
    # Show the human player the current board and ask them for the next move       
    def makeMove(self, board):
        print(board)

        if self.heuristic != None:
            print(f"Heuristic: {self.heuristic} calculated the best move is: {self.heuristic.getBestAction(self.playerID, board)+1}")        
        #not sure what is referred by this in Java
        column = int(input("Player " + str(self) + "\nWhich column would you like to play in? "))
        print(f"Selected Column: {column}")
        
        return column - 1 


    
    
    
    
    