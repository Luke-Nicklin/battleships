import random

"""
Battleships welcome message
"""

print("Welcome to Battleships! Let's play...")

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

while True:
    try:
        columns = int(input("Enter the number of columns between 5 and 10: \n"))
        if 5 <= columns <= 10:
            break
        else:
            print("You must enter a number between 5 and 10.")
    except ValueError:
        print("Erro. You must enter a valid number.")
