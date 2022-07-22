from itens.efeitosnojogador import EfeitosNoJogador
from ImageLibrary import ImageLibrary
import time


marrom = (75, 54, 33)
efeito = 0

imagem = ImageLibrary()
imagem_espinho = imagem.espinho

class Espinho(EfeitosNoJogador):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("espinho", 15, 10, coordenadax, coordenaday, marrom, efeito)
        self.__efeito = efeito

        '''self.__imagem = ImageLibrary()
        self.__sprite = self.__imagem.espinho'''

    
    def aplicar_efeito(self, jogador):
        jogador.alterar_velocidade(self.__efeito)
