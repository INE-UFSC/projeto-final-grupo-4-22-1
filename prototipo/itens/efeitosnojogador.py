from itens.item import Item
from abc import ABC


class EfeitosNoJogador(ABC, Item):
    def __init__(self, nome, largura, altura, coordenadax, coordenaday):
        super().__init__(nome, largura, altura, coordenadax, coordenaday)
