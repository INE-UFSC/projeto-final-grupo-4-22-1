import time

from game.items.efeitosnoplayer import EfeitosNoJogador
from game.imageLibrary.ImageLibrary import ImageLibrary
from game.character.player.Player import Player
cinza = (124, 134, 153)
efeito = -1

image = ImageLibrary()
image_mushroom = image.mushroom

class Mushroom(EfeitosNoJogador):
    def __init__(self, coordenadax, coordenaday):
        super().__init__("mushroom", 15, 10, coordenadax, coordenaday, cinza, efeito)
        self.__efeito = efeito

    def aplicar_efeito(self, player):
        if player.envenenado == True:
            player.envenenado = False
        else:
            player.envenenado = True
        player.alterar_velocidade(self.__efeito)
