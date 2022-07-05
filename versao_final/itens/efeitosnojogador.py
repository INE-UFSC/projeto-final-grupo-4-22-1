from itens.item import Item
from abc import ABC


class EfeitosNoJogador(Item, ABC):
    def __init__(self, nome, largura, altura, coordenadax, coordenaday, COR):
        super().__init__(nome, largura, altura, coordenadax, coordenaday, COR)