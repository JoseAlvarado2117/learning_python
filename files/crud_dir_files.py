"""
    Programa que nos permitirá crear, listar, eliminar y renombrar directorios
    y archivos
"""

from files.customs_os_functions import *

# Aqui definir el menu principal
def menu():
    print("\n******** Menu de opciones: ********\n")
    print("\Directorio actual: adir")
    print("\tCrear un directorio: cdir")
    print("\tCambiar al directorio: chdir")
    print("\tlistar un directorio: ldir")
    print("\tEliminar un directorio: rdir")
    print("\tRenombrar un directorio: updir")
    print("\tPara salir: q")


looping = True

while looping:
    menu()
    accion = input("Que desea realizar? ")

    if accion == 'q':
        looping = False
        print('\Saliendo de la aplicación ...')
        break

    if accion == 'cdir':
        dirname = input("Introduzca el nombre del directorio a crear: ")
        crearDirectorios(dirname)
        continue
    elif accion == 'adir':
        actualDirectorio()
        continue
    elif accion == 'chdir':
        dirname = input("Introduzca el nombre del directorio a acceder: ")
        accederDirectorio(dirname)
        continue
    elif accion == 'ldir':
        dirname = input("Introduzca el nombre del directorio a listar: ")
        leerDirectorio(dirname)
        continue
    elif accion == 'rdir':
        dirname = input("Introduzca el nombre del directorio a eliminar: ")
        eliminarDirectorio(dirname)
        continue
    elif accion == 'updir':
        dirname = input("Introduzca el nombre del directorio a renombrar: ")
        newdirname = input("Introduzca el nombre del directorio: ")
        renombrarDirectorio(dirname, newdirname)
        continue
    else:
        print("Operación no soportada")
