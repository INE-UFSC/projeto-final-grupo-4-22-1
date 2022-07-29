class ConstrutorDeFases:
    def __init__(self, mapa):
        self.__mapa = mapa

    def gerar_fase(self, colisoes, nivel):
        try:
            self.__mapa.load_map(nivel)
            self.__mapa.spawn_all(colisoes, 2, 2, 2, 2)
        except IndexError:
            return "Finished!"
