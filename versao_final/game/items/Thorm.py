import time

from game.items.efeitosnojogador import EfeitosNoJogador
from game.imageLibrary.ImageLibrary import ImageLibrary

marrom = (75, 54, 33)
efeito = 0

imagem = ImageLibrary()
imagem_thorm = imagem.thorm

class Thorm(EfeitosNoJogador):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("thorm", 15, 10, coordenadax, coordenaday, marrom, efeito)
        self.__efeito = efeito

        '''self.__imagem = ImageLibrary()
        self.__sprite = self.__imagem.thorm'''

    
    def aplicar_efeito(self, jogador):
        jogador.alterar_velocidade(self.__efeito)
