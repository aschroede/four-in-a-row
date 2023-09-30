from Players import HumanPlayer, MinMaxPlayerPruning, MinMaxPlayer
from Game import Game
from Heuristics import SimpleHeuristic, AdvancedHeuristic

class App:

    # Constructor
    def __init__(self) -> None:
        self.gameN = 4
        self.rows = 6
        self.columns = 7
        self.players = []
                          
    def getGame(self):
        return Game(self.gameN, self.rows, self.columns, self.players)

    # Asks the user for the number of rows, columns, and gameN
    def getBoardSettings(self):
         
        default = input("Do you want to use the default board size (6x7) [yes/no]? ")

        if(default != "yes"):
            
            # Get rows
            self.rows = int(input("How many rows? "))

            # Get columns
            while(True):
                self.columns = int(input("How many columns? (Must be odd) "))

                if self.columns % 2 == 0:
                    print("Invalid - column count is even.")
                else:
                    break
        
            # Get gameN
            self.gameN = int(input("How many pieces in a row is a win? "))

    def getPlayers(self):
            
            heuristic1 = SimpleHeuristic.SimpleHeuristic(self.gameN)
            heuristic2 = SimpleHeuristic.SimpleHeuristic(self.gameN)
            players = []

            # First player
            human = HumanPlayer.HumanPlayer(1, self.gameN, heuristic1)
            players.append(human)

            # Second player
            opponent = int(input("Who would you like to play against: Human[1] or Computer[2]? "))

            if(opponent==1):
                 
                human = HumanPlayer.HumanPlayer(2, self.gameN, heuristic2)
                players.append(human)

            elif(opponent==2):
                 
                depth = int(input("What depth should the computer go to? "))
                 
                alphabeta = input("Should the computer use alpha beta pruning? [yes/no] ")
                if(alphabeta=="yes"):
                    computer = MinMaxPlayerPruning.MinMaxPlayerPruning(2, depth, self.gameN, heuristic2)
                elif(alphabeta=="no"):
                    computer = MinMaxPlayer.MinMaxPlayer(2, depth, self.gameN, heuristic2)

                players.append(computer)
           
            self.players = players

    def start(self):
        self.getBoardSettings()
        self.getPlayers()
        game = self.getGame()
        game.startGame()

    
app = App()
app.start()