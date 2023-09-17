from Players import HumanPlayer
from Game import Game

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
            #heuristic1 = SimpleHeuristic(gameN)
            #heuristic2 = SimpleHeuristic(gameN)

            human1 = HumanPlayer.HumanPlayer(1, gameN, None)
            human2 = HumanPlayer.HumanPlayer(2, gameN, None)

            #TODO: Implment other PlayerControllers (MinMax, AlphaBeta)


            players = []
            players.append(human1)
            players.append(human2)
            return players
    
    

app = App()