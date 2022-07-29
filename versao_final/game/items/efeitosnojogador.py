from abc import ABC, abstractmethod

from game.items.Item import Item


class EfeitosNoJogador(Item, ABC):
    def __init__(self, nome, largura, altura, coordenadax, coordenaday, COR, efeito, sprite):
        super().__init__(nome, largura, altura, coordenadax, coordenaday, COR, sprite)
        self.__efeito = efeito

    @property
    def efeito(self):
        return self.__efeito

    @abstractmethod
    def aplicar_efeito(self, jogador):
        jogador.alterar_velocidade(self.__efeito)
