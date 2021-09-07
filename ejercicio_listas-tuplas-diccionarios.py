# -- LISTAS
lista_de_cosas=["Karina", "Daniel", "Kimba", "Sasha", "Manuelita",12,8,12,1995, True]
print(lista_de_cosas)
print(lista_de_cosas[2])
print(lista_de_cosas[-1])
print(lista_de_cosas[:2])

lista_de_cosas[9]=False     # cambia el valor de una posición
print(lista_de_cosas)  

for cosas in lista_de_cosas:    # imprime los elementos
    print(cosas)

print(len(lista_de_cosas))      # imprime la cantidad de elementos de la lista


lista_de_cosas.append("Yolanda")     # agrega un elemento al final de la lista
lista_de_cosas.insert(0,"El primero")    # agrega un elemento en la posición indicada
print(lista_de_cosas)

lista_de_cosas.remove(False)     # remueve el elemento
lista_de_cosas.pop()        # remueve el último elemento
del lista_de_cosas [0]      # elimina el elemento perteneciente al índice indicado.
print(lista_de_cosas)

lista_de_cosas.clear()      # elimina todos los elementos de la lista.
print(lista_de_cosas)

# del lista_de_cosas # elimina por completo de la memoria la lista.
# print(lista_de_cosas)


  
# -- TUPLA  --> No se pueden modificar los elementos de la lista.
frutas=("Frutilla", "Anana", "Banana", "Naranja", "Sandia")
print(frutas)
print(len(frutas))
print(frutas[0])
print(frutas[-1])
print(frutas[:3])
for fruta in frutas:
    print(fruta, end=" - ") # se imprimirá en una línea finalizando cada elemento con lo proporcionado en end.

frutasLista=list(frutas)       # tansformo una tupla a una lista para cambiarle los elementos
print(frutasLista)              # no es una buena práctica
frutasLista[0]="Kiwi"
print(frutasLista)
frutasListas=tuple(frutasLista)
print(frutasListas)

# del frutasLista
# print(frutasLista)

ejercicioTupla=(13, 1, 8, 3, 2, 5, 8)
ejercicio_tupla_en_lista=[]
for i in ejercicioTupla:
    if i < 5:
        ejercicio_tupla_en_lista.append(i)
print(ejercicio_tupla_en_lista)




# -- SET    --> no guarda un orden, no permite elementos duplicados
planetas={"Marte", "Venus", "Júpiter"}  
print(planetas)
print("Marte" in planetas)  # comprueba si un elemento se encuentra en el set
planetas.add("Saturno")     # se agrega un nuevo elemento
print(planetas)
# planetas.remove("Marte")
planetas.discard("Marte")   # elimina sin arrojar un error en caso de que no se encuentre
print(planetas)


# -- DICCIONARIOS       --> key:value
diccionario={
    "Fútbol":"Cancha",
    "Amigos":"Si",
    "Bar dentro":"Si"
}
print(diccionario)
print(len(diccionario))
print(diccionario["Fútbol"])    # proporcionar la key para acceder al value
diccionario["Fútbol"]="Sala"
print(diccionario)

for i in diccionario.items():   # permite recorrer los elementos de un diccionario
    print(i)

for i in diccionario.keys():   # permite recorrer las keys de un diccionario
    print(i)

for i in diccionario.values():   # permite recorrer los values de un diccionario
    print(i)

print("Fútbol" in diccionario)
diccionario["Localidad"]="San Justo"
print(diccionario)
diccionario.pop("Bar dentro")
print(diccionario)