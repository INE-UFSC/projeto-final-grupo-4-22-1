from game.items.collectibles.Collectibles import Collectibles
from game.imageLibrary.ImageLibrary import ImageLibrary

rosa = (255, 0, 132)

image = ImageLibrary()
image_jasminen = image.jasminen

class Jasminen(Collectibles):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("jasminen", 15, 10,
                         coordenadax, coordenaday, 1, rosa)
        
        '''self.__image = ImageLibrary()
        self.__sprite = self.__image.jasminen'''
