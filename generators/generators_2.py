"""
    Generators with yield from
"""


def return_cities(*citiesinner):
    for item in citiesinner:
        # for iteminner in item:
        # yield iteminner
        yield from item


cities = return_cities("Madrid", "Belgrado", "Caracas", "California", "Paris", "Sevilla", "Cumana")
print(cities)

print(next(cities))
print(next(cities))
