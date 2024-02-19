"""EX03 - Functiona Battleship exercise."""

__author__ = "730464517"

import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

def input_guess(grid_size: int, guess_type: str) -> int:
    assert guess_type == "row" or guess_type == "column"
    
    while True:
        guess = input(f"Guess a {guess_type}: ")
        if type(guess)==int:
            guess = int(guess)
            if 1 <= guess <= grid_size:
                return guess
            else:
                print(f"The number must be between 1 and {grid_size}. Try again.")

def print_grid(grid_size: int, row_guess: int, col_guess: int, is_correct: bool) -> None:
    row_counter = 0
    while row_counter < grid_size:
        row_str = ""
        column_counter = 0
        while column_counter < grid_size:
            if row_guess - 1 == row_counter and col_guess - 1 == column_counter:  # Adjust indices by subtracting 1
                if is_correct:
                    row_str += RED_BOX
                else:
                    row_str += WHITE_BOX
            else:
                row_str += BLUE_BOX
            column_counter += 1
        print(row_str)
        row_counter += 1

def correct_guess(secret_row: int, secret_col: int, guess_row: int, guess_col: int) -> bool:
    return secret_row == guess_row and secret_col == guess_col

def main(grid_size: int, secret_row: int, secret_col: int) -> None:
    max_turns = 5
    turn = 0
    while turn < max_turns:
        turn += 1
        print(f"=== Turn {turn}/{max_turns} ===")

        guess_row = input_guess(grid_size, "row")
        guess_col = input_guess(grid_size, "column")

        is_correct = correct_guess(secret_row, secret_col, guess_row, guess_col)

        print_grid(grid_size, guess_row, guess_col, is_correct)  # Pass the guesses correctly

        if is_correct:
            print(f"Hit! You won in {turn}/{max_turns} turns!")
            return

        print("Miss!")

    print(f"X/{max_turns} - Better luck next time!")

if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
