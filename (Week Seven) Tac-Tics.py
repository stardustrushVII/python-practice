board = [' ' for _ in range(9)]

def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def make_move(position, player):
    if board[position] == ' ':
        board[position] = player
        return True
    else:
        print("Spot's taken, moron...")
        return False

def check_win(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)

def play_game():
    current_player = 'X'
    moves = 0

    while True:
        print_board()
        try:
            move = int(input(f"{current_player}'s turn (0–8): "))
        except ValueError:
            print("Please enter a number from 0 to 8.")
            continue

        if move < 0 or move > 8:
            print("Invalid move. Try again.")
            continue

        if make_move(move, current_player):
            moves += 1
            if check_win(current_player):
                print_board()
                print(f"{current_player} wins!")
                break
            elif moves == 9:
                print_board()
                print("Draw")
                break
            current_player = 'O' if current_player == 'X' else 'X'

play_game()