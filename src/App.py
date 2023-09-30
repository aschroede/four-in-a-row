from Players import HumanPlayer, MinMaxPlayerPruning, MinMaxPlayer
from Game import Game
from Heuristics import SimpleHeuristic, AdvancedHeuristic

class App:

    game = 0

    def __init__(self) -> None:
        gameN = 4
        rows = 6
        columns = 7

        players = []
        players = self.getPlayers(gameN)

        game = Game(gameN, rows, columns, players)                  
        game.startGame()

    def startGame(self):
         self.startGame()
                                        
    def getPlayers(self,gameN):
            heuristic1 = SimpleHeuristic.SimpleHeuristic(gameN)
            heuristic2 = SimpleHeuristic.SimpleHeuristic(gameN)
            heuristic3 = AdvancedHeuristic.AdvancedHeuristic(gameN)
            heuristic4 = AdvancedHeuristic.AdvancedHeuristic(gameN)

            human1 = HumanPlayer.HumanPlayer(1, gameN, heuristic1)
            player2 = HumanPlayer.HumanPlayer(2, gameN, heuristic4)
            pruning = MinMaxPlayerPruning.MinMaxPlayerPruning(2, 5, gameN, heuristic2)
            nopruning = MinMaxPlayer.MinMaxPlayer(2, 5, gameN, heuristic2)

            #TODO: Implment other PlayerControllers (MinMax, AlphaBeta)

            players = []
            players.append(human1)
            players.append(pruning)
            return players
    
app = App()