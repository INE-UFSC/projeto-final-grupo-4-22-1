from itens.item import Item
from abc import ABC


class Coletaveis(ABC, Item):
    def __init__(self, nome, largura, altura, coordenadax, coordenaday, peso):
        super().__init__(nome, largura, altura, coordenadax, coordenaday)
        self.__peso = peso
