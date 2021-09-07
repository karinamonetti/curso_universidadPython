class Aritmetica:
    """
        Esta clase realiza las operaciones de suma, resta, multiplicación y división
    """
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def suma(self):
        return self.num1+self.num2
    
    def resta(self):
        return self.num1-self.num2

    def multipli(self):
        return self.num1*self.num2

    def divi(self):
        return self.num1/self.num2

valoresProporcionados=Aritmetica(10,4)
print(f"El valor de la suma es de: {valoresProporcionados.suma()}, de la resta: {valoresProporcionados.resta()}, de la multiplicación: {valoresProporcionados.multipli()} y de la división: {valoresProporcionados.divi()}")




