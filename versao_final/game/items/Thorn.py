from game.items.efeitosnoplayer import EfeitosNoJogador
from game.imageLibrary.ImageLibrary import ImageLibrary
efeito = 0

class Thorn(EfeitosNoJogador):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("thorm", 20, 20, coordenadax, coordenaday, efeito, ImageLibrary().thorn)
        self.__efeito = efeito
    
    def aplicar_efeito(self, player):
        player.alterar_velocidade(self.__efeito)
        return "Perdeu!"

