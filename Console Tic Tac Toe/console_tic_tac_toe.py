import math


class InvalidPosition(Exception):
    pass

# checking for a win


def symbol_selection():
    while True:
        one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O'?: ").upper()

        if one_symbol == "X":
            two_symbol = "O"
            break
        elif one_symbol == "O":
            two_symbol = "X"
            break
        else:
            print("Please select a valid symbol!")

    return one_symbol, two_symbol


def print_board_numeration():
    print("This is the numeration of the board:")
    for num in range(1, 10, 3):
        print(f"|  {num}  |  {num + 1}  |  {num + 2}  |")


def place_symbol(pos, board):
    row = math.ceil(pos / 3) - 1
    col = pos % 3 - 1
    invalid = False

    if board[row][col] == " ":
        board[row][col] = symbol
    else:
        print("This position was already selected! Choose other!")
        invalid = True

    return board, invalid


def print_board(board):
    for row in range(3):
        print(f"|  {board[row][0]}  |  {board[row][1]}  |  {board[row][2]}  |")

    return board


def check_winner(board):
    won = False
    player_num = ""
    for row in range(3):
        if not all(board[row]) and all(board[row]) == " ":
            won = True
            if board[row][1] == "X":
                player_num = "one"
            else:
                player_num = "two"

            return won, player_num

        if board[0][row] == board[1][row] and board[1][row] == board[2][row] and \
                board[1][row] != " ":
            won = True

            if board[row][1] == "X":
                player_num = "one"
            else:
                player_num = "two"

            return won, player_num

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
        won = True
        if board[1][1] == "X":
            player_num = "one"
        else:
            player_num = "two"

        return won, player_num

    if board[2][2] == board[1][1] and board[1][1] == board[2][0] and board[2][2] != " ":
        won = True
        if board[1][1] == "X":
            player_num = "one"
        else:
            player_num = "two"

        return won, player_num

    return won, player_num

def play_again(board, player_one_name, player_two_name, player_one_symbol, player_two_symbol):
    is_again = True
    restart_the_game = input("Would you like to play again? (y/n): ").lower()
    if restart_the_game == "y":
        print(f"\n==================================\n")
        board = [[" " for x in range(3)] for y in range(3)]
        player_one_name = input("Player one name: ")
        player_two_name = input("Player one name: ")
        player_one_symbol, player_two_symbol = symbol_selection()
        print_board_numeration()
        print(f"{player_one_name} starts first!")
    else:
        is_again = False

    return is_again, board, player_one_name, player_two_name, player_one_symbol, player_two_symbol


def board_full(b):
    for row in b:
        for col in row:
            if col == " ":
                return False

    return True


# reading and saving players names
player_one_name = input("Player one name: ").strip()
player_two_name = input("Player two name: ").strip()

# creating the board
board = [[" " for x in range(3)] for y in range(3)]

# reading and saving players symbols

player_one_symbol, player_two_symbol = symbol_selection()

# printing the numeration of the board

print_board_numeration()

# first player

print(f"{player_one_name} starts first!")

# placing the symbol on the board if possible

counter = 0
while True:
    player = player_one_name if counter % 2 == 0 else player_two_name
    symbol = player_one_symbol if counter % 2 == 0 else player_two_symbol

    # choosing the symbol position
    try:
        position = int(input(f"{player} choose a free position [1 - 9]: "))
        if position < 1 or position > 9:
            raise InvalidPosition
    except (ValueError, InvalidPosition):
        print(f"Position must be a integer between 1 and 9 inclusive! Please try again!")
        continue

    # placing the symbol on its position
    board, invalid = place_symbol(position, board)

    if invalid:
        continue
    # print the board after the move
    print_board(board)

    # check if the player won

    won, player_won = check_winner(board)

    if won:
        if player_won == "one":
            player_won = player_one_name
        else:
            player_won = player_two_name

        print(f"{player_won} won!")

        restart, board, player_one_name, player_two_name, player_one_symbol, player_two_symbol = play_again(board, player_one_name, player_two_name, player_one_symbol, player_two_symbol)

        if not restart:
            print("Have a nice day! :)")
            break
        else:
            counter = 0
            continue

    if board_full(board):
        print("Draw")
        restart, board, player_one_name, player_two_name, player_one_symbol, player_two_symbol = play_again(board, player_one_name, player_two_name, player_one_symbol, player_two_symbol)
        if not restart:
            print("Have a nice day! :)")
            break

        else:
            counter = 0
            continue

    counter += 1
