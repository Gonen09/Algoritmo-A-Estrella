import pygame

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)


def main():

    pygame.init()
    pantalla = pygame.display.set_mode([300, 300])
    pygame.display.set_caption("Laberinto")

    salida = False
    reloj = pygame.time.Clock()

    s1 = pygame.Surface([25, 25])
    s1.fill(BLANCO)
    s2 = pygame.Surface([25, 25])
    s2.fill(ROJO)
    s3 = pygame.Surface([25, 25])
    s3.fill(VERDE)
    s4 = pygame.Surface([25, 25])
    s4.fill(AZUL)

    while salida is not True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                salida = True

        reloj.tick(20)
        pantalla.fill(NEGRO)
        pantalla.blit(s1, [0, 0])
        pantalla.blit(s2, [275, 0])
        pantalla.blit(s3, [275, 275])
        pantalla.blit(s4, [0, 275])
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
