## conversión de grados celsius a fahrenheit y viceversa
def grados():
    grado=input("Esta es una función para convertir los grados Fahrenheit a Celcius y viceversa. ¡IMPORTANTE! Ingresa C para convertir Fahrenheit a Celsius o F para convertir Celsius a Fahrenheit: ")
    grado=grado.lower()
    if grado == "c" or grado == "f":
        if grado == "c":
            print("TO CELSIUS: Convertiremos una temperatura Fahrenheit a Celsius.")
            toCelsius=int(input("Ok. Dime la temperatura que quieras convertir (solo el número): "))
            toCelsiusCalculator=(toCelsius-32)*(5/9)
            print(f"La temperatura en Celsius es de {toCelsiusCalculator}")
        elif grado == "f":
            print("TO FAHRENHEIT: Convertiremos una temperatura Celsius a Fahrenheit.")
            toFahreheit=int(input("Ok. Dime la temperatura que quieras convertir (solo el número): "))
            toFahrenheitCalculator= toFahreheit*(9/5) + 32 
            print(f"La temperatura en Fahrenheit es de {toFahrenheitCalculator}")     
    else:
        print("Esta función solo acepta C para Celsius o F para Fahrenheit")
grados()    