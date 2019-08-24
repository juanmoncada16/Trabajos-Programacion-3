if __name__ == "__main__":
    print("FONDA LA SABROSONA")
    print("------------------\n")

    cliente = input ("Cliente: ")
    while True:
        print("MENU")
        lista = ['1. Mondongo\t$1.50', '2. Lengua\t$0.75', '3. Pata\t\t$2.00']
        for elementon in lista:
            print(elementon)
        try:
            opcion = int(input("Opcion: "))
        except:
            opcion = -1

        if opcion == 1:
            precio = 1.50
            comida = "Mondongo"
            break
        elif opcion == 2:
            precio = 0.75
            comida = "Lengua"
            break
        elif opcion == 3:
            precio = 2.00
            comida = "Pata"
            break
        else:
            print("Opcion Invalida")

    total = precio * 1.07

    print(cliente + ", debe pagar $" + str(total))

    pago = input ("pago? (S/N)")
    if pago.upper() == "S":
        print("Toma tu", comida + ",", cliente + " ¡Gracias!")
    else:
        print("Pedido Cancelado")
