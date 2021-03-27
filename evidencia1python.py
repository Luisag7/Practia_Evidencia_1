clave = 0
desglose = []
while True :
    print()
    print ("Menú De Opciones")
    print ()
    print ("[1] Registrar una venta")
    print ("[2] Consultar una venta")
    print ("[3] Salir")
    opcion = int(input("Qué opción deseas realizar?: "))
    if opcion == 1:
        suma_venta = 0
        while True:
            print("")
            registro = []
            desc_articulo = input("\nDescripción del articulo: ")
            cant_pzas = int(input("Dame la cantidad de piezas: "))
            precio_venta = float(input("Dame el precio de venta: "))
            subtotal = cant_pzas * precio_venta
            registro.append(desc_articulo)
            registro.append(cant_pzas)
            registro.append(subtotal)
            desglose.append(registro)
            suma_venta= suma_venta + subtotal
            respuesta = int(input("\n¿Deseas elegir otro articulo? \n (1-Si / 0-No): "))
            if respuesta == 0:
                print("\nEl monto total es: $",suma_venta)
                break
    elif opcion==2:
        print("Este es el número de ventas: ",len(desglose))
        valor = int(input("Qué número de venta quieres consultar? :"))
        if valor > len(desglose):
            print("Este número de venta no esta disponible.")
        else:
            print(desglose[valor])
    elif opcion==3:
        print("Saliendo...")
        break
    else:
        print ("Opción incorrecta, vuelva a elegir un número del menú")
            
