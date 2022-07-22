import pygame
from ImageLibrary import ImageLibrary

class Water(pygame.sprite.Sprite):
    def __init__(self):
        self.__altura = 100
        self.__largura = 100

        self.__vitorias_regias = []
        pygame.sprite.Sprite.__init__(self)
        
        self.__imagens = ImageLibrary()
        self.__sprite = self.__imagens.water

    @property
    def altura(self):
        return self.__altura
    
    @property
    def largura(self):
        return self.__largura

    @property
    def sprite(self):
        return self.__sprite

    @property
    def vitorias_regias(self):
        return self.__vitorias_regias

    @vitorias_regias.setter
    def vitorias_regias(self, flor):
        self.__vitorias_regias.append(flor)
