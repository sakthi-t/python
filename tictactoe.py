user_input = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
number1 = 0  # Two numbers are stored as strings and type casted to integers
number2 = 0
numbers = [1, 2, 3]


def empty_board():  # Prints the empty board followed by 'X' and 'O' upon iteration
    print('-'*9)
    print(f'| {user_input[0]} {user_input[1]} {user_input[2]} |')
    print(f'| {user_input[3]} {user_input[4]} {user_input[5]} |')
    print(f'| {user_input[6]} {user_input[7]} {user_input[8]} |')
    print('-'*9)


empty_board()

# Two separate functions to determine whether X or Y is the winner.
# using count method to count the total numbers of 'X' and 'Y'


def x_winner(game=False):

    row1_x = user_input[0:3]
    row2_x = user_input[3:6]
    row3_x = user_input[6:9]

    col1_x = user_input[0] + user_input[3] + user_input[6]
    col2_x = user_input[1] + user_input[4] + user_input[7]
    col3_x = user_input[2] + user_input[5] + user_input[8]

    diagonal1_x = user_input[0] + user_input[4] + user_input[8]
    diagonal2_x = user_input[6] + user_input[4] + user_input[2]

    count_row1_x = row1_x.count('X')
    count_row2_x = row2_x.count('X')
    count_row3_x = row3_x.count('X')

    count_col1_x = col1_x.count('X')
    count_col2_x = col2_x.count('X')
    count_col3_x = col3_x.count('X')

    count_diagonal1_x = diagonal1_x.count('X')
    count_diagonal2_x = diagonal2_x.count('X')

    if count_row1_x == 3 or count_row2_x == 3 or count_row3_x == 3 or count_col1_x == 3 or count_col2_x == 3 or \
            count_col3_x == 3 or count_diagonal1_x == 3 or count_diagonal2_x == 3:
        game = True
        if game is True:
            return True
        else:
            return False


def y_winner(game=False):

    row1_y = user_input[0:3]
    row2_y = user_input[3:6]
    row3_y = user_input[6:9]

    col1_y = user_input[0] + user_input[3] + user_input[6]
    col2_y = user_input[1] + user_input[4] + user_input[7]
    col3_y = user_input[2] + user_input[5] + user_input[8]

    diagonal1_y = user_input[0] + user_input[4] + user_input[8]
    diagonal2_y = user_input[6] + user_input[4] + user_input[2]

    count_row1_y = row1_y.count('O')
    count_row2_y = row2_y.count('O')
    count_row3_y = row3_y.count('O')

    count_col1_y = col1_y.count('O')
    count_col2_y = col2_y.count('O')
    count_col3_y = col3_y.count('O')

    count_diagonal1_y = diagonal1_y.count('O')
    count_diagonal2_y = diagonal2_y.count('O')

    if count_row1_y == 3 or count_row2_y == 3 or count_row3_y == 3 or count_col1_y == 3 or count_col2_y == 3 or \
            count_col3_y == 3 or count_diagonal1_y == 3 or count_diagonal2_y == 3:
        game = True
        if game is True:
            return True
        else:
            return False


