"""
    Programming Challenges:

    Create a program that contains a function called isEven. The function is passed one numeric (integer)
    parameter. isEven should return as follows:

    True    => if the number is even (..., -6, -4, -2, 0, 2, 4, 6, ...)
    False   => if the number is odd (...,-5, -3, -1, 1, 3, 5, ...)
"""


def isEven(number):
    remainder = number % 2
    if remainder == 0:
        return True
    else:
        return False


def printEvenOrOdd(some_value):
    if isEven(some_value):
        print(some_value, 'is even')
    else:
        print(some_value, 'is odd')


def getNumber():
    usernumber = input('Enter a number: ')
    usernumber = int(usernumber)
    return usernumber


try:
    userNumber = getNumber()
except:
    print('the number must be an integer')
    userNumber = getNumber()

printEvenOrOdd(userNumber)
