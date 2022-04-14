"""
    Program that add numbers and calculate the average. the numbers on type
    for the user
"""

numbers = []

looping = False
while not looping:
    number = float(input("Enter a number: "))

    if number == -1:
        looping = True
    else:
        numbers.append(number)

print(numbers)

for number in numbers:
    print(number)