# The tic_tac_toe() uses a while loop and nested if statements. It's a very basic solution without abstraction.
# I've come only till lists. I just held on to the basics! Haven't hardcoded. Ensured that it works for a 3x3 matrix
def tic_tac_toe():
    count = 0
    game_start = False
    while not game_start:
        number = input('Enter the coordinates: ').split()
        try:
            if number[0].isnumeric() and number[1].isnumeric():
                number1 = int(number[0])
                number2 = int(number[1])

                if (number1 == 1 or number1 == 2 or number1 == 3) and (number2 == 1 or number2 == 2 or number2 == 3):

                    if user_input[6] == ' ' and number1 == 1 and number2 == 1 and (count == 0 or count == 2 or
                            count == 4 or count == 6):
                        user_input[6] = user_input[6].replace(' ', 'X')
                        empty_board()
                        count += 1
                        x_wins = x_winner()
                        if x_wins:
                            print('X wins')
                            game_start = True

                    elif user_input[6] == ' ' and number1 == 1 and number2 == 1 and (count == 1 or count == 3 or
                            count == 5 or count == 7):
                        user_input[6] = user_input[6].replace(' ', 'O')
                        empty_board()
                        count += 1
                        y_wins = y_winner()
                        if y_wins:
                            print('O wins')
                            game_start = True

                    elif user_input[7] == ' ' and number1 == 2 and number2 == 1 and (count == 0 or count == 2 or
                            count == 4 or count == 6):
                        user_input[7] = user_input[7].replace(' ', 'X')
                        empty_board()
                        count += 1
                        x_wins = x_winner()
                        if x_wins:
                            print('X wins')
                            game_start = True

                    elif user_input[7] == ' ' and number1 == 2 and number2 == 1 and (count == 1 or count == 3 or
                            count == 5 or count == 7):
                        user_input[7] = user_input[7].replace(' ', 'O')
                        empty_board()
                        count += 1
                        y_wins = y_winner()
                        if y_wins:
                            print('O wins')
                            game_start = True

                    elif user_input[8] == ' ' and number1 == 3 and number2 == 1 and (count == 0 or count == 2 or
                            count == 4 or count == 6):
                        user_input[8] = user_input[8].replace(' ', 'X')
                        empty_board()
                        count += 1
                        x_wins = x_winner()
                        if x_wins:
                            print('X wins')
                            game_start = True

                    elif user_input[8] == ' ' and number1 == 3 and number2 == 1 and (count == 1 or count == 3 or
                            count == 5 or count == 7):
                        user_input[8] = user_input[8].replace(' ', 'O')
                        empty_board()
                        count += 1
                        y_wins = y_winner()
                        if y_wins:
                            print('O wins')
                            game_start = True

                    elif user_input[3] == ' ' and number1 == 1 and number2 == 2 and (count == 0 or count == 2 or
                            count == 4 or count == 6):
                        user_input[3] = user_input[3].replace(' ', 'X')
                        empty_board()
                        count += 1
                        x_wins = x_winner()
                        if x_wins:
                            print('X wins')
                            game_start = True

                    elif user_input[3] == ' ' and number1 == 1 and number2 == 2 and (count == 1 or count == 3 or
                            count == 5 or count == 7):
                        user_input[3] = user_input[3].replace(' ', 'O')
                        empty_board()
                        count += 1
                        y_wins = y_winner()
                        if y_wins:
                            print('O wins')
                            game_start = True

                    elif user_input[4] == ' ' and number1 == 2 and number2 == 2 and (count == 0 or count == 2 or
                            count == 4 or count == 6):
                        user_input[4] = user_input[4].replace(' ', 'X')
                        empty_board()
                        count += 1
                        x_wins = x_winner()
                        if x_wins:
                            print('X wins')
                            game_start = True

                    elif user_input[4] == ' ' and number1 == 2 and number2 == 2 and (count == 1 or count == 3 or
                            count == 5 or count == 7):
                        user_input[4] = user_input[4].replace(' ', 'O')
                        empty_board()
                        count += 1
                        y_wins = y_winner()
                        if y_wins:
                            print('O wins')
                            game_start = True

                    elif user_input[5] == ' ' and number1 == 3 and number2 == 2 and (count == 0 or count == 2 or
                            count == 4 or count == 6):
                        user_input[5] = user_input[5].replace(' ', 'X')
                        empty_board()
                        count += 1
                        x_wins = x_winner()
                        if x_wins:
                            print('X wins')
                            game_start = True

                    elif user_input[5] == ' ' and number1 == 3 and number2 == 2 and (count == 1 or count == 3 or
                            count == 5 or count == 7):
                        user_input[5] = user_input[5].replace(' ', 'O')
                        empty_board()
                        count += 1
                        y_wins = y_winner()
                        if y_wins:
                            print('O wins')
                            game_start = True

                    elif user_input[0] == ' ' and number1 == 1 and number2 == 3 and (count == 0 or count == 2 or
                            count == 4 or count == 6):
                        user_input[0] = user_input[0].replace(' ', 'X')
                        empty_board()
                        count += 1
                        x_wins = x_winner()
                        if x_wins:
                            print('X wins')
                            game_start = True

                    elif user_input[0] == ' ' and number1 == 1 and number2 == 3 and (count == 1 or count == 3 or
                            count == 5 or count == 7):
                        user_input[0] = user_input[0].replace(' ', 'O')
                        empty_board()
                        count += 1
                        y_wins = y_winner()
                        if y_wins:
                            print('O wins')
                            game_start = True

                    elif user_input[1] == ' ' and number1 == 2 and number2 == 3 and (count == 0 or count == 2 or
                            count == 4 or count == 6):
                        user_input[1] = user_input[1].replace(' ', 'X')
                        empty_board()
                        count += 1
                        x_wins = x_winner()
                        if x_wins:
                            print('X wins')
                            game_start = True

                    elif user_input[1] == ' ' and number1 == 2 and number2 == 3 and (count == 1 or count == 3 or
                            count == 5 or count == 7):
                        user_input[1] = user_input[1].replace(' ', 'O')
                        empty_board()
                        count += 1
                        y_wins = y_winner()
                        if y_wins:
                            print('O wins')
                            game_start = True

                    elif user_input[2] == ' ' and number1 == 3 and number2 == 3 and (count == 0 or count == 2 or
                            count == 4 or count == 6):
                        user_input[2] = user_input[2].replace(' ', 'X')
                        empty_board()
                        count += 1
                        x_wins = x_winner()
                        if x_wins:
                            print('X wins')
                            game_start = True

                    elif user_input[2] == ' ' and number1 == 3 and number2 == 3 and (count == 1 or count == 3 or
                            count == 5 or count == 7):
                        user_input[2] = user_input[2].replace(' ', 'O')
                        empty_board()
                        count += 1
                        y_wins = y_winner()
                        if y_wins:
                            print('O wins')
                            game_start = True

                    elif user_input.count('X') == user_input.count('O'):
                        if (user_input.count('X') + user_input.count('O')) >= 8:
                            for x in user_input:
                                if x == ' ' and (count % 2 == 0):
                                    index_x = user_input.index(x)
                                    user_input[index_x] = user_input[index_x].replace(' ', 'X')
                                    empty_board()
                                    if (user_input[0] == 'X' and user_input[4] == 'X' and user_input[8] == 'X') or \
                                            (user_input[6] == 'X' and user_input[4] == 'X' and user_input[2] == 'X'):
                                        print('X wins')
                                    elif (user_input[0] == 'O' and user_input[4] == 'O' and user_input[8] == 'O') or \
                                            (user_input[6] == 'O' and user_input[4] == 'O' and user_input[2] == 'O'):
                                        print('O wins')
                                    else:
                                        print('Draw')
                                    game_start = True
                                elif x == ' ' and (count % 2 == 1):
                                    index_x = user_input.index(x)
                                    user_input[index_x] = user_input[index_x].replace(' ', 'O')
                                    empty_board()
                                    print('Draw')
                                    game_start = True
                        else:
                            print('Draw')
                            game_start = True

                    else:
                        print("This cell is occupied! Choose another one!")

                else:
                    print("Coordinates should be from 1 to 3!")

            else:
                print('You should enter numbers!')

        except IndexError:
            print("You should enter numbers!")

tic_tac_toe()
