from personagem import Personagem
import pygame

ROXO = (72, 61, 139)

class Ra(Personagem):
    def __init__(self, altura_ra:int, largura_ra:int, coordenadax_ra:int, coordenaday_ra:int):
        super().__init__(altura_ra, largura_ra, coordenadax_ra, coordenaday_ra, ROXO)
