"""
    Building Error-Checking Utility Functions
"""


def getIntegerFromUser(prompt):
    while True:
        number = input(prompt)
        try:
            number = int(number)
        except:
            print("That is not an integer, please try again.")
            continue

        # everything OK
        return number


def getFloatFromUser(prompt):
    while True:
        number = input(prompt)
        try:
            number = float(number)
        except:
            print("That is not a float, please try again.")
            continue

        # everything OK
        return number


def getTypeFromUser(type, prompt):
    while True:
        number = input(prompt)
        try:
            number = type(number)
        except:
            print("That is not (a/an)", type, "please try again.")
            continue

        # everything OK
        return number


my_integer = getIntegerFromUser('Please enter an integer: ')
print(my_integer)

my_float = getFloatFromUser('Please enter a float: ')
print(my_float)

my_type = getTypeFromUser(int, 'Please type an integer: ')
print(my_type)

my_type_float = getTypeFromUser(float, 'Please type a float: ')
print(my_type_float)
