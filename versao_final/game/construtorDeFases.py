class ConstrutorDeFases:
    def __init__(self, mapa):
        self.__mapa = mapa

    def gerar_fase(self, nivel):
        try:
            self.__mapa.load_map(nivel)
            self.__mapa.spawn_all(1, 1, 1, 1)
        except:
            return "Finished!"
