"""
    A list is an ordered collection of that is referred to by a single variable name.
    (In most other computer languages, the same concept is called an array)

    [<element>, <element>, ..., <element>]
"""

# Position of an element in a list: index

shopping_list = ['apples', 'bananas', 'cherries', 'dates', 'eggplant']

# printed
print(shopping_list)
i = -1
for item in shopping_list:
    i = i + 1
    print(i, " => ", item)


def search(index, mylist):
    while True:
        if str(index) == 'q':
            print("Bye")
            break

        if index > len(mylist):
            print("The index must be low a the length of the list")
        else:
            index = int(index)
            myelement = mylist[index]
            print("The element at index", index, "is", myelement)
            break


while True:
    myindex = int(input("Enter a number to use as an index: "))
    search(myindex, shopping_list)

    goAgain = input("\nPlay again? (Press ENTER to continue, or q to quit): ")
    if goAgain == 'q':
        break

print("Logout! Bye")
