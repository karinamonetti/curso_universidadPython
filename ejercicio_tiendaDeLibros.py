def tienda_de_libros():
    print("Ingresa los siguientes datos del libro:")
    titulo=input("Proporciona el nombre del libro: ")
    identificacion=int(input("Proporciona el ID del libro: "))
    precio=float(input("Proporciona el precio del libro: "))
    envio=input("Indica si el envío del libro es gratuito (True/False): ")
    if envio.lower() == "true":
            envio=True
    elif envio.lower() == "false":
            envio=False
    else:
            print("No has ingresado True o False en la casilla del envío del libro.")
            return
    if titulo and identificacion and precio and (envio == True or envio == False):
        print(f"""Los datos del libro son:
        Título del libro: {titulo}
        Número de ID: {identificacion}
        Precio: ${precio}
        Envío gratuito: {envio}
        """)
        
tienda_de_libros()
