from game.items.collectibles.Collectibles import Collectibles
from game.imageLibrary.ImageLibrary import ImageLibrary

class Sunflower(Collectibles):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("sunflower", 20, 15,
                         coordenadax,coordenaday, 2, ImageLibrary().sunflower)
