from random import randint
import random
import sys


def ticttGame():
    def print_board():
        print(row1)
        print(row2)
        print(row3)

    o = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    choose_spot = []
    playing = True
    row1 = ["0", "1", "2"]
    row2 = ["3", "4", "5"]
    row3 = ["6", "7", "8"]

    print_board()

    while playing:

        player1 = input("Player 1, Choose a number to place your x\n")
        player2 = input("Player 2, Choose a number to place your o\n")

        if player1 == "0":
            row1[0] = "x"
            print("Player 2's turn")
        # print_board()
        if player2 == "0":
            row1[0] = "o"

        if player1 == "1":
            row1[1] = "x"
            print("Player 2's turn")
        # print_board()
        if player2 == "1":
            row1[1] = "o"

        if player1 == "2":
            row1[2] = "x"
            print("Player 2's turn")
        # print_board()
        if player2 == "2":
            row1[2] = "o"

        if player1 == "3":
            row2[0] = "x"
            print("Player 2's turn")
        # print_board()
        if player2 == "3":
            row2[0] = "o"

        if player1 == "4":
            row2[1] = "x"
            print("Player 2's turn")
        # print_board()
        if player2 == "4":
            row2[1] = "o"

        if player1 == "5":
            row2[2] = "x"
            print("Player 2's turn")
        # print_board()
        if player2 == "5":
            row2[2] = "o"

        if player1 == "6":
            row3[0] = "x"
            print("Player 2's turn")
        # print_board()
        if player2 == "6":
            row3[0] = "o"

        if player1 == "7":
            row3[1] = "x"
            print("Player 2's turn")
        # print_board()
        if player2 == "7":
            row3[1] = "o"

        if player1 == "8":
            row3[2] = "x"
            print("Player 2's turn")
        # print_board()
        if player2 == "8":
            row3[2] = "o"

        print_board()
        if (row1[0] == "x" and row1[1] == "x" and row1[2] == "x" or \
                row2[0] == "x" and row2[1] == "x" and row2[2] == "x" or \
                row3[0] == "x" and row3[1] == "x" and row3[2] == "x" or \
                row1[0] == "x" and row2[0] == "x" and row3[0] == "x" or \
                row1[1] == "x" and row2[1] == "x" and row3[1] == "x" or \
                row1[2] == "x" and row2[2] == "x" and row3[2] == "x" or \
                row1[2] == "x" and row2[1] == "x" and row3[0] == "x" or \
                row1[0] == "x" and row2[1] == "x" and row3[2] == "x"):
            print("Player 1 Wins!")
            playing = False
        elif (row1[0] == "o" and row1[1] == "o" and row1[2] == "o" or \
              row2[0] == "o" and row2[1] == "o" and row2[2] == "o" or \
              row3[0] == "o" and row3[1] == "o" and row3[2] == "o" or \
              row1[0] == "o" and row2[0] == "o" and row3[0] == "o" or \
              row1[1] == "o" and row2[1] == "o" and row3[1] == "o" or \
              row1[2] == "o" and row2[2] == "o" and row3[2] == "o" or \
              row1[2] == "o" and row2[1] == "o" and row3[0] == "o" or \
              row1[0] == "o" and row2[1] == "o" and row3[2] == "o"):
            print("Player 2 Wins!")
            playing = False
        else:
            pass




ticttGame()