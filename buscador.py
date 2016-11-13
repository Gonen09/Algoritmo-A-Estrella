# -*- coding: utf-8 -*-
import time
import os
import random
import threading
import pygame


TIEMPO_ESPERA = 0.5
TAM_TEXTURA = 32  # 32 x 32

# Colores

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)


class Mapa:

    def __init__(self, archivo="mapas/mapa.txt"):
        self.mapa = leerMapa(archivo)
        self.fil = len(self.mapa)
        self.col = len(self.mapa[0])

    def __str__(self):

        salida = ""

        for f in range(self.fil):
            for c in range(self.col):
                if self.mapa[f][c] == 0:
                    salida += "  "
                if self.mapa[f][c] == 1:
                    salida += "# "
                if self.mapa[f][c] == 2:
                    salida += "T "
                if self.mapa[f][c] == 3:
                    salida += "S "
                if self.mapa[f][c] == 4:
                    salida += ". "
            salida += "\n"
        return salida

    def camino(self, lista):

        # muestra el camino que recorre definido con ". . . ."

        for i in range(len(lista) - 1):
            self.mapa[lista[i][0]][lista[i][1]] = 4
            print self
            time.sleep(TIEMPO_ESPERA)
            os.system("cls")


class Nodo:
    def __init__(self, pos=[0, 0], padre=None):
        self.pos = pos
        self.padre = padre
        self.h = distancia(self.pos, pos_f)

        if self.padre == None:
            self.g = 0
        else:
            self.g = self.padre.g + 1

        # Peso del nodo
        self.f = self.g + self.h


class AEstrella:

    # abierta: Lista con los nuevos nodos visitados (vecinos)
    # cerrada: Lista con los nodos ya visitados

    def __init__(self, mapa):
        self.mapa = mapa

        # Nodos de inicio y fin.
        self.inicio = Nodo(buscarPos(2, mapa))  # busca una T (entrada)
        self.fin = Nodo(buscarPos(3, mapa))  # busca una S (salida)

        # Crea las listas abierta y cerrada.
        self.abierta = []
        self.cerrada = []

        # Añade el nodo inicial a la lista cerrada.
        self.cerrada.append(self.inicio)

        # Añade los vecinos a la lista abierta
        self.abierta += self.vecinos(self.inicio)

        # Buscar mientras objetivo no este en la lista cerrada.
        g = Grafica(self.mapa)

        while self.objetivo():

            g.dibujarMapa()
            g.dibujarPaso(self.cerrada[-1])
            time.sleep(TIEMPO_ESPERA)
            g.borrarPaso(self.cerrada[-1])
            time.sleep(TIEMPO_ESPERA)
            print "Dentro de A Estrella"
            if self.fin.pos != pos_f:
                if self.cerrada[-1].pos is not pos_f:
                    print "Mapa cambiado"
                    time.sleep(TIEMPO_ESPERA)
                    self.reInicio(self.inicio, self.cerrada[-1])
                    self.recargar(self.mapa)
                    time.sleep(TIEMPO_ESPERA)
                else:
                    print "Mapa choque"
                    print "actual: " + str(self.cerrada[-1].pos)
                    print "final n: " + str(pos_f)
                    g.visualizar()
            self.buscar()

        print "Fuera de A Estrella"
        self.camino = self.camino()

    # Devuelve una lista con los nodos vecinos transitables.
    def vecinos(self, nodo):
        vecinos = []

        if self.mapa.mapa[nodo.pos[0] + 1][nodo.pos[1]] != 1:
            vecinos.append(Nodo([nodo.pos[0] + 1, nodo.pos[1]], nodo))
        if self.mapa.mapa[nodo.pos[0] - 1][nodo.pos[1]] != 1:
            vecinos.append(Nodo([nodo.pos[0] - 1, nodo.pos[1]], nodo))
        if self.mapa.mapa[nodo.pos[0]][nodo.pos[1] - 1] != 1:
            vecinos.append(Nodo([nodo.pos[0], nodo.pos[1] - 1], nodo))
        if self.mapa.mapa[nodo.pos[0]][nodo.pos[1] + 1] != 1:
            vecinos.append(Nodo([nodo.pos[0], nodo.pos[1] + 1], nodo))
        return vecinos

    # Pasa el elemento de f menor de la lista abierta a la cerrada.
    def f_menor(self):
        a = self.abierta[0]
        n = 0
        for i in range(1, len(self.abierta)):
            if self.abierta[i].f < a.f:
                a = self.abierta[i]
                n = i
        self.cerrada.append(self.abierta[n])
        del self.abierta[n]

    # Comprueba si un nodo está en una lista.
    def en_lista(self, nodo, lista):
        for i in range(len(lista)):
            if nodo.pos == lista[i].pos:
                return 1
        return 0

    # Gestiona los vecinos del nodo seleccionado.
    def ruta(self):
        for i in range(len(self.nodos)):
            if self.en_lista(self.nodos[i], self.cerrada):
                continue
            elif not self.en_lista(self.nodos[i], self.abierta):
                self.abierta.append(self.nodos[i])
            else:
                if self.select.g + 1 < self.nodos[i].g:
                    for j in range(len(self.abierta)):
                        if self.nodos[i].pos == self.abierta[j].pos:
                            del self.abierta[j]
                            self.abierta.append(self.nodos[i])
                            break

    # Analiza el último elemento de la lista cerrada.
    def buscar(self):
        self.f_menor()
        self.select = self.cerrada[-1]  # ultimo elemento
        self.nodos = self.vecinos(self.select)
        self.ruta()

    # Comprueba si el objetivo está en la lista abierta.
    def objetivo(self):
        for i in range(len(self.abierta)):
            if self.fin.pos == self.abierta[i].pos:
                return 0
        return 1

    # Retorna una lista con las posiciones del camino a seguir.
    def camino(self):

        for i in range(len(self.abierta)):
            if self.fin.pos == self.abierta[i].pos:
                objetivo = self.abierta[i]

        camino = []

        while objetivo.padre != None:
            camino.append(objetivo.pos)
            objetivo = objetivo.padre

        camino.reverse()

        return camino

    # Crea nuevo punto de partida

    def reInicio(self, nodo_inicial, nodo_actual):

        inicio_original = nodo_inicial.pos
        inicio_nuevo = nodo_actual.pos  # ultimo nodo en lista cerrada
        self.mapa.mapa[inicio_original[0]][inicio_original[1]] = 0  # " "
        self.mapa.mapa[inicio_nuevo[0]][inicio_nuevo[1]] = 2  # "T"

    # Recargar datos iniciales
    def recargar(self, mapa):

        print "Dentro de recargar"

        # Nodos de inicio y fin

        self.inicio = Nodo(buscarPos(2, mapa))  # busca una T (entrada)
        self.fin = Nodo(buscarPos(3, mapa))  # busca una S (salida)
        print "recargar inicio: " + str(self.inicio.pos)
        print "recargar fin: " + str(self.fin.pos)

        # Crea las listas abierta y cerrada.
        self.abierta = []
        self.cerrada = []

        # Añade el nodo inicial a la lista cerrada.
        self.cerrada.append(self.inicio)

        # Añade los vecinos a la lista abierta
        self.abierta += self.vecinos(self.inicio)


