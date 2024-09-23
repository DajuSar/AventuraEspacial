import pygame
import random
from utils import pantalla, reloj, mostrar_texto, ANCHO, ALTO, NEGRO, BLANCO
from pause import pausa
from scores import guardar_puntuacion, mostrar_puntuaciones

# Cargar imágenes
imagen_jugador = pygame.image.load("assets/nave.png")
imagen_enemigo = pygame.image.load("assets/enemigo.png")

def juego():
    # Variables del jugador
    x_jugador = ANCHO * 0.45
    y_jugador = ALTO * 0.8
    velocidad_jugador = 0

    # Lista de enemigos
    lista_enemigos = []

    # Función para crear enemigos
    def crear_enemigo():
        x_enemigo = random.randrange(0, ANCHO - imagen_enemigo.get_width())
        y_enemigo = -imagen_enemigo.get_height()
        lista_enemigos.append([x_enemigo, y_enemigo])

    # Contador para controlar la aparición de enemigos
    contador_enemigos = 0

    # Sistema de puntuación
    tiempo_inicio = pygame.time.get_ticks()
    puntuacion = 0

    jugando = True
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    velocidad_jugador = -5
                elif evento.key == pygame.K_RIGHT:
                    velocidad_jugador = 5
                elif evento.key == pygame.K_ESCAPE:
                    accion = pausa()
                    if accion == "menu_principal":
                        return
                    elif accion == "salir":
                        pygame.quit()
                        quit()
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    velocidad_jugador = 0

        x_jugador += velocidad_jugador

        # Mantener al jugador dentro de la pantalla
        if x_jugador < 0:
            x_jugador = 0
        elif x_jugador > ANCHO - imagen_jugador.get_width():
            x_jugador = ANCHO - imagen_jugador.get_width()

        pantalla.fill(NEGRO)

        # Dibujar jugador
        pantalla.blit(imagen_jugador, (x_jugador, y_jugador))

        # Crear enemigos
        if contador_enemigos == 0:
            crear_enemigo()
            contador_enemigos = 50  # Tiempo entre enemigos
        else:
            contador_enemigos -= 1

        # Mover y dibujar enemigos
        for enemigo in lista_enemigos[:]:
            enemigo[1] += 5  # Velocidad del enemigo
            pantalla.blit(imagen_enemigo, (enemigo[0], enemigo[1]))

            # Comprobar si el enemigo sale de la pantalla
            if enemigo[1] > ALTO:
                lista_enemigos.remove(enemigo)

            # Comprobar colisiones
            if y_jugador < enemigo[1] + imagen_enemigo.get_height():
                if (x_jugador > enemigo[0] and x_jugador < enemigo[0] + imagen_enemigo.get_width()) or \
                   (x_jugador + imagen_jugador.get_width() > enemigo[0] and x_jugador + imagen_jugador.get_width() < enemigo[0] + imagen_enemigo.get_width()):
                    # Guardar puntuación
                    tiempo_fin = pygame.time.get_ticks()
                    puntuacion = (tiempo_fin - tiempo_inicio) // 1000  # Convertir a segundos
                    guardar_puntuacion(puntuacion)
                    game_over(puntuacion)
                    return

        # Actualizar puntuación
        tiempo_actual = pygame.time.get_ticks()
        puntuacion = (tiempo_actual - tiempo_inicio) // 1000
        mostrar_texto(pantalla, f"Puntuación: {puntuacion}", 30, 70, 20)

        pygame.display.update()
        reloj.tick(60)

def game_over(puntuacion_actual):
    opciones = ["Jugar de Nuevo", "Menú Principal", "Salir"]
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
                    if opciones[seleccion] == "Jugar de Nuevo":
                        juego()
                        return
                    elif opciones[seleccion] == "Menú Principal":
                        return
                    elif opciones[seleccion] == "Salir":
                        pygame.quit()
                        quit()

        pantalla.fill(NEGRO)
        mostrar_texto(pantalla, "¡Has perdido!", 75, pantalla.get_width() // 2, pantalla.get_height() // 2 - 200)
        mostrar_texto(pantalla, f"Tu puntuación: {puntuacion_actual} s", 50, pantalla.get_width() // 2, pantalla.get_height() // 2 - 150)

        # Mostrar mejores puntuaciones
        mostrar_puntuaciones()

        # Mostrar opciones del menú
        for i, opcion in enumerate(opciones):
            if i == seleccion:
                # Resaltar la opción seleccionada
                pygame.draw.rect(pantalla, BLANCO, (pantalla.get_width() // 2 - 150, pantalla.get_height() // 2 + 75 + i * 60, 300, 50))
                mostrar_texto(pantalla, opcion, 50, pantalla.get_width() // 2, pantalla.get_height() // 2 + 100 + i * 60, color=NEGRO)
            else:
                mostrar_texto(pantalla, opcion, 50, pantalla.get_width() // 2, pantalla.get_height() // 2 + 100 + i * 60)

        pygame.display.update()
        reloj.tick(15)