"""
    Working widt String and how manipulate it's
"""

string1 = 'Hello'
string2 = 'there'
greeting = string1 + ' ' + string2

print(greeting)

# len() Function Applied to String

state = 'Mississippi'
theLength = len(state)
print(theLength)

password = ' miclave'
password = password.strip()
passwordLength = len(password)

print(password, 'have', passwordLength, 'strings')

# Indexing Characters in a String:

j = 0
for index in state:
    if len(str(j)) == 1:
        print(j, '  => ', index)
    else:
        print(j, ' => ', index)
    j += 1

# Accessing Characters in a string
email = 'josealvarado2117@hotmail.com'

isEmail = []
dotEmail = False

for item in email:
    if item == '@':
        isEmail = isEmail.append(item)
        print('Tiene formato de email')

# Iterating Through Characters in a String
# This is the WRONG approach, just showing a concept!

state = 'Mississippi'
myIndex = 0

while myIndex < len(state):
    print(state[myIndex])
    myIndex += 1

print('**********************************')
myString = 'abcdefg'
for letter in myString:
    print(letter)

# Creating a Substring: A Slice
# <string>[<startIndex> : <upToButNotIncludingEndingIndex>]

myName = 'Jose Alvarado'

firstName = myName.split(' ')

print(firstName[0])
print(myName[0:4])

nChars = len(myName)
print(nChars)

lastName = myName[5:nChars]
print(lastName)

# Splitting String: the string are inmutable, you will often want to split them up into
# lists in order to manipulate their contents.

sent4 = "A much, much longer sentence"

sent4Split = sent4.rstrip('sentence').split()
print(sent4Split)

sent4_split = sent4.rsplit(' ', 2)
print(sent4_split)

# joining String, or Avoiding Concatenation

s0 = 'example'
s1 = 'text'
sep = ' '
sep = sep.join([s0, s1])
print(sep)

# string.join() is expecting a sequence of strings as an argument
sep = ' - '
sep = sep.join('potrzebie')
print(sep)

# convert other data types into strings and join up any sublists first,
# so that you present the outermost join() with a list of strings

sep = ' - '
a = 1
b = 2.37
sep1 = sep.join(('skidoo', sep.join([str(a), str(b)])))
print(sep1)

# other form
ab = sep.join([str(a), str(b)])
print(ab)
abc = sep.join(['skidoo', ab])
print(abc)

# Changing Case
s3 = "eXamPle tEXt"
s3 = s3.capitalize()
print(s3)

# other example
p1 = 'quantum exPrESo'
p1 = p1.title()
print(p1)

p1 = p1.upper()
print(p1)

p1 = p1.lower()
print(p1)

s5 = "it's thirteen o'clock"
s5 = s5.title()
print(s5)

s3 = s3.swapcase()
print(s3)

# Simple Methods of Formatting
x = s3.lower()

# To align text in the center, use string.center(width[, fillchar]).
print(x.center(37, '*'))

# To align text on the left, use string.ljust(width[, fillchar]).
print(x.ljust(37, '='))

# To align text on the right, use string.rjust(width[, fillchar]).
print(x.rjust(37, '+'))

# To align text on the right, fill a field with zeros, use string.zfill(width).
print(x.zfill(37))

# Finally, string.expandtabs([tabsize]) can ve used to expanded all the tab characters
# in a string using spaces. if tabsize is not given, a tab size of 8 characters will be used by default

s2 = "one\ttwo\tthree"
s2 = s2.expandtabs(16)
print(s2)

# Advanced Formatting: string.format(*args, **kwargs)

mystring: str = "value {0} equals {1}: {message}"
print(mystring.format('x', '23', message='[ok]'))


mystring = "value {0!s} equals {1!r}: {message!s}"
print(mystring.format('z', '37', message='[well, you know ...]'))