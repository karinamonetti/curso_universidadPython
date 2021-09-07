def miFuncion(a,b):
    return (a+b)
miResultado=miFuncion(2,5)
print(miResultado)


def sumar(a=0, b=0):        # valores por default
    return a+b
resultadoSuma=sumar(10,5)
print(resultadoSuma)
print(sumar())


def listarNombres(*nombres):  # cuando no sé la cantidad de parámetros que recibirá la función le pongo un * (funciona como el ... de JS)
    for i in nombres:
        print(i)
listarNombres("Carla", "Juan", "Franco")
listarNombres("Laura", "Carlos")

# ejercicio argumentos variables
def multiNumeros(*numeros):
    resultado=1
    for i in numeros:   # i vendría siendo el número que la función recibe como parámetro
        resultado*=i
    return resultado

print(multiNumeros(2,3,2))




def diccionarioVariable(**elementos):   # **diccionario variable
    for key, value in elementos.items():    # items() recorre elementos del diccionario
        print(f"Key: {key}, Value: {value}")
diccionarioVariable(Nombre="Kimba", Edad=12, Raza="Mestizo", Feliz=True)




def losNombres(nombres):
    for i in nombres:
        print(i)
nombres=["Juan", "Juancito", "Jorgito"]
losNombres(nombres)
losNombres("Carlos")



def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
resultado=factorial(5)
print(f"El factorial de 5 es {resultado}")



def imprimirDescendente(num):
    if num >0:
        print(num)
        imprimirDescendente(num-1)  # se vuelve a llamar la función y se le resta 1 al parámetro
imprimirDescendente(15)




