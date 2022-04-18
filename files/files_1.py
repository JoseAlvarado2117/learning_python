import os

# crear un directorio
# os.makedirs("files_makedirs")

# listar contenido de un directorio
print(os.listdir('./'))

# mostrar el directorio actual de trabajo
path_working = os.getcwd()
print(path_working)

# mostrar el tamaño del archivo en bytes
size_file = os.path.getsize("files_1.py")
print(size_file, "bytes")

# saber si un parámetro es un directorio
isdir = os.path.isdir("files_makedirs")
print(isdir)

# cambiar de directorio
os.chdir("files_makedirs")
file = open(os.getcwd() + "/" + 'file.txt', 'w')
file.write('trabajando con el modulo os' + os.linesep)
file.close()

print(os.listdir('./'))

# volvemos al directorio principal
os.chdir('../')
print(os.listdir('./'))

# creamos otro archivo para pruebas
direxiste = input("Nombre del directorio a crear: ")

if not os.path.isdir(direxiste):
    os.makedirs(direxiste)
    print(direxiste, "fue creado exitosamente")
os.chdir(direxiste)
archivo = open(os.getcwd() + "/" + "archivo.py", "w")
codigo = "Hola Mundo" + direxiste
archivo.write(codigo + os.linesep)
file.close()

print(os.listdir('./'))

archivo = input("Archivo a eliminar: ")
if os.path.isfile(archivo):
    os.remove(os.getcwd() + "/archivo.py")
    print(os.listdir('./'))
else:
    print("El archivo", archivo, "no existe en este directorio")


