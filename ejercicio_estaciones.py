mes=int(input("Ingresa el mes del año (1-12): "))
estacion=None
if mes== 12 or mes== 1 or mes==2:
    estacion="La estación del año en que nos encontramos es verano"
    print(estacion)
elif mes==3 or mes==4 or mes==5:
    estacion="La estación del año en que nos encontramos es otoño"
    print(estacion)
elif mes==6 or mes== 7 or mes==8:
    estacion="La estación del año en que nos encontramos es invierno"
    print(estacion)
elif mes==9 or mes==10 or mes==11:
    estacion="La estación del año en que nos encontramos es primavera"
    print(estacion)
else:
    print("Mes incorrecto")
    
    