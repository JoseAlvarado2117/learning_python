
"""
    programa que nos permite adivinar un número en 5 intentos
"""

import random

MAX_GUESSES = 5
MAX_RANGE = 20

print("**** Welcome to my Guess the number program ****")
print("Guess my number between 1 and", MAX_RANGE)
print("You will have", MAX_GUESSES, "guesses.")

number_secret = random.randrange(1, 100)
print(number_secret)

looping = 0
logout = False

while looping < MAX_GUESSES and not logout:

    # Ask the user to for a guess
    number_user = float(input("Take a guess: "))

    # increment guess counter
    looping = looping + 1

    if number_user == number_secret:
        print("\nYou got it!")
        print("It only took you", looping, "guess(es).")
        logout = True
    else:

        if number_user > number_secret:
            print("Your guess was too high!")
        else:
            print("Your guess was too low!")

    if looping == MAX_GUESSES:
        print("Sorry, you did not get it in", MAX_GUESSES, 'guesses.')
        print("The number was: ", number_secret)
        break

print("Thanks for playing.")