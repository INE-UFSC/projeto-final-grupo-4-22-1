from itens.efeitosnojogador import EfeitosNoJogador
from abc import ABC


class EfeitoBonus(EfeitosNoJogador, ABC):
    def __init__(self, nome, largura, altura, coordenadax, coordenaday, bonus):
        super().__init__(nome, largura, altura, coordenadax, coordenaday)
        self.__bonus = bonus

    @property
    def bonus(self):
        return self.__bonus