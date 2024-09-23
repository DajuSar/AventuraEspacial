import pygame
from utils import pantalla, mostrar_texto, ANCHO, ALTO

# Lista global de puntuaciones altas
high_scores = []

def guardar_puntuacion(puntuacion):
    global high_scores
    if puntuacion not in high_scores:
        high_scores.append(puntuacion)
        high_scores.sort(reverse=True)
        high_scores = high_scores[:3]  # Mantener solo las 3 mejores puntuaciones

def mostrar_puntuaciones():
    global high_scores
    mostrar_texto(pantalla, "Mejores puntuaciones:", 50, ANCHO // 2, ALTO // 2 - 80)
    for i, score in enumerate(high_scores):
        mostrar_texto(pantalla, f"{i+1}. Total: {score}", 40, ANCHO // 2, ALTO // 2 - 50 + i * 30)
