from inimigos.inimigo import Inimigo
import pygame

altura_cobra = 50
largura_cobra = 30
coordenadax_cobra = 80
coordenaday_cobra = 80
velocidade_cobra = 5
dano = 2
terreno = 'terrestre'

class Cobra(Inimigo, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(altura_cobra, largura_cobra, coordenadax_cobra, coordenaday_cobra, velocidade_cobra, dano, terreno)
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([largura_cobra, altura_cobra])
        self.image.fill((139, 0, 0))

        self.rect = self.image.get_rect()
