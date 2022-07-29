import time

from game.items.efeitosnoplayer import EfeitosNoJogador
from game.imageLibrary.ImageLibrary import ImageLibrary


class Apple(EfeitosNoJogador):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("apple", 20, 20, coordenadax,coordenaday, 2, ImageLibrary().apple)
        self.__efeito = 2
    
    def aplicar_efeito(self, player):
        player.alterar_velocidade(self.__efeito)

