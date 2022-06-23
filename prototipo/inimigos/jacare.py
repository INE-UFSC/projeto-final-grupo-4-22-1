from inimigos.inimigo import Inimigo
import pygame

altura_jacare = 70
largura_jacare = 40
coordenadax_jacare = 600
coordenaday_jacare = 190
velocidade_jacare = 5
dano = 3
terreno = 'aquatico'
VERDE_ESCURO = (0, 100, 0)

class Jacare(Inimigo):
    def __init__(self):
        super().__init__(altura_jacare, largura_jacare, coordenadax_jacare, coordenaday_jacare, velocidade_jacare, dano, terreno, VERDE_ESCURO)
