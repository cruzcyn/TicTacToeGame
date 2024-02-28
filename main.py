board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

current_player = 1
winner = None
playing = True

# PRINT GAMEBOARD TO THE CONSOLE 

# If done inside of a function and split into different lines of print statements, we can print something to the console that looks like a board
# while preventing writing so many repetitive lines of code throughout the game

def print_board(game_board):
    """ Prints the list that represents the gameboard, separating each item so that what is printed looks like the actual gameboard."""
    print(game_board[0][0] + " | " + game_board[0][1] + " | " + game_board[0][2])
    print("---------")
    print(game_board[1][0] + " | " + game_board[1][0] + " | " + game_board[1][0])
    print("---------")
    print(game_board[2][0] + " | " + game_board[2][0] + " | " + game_board[2][0])


def switch_player(current_player):
    """Checks to see whose turn is it currently and re-sets the variable to represent the other player."""
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1

# GAME LOGIC IMPLEMENTATION

# Greet user
print("Welcome to TicTacToe!")
# Game loop
while playing:
    print_board(board)
    
    # Ask for player input
    current_player_input = input("In which row and column, respectively, would you like to make your move? ")

    try:
        row = int(current_player_input.split(",")[0])
        column = int(current_player_input.split(",")[1])
    except ValueError:
        print("Invalid input. Your answer must be given in numbers formatted as such: 'row, column'")
    
    if board[row][column] == " ":
        if current_player == 1:
            board[row][column] = "X"
            current_player = 2
        else:
            board[row][column] = "O"
            current_player = 1
    else:
        print("Sorry, that spot's already taken! Choose another.")

    # "Secret password" to exit while loop for testing purposes:
    if current_player_input == "exit":
        playing = False
        print("Bye!")



# TODO: check for win or tie
# TODO: switch player
# TODO: loop until someone wins or there's a tie
