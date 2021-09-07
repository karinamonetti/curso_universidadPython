"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos
Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )

Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )

Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
"""

class Vehiculo:
    def __init__(self,color,ruedas):
        self.__color=color
        self.__ruedas=ruedas

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color=color
    
    @property
    def ruedas(self):
        return self.__ruedas
    
    @ruedas.setter
    def ruedas(self, ruedas):
        self.__ruedas=ruedas
    
    def __str__(self):
        return f"Vehiculo [Color: {self.__color}, Ruedas: {self.__ruedas}]"

miVehiculo=Vehiculo("Rojo", "Rueditas lindas")
print(miVehiculo)


class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)
        self.__velocidad=velocidad
    
    @property
    def velocidad(self):
        return self.__velocidad
    
    @velocidad.setter
    def velocidad(self,velocidad):
        self.__velocidad=velocidad

    def __str__(self):
        return f"{super().__str__()} Coche [Velocidad: {self.__velocidad}]"

miCoche=Coche("Negro", "Ford", "50 km/h")
print(miCoche)


class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas, tipo):
        super().__init__(color,ruedas)
        self.__tipo=tipo

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo=tipo
    
    def __str__(self):
        return f"{super().__str__()} Bicicleta [Tipo: {self.__tipo}]"

miBici=Bicicleta("Azul oscuro", "Comunes", "De montaña")
print(miBici)



    
