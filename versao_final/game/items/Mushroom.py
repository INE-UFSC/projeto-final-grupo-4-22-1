from game.items.efeitosnoplayer import EfeitosNoJogador
from game.imageLibrary.ImageLibrary import ImageLibrary
from game.character.player.Player import Player

class Mushroom(EfeitosNoJogador):
    def __init__(self, coordenadax, coordenaday):
        super().__init__("mushroom", 20, 20, coordenadax, coordenaday, -1, ImageLibrary().mushroom)

    def aplicar_efeito(self, player):
        if player.envenenado == True:
            player.envenenado = False
        else:
            player.envenenado = True
        player.alterar_velocidade(self.__efeito)
