from itens.collectibles import Collectibles
from ImageLibrary import ImageLibrary
import random

amarelo = (255, 255, 0)

imagem = ImageLibrary()
imagem_sunflower = imagem.sunflower

class Sunflower(Collectibles):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("sunflower", 20, 15,
                         coordenadax,coordenaday, 3, amarelo)
        
        '''self.__imagem = ImageLibrary()
        self.__sprite = self.__imagem.sunflower'''
