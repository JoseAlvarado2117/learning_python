"""
    # Working with string and python string methods
"""

nombre: str = 'Jose Alvarado'
edad: int = 18
promedio: float = 26.99

first_name = 'janetsys paola'
last_name = 'rodriguez astudillo'
print(first_name.title())
print(first_name.upper())
print(first_name.lower())

fullname = first_name + " " + last_name
print(fullname.title())

print(nombre)
print(edad)
print(promedio)


# **** Adding whitespace to String with Tabs or Newlines ****

print("\tProgramming in python")

print("Languages:\nPython\nC++\nJavaScript\nJava")

print("Languages: \n\tPython\n\tC++\n\tKotlin")


# **** Stripping Whitespace (Quitando espacios extras) ****

favorite_language = ' Python '
print(favorite_language)

# Quitando espacio por la derecha
print(favorite_language.rstrip())
favorite_language = favorite_language.rstrip()
print(favorite_language)

# Quitando espacio por la izquierda
favorite_language = favorite_language.lstrip()
print(favorite_language)

# Quitando espacios de ambos lados

favorite_framework = '  React  '
print(favorite_framework)

favorite_framework = favorite_framework.strip()
print(favorite_framework)

# **** Avoiding Type Errors with str() Function ****

age = 23
message = "Happy " + str(age) + "rd Birthday!"  # srt() convierte un número a un string
print(message)

new_message = "pi = " + str(3.14156) + " is my favorite number"
print(new_message)


# **** String methods ****

# slice
my_string = 'hello word'

print(my_string)

# obtener un elemento del string
print(my_string[0])
print(my_string[-1])

# obtener una fracción del string:  string[start:stop:change]
print(my_string[0:5:1])
print(my_string[5:])

print(my_string[::])

# new methods
name = "pam"
ultimas_letras = name[1:]

print('p' + ultimas_letras)

apellido = 'alvarado'
print(f'Apellido: {apellido[0].upper()}{apellido[1:]}')


# **** Interpolación de string ****

first_name = 'jose'
last_name = 'alvarado'
age = 33

print('Te llamas {0} {1} y tienes {2} años de edad'.format(first_name.title(), last_name.title(), age))

# otro método
results = 100/888

print("Los resultados son {r:1.5f}".format(r=results))

nombre = 'Paola'

print(f'El nombre es {nombre}')