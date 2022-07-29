from game.items.collectibles.Collectibles import Collectibles
from game.imageLibrary.ImageLibrary import ImageLibrary

amarelo = (255, 255, 0)

image = ImageLibrary()
image_sunflower = image.sunflower

class Sunflower(Collectibles):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("sunflower", 20, 15,
                         coordenadax,coordenaday, 2, amarelo)
        
        '''self.__image = ImageLibrary()
        self.__sprite = self.__image.sunflower'''
