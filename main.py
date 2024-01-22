# TIC TAC TOE GAME
# Done by João Pedro Costa
# 22/01/2024
import random


def attribute_symbol():
    # In this function attribute the users a number where 1 == X and 2 == O randomly
    # Then prints to users what symbol it was given to them
    # After that save the name and number the user in an array player1 and player2, then return both arrays
    # In here ask the users their name and pass them to the next function
    player_name1: str = input("Introduce first player name: ")
    player_name2: str = input("Introduce second player name: ")
    print("")

    num = random.randint(1, 2)
    if num == 1:
        player_num1 = 1
        player_num2 = 2
        player_symb1 = 'X'
        player_symb2 = 'O'
        print(player_name1, end=': X\n')
        print(player_name2, end=': O\n')
    else:
        player_num1 = 2
        player_num2 = 1
        player_symb1 = 'O'
        player_symb2 = 'X'
        print(player_name1, end=': O\n')
        print(player_name2, end=': X\n')

    print("")

    player1 = [player_name1, player_num1, player_symb1]
    player2 = [player_name2, player_num2, player_symb2]

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

    print("\nPlayers Options: ")
    print("00|01|02")
    print("10|11|12")
    print("20|21|22\n")


def vertical_win(board):
    # These function will check all the positions of the array vertically
    # If it does it will return the number that won vertically
    if board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:
        return 1
    elif board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
        return 2
    elif board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1:
        return 1
    elif board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
        return 2
    elif board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1:
        return 1
    elif board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
        return 2
    else:
        return 0


def horizontal_win(board):
    # These function willl check the array horizontally
    # If it does it will return the number that won
    if board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
        return 1
    elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
        return 2
    elif board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
        return 1
    elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
        return 2
    elif board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
        return 1
    elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
        return 2
    else:
        return 0


def diagonal_win(board):
    # These function will check the array in diagonal
    # If it does it will return the number that won
    if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        return 1
    elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        return 2
    elif board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 1:
        return 1
    elif board[2][0] == 2 and board[1][1] == 2 and board[0][2] == 2:
        return 2
    else:
        return 0


def verify_win(board, player1, player2):
    # These function will receive a number, and if confirm it
    # sees witch player has the number 1 for example and then
    # shows a print with the winner name
    if vertical_win(board) == 1:
        if player1[1] == 1:
            print("Player {} wins!".format(player1[0]))
        elif player2[1] == 1:
            print("Player {} wins!".format(player2[0]))
    elif vertical_win(board) == 2:
        if player1[1] == 2:
            print("Player {} wins!".format(player1[0]))
        elif player2[1] == 2:
            print("Player {} wins!".format(player2[0]))
    elif horizontal_win(board) == 1:
        if player1[1] == 1:
            print("Player {} wins!".format(player1[0]))
        elif player2[1] == 1:
            print("Player {} wins!".format(player2[0]))
    elif horizontal_win(board) == 2:
        if player1[1] == 2:
            print("Player {} wins!".format(player1[0]))
        elif player2[1] == 2:
            print("Player {} wins!".format(player2[0]))
    elif diagonal_win(board) == 1:
        if player1[1] == 1:
            print("Player {} wins!".format(player1[0]))
        elif player2[1] == 1:
            print("Player {} wins!".format(player2[0]))
    elif diagonal_win(board) == 2:
        if player1[1] == 2:
            print("Player {} wins!".format(player1[0]))
        elif player2[1] == 2:
            print("Player {} wins!".format(player2[0]))
    else:
        return 0


def player_choice(board, player1, player2):
    # As long as the verify function is equal to 0 (Nobody has won yet) it will ask the players to play. Each player
    # has a while so that when they exceed the size of the matrix they ask for a new input until it is valid, and then
    # they continue.
    # The x = -1 and y = 0 force entry in the while loop, and used twice to reset first player input.
    while verify_win(board, player1, player2) == 0:
        # ----------------------- Player 1 ------------------------
        x = -1
        y = 0
        while not (2 >= int(x) >= 0 == board[int(x)][int(y)] and 0 <= int(y) <= 2):
            x, y = input("Player {} - {} turn: ".format(player1[0], player1[2]))
        print(" ")

        board[int(x)][int(y)] = player1[1]
        print_board(board)
        print(" ")
        if verify_win(board, player1, player2) != 0:
            break

        # ------------------- Player 2 -----------------------------
        x = -1
        y = 0
        while not (2 >= int(x) >= 0 == board[int(x)][int(y)] and 0 <= int(y) <= 2):
            x, y = input("Player {} - {} turn: ".format(player2[0], player2[2]))

        print(" ")

        board[int(x)][int(y)] = player2[1]
        print_board(board)
        print(" ")
        if verify_win(board, player1, player2) != 0:
            break


def game():
    player1, player2 = attribute_symbol()
    while True:
        board = create_board()
        print_board(board)
        player_choice(board, player1, player2)
        exit_choice = input("You want to continue playing? (y/n): ")
        if exit_choice == "n" or exit_choice == "N":
            break
        else:
            continue


game()
