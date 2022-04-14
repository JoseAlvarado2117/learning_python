"""
    Working with IF, ELSE, AND ELIF STATEMENTS
"""

age = input('Enter your age: ')
age = int(age)


def verifyPerson(ageparam):
    if ageparam >= 18:
        return 'You entry is accepted'
    else:
        return "You entry isn't accepted"


entry = verifyPerson(age)

print(entry)


# Using IF/ELSE Inside a Function

def createHeader(fullname, gender):
    if gender == 'm':
        title = 'Mr.'
    elif gender == 'f':
        title = 'Ms.'
    else:
        title = 'Mr. or Ms.'

    header = 'Dear ' + title + ' ' + fullname + ','
    return header


print(createHeader('José Alvarado', 'm'))
print(createHeader('Paola Rodriguez', 'f'))
print(createHeader('Milagros Alvarado', 'f'))
print(createHeader('Carlos soler', 'fr'))
