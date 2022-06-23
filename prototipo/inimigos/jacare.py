from inimigos.inimigo import Inimigo
import pygame

altura_jacare = 70
largura_jacare = 40
coordenadax_jacare = 150
coordenaday_jacare = 190
velocidade_jacare = 5
dano = 3
terreno = 'terrestre'

class Jacare(Inimigo, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(altura_jacare, largura_jacare, coordenadax_jacare, coordenaday_jacare, velocidade_jacare, dano, terreno)
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([largura_jacare, altura_jacare])
        self.image.fill((255, 255, 255))

        self.rect = self.image.get_rect()
