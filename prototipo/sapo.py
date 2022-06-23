from player import Player
import pygame

altura_do_sapo = 30
largura_do_sapo = 30
vidas_do_sapo = 3
coordenadax_sapo = 30
coordenaday_sapo = 30
velocidade_do_sapo = 12
BRANCO = (0,0,0)

class Sapo(Player, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(altura_do_sapo, largura_do_sapo, vidas_do_sapo, coordenadax_sapo, coordenaday_sapo, velocidade_do_sapo)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([largura_do_sapo, altura_do_sapo])
        self.image.fill(BRANCO)

        self.rect = self.image.get_rect()
