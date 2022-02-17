xoxo = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
win_state = 0
x_win_state = 0
o_win_state = 0
move_count = 0
x_count = 0
o_count = 0
players_turn = 'X'

row_coordinates = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]
legal_moves = {
    (1, 1): 0, (1, 2): 1, (1, 3): 2,
    (2, 1): 3, (2, 2): 4, (2, 3): 5,
    (3, 1): 6, (3, 2): 7, (3, 3): 8
}
legal_numbers = [1, 2, 3]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def print_table():
    print('-' * 9)
    print('| ' + xoxo[0] + ' ' + xoxo[1] + ' ' + xoxo[2] + ' |')
    print('| ' + xoxo[3] + ' ' + xoxo[4] + ' ' + xoxo[5] + ' |')
    print('| ' + xoxo[6] + ' ' + xoxo[7] + ' ' + xoxo[8] + ' |')
    print('-' * 9)


def letter_count():
    global move_count
    global x_count
    global o_count
    for letter in xoxo:
        if letter != '_':
            move_count += 1
        if letter == 'X':
            x_count += 1
        if letter == 'O':
            o_count += 1


def game_state():
    if o_win_state >= 1 and x_win_state >= 1:
        print("Impossible")
    elif max(x_count, o_count) - min(x_count, o_count) > 1:
        print("Impossible")
    elif o_win_state == 0 and x_win_state == 0 and move_count == 9:
        print("Draw")
    elif o_win_state == 1:
        print("O wins")
    elif x_win_state == 1:
        print("X wins")
    else:
        print("Game not finished")


def win_check(x, y, z):
    global win_state
    global x_win_state
    global o_win_state
    if xoxo[x] == xoxo[y] and xoxo[x] == xoxo[z] and xoxo[x] != '_':
        win_state += 1
        if xoxo[x] == 'X':
            x_win_state += 1
        elif xoxo[x] == 'O':
            o_win_state += 1
        else:
            pass
    else:
        pass


def user_input():
    if x_movex not in numbers or x_movey not in numbers:
        return 'You should enter numbers!'
    elif x_movex not in legal_numbers or x_movey not in legal_numbers:
        return 'Coordinates should be from 1 to 3!'
    elif xoxo[legal_moves[x_move]] != '_':
        return 'This cell is occupied! Choose another one!'
    else:
        return True


def ask_user_input():
    global x_movex
    global x_movey
    global x_move
    (x_movex, x_movey) = input('Enter the coordinates: ').split()
    x_movex = int(x_movex)
    x_movey = int(x_movey)
    x_move = (x_movex, x_movey)


print_table()
while True:
    ask_user_input()
    if user_input() == True:
        if players_turn == 'X':
            xoxo[legal_moves[x_move]] = players_turn
            players_turn = 'O'
        elif players_turn == 'O':
            xoxo[legal_moves[x_move]] = players_turn
            players_turn = 'X'
        else:
            pass
        move_count += 1
        print_table()
    elif user_input() != True:
        print(user_input())
    else:
        pass
    for row in row_coordinates:
        win_check(row[0], row[1], row[2])
    if win_state == 1 or move_count > 8:
        game_state()
        break
    else:
        continue
