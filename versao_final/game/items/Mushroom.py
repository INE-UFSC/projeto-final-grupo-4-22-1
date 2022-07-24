import time

from game.items.efeitosnojogador import EfeitosNoJogador
from game.imageLibrary.ImageLibrary import ImageLibrary

cinza = (124, 134, 153)
efeito = -1

imagem = ImageLibrary()
imagem_mushroom = imagem.mushroom

class Mushroom(EfeitosNoJogador):
    def __init__(self, coordenadax, coordenaday):
        super().__init__("mushroom", 15, 10, coordenadax, coordenaday, cinza, efeito)
        self.__efeito = efeito

    def aplicar_efeito(self, jogador):
        jogador.alterar_velocidade(self.__efeito)
