import pygame

class Personagem(pygame.sprite.Sprite):
    def __init__(self, altura, largura, coordenadax, coordenaday, velocidade, COR):
        self.__altura = altura
        self.__largura = largura
        self.__coordenadax = coordenadax
        self.__coordenaday = coordenaday
        self.__velocidade = velocidade
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([altura, largura])
        self.image.fill(COR)
        self.rect = self.image.get_rect()
        self.rect.center = [coordenadax, coordenaday]

    @property
    def altura(self):
        return self.__altura
    
    @property
    def largura(self):
        return self.__largura

    @property
    def coordenadax(self):
        return self.__coordenadax

    @property
    def coordenaday(self):
        return self.__coordenaday

    @property
    def velocidade(self):
        return self.__velocidade

    def moverx(self, velocidade):
        self.__coordenadax += velocidade

    def movery(self, velocidade):
        self.__coordenaday += velocidade
