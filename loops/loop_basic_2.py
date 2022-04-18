email = input("Enter your email: ")

counter = 0
counterArroba = -99
punto = False
arroba = False

for item in email:

    counter += 1
    if item == '@':
        arroba = True
        counterArroba = counter
        continue
    if counter > counterArroba and arroba is True and item == '.':
        punto = True
        break

else:
    arroba = False

if counterArroba != -99:
    print(arroba, counterArroba)
if punto:
    print("Email válido")
else:
    print("Email no válido")
