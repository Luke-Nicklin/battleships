import random
from random import randint

import colorama
# import colorma module
from colorama import init, Fore, Back, Style

# Initialize Colorama
init()

# import pyfiglet module 
import pyfiglet

"""
Battleships welcome message
"""
print("-" * 79)
print("Welcome to...")
print(" ")
result = pyfiglet.figlet_format("Battleships", font = "colossal" ) 
print(result)
print("Select the size of your board by entering the number of rows and columns below.")
print("Good luck!")
print("-" * 79)

"""
Asks the user to select easy or hard board
"""
def board_difficulty():
    while True:
        try:
            difficulty = input("Select difficulty: 'Easy' or 'Hard': ")
            if difficulty == "Easy":
                return 5, 5
            elif difficulty == "Hard":
                return 9, 9
            else:
                print("Invalid input. You must enter either 'Easy' or 'Hard'.")
        except ValueError:
            print("Invalid input. You must enter either 'Easy' or 'Hard'.")

rows, columns = board_difficulty(board)

"""
Creates the Battleships board.
Places the ships on the board randomly.
Allows the user to take a shot by selecting coordinates.
"""

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [["." for _ in range(columns)] for _ in range(rows)]
        self.ships = []
        self.hits = set()
        self.misses = set()

    def display_board(self, hide_ships=False):
        print("    ", end="")
        for i in range(self.columns):
            print("{:3}".format(i + 1), end=" ")
        print()

        for i in range(self.rows):
            print("{:3}".format(i + 1), end=" ")
            for j in range(self.columns):
                if hide_ships and (i, j) in self.ships and (i, j) not in self.hits and (i, j) not in self.misses:
                    print("  .", end=" ")
                else:
                    print("  " + self.board[i][j], end=" ")
            print()

    def ship_location(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.board[row][col] = "S"
            self.ships.append((row, col))
            return True
        return False
    
    def random_ship_location(self):
        while True:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.columns - 1)
            if self.ship_location(row, col):
                break

    def choose_coordinate(self, row, col):
        if (row, col) in self.hits or (row, col) in self.misses:
            return "Coordinate already selected"
        elif (row, col) in self.ships:
            self.hits.add((row, col))
            self.board[row][col] = "X"
            return "Hit!"
        else:
            self.misses.add((row, col))
            self.board[row][col] = "O"
            return "Miss!"

player_board = Board(rows, columns)
computer_board = Board(rows, columns)

num_ships = 5

for _ in range(num_ships):
    player_board.random_ship_location()
    computer_board.random_ship_location()

print("Your board:")
player_board.display_board()

print("Computer's board:")
computer_board.display_board(hide_ships=True)

"""
Allows the user to take a shot by selecting the coordinates.
"""
while True:
    try:
        row = int(input(f"Select a row (1-{rows}): ")) - 1
        col = int(input(f"Select a column (1-{columns}): ")) - 1
        if 0 <= row < rows and 0 <= col < columns:
            result = computer_board.choose_coordinate(row, col)
            print(result)
            computer_board.display_board(hide_ships=True)

            if "Hit!" in result:
                if len(computer_board.hits) == num_ships:
                    print(Fore.GREEN + "You sunk all the computer's ships.")
                    print(" ")
                    result = pyfiglet.figlet_format("Y o u  w i n !", font = "colossal" ) 
                    print(result) 
                    break
            
            computer_row = random.randint(0, rows - 1)
            computer_col = random.randint(0, columns - 1)
            computer_result = player_board.choose_coordinate(computer_row, computer_col)
            print(f"Computer's turn: {computer_result}")
            player_board.display_board()
            
        else:
            print(f"Please enter a row and column between 1 and {rows}/{columns}.")
    except ValueError:
        print("Please enter a valid number.")
