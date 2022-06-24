import pygame

altura = 800
largura = 200
coordenadax = 500
coordenaday = 0
AZUL = (0, 191, 255)

class Aquatico(pygame.sprite.Sprite):
    def __init__(self, altura, largura, coordenadax, coordenaday, AZUL):
        self.__altura = altura
        self.__largura = largura
        self.__coordenadax = coordenadax
        self.__coordenaday = coordenaday
        self.__cor = AZUL

        self.__vitorias_regias = []
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([altura, largura])
        self.image.fill(self.__cor)
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
    def vitorias_regias(self):
        return self.__vitorias_regias

    @vitorias_regias.setter
    def vitorias_regias(self, flor):
        self.__vitorias_regias.append(flor)
