board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

current_player = 1
winner = None
playing = True

def print_board(game_board):
    """ Prints the list that represents the gameboard, separating each item so that what is printed looks like the actual gameboard."""
    print(game_board[0][0] + " | " + game_board[0][1] + " | " + game_board[0][2])
    print("---------")
    print(game_board[1][0] + " | " + game_board[1][0] + " | " + game_board[1][0])
    print("---------")
    print(game_board[2][0] + " | " + game_board[2][0] + " | " + game_board[2][0])


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
            current_player = 2
        else:
            board[row][column] = "O"
            current_player = 1
    else:
        print("Sorry, that spot's already taken! Choose another.")


