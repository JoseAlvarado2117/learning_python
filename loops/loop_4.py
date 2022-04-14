"""
    programa que nos permite adivinar un número en
"""

import random

MAX_GUESSES = 5
MAX_RANGE = 20

print("**** Welcome to my Guess the number program ****")
print("Guess my number between 1 and", MAX_RANGE)
print("You will have", MAX_GUESSES, "guesses.")


def playOneRound():
    # Choose random target
    number_secret = random.randrange(1, 100)

    # Initialize a guess counter
    looping = 0

    # Initialize a logout play
    logout = False

    while looping < MAX_GUESSES and not logout:

        # Ask the user to for a guess
        number_user = input("Take a guess: ")

        try:
            number_user = int(number_user)
        except:
            print("Hey, that was NOT an integer!")
            continue  # transfer control back to the while

        # increment guess counter
        looping = looping + 1

        if number_user == number_secret:
            print("\nYou got it!")
            print("It only took you", looping, "guess(es).")
            logout = True
        else:

            if number_user > number_secret:
                print("\nYour guess was too high!")
            else:
                print("\Your guess was too low!")

        if not logout and looping == MAX_GUESSES:
            print("\nSorry, you did not get it in", MAX_GUESSES, 'guesses.')
            print("The number was: ", number_secret)
            break


# main code
while True:
    playOneRound()  # call a function to play one round of the game
    goAgain = input("\nPlay again? (Press ENTER to continue, or q to quit): ")

    if goAgain == 'q':
        break

print("\nThanks for playing.")
