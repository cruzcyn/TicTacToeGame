board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

winner = None
playing = True

# PRINT GAMEBOARD TO THE CONSOLE 

# If done inside of a function and split into different lines of print statements, we can print something to the console that looks like a board
# while preventing writing so many repetitive lines of code throughout the game

def printBoard(game_board):
    """ Prints the list that represents the gameboard, separating each item so that what is printed looks like the actual gameboard."""
    print(game_board[0][0] + " | " + game_board[0][1] + " | " + game_board[0][2])
    print("---------")
    print(game_board[1][0] + " | " + game_board[1][0] + " | " + game_board[1][0])
    print("---------")
    print(game_board[2][0] + " | " + game_board[2][0] + " | " + game_board[2][0])

printBoard(board)

# TODO: take player input


# GAME LOGIC IMPLEMENTATION

# Greet user
print("Welcome to TicTacToe!")

# Game loop
while playing:
    printBoard(board)
    
    # Ask for player input
    current_player_input = input("In which row and column, respectively, would you like to make your move? ")
    row = int(current_player_input.split(",")[0])
    column = int(current_player_input.split(",")[1])

    # TODO: check if space in board is empty
    if board[row][column] == " ":
        

    # Safe exit from while loop for testing purposes:
    playing = False
    print("Bye!")

# TODO: check if space in board is empty
# TODO: check for win or tie
# TODO: switch player
# TODO: loop until someone wins or there's a tie
