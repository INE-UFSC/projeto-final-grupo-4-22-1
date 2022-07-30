from game.character.Character import Character
from game.imageLibrary.ImageLibrary import ImageLibrary
import pygame

class Ra(Character):
    def __init__(self, altura_ra:int, largura_ra:int, coordenadax_ra:int, coordenaday_ra:int):
        super().__init__(altura_ra, largura_ra, coordenadax_ra, coordenaday_ra)
        self.__sprite = pygame.image.load(ImageLibrary().ra)

    @property
    def sprite(self):
        return self.__sprite
