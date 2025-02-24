import random

from random import randint

"""
Battleships welcome message
"""
print("-" * 79)
print("Welcome to BATTLESHIPS...")
print("Select the size of your board by entering the number of rows and columns below.")
print("Good luck!")
print("-" * 79)

"""
Ask user to select number of rows
"""
while True:
    try:
        rows = int(input("Enter the number of rows between 5 and 9: \n"))
        if 5 <= rows <= 9:
            break
        else:
            print("You must enter a number between 5 and 9.")
    except ValueError:
        print("Error. You must enter a valid number.")

"""
Ask user to select number of columns
"""
while True:
    try:
        columns = int(input("Enter the number of columns between 5 and 9: \n"))
        if 5 <= columns <= 9:
            break
        else:
            print("You must enter a number between 5 and 9.")
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

    def ship_location(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.board[row][col] = "S"
            self.ships.append((row, col))
            return True
        return False

player_board = Board(rows, columns)
computer_board = Board(rows, columns)

print("Your board:")
player_board.display_board()

print("Computer's board:")
computer_board.display_board()

while True:
    try:
        player_column = int(input("Enter a column of the ship: \n"))
        if 1 <= rows <= 9:
            break
        else:
            print("You must enter a number between 1 and 9.")
    except ValueError:
        print("Error. You must enter a valid number.")

while True:
    try:
        player_row = int(input("Enter a row of the ship: \n"))
        if 1 <= columns <= 9:
            break
        else:
            print("You must enter a number between 1 and 9.")
    except ValueError:
        print("Error. You must enter a valid number.")
