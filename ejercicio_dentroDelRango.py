# -- AND
tuNumero= int(input("Escribe un valor numérico: "))
if tuNumero >=0 and tuNumero<=5:
    print(f"El número proporcionado ({tuNumero}) se encuentra entre los números 0 y 5.")
else:
    print(f"El número proporcionado ({tuNumero}) es menor a 0 o mayor a 5.")


# -- OR
vacaciones=False
descanso=False
if vacaciones or descanso:
    print("Puede asistir al juego de su hijo")
else:
    print("No puede asistir al juego de su hijo")


# -- NOT
vacaciones=False
descanso=False
if not (vacaciones or descanso):
    print("Puede asistir al juego de su hijo")
else:
    print("No puede asistir al juego de su hijo")


# -- Combinación de operadores
edad=int(input("Introduce tu edad: "))
if (edad >= 20 and edad <30) or (edad >= 30 and edad <40):
    print("Tu edad se encuentra dentro del rango entre los 20 y 30 años.")
elif edad < 20:
    print("Aún no entras en el rango entre los 20 y 30 años.")
else:
    print("No estás dentro del rango de edades a considerar.")


# -- Número mayor
numero1=int(input("Introduce el primer número: "))
numero2=int(input("Introduce el segundo número: "))
if numero1>numero2:
    print(f"El número mayor es {numero1}")
elif numero1<numero2:
    print(f"El número mayor es {numero2}")
else:
    print("Los números ingresados son iguales")