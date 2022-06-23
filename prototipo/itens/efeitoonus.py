from itens.efeitosnojogador import EfeitosNoJogador
from abc import ABC


class EfeitoOnus(EfeitosNoJogador, ABC):
    def __init__(self, nome, largura, altura, coordenadax, coordenaday, onus):
        super().__init__(nome, largura, altura, coordenadax, coordenaday)
        self.__onus = onus

    @property
    def onus(self):
        return self.__onus