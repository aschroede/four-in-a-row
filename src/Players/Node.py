# Node class for building up the tree structure
class Node:

    def __init__(self, board):
        self.board = board
        self.value = None
        self.column = None
        self.children = []

    # Adds children nodes
    def addChild(self, child):
        self.children.append(child)