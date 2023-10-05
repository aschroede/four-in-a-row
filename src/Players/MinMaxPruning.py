from . import PlayerController
from Heuristics import AdvancedHeuristic
from Heuristics import SimpleHeuristic
from . import Node
import sys
from Game import Game

class MinMaxPlayerPruning(PlayerController.PlayerController):

    # Constructor
    def __init__(self, playerID, depth, gameN, heuristic):
        self.playerID = playerID
        self.depth = depth
        self.gameN = gameN
        self.heuristic = heuristic
        self.history = []
    
    def makeMove(self, board): 

        maxValue = -sys.maxsize
        maxMove = -1
        
        # Create a node from the current board state
        startNode = Node.Node(board)
        
        # Run miniMax on this node
        self.miniMax(startNode, self.depth, -sys.maxsize, sys.maxsize, self.playerID)
        
        # Go through the children of the current boardstate and select the child
        # with the highest value and return the associated column.
        for child in startNode.children:
            if child.value >= maxValue:
                maxValue = child.value
                maxMove = child.column           

        # Record move
        self.history.append(maxMove+1)
        return maxMove


    def miniMax(self, node, depth, alpha, beta, player):
            
        # ----Base cases to bottom out the recursion----

        # 1) Depth = 0
        if(depth == 0):
            
            # Evaluate nodes
            if(type(self.heuristic) == SimpleHeuristic.SimpleHeuristic):
                node.value = self.heuristic.evaluateBoard(player, node.board)
            else:
                node.value = self.heuristic.getBestAction(player, node.board)
            return node.value
    
        # 2) Game over
        winner = Game.winning(node.board.boardState, self.gameN)
        if(winner != 0):
            if(winner == self.playerID):
                node.value = sys.maxsize
            else:
                    node.value = -sys.maxsize
            return node.value


        # ----Recursive State----

        # Perform minimax on nodes
        if(player == self.playerID): 
            currentMax = -sys.maxsize

            for i in range (node.board.columns):
                if node.board.isValid(i):

                    # Generate children nodes for valid moves
                    child = Node.Node(node.board.getNewBoard(i, player))
                    child.column = i
                    node.addChild(child)

                    # Perform minMax on child nodes
                    evalResult = self.miniMax(child, depth-1, alpha, beta, 1 if player==2 else 2)
                    currentMax  = max(currentMax, evalResult)    # Recursion step

                    # Perforam alpha/beta pruning
                    alpha = max(alpha, currentMax)
                    if beta < alpha:
                        break
            
            node.value = currentMax
            return currentMax
                
        else: # We are the minimizer
            currentMin = sys.maxsize

            for i in range (node.board.columns):
                if node.board.isValid(i):

                    # Generate children nodes for valid moves
                    child = Node.Node(node.board.getNewBoard(i, player))
                    child.column = i
                    node.addChild(child)

                    # Perform minMax on child nodes
                    evalResult = self.miniMax(child, depth-1, alpha, beta, 1 if player==2 else 2)
                    currentMin = min(currentMin, evalResult)     # Recursion step
                    
                    # Perforam alpha/beta pruning
                    beta = min(beta, currentMin)
                    if beta < alpha:
                        break
            
            node.value = currentMin
            return currentMin
                    
                 
        