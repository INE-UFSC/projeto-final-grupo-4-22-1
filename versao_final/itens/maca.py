from itens.efeitosnojogador import EfeitosNoJogador
from ImageLibrary import ImageLibrary
import time

vermelho = (255, 0, 0)
efeito = 2

imagem = ImageLibrary()
imagem_maca = imagem.maca


class Maca(EfeitosNoJogador):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("maca", 15, 10, coordenadax,coordenaday, vermelho, efeito)
        self.__efeito = efeito 

        '''self.__imagem = ImageLibrary()
        self.__sprite = self.__imagem.maca'''
        
    
    @property
    def sprite(self):
        return self.__sprite
    
    def aplicar_efeito(self, jogador):
        jogador.alterar_velocidade(self.__efeito)
