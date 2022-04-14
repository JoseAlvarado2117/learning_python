
"""
    Programming Challenges:

    create a program that contains a function called negativePositiveZero. It is passed
    one numeric (integer or float) parameter. The function should return one of the following
    strings values:

    'negative' if the number is negative
    'positive' if the number is positive
    'zero' if the number is zero
"""


def negativePositiveZero(number):

    if number > 0:
        return 'positive'
    elif number < 0:
        return 'negative'
    else:
        return 'zero'


userNumber = input('Enter a number: ')
userNumber = float(userNumber)

test1 = negativePositiveZero(userNumber)
print(f'{userNumber} is a number {test1}')

