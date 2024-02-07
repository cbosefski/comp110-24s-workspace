"""Number Guessing Game."""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False

while correct == False:
    guess: int = int(input("Guess a number:"))
    if guess == SECRET:
    #print("Correct!"+ str(guess) + "is the number!")original way
        print(f"Correct! {guess} is the number!")
        correct = True
    elif guess < SECRET:
        print(f"{guess} is too small. Guess again!")
    elif guess > SECRET:
        print(f"{guess} is too large. Guess again!")

        #we want to use a while loop so it doesnt exit if u get it wrong