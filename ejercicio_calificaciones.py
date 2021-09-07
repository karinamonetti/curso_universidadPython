def tuCalificacion():
    calificacion=int(input("Ingresa una calificación entre 0 y 10: "))
    nota=None
    if calificacion>=0 and calificacion <6:
        nota="F"
        print(f"Tu calificación es de {nota}")
    elif calificacion >=6 and calificacion <7:
        nota="D"
        print(f"Tu calificación es de {nota}")
    elif calificacion >=7 and calificacion <8:
        nota="C"
        print(f"Tu calificación es de {nota}")
    elif calificacion >=8 and calificacion <9:
        nota="B"
        print(f"Tu calificación es de {nota}")
    elif calificacion ==9 or calificacion== 10:
        nota="A"
        print(f"Tu calificación es de {nota}")
    else:
        print("Valor desconocido")
tuCalificacion()