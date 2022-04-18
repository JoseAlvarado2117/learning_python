"""
    Trabajando con Programación Orientada a Objetos en Python

    En esta clase aprenderemos a usar la herencia entre clases
"""


class Vehiculos(object):

    def __init__(self, marca, modelo, ruedas, color):
        self.color = color
        self.ruedas = ruedas
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("\nMarca:", self.marca, "\nModelo:", self.modelo, "\nLa moto es:", self.color,
              "\nTiene:", self.ruedas, "ruedas", "\nEn marcha:", self.enmarcha,
              "\nEstá acelerando:", self.acelera, "\nEstá frenando:", self.frena)


class Furgoneta(Vehiculos):

    def __init__(self, marca, modelo, ruedas, color):
        Vehiculos.__init__(self, marca, modelo, ruedas, color)
        self.cargando = None

    def carga(self, cargar):
        self.cargando = cargar

        if self.cargando:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class Moto(Vehiculos):

    def __init__(self, marca, modelo, ruedas, color):
        Vehiculos.__init__(self, marca, modelo, ruedas, color)
        self.hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("\nMarca:", self.marca, "\nModelo:", self.modelo, "\nLa moto es:", self.color,
              "\nTiene:", self.ruedas, "ruedas", "\nEn marcha:", self.enmarcha,
              "\nEstá acelerando:", self.acelera, "\nEstá frenando:", self.frena, "\n", self.hcaballito)


class VElectricos(Vehiculos):

    def __init__(self, marca, modelo, ruedas, color):
        super().__init__(marca, modelo, ruedas, color)
        self.cargando = False
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True
        print("Se esta cargando la energía")


class BicicletaElectrica(VElectricos, Vehiculos):
    def __init__(self, marca, modelo, ruedas, color):
        super().__init__(marca, modelo, ruedas, color)



print("\n**** Mi moto tiene las siguientes propiedades: ****")
miMoto = Moto("Ducati", "CBR", 2, "Negra")

miMoto.caballito()
miMoto.estado()

print("\n**** Mi Furgoneta tiene las siguientes propiedades: ****")
miFurgoneta = Furgoneta("Renault", "Kangoo", 4, "Roja")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))


print("\n**** Mi Bicicleta eléctrica tiene las siguientes propiedades: ****")

miBici = BicicletaElectrica("Orbea", "RX", 2, "Azul")
print(miBici)

miBici.estado()
miBici.cargarEnergia()