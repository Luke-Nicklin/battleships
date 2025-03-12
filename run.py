import random
from random import randint

# import pyfiglet module
import pyfiglet

# import colorma module
from colorama import init, Fore, Style

# Initialize Colorama
init()


def welcome_message():
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


def board_difficulty():
    """
    Asks the user to select easy or hard board.
    """
    while True:
        try:
            diff = input("Select difficulty: 'easy' or 'hard': \n").lower()
            if diff == "easy":
                return 5, 5
            elif diff == "hard":
                return 9, 9
            else:
                print("Invalid input. You must enter either 'easy' or 'hard'.")
        except ValueError:
            print("Invalid input. You must enter either 'easy' or 'hard'.")


def create_game_board(rowsin, columnsin):
    """
    Creates the battleships board.
    """
    board = [['~' for _ in range(columnsin)] for _ in range(rowsin)]
    return board


def show_board(board, hide_ships=False):
    """
    Displays the easy or hard board based off of the user's input.
    Hides the ships on the computer's board.
    """
    for row in board:
        display_row = []
        for cell in row:
            if hide_ships and cell == 'S':
                display_row.append('~')
            else:
                display_row.append(cell)
        print("  ".join(display_row))


def ship_location(board, num_ships):
    """
    Randomly places the ships on the board.
    """
    ships = []
    while len(ships) < num_ships:
        row = randint(0, len(board) - 1)
        col = randint(0, len(board[0]) - 1)
        if (row, col) not in ships:
            ships.append((row, col))
            board[row][col] = 'S'
    return ships


def choose_coordinate(board, row, col):
    """
    Allows the user to select a coordinate to take their shot.
    """
    if board[row][col] == 'S':
        board[row][col] = 'X'
        return Fore.GREEN + "Direct hit!" + Style.RESET_ALL
    elif board[row][col] == '~':
        board[row][col] = 'O'
        return Fore.RED + "Miss!" + Style.RESET_ALL
    else:
        return Fore.CYAN + "Coordinate already selected." + Style.RESET_ALL


def main():
    """
    Welcome message.
    Asks the user to select easy or hard difficulty.
    Creates the Battleships board.
    Displays the easy or hard board based off of the user's input.
    Places the ships on the board.
    """
    welcome_message()
    rows, columns = board_difficulty()
    player_board = create_game_board(rows, columns)
    computer_board = create_game_board(rows, columns)

    num_ships = 5

    ship_location(computer_board, num_ships)
    ship_location(player_board, num_ships)

    print("Your board:")
    show_board(player_board)

    print("Computer's board:")
    show_board(computer_board, hide_ships=True)

    play_game(player_board, computer_board, rows, columns, num_ships)


def play_game(player_board, computer_board, rows, columns, num_ships):
    """
    Allows the player to enter a row and a column to take a shot.
    Computer selects a random coordinate for its shot.
    Shows number of player hits and number of computer hits.
    Shows win or lose message based on outcome of the game.
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
                        print(Fore.GREEN + "You sunk all my battleships.")
                        print(" ")
                        result = pyfiglet.figlet_format("You \
win!", font="colossal")
                        print(result)
                        break

                comp_row = random.randint(0, rows - 1)
                comp_col = random.randint(0, columns - 1)
                comp_result = choose_coordinate(player_board, comp_row,
                                                comp_col)
                print(f"Computer's turn: {comp_result}")
                show_board(player_board)

                if "Direct hit!" in comp_result:
                    computer_hits += 1
                    print(f"Computer hits: {computer_hits}")
                    if computer_hits == num_ships:
                        print(Fore.RED + "Computer sunk all your ships.")
                        print(" ")
                        result = pyfiglet.figlet_format("Loser! \
", font="colossal")
                        print(result)
                        break

            else:
                print(f"Please enter a row and column between 1 and {columns}")
        except ValueError:
            print("Please enter a valid number.")


main()
