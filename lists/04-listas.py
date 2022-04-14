"""
    Learning on List in python:
    A list is a collection of items in a particular order.
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

# Accessing Elements in a list
print(bicycles[0])      # return trek
print(bicycles[-1])     # return specialized
print(bicycles[::-1])   # return ['specialized', 'redline', 'cannondale', 'trek']


# **** Changing, Adding, and Removing Elements ****

# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements to the End of a List
motorcycles.append('honda')
print(motorcycles)

types_person = []

types_person.append('man')
types_person.append('women')
types_person.append('others')

print(types_person)

# inserting Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)


# Removing an item Using the del Statement
del motorcycles[0]
print(motorcycles)

# Removing an item using the pop() method
"""
    Este método remueve el último elemento de la lista.
"""

motorcycles = ['honda', 'yamaha', 'suzuki', 'dugati']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(popped_motorcycle)

frameworks = ['React', 'Angular', 'View', 'Svelte']
favorite_framework = frameworks.pop()
print('My favorite framework for work with javascript is ' + favorite_framework.title() + '.')

# Popping Items from any Position in a List
"""
    Se puede usar pop() para remover un elemento especifico de la lista
    incluyendo su indice en el método pop().
"""

lenguages = ['python', 'C++', 'Java', 'Rust', 'JavaScript', 'Ruby', 'Go']
favorite_lenguage = lenguages.pop(0)
print(f'My favorite language is {favorite_lenguage}')

# Removing an item by value
motorcycles = ['ducati', 'honda', 'suzuki', 'yamaha']
print(motorcycles)

motorcycles.remove('ducati')

print(motorcycles)

# **** Sorting a List permanently with the sort() method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Printing a List in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# Finding the length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars_length = len(cars)
print(cars_length)