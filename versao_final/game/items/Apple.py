import time

from game.items.efeitosnoplayer import EfeitosNoJogador
from game.imageLibrary.ImageLibrary import ImageLibrary

vermelho = (255, 0, 0)

class Apple(EfeitosNoJogador):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("apple", 15, 10, coordenadax,coordenaday, vermelho, 2)
        self.__efeito = 2

        '''self.__image = ImageLibrary()
        self.__sprite = self.__image.apple'''

    @property
    def sprite(self):
        return self.__sprite
    
    def aplicar_efeito(self, player):
        player.alterar_velocidade(self.__efeito)

