from Players import Human, MinMax, MinMaxPruning
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
        
            players = []

            player1 = self.getPlayer(1)
            player2 = self.getPlayer(2)

            players.append(player1)
            players.append(player2)
           
            self.players = players

    def getPlayer(self, playerID):
        heuristic = SimpleHeuristic.SimpleHeuristic(self.gameN)

        playerType = int(input("Select player type: Human(1), MinMax(2), AlphaBeta(3): "))

        if(playerType==1):
            return Human.HumanPlayer(playerID, self.gameN, heuristic)
        else:
            depth = int(input("What depth should the computer go to? "))

            if(playerType==2):
                return MinMax.MinMaxPlayer(playerID, depth, self.gameN, heuristic)
            else:
                return MinMaxPruning.MinMaxPlayerPruning(playerID, depth, self.gameN, heuristic)


    def start(self):
        self.getBoardSettings()
        self.getPlayers()
        game = self.getGame()
        game.startGame()

    
app = App()
app.start()