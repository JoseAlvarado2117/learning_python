"""
    Custom functions for working with os system

    crearDirectorios
    accederDirectorio
    leerDirectorio
    eliminarDirectorio
    renombrarDirectorio
"""


import os

def crearDirectorios(name):
    if not os.path.isdir(name):
        os.makedirs(name)
        print("El directorio", name, "fue creado exitosamente.")

def accederDirectorio(name):
    print('Ha cambiado en path a', name)
    path = os.getcwd() + "/" + name
    if os.path.isdir(path):
        os.chdir(path)
        print("Directorio actual: ", path)
    else:
        print("El directorio no existe.")

def leerDirectorio(name):
    path = os.getcwd() + "/" + name
    accederDirectorio(name)
    print("Se ejecuto")
    if os.path.isdir(path):
        contentDir = os.listdir(path)
        print(contentDir)
    else:
        print("El directorio no existe.")

def actualDirectorio():
    print(os.getcwd())

def eliminarDirectorio(name):
    if os.path.isdir(name):
        os.rmdir(name)
        print("Directorio:", name, "eliminado exitosamente.")

def renombrarDirectorio(name, newname):
    os.rename(name, newname)
    print("Renombrando el directorio:", name, "a", newname)