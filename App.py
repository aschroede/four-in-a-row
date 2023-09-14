

class App:

    def __init__(self) -> None:
        gameN = 4
        boardWidth = 7
        boardHeight = 6

        players = []
        players = self.getPlayers(gameN)

        game = Game(gameN, boardWidth, boardHeight, players)


    def getPlayers(gameN):
            heuristic1 = SimpleHeuristic(gameN)
            heuristic2 = SimpleHeuristic(gameN)

            human1 = HumanPlayer(1, gameN, heuristic1)
            human2 = HumanPlayer(2, gameN, heuristic2)

            #TODO: Implment other PlayerControllers (MinMax, AlphaBeta)


            players = []
            players.append(human1, human2)
            return players
    
    

