"""
    Working with user-defined functions
"""


# Building Our first Function

def getGroceries():
    print('milk')
    print('flour')
    print('sugar')
    print('butter')
    print()  # blank line


getGroceries()


def getGroceriesParams(item):
    print(item)


getGroceriesParams('item')
getGroceriesParams('eggs')
getGroceriesParams('apples')
getGroceriesParams('flour')


# Building a simple function that does addition

def addTwoIntegers(integer1, integer2):
    sum = integer1 + integer2
    return sum


sum1 = addTwoIntegers(5, 7)
sum2 = addTwoIntegers(3, 6)

print('sum = {}'.format(sum1))
print('sum = {}'.format(sum2))


# Building a function to calculate an average

def calculateAverage(param1, param2, param3, param4):
    """Add up numbers, divide by the number of numbers """
    total = param1 + param2 + param3 + param4
    average = total / 4.0
    print('Average value is: ', average)


calculateAverage(2, 3, 4, 5)
calculateAverage(-3, 5.2, 15, 1000.8)


# Returning an Value:

def square(number):
    answer = number * number
    return answer


userNumber = input('Enter a number: ')
userNumber = float(userNumber)

numberSquared = square(userNumber)

print('The square of your number is ', numberSquared)


# Returning More than One Value

def operationsMathematical(number1, number2):
    sum = number1 + number2
    rest = number1 - number2
    mult = number1 * number2
    divide = number1 / number2

    return sum, rest, mult, divide


number1 = input('What is the value of number1: ')
number1 = float(number1)

number2 = input('What is the value of number1: ')
number2 = float(number2)

sum, rest, mult, divide = operationsMathematical(number1, number2)

print(sum, rest, mult, divide)


# Temperature conversion Functions
""" 
    C = (F - 32)*(5/9)  => Fahrenheit to Centigrade
    F = (1.8xC) + 32    => Centigrade to Fahrenheit 
"""

def F2C(nDegreesF):
    nDegreesC = (nDegreesF - 32)*(5.0/9.0)
    return nDegreesC

def C2F(nDegreeC):
    nDegreeF = (1.8*nDegreeC) + 32.0
    return nDegreeF

usersTempF = input('Enter a value of degree Fahrenheit: ')
usersTempF = float(usersTempF)
convertedTempC = F2C(usersTempF)
print(usersTempF, 'degree Fahrenheit is: ', convertedTempC, 'degree Centigrade')

usersTempC = input('Enter a value of degree Centigrade: ')
usersTempC = float(usersTempC)
convertedTempF = C2F(usersTempC)
print(usersTempC, 'degree Centigrade is: ', convertedTempF, 'degree Fahrenheit')