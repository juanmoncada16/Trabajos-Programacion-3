class perro:
    especie = 'mamifero' #atributo

    def __init__(self, nombre, edad):
        self.nombre = nombre #atributos de instancia
        self.edad = edad #atributos de instancia

    def description(self):
        return "{} tiene {} años de edad".format(self.nombre, self.edad)

    def hablar(self, sonido):
        return "{} dice {}".format(self.nombre, sonido)

class Rottweiler(perro):
    def correr(self, velocidad):
        print("{} corre a {}".format(self.nombre, velocidad))

lassie = perro("lassie", 5)
print(lassie.description())
print(lassie.hablar("Woof Woof"))
roco = Rottweiler("Roco", 10)
roco.correr(50)
print (roco.hablar("que es lo que eh"))


