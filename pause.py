import pygame
import time
from utils import pantalla, reloj, mostrar_texto, NEGRO, BLANCO

def pausa():
    opciones = ["Continuar", "Menú Principal", "Salir"]
    seleccion = 0
    pausado = True  # Variable para controlar el bucle

    while pausado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if opciones[seleccion] == "Continuar":
                        return
                    elif opciones[seleccion] == "Menú Principal":
                        return "menu_principal"
                    elif opciones[seleccion] == "Salir":
                        return "salir"

        # Dibujar el menú de pausa
        mostrar_texto(pantalla, "Juego Pausado", 75, pantalla.get_width() // 2, pantalla.get_height() // 2 - 150)

        for i, opcion in enumerate(opciones):
            if i == seleccion:
                # Resaltar la opción seleccionada
                pygame.draw.rect(pantalla, BLANCO, (pantalla.get_width() // 2 - 150,
                                                    pantalla.get_height() // 2 - 25 + i * 60, 300, 50))
                mostrar_texto(pantalla, opcion, 50, pantalla.get_width() // 2,
                              pantalla.get_height() // 2 + i * 60, color=NEGRO)
            else:
                mostrar_texto(pantalla, opcion, 50, pantalla.get_width() // 2,
                              pantalla.get_height() // 2 + i * 60)

        pygame.display.update()
        reloj.tick(15)
