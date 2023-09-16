
from Board import Board


# let player PlayerId make a move in column x
def play(col, playerId, TwoDArray):
    # Iterate through each row
    for index, value in reversed(list(enumerate(TwoDArray))):
        print(index)





def main():
    input = ([[1, 2], [3, 4], [5, 6]])
    play(3, 3, input)
    board = Board(10, 10)
    print(board)


main()