import time

from game.items.efeitosnoplayer import EfeitosNoJogador
from game.imageLibrary.ImageLibrary import ImageLibrary
marrom = (75, 54, 33)
efeito = 0

image = ImageLibrary()
image_thorn = image.thorn

class Thorn(EfeitosNoJogador):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("thorm", 15, 10, coordenadax, coordenaday, marrom, efeito)
        self.__efeito = efeito

        '''self.__image = ImageLibrary()
        self.__sprite = self.__image.thorn'''

    
    def aplicar_efeito(self, player):
        player.alterar_velocidade(self.__efeito)
        return "Perdeu!"
