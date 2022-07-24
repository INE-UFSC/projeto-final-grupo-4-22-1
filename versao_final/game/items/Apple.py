import time

from game.items.efeitosnojogador import EfeitosNoJogador
from game.imageLibrary.ImageLibrary import ImageLibrary

vermelho = (255, 0, 0)
efeito = 2

imagem = ImageLibrary()
imagem_apple = imagem.apple


class Apple(EfeitosNoJogador):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("apple", 15, 10, coordenadax,coordenaday, vermelho, efeito)
        self.__efeito = efeito 

        '''self.__imagem = ImageLibrary()
        self.__sprite = self.__imagem.apple'''
        
    
    @property
    def sprite(self):
        return self.__sprite
    
    def aplicar_efeito(self, jogador):
        jogador.alterar_velocidade(self.__efeito)
