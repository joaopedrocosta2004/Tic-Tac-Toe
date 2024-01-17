# Here I want to create a Tic Tac Toe game
# 1º Ask the users their name -
# 2º Attribute the users a number for the board where 1 == X and 2 == O -
# 3º Create the board 3 x 3 and set it to 0 -
# 4º Print the board -
import random


def players_name():
    # In here ask the users their name and pass them to the next function
    player_name1: str = input("Introduce first player name: ")
    player_name2: str = input("Introduce second player name: ")
    print("")
    attribute_symbol(player_name1, player_name2)


def attribute_symbol(player_name1, player_name2):
    # In this function attribute the users a number where 1 == X and 2 == O randomly
    # Then prints to users what symbol it was given to them
    # After that save the name and number the user in an array player1 and player2, then return both arrays
    num = random.randint(1, 2)
    if num == 1:
        player_num1 = 1
        player_num2 = 2
        print(player_name1, end=': X\n')
        print(player_name2, end=': O\n')
    else:
        player_num1 = 2
        player_num2 = 1
        print(player_name1, end=': O\n')
        print(player_name2, end=': X\n')

    print("")

    player1 = [player_name1, player_num1]
    player2 = [player_name2, player_num2]

    return player1, player2


def create_board():
    # This function is used to create a 3 x 3 array, with 0 and return it
    # 0 means that the board is clean
    board = [[0 for i in range(3)] for j in range(3)]
    return board


def print_board(board):
    # Here prints the board to the users
    # The 0 in the board means clear space
    # The 1 means X player
    # The 2 means O player
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print("-", end=' ')
            elif board[i][j] == 1:
                print("X", end=' ')
            elif board[i][j] == 2:
                print("O", end=' ')
            if j < 2:
                print("|", end=' ')
        print("")


def game():
    # players_name()
    board = create_board()
    print_board(board)


game()
