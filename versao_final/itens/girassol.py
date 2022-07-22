from itens.coletaveis import Coletaveis
from ImageLibrary import ImageLibrary
import random

amarelo = (255, 255, 0)

imagem = ImageLibrary()
imagem_girassol = imagem.girassol

class Girassol(Coletaveis):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("girassol", 20, 15,
                         coordenadax,coordenaday, 3, amarelo)
        
        '''self.__imagem = ImageLibrary()
        self.__sprite = self.__imagem.girassol'''
