from personagem import Personagem
import pygame

altura_do_ra = 30
largura_do_ra = 30
coordenadax_ra = 15
coordenaday_ra = 585
ROXO = (72, 61, 139)

class Ra(Personagem):
    def __init__(self):
        super().__init__(altura_do_ra, largura_do_ra, coordenadax_ra, coordenaday_ra, ROXO)