class Grafica:

    def __init__(self, mapa):

        # Dimensiones
        self.mapa = mapa
        self.dimx = mapa.col * TAM_TEXTURA
        self.dimy = mapa.fil * TAM_TEXTURA
        self.dimTextura = [TAM_TEXTURA, TAM_TEXTURA]

        # Inicializar graficos
        pygame.init()
        pygame.display.set_caption("Laberinto")
        self.pantalla = pygame.display.set_mode([self.dimx, self.dimy])
        self.pantalla.fill(NEGRO)
        self.texturas = self.cargarTexturas()

    def cargarTexturas(self):

        texturas = []
        fondo = "texturas/fondo.png"
        muro = "texturas/bloque" + str(random.randint(1, 7)) + ".png"
        entrada = "texturas/entrada.png"
        salida = "texturas/salida.png"
        personaje = "texturas/trugg.png"

        if existeArchivo(fondo):
            s0 = pygame.image.load(fondo)
        else:
            s0 = pygame.Surface(self.dimTextura)
            s0.fill(NEGRO)
        texturas.append(s0)

        if existeArchivo(muro):
            s1 = pygame.image.load("texturas/bloque" + str(random.randint(1, 7)) + ".png")
        else:
            s1 = pygame.Surface(self.dimTextura)
            s1.fill(ROJO)
        texturas.append(s1)

        if existeArchivo(entrada):
            s2 = pygame.image.load(entrada)
        else:
            s2 = pygame.Surface(self.dimTextura)
            s2.fill(AZUL)
        texturas.append(s2)

        if existeArchivo(salida):
            s3 = pygame.image.load(salida)
        else:
            s3 = pygame.Surface(self.dimTextura)
            s3.fill(VERDE)
        texturas.append(s3)

        if existeArchivo(personaje):
            s4 = pygame.image.load(personaje)
        else:
            s4 = pygame.Surface(self.dimTextura)
            s4.fill(BLANCO)
        texturas.append(s4)

        return texturas

    def crearMapa(self):

        for f in range(self.mapa.fil):
            for c in range(self.mapa.col):

                if self.mapa.mapa[f][c] == 0:
                    self.pantalla.blit(self.texturas[0], [c * TAM_TEXTURA, f * TAM_TEXTURA])  # " "
                if self.mapa.mapa[f][c] == 1:
                    self.pantalla.blit(self.texturas[1], [c * TAM_TEXTURA, f * TAM_TEXTURA])  # "#"
                if self.mapa.mapa[f][c] == 2:
                    self.pantalla.blit(self.texturas[2], [c * TAM_TEXTURA, f * TAM_TEXTURA])  # "T"
                if self.mapa.mapa[f][c] == 3:
                    self.pantalla.blit(self.texturas[3], [c * TAM_TEXTURA, f * TAM_TEXTURA])  # "S"
                if self.mapa.mapa[f][c] == 4:
                    self.pantalla.blit(self.texturas[0], [c * TAM_TEXTURA, f * TAM_TEXTURA])  # "." En caso de haber

    def dibujarMapa(self):
        self.crearMapa()
        pygame.display.update()

    def dibujarPaso(self, nodo):

        self.crearMapa()
        self.pantalla.blit(self.texturas[4], [nodo.pos[1] * TAM_TEXTURA, nodo.pos[0] * TAM_TEXTURA])
        pygame.display.update()

    def borrarPaso(self, nodo):
        self.crearMapa()
        self.pantalla.blit(self.texturas[0], [nodo.pos[1] * TAM_TEXTURA, nodo.pos[0] * TAM_TEXTURA])
        pygame.display.update()

    def dibujarRecorrido(self, camino):

        self.crearMapa()  # Creamos el entorno
        longitud = len(camino) - 1  # Hasta uno antes de la salida

        for i in range(longitud):
            self.pantalla.blit(self.texturas[4], [camino[i][1] * TAM_TEXTURA, camino[i][0] * TAM_TEXTURA])
            pygame.display.update()

            time.sleep(TIEMPO_ESPERA)  # Para alcanzar a visualizar el cambio en los componentes

            if i is not longitud:
                self.pantalla.blit(self.texturas[0], [camino[i][1] * TAM_TEXTURA, camino[i][0] * TAM_TEXTURA])
                pygame.display.update()

        salida = self.buscarSalida()

        # Cerrar puerta
        self.pantalla.blit(self.texturas[2], [salida[0] * TAM_TEXTURA, salida[1] * TAM_TEXTURA])  # "S"
        pygame.display.update()

    # Mantiene la ventana visible
    def visualizar(self):

        salida = False
        reloj = pygame.time.Clock()

        while salida is not True:
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    salida = True

            reloj.tick(30)
            pygame.display.update()

        pygame.quit()

    def buscarSalida(self):

        salida = [0, 0]
        for f in range(self.mapa.fil):
            for c in range(self.mapa.col):
                if self.mapa.mapa[f][c] == 3:
                    salida = [c, f]
                    break
        return salida

