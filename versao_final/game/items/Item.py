from abc import ABC, abstractmethod
import pygame


class Item(ABC, pygame.sprite.Sprite):
    def __init__(self, nome, largura, altura, coordenadax, coordenaday, sprite):
        self.__nome = nome
        self.__largura = largura
        self.__altura = altura
        self.__coordenadax = coordenadax
        self.__coordenaday = coordenaday
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([altura, largura])
        self.rect = self.image.get_rect()
        self.rect.center = [coordenadax, coordenaday]
        self.__sprite = pygame.image.load(sprite)

    @property
    def nome(self):
        return self.__nome

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura

    @property
    def coordenadax(self):
        return self.__coordenadax

    @property
    def coordenaday(self):
        return self.__coordenaday

    @property
    def sprite(self):
        return self.__sprite
