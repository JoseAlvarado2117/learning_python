"""
    Aprendiendo polimorfismo en python
"""


class Coche:
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")


class Moto:
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")


class Camion:
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo1 = Moto()
desplazamientoVehiculo(miVehiculo1)

miVehiculo2 = Camion()
desplazamientoVehiculo(miVehiculo2)