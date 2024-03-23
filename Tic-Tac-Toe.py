# Create the board
board = [' '] * 9

# Define winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

# Function to print the board
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Function to check if a player has won
def check_winner(player):
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()

        # Get the current player's move
        move = input("It's Player " + current_player + "'s turn. Enter the position (1-9): ")

        # Validate the move
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == ' ':
            move = int(move) - 1
            board[move] = current_player

            # Check if the current player has won
            if check_winner(current_player):
                print_board()
                print('Player', current_player, 'wins!')
                game_over = True
            # Check if the game is a draw
            elif is_board_full():
                print_board()
                print("It's a draw!")
                game_over = True
            else:
                # Switch to the other player
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Invalid move. Try again.')

# Start the game
play_game()
