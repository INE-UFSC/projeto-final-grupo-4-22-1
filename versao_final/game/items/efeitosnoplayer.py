from abc import ABC, abstractmethod

from game.items.Item import Item


class EfeitosNoJogador(Item, ABC):
    def __init__(self, nome, largura, altura, coordenadax, coordenaday, COR, efeito):
        super().__init__(nome, largura, altura, coordenadax, coordenaday, COR)
        self.__efeito = efeito

    @property
    def efeito(self):
        return self.__efeito

    @abstractmethod
    def aplicar_efeito(self, player):
        player.alterar_velocidade(self.__efeito)
