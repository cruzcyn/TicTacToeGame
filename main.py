board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

current_player = 1
playing = True

def print_board(game_board):
    """ Prints the list that represents the gameboard, separating each item so that what is printed looks like the actual gameboard."""
    print(game_board[0][0] + " | " + game_board[0][1] + " | " + game_board[0][2])
    print("---------")
    print(game_board[1][0] + " | " + game_board[1][0] + " | " + game_board[1][0])
    print("---------")
    print(game_board[2][0] + " | " + game_board[2][0] + " | " + game_board[2][0])

# Check winning conditions
def check_horizontals(game_board):
    """ Checks that the strings in the horizontals are all the same, but that they aren't whitespaces. If so, returns True."""
    if game_board[0][0] == game_board[0][1] == game_board[0][2] and game_board[0][0] != " ":
        return True
    elif game_board[1][0] == game_board[1][1] == game_board[1][2] and game_board[1][0] != " ":
        return True
    elif game_board[2][0] == game_board[2][1] == game_board[2][2] and game_board[2][0] != " ":
        return True
    
def check_verticals(game_board):
    """ Checks that the strings in the verticals are all the same, but that they aren't whitespaces. If so, returns True."""
    if game_board[0][0] == game_board[1][0] == game_board[2][0] and game_board[0][0] != " ":
        return True
    elif game_board[0][1] == game_board[1][1] == game_board[2][1] and game_board[0][1] != " ":
        return True
    elif game_board[0][2] == game_board[1][2] == game_board[2][2] and game_board[0][2] != " ":
        return True
    
def check_diagonals(game_board):
    """ Checks that the strings in the diagonals are all the same, but that they aren't whitespaces. If so, returns True."""
    if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] != " ":
        return True
    elif game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[0][2] != " ":
        return True

# Check for tie:
def check_tie(game_board):
    """ Checks if there are any more whitespaces in the board and returns true in case there aren't (meaning that the board is full)"""
    if " " not in board:
        return True

# GAME LOGIC IMPLEMENTATION

# Greet user
print("Welcome to TicTacToe!")

# Game loop
while playing:
    print_board(board)
    print(f"Current player: {current_player}")
    # Ask for player input
    current_player_input = input("In which row and column, respectively, would you like to make your move? ")
    row = int(current_player_input.split(",")[0])
    column = int(current_player_input.split(",")[1])
    
    if board[row][column] == " ":
        if current_player == 1:
            board[row][column] = "X"
            if check_horizontals or check_verticals or check_diagonals:
                playing = False
                print(f"The winner is player {current_player}!")
            elif check_tie(board):
                playing = False
                print(f"There's a tie!")
            else:
                current_player = 2
        else:
            board[row][column] = "O"
            if check_horizontals or check_verticals or check_diagonals:
                playing = False
                print(f"The winner is player {current_player}!")
            else:
                current_player = 1
    else:
        print("Sorry, that spot's already taken! Choose another.")


