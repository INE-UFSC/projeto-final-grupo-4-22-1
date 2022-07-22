import pygame

from ImageLibrary import ImageLibrary

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        self.__altura = 100
        self.__largura = 100

        pygame.sprite.Sprite.__init__(self)
        
        self.__imagens = ImageLibrary()
        self.__sprite = self.__imagens.ground

    @property
    def altura(self):
        return self.__altura
    
    @property
    def largura(self):
        return self.__largura

    @property
    def sprite(self):
        return self.__sprite
