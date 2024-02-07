"""EX02 - One shot Battleship exercise"""

__author__ = "730464517"
# Establish variables
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid_size = 4
secret_row = 3
secret_column = 2

# Prompt user for guesses
guess_row = int(input("Guess a row: "))
while guess_row < 0 or guess_row > grid_size:
    print(f"The grid is only {grid_size} by {grid_size}. Try again:")
    guess_row = int(input())

guess_column = int(input("Guess a column: "))
while guess_column < 0 or guess_column > grid_size:
    print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    guess_column = int(input())

# Check hit or miss
if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row:
    print("Close! Correct row, wrong column.")
elif guess_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")


# Print grid
row_counter = 1
while row_counter <= grid_size:
    row_str = ""
    column_counter = 1
    while column_counter <= grid_size:
        if guess_row == row_counter:
            if guess_column == secret_column and guess_column == column_counter:
                row_str += RED_BOX
            elif guess_column != secret_column and guess_column == column_counter:
                row_str += WHITE_BOX
            else:
                row_str += BLUE_BOX
        else:
            row_str += BLUE_BOX
        column_counter += 1
    print(row_str)
    row_counter += 1
