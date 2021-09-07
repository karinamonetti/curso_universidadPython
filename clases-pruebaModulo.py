from clases import Localidad    # si quisiera importar todas las clases utilizo import *

danielLocalidad=Localidad("La Guaira", "Vargas", "Venezuela", 30000)
print(danielLocalidad.nombre)       

# para evitar que se ejecuten las líneas de código del otro archivo:

# print(__name__)