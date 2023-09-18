from Players import HumanPlayer
from Game import Game
from Heuristics import SimpleHeuristic

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

            # This is a test
            #This is another test

            human1 = HumanPlayer.HumanPlayer(1, gameN, heuristic1)
            human2 = HumanPlayer.HumanPlayer(2, gameN, heuristic2)

            #TODO: Implment other PlayerControllers (MinMax, AlphaBeta)


            players = []
            players.append(human1)
            players.append(human2)
            return players
    
    

app = App()