import os


class MapsLibrary:
    def __init__(self):
        self.__easy = os.path.join("game/maps/csv_files/mapa_facil.csv")
        self.__medium = os.path.join("game/maps/csv_files/mapa_medio.csv")
        self.__hard = os.path.join("game/maps/csv_files/mapa_dificil.csv")
        self.__mapas = [self.__easy, self.__medium, self.__hard]
    
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
