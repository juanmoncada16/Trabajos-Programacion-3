if __name__ == "__main__":
    import re
    print("\t\t\t----------------------------------------------------")
    print("\t\t\t| BIENVENIDOS A IDENTIFICACION DE PLACAS DE PANAMA |")
    print("\t\t\t----------------------------------------------------\n\n")

    placa = input("Introduzca El Tipo de Placa: ")

    if re.match("M-[0-9]{5}$", placa):
        print("\n\nES UNA PLACA DE MOTO")
    elif re.match("B-[0-9]{5}$", placa):
        print("\n\nES UNA PLACA DE BICICLETA")
    elif re.match("T[0-9]{5}$", placa):
        print("\n\nES PLACA DE TAXI")
    elif re.match("MB[0-9]{4}$", placa):
        print("\n\nES PLACA DE METROBUS")
    elif re.match("MB[0-9]{4}$", placa):
        print("\n\nES PLACA DE METROBUS")
    elif re.match("CP[0-9]{4}$", placa):
        print("\n\nES PLACA DE AUTO DE CANAL DE PANAMA")
    elif re.match("CC[0-9]{4}$", placa):
        print("\n\nES PLACA DE AUTO DE CUERPO CONSULAR")
    elif re.match("CH[0-9]{4}$", placa):
        print("\n\nES PLACA DE AUTO DE CUERPO HONORARIO")
    elif re.match("MI[0-9]{4}$", placa):
        print("\n\nES PLACA DE AUTO DE MISION INTERNACIONAL")
    elif re.match("CD[0-9]{4}$", placa):
        print("\n\nES PLACA DE AUTO DE CUERPO DIPLOMATICO")
    elif re.match("E[0-9]{4}$", placa):
        print("\n\nES PLACA DE AUTO DE JUECES O FISCALES")
    elif re.match("ADM[0-9]{3}$", placa):
        print("\n\nES PLACA DE AUTO DE ADMINISTRACION")
    elif re.match("PR[0-9]{4}$", placa):
        print("\n\nES PLACA DE AUTO DE PRENSA")
    elif re.match("HP[0-9]{4}$", placa):
        print("\n\nES PLACA DE AUTO DE RADIO")
    elif re.match("\w\w\w\d\d\d$", placa):
        print("\n\nES UNA PLACA DE CARRO")
    else:
        print("\n\nES PLACA INVALIDA")