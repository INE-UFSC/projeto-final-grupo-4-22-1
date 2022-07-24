from abc import ABC

from game.items.Item import Item


class Collectibles(Item, ABC):
    def __init__(self, nome, largura, altura, coordenadax, coordenaday, peso, COR):
        super().__init__(nome, largura, altura, coordenadax, coordenaday, COR)
        self.__peso = peso

    @property
    def peso(self):
        return self.__peso
