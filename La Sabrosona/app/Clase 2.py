    #funciones calcular un area de un circulo
def calcular_area (lado):
    area = lado * lado
    return area

def saludar ():
    print("Bienvenido Sr. Cuadrado")

if __name__ == "__main__":
    saludar()
    lado = float(input("Lado: "))
    resultado = calcular_area(lado)
    print (resultado)



