class Persona:
    pass        # se utiliza para no agregar contenido.
print(type(Persona))


# class MiPersona:
#     def __init__(self):     #objeto inicializador
#       parámetro <--- self.nombre="Karina"    ---> atributo
#                      self.edad=26
#                      self.nacionalidad="ARG"
#                      self.estudios="Universitarios en curso"

# persona1= MiPersona()
# print(persona1.nombre)  #accedo al atributo


class Perro:
    def __init__(self, nombre, edad, raza, dueño, prueba, *args, **kwargs):     # *args cuando queremos pasar n atributos y **kwargs cuando queremos pasar un diccionario de valores.
        self.nombre=nombre      # self = this (JS)
        self.edad=edad
        self.raza=raza
        self.dueño=dueño
        self._prueba=prueba     #el _ indica que no se puede modificar fuera de la clase

    def mostrar_detalle(self):
        print(f"Perro: Nombre: {self.nombre} Edad: {self.edad} Raza: {self.raza} Dueño/a: {self.dueño} Prueba: {self._prueba}")


kimba=Perro("Kimba", 12, "Mestizo","Karina Monetti", "Prueba")
# print(kimba.nombre, kimba.edad, kimba.raza, kimba.dueño)
kimba.mostrar_detalle()

kimba.edad=11       #modificar los atributos
print(kimba.edad)
## -
sasha=Perro("Sasha", 8,"Mestizo", "Karina Monetti", "Prueba")
sasha.glotona=True      #le agrego otro atributo pero esta vez sería a la "sub-clase" sasha
sasha.mostrar_detalle() 
print(sasha.glotona) 

sasha._prueba="Otra cosa"   #aunque lo trate de cambiar no cambia.


# -- métodos GET (para obtener/recuperar atributos) y SET (para colocar/modificar atributos)

class Localidad:
    def __init__(self, nombre, provincia, pais, cantidadDeHabitantes):
        self._nombre=nombre
        self._provincia=provincia
        self._pais=pais
        self._cantidadDeHabitantes=cantidadDeHabitantes
    
    @property       #GET: con property puedo acceder al atributo sin necesidad de llamarlo con () -o sea, nos impide poder llamarlo como método-
    def nombre(self):       #esto se debería hacer con todos los métodos para evitar que sean modificados/llamados libremente
        return self._nombre
    
    @nombre.setter  #SET: esta línea me permitirá modificar el contenido.
    def nombre(self,nombre):
        self._nombre=nombre



# -- read Only
# Si quito la parte del setter no se podrá modificar el atributo (read Only)

#¿Cómo utilizar una clase desde otro archivo? --> ver. clases-pruebaModulo.py
# Para evitar que el código de este archivo se ejecute en el otro debo encapsular todo el código ejecutable en un if:
if __name__ == "__main__":
    miLocalidad=Localidad("Ramos Mejía", "Buenos Aires", "Argentina", 150000)
    print(miLocalidad.nombre)
    miLocalidad.nombre="Chacarita"
    print(miLocalidad.nombre)
    print(__name__)