from inimigos.inimigo import Inimigo
import pygame

altura_cobra = 50
largura_cobra = 30
coordenadax_cobra = 200
coordenaday_cobra = 200
velocidade_cobra = 5
dano = 2
terreno = 'terrestre'
VERMELHO = 	(139, 0, 0)

class Cobra(Inimigo):
    def __init__(self):
        super().__init__(altura_cobra, largura_cobra, coordenadax_cobra, coordenaday_cobra, velocidade_cobra, dano, terreno, VERMELHO)
