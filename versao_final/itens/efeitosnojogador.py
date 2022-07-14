from itens.item import Item
from abc import ABC, abstractmethod


class EfeitosNoJogador(Item, ABC):
    def __init__(self, nome, largura, altura, coordenadax, coordenaday, COR, efeito):
        super().__init__(nome, largura, altura, coordenadax, coordenaday, COR)
        self.__efeito = efeito
    
    @property
    def efeito(self):
        return self.__efeito

    @abstractmethod
    def aplicar_efeito(self, jogador):
        jogador.alterar_velocidade(self.__efeito)