from itens.efeitosnojogador import EfeitosNoJogador
from abc import ABC


class EfeitoBonus(ABC, EfeitosNoJogador):
    def __init__(self, nome, largura, altura, coordenadax, coordenaday):
        super().__init__(nome, largura, altura, coordenadax, coordenaday)
