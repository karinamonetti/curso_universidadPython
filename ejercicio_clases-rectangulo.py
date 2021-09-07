class Area:
    def __init__(self,altura,base):
        self.altura=altura
        self.base=base

    def calcularArea(self):
        return self.base*self.altura
    
def tuArea():
    print("Esta función te devolverá el área de un rectángulo.")
    baseFunct=int(input("Proporciona en centímetros la base: "))
    alturaFunct=int(input("Proporciona en centímetros la altura: "))
    rectangulo=Area(baseFunct,alturaFunct)
    print(f"El área del rectángulo es de {rectangulo.calcularArea()}")
tuArea()