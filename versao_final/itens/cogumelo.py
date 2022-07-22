from itens.efeitosnojogador import EfeitosNoJogador
from ImageLibrary import ImageLibrary
import time

cinza = (124, 134, 153)
efeito = -1

imagem = ImageLibrary()
imagem_cogumelo = imagem.cogumelo

class Cogumelo(EfeitosNoJogador):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("cogumelo", 15, 10,coordenadax,coordenaday, cinza, efeito)
        self.__efeito = efeito
        
        '''self.__imagem = ImageLibrary()
        self.__sprite = self.__imagem.espinho'''

    def aplicar_efeito(self, jogador):
        jogador.alterar_velocidade(self.__efeito)
