"""
    Trabajando con herencia multiple
"""


class Person:
    def __init__(self, name, age, direction):
        self.direction = direction
        self.age = age
        self.name = name

    def description(self):
        print(f'\nName: {self.name} \nAge: {self.age} years ald \nDirection: {self.direction}')


class Employee(Person):
    def __init__(self, salary, seniority, name_employee, age_employee, direction_employee):
        super().__init__(name_employee, age_employee, direction_employee)
        self.salary = salary
        self.seniority = seniority

    def description(self):
        super().description()
        print(f'Salary: {self.salary} $ \nSeniority: {self.seniority} years')


person1 = Person('Jose Alvarado', 33, 'Calle Vargas')
person1.description()

employee1 = Employee(1560, 15, 'Paola Rodriguez', 31, 'Venezuela')
employee1.description()

print(isinstance(employee1, Employee))
print(isinstance(employee1, Person))
print(isinstance(person1, Employee))