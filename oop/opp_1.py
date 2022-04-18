"""
    Working with opp in python
    Aprenderé:
     todo sobre clases, objetos, instancia de una clase, herencia, modulización, polimorfismo

    Vimos:
    Clases, Objetos, Métodos, Encapsulación

    los objetos tienen propiedades (atributos) y comportamientos
"""


class Coche:

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False
        self.__color = 'azul'

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if self.__enmarcha:
            chequeo = self.__chequeo_interno()

        if self.__enmarcha and chequeo:
            return "El coche está en marcha"
        elif self.__enmarcha and chequeo is False:
            return "Algo ha ido mal en el chequeo, no podemos arrancar."
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Es de color", self.__color, ". Tiene un ancho de",
              self.__anchoChasis, "y un largo de", self.__largoChasis)

    def frenar(self):
        self.__enmarcha = False
        return self.__enmarcha

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False


Bugati = Coche()  # => Instanciar una clase ó Ejemplarizar una clase

print("\n*************** Primera instancia de mi Coche: Bugatti ***************\n")
print(Bugati.arrancar(True))
Bugati.estado()

print("\n*************** Segunda instancia de mi Coche: Bugatti ***************\n")

Corrola = Coche()

print(Bugati.arrancar(False))
Corrola.ruedas = 2
Corrola.estado()
print("\n")
