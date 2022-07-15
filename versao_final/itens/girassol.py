from itens.coletaveis import Coletaveis
from bibliotecaImagens import BibliotecaImagens
import random

amarelo = (255, 255, 0)

imagem = BibliotecaImagens()
imagem_girassol = imagem.girassol

class Girassol(Coletaveis):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("girassol", 20, 15,
                         coordenadax,coordenaday, 3, amarelo)
        
        '''self.__imagem = BibliotecaImagens()
        self.__sprite = self.__imagem.girassol'''
