from itens.collectibles import Collectibles
from ImageLibrary import ImageLibrary
import random

# coordenadas aleatórias do sunflower
'''coordenadax_jasminen = random.randint(0, 1000) #TODO: restringir p/ terreno ground
coordenaday_jasminen = random.randint(0, 700) #TODO: restringir p/ terreno ground'''

rosa = (255, 0, 132)

imagem = ImageLibrary()
imagem_jasminen = imagem.jasminen

class Jasminen(Collectibles):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("jasminen", 15, 10,
                         coordenadax, coordenaday, 1, rosa)
        
        '''self.__imagem = ImageLibrary()
        self.__sprite = self.__imagem.jasminen'''
