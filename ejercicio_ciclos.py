# -- WHILE
contador= 6
while contador>1:
    contador-=1
    print(f"El valor del contador está en {contador}")
else:
    print("Ha terminado el ciclo While")


# -- FOR
cadena="Karina la Mandarina"
for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo for")


# -- BREAK
for letra in cadena:
    if letra.lower() == "k":
        print(f"Letra encontrada {letra}")
        print("Se ha encontrado la letra requerida y se ha terminado con el ciclo for.")
        break
    else:
        print("Fin del ciclo for")


# -- CONTINUE
for i in range(10):
    if i%2!=0:
        continue    # --> ejecuta lo que sigue (funciona al revés que break)
    else:
        print(f"El número par es {i}")