# ---------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------

# Devuelve la posición de "x" en una lista.
def buscarPos(x, mapa):
    for f in range(mapa.fil):
        for c in range(mapa.col):
            if mapa.mapa[f][c] == x:
                return [f, c]
    return 0


# Distancia entre dos puntos.
def distancia(a, b):

    # heurística de Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Valor absoluto.


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


# Comprueba si existe el archivo
def existeArchivo(archivo):

    if os.path.exists(archivo):
        return True
    else:
        return False


# Genera una nueva posicion de salida valida
def nuevaSalida(mapa):

    salida = False
    nueva = [0, 0]

    while not salida:

        x_nueva = random.randint(0, mapa.fil - 1)
        y_nueva = random.randint(0, mapa.col - 1)

        nueva = [x_nueva, y_nueva]
        # print nueva

        if nueva is not pos_f:

            if mapa.mapa[x_nueva][y_nueva] is 0:  # camino, 0 = .
                # print "La salida cambió a: " + str(nueva)
                salida = True

    return nueva


def cambiarSalida(mapa):

    print "Inicio cambio mapa"
    print mapa

    salida_original = pos_f  # S
    salida_nueva = nuevaSalida(mapa)

    # Comprueba si la salida está en los bordes del mapa

    if (salida_original[0] == 0) or (salida_original[0] == (mapa.fil - 1)) or \
       (salida_original[1] == 0) or (salida_original[1] == (mapa.col - 1)):
        mapa.mapa[salida_original[0]][salida_original[1]] = 1  # "#"
    else:
        mapa.mapa[salida_original[0]][salida_original[1]] = 0  # " "

    mapa.mapa[salida_nueva[0]][salida_nueva[1]] = 3  # "S"
    globals()["pos_f"] = salida_nueva

    print mapa
    print "fin cambio mapa"


def resolverLaberinto(mapa):

    A = AEstrella(mapa)
    globals()["Fin"] = True
    # mapa.camino(A.camino)
    g = Grafica(mapa)
    g.dibujarRecorrido(A.camino)
    longitud = len(A.camino)

    for i in range(longitud):
        print "pos: " + str(A.camino[i])
    g.visualizar()
    os.system("cls")

# ---------------------------------------------------------------------


def main():

    globals()["mapa"] = Mapa()
    globals()["pos_f"] = buscarPos(3, mapa)
    globals()["Fin"] = False

    cs = threading.Thread(target=resolverLaberinto, args=(mapa,))
    cs.start()

    while cs.isAlive():

        if Fin is False:
            cambiarSalida(mapa)
        time.sleep(1)

    return 0

if __name__ == '__main__':
    main()
