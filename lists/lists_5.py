"""
    List Manipulation
"""

frameworks = ['Flask', 'Django', 'Express', 'Nestjs', 'Ruby', 'Sprint Boot', '.net']

# Add an element to the end of a list
frameworks.append('Laravel')
print(frameworks)

# Returns the number of times <thing> was found in the <list>
countElement = frameworks.count('Flask')
print('Flask was found: ', countElement, 'of times')

# Appends all elements in <otherList> to <list>
frameworks_copy = []

frameworks_copy.extend(frameworks)
print(frameworks_copy)

# Returns the first index in the <list> where <thing> is found
favoriteIndex = frameworks.index('Flask')
print('My favorite framework is: ', frameworks[favoriteIndex])

# Inserts <thing> into the <list> at position <index>
laravel = frameworks.index('Laravel')
frameworks.insert(laravel, 'Symphony')
frameworks.insert(-1, 'Fast API')
print(frameworks)

# Remove and return the last element from a <list>
favoriteFramework = frameworks.pop(1)
print(favoriteFramework)
print(frameworks)

# Find first occurrence of <thing> in a <list> and remove it
frameworks.remove('Symphony')
print(frameworks)

# Reverse the position of all the elements in a <list>
frameworks.reverse()
print(frameworks)

frameworks.reverse()

# Sort elements in a <list> from low to high
print('\n', frameworks)
frameworks.sort()
print(frameworks)