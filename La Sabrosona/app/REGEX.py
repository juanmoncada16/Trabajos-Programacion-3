if __name__ == "__main__":
    import re

    palabra = input("palabra a evaluar: ")
    #usar los punto . que son comodines que puede usarse para variar
    #usar \ para evaluar los puntos
    #usar | para clasificar unos de las variables
    #usar () para agrupar los que desea evaluar
    #usar .. o ... etc. dependiendo lo que se quiere evaluar
    #Usar R 0-9 con D para usar el rango de numeros
    #Usar a-z para usar rango de letras
    #se puede combinar rangos ejemplo a-z0-5 se usa entre letras y numeros
    #\d se indica que el caracter que se coloque sea un digito y \D indica que no sea un digito
    #\w se indica que sea un caracter alfanumerico y \W indica que no sea un caracter alfanumerico
    #\s indica un espacio en blanco y \S indica que sea cualquier cosa pero que no sea un espacio en blanco
    # + significa que lo que esta en la izquierda una varias veces
    # * significa 0 o varias
    # ? significa 0 o una
    # [] significa el numero de veces que se repite
    # usar re.search si queremos que dicho caracteres coincida sin importa la posicion
    # usar re.match si queremos evaluar palabras de izquiera a derecha
    # Evaluar Inicio de la palabra ^ y para el final usar $

    if re.match("ca\da", palabra):
        print("coincidencia")
    else:
        print("no coincidencia")

    if re.match("ca.a\w", palabra):
        print("coincidencia")
    else:
        print("no coincidencia")

    if re.match("ca.a\s", palabra):
        print("coincidencia")
    else:
        print("no coincidencia")

    if re.match("ca[a-c0-5a]", palabra):
        print("coincidencia")
    else:
        print("no coincidencia")

    if re.match("ca[0-9]a", palabra):
        print("coincidencia")
    else:
        print("no coincidencia")

    if re.match("ca.a", palabra):
        print("coincidencia")
    else:
        print("no coincidencia")

    if re.match("ca(..|...)a", palabra):
        print("coincidencia")
    else:
        print("no coincidencia")

    if re.match("\.(jpg|png|gif)", palabra):
        print("coincidencia")
    else:
        print("no coincidencia")

    if re.match("\.casa", palabra):
        print("coincidencia")
    else:
        print("no coincidencia")

    if re.match("jpg|png|gif", palabra):
        print("coincidencia")
    else:
        print("no coincidencia")

    if re.match("[A-Z][a-z]+\s[A-Z](\.|[a/z]*)", palabra):
        print("coincidencia")
    else:
        print("no coincidencia")