board = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " ",
]

winner = None
playing = True

# PRINT GAMEBOARD TO THE CONSOLE 

# If done inside of a function, split into different lines of print statements, 
# we can print something that looks like a board
# while preventing writing so many repetitive lines of code throughout the game
def printBoard(game_board):
    """ Prints the list that represents the gameboard formatted in a way that makes it look like the game when it's played with pen and paper."""
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print("---------")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print("---------")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])

printBoard(board)

# TODO: take player input
# TODO: check if space in board is empty
# TODO: check for win or tie
# TODO: switch player
# TODO: loop until someone wins or there's a tie
