import os


class MapsLibrary:
    def __init__(self):
        fase_1 = os.path.join("game/maps/csv_files/mapa_facil.csv")
        fase_2 = os.path.join("game/maps/csv_files/mapa_dificil.csv")
        self.__mapas = [fase_1, fase_2]
    
    @property 
    def easy(self):
        return self.__easy

    @property 
    def medium(self):
        return self.__medium

    @property 
    def hard(self):
        return self.__hard

    @property
    def mapas(self):
        return self.__mapas
