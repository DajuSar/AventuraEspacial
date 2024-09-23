import pygame
from game import juego
from utils import pantalla, reloj, mostrar_texto, NEGRO, BLANCO

def menu_principal():
    opciones = ["Comenzar Juego", "Salir"]
    seleccion = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if opciones[seleccion] == "Comenzar Juego":
                        juego()
                    elif opciones[seleccion] == "Salir":
                        pygame.quit()
                        quit()

        pantalla.fill(NEGRO)
        mostrar_texto(pantalla, "Aventura Espacial", 75, pantalla.get_width() // 2, pantalla.get_height() // 2 - 200)
        for i, opcion in enumerate(opciones):
            if i == seleccion:
                # Resaltar la opción seleccionada
                pygame.draw.rect(pantalla, BLANCO, (pantalla.get_width() // 2 - 150, pantalla.get_height() // 2 - 25 + i * 60, 300, 50))
                mostrar_texto(pantalla, opcion, 50, pantalla.get_width() // 2, pantalla.get_height() // 2 + i * 60, color=NEGRO)
            else:
                mostrar_texto(pantalla, opcion, 50, pantalla.get_width() // 2, pantalla.get_height() // 2 + i * 60, color=BLANCO)

        pygame.display.update()
        reloj.tick(15)
