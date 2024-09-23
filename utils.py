import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (206, 224, 220)

# Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Aventura Espacial")

# Reloj para controlar FPS
reloj = pygame.time.Clock()

def mostrar_texto(superficie, texto, tamaño, x, y, color=BLANCO):
    fuente = pygame.font.Font(None, tamaño)
    texto_superficie = fuente.render(texto, True, color)
    texto_rect = texto_superficie.get_rect(center=(x, y))
    superficie.blit(texto_superficie, texto_rect)
