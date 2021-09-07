class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
        
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,edad):
        self.__edad=edad

    def __str__(self):
        return f"Persona[Nombre: {self.__nombre}, Edad:{self.__edad}]"

if __name__=="__main__":
    persona1=Persona(nombre="Lucas", edad=15)
    print(persona1.nombre)
    print(__name__)


class Empleado(Persona):        #lo que está entre paréntesis es de donde se hereda
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre,edad)
        self.__sueldo=sueldo

    #--sueldo (get y set)
    @property
    def sueldo(self):
        return self.__sueldo
    @sueldo.setter
    def sueldo(self,sueldo):
        self.__sueldo=sueldo

    def __str__(self):
        return f"{super().__str__()} Empleado: [Sueldo: {self.__sueldo}]"  # sobre escribo el método en la clase hija


empleado1=Empleado("Juan", 28, 5000)
if __name__=="__main__":
    print(type(empleado1))
    print(empleado1.sueldo)
    print(__name__)
