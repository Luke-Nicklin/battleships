import random

"""
Battleships welcome message
"""

print("*** Welcome to Battleships! Let's play... ***")

"""
Ask user to select number of rows
"""
while True:
    try:
        rows = int(input("Enter the number of rows between 5 and 10: \n"))
        if 5 <= rows <= 10:
            break
        else:
            print("You must enter a number between 5 and 10.")
    except ValueError:
        print("Error. You must enter a valid number.")

"""
Ask user to select number of columns
"""
while True:
    try:
        columns = int(input("Enter the number of columns between 5 and 10: \n"))
        if 5 <= columns <= 10:
            break
        else:
            print("You must enter a number between 5 and 10.")
    except ValueError:
        print("Error. You must enter a valid number.")

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [["." for _ in range(columns)] for _ in range(rows)]
        self.ships = []

    def display_board(self):
        print(" ", end="")
        for i in range(self.columns):
            print(i + 1, end=" ")
        print()

        for i in range(self.rows):
            print(i + 1, end=" ")
            for j in range(self.columns):
                print(self.board[i][j], end=" ")
            print()

player_board = Board(rows, columns)
computer_board = Board(rows, columns)

print("Your board:")
player_board.display_board()

print("Computer's board:")
computer_board.display_board()

while True:
    try:
        player_column = int(input("Choose a column: \n"))
        if 1 <= rows <= 10:
            break
        else:
            print("You must enter a number between 1 and 10.")
    except ValueError:
        print("Error. You must enter a valid number.")

while True:
    try:
        player_row = int(input("Choose a row: \n"))
        if 1 <= columns <= 10:
            break
        else:
            print("You must enter a number between 1 and 10.")
    except ValueError:
        print("Error. You must enter a valid number.")
