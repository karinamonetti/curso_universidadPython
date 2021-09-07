## calculadora de precio con impuesto
def calcular_total():
    print("Esta función te devolverá el valor a pagar final de un producto/servicio al ingresar su precio y el valor del impuesto.")
    pago_sin_impuesto=float(input("Dime el precio: "))
    impuesto=float(input("Dime el valor del impuesto: "))
    impuesto=impuesto*0.01
    resultado=pago_sin_impuesto+(pago_sin_impuesto*impuesto)
    return print(f"El precio a pagar es de {resultado}")
calcular_total()


