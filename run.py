import random
from random import randint

# import pyfiglet module
import pyfiglet

import colorama
# import colorma module
from colorama import init, Fore, Back, Style

# Initialize Colorama
init()

"""
Battleships welcome message
"""
print("-" * 79)
print("Welcome to...")
print(" ")
result = pyfiglet.figlet_format("Battleships", font="colossal")
print(result)
print("Choose an easy board or a hard board below.")
print("Good luck!")
print("-" * 79)

"""
Asks the user to select easy or hard board
"""


def board_difficulty():
    while True:
        try:
            difficulty = input("Select difficulty: 'Easy' or 'Hard': \n")
            if difficulty == "Easy":
                return 5, 5
            elif difficulty == "Hard":
                return 9, 9
            else:
                print("Invalid input. You must enter either 'Easy' or 'Hard'.")
        except ValueError:
            print("Invalid input. You must enter either 'Easy' or 'Hard'.")


rows, columns = board_difficulty()

"""
Creates the Battleships board.
Displays the board with the correct header and board alignment.
Places the ships on the board.
"""


def create_game_board(rows, columns):
    board = [['~' for _ in range(columns)] for _ in range(rows)]
    return board


def show_board(board, hide_ships=False):
    for row in board:
        display_row = []
        for cell in row:
            if hide_ships and cell == 'S':
                display_row.append('~')
            else:
                display_row.append(cell)
        print("  ".join(display_row))


def ship_location(board, num_ships):
    ships = []
    while len(ships) < num_ships:
        row = randint(0, len(board) - 1)
        col = randint(0, len(board[0]) - 1)
        if (row, col) not in ships:
            ships.append((row, col))
            board[row][col] = 'S'
    return ships


def choose_coordinate(board, row, col):
    if board[row][col] == 'S':
        board[row][col] = 'X'
        return "Direct hit!"
    elif board[row][col] == '.':
        board[row][col] = 'O'
        return "Miss!"
    else:
        return "You've already selected that coordinate."


player_board = create_game_board(rows, columns)
computer_board = create_game_board(rows, columns)

num_ships = 5

player_ships = ship_location(player_board, num_ships)
computer_ships = ship_location(computer_board, num_ships)

print("Your board:")
show_board(player_board)

print("Computer's board:")
show_board(computer_board, hide_ships=True)

"""
Allows the user to take a shot by selecting the coordinates.
"""
player_hits = 0
computer_hits = 0

while True:
    try:
        row = int(input(f"Select a row (1-{rows}): \n")) - 1
        col = int(input(f"Select a column (1-{columns}): \n")) - 1
        if 0 <= row < rows and 0 <= col < columns:
            result = choose_coordinate(computer_board, row, col)
            print(result)
            show_board(computer_board, hide_ships=True)

            if "Direct hit!" in result:
                player_hits += 1
                print(f"Player hits: {player_hits}")
                if player_hits == num_ships:
                    print(Fore.GREEN + "You sunk all the computer's ships.")
                    print(" ")
                    result = pyfiglet.figlet_format("You win", font="colossal")
                    print(result)
                    break

            comp_row = random.randint(0, rows - 1)
            comp_col = random.randint(0, columns - 1)
            comp_result = choose_coordinate(player_board, comp_row, comp_col)
            print(f"Computer's turn: {comp_result}")
            show_board(player_board)

            if "Direct hit!" in comp_result:
                computer_hits += 1
                print(f"Computer hits: {computer_hits}")
                if computer_hits == num_ships:
                    print(Fore.RED + "Computer sunk all your ships.")
                    print(" ")
                    result = pyfiglet.figlet_format("Loser!", font="colossal")
                    print(result)
                    break

        else:
            print(f"Please enter a row and column between 1 and {columns}.")
    except ValueError:
        print("Please enter a valid number.")
