from . import PlayerController
from . import Node
import sys
from Game import Game

class MinMaxPlayer(PlayerController.PlayerController):
    
    def __init__(self, playerID, depth, gameN, heuristic):
        self.playerID = playerID
        self.depth = depth
        self.gameN = gameN
        self.heuristic = heuristic
        
    def makeMove(self, board): 

        maxValue = -sys.maxsize
        maxMove = 0

        startNode = Node.Node(board)
        self.miniMax(startNode, self.depth, self.playerID)
        
        for child in startNode.children:
            if child.value > maxValue:
                maxValue = child.value
                maxMove = child.column           

        return maxMove

    def miniMax(self, node, depth, player):
            
            # Base cases to bottom out the recursion. 

            # 1) Depth = 0
            if(depth == 0):
                
                # Evaluate nodes
                node.value = self.heuristic.evaluateBoard(player, node.board)
                return node.value
        
            # 2) Game over
            winner = Game.winning(node.board.boardState, self.gameN)
            if(winner != 0):
                if(winner == self.playerID):
                    node.value = sys.maxsize
                else:
                     node.value = -sys.maxsize
                return node.value
            
            # Generate child nodes of this node
            for i in range(node.board.columns):
                if node.board.isValid(i):
                    new_Node = Node.Node(node.board.getNewBoard(i, player))
                    new_Node.column = i
                    node.addChild(new_Node)
            
            # Perform minimax on nodes
            if(player == self.playerID): # We are the maximiser
                currentMax = -sys.maxsize

                for child in node.children:
                    evalResult = self.miniMax(child, depth-1, 1 if player==2 else 2)   # Recursion step
                    currentMax = max(currentMax, evalResult)
                
                node.value = currentMax
                return currentMax
                 
            else: # We are the minimizer
                currentMin = sys.maxsize

                for child in node.children:
                    evalResult = self.miniMax(child, depth-1, 1 if player==2 else 2)    # Recursion step
                    currentMin = min(currentMin, evalResult)
                
                node.value = currentMin
                return currentMin
                    
                 
        