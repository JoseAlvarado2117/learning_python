"""
    Programming Challenges:

    Create a program that contains a function called isSquare. The function is passed two parameters that
    represent the length and the width of a shape. Assume that we are talking about a rectangle. The
    function isSquare should return one of the following:

    True    => if the sides represent a square
    False   => if the sides do not represent a square
"""


def isSquare(lengthinside, widthinside):
    if lengthinside == widthinside:
        its_a_square = True
    else:
        its_a_square = False
    return its_a_square


length = input('Enter a Length: ')
length = float(length)

width = input('Enter a Width: ')
width = float(width)

# Test cases
result = isSquare(length, width)

if result:
    print(length, 'and', width, 'represent a square')
else:
    print(length, 'and', width, 'do not represent a square')
