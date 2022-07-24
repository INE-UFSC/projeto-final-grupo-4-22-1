from game.items.collectibles.Collectibles import Collectibles
from game.imageLibrary.ImageLibrary import ImageLibrary

rosa = (255, 0, 132)

imagem = ImageLibrary()
imagem_jasminen = imagem.jasminen

class Jasminen(Collectibles):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("jasminen", 15, 10,
                         coordenadax, coordenaday, 1, rosa)
        
        '''self.__imagem = ImageLibrary()
        self.__sprite = self.__imagem.jasminen'''
