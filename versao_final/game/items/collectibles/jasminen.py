from game.items.collectibles.Collectibles import Collectibles
from game.imageLibrary.ImageLibrary import ImageLibrary

class Jasminen(Collectibles):
    def __init__(self,coordenadax,coordenaday):
        super().__init__("jasminen", 20, 20,
                         coordenadax, coordenaday, 1, ImageLibrary().jasminen)
