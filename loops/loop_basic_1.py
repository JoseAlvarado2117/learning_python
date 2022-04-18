
for letter in 'Python':

    if letter == 'h':
        continue

    print("seeing the letter", letter)

name = "pildoras Informaticas"
counter = 0

for letter in name:

    if letter == ' ':
        continue

    counter += 1

print(counter)


print("******** Program for find the number the students that failed ********")
notas = []

print("\nTo stop entering notes type '-1'")
while True:
    nota = input("Enter the note of the student: ")
    nota = float(nota)

    if nota == -1:
        break
    elif nota > 10 or nota < 0:
        print('The note range is between 0 and 10 points')
        continue

    notas.append(nota)


print(notas)

aprobados = 0
reprobados = 0

for item in notas:

    if item < 5:
        reprobados += 1
    else:
        aprobados += 1

print("Students passed: ", aprobados)
print("Students failed: ", reprobados)
print("Total number of Students: ", len(notas))