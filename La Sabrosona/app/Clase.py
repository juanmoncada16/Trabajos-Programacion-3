if __name__ == "__main__":
    #crar lista
    lista = ['bah', 'beh', 'bih', 'boh']
    print(lista)

    #recorrer lista
    print(lista)
    for elementon in lista:
        print(elementon)

    #comparar lista
    lista1 = ['beh', 'bah', 'boh', 'bih']
    if lista == lista1:
        print("Son identicas")

    #Longitud de lista
    print(len(lista))

    #concatenar lista
    print(lista + lista1)

    #sacar el numero mayor de la lista
    lista2 = [1,2,3,4,5]
    print(max(lista2))

    #sacar el numero minimo de la lista
    lista2 = [1, 2, 3, 4, 5]
    print(min(lista2))

    #lista enlanzada
    lista3 = ['esto es', [1,2,3], 75]
    print(lista3)
    print(lista3[0])
    print(lista3[1])
    print(lista3[1][1])

    #manipular lista
    lista4 = ['x', 'o', 'p','a']
    lista4.append('z')
    print(lista4)
    lista4.insert(0,'x')
    print(lista4)
    lista4.extend(lista2)
    print(lista4)
    lista4.remove('z')
    print(lista4)
    for i in range(5):
        lista4.pop()
    print(lista4)
    lista4[0] = 's'
    print(lista4)

    #replicar lista
    lista5 = [1,2,3]
    print(lista5 * 2)

    #slicing
    lista6 = ['carimanola', 'pajarilla', 'bofe']
    print(lista6[1:2])
    lista7 = []
    for i in range(100):
        lista7.append(i)
    print(lista7[6:70])
    print(lista7[:51])
    print(lista7[25:])
    