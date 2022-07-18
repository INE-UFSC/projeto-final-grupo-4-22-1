from mapa import Mapa

class ConstrutorDeFases:
    def __init__(self, mapa):
        self.__mapa = mapa

    def gerar_fase(self, nivel):
        if nivel == 1:
            self.__mapa.load_map()
            self.__mapa.spawn_all(2, 5, 2, 5)
        if nivel == 2:
            self.__mapa.load_map()
            self.__mapa.spawn_all(5, 5, 5, 10)
