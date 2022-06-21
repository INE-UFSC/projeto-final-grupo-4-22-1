from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, nome, largura, altura, coordenadax, coordenaday):
        self.__nome = nome
        self.__largura = largura
        self.__altura = altura
        self.__coordenadax = coordenadax
        self.__coordenaday = coordenaday

    @property
    def nome(self):
        return self.__nome

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura

    @property
    def coordenadax(self):
        return self.__coordenadax

    @property
    def coordenaday(self):
        return self.__coordenaday

    @abstractmethod
    def criar(self, coordenadax, coordenaday):
        pass
