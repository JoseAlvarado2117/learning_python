"""
    Working with generators: Entre llamadas y llamadas el generador entra en un estado
    de suspensión.
"""


def generaPares(limit):
    num = 1
    mylist = []

    while num < limit:
        mylist.append(num * 2)
        num += 1

    return mylist


pares = generaPares(10)

print(pares)

# using generators

def generatorEven(limit):
    num = 1

    while num < limit:
        yield num*2
        num += 1


evens = generatorEven(10)

print(next(evens))

print("TypeError: 'function' object is not an iterator")
print("TypeError: 'function' object is not an iterator")

print(next(evens))

print("TypeError: 'function' object is not an iterator")
print("TypeError: 'function' object is not an iterator")
print("TypeError: 'function' object is not an iterator")

print(next(evens))
