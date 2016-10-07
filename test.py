from buscador import quitarUltimo


class Figura:

    def __init__(self, largo=0, alto=0, nombre='sin nombre'):
        self.largo = largo
        self.alto = alto
        self.nombre = nombre
        self.clase = 'Figura'

    def __str__(self):
        return "Figura: " + self.nombre + " Largo: " + str(self.largo) + " Alto: " + str(self.alto)

lista_enteros = []
lista_enteros.append(1)
lista_enteros.append(2)
lista_enteros.append(3)
lista_enteros.append(4)
lista_enteros.append(5)

print lista_enteros

lista_caracteres = []
lista_caracteres.append('A')
lista_caracteres.append('B')
lista_caracteres.append('C')
lista_caracteres.append('D')
lista_caracteres.append('E')
lista_caracteres.append('F')
lista_caracteres.append('G')
lista_caracteres.append('H')

print lista_caracteres

lista_final = []
lista_final += lista_enteros
lista_final += lista_caracteres

print lista_final

print lista_enteros
del lista_enteros[-1]
print lista_enteros
# quitarUltimo(lista_enteros) no tiene el atributo __getitem__
# print lista_enteros

lista_caracteres = []
lista_caracteres.append('A')
lista_caracteres.append('B')
lista_caracteres.append('C')
lista_caracteres.append('D')
lista_caracteres.append('E')
lista_caracteres.append('F')
lista_caracteres.append('G')
lista_caracteres.append('H')

print lista_caracteres
del lista_caracteres[-1]
print lista_caracteres
elemento = lista_caracteres[-1]
print "elemento = "+elemento
print lista_caracteres
lista_caracteres.reverse()
print lista_caracteres
quitarUltimo(lista_caracteres)
print lista_caracteres


test = []

duotest = ['a', 'b', 'c', 'd']

for i in range(5):
    test.append(duotest)

print test

print test[0][1]


a = duotest[0]

print "a:" + a
print duotest
