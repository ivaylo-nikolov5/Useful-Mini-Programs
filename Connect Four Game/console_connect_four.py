def check_win(field, row, col):
    won = False
    # left

    if col >= 3:
        if field[row][col] == field[row][col - 1] and field[row][col - 1] == field[row][col - 2] \
                and field[row][col - 2] == field[row][col - 3]:
            won = True
            return won

    # right

    if col <= 3:
        if field[row][col] == field[row][col + 1] and field[row][col + 1] == field[row][col + 2] \
                and field[row][col + 2] == field[row][col + 3]:
            won = True
            return won

    # up

    if row >= 3:
        if field[row][col] == field[row - 1][col] and field[row - 1][col] == field[row - 2][col] \
                and field[row - 2][col] == field[row - 3][col]:
            won = True
            return won

    # down

    if row <= 2:
        if field[row][col] == field[row + 1][col] and field[row + 1][col] == field[row + 2][col] \
                and field[row + 2][col] == field[row + 3][col]:
            won = True
            return won
    # up right

    if row >= 3 and col < 4:
        if field[row][col] == field[row - 1][col + 1] and field[row - 1][col + 1] == field[row - 2][col + 2] \
                and field[row - 2][col + 2] == field[row - 3][col + 3]:
            won = True
            return won

    # down right

    if row < 3 and col <= 3:
        if field[row][col] == field[row + 1][col + 1] and field[row + 1][col + 1] == field[row + 2][col + 2] \
                and field[row + 2][col + 2] == field[row + 3][col + 3]:
            won = True
            return won

    # up left

    if row >= 3 and col >= 3:
        if field[row][col] == field[row - 1][col - 1] and field[row - 1][col - 1] == field[row - 2][col - 2] \
                and field[row - 2][col - 2] == field[row - 3][col - 3]:
            won = True
            return won

    # down left

    if row <= 2 and col >= 3:
        if field[row][col] == field[row + 1][col - 1] and field[row + 2][col - 2] == field[row + 2][col - 2] \
                and field[row + 2][col - 2] == field[row + 3][col - 3]:
            won = True
            return won

    # edge case 1

    if 0 < col <= 4:
        if field[row][col] == field[row][col - 1] and field[row][col - 1] == field[row][col + 1] \
                and field[row][col + 1] == field[row][col + 2]:
            won = True
            return won
    if 1 < col < 5:
        if field[row][col] == field[row][col + 1] and field[row][col + 1] == field[row][col - 1] \
                and field[row][col - 1] == field[row][col - 2]:
            won = True
            return won

    # edge case 2

    if 1 < row < 5 and 0 < col < 5:
        if field[row][col] == field[row + 1][col - 1] and field[row + 1][col - 1] == field[row - 1][col + 1] \
                and field[row - 1][col + 1] == field[row - 2][col + 2]:
            won = True
            return won

    if 0 < row < 4 and 1 < col < 6:
        if field[row][col] == field[row - 1][col + 1] and field[row - 1][col + 1] == field[row + 1][col - 1] \
                and field[row + 1][col - 1] == field[row + 2][col - 2]:
            won = True
            return won

    if 0 < row < 4 and 0 < col < 5:
        if field[row][col] == field[row - 1][col - 1] and field[row - 1][col - 1] == field[row + 1][col + 1] \
                and field[row + 1][col + 1] == field[row + 2][col + 2]:
            won = True
            return won

    if 1 < row < 5 and 1 < col < 6:
        if field[row][col] == field[row + 1][col + 1] and field[row + 1][col + 1] == field[row - 1][col - 1] \
                and field[row - 1][col - 1] == field[row - 2][col - 2]:
            won = True
            return won


def insert_number(field, player, num):
    row, col = 5, player - 1
    while True:
        if row < 0:
            break

        if field[row][col] == 0:
            field[row][col] = num
            return field, row

        row -= 1


def print_field(f):
    print(*f, sep="\n")


def are_there_zeros(f):
    for row in f:
        for col in row:
            if col == 0:
                return True

    return False


def play_again():
    again = input("Do you want to play again? (y/n):").lower()
    return again


field = [[0 for x in range(7)] for _ in range(6)]
print("     Connect Four")
print_field(field)

player_num = 1
while True:
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        player_one = int(input(f"\nPlayer {player_num}, please choose a column: \n"))
        if 0 > player_one or 7 < player_one:
            print("Invalid column!!!")
            continue

        field, row = insert_number(field, player_one, player_num)

        row, col = row, player_one - 1
        print_field(field)

        if check_win(field, row, col):
            print(f"\nThe winner is player {player_num}")
            play = play_again()
            if play == "y":
                field = [[0 for x in range(7)] for _ in range(6)]
                print(f"\n    Connect Four")
                print_field(field)
                continue
            break
    except ValueError:
        print("Please insert number")
        continue

    if not are_there_zeros(field):
        print("The field is full! Game Over!")
        play = play_again()
        if play == "y":
            field = [[0 for x in range(7)] for _ in range(6)]
            print(f"\n    Connect Four")
            print_field(field)
            continue
        break

    player_num += 1
