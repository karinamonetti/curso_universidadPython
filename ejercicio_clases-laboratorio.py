class Cubo:
    def __init__ (self,ancho,profundidad,alto):
        self.ancho=ancho
        self.alto=alto
        self.profundidad=profundidad
    
    def volumen(self):
        return self.ancho*self.alto*self.profundidad

def tuVolumen():
    print("Esta función te devolverá el volúmen de un cubo.")
    ancho=int(input("Proporciona en centímetros el ancho: "))
    alto=int(input("Proporciona en centímetros el alto: "))
    profundidad=int(input("Proporciona en centímetros la profundidad: "))
    tuCubo=Cubo(ancho, alto,profundidad)
    print(f"El volúmen del cubo es de {tuCubo.volumen()}")
tuVolumen()