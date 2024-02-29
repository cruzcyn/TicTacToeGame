board = [
    ".", ".", ".",
    ".", ".", ".",
    ".", ".", ".",
]

current_player = 1
playing = True

def print_board(game_board):
    """ Prints the list that represents the gameboard, separating each item so that what is printed looks like the actual gameboard."""
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print("---------")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print("---------")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])

# Check winning conditions
def check_horizontals(game_board):
    """ Checks that the strings in the horizontals are all the same, but that they aren't whitespaces. If so, returns True."""
    if game_board[0] == game_board[1] == game_board[2] and game_board[0] != ".":
        return True
    elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != ".":
        return True
    elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != ".":
        return True
    else:
        return False
    
def check_verticals(game_board):
    """ Checks that the strings in the verticals are all the same, but that they aren't whitespaces. If so, returns True."""
    if game_board[0] == game_board[3] == game_board[6] and game_board[0] != ".":
        return True
    elif game_board[1] == game_board[4] == game_board[7] and game_board[1] != ".":
        return True
    elif game_board[2] == game_board[5] == game_board[8] and game_board[2] != ".":
        return True
    else:
        return False
    
def check_diagonals(game_board):
    """ Checks that the strings in the diagonals are all the same, but that they aren't whitespaces. If so, returns True."""
    if game_board[0] == game_board[4] == game_board[8] and game_board[0] != ".":
        return True
    elif game_board[2] == game_board[4] == game_board[6] and game_board[2] != ".":
        return True
    else:
        return False

# Check for tie:
def check_tie(game_board):
    """ Checks if there are any more whitespaces in the board and returns true in case there aren't (meaning that the board is full)"""
    if "." not in board:
        return True
    else:
        return False

# GAME LOGIC IMPLEMENTATION

# Greet user
print("Welcome to TicTacToe!")

# Game loop
while playing:
    print_board(board)

    # Ask for player input
    current_player_input = int(input("Type a number from 0 to 8: "))
    
    # Check to see if the location wanted by the player is empty:
    if board[current_player_input] == ".":

        # Check who's playing so that the appropriate string can be passed to the location wanted
        if current_player == 1:
            board[current_player_input] = "X"
            if check_horizontals(board) or check_verticals(board) or check_diagonals(board):
                playing = False
                print_board(board)
                print(f"The winner is player {current_player}!")
            elif check_tie(board):
                playing = False
                print_board(board)
                print(f"There's a tie!")
            else:
                current_player = 2
        else:
            board[current_player_input] = "O"
            if check_horizontals(board) or check_verticals(board) or check_diagonals(board):
                playing = False
                print_board(board)
                print(f"The winner is player {current_player}!")
            elif check_tie(board):
                playing = False
                print_board(board)
                print(f"There's a tie!")
            else:
                current_player = 1
    else:
        print("Sorry, that spot's already taken! Choose another.")
