"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = 730464517
# Part 1: Player 1 picks a secret boat location
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
secret_boat_location = int(input("Pick a secret boat location between 1 and 4: "))

# Check if location is within valid range
if secret_boat_location < 1:
    print(f"Error! {secret_boat_location} too low!") + exit()
else:
    if secret_boat_location > 4:
        print(f"Error! {secret_boat_location} too high!") + exit()

# part 2: Player 2 is prompted to guess boat location
guess = int(input("Guess a number between 1 and 4: "))

if guess < 1:
    print(f"Error! {guess} too low!")
else:
    if guess > 4:
        print(f"Error! {guess} too high!")
    else:
        result = RED_BOX if guess == secret_boat_location else WHITE_BOX
        emoji_boxes = ""
        if guess == 1:
            emoji_boxes += result
        else:
            emoji_boxes += BLUE_BOX
        
        if guess == 2:
            emoji_boxes += result
        else:
            emoji_boxes += BLUE_BOX
        
        if guess == 3:
            emoji_boxes += result
        else:
            emoji_boxes += BLUE_BOX
        
        if guess == 4:
            emoji_boxes += result
        else:
            emoji_boxes += BLUE_BOX
        print(emoji_boxes)
        # Part 3: Check if guess is correct
        if guess == secret_boat_location:
            print("Correct! You hit the ship")
        else:
            print("Incorrect! You missed the ship.")