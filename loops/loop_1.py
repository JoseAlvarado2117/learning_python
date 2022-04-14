
"""
    Working with loops in python
"""


looping = True
while looping:
    answer = input("Please type the letter 'a': ")
    if answer == 'a':
        looping = False
    else:
        print("Come on, type an 'a'!")

print("Thanks for typing an 'a'")