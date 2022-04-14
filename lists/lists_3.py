"""
    Building a Simple Mad Libs Game

    MadLib (version 1)
"""

while True:
    name = input('Enter a name: ')
    verb = input('Enter a verb: ')
    adjective = input('Enter an adjective: ')
    noun = input('enter a noun: ')

    sentence = name + ' ' + verb + ' through the forest, hoping to escape the ' + adjective + ' ' + noun + '.'
    print('\n')
    print(sentence)
    print('\n')

    # See if the user wants to quit or continue
    answer = input("Type 'q' to quit, or anything else (even Return/Enter) to continue: ")
    if answer == 'q':
        break

    print('Bye')
