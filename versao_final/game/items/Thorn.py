import time

from game.items.efeitosnojogador import EfeitosNoJogador
from game.imageLibrary.ImageLibrary import ImageLibrary
marrom = (75, 54, 33)
efeito = 0

imagem = ImageLibrary()
imagem_thorn = imagem.thorn

class Thorn(EfeitosNoJogador):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("thorm", 15, 10, coordenadax, coordenaday, marrom, efeito)
        self.__efeito = efeito

        '''self.__imagem = ImageLibrary()
        self.__sprite = self.__imagem.thorn'''

    
    def aplicar_efeito(self, jogador):
        jogador.alterar_velocidade(self.__efeito)
