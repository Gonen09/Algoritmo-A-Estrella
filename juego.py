#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos


# Clases
# ---------------------------------------------------------------------

class Mapa:
	def __init__(self, archivo="mapa.txt"):
		self.mapa = leerMapa(archivo)
		self.fil = len(self.mapa)
		self.col = len(self.mapa[0])
				
	def __str__(self):
		salida = ""
		for f in range(self.fil):
			for c in range(self.col):
				if self.mapa[f][c] == 0:
					salida += ". "
				if self.mapa[f][c] == 1:
					salida += "# "
				if self.mapa[f][c] == 2:
					salida += "T "
				if self.mapa[f][c] == 3:
					salida += "S "
			salida += "\n"
		return salida

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

# Quita el ultimo caracter de una lista.
def quitarUltimo(lista):
	for i in range(len(lista)):
		lista[i] = lista[i][:-1]
	return lista

# Covierte una cadena en una lista.	
def listarCadena(cadena):
	lista = []
	for i in range(len(cadena)):
		if cadena[i] == ".":
			lista.append(0)
		if cadena[i] == "#":
			lista.append(1)
		if cadena[i] == "T":
			lista.append(2)
		if cadena[i] == "S":
			lista.append(3)
	return lista

# Lee un archivo de texto y lo convierte en una lista.
def leerMapa(archivo):
	mapa = open(archivo, "r")
	mapa = mapa.readlines()
	mapa = quitarUltimo(mapa)
	for i in range(len(mapa)):
		mapa[i] = listarCadena(mapa[i])
	return mapa

# ---------------------------------------------------------------------

def main():
	mapa = Mapa()
	print mapa
	return 0

if __name__ == '__main__':
	main()
