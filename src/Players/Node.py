
class Node:

    def __init__(self, board):
        self.board = board
        self.value = None
        self.column = None
        self.children = []


    def addChild(self, child):
        self.children.append(